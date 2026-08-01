# CONTEXT — authoring notes for *DutchABC*

Internal guide for the chapter series. Not published as a reader-facing page.

Title: **DutchABC** — chosen by the user, 2026-08-01. Settled, not a working title.

Note for consistency, not for reopening: this breaks the series' naming pattern, where the title is an
evocative phrase drawn from the last chapter (*The Quantum Quartet*, *The Bridge*, *No Such Form*).
*DutchABC* is plainer and more searchable. Two consequences to honour rather than fight:

- **The title carries no argument, so the landing page must.** In the three previous books the title
  did some of the framing work. Here `index.html`'s lede is the only thing standing between the reader
  and the assumption that this is another beginner's course — which is the one thing it is not. Write
  that lede with care.
- **Do not let the plain title license plain prose.** The house style is unchanged.

Chapter 14 therefore loses its title-as-punchline role. It keeps its structural role as the
destination: the blue envelope, read end to end.

Fourth in a series built the same way, after *The Quantum Quartet*, *The Bridge* and *No Such Form*.

## Scope — decided 2026-08-01

**This is a reading book.** Listening is handled elsewhere by the reader and is out of scope. Speaking
and writing production are out of scope. Say so on the About page plainly rather than implying full
coverage.

That decision is load-bearing and improves the project in three ways:

1. It removes the medium mismatch. A static HTML book cannot teach listening; it is an excellent
   vehicle for reading, because the artefacts being read *are text* and can sit on the page.
2. It closes the project's biggest sourcing hole. Chapter 01 previously rested on connected speech and
   reduction, for which **no source in `sources/` was adequate** — Donaldson gives pronunciation one
   page. Every source we own is written material about written material.
3. It makes the destination concrete and testable: *read the letter that arrived today, unaided.*

## Premise

The reader has lived in the Netherlands for seven years and is at A1. That is not a beginner. It is
someone surrounded by written Dutch — post, forms, signage, contracts, the buurtapp, Marktplaats,
work email, the blue envelope on the mat — who routes around every piece of it. Asks a colleague.
Runs it through a translator. Files it unread and hopes.

**The thesis: what blocks an adult reading real Dutch is not vocabulary. It is that Dutch text is
built out of a few devices that make the words you know unrecognisable.** Nouns are welded into
compounds that no dictionary contains. Verbs split in half and the halves sit ten words apart.
Pronouns fuse with prepositions into *daarbij*, *hiervan*, *waarop*. Officialese nominalises its verbs
and hides its one actionable sentence in the fourth paragraph.

Each of those is mechanical, learnable in a sitting, and almost never taught — because a course
teaches you to read *the course*, and the course was written to be readable. **This book is about
Dutch that was not written for you.**

## Reader

- Seven years in NL. A1 "at best." Recognises maybe 800 words on sight.
- Routes around written Dutch entirely, and the workarounds are good enough that nothing forces the
  issue — which is why seven years produced no progress.
- Is an adult with an analytical job and does **not** need to be protected from an explanation.
  Cartoon mnemonics and "don't worry about why" are the register of every A1 book on the market and
  are part of why the reader is still at A1. Explain the actual rule. It is not hard; it was withheld.
- Wants everyday competence, not a certificate. **Target: everyday life in NL, not the inburgering
  inventory.** Real documents, not exam scenarios.

## What "solid A2 reading" means here

Concretely, the reader can:

- decompose an unfamiliar compound — *arbeidsongeschiktheidsverzekering* — without a dictionary;
- find the verb that governs a long sentence, and the particle that belongs to it;
- tell which noun a *die* / *dat* / *waarvan* clause is attached to;
- read *daarbij*, *hiervan*, *waarop* without stalling;
- skim a formal letter and locate the two sentences that say **what is required** and **by when**;
- read a belastingdienst letter end to end and know what it wants.

The last one is the exit criterion and the last chapter.

## Style — inherited from the series, and non-negotiable

