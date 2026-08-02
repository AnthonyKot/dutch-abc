#!/usr/bin/env python3
"""Every chapter carries the full teaching apparatus. HARD FAIL.

WHY THIS IS A GATE AND THE KAART LEDGER IS NOT. CONTEXT.md records a deliberate
decision that the kaart is advisory, on the grounds that a hard lexical gate would
make the Dutch stilted. That reasoning is about CONTENT — which words a chapter is
allowed to use. It does not extend to STRUCTURE. A chapter that ships without a
self-check block is not a chapter with slightly awkward Dutch; it is a chapter that
teaches a procedure and gives the reader no way to find out whether they applied it
correctly, which is the specific failure this apparatus exists to prevent.

WHAT THIS CHECKS, per chapter:
  * one .recall at the top (chapter 02 on), naming exactly the previous chapter,
    and placed BEFORE the .device box — a retrieval prompt after the restatement
    is not retrieval
  * one details.worked inside step 3 — the reader attempts before the answer shows
  * one .check inside step 3, with at least one li.hard in it
  * one .undecided inside step 3 — the case the procedure cannot settle
  * step 4 points back at step 3's tests rather than restating them
  * every kaart terug entry is a details with a question and an answer, and every
    chapter it cites is strictly EARLIER than this one — including multi-cites of
    the form (ch. 01, 05), which the first version of this check silently ignored

WHAT IT DOES NOT CHECK: whether the retrieval question is a good one, whether the
self-check criteria are correct, or whether the undecidable case is genuinely
undecidable. Those are editorial and they are where the real work is. This check
only guarantees the slots are filled, which is the part a later pass can silently
undo while tidying.
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from corpus import chapters  # noqa: E402

problems = []
# Single cite: (ch. 01). Multi-cite: (ch. 01, 05) or (ch. 08, 09, 10).
# The old regex only matched the single form, so multi-cites were silently
# unchecked for the backwards-only rule — the hole that let a forward cite
# hide as (ch. 12, 14) with nothing failing.
KREF_BLOCK = re.compile(r"\(ch\.\s*([\d,\s]+)\)")


def chapter_cites(text):
    """Every chapter number mentioned in (ch. …) forms, single or multi."""
    cites = []
    for m in KREF_BLOCK.finditer(text):
        for part in m.group(1).split(","):
            part = part.strip()
            if part.isdigit():
                cites.append(int(part))
    return cites


def chapter_number(fn):
    return int(fn.name[:2])


def block(text, cls, tag="div"):
    """Positions of every <tag class="...cls..."> in the file."""
    return [m.start() for m in
            re.finditer(rf'<{tag} class="[^"]*\b{cls}\b[^"]*"', text)]


def terug_column(text):
    m = re.search(r'<div class="col terug">(.*?)</div>\s*<div class="col',
                  text, flags=re.S)
    return m.group(1) if m else None


def check_chapter(fn):
    text = fn.read_text(encoding="utf-8")
    n = chapter_number(fn)
    name = fn.name

    steps = [m.start() for m in re.finditer(r'<section class="step">', text)]
    if len(steps) != 4:
        problems.append(f"{name}  expected 4 step sections, found {len(steps)}")
        return
    step3, step4 = steps[2], steps[3]

    def inside_step3(positions, what):
        if not positions:
            problems.append(f"{name}  no {what}")
            return None
        hit = [p for p in positions if step3 < p < step4]
        if not hit:
            problems.append(f"{name}  {what} exists but is not inside step 3 "
                            f"(it must sit with the worked example, not elsewhere)")
            return None
        if len(hit) > 1:
            problems.append(f"{name}  {len(hit)} {what} blocks in step 3; expected one")
        return hit[0]

    # ---- the opening retrieval prompt -------------------------------------
    recall = block(text, "recall", tag="section")
    if n == 1:
        if recall:
            problems.append(f"{name}  chapter 01 has a .recall — there is nothing behind it "
                            f"to retrieve")
    elif not recall:
        problems.append(f"{name}  no .recall block; every chapter from 02 opens with one "
                        f"retrieval prompt from the chapter before")
    else:
        device = block(text, "device")
        if device and recall[0] > device[0]:
            problems.append(f"{name}  .recall sits after the .device box. A prompt asked once "
                            f"the rule has been restated is a quiz, not retrieval")
        head = text[recall[0]:recall[0] + 1200]
        cited = chapter_cites(head)
        if not cited:
            problems.append(f"{name}  .recall names no chapter; it must carry (ch. NN)")
        elif cited[0] != n - 1:
            problems.append(f"{name}  .recall cites ch. {cited[0]}, expected ch. {n - 1:02d} "
                            f"— the prompt is meant to reach back exactly one chapter")
        if len(cited) > 1:
            problems.append(f"{name}  .recall cites more than one chapter {cited}; the opening "
                            f"prompt reaches back exactly one chapter (kaart terug covers the rest)")
        if "<details" not in head:
            problems.append(f"{name}  .recall reveals its answer immediately; it must be "
                            f"behind a <details> so the reader attempts first")

    # ---- attempt before reveal, self-check, undecidable case --------------
    worked = [m.start() for m in re.finditer(r'<details class="worked"', text)]
    if not [p for p in worked if step3 < p < step4]:
        problems.append(f"{name}  no <details class=\"worked\"> in step 3; the worked answers "
                        f"must be hidden until the reader has attempted them")

    chk = inside_step3(block(text, "check"), ".check block")
    if chk is not None:
        body = text[chk:step4]
        if 'class="hard"' not in body:
            problems.append(f"{name}  .check has no li.hard — at least one test must be able "
                            f"to prove the reader wrong outright")
        if body.count("<li") < 3:
            problems.append(f"{name}  .check lists fewer than three tests")

    inside_step3(block(text, "undecided"), ".undecided block")

    # ---- step 4 reuses step 3's tests rather than restating them ----------
    tail = text[step4:]
    if not re.search(r"(same|these)[^.<]{0,40}tests? from step 3", tail):
        problems.append(f"{name}  step 4 does not send the reader back to step 3's tests; "
                        f"the self-check must be run again on their own document")

    # ---- the kaart's terug column is retrieval, not restatement ----------
    col = terug_column(text)
    if col is None:
        problems.append(f"{name}  kaart has no terug column")
        return
    if n == 1:
        return                      # chapter 01 legitimately has nothing behind it
    items = re.findall(r"<li>(.*?)</li>", col, flags=re.S)
    if not items:
        problems.append(f"{name}  terug column has no entries")
    for i, item in enumerate(items, 1):
        if "<details" not in item or "<summary" not in item:
            problems.append(f"{name}  terug entry {i} is a statement, not a question. "
                            f"Wrap it in <details><summary>question</summary><p>answer</p>")
            continue
        summary = re.search(r"<summary>(.*?)</summary>", item, flags=re.S)
        if not summary or "?" not in summary.group(1):
            problems.append(f"{name}  terug entry {i} has a summary that does not ask anything")
        after = item[summary.end():] if summary else ""
        if "<p>" not in after:
            problems.append(f"{name}  terug entry {i} hides no answer behind its question")
        for cited in chapter_cites(item):
            if cited >= n:
                problems.append(f"{name}  terug entry {i} cites ch. {cited}, which is not "
                                f"earlier than {n:02d}. The terug column looks backwards only")


def main():
    ch = chapters()
    if not ch:
        print("  no chapters yet — nothing to check")
        return 0
    for fn in ch:
        check_chapter(fn)
    if problems:
        for p in problems:
            print(f"  FAIL {p}")
        return 1
    print(f"  {len(ch)} chapters: recall, worked reveal, self-check, undecidable case and "
          f"retrieval kaart all present")
    return 0


if __name__ == "__main__":
    sys.exit(main())
