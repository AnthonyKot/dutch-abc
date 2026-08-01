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

**The thesis: vocabulary matters, but it is not the whole problem. Dutch text is built out of a few
recurring devices that can make words the reader already knows hard to recognise.** Nouns are welded
into compounds that will not appear as dictionary entries. Verbs split in half and the halves sit ten
words apart.
Pronouns fuse with prepositions into *daarbij*, *hiervan*, *waarop*. Officialese nominalises its verbs
and hides its one actionable sentence in the fourth paragraph.

Each of those is mechanical rather than mysterious, and the core mechanism of each can be explained
in a page. Courses teach several of them as grammar — the verified teaching order in this file records
*Taaltalent* covering separable verbs twice, gender, the imperfect and relative pronouns — but they
rarely assemble them into a practical method for reading real documents. **That is the book's claim,
and it is deliberately narrower than "nobody teaches this": it is that nobody puts it together for
this task.** Do not let a chapter drift back to the stronger version; the project's own source notes
refute it.

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
- read a Belastingdienst letter end to end and know what it wants.

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

- Letters and forms: gemeente, Belastingdienst, zorgverzekeraar, huurcommissie, energy, bank
- Contracts and statements: employment, tenancy, insurance policy, jaaropgave
- Marktplaats listings, buurtapp and WhatsApp messages, work email — the informal written register
- Signage, packaging, ticket machines, parking apps, NS disruption notices

**Genre is content, not backdrop.** A brief from the Belastingdienst and a buurtapp message are
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

**Restructured 2026-08-02.** Three open items — chapter 07 having no specimen, the extended
attributive participle being homeless, and a forward dependency they created between them — turned
out to be one problem with one fix. Recorded in full below, because the reasoning is the kind that
gets silently undone later.

### PART I — WHAT MAKES A KNOWN WORD UNRECOGNISABLE (4)

| # | Slug | The one idea | Notes |
|---|------|--------------|-------|
| 01 | words-you-cannot-look-up | Dutch welds nouns into compounds without limit: *ziektekostenverzekering*, *inkomstenbelasting*, *arbeidsongeschiktheidsverzekering*. Dutch productively welds these into single written words. Many will not have their own dictionary entry, and in ordinary noun compounds the rightmost element is usually the head — the noun that actually matters. ⚠ *Usually*, not always: this is a strong generalisation, not an exceptionless rule. | **The diagnosis chapter and the highest-value skill in the book.** A great deal of officialese becomes readable once you can split. The linking *-s-* and *-en-* are a real sub-rule. Donaldson has noun formation; the courses have nothing systematic. |
| 02 | the-verb-at-the-end | The verb bracket, at reading speed. In an ordinary declarative main clause Dutch puts the finite verb second and throws the rest of the cluster to the end, so the meaning-bearing word arrives last. (Questions can be verb-first; subordinate clauses send the finite verb to the final cluster too; and material can be extraposed after it.) Reading — unlike listening — you can jump to the end first, and should. | Highest-dependency chapter: 03, 04, 06, 07, 08 and 09 all speak its language. Donaldson **refused** to write a word-order chapter — every formalisation he had seen "fails miserably" — which is the argument for a reading *strategy* over a rule table. His Time–Manner–Place order (printed 95) is usable. |
| 03 | verbs-that-split | Separable verbs at a distance: *bel … op*, *neem … mee*, *maken … over*. In a long written clause the halves can sit fifteen words apart, and neither half alone is findable. | Taught twice before A2 by *Taaltalent*, so this is not an introduction. It is about the *reading* failure: you looked up *maken*, you looked up *over*, and both were wrong. |
| 04 | verbs-that-change-shape | A past tense or participle on the page is usually not its own dictionary entry, and there are **four separate reasons**, not one: weak *-d/-t* participles with *ge-* (*gebaseerd*); separable verbs with *ge-* **infixed** (*invullen* → *ingevuld*, *vaststellen* → *vastgesteld*); prefixed verbs that take **no** *ge-* (*verrekenen* → *verrekend*); and strong verbs with a **stem-vowel change** (*ontvangen* → *ontving*/*ontvangen*, *blijken* → *bleek*/*gebleken*). | **Was chapter 07. Reframed and moved — see below.** ⚠ **Corrected after external review:** an earlier draft said one stem-change story yields both imperfect and participle. It does not. Vowel alternation characterises *strong* verbs only; the imperfect does not predict the participle (*worden–werd–geworden*); mixed verbs exist (*bakken–bakte–gebakken*). And six of the seven participles cited from the specimens are **weak**, so a strong-verb-only chapter would not serve 06 and 09. The *ge-* infix rule links this chapter directly back to 03. Donaldson printed 125–135 for the strong list. |