- **One idea per chapter**, motivated before it is stated. If a chapter grows a second, split it.
- **Scholarly but plain.** Short sentences. No exclamation marks, no emoji, no encouragement. The
  reader is an adult who has been condescended to by four books already.
- **Name the gap.** Where the standard courses teach something that does not match real documents, say
  so plainly and say what the documents do instead. That honesty is the book's value, not a defect —
  the same rule as *The Bridge*'s "where L&L never reaches the idea, the essay says so."
- **No self-assessment.** Never write that a chapter is the clearest or the most important. *Show* it.
  (This tic recurred in all three previous books and has a standing grep in `verify.sh`.)
- British/neutral spelling in the English prose. Dutch is Dutch.
- **Never reproduce course-book prose, dialogues or exercises.** A grammatical fact is free; an
  author's sentence and an author's example are not. Every Dutch example is ours or observed.

## Examples — the thing that makes or breaks it

**Every example is a piece of real Dutch text the reader could have received.** The test: *where would
this have arrived?* If there is no answer, cut it.

- Letters and forms: gemeente, belastingdienst, zorgverzekeraar, huurcommissie, energy, bank
- Contracts and statements: employment, tenancy, insurance policy, jaaropgave
- Marktplaats listings, buurtapp and WhatsApp messages, work email — the informal written register
- Signage, packaging, ticket machines, parking apps, NS disruption notices

**Genre is content, not backdrop.** A brief from the belastingdienst and a buurtapp message are
different languages, and the book says which devices belong to which. Parts IV and V exist for that.

**Keep one document running.** *No Such Form* kept $X_0(11)$ visible through its hardest Part so the
abstract material had one concrete object the reader already knew. Do the same: one real letter,
introduced in chapter 01 as unreadable, returned to in every Part as more machinery lands, and read
completely in chapter 14. Choose it before drafting 02.

## Chapter template (every chapter)

Exact headings, `<section class="step">` with a numbered pill on the `<h2>`:

1. **On the page** — the raw material. A real fragment the reader cannot currently get through, and a
   plain statement of exactly where the eye stops and why.
2. **What it is doing** — the one device, explained properly, with a rule you can apply. The single idea.
3. **Read it** — the reader works the device on the fragment from step 1, then on two more. Includes the
   failure modes: the wrong parse a learner reaches for, and how the text would have looked if it
   meant that instead.
4. **In your own post** — where this appears in documents the reader already owns, and what to go look
   at this week. Plus references, checked.

Then a short **kaart** (`<section class="kaart">`): three columns — *nieuw* (introduced here), *terug*
(earlier chapters leaned on, by number), *nog niet* (deliberately postponed, and to which chapter).
The ledger idea, kept because it enforces the no-forward-reference discipline that made book 3
readable — but advisory, not a build gate. See Verification.

## Spine — 14 chapters, five parts

### PART I — WHAT MAKES A KNOWN WORD UNRECOGNISABLE (3)

| # | Slug | The one idea | Notes |
|---|------|--------------|-------|
| 01 | words-that-arent-in-the-dictionary | Dutch welds nouns into compounds without limit: *ziektekostenverzekering*, *inkomstenbelasting*, *arbeidsongeschiktheidsverzekering*. They are not in any dictionary and they are not one word — they decompose, right-to-left, and the last element is the noun that matters. | **The diagnosis chapter and the highest-value skill in the book.** Half of officialese becomes readable the moment you can split. The linking *-s-* and *-en-* are a real sub-rule. Donaldson has noun formation; the courses have nothing systematic. |
| 02 | the-verb-at-the-end | The verb bracket, at reading speed. Dutch puts one verb second and throws the rest to the end of the clause, so the meaning-bearing word arrives last. Reading — unlike listening — you can jump to the end first, and should. | Highest-dependency chapter: 03, 06, 07, 08 and 09 all speak its language. Donaldson **refused** to write a word-order chapter — every formalisation he had seen "fails miserably" — which is the argument for a reading *strategy* over a rule table. His Time–Manner–Place order (printed 95) is usable. |
| 03 | verbs-that-split | Separable verbs at a distance: *bel … op*, *neem … mee*, *geeft … aan*. In a long written clause the two halves can sit fifteen words apart, and neither half alone is findable. | Taught twice before A2 by *Taaltalent* — so this is not an introduction. It is about the *reading* failure: you looked up *bel*, you looked up *op*, and both were wrong. |

