#!/usr/bin/env python3
"""Draft status agrees with the files on disk, everywhere it is stated. HARD FAIL.

WHY THIS EXISTS. Three times now a fact has been fixed in one file and left stale
in another: the spine restructure updated the contents page and not README.md;
chapter 04's description survived two correction rounds because the fixes landed
in CONTEXT.md; and chapter 02 shipped with docs/about.html and README.md both
still saying only chapter 01 was written. checks/spine.py closed the first case.
This closes the second, which is the same bug wearing different clothes: a
human-readable claim about the book's state, duplicated across files, with
nothing tying it to the state.

THE CONTRACT. The set of written chapters is a fact about the filesystem, so it
is computed here and never typed. Every file listed in FILES must contain the
resulting sentence verbatim (whitespace-insensitive, because HTML wraps). Add a
chapter and all three files fail until they are updated — which is the point.

The sentence is deliberately ordinary prose rather than a hidden marker or an
HTML comment. A marker can rot invisibly while the prose beside it lies; a
sentence that has to read naturally in three different documents cannot.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
FILES = ["docs/index.html", "docs/about.html", "README.md"]


def written():
    """Chapter numbers with a file on disk, as zero-padded strings."""
    out = []
    for p in sorted((ROOT / "docs" / "chapters").glob("*.html")):
        m = re.match(r"(\d{2})-", p.name)
        if m:
            out.append(m.group(1))
    return out


def sentence(nums):
    """The one canonical phrasing. Range form only when the run is contiguous."""
    if not nums:
        return "No chapters are written yet"
    if len(nums) == 1:
        return f"Chapter {nums[0]} is written"
    if len(nums) == 2:
        return f"Chapters {nums[0]} and {nums[1]} are written"
    contiguous = all(int(b) - int(a) == 1 for a, b in zip(nums, nums[1:]))
    if contiguous:
        return f"Chapters {nums[0]}–{nums[-1]} are written"
    return f"Chapters {', '.join(nums[:-1])} and {nums[-1]} are written"


def main():
    nums = written()
    want = sentence(nums)
    missing = []
    for rel in FILES:
        fn = ROOT / rel
        if not fn.exists():
            missing.append(f"{rel} — file not found")
            continue
        # HTML wraps mid-sentence, so compare on collapsed whitespace.
        hay = re.sub(r"\s+", " ", fn.read_text(encoding="utf-8"))
        if want not in hay:
            missing.append(f"{rel} — does not contain {want!r}")

    if missing:
        print(f"  {len(nums)} chapter file(s) on disk, so every status claim must read: {want!r}")
        for m in missing:
            print(f"  FAIL {m}")
        return 1

    print(f"  draft status consistent across {len(FILES)} files: {want.lower()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
