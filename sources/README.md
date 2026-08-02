# sources/

Git-ignored. Never pushed, never reproduced. See CONTEXT.md → *Sourcing discipline*.

Two passes, as in books 2 and 3: **verification pass with these files open** to pin every pointer,
then **writing pass with them closed**. A course book's example dialogue in the context window is the
single most likely way this project ships someone else's sentences.

## Arrived

| File | What it is | Status |
|---|---|---|
| `donaldson-dutch-reference-grammar.pdf` | **Bruce C. Donaldson, *Dutch Reference Grammar*, Martinus Nijhoff, © 1981, ISBN 90 247 2354 x.** 273 PDF pages, **two printed pages per scan**, no text layer, very legible. The only book here that *explains* rather than drills. ⚠ **Written December 1980** — see the caution below. | **Tier A**, with a standing date caveat. |
| `de-opmaat-a2.pdf` | **Beersmans & Tersteeg, *De Opmaat: naar NT2-niveau A2*, 2009 (2e oplage 2010), ISBN 978 90 8506 723 8.** 289pp, complete. Scanned — no text layer — but renders legibly at 100 dpi via `pdftoppm`. | **Tier A.** The single most valuable file in the project. |
| `taaltalent-2-preview.pdf` | **Verbruggen & Taks, *Taaltalent deel 2*, Coutinho, 2e druk 2020, ISBN 978 90 469 0756 6.** Publisher *inkijk* sample, 31pp: complete `Inhoud` plus all of chapter 1 *De hobby* and part of chapter 4 *Het werk*. Has a text layer. Subtitled **"van A1 naar A2"** — this book's exact span. | **Tier A for its contents and the sampled chapters only.** Everything else in it is Tier C. |
| `taaltalent-1-preview.pdf` | *Taaltalent deel 1* (→A1), same series, ISBN 978 90 469 0755 9. 44pp preview, text layer. | Tier A for its chapter/grammar list. Establishes what the reader was supposed to already have. |
| `taaltalent-3-preview.pdf` | *Taaltalent deel 3* (→B1), ISBN 978 90 469 0837 2. 36pp preview, scanned. | Low priority — above our ceiling. Useful only to confirm a topic is deferred past A2. |

### Donaldson — page map and the date caution

**Two printed pages per PDF page: printed page `P` is on PDF page `floor(P/2)`.** Verified against
the preface (printed 8 → PDF 4) and chapter 2 (printed 14 → PDF 7).

```bash
pdftoppm -png -r 110 -f $((P/2)) -l $((P/2)) sources/donaldson-dutch-reference-grammar.pdf /tmp/…/out
```

| Printed | Section | Our chapter |
|---|---|---|
| 13 | Pronunciation — one page | — (out of scope: reading only) |
| 27–32 | Rules for the gender of Dutch nouns | 05 |
| 43–49 | Diminutives, seven pages | 11 |
| 50–57 | Personal pronouns (*u* / *je*) | 11 |
| 74–91 | Adjectives, rules for inflection | 05 |
| 92–111 | Adverbs; 94 intensifying; **95 Time–Manner–Place order** | 02 |
| 146–153 | Modal auxiliary verbs | 08 |
| 180–184 | Separable / inseparable verbs | 03 |
| 185–189 | **Verbs followed by prepositional objects** | 07 |
| 190–204 | Conjunctions: 190 co-ordinating, 192 subordinating | 10 |
| 222–234 | Numerals; 229 money, **230 time**, 231 dates | 12 |
| **235–238** | ***Er* — its own chapter** | 07 |
| 239–243 | Negation | — |
| 244–247 | Appendix 1: letter writing | 13 (writing, as evidence of the conventions a reader meets) |
| 125–135 | Alphabetical list of strong and irregular verbs | 04 |
| 265–274 | Index — Donaldson's substitute for a syntax chapter | 02 |