### PART II — WHAT REFERS TO WHAT (3)

| # | Slug | The one idea | Notes |
|---|------|--------------|-------|
| 04 | de-het-die-dat | *de*/*het* is not trivia for a reader: it is the tag that tells you which noun a later *die* or *dat* points back to. Roughly two-thirds *de*; all plurals *de*; all diminutives *het*. | Reframed for reading — a speaker's problem with gender is embarrassment, a reader's is ambiguity. Donaldson gives six pages of gender rules (printed 27–32), so the "80% is rule-governed" claim is sourced. |
| 05 | the-clause-that-hangs-off | Relative clauses: *die*, *dat*, *wat*, *waarvan*, *waarbij*, *waarin*. Formal Dutch stacks them, and the verb of the relative clause goes to the end, so the reader must hold two brackets at once. | Depends on 02 and 04, and is where they pay off together. The single most common structure in a legal or official sentence. |
| 06 | daarbij-hiervan-waarop | The *er* / *hier‑* / *daar‑* / *waar‑* + preposition family. *Daarbij, hiervan, waarop, ernaar, hierbij, waardoor.* One closed system, mechanically decodable, and utterly opaque until someone shows you it is preposition-plus-pointer written backwards. | ⚠ **Confirmed gap.** *De Opmaat* gives three uses of *er* and *Taaltalent 2* gives one; **neither gives the prepositional forms**, which are exactly the ones that saturate written Dutch. Donaldson devotes a whole chapter to *Er* (printed 235–238). Pair with 12's abbreviations as pure decoding wins. |

### PART III — WHO MUST DO WHAT, AND WHEN (3)

| # | Slug | The one idea | Notes |
|---|------|--------------|-------|
| 07 | the-other-past-tense | Courses teach the perfect first because it dominates speech. **Written Dutch — narrative, formal, official — runs on the imperfect**: *ontving, verzocht, bleek, diende*. The tense you were taught last is the one on the page. | **A cleaner claim than the spoken version this chapter had before the scope change.** Verified: *Taaltalent 1* teaches the perfect at A1, *Taaltalent 2* the imperfect at A2. The strong-verb list is the work, and Donaldson's alphabetical list (printed 125–135) is exactly the reference. |
| 08 | moeten-dienen-hoeven | Obligation, and its written register. *Moet* becomes *dient u te*; *hoeft niet* becomes *is niet vereist*; permission becomes *kunt u*. Finding the obligation is most of what reading a letter is for. | Modal auxiliaries in Donaldson printed 146–153. *Taaltalent 2* teaches *moeten* vs *hoeven*; neither course teaches *dienen te*, which is the form that actually appears in post. |
| 09 | nobody-does-anything | The passive and nominalisation — officialese's two habits. *Wordt verstrekt*, *is vastgesteld*, *na ontvangst van*, *het indienen van*. Both delete the actor, which is why you cannot tell who must act. | Donaldson: passive printed 161–165. The reading skill is restoring the missing subject: *who* files, *who* decides, *who* pays. Sets up 13 and 14 directly. |

### PART IV — REGISTER (2)

| # | Slug | The one idea | Notes |
|---|------|--------------|-------|
| 10 | echter-tenzij-mits | The logic words — the joints of a formal text. *Echter, tenzij, mits, indien, voorts, derhalve, alsmede, bijgaand.* They carry the conditions and exceptions, they are invisible to a learner, and getting one wrong inverts the meaning of a letter. | Conjunctions in Donaldson printed 190–204; *want* vs *omdat* is *Taaltalent 2* ch. 4. But *tenzij* / *mits* / *indien* are the ones in your post and no course reaches them at A2. |
| 11 | u-je-and-the-buurtapp | The two written registers side by side: *Geachte heer/mevrouw … hoogachtend* against a buurtapp message full of diminutives and particles. What *-je* and *even*, *maar*, *hoor*, *toch* are doing when they appear in writing. | Merges the old chapters 10, 11 and 12, correctly — for a *reader* these are one topic: recognising which register you are in and what its markers mean. ⚠ **Particles confirmed absent from all three sources** (Donaldson's "intensifying adverbs", printed 94, is *heel/erg/zeer* — checked). ⚠ **Donaldson is 1981 and prescriptive; do not take his *u*/*je* usage as current.** |