### PART II — WHAT REFERS TO WHAT (3)

| # | Slug | The one idea | Notes |
|---|------|--------------|-------|
| 05 | de-het-die-dat | *de*/*het* is not trivia for a reader: it is the tag that tells you which noun a later *die* or *dat* points back to. Roughly two-thirds *de*; all plurals *de*; all **singular** diminutives *het* (but *de huisjes* — plurals are still *de*). | Reframed for reading — a speaker's problem with gender is embarrassment, a reader's is ambiguity. Donaldson gives six pages of gender rules (printed 27–32), so the useful suffix and semantic classes are sourced. ⚠ For many nouns gender is simply lexical and not visible on the noun; say that rather than implying a rule covers it. And *die*/*dat* narrows the antecedent, it does not always identify it — several candidates can share gender and number. |
| 06 | modifiers-on-both-sides | Relative clauses — *die, dat, wat, waarvan, waarbij, waarin*, and formal *welke* — stacked, each with its own verb at the end. **Then the mirror image: the extended attributive participle**, an entire clause crammed between the article and its noun — *het **door u ingevulde** formulier*. | Needs 02, 04 and 05, and is where all three pay off. **The heaviest chapter in the book, deliberately** — the attributive participle is the same question as a relative clause with the modifier on the left, and separating them would hide that. ⚠ Not "English cannot do this" — English has prenominal participles (*the completed form*). What English cannot do is carry a **long agent phrase** in front of the noun: it says *the form filled in by you*, never *the by-you-filled-in form*. That narrower contrast is the useful one. |
| 07 | daarbij-hiervan-waarop | Pronominal adverbs: an R-word (*er, hier, daar, waar*) plus an adposition. *Daarbij, hiervan, waarop, ernaar, hierbij, waardoor.* Opaque until someone shows you it is a pointer and a preposition written backwards. ⚠ **They split, and often must** — *daar … mee*, *waar … aan*, and especially *er … op*; there are substitutions (*met* → *mee*, *tot* → *toe*); and *ergens/nergens/overal* belong to the same family. "Pointer before preposition" is a decoding heuristic, not a closed mechanical system. | ⚠ **Confirmed gap.** *De Opmaat* gives three uses of *er* and *Taaltalent 2* gives one; **neither gives the prepositional forms**, which are exactly the ones that saturate written Dutch. Donaldson devotes a whole chapter to *Er* (printed 235–238). Pair with 12's abbreviations as pure decoding wins. |

### PART III — WHO MUST DO WHAT (2)

| # | Slug | The one idea | Notes |
|---|------|--------------|-------|
| 08 | moeten-dienen-hoeven | Obligation, and its written register. *Moet* becomes *dient u te*; *hoeft niet* becomes *is niet vereist*. ⚠ *Kunt u* is **not** simply permission — depending on context it is ability, possibility, an available option, or a polite request, and telling those apart is part of the chapter. Finding the obligation is most of what reading a letter is for. | Modal auxiliaries in Donaldson printed 146–153. *Taaltalent 2* teaches *moeten* vs *hoeven*; neither course teaches *dienen te*, which the IND specimen uses four times. |
| 09 | nobody-does-anything | The passive and nominalisation — officialese's two habits. *Wordt verstrekt*, *is vastgesteld*, *na ontvangst van*, *het indienen van*. Both **background** the actor — they do not always remove it; a passive can keep *door X* and a nominalisation can keep an agent. The reading skill is knowing when the actor is genuinely absent and when it is merely late. | Needs 04's participles. Donaldson: passive printed 161–165. The reading skill is restoring the missing subject: *who* files, *who* decides, *who* pays. Sets up 13 and 14 directly. **Two chapters is the right size for this Part** — it is one question asked twice, and padding it would be padding. |

