#!/usr/bin/env python3
"""Report vocabulary growth. ADVISORY — never fails the build.

Deliberate decision, recorded in CONTEXT.md: a hard lexical gate would make the
Dutch stilted, and this book is judged on whether it is worth reading. So this
reports and the author reads it.

Two numbers per chapter and one list:
  * new words introduced, and the running total
  * any word used in a chapter earlier than the one that introduces it

The second is the forward-reference check that made No Such Form readable. It is
the thing to actually look at.
"""
import html
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
LEXICON = ROOT / "data" / "lexicon.json"
CHAPTERS = sorted((ROOT / "chapters").glob("*.html"))

WORD = re.compile(r"[a-zà-ÿ]+(?:['’][a-zà-ÿ]+)?", re.I)


def dutch_text(text):
    out = []
    for m in re.finditer(
        r'<(?:span|p|div)[^>]*class="[^"]*\bnl\b[^"]*"[^>]*>(.*?)</(?:span|p|div)>',
        text, flags=re.S,
    ):
        out.append(html.unescape(re.sub(r"<[^>]+>", "", m.group(1))))
    return " ".join(out)


def main():
    if not CHAPTERS:
        print("  no chapters yet — nothing to report")
        return 0

    introduced = {}
    seen = set()
    print(f"  {'chapter':<34} {'new':>5} {'total':>6}")
    for fn in CHAPTERS:
        words = {w.lower() for w in WORD.findall(dutch_text(fn.read_text(encoding="utf-8")))}
        new = words - seen
        seen |= words
        for w in new:
            introduced[w] = fn.name
        print(f"  {fn.name:<34} {len(new):>5} {len(seen):>6}")

    # Gender coverage: how much of the corpus checks/forms.py can actually check.
    if LEXICON.exists():
        nouns = json.loads(LEXICON.read_text(encoding="utf-8")).get("nouns", {})
        known = len(seen & set(nouns))
        print(f"\n  lexicon covers {known} of {len(seen)} distinct words "
              f"({100 * known // max(len(seen), 1)}%) — forms.py can only check these")

    print("\n  (advisory: no failures are raised from this script)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
