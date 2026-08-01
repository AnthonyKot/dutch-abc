#!/usr/bin/env python3
"""Every piece of Dutch must be marked up, so the corpus is extractable. HARD FAIL.

HEURISTIC, and labelled as one: it recognises Dutch by a list of common function
words. It catches carelessness — a Dutch sentence typed as English prose — not
every possible unmarked word.
"""
import re
import sys

from corpus import chapters, strip_dutch

TELLS = re.compile(
    r"\b(het|een|niet|geen|wordt|worden|werd|dient|dienen|tenzij|mits|indien|echter|"
    r"daarbij|hiervan|waarop|daarvan|hierbij|geachte|hoogachtend|uw|zijn|hebben|"
    r"aanvraag|ontvangen|betaling|bedrag|verzoek)\b", re.I)

problems = []
for fn in chapters():
    english = strip_dutch(fn.read_text(encoding="utf-8"))
    for m in TELLS.finditer(english):
        line = english[: m.start()].count("\n") + 1
        problems.append(f"{fn.name}: unmarked Dutch {m.group(0)!r} near line {line} — wrap it in .nl")

if problems:
    for p in problems:
        print(f"  FAIL {p}")
    sys.exit(1)
print(f"  {len(list(chapters()))} chapters: all recognised Dutch is marked up")
