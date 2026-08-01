#!/usr/bin/env python3
"""Shared extractor: the one place that knows how Dutch is marked up.

Three scripts and verify.sh previously each rolled their own regex for this, and
the one in verify.sh was broken — a backreference </\\1?> that can never match a
closing tag, so correctly marked <p class="nl"> blocks were reported as unmarked.
One parser, used everywhere, is the fix.
"""
import html
import pathlib
import re
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).resolve().parent.parent
NL_CLASSES = {"nl"}
DOC_CLASSES = {"doc", "split", "gloss", "contrast"}


class _Collector(HTMLParser):
    """Collect text inside any element carrying a Dutch-bearing class.

    Nesting-aware: tracks depth so an inner <span> or <strong> does not close the
    region early, which is how a wrong article after nested markup slipped past.
    """

    def __init__(self, classes):
        super().__init__(convert_charrefs=True)
        self.classes = classes
        self.spans = []          # (line, text)
        self._stack = []         # open tags, with the depth we started capturing
        self._buf = None
        self._line = 0

    def handle_starttag(self, tag, attrs):
        cls = set((dict(attrs).get("class") or "").split())
        if self._buf is None and cls & self.classes:
            self._buf, self._line, self._stack = [], self.getpos()[0], [tag]
        elif self._buf is not None:
            self._stack.append(tag)

    def handle_endtag(self, tag):
        if self._buf is None:
            return
        if self._stack:
            self._stack.pop()
        if not self._stack:
            self.spans.append((self._line, html.unescape("".join(self._buf))))
            self._buf = None

    def handle_data(self, data):
        if self._buf is not None:
            self._buf.append(data)


def dutch_spans(text, classes=None):
    """[(line_number, plain_text)] for every marked-up Dutch region."""
    c = _Collector(classes or NL_CLASSES)
    c.feed(text)
    return c.spans


class _Stripper(HTMLParser):
    """Collect only the text OUTSIDE every Dutch-bearing region.

    The first version did this with a marker-and-scan over the raw string. That
    was wrong in a way worth recording: it replaced each Dutch opening tag with a
    sentinel, but the matching </span> stayed in the text, so a later region's
    depth count consumed the wrong close and leaked part of a marked span. It
    surfaced as chapter 01's kaart heading reporting 'niet' as unmarked while
    'Nog' was correctly stripped. Counting tags by hand across a string is the
    bug; a parser that tracks its own stack is the fix.
    """

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []
        self.depth = 0        # >0 while inside a Dutch region
        self._stack = []

    def handle_starttag(self, tag, attrs):
        cls = set((dict(attrs).get("class") or "").split())
        if self.depth:
            self._stack.append(tag)
        elif cls & (NL_CLASSES | DOC_CLASSES):
            self.depth, self._stack = 1, [tag]

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        if not self.depth:
            return
        if self._stack:
            self._stack.pop()
        if not self._stack:
            self.depth = 0

    def handle_data(self, data):
        self.out.append(data if not self.depth else "\n" * data.count("\n"))


def strip_dutch(text):
    """The page with every Dutch-bearing region removed, line numbers preserved.

    What is left should be English prose; anything Dutch in it is unmarked.
    """
    s = _Stripper()
    s.feed(text)
    return "".join(s.out)


def chapters():
    return sorted((ROOT / "docs" / "chapters").glob("*.html"))
