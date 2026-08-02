#!/usr/bin/env python3
"""Statistics quoted in the chapters match the data they were computed from. HARD FAIL.

Chapter 05 makes measured claims — how many nouns the register holds, what share
are de, how many words end in -je, which words are the exceptions. Those numbers
came from data/lexicon.json, and the moment a noun is added they are wrong on a
published page with nothing to say so.

This is the same bug as checks/spine.py and checks/status.py: a fact duplicated
into prose, with nothing tying the copy to the original. It has now caused a
defect three times in this project, and it caused one here — adding six nouns for
chapter 05's own examples moved the total from 1033 to 1039 and the de share from
72% to 73% while the drafted page still said 1036 and 72%.

Rather than assert the numbers here (which would just move the duplication), the
values are RECOMPUTED from the lexicon and each must appear in the chapter text.
"""
import collections
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
LEXICON = ROOT / "data" / "lexicon.json"
CHAPTER = ROOT / "docs" / "chapters" / "05-de-het-die-dat.html"

SUFFIXES = ["je", "ing", "tie", "teit", "um", "ij"]


def main():
    if not CHAPTER.exists() or not LEXICON.exists():
        print("  chapter 05 or lexicon absent — nothing to check")
        return 0

    nouns = json.loads(LEXICON.read_text(encoding="utf-8"))["nouns"]
    text = re.sub(r"\s+", " ", CHAPTER.read_text(encoding="utf-8"))

    g = collections.Counter("both" if isinstance(e["gender"], list) else e["gender"]
                            for e in nouns.values())
    total = sum(g.values())
    want = [(str(total), f"lexicon total ({total} nouns)"),
            (f"{round(100 * g['de'] / total)}%", "de share"),
            (f"{round(100 * g['het'] / total)}%", "het share")]

    for suf in SUFFIXES:
        sub = {w: e["gender"] for w, e in nouns.items()
               if w.endswith(suf) and len(w) > len(suf) + 2
               and not isinstance(e["gender"], list)}
        if not sub:
            continue
        top, n = collections.Counter(sub.values()).most_common(1)[0]
        want.append((str(len(sub)), f"-{suf} count ({len(sub)})"))
        for w, gender in sub.items():
            if gender != top:                      # a named exception must be named
                want.append((w, f"-{suf} exception '{w}'"))

    missing = [why for value, why in want if value not in text]
    if missing:
        print(f"  chapter 05 quotes figures that no longer match data/lexicon.json:")
        for m in missing:
            print(f"  FAIL {m} — recomputed value is absent from the chapter")
        return 1

    print(f"  chapter 05's {len(want)} quoted figures all agree with the lexicon "
          f"({total} nouns, {round(100 * g['de'] / total)}% de)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
