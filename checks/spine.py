#!/usr/bin/env python3
"""The contents page and the authoring spine must agree. HARD FAIL.

Exists because the same failure happened three times: a decision was recorded in
CONTEXT.md and the public page kept the superseded wording. Chapter 04's
description survived two rounds of correction that way, and the Part III heading
kept "and when" after the tense chapter had left the Part.

Checks what can be checked mechanically:
  * the five Part names match, case-insensitively
  * each Part holds the number of chapters its spine table declares
  * chapter numbers are 01..14, contiguous, in both files

It cannot check that a chapter's DESCRIPTION still reflects its spine row — that
needs a human. But a Part that drifts is now caught, and a chapter that moves
between Parts cannot go unnoticed.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
problems = []

ctx = (ROOT / "CONTEXT.md").read_text(encoding="utf-8")
idx = (ROOT / "docs" / "index.html").read_text(encoding="utf-8")

spine = re.findall(r"^### PART [IVX]+ — (.+?) \((\d+)\)\s*$", ctx, flags=re.M)
# The Part divisions are <h2 class="part-head">; they were <p> until the
# accessibility pass, since they divide the contents page and belong in the
# heading outline. Matched on the CLASS rather than the tag so the next change of
# element does not silently reduce this check to zero Parts — which is exactly what
# happened when they became headings.
page = re.findall(r'<[a-z0-9]+ class="part-head">Part [IVX]+ · (.+?)</[a-z0-9]+>', idx)
page_counts = [len(re.findall(r'<span class="n">\d\d</span>', block))
               for block in re.split(r'<[a-z0-9]+ class="part-head">', idx)[1:]]

if len(spine) != len(page):
    problems.append(f"Part count differs: CONTEXT.md has {len(spine)}, index.html has {len(page)}")
else:
    for i, ((sname, scount), pname, pcount) in enumerate(zip(spine, page, page_counts), 1):
        sn = re.sub(r"\s+", " ", sname).strip().lower()
        pn = re.sub(r"<[^>]+>", "", pname)
        pn = re.sub(r"\s+", " ", pn).strip().lower()
        if sn != pn:
            problems.append(f"Part {i} name differs:\n"
                            f"      CONTEXT.md: {sname}\n"
                            f"      index.html: {pn}")
        if int(scount) != pcount:
            problems.append(f"Part {i} ({sname}): spine declares {scount} chapters, "
                            f"contents page lists {pcount}")

nums = re.findall(r'<span class="n">(\d\d)</span>', idx)
expected = [f"{i:02d}" for i in range(1, len(nums) + 1)]
if nums != expected:
    problems.append(f"contents page chapter numbers are not contiguous: {' '.join(nums)}")

# Scan for spine rows ONLY inside the "### PART …" sections.
#
# This used to scan the whole of CONTEXT.md for "| NN | slug |", which quietly
# assumed no other table in the file would ever have a two-digit first column and
# a single-token second one. A measurement table added under Editorial gates —
# "| 01 | 1457 | 557 |" — matched it immediately and the check failed with five
# phantom chapters. The row pattern was never the right anchor: the spine is a
# location in the document, not a shape of row, so ask for the location.
part_blocks = []
for m in re.finditer(r"^### PART [IVX]+ — .*$", ctx, flags=re.M):
    nxt = re.search(r"^#{1,3} ", ctx[m.end():], flags=re.M)
    part_blocks.append(ctx[m.end(): m.end() + nxt.start() if nxt else len(ctx)])

ctx_nums = re.findall(r"^\| (\d\d) \| [a-z0-9-]+ \|", "\n".join(part_blocks), flags=re.M)
if ctx_nums != nums:
    problems.append(f"spine table numbers {' '.join(ctx_nums)} != contents page {' '.join(nums)}")

if problems:
    for p in problems:
        print(f"  FAIL {p}")
    sys.exit(1)
print(f"  {len(spine)} Parts, {len(nums)} chapters: spine and contents page agree")
