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


def strip_dutch(text):
    """The page with every Dutch-bearing region and every tag removed.

    What is left should be English prose. Anything Dutch in it is unmarked.
    """
    out = re.sub(
        r'<(?P<t>span|p|div|section)\b[^>]*class="[^"]*\b(?:nl|doc|split|gloss|contrast)\b[^"]*"[^>]*>',
        lambda m: "\x00" + m.group("t"), text)
    # Drop from each marker to its matching close, counting nesting.
    result, i = [], 0
    while i < len(out):
        j = out.find("\x00", i)
        if j == -1:
            result.append(out[i:]); break
        result.append(out[i:j])
        tag = re.match(r"\x00(\w+)", out[j:]).group(1)
        depth, k = 1, j + 1 + len(tag)
        pat = re.compile(rf"</?{tag}\b", re.I)
        while depth and (m := pat.search(out, k)):
            depth += -1 if m.group(0).startswith("</") else 1
            k = m.end()
        i = k
    stripped = "".join(result)
    return re.sub(r"<[^>]+>", " ", stripped)


def chapters():
    return sorted((ROOT / "chapters").glob("*.html"))
