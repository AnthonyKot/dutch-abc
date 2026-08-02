#!/usr/bin/env python3
"""Draft status agrees with the files on disk, everywhere it is stated. HARD FAIL.

WHY THIS EXISTS. Three times now a fact has been fixed in one file and left stale
in another: the spine restructure updated the contents page and not README.md;
chapter 04's description survived two correction rounds because the fixes landed
in CONTEXT.md; and chapter 02 shipped with docs/about.html and README.md both
still saying only chapter 01 was written. checks/spine.py closed the first case.
This closes the second, which is the same bug wearing different clothes: a
human-readable claim about the book's state, duplicated across files, with
nothing tying it to the state.

THE CONTRACT. The set of written chapters is a fact about the filesystem, so it
is computed here and never typed. Every file listed in FILES must contain the
resulting sentence verbatim (whitespace-insensitive, because HTML wraps). Add a
chapter and all three files fail until they are updated — which is the point.

The sentence is deliberately ordinary prose rather than a hidden marker or an
HTML comment. A marker can rot invisibly while the prose beside it lies; a
sentence that has to read naturally in three different documents cannot.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
FILES = ["docs/index.html", "docs/about.html", "README.md"]

# The spine is 14 chapters; checks/spine.py is what enforces that the contents page
# and CONTEXT.md agree on it. Needed here only to resolve "the last chapter".
TOTAL_CHAPTERS = 14


def written():
    """Chapter numbers with a file on disk, as zero-padded strings."""
    out = []
    for p in sorted((ROOT / "docs" / "chapters").glob("*.html")):
        m = re.match(r"(\d{2})-", p.name)
        if m:
            out.append(m.group(1))
    return out


def sentence(nums):
    """The one canonical phrasing. Range form only when the run is contiguous."""
    if not nums:
        return "No chapters are written yet"
    if len(nums) == 1:
        return f"Chapter {nums[0]} is written"
    if len(nums) == 2:
        return f"Chapters {nums[0]} and {nums[1]} are written"
    contiguous = all(int(b) - int(a) == 1 for a, b in zip(nums, nums[1:]))
    if contiguous:
        return f"Chapters {nums[0]}–{nums[-1]} are written"
    return f"Chapters {', '.join(nums[:-1])} and {nums[-1]} are written"


# Verbs that assert work already DONE to an artefact. A chapter with no file on
# disk cannot have been composed, modelled or checked against anything.
DONE_TO_IT = re.compile(
    r"\b(composed|modelled|modeled|checked|verified|reproduced|transcribed|"
    r"proof-?read|audited)\b", re.I)
PLANNED = re.compile(r"\b(will|not yet|to be|planned|would|is going to)\b", re.I)


def unwritten_asserted_as_done(rel, text, nums):
    """A chapter with no file is described as having had work done to it.

    Caught by an external reviewer who read the About page's "Chapter 14 works
    through a reconstructed Belastingdienst letter — composed for this book,
    modelled and CHECKED AGAINST A REAL ONE", went looking for chapter 14 on the
    public branch, and did not find it. The tense was the small problem. The real
    one is that the sentence asserted VERIFICATION — composed, modelled, checked —
    of an artefact that did not exist, on the page whose entire subject is what has
    been checked.

    NARROWED DELIBERATELY, AFTER THE BROAD VERSION FAILED. The first attempt
    flagged any present-tense mention of an unwritten chapter. It fired on
    "Chapter 09 needs the participles built in chapter 04" and on
    "Chapter 10's connectives govern clauses built in chapters 02 and 06" — which
    are statements about the SPINE's dependency structure, true of the plan, and
    not claims that anything exists. A check that cries wolf on the contents page's
    own design notes gets ignored, and an ignored check is worse than none.

    So this asks the narrow question that matches the actual harm: has the prose
    claimed that work was DONE to something that is not there? Describing a planned
    chapter's content in the present tense is ordinary book-blurb English and is
    left alone.
    """
    out = []
    flat = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", text))
    # A parenthetical "(chapter 13)" is a pointer into the contents map, not a
    # claim that the chapter exists — the contents page is the authority on that,
    # and it marks unwritten chapters as stubs. Flagging those was this check's
    # first behaviour and it produced four false positives immediately. Only a
    # chapter named in running prose is asserting anything.
    spans = [(m.start(), m.end()) for m in re.finditer(r"\([^()]*\)", flat)]

    refs = []
    # (?:&nbsp;|\s)+ and not \s*&nbsp;?\s* — the latter makes only the SEMICOLON
    # optional, so it demanded the literal string "&nbsp" and quietly matched only
    # the one site that used the entity. Three of four injected faults passed
    # because of it, which is the whole reason faults get injected.
    for m in re.finditer(r"[Cc]hapters?(?:&nbsp;|\s)+(\d{1,2})", flat):
        refs.append((m.start(), f"{int(m.group(1)):02d}"))
    # "The last chapter" is a reference to chapter 14 by another name, and it is
    # how both the homepage and README phrase it. A number-only pattern cannot see
    # them, and they were two of the four sites that needed correcting.
    last = f"{max(int(n) for n in nums) if nums else 0:02d}"
    total = TOTAL_CHAPTERS
    if last != f"{total:02d}":
        for m in re.finditer(r"[Tt]he (?:last|final) chapter", flat):
            refs.append((m.start(), f"{total:02d}"))

    seen = set()
    for at, n in sorted(refs):
        if n in nums or any(a <= at < b for a, b in spans):
            continue
        start = max(0, flat.rfind(".", 0, at) + 1)
        end = flat.find(".", at)
        sent = flat[start: end if end != -1 else len(flat)].strip()
        verb = DONE_TO_IT.search(sent)
        if not verb or PLANNED.search(sent) or (rel, n, sent) in seen:
            continue
        seen.add((rel, n, sent))
        out.append(f"{rel} — chapter {n} has no file on disk, but the prose says it was "
                   f"{verb.group(0).lower()}: …{sent[:110]}…")
    return out


def main():
    nums = written()
    want = sentence(nums)
    missing = []
    for rel in FILES:
        fn = ROOT / rel
        if not fn.exists():
            missing.append(f"{rel} — file not found")
            continue
        text = fn.read_text(encoding="utf-8")
        # HTML wraps mid-sentence, so compare on collapsed whitespace.
        hay = re.sub(r"\s+", " ", text)
        if want not in hay:
            missing.append(f"{rel} — does not contain {want!r}")
        missing += unwritten_asserted_as_done(rel, text, nums)

    if missing:
        print(f"  {len(nums)} chapter file(s) on disk, so every status claim must read: {want!r}")
        for m in missing:
            print(f"  FAIL {m}")
        return 1

    print(f"  draft status consistent across {len(FILES)} files: {want.lower()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