### PART IV — REGISTER (2)

| # | Slug | The one idea | Notes |
|---|------|--------------|-------|
| 10 | echter-tenzij-mits | The logic words — the joints of a formal text. *Echter, tenzij, mits, indien, voorts, derhalve, alsmede, bijgaand.* They carry the conditions and the exceptions, they are easy to read past, and getting one wrong can invert the meaning of a letter. | Conjunctions in Donaldson printed 190–204; *want* vs *omdat* is *Taaltalent 2* ch. 4. But *tenzij* / *mits* / *indien* are the ones in your post and no course reaches them at A2. |
| 11 | u-je-and-the-buurtapp | The two written registers side by side: *Geachte heer/mevrouw … hoogachtend* against a buurtapp message full of diminutives and particles. What *-je* and *even*, *maar*, *hoor*, *toch* are doing when they appear in writing. | For a *reader* these are one topic: recognising which register you are in and what its markers mean. ⚠ **Particles confirmed absent from all three sources** (Donaldson's "intensifying adverbs", printed 94, is *heel/erg/zeer* — checked). ⚠ **Donaldson is 1981 and prescriptive; do not take his *u*/*je* usage as current.** |

### PART V — THE REAL DOCUMENTS (3)

| # | Slug | The one idea | Notes |
|---|------|--------------|-------|
| 12 | z-o-z | The furniture of Dutch documents: abbreviations (*o.a., d.w.z., i.v.m., t/m, m.b.t., z.o.z., a.u.b., excl.*), dates, money, and how amounts and periods are written. **€ 5.000 is five thousand; 9,320% has a decimal comma.** ***Half drie* is 2:30, not 3:30.** | Small, unglamorous, and the source of years of real errors — missed appointments and wrong payments. Donaldson: numerals printed 222–234, **Appendix 3 abbreviations printed 260–264**. Justify by the failure, not the grammar. Completes the toolkit; nothing new after this. |
| 13 | anatomy-of-a-dutch-brief | The shape of a Dutch official letter: *kenmerk*, *betreft*, the dated opening, the conditions, the one actionable sentence, the *bezwaar* paragraph, *zie ommezijde*. Where each lives, and how to skim to the two that matter. | Genre, not grammar. Donaldson's Appendix 1 (printed 244–247) is letter *writing*, the mirror image, usable as evidence of the conventions. The highest practical payoff per page in the book. |
| 14 | the-blue-envelope | A Belastingdienst letter, read completely, using every device in the book — compounds, the bracket, a split verb, a strong participle, two relative clauses, *daarbij*, a *dient u te*, a passive, a *tenzij*, three abbreviations. | The destination. Nothing new is introduced; everything is consumed. A **reconstruction**, not the specimen — see `data/running-document.md`. If a device in this letter has no earlier chapter, that is a spine defect: fix the spine, not the letter. |

### Why 07 became 04, and what it fixed

Three problems, one cause. Recorded because a later pass will otherwise "restore" the tense chapter.

1. **Chapter 07 had no specimen.** Neither the aanslag nor the IND form contains a single finite
   imperfect, because both are *procedural* — standing rules and required actions, which is
   present-tense work. Waiting for a *beschikking* to arrive would have blocked the chapter indefinitely.
2. **The extended attributive participle was homeless.** Found in the IND specimen
   (*het door u ingevulde formulier*), genuinely hard, and in no chapter.
3. **Folding it into 05 created a forward dependency.** *Ingevulde* is a past participle, and
   participle formation lived in the old chapter 07 — two chapters later.

The fix is to notice what that chapter is *actually about for a reader*. Not "which past tense does
written Dutch prefer" — a question about style — but **"why is this verb form not in the dictionary"**,
which is a question about lookup, and therefore the same failure as chapters 01 and 03. *Ontving* is
not an entry; you need to get back to *ontvangen*. One stem-change story yields the imperfect **and**
the past participle.

That reframing pays three times:

- **It unblocks the chapter with sources we already hold.** Finite imperfects are absent from both
  specimens, but **participles are everywhere in both** — *ingevuld, vastgesteld, aangeboden,
  toegekend, uitbetaald, gebaseerd, opgeslagen, beoordeeld, gedeeld*. And Donaldson printed 125–135 is
  the strong-verb list, already mapped.
- **It makes Part I coherent.** Four chapters, one question: *why can I not find this word?* A word
  welded into a compound, a verb displaced to the end, a verb split in half, a verb whose stem changed.
- **It repairs the dependency chain.** 04 now precedes both 06 (attributive participles) and 09
  (passives), each of which needs participles.

⚠ **"Nothing points forward" is still not true of the *examples*.** External review found three: the
chapter-06 and chapter-08 specimen sentences both contain passives, which chapter 09 introduces, and
the chapter-01 thread line was annotated with a nominalisation (*beschikking*), also chapter 09.
The spine order is sound; the **example selection** is not. Fix when drafting: choose chapter-06 and
chapter-08 examples without passives, or move the passive earlier. Tracked in `data/running-document.md`.

Chapters **08–14 keep their numbers**; only 04–07 moved.

**Honesty requirement for chapter 04.** The old framing claimed written Dutch "runs on the imperfect".
Do not carry that over — the two specimens refute it for procedural documents. The chapter should say
plainly that finite imperfects are commoner in narrative and decision letters than in the forms and
assessments that arrive most often, and that the *participles* are what the reader will meet daily.

## Sequencing notes

- **Write 01 and 14 first**, the two ends of the rope, as in all three previous books. 01 fixes the
  diagnosis and 14 fixes the destination; everything between justifies itself against both. The
  running document is chosen (`data/running-document.md`), so this is unblocked.
- **02 is the highest-dependency chapter.** Six later chapters speak its language. Write it early
  and well.
- **04 is the second-highest, and it is new to that role.** Both 06 and 09 need its participles.
  It was the last chapter in the old spine to be written; it is now nearly the first.
- **06 needs 02, 04 and 05 all landed**, and is the first chapter that combines rather than
  introduces. It is also the heaviest. Do not start it until its three inputs exist.
- **07 and 12 are pure decoding wins** and the most immediately satisfying chapters to read. Do not
  bury both in the same Part; 07 closes Part II deliberately.
- **Part III is short — two chapters — and that is correct.** It asks one question twice. If it
  starts growing a third chapter, check whether the new material belongs in Part IV.

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
- **Pronominal adverbs at this level.** ⚠ Not "absent from all sources" — Donaldson devotes a chapter
  to *Er* (printed 235–238). Absent from **both courses** at A2. → ch. 07
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
2. ~~The running document.~~ **Settled: the definitieve aanslag, with IND form 1310 as the foil.**
   Device maps in `data/running-document.md`.
3. ~~Chapter 07 has no specimen / the attributive participle is homeless.~~ **Both closed by the
   2026-08-02 restructure** — see *Why 07 became 04*. Nothing is blocked on a document arriving.
4. **Which of the four books they actually tried to work through**, and where they stopped. Shapes
   chapter 01's diagnosis. "Bought it and never opened it" is also an answer, and an interesting one.
5. **Still welcome, no longer blocking:** a letter from a gemeente, and a *beschikking* that recounts
   a history. The second would let chapter 04 show a finite imperfect in the reader's own post rather
   than only in narrative.

## Standing work

- **Transcribe the gender register** from *De Opmaat*'s woordenlijst (printed 283–289) into
  `data/lexicon.json`. Currently seeded with 17 nouns chosen by hand, which is enough to prove
  `checks/forms.py` works and not enough to check a real chapter. Wanted before chapter 05.
