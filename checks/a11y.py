#!/usr/bin/env python3
"""Language marking and document structure. HARD FAIL.

WHY THIS IS A GATE IN A BOOK THAT HAS NO OTHER ACCESSIBILITY MACHINERY.

This book is bilingual on every page — 1200-odd Dutch fragments embedded in
English prose. Without lang="nl" a screen reader pronounces
arbeidsongeschiktheidsverzekering with English phonetics, in a chapter whose
entire claim is that you can read that word once you split it. The marking is
semantic, not compliance decoration, and it is the difference between the book
working and not working for anyone reading by ear.

It is a gate rather than a good intention because THE HARD PART WAS ALREADY DONE.
Every piece of Dutch is already in an element carrying a Dutch-bearing class, so
"is it marked" is answerable mechanically. checks/corpus.py owns the definition of
which classes those are and this imports it rather than keeping a second copy —
the same discipline as lexicon.py importing head_noun from forms.py, adopted after
two copies of one rule drifted apart for a commit.

WHAT THIS CHECKS
  * every page declares a document language on <html>
  * every element with a Dutch-bearing class carries lang="nl"
  * no English-glossed element sits inside a lang="nl" region
  * every page has a skip link pointing at an id that exists on that page
  * exactly one <h1>, and no skipped heading levels

WHAT IT DOES NOT CHECK: colour contrast, focus order, reading order, alt text
(there are no images), or whether the prose is comprehensible. This is the subset
that is decidable from the markup. It is not an accessibility audit and the About
page must not claim it is one.
"""
import pathlib
import re
import sys
from html.parser import HTMLParser

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from corpus import NL_CLASSES  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGES = sorted((ROOT / "docs").glob("*.html")) + sorted((ROOT / "docs" / "chapters").glob("*.html"))

# Dutch-bearing classes that are not class="nl": the compound-split machinery and
# the facsimile subject line. Kept beside the transformer that applied them.
EXTRA = {"whole", "parts", "doc-head"}
DUTCH = NL_CLASSES | EXTRA

problems = []


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.html_lang = None
        self.ids = set()
        self.skip_targets = []
        self.headings = []          # (level, line)
        self.unmarked = []          # (line, class) Dutch without lang
        self.en_in_nl = []          # (line,) English gloss inside a nl region
        self._nl_depth = 0
        self._stack = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = set((a.get("class") or "").split())

        if tag == "html":
            self.html_lang = a.get("lang")
        if a.get("id"):
            self.ids.add(a["id"])
        if "skip" in cls and a.get("href", "").startswith("#"):
            self.skip_targets.append(a["href"][1:])
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.headings.append((int(tag[1]), self.getpos()[0]))

        if cls & DUTCH:
            if a.get("lang") != "nl":
                self.unmarked.append((self.getpos()[0], " ".join(sorted(cls))))
        # An English gloss nested inside a Dutch region would be read aloud in
        # Dutch. They are siblings today; this fails if that ever changes.
        if "en" in cls and self._nl_depth > 0:
            self.en_in_nl.append(self.getpos()[0])

        if tag not in ("meta", "link", "br", "hr", "img", "input"):
            entering = a.get("lang") == "nl"
            self._stack.append(entering)
            if entering:
                self._nl_depth += 1

    def handle_endtag(self, tag):
        if self._stack and self._stack.pop():
            self._nl_depth -= 1


def check(path):
    name = path.relative_to(ROOT / "docs").as_posix()
    p = Page()
    p.feed(path.read_text(encoding="utf-8"))

    if p.html_lang is None:
        problems.append(f"{name}  no <html lang=…>; the document has no language at all")
    elif p.html_lang != "en":
        problems.append(f"{name}  <html lang=\"{p.html_lang}\">, expected \"en\"")

    for line, cls in p.unmarked:
        problems.append(f"{name}:{line}  class=\"{cls}\" holds Dutch but carries no lang=\"nl\"")
    for line in p.en_in_nl:
        problems.append(f"{name}:{line}  an English gloss sits inside a lang=\"nl\" region "
                        f"and would be read aloud as Dutch")

    if not p.skip_targets:
        problems.append(f"{name}  no skip link")
    for t in p.skip_targets:
        if t not in p.ids:
            problems.append(f"{name}  skip link points at #{t}, which does not exist on this page")

    h1s = [ln for lvl, ln in p.headings if lvl == 1]
    if len(h1s) != 1:
        problems.append(f"{name}  {len(h1s)} <h1> elements; expected exactly one")
    prev = 0
    for lvl, line in p.headings:
        if prev and lvl > prev + 1:
            problems.append(f"{name}:{line}  heading jumps from h{prev} to h{lvl}; "
                            f"a level was skipped")
        prev = lvl
    # The contents page is navigation: if it has no sublevel headings at all, a
    # screen-reader user browsing by heading gets the title and nothing else.
    if name == "index.html" and not any(lvl == 2 for lvl, _ in p.headings):
        problems.append("index.html  no <h2> on the contents page — its Part divisions "
                        "must be headings, not styled paragraphs")


def main():
    if not PAGES:
        print("  no pages — nothing to check")
        return 0
    for path in PAGES:
        check(path)
    if problems:
        for p in problems[:40]:
            print(f"  FAIL {p}")
        if len(problems) > 40:
            print(f"  … and {len(problems) - 40} more")
        return 1
    total = sum(page.read_text(encoding="utf-8").count('lang="nl"') for page in PAGES)
    print(f"  {len(PAGES)} pages: document language set, {total} Dutch fragments marked "
          f"lang=\"nl\", skip links resolve, heading levels contiguous")
    return 0


if __name__ == "__main__":
    sys.exit(main())
