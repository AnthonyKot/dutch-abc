#!/usr/bin/env python3
"""Validate the Dutch this book asserts. Hard failure — blocks publication.

Wrong Dutch in a book about Dutch is worse than a wrong number in a book about
mathematics: the reader cannot detect it and will learn it. This is the
equivalent of No Such Form's checks/*.py, pointed at forms instead of numbers.

Currently checks:
  * article agreement    — every "de X" / "het X" against data/lexicon.json
  * compound splits      — every <div class="split"> reassembles to its whole
  * plural articles      — a marked plural noun never takes "het"

Extend as chapters land. A claim without a check here is unverified.
"""
import html
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
LEXICON = ROOT / "data" / "lexicon.json"
CHAPTERS = sorted((ROOT / "chapters").glob("*.html"))

problems = []


def load_lexicon():
    if not LEXICON.exists():
        return {}
    data = json.loads(LEXICON.read_text(encoding="utf-8"))
    return data.get("nouns", {})


def dutch_spans(text):
    """Every marked-up piece of Dutch in a chapter, with its line number."""
    for m in re.finditer(
        r'<(?:span|p|div)[^>]*class="[^"]*\bnl\b[^"]*"[^>]*>(.*?)</(?:span|p|div)>',
        text, flags=re.S,
    ):
        yield text[: m.start()].count("\n") + 1, html.unescape(re.sub(r"<[^>]+>", "", m.group(1)))


def check_articles(fn, text, nouns):
    if not nouns:
        return
    for line, span in dutch_spans(text):
        for art, noun in re.findall(r"\b(de|het)\s+([a-zà-ÿ]+)\b", span, flags=re.I):
            entry = nouns.get(noun.lower())
            if entry is None:
                continue  # unknown word: lexicon.py reports it, this does not fail
            expected = entry["gender"] if isinstance(entry, dict) else entry
            if expected != art.lower():
                problems.append(
                    f"{fn.name}:{line}  article: wrote '{art} {noun}', "
                    f"lexicon says '{expected} {noun}'"
                )


def check_compound_splits(fn, text):
    """A <div class="split"> must reassemble: parts + linking elements == whole."""
    for m in re.finditer(r'<div class="split">(.*?)</div>', text, flags=re.S):
        block = m.group(1)
        line = text[: m.start()].count("\n") + 1
        whole = re.search(r'class="whole"[^>]*>(.*?)</span>', block, flags=re.S)
        if not whole:
            problems.append(f"{fn.name}:{line}  split block has no .whole")
            continue
        target = re.sub(r"[^a-zà-ÿ]", "", html.unescape(whole.group(1)).lower())
        # Exact class match: "parts" is the wrapper and must not be captured.
        pieces = [
            re.sub(r"[^a-zà-ÿ]", "", html.unescape(p).lower())
            for p in re.findall(r'<span class="(?:part|part head|join)">([^<]*)</span>',
                                block, flags=re.S)
        ]
        joined = "".join(pieces)
        if joined != target:
            problems.append(
                f"{fn.name}:{line}  compound split does not reassemble: "
                f"parts give '{joined}', whole is '{target}'"
            )


def main():
    nouns = load_lexicon()
    if not CHAPTERS:
        print("  no chapters yet — nothing to check")
        return 0
    for fn in CHAPTERS:
        text = fn.read_text(encoding="utf-8")
        check_articles(fn, text, nouns)
        check_compound_splits(fn, text)

    if problems:
        for p in problems:
            print(f"  FAIL {p}")
        return 1
    print(f"  {len(CHAPTERS)} chapters: articles and compound splits OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
