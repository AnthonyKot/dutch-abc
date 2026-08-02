#!/usr/bin/env python3
"""Catch personal data before it is published. Hard failure.

The best material in this book is the reader's own post. That is also its only
privacy risk, and the repository is public. A hit blocks publication rather than
raising a warning.

Two bugs were found in the first version of this file, both by running it against
real material rather than by reasoning about it. Both are recorded because they
generalise:

  1. SCOPE.  It scanned *.html only. The authoring notes in data/ and CONTEXT.md
     are committed too, and a real aanslagnummer had already been written into
     data/running-document.md. A privacy check that does not cover every committed
     file is not a privacy check. It now scans every text file git would track.

  2. THE CHECK LEAKED WHAT IT PROTECTED. The names to search for were hardcoded
     here, so the file published them. They now live in checks/names.local.txt,
     which is git-ignored. If that file is absent the name check is skipped and
     says so loudly rather than passing quietly.

  3. THE ALLOW LIST EXEMPTED WHOLE LINES. A real BSN sharing a Markdown line with
     the string "example.com" was skipped. It now exempts the matched text only.

WHAT THIS IS: a pattern matcher for STRUCTURED identifiers and a private name
list. It cannot recognise a street address, an unlisted name, or a fact that is
private for reasons only a human knows. It is a safety net under a manual
reading, never a substitute for one. Do not let the public pages claim more.

False positives are expected and are the correct trade. If a match is genuinely
fine, change the example rather than the check.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
NAMES_FILE = ROOT / "checks" / "names.local.txt"

# Every committed text file, not just the pages. sources/ is git-ignored and is
# the one place raw material is allowed to sit.
SUFFIXES = {".html", ".md", ".json", ".txt", ".css", ".js", ".py", ".sh", ".yml", ".yaml", ".csv", ".svg", ".xml"}
SKIP_DIRS = {".git", "sources", "__pycache__", ".claude"}


def targets():
    for p in sorted(ROOT.rglob("*")):
        if not p.is_file() or p.suffix not in SUFFIXES:
            continue
        if any(part in SKIP_DIRS for part in p.relative_to(ROOT).parts):
            continue
        if p == NAMES_FILE:      # git-ignored, and it is the list itself
            continue
        yield p


PATTERNS = [
    ("BSN / 9-digit personal number", re.compile(r"(?<!\d)\d{9}(?!\d)")),
    # A belastingdienst aanslagnummer embeds the BSN, split by dots, so the plain
    # 9-digit pattern above does NOT catch it. Identifiers in Dutch documents are
    # punctuated; assume separators in every future pattern here.
    ("aanslagnummer (contains BSN)", re.compile(r"\b\d{4}\.\d{2}\.\d{3}\.[A-Z]\.\d{2}\.\d{2}\b")),
    ("dotted digit group (9+ digits)", re.compile(r"\b(?:\d[\d.]{9,})\b(?<!\.)")),
    ("SVB / V-number",               re.compile(r"\b(?:VZ|V)[- ]?\d{7,10}\b")),
    ("KvK number",                   re.compile(r"(?<!\d)\d{8}(?!\d)")),
    ("IBAN",                         re.compile(r"\bNL\d{2}[ ]?[A-Z]{4}(?:[ ]?\d{4}){2}[ ]?\d{2}\b|\bNL\d{2}[A-Z]{4}\d{10}\b")),
    ("spaced/hyphenated 9-digit id", re.compile(r"\b\d{3}[ -]\d{3}[ -]\d{3}\b")),
    # Case is the discriminator, not a stopword list. The first version allowed a
    # lowercase spaced form and excluded common English two-letter words, which
    # cannot work in a book whose examples are Dutch: a four-digit year followed
    # by op / in / en / te / om / uw is ordinary prose, and chapter 02 produced
    # three such hits in one page ("belastingjaar 2025 op dit moment"). Growing
    # the list would mean re-growing it for every chapter.
    #
    # Real postcodes are printed uppercase in every Dutch document, so requiring
    # uppercase removes the whole class of false hits at a cost that is stated
    # rather than hidden: a postcode HAND-TYPED in lowercase is now missed. That
    # is acceptable only because copied document text is the actual risk here and
    # it is uppercase, and because real documents get a redaction pass before use.
    # Never match inside a longer alphanumeric run ("#6389ad" is a hex colour).
    ("Dutch postcode", re.compile(r"(?<![#\w])\d{4} ?[A-Z]{2}\b")),
    ("foreign postcode",             re.compile(r"\b\d{2}-\d{3}\b")),
    ("phone number",                 re.compile(r"\b(?:\+\d{2}|0)\s?\d[\s-]?\d{7,9}\b")),
    ("email address",                re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.]+\b")),
    ("long digit run",               re.compile(r"(?<!\d)\d{12,}(?!\d)")),
]

# Lines that are allowed to contain a pattern: this file defines them, and the
# specimen policy notes describe formats rather than carrying real values.
# Matched text that is a documented placeholder rather than a real identifier.
ALLOW = re.compile(r"0000\.00\.000\.[A-Z]\.00\.00|NNNN[.\w]*|<nummer>")
ALLOW_LITERAL = {"1000 AA", "1000 aa", "example.com", "git@github.com",
                 "0000.00.000.X.00.00", "NL00BANK0000000000"}


def main():
    problems = []
    files = list(targets())

    for fn in files:
        text = fn.read_text(encoding="utf-8", errors="replace")
        rel = fn.relative_to(ROOT)
        if rel.parts[0] == "checks" and fn.name == "redaction.py":
            continue
        for label, rx in PATTERNS:
            for m in rx.finditer(text):
                line_no = text[: m.start()].count("\n") + 1
                # Exempt the MATCH, never the whole line: a real identifier
                # sharing a line with a placeholder was previously skipped.
                if ALLOW.fullmatch(m.group(0)) or m.group(0) in ALLOW_LITERAL:
                    continue
                problems.append(f"{rel}:{line_no}  {label}: {m.group(0)!r}")

    if NAMES_FILE.exists():
        names = [n.strip() for n in NAMES_FILE.read_text(encoding="utf-8").splitlines()
                 if n.strip() and not n.startswith("#")]
        for fn in files:
            text = fn.read_text(encoding="utf-8", errors="replace")
            for name in names:
                for m in re.finditer(rf"\b{re.escape(name)}\b", text, flags=re.I):
                    line_no = text[: m.start()].count("\n") + 1
                    problems.append(
                        f"{fn.relative_to(ROOT)}:{line_no}  personal name: {m.group(0)!r}")
        name_note = f"{len(names)} names checked"
    else:
        name_note = ("NO NAME LIST — create checks/names.local.txt (git-ignored), "
                     "one name per line, before publishing")
        print(f"  WARNING: {name_note}")

    if problems:
        for p in problems:
            print(f"  FAIL {p}")
        return 1

    print(f"  {len(files)} text files scanned for structured identifiers, none found; {name_note}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
