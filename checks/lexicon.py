#!/usr/bin/env python3
"""Report vocabulary growth. ADVISORY — never fails the build.

Deliberate decision, recorded in CONTEXT.md: a hard lexical gate would make the
Dutch stilted, and this book is judged on whether it is worth reading. So this
reports and the author reads it.

  * new words per chapter, and the running total
  * how much of the corpus data/lexicon.json can actually vouch for

NOT a forward-reference check, and it never was one. The first version claimed to
report "any word used before the chapter that introduces it", built the data, and
then never printed it — and the check was incoherent anyway, because it defined a
word's introduction as its first occurrence, so by construction nothing could ever
precede it. A real version needs explicit introduced_in metadata. Until that
exists, this script does not pretend to provide it.
"""
import html
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from corpus import dutch_spans  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
LEXICON = ROOT / "data" / "lexicon.json"
CHAPTERS = sorted((ROOT / "docs" / "chapters").glob("*.html"))

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

    seen = set()
    print(f"  {'chapter':<34} {'new':>5} {'total':>6}")
    for fn in CHAPTERS:
        words = {w.lower() for w in WORD.findall(dutch_text(fn.read_text(encoding="utf-8")))}
        new = words - seen
        seen |= words
        print(f"  {fn.name:<34} {len(new):>5} {len(seen):>6}")

    # Gender coverage.
    #
    # This used to report lexicon-hits over ALL distinct Dutch words, which was a
    # meaningless denominator and actively misleading: most words in a chapter are
    # verbs, adverbs and function words that a gender register can never cover, so
    # the figure was pinned near 15% and barely moved when the lexicon went from 50
    # entries to 1000. The number that means something is how many of the nouns the
    # chapters ACTUALLY USE WITH AN ARTICLE the checker can vouch for — because that
    # is exactly the set checks/forms.py is able to fail on.
    if LEXICON.exists():
        nouns = json.loads(LEXICON.read_text(encoding="utf-8")).get("nouns", {})
        plurals = {v["plural"].lower() for v in nouns.values()
                   if isinstance(v, dict) and v.get("plural")}
        used, unchecked = set(), set()
        for fn in CHAPTERS:
            for _, span in dutch_spans(fn.read_text(encoding="utf-8")):
                for noun in re.findall(r"\b(?:de|het)\s+([a-zà-ÿ]+)\b", span, flags=re.I):
                    n = noun.lower()
                    used.add(n)
                    if n not in nouns and n not in plurals:
                        unchecked.add(n)
        checked = len(used) - len(unchecked)
        print(f"\n  lexicon: {len(nouns)} nouns")
        print(f"  nouns used with an article in the chapters: {len(used)}; "
              f"forms.py can check {checked}, cannot check {len(unchecked)}")
        if unchecked:
            print(f"    unchecked: {', '.join(sorted(unchecked))}")
            print("    (the pattern cannot tell article 'het' from pronoun 'het', and it "
                  "picks up\n     the adjective in 'het ingevulde formulier' — see forms.py)")

    print("\n  (advisory: no failures are raised from this script)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
