# DutchABC

Fourteen chapters on reading real Dutch — letters, forms, contracts, messages — for someone who has
lived in the Netherlands for years, is still at A1, and has a stack of unopened Dutch post to show
for it.

Fourth in a series built the same way, after [The Quantum Quartet](https://anthonykot.github.io/quantum-quartet/)
(four physicists on early quantum mechanics), *The Bridge* (a quantum-mechanics course carried forward
into quantum information) and *No Such Form* (the proof of Fermat's Last Theorem, one rung at a time).

## The claim

What blocks an adult reading real Dutch is not vocabulary. It is that Dutch text is built out of a
small number of devices that make the words you already know unrecognisable — compounds no dictionary
contains, verbs split fifteen words apart, pronouns fused with prepositions into *daarbij* and
*waarop*, and an official register that deletes the actor from its sentences.

Each is mechanical, learnable in a sitting, and almost never taught, because a course teaches you to
read the course. This book is about the Dutch that was not written for you.

**Reading only.** Not listening, speaking or writing; not inburgering preparation. Stated on the
landing page and in About rather than left to be discovered.

## Reading it

A plain static site. Open `index.html`, or serve it:

```bash
python3 -m http.server 8000
# then visit http://localhost:8000/
```

## Structure

Each chapter follows four steps — **On the page → What it is doing → Read it → In your own post** —
and closes with a **kaart**: what was introduced, which earlier chapters it leaned on, and what is
deliberately postponed. Chapters are in dependency order; nothing uses what a later chapter builds.

The last chapter reads one real belastingdienst letter end to end, using every device in the book and
introducing nothing new. If it needs something with no earlier chapter, that is a defect in the spine.

## Status

Scaffold and the full fourteen-chapter map are in place. **No chapters written yet.**

| | |
|---|---|
| Part I | What makes a known word unrecognisable — compounds, the verb bracket, split verbs |
| Part II | What refers to what — de/het and die/dat, relative clauses, the *daarbij* family |
| Part III | Who must do what, and when — the imperfect, *dient u te*, the passive |
| Part IV | Register — *echter/tenzij/mits*, and formal against informal |
| Part V | The real documents — abbreviations and dates, the anatomy of a brief, the blue envelope |

## Verification

```bash
./verify.sh
```

Wrong Dutch in a book about Dutch is worse than a wrong number in a book about mathematics: the reader
cannot detect it and will learn it. So the Dutch is checked by machine, not by eye.

- **Every Dutch example is marked up** in the HTML, so the whole corpus is extractable. `verify.sh`
  fails on Dutch left as bare prose — a chapter cannot silently opt out of the checks below.
- **`checks/forms.py`** *(hard fail)* — article agreement against `data/lexicon.json`, and every
  compound split must reassemble to the word it claims to decompose.
- **`checks/redaction.py`** *(hard fail)* — scans every page for personal numbers, IBANs, postcodes,
  phone numbers, email addresses and names. Real post is this book's best material and its only
  privacy risk.
- **`checks/lexicon.py`** *(advisory, by decision)* — new words per chapter, cumulative total, lexicon
  coverage, and any word used before the chapter that introduces it. Reports; never fails.
- Plus the checks ported from the previous three books: computed count sync, link resolution, HTML
  well-formedness, a quotation scan, a self-assessment scan, and a ban on page numbers for books not
  in `sources/`.

Every check above was exercised against a deliberately broken chapter before being trusted.

## Sources

Every specific claim is checked against a real copy in `sources/` (git-ignored, never pushed):
Donaldson's *Dutch Reference Grammar* (1981), *De Opmaat: naar NT2-niveau A2* (2009), and *Taaltalent*
deel 1 and 2 (2020). Donaldson is authoritative for structure and not for current usage — he is
forty-five years old and self-describedly prescriptive; where he conflicts with the modern course
books, they win and the chapter says so.

No source text is reproduced anywhere. The content of a rule is free; an author's sentences are not.
Every Dutch example was written for this book or observed in the wild.

## Stack

- Plain HTML, one stylesheet (`static/style.css`), one small script (`static/theme.js`).
- No build step, no framework, no static-site generator. **No KaTeX** — unlike its three predecessors
  this book has no mathematics.
- Light/dark theme honouring `prefers-color-scheme`, toggle persisted in `localStorage`.
- Print-friendly stylesheet.
- `.nojekyll` so GitHub Pages serves the files as-is.

```
index.html               landing page + full 14-chapter contents
about.html               method, scope fence, sources, verification
chapters/NN-slug.html    one file per chapter
static/style.css         shared styles (themes, reading components, print)
static/theme.js          theme toggle
checks/*.py              the Dutch and privacy checks
data/lexicon.json        gender and form register
verify.sh                all local checks
CONTEXT.md               authoring notes: premise, spine, style guide, verified findings
sources/README.md        what is here, page maps, what is still wanted
```

## Deploying to GitHub Pages

Served from the repository root — no build, no workflow.

1. Create an empty repository on GitHub (no README, no `.gitignore` — this repo has both).
2. Add it as a remote and push:

   ```bash
   git remote add origin git@github.com:<user>/<repo>.git
   git push -u origin main
   ```

3. **Settings → Pages**, source *Deploy from a branch*, branch `main`, folder `/ (root)`.

`.nojekyll` is committed and all internal links are relative, so the site works under the `/<repo>/`
subpath without configuration.