### PART V — THE REAL DOCUMENTS (3)

| # | Slug | The one idea | Notes |
|---|------|--------------|-------|
| 12 | z-o-z | The furniture of Dutch documents: abbreviations (*o.a., d.w.z., i.v.m., t/m, m.b.t., z.o.z., a.u.b., excl.*), dates, money, and how amounts and periods are written. ***Half drie* is 2:30, not 3:30.** | Small, unglamorous, and the source of seven years of real errors — missed appointments and wrong payments. Donaldson: numerals printed 222–234, **Appendix 3 abbreviations printed 260–264**. Justify by the failure, not the grammar. |
| 13 | anatomy-of-a-brief | The shape of a Dutch official letter: *kenmerk*, *betreft*, the dated opening, the conditions, the one actionable sentence, the *bezwaar* paragraph, *zie ommezijde*. Where each lives, and how to skim to the two that matter. | Genre, not grammar. Donaldson's Appendix 1 (printed 244–247) is letter *writing*, which is the mirror image and usable as evidence of the conventions. The highest practical payoff per page in the book. |
| 14 | the-blue-envelope | One real belastingdienst letter, read completely, using every device in the book — compounds, the bracket, a split verb, two relative clauses, *daarbij*, an imperfect, a *dient u te*, a passive, a *tenzij*, three abbreviations. | The destination. Nothing new is introduced; everything is consumed. If a device in this letter has no earlier chapter, that is a spine defect — fix the spine, not the letter. |

## Sequencing notes

- **Write 01 and 14 first**, the two ends of the rope, as in all three previous books. 01 fixes the
  diagnosis and 14 fixes the destination; everything between justifies itself against both.
  **Choose the real letter for 14 before drafting anything else** — the spine is answerable to it.
- **02 is the highest-dependency chapter.** Write it early and well.
- **05 needs 02 and 04 both landed.** It is the first chapter that combines rather than introduces.
- **Part III is where a reader could stall** — three chapters of formal-register machinery. Keep the
  running letter most visible there.
- **06 and 12 are pure decoding wins** and are the most immediately satisfying chapters in the book.
  Do not bury both in the same Part; 06 sits at the end of Part II deliberately.

## Sourcing discipline

The user owns Dutch material in hardcopy and PDF. **This restores book 2's rule, which book 3 had to
work around:** every specific pointer is checked against an actual copy in `sources/`. Books we do not
have are cited by topic only, never by page.

- **Two passes, as in books 2 and 3.** Verification pass: sources open, pin every pointer. Writing
  pass: **sources closed**, write from understanding. With a course book's example in the context
  window the path of least resistance is to reproduce it — that is exactly how book 2 shipped three
  verbatim quotes before the sweep caught them.
- **Tier A** — the four books in `sources/`, by printed page, once checked. See `sources/README.md`.
- **Tier B — orientation only, never cited.** Wikipedia, Duolingo, forums, YouTube, blogs.
- **Tier C** — anything not in `sources/`. Topic-level only, forever.
- `sources/` is git-ignored and never pushed. No source text is reproduced anywhere.

## Verified against the sources — 2026-08-01

Everything below was checked against a copy in `sources/`. **Nothing here is recalled.**

### The standard teaching order

