#!/usr/bin/env python3
"""Statistics quoted in the chapters match the data they were computed from. HARD FAIL.

Chapter 05 makes measured claims — how many nouns the register holds, how many
are de, how many words end in -je, which words are the exceptions. Those numbers
came from data/lexicon.json, and the moment a noun is added they are wrong on a
published page with nothing to say so.

This is the same bug as checks/spine.py and checks/status.py: a fact duplicated
into prose with nothing tying the copy to the original. It has caused a defect
three times in this project, and it caught two more here — adding six nouns for
chapter 05's own examples moved the total from 1033 to 1039 while the drafted
page still said 1036, and an external review found a stale "72%" surviving in the
kaart after the body had been corrected to 73%.

WHY THE CHAPTER QUOTES COUNTS AND NOT PERCENTAGES. That second failure exposed
something worse than staleness. Adding a single noun — 'feit' — moved the de
share from 73% back to 72%, because the ratio sits almost exactly on the rounding
boundary. A published figure that flips when one word is added is not a claim
worth printing, however diligently it is synchronised. The chapter now states
exact integers, which are stable in character as well as checkable, and says
"a little over seven in ten" for the shape of it.

So this check enforces two things: every computed integer appears in the text,
and NO bare percentage does. The second half exists so that a later pass cannot
quietly reintroduce a brittle figure.
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

    # Only the WORD LIST counts, and that is what the chapter claims.
    #
    # Chapter 05 says "across the A2 word list this book checks its examples against
    # — 1044 nouns". That sentence is about a register with a provenance: the 50
    # hand-seeded entries (no "src") and the bulk transcription from De Opmaat's
    # woordenlijst ("src": "opmaat"). Everything else in data/lexicon.json was added
    # later for a different reason — to make one chapter's example machine-checkable
    # — and is not an observation about A2 vocabulary at all.
    #
    # This is an allowlist rather than a denylist on purpose: a provenance tag
    # invented next month is excluded by default instead of silently entering a
    # published figure. Two tags have needed it so far, "compound-head" (gender
    # deduced from an entry already present) and "chapter-example" (an ordinary noun
    # a chapter used with an article).
    #
    # Found the moment it mattered: adding one derived compound for chapter 05's own
    # article-agreement exercise moved four published integers at once, and the
    # honest correction was the denominator, not the prose.
    IN_REGISTER = (None, "opmaat")
    nouns = {w: e for w, e in nouns.items() if e.get("src") in IN_REGISTER}
    text = re.sub(r"\s+", " ", CHAPTER.read_text(encoding="utf-8"))
    # Figures must be in prose, not in attributes. Tags become a SPACE, not nothing:
    # stripping "<td>36</td><td>36 het</td>" to "" yields "3636 het" and no \b36\b.
    stripped = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", text))

    g = collections.Counter("both" if isinstance(e["gender"], list) else e["gender"]
                            for e in nouns.values())
    total = sum(g.values())
    want = [(total, f"lexicon total ({total})"),
            (g["de"], f"de count ({g['de']})"),
            (g["het"], f"het count ({g['het']})")]
    names = []

    for suf in SUFFIXES:
        sub = {w: e["gender"] for w, e in nouns.items()
               if w.endswith(suf) and len(w) > len(suf) + 2
               and not isinstance(e["gender"], list)}
        if not sub:
            continue
        top, n = collections.Counter(sub.values()).most_common(1)[0]
        want.append((len(sub), f"-{suf} total ({len(sub)})"))
        want.append((n, f"-{suf} conforming ({n})"))
        names += [(w, f"-{suf} exception '{w}' must be named")
                  for w, gender in sub.items() if gender != top]

    problems = [why for value, why in want if not re.search(rf"\b{value}\b", stripped)]
    problems += [why for name, why in names if name not in stripped]

    # No bare percentages: see the module docstring. Rounded shares are unstable.
    for pct in set(re.findall(r"\b(\d{1,3})%", stripped)):
        problems.append(f"percentage '{pct}%' in the chapter — quote exact counts instead, "
                        f"a rounded share flips when one noun is added")

    if problems:
        print("  chapter 05's figures do not agree with data/lexicon.json:")
        for p in problems:
            print(f"  FAIL {p}")
        return 1

    print(f"  chapter 05: {len(want)} counts and {len(names)} named exceptions all agree with the "
          f"lexicon ({total} nouns); no unstable percentages")
    return 0


if __name__ == "__main__":
    sys.exit(main())
