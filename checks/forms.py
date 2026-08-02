#!/usr/bin/env python3
"""Validate the Dutch this book asserts. HARD FAIL.

Wrong Dutch in a book about Dutch is worse than a wrong number in a book about
mathematics: the reader cannot detect it and will learn it.

WHAT THIS CHECKS — and the public pages must not claim more:
  * article agreement, singular AND plural, against data/lexicon.json
  * compound splits reassemble to the whole, with at least two real constituents

WHAT IT DOES NOT CHECK: inflection, tense formation, word order, idiom, or
whether a sentence is natural. It is a narrow net, not a proof.

KNOWN NOISE IN THE UNKNOWN-NOUN NOTE, so nobody "fixes" a non-bug: the article
pattern cannot tell the article 'het' from the pronoun 'het'. "Het is niet
nodig" and "stuur het vóór 1 juni" therefore report 'is' and 'vóór' as unchecked
nouns. They are not nouns and nothing is wrong with the Dutch. Resist adding a
function-word stoplist for this — the words that can follow pronoun 'het' are
most of the language, and the note is advisory anyway. Read past them.

An external review found four ways a bad example passed the first version:
'het bedragen' (plurals never looked up), a wrong article after a nested <span>
(extraction stopped at the first </span>), an unknown noun with a wrong article
(silently skipped, and never reported anywhere), and a "split" whose single part
was the entire compound. All four are covered now; the last two are reported
rather than ignored.
"""
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from corpus import chapters, dutch_spans  # noqa: E402

LEXICON = pathlib.Path(__file__).resolve().parent.parent / "data" / "lexicon.json"
problems, unknown = [], set()


def load():
    if not LEXICON.exists():
        return {}, {}
    nouns = json.loads(LEXICON.read_text(encoding="utf-8")).get("nouns", {})
    plurals = {v["plural"].lower(): k for k, v in nouns.items() if isinstance(v, dict) and v.get("plural")}
    return nouns, plurals


def head_noun(words, nouns, plurals):
    """The noun an article governs, which is not always the next word.

    Chapter 06 is built on modifiers wedged between an article and its noun —
    'het door u ingevulde formulier' — and the first version of this check only
    ever looked at the adjacent word. It therefore never saw 'formulier', so the
    construction the chapter is ABOUT went unverified, while 'door' and 'in' were
    reported as unknown nouns.

    So: scan forward for the first word the lexicon knows, and stop at anything
    that starts a new noun phrase. Stopping is what keeps this safe — in
    'de door het formulier veroorzaakte fout' the scan halts at 'het' rather than
    matching 'formulier' against 'de' and raising a false failure. The check
    would rather verify less than accuse wrongly.
    """
    for w in words:
        if w in ("de", "het", "een"):        # a new noun phrase; this one is not ours
            return None
        if w in nouns or w in plurals:
            return w
    return None


def check_articles(fn, text, nouns, plurals):
    for line, span in dutch_spans(text):
        for m in re.finditer(r"\b(de|het)\s+([a-zà-ÿ]+((?:\s+[a-zà-ÿ0-9]+){0,6}))",
                             span, flags=re.I):
            art = m.group(1)
            following = [w.lower() for w in m.group(2).split()]
            noun = head_noun(following, nouns, plurals) or following[0]
            n, a = noun.lower(), art.lower()
            if n in plurals:                      # every plural takes 'de'
                if a != "de":
                    problems.append(f"{fn.name}:{line}  article: '{art} {noun}' — "
                                    f"'{noun}' is the plural of '{plurals[n]}'; all plurals take 'de'")
                continue
            entry = nouns.get(n)
            if entry is None:
                unknown.add(n)
                continue
            expected = entry["gender"] if isinstance(entry, dict) else entry
            # A minority of Dutch nouns genuinely take either article — het/de tablet,
            # het/de parfum. De Opmaat marks these, so the lexicon stores a list and
            # both readings pass. Not a fudge for uncertainty: a single-gender entry
            # still fails hard.
            allowed = expected if isinstance(expected, list) else [expected]
            if a not in allowed:
                problems.append(f"{fn.name}:{line}  article: wrote '{art} {noun}', "
                                f"lexicon says '{'/'.join(allowed)} {noun}'")


def check_splits(fn, text):
    for m in re.finditer(r'<div class="split">(.*?)</div>', text, flags=re.S):
        block, line = m.group(1), text[: m.start()].count("\n") + 1
        whole = re.search(r'class="whole"[^>]*>(.*?)</span>', block, flags=re.S)
        if not whole:
            problems.append(f"{fn.name}:{line}  split block has no .whole")
            continue
        target = re.sub(r"[^a-zà-ÿ]", "", whole.group(1).lower())
        parts = re.findall(r'<span class="(part|part head|join)">([^<]*)</span>', block, flags=re.S)
        joined = "".join(re.sub(r"[^a-zà-ÿ]", "", p.lower()) for _, p in parts)
        lexical = [p for kind, p in parts if kind != "join" and re.sub(r"[^a-zà-ÿ]", "", p)]
        if joined != target:
            problems.append(f"{fn.name}:{line}  split does not reassemble: parts give "
                            f"'{joined}', whole is '{target}'")
        elif len(lexical) < 2:
            problems.append(f"{fn.name}:{line}  split has {len(lexical)} lexical part(s): a "
                            f"decomposition needs at least two constituents, not the whole word")


def main():
    nouns, plurals = load()
    ch = chapters()
    if not ch:
        print("  no chapters yet — nothing to check")
        return 0
    for fn in ch:
        t = fn.read_text(encoding="utf-8")
        check_articles(fn, t, nouns, plurals)
        check_splits(fn, t)
    if unknown:
        print(f"  NOTE {len(unknown)} noun(s) took an article but are not in the lexicon, so their "
              f"agreement was NOT checked: {', '.join(sorted(unknown)[:12])}"
              f"{' …' if len(unknown) > 12 else ''}")
    if problems:
        for p in problems:
            print(f"  FAIL {p}")
        return 1
    print(f"  {len(ch)} chapters: article agreement and compound splits OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