⚠ **Donaldson is 45 years old and says himself he is "quite strongly prescriptive."** For a book whose
thesis is how people speak *now*, that is a live risk, not a footnote. Usage has moved since 1980,
most visibly on *u* vs *je* — which is chapter 11's entire subject. **Rule: Donaldson is authoritative
for structure and for what a form is; he is not authoritative for current usage or social register.**
Where the two conflict, prefer *De Opmaat* (2009) and *Taaltalent* (2020), and say in the chapter that
the older account differs.

### Reading the scans

`de-opmaat-a2.pdf` is 106 MB and exceeds the Read tool's extraction limit. Render pages first:

```bash
pdftoppm -png -r 100 -f <first> -l <last> sources/de-opmaat-a2.pdf /tmp/…/out
```

100 dpi is enough to read body text and is ~200 KB/page. Key page offsets (PDF page = printed page + 2):

- printed 222–268 — the whole grammar reference
- printed 263–265 — `8 Er`, all three subsections
- printed 269–282 — **transcripten luisterteksten**
- printed 283–289 — **woordenlijst**, gender-marked, grouped by thema

## Specimens

Two real documents, chosen 2026-08-02 as the book's running pair. Device maps in
`data/running-document.md`.

| File | What | Role |
|---|---|---|
| `specimen-aanslag.txt` | definitieve aanslag inkomstenbelasting, **fully redacted — every monetary amount replaced with invented figures** | The running document. The *modernised* end of officialese: plain language, short sentences, questions as headings. |
| `specimen-ind-1310.pdf` | IND form 1310, *Bewijs van garantstelling*. A public blank form, no personal data. | The foil. The *un-modernised* end: `dient te worden`, `welke`, `bescheiden`, stacked passives, extended attributive participles. |

The contrast between them is itself content — the tax office rewrote its letters and the immigration
service did not.

## Still wanted

1. ~~A reference grammar in English for adults.~~ **Arrived** — Donaldson, above. A later edition
   (*Dutch: A Comprehensive Grammar*, Routledge, 1997/2008) would still be worth having purely to check
   the 1980 usage claims against a modern revision by the same author, but this is no longer blocking.
2. ~~Anything on Dutch connected speech / reduction.~~ **Moot — the book is reading-only as of
   2026-08-01.** Listening is handled elsewhere by the reader. Donaldson's single page on pronunciation
   (printed 13) no longer matters. Recorded so nobody re-opens this as a gap.
3. ~~Real post.~~ **Two specimens chosen** — see above. Two specific gaps remain:
   - **A letter from a gemeente.** Searched every PDF in the user's Downloads for gemeente / BRP / WOZ
     / huurcommissie markers; there is none. A WOZ-beschikking, afvalstoffenheffing, parkeervergunning
     or BRP uittreksel would all serve.
   - **A *beschikking* or *besluit* that recounts a history** — anything containing *"Wij hebben
     vastgesteld dat…"* or *"Bij besluit van … werd…"*. **No longer blocking**: the 2026-08-02
     restructure made this chapter 04, about verb forms you cannot look up, which the participles in
     both specimens support. A decisional letter would still let it show a finite imperfect in the
     reader's own post rather than only in narrative.
4. Official inburgering / staatsexamen A2 material — not the target, but a free coverage cross-check.

## Candidate real-world corpus (held locally, never copied in)

Chapter 14's raw material is the reader's own mail — better than anything published.

**Filenames are deliberately NOT listed here.** An earlier version of this file named them, and two
were themselves disclosures: one contained a street name and house number, another a case identifier.
`checks/redaction.py` cannot catch that class of leak — it matches structured identifiers, not
meaning — so this is a standing editorial rule, not something a script will enforce:

> **Never record a source filename in a committed file.** Describe the document by type.

Held locally, by type:

- two Belastingdienst income-tax assessments
- one item of correspondence from a social-insurance body
- two consent/registration forms from the business register
- one Handelsregister extract
- one property valuation report
- one bilingual employment document (the Dutch/English pair is useful in itself: same content,
  two registers)

Each needs the user's explicit say-so and a redaction pass before use, even git-ignored.