*Taaltalent* deel 1 (→A1): personal pronouns, finite verb, conjugation, question forms, *willen*,
inversion, noun + article, plurals, *niet/geen*, adjectives, *kunnen/mogen*, frequency words, the
comparative, *moeten*, *even … als*, **the perfect (2 units)**, prepositions, **separable verbs
(2 units)**, sequence words.

*Taaltalent* deel 2 (A1→A2): **the diminutive**, superlative, future with *gaan*; *deze/dit/die/dat*,
conjunctions *en/maar/want/of/dus*, separable vs inseparable verbs; the imperative; *lopen/staan/
zitten/liggen/hangen* + *te*; ***want* vs *omdat***; ordinals, indirect question, ***er* and *daar* as
place**, *omdat* vs *als*; *om … te*; **the imperfect** and *toen*; reflexive verbs; *moeten* vs *hoeven*.

*De Opmaat*'s grammar reference (printed 222–268) is organised by category: verb (present, modals,
perfect, imperfect, future, separable, reflexive, *om…te*), sentence structure, pronouns, adjective,
comparative/superlative, negation, plurals, **Er (8.1 + numeral, 8.2 place, 8.3 indefinite subject)**,
irregular verbs.

### Corrections to my first draft — all three found by checking

1. **Diminutives are not neglected.** *Taaltalent 2* opens with them. My draft said no course teaches
   them; false. Chapter 11 therefore does the thing the courses do not — what *-je* signals in a
   written message — not how to form it.
2. **The perfect is an A1 topic**, the imperfect an A2 one. Under the reading scope this became a
   *better* chapter (07): the tense taught last is the one the documents use.
3. **Separable verbs are taught twice before A2.** Chapter 03 is not an introduction; it is about the
   reading failure.

### Donaldson — what it settles, and what it does not

**Bruce C. Donaldson, *Dutch Reference Grammar*, Martinus Nijhoff 1981.** The only source that explains
rather than drills. Backs chapters 03–10 and 12 directly; page map in `sources/README.md`. ***Er* has
its own chapter** (printed 235–238), gender rules six pages (27–32), diminutives seven (43–49),
prepositional objects (185–189), abbreviations (Appendix 3, 260–264), letter writing (Appendix 1,
244–247).

**He deliberately refused to write a word-order chapter** — every formalisation he had seen "fails
miserably", so he put an index entry instead. **A gift to chapter 02, not a problem:** a serious
reference grammarian declining to tabulate word order is the argument for a reading strategy over a
rule table. Quote the decision, never his sentences.

⚠ **Standing caution: Donaldson is 45 years old and self-describedly "quite strongly prescriptive."**
Authoritative for structure and for what a form *is*; **not** for current usage or social register.
Chapter 11 is the sharpest exposure. Where he conflicts with *De Opmaat* (2009) or *Taaltalent* (2020),
prefer the modern source and say the older account differs. Do not let a later pass "restore" him.

### Gaps confirmed across all sources

Absent from *De Opmaat*, *Taaltalent* 1–2 **and** Donaldson:

- **Compound decomposition as a reading skill** — the pieces exist under word formation; nothing
  teaches splitting an unknown compound. → ch. 01
- **Prepositional *er* / *hier‑* / *daar‑* / *waar‑*** at A2 level. Donaldson has the chapter; neither
  course reaches it. → ch. 06
- ***dienen te*** and the written obligation register. → ch. 08
- ***tenzij* / *mits* / *indien*** — the conditional joints of a real letter. → ch. 10
- **Modal particles** — checked Donaldson's "intensifying adverbs" (printed 94) directly; it is
  *heel/erg/zeer*, degree, not *even/maar/eens/nou/toch/hoor*. → ch. 11
- **Officialese as a genre**, and how to skim it. → ch. 13

### Two source assets worth more than their page count

- ***De Opmaat*'s woordenlijst (printed 283–289)** — an A2 word list, **gender-marked on every noun**,
  grouped by thema. This is `data/lexicon.json` ready-made, and what makes `checks/forms.py` possible.
  Transcribe the gender register; write our own examples.
