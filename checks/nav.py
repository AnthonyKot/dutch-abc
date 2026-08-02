#!/usr/bin/env python3
"""Chapter prev/next links agree with the contents page. HARD FAIL.

WHY THIS EXISTS, AND THE UNCOMFORTABLE PART.

verify.sh's own header has listed "prev/next contiguity" among the checks ported
from the previous books since the first commit, and README describes the nav as
"generated prev/next — derived from the chapter files, never hand-maintained".
Neither was true. There was no such check, the nav is hand-written in every
chapter, and the documentation asserting otherwise is what stopped anyone looking.

It caught a live defect immediately: chapter 07 linked forward to
"08 · dient u, gelieve", a chapter title that appears nowhere in the spine or on
the contents page. The real chapter 08 is "Moeten, dienen, hoeven". A reader
following that link would have been told the name of a chapter that does not
exist.

This is the project's recurring bug class for the fifth time — a fact copied into
prose with nothing tying the copy to the original — and the fix is the same as
spine.py, status.py and stats.py: recompute it and compare.

WHAT THIS CHECKS
  * chapter files are numbered contiguously from 01
  * each chapter's prev link targets the file immediately before it, and its next
    link the file immediately after; chapter 01's prev and the last chapter's next
    both go to the contents page
  * the chapter TITLE quoted in a nav link matches that chapter's title on the
    contents page
  * a nav entry is marked "(not yet written)" exactly when the file is absent

WHAT IT DOES NOT CHECK: that the titles are good, or that the contents page
describes the chapter accurately. Those are editorial.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
INDEX = ROOT / "docs" / "index.html"
CHAPTERS = sorted((ROOT / "docs" / "chapters").glob("*.html"))

problems = []


def plain(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s)).strip()


def contents_titles():
    """{'07': 'daarbij, hiervan, waarop'} from the contents page."""
    idx = INDEX.read_text(encoding="utf-8")
    out = {}
    for m in re.finditer(r'<span class="n">(\d\d)</span>(.*?)<span class="adds">',
                         idx, flags=re.S):
        out[m.group(1)] = plain(m.group(2))
    return out


def nav_links(text):
    """[(kind, href, number, title, stubbed)] for the chapter-nav block."""
    m = re.search(r'<nav class="chapter-nav">(.*?)</nav>', text, flags=re.S)
    if not m:
        return None
    links = []
    for a in re.finditer(r'<a\s+([^>]*)>(.*?)</a>', m.group(1), flags=re.S):
        attrs, body = a.group(1), a.group(2)
        href = re.search(r'href="([^"]+)"', attrs)
        kind = "next" if 'class="next"' in attrs else "prev"
        stub = "not yet written" in body
        body = re.sub(r"<em>\(not yet written\)</em>", "", body)
        label = plain(re.sub(r'<span class="dir">.*?</span>', "", body, flags=re.S))
        num = re.match(r"(\d\d)\s*·\s*(.*)", label)
        links.append((kind, href.group(1) if href else "",
                      num.group(1) if num else None,
                      num.group(2).strip() if num else label, stub))
    return links


def main():
    if not CHAPTERS:
        print("  no chapters yet — nothing to check")
        return 0

    nums = [c.name[:2] for c in CHAPTERS]
    if nums != [f"{i:02d}" for i in range(1, len(nums) + 1)]:
        problems.append(f"chapter files are not contiguous from 01: {' '.join(nums)}")

    titles = contents_titles()
    by_num = {c.name[:2]: c for c in CHAPTERS}

    for i, path in enumerate(CHAPTERS):
        n = path.name[:2]
        links = nav_links(path.read_text(encoding="utf-8"))
        if links is None:
            problems.append(f"{path.name}  no <nav class=\"chapter-nav\">")
            continue
        got = {k: v for k, *v in [(k, h, num, t, s) for k, h, num, t, s in links]}

        for kind, delta in (("prev", -1), ("next", +1)):
            if kind not in got:
                problems.append(f"{path.name}  no {kind} link")
                continue
            href, num, title, stub = got[kind]
            want_num = f"{int(n) + delta:02d}"
            exists = want_num in by_num
            target_exists = 1 <= int(n) + delta <= len(titles)

            if not target_exists:
                if href != "../index.html":
                    problems.append(f"{path.name}  {kind} link should go to the contents "
                                    f"page, goes to {href}")
                continue

            if exists:
                want_href = by_num[want_num].name
                if href != want_href:
                    problems.append(f"{path.name}  {kind} link points at {href}, "
                                    f"expected {want_href}")
                if stub:
                    problems.append(f"{path.name}  {kind} link is marked "
                                    f"\"(not yet written)\" but {want_num} exists")
            else:
                if href != "../index.html":
                    problems.append(f"{path.name}  {kind} link points at {href}, but "
                                    f"chapter {want_num} is not written; it must go to "
                                    f"the contents page")
                if not stub:
                    problems.append(f"{path.name}  {kind} link to unwritten chapter "
                                    f"{want_num} is not marked \"(not yet written)\"")

            if num != want_num:
                problems.append(f"{path.name}  {kind} link is labelled chapter "
                                f"{num}, expected {want_num}")
            elif titles.get(want_num, "").lower() != title.lower():
                problems.append(f"{path.name}  {kind} link calls chapter {want_num} "
                                f"'{title}'; the contents page calls it "
                                f"'{titles.get(want_num)}'")

    if problems:
        for p in problems:
            print(f"  FAIL {p}")
        return 1
    print(f"  {len(CHAPTERS)} chapters: prev/next links contiguous and titled as the "
          f"contents page titles them")
    return 0


if __name__ == "__main__":
    sys.exit(main())