- ***De Opmaat*'s transcripten luisterteksten (printed 269–282)** — now less central under the reading
  scope, but still the cleanest written-vs-formal register contrast we own.

### Still wanted

Nothing is blocking. The phonology gap that worried the earlier draft **closed with the scope
decision** rather than with a source. A modern Donaldson revision (*Dutch: A Comprehensive Grammar*,
Routledge) would be nice purely to check the 1981 usage claims, but is not needed.

**The real gap is now documents, not books** — see `sources/README.md` for the candidate corpus
already sitting in the user's Downloads. Chapter 14 cannot be written without one real letter.

## Verification — `verify.sh`

Deliberately lighter than book 3's. The user's call: the lexical budget is **advisory, not a gate**.
The book is judged on whether it is worth reading, and an invariant that makes the Dutch stilted would
cost more than it buys.

Ported from books 2 and 3:

1. **Count sync** — chapter files vs distinct contents links. Computed, never typed.
2. **Link resolution** — every internal link resolves.
3. **Generated prev/next** — derived from the chapter files, never hand-maintained.
4. **Quotation scan** — grep ASCII and curly quotes, read every `<blockquote>` by eye. **Higher stakes
   here than in any previous book**, because the sources are pedagogical texts full of exactly the
   sentences we would be tempted to lift, and because real letters are quotable and must not be quoted.
5. **Self-assessment scan** — the grading tic. Caught in all three previous books.
6. **No page numbers for anything not in `sources/`.**

New, and this book's equivalent of book 3's `checks/*.py` — **because wrong Dutch in a Dutch book is
worse than a wrong number in a maths book: the reader cannot detect it and will learn it.**

7. **Every Dutch example is marked up** (`<span class="nl">`, `<p class="nl">`) so the corpus can be
   extracted mechanically. Non-negotiable, and cheap if done from chapter 01.
8. **`checks/forms.py`** — extract every Dutch example and check what this book asserts: article
   agreement against `data/lexicon.json`, adjective inflection, participle and imperfect formation,
   and compound splits against their claimed parts. **Fails the build.**
9. **`checks/lexicon.py`** — reports, does not fail: new words per chapter, cumulative total, and any
   word used before the chapter that introduces it.
10. **`checks/redaction.py`** — **new and important.** Any real document text used as an example is
    scanned for BSN patterns, IBANs, postcodes, addresses, phone numbers and the user's name.
    **Fails the build.** Real post is the book's best material and its only privacy risk.

## Tech stack (unchanged from books 1–3, minus the maths)

- Plain HTML, one `static/style.css`, one small `static/theme.js`. No build step, no framework.
- **KaTeX comes out.** Nothing to typeset. Freed budget goes to reading-specific markup: document
  facsimile blocks, gloss/translation pairs, compound-splitting displays, and a *fout/goed* contrast
  block for the wrong parses in step 3.
- Light/dark theme honouring `prefers-color-scheme`, toggle persisted in `localStorage`.
- Relative links only; `.nojekyll`; GitHub Pages from repo root; the push is the deploy.
- `data/lexicon.json` — the gender and forms register `checks/` validates against.
- `sources/` git-ignored, README listing what is here and what is wanted.

## Open questions for the user

1. ~~Title.~~ **Settled: *DutchABC*.**
2. ~~The running document.~~ **Settled 2026-08-02: the definitieve aanslag inkomstenbelasting.**
   Redacted specimen in `sources/`, device map in `data/running-document.md`. Eleven of the fourteen
   devices are exemplified in one two-page letter.
   **Follow-on, and it is blocking chapter 07:** the tax office writes in deliberately plain language,
   so the letter contains no imperfect, no *tenzij / mits / echter*, and no *dient u te*. A second,
   un-modernised document is needed as a foil — huurcommissie, gemeente, the KvK uittreksel or the
   *waardebepaling*, all already in the user's Downloads. **Pick one before drafting 07.**
3. **Which of these four they actually tried to work through**, and where they stopped. Shapes chapter
   01's diagnosis. "Bought it and never opened it" is also an answer, and an interesting one.
