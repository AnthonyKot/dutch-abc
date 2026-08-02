# The running document — definitieve aanslag inkomstenbelasting

Chosen 2026-08-02. The letter chapters 01–13 keep returning to, and that chapter 14 reads end to end.

The specimen lives in `sources/specimen-aanslag.txt` (git-ignored, fully redacted, **every monetary
amount replaced with invented figures** — a person's income is private even with the name removed).
This file records what is structurally true about the genre.

⚠ **Policy note, after external review.** The device tables below quote whole sentences from the
specimen. That is inconsistent with the standing "no source text is reproduced" rule as written. The
resolution: **this is a git-ignored-adjacent working note, and the rule governs the published book,
not the evidence file** — but the rule must say so rather than being quietly broken. Two obligations
follow, and they are not optional: nothing quoted here may reach `chapters/`, and every Dutch example
in a published chapter is written for this book. See CONTEXT.md, *Sourcing discipline*.

## Why this letter

It is the document a resident cannot ignore, it arrives annually, and it is dense: twelve distinct
devices from the fourteen chapters appear in a two-page letter (twelve, counting the table below; the earlier text said eleven). It also happens to be *available* —
the reader has two years of them.

## Device map — verified against the specimen

| Ch | Device | In this letter | Strength |
|----|--------|----------------|----------|
| 01 | compounds | *inkomstenbelasting, volksverzekeringen, loonheffing, heffingskortingen, arbeidskorting, aanslagnummer, bezwaarformulier, bezwaarschrift, rendementsgrondslag, spaartegoeden, verzamelinkomen, belastingconsulent, bronheffing, aftrekposten, rekeningnummer, inkomensafhankelijke regelingen* | **superb** |
| 02 | verb bracket | *Dan moet uw bezwaarschrift op 28 mei 2026 binnen **zijn** bij de Belastingdienst* · *Dan ontvangt u het bedrag meestal binnen 2 weken nadat wij uw rekeningnummer hebben **ontvangen*** | strong |
| 03 | separable verbs at distance | ***maken** het bedrag binnen 1 week na de datum van deze beschikking **over*** — eleven tokens apart · *geeft uw rekeningnummer gemakkelijk **door*** · *hebt **ingevuld*** · *Log **in*** | **superb** |
| 04 | verb forms that change shape | participles throughout — *ingevuld, vastgesteld, gebaseerd, toegekend, uitbetaald, ontvangen, verrekend*; **no finite imperfect**, which is what reframed the chapter | strong for participles |
| 05 | de/het → die/dat | *het bedrag **dat** u ontvangt* — neuter singular takes *dat*. ⚠ **Not a minimal pair**: *deze aanslag* / *de reden* carry no relative clause. A real pair needs a *de*-word with *die* (*de reden **die** …*), which this letter does not supply — construct one, or take it from the IND form | partial |
| 06 | relative clauses | *het bedrag dat u ontvangt* · *Aandeel rendementsgrondslag dat aan u wordt toegekend* ⚠ — the second contains a **passive**, introduced in chapter 09, so it cannot be used in 06 as it stands | good, one example unusable |
| 07 | *hier-* / *daar-* / *waar-* | ***hiermee** verrekenen* and ***Hierdoor** wordt het bedrag … lager* — two, in consecutive sentences | **superb** |
| 08 | obligation | *Moet u nog aanslagen aan ons betalen?* · *U **hoeft** deze brief **niet af te wachten*** · *of u bezwaar moet maken* · *Kunt u* · *Wilt u* | strong, but no *dient u te* |
| 09 | passive / nominalisation | *is gebaseerd op* · *Het rendement … **is vastgesteld** op basis van forfaitair rendement* (no actor at all) · *wordt toegekend* · *Wordt het bedrag aan u uitbetaald* · nominalisations *de verrekening*, *de berekening*. ⚠ *Vastgesteld vermogen* is an **attributive participle + noun**, not a nominalisation — it belongs to chapter 06 | **superb** |
| 10 | *echter / tenzij / mits* | ⚠ **absent** — see below | **none** |
| 11 | register | consistently *u* / *uw*; closes *Hoogachtend, de inspecteur*. But **no** *Geachte heer/mevrouw*, and nothing informal | half |
| 12 | numbers and furniture | **€ 5.000 — dot is the thousands separator**; *9,320%* — **comma is the decimal separator**; *af* and *bij* as subtract/add markers; *1e schijf*, *2e schijf*; dates as *16 april 2026*; postcode *1000 AA* | **superb** |
| 13 | anatomy | address block; right-hand metadata column (*Jaar*, *Aanslagnummer*, *Datum*); headline amount boxed at the top; explanation; calculation tables; then three action sections — *Is uw rekeningnummer niet bekend?*, *Aangifte wijzigen*, *Bezwaar maken*; *Uw belastingkantoor*; *Hoogachtend* | **superb** |

## Three findings that change the plan

### 1. The belastingdienst writes in deliberately plain language, and that is why 07 and 10 are missing

This letter has **no finite imperfect** and **none of** *echter*, *tenzij*, *mits*, *indien*
(chapter 10). It also has no *dient u te* (chapter 08's headline form). It uses questions as section
headings, short sentences, and *moet* / *hoeft* rather than their formal equivalents.

That is not an accident of this one letter; it is the plain-language style the tax office adopted.
**So the running document sits at the easy end of officialese, not the hard end.**

Two consequences, both good:

- **The book gains a spectrum instead of a sample.** Chapter 10 and the formal half of 11 need a
  second, un-modernised document as a foil. Candidates already in the user's Downloads: the
  huurcommissie or gemeente correspondence, the KvK *uittreksel*, the *toestemmingsverklaring*, the
  property *waardebepaling*. **Selected: IND form 1310, below.**
- **It is a genuine observation the book can make.** "The tax office rewrote its letters and the
  housing association did not" is exactly the kind of concrete, checkable claim about real Dutch that
  no course book contains.

### 2. Chapter 14 reads a reconstruction, not this letter

Standing policy is that no source text is reproduced. A government form letter is boilerplate rather
than an author's prose, but the policy does not have an exception and should not grow one.

**So chapter 14 reads a letter we compose** — same genre, same shape, same devices, invented names and
figures, modelled on the specimen. That is better than the original for the purpose: we can pack in
every device from the preceding thirteen chapters deliberately, which a real letter will never do.
The specimen's role is to keep the reconstruction honest.

### 3. The aanslagnummer is the BSN wearing punctuation

The format is `NNNN.NN.NNN.X.NN.NN`, and **the first nine digits are the citizen service number.** The plain nine-digit
pattern in `checks/redaction.py` did **not** catch it, because of the dots. Found by reading a real
letter rather than by reasoning about the check. Two patterns added and tested:
`aanslagnummer (contains BSN)` and `dotted digit group (9+ digits)`.

Recorded because it generalises: **identifiers in Dutch documents are punctuated**, and every future
pattern in that file should assume separators.

## The foil — IND form 1310, *Bewijs van garantstelling en/of particuliere logiesverstrekking*

Chosen 2026-08-02 as the second document, after searching every PDF in the user's Downloads for
gemeente / BRP / WOZ / huurcommissie markers. **There is no gemeente letter there.** The intent was a
gemeente document; this form is what actually delivers that register, and it delivers it harder than a
gemeente letter would. It is a public blank form, not personal correspondence — `sources/specimen-ind-1310.pdf`.

Where the aanslag is the modernised end of officialese, this is the un-modernised end, and the
contrast is the point. It supplies precisely what the aanslag lacked:

| Ch | Device | In this form |
|----|--------|--------------|
| 01 | compounds | *garantstelling, logiesverstrekking, visumplichtig, visumaanvraag, Vreemdelingenwet, garantsteller, logiesverstrekker, dataprotectie, wet-en regelgeving* — note the **suspended hyphen** in the last, which the aanslag also shows in *Bank- en spaartegoeden* |
| 06 | relative clauses | ***welke*** as the formal relative pronoun — *alle overige bescheiden **welke** kunnen dienen* — where a course teaches only *die/dat*; plus *personen … **aan wie** u logies wenst te verstrekken* |
| 07 | *waar-* / *daar-* | *de wijze **waarop** de visumaanvraag wordt beoordeeld* · *binnen de **daarvoor** geldende wet- en regelgeving* (the specimen prints it without the space; standard spelling has one) |
| 08 | ***dient … te*** | four times, and three of them stack a passive inside: *dient voor legalisatie van uw handtekening bij de gemeente **te worden aangeboden***. This is the form chapter 08 exists for, and the aanslag has none of it. ⚠ Every instance embeds a **passive** (ch. 09) — chapter 08 needs a *dient te* example without one, or 09 must move earlier |
| 09 | passive, stacked with modals | *dient te worden aangeboden* · *kunnen worden gedeeld* · *wordt beoordeeld* · *worden opgeslagen* · *wat er met uw gegevens wordt gedaan* — five layers of actor deletion in one page |
| 10 | conditional joints | *In geval sprake is van…* · *Wanneer u … dan hoeft u…* · *voordat u begint* · *Daarnaast* · *tezamen met* · *ter onderbouwing van* |
| 11 | register | archaic formal vocabulary a course never mentions: *bescheiden* (documents), *geschiedt*, *tezamen*, *overige*, *Raadpleeg* |

### A device this form exposed that the spine did not have — now chapter 06

> ***Het door u ingevulde formulier*** dient … te worden aangeboden.
> *de **door u uitgenodigde** persoon*

An entire clause crammed between the article and its noun — *the by-you-filled-in form*. The
**extended attributive participle**. English cannot do this at all, so a reader has no instinct for
it, and formal Dutch uses it constantly. It is not in the fourteen-chapter spine.

**Resolved 2026-08-02: folded into chapter 06**, which becomes *modifiers on both sides* — a relative
clause is a modifier on the right, this is the same question with the modifier on the left, and
separating them would hide that. It makes 06 the heaviest chapter in the book, which is the accepted
cost; a fifteenth chapter for one device would be worse. The fold required moving participle formation
ahead of it, which is what chapter 04 now does.

### The imperfect: resolved by restructuring, not by a new document

Neither document contains a finite imperfect. Both are **procedural** — they describe standing rules
and required actions, which is present-tense work. The imperfect lives in **decision** letters that
recount a history.

**This is closed, and not by waiting for a document.** Old chapter 07 asked *which past tense does
written Dutch prefer*, a question about style that these specimens cannot answer. The chapter's real
subject for a reader is *why is this verb form not in the dictionary* — a question about lookup, which
both specimens answer abundantly, because they are **full of participles** even with no finite
imperfect. Reframed as *verbs that change shape* and moved to **chapter 04**, alongside the other
lookup failures. Full reasoning in CONTEXT.md, *Why 07 became 04*.

A *beschikking* that recounts a history is still welcome — it would let chapter 04 show a finite
imperfect in the reader's own post rather than only in narrative — but nothing is blocked on it.

## The thread through the book

One sentence from this letter carries four devices at once and should recur from chapter 01 onward,
gaining a layer each time:

> *We maken het bedrag binnen 1 week na de datum van deze beschikking over naar uw rekening.*

- **ch. 02** — where does the clause actually end?
- **ch. 03** — *maken … over* is one verb, ten words apart; neither half is findable alone
- **ch. 01** — ⚠ this sentence contains no compound, so it cannot carry chapter 01. Either pick a different thread sentence or introduce the thread at *rekeningnummer* / *bezwaarformulier* elsewhere in the letter. (*beschikking* is a nominalisation, which is chapter 09 — a forward reference.)
- **ch. 12** — *binnen 1 week na de datum* is a deadline expressed relatively, and the letter contains
  three different time windows (1 week, 2 weken, 4 weken) that mean different things

And the letter's actual point — the one line requiring action — is neither the amount at the top nor
anything in the tables. It is *Verstuur het online bezwaarformulier uiterlijk 28 mei 2026*, buried in
the last section. **That gap between what the letter leads with and what it requires is chapter 13's
whole lesson**, and this document demonstrates it without any help.

---

# Appendix — the chapter 14 reconstruction (stage A, 2026-08-02)

**Composed for this book. Not the specimen, and no sentence of the specimen is reproduced here.**
Modelled on the anatomy recorded above; every name, number and amount invented; identifiers use the
placeholder forms `checks/redaction.py` sanctions.

Written and audited **before** any chapter-14 prose, because the contents page carries a promise —
*"if it turns out to need a device that has no earlier chapter, that is a defect in this contents
page, not in the letter"* — and that promise is only honest if the audit is actually run.

## The letter

```
Belastingdienst

A. B. Voorbeeld                     Definitieve aanslag 2025
Voorbeeldstraat 1                   Inkomstenbelasting
1000 AA AMSTERDAM                   Premie volksverzekeringen

                                    Jaar             2025
                                    Aanslagnummer    0000.00.000.X.00.00
                                    Datum            16 april 2026


Te betalen  € 1.245,-

Deze definitieve aanslag is vastgesteld op basis van de door u ingediende aangifte.
Het bedrag dat u nog moet betalen, staat hierboven. De heffingskorting die is
toegepast, vindt u in de specificatie hiervan (z.o.z.).

Berekening
Verschuldigde inkomstenbelasting              €  3.245,-
Ingehouden loonheffing                    af  €  2.000,-
Te betalen                                    €  1.245,-

Betalen
Wij schrijven het verschuldigde bedrag binnen drie weken na de dagtekening van deze
beschikking van uw rekening af, mits u ons daarvoor gemachtigd hebt. Indien wij geen
machtiging hebben, dient u het bedrag zelf over te maken op NL00BANK0000000000
t.n.v. Belastingdienst, onder vermelding van het aanslagnummer.

Is uw adres gewijzigd?
Bij een adreswijziging dient u dit binnen vier weken aan ons door te geven. Doet u
dat niet, dan ontvangt u onze post op het oude adres.

Bezwaar maken
Bent u het niet eens met deze aanslag? Dan kunt u t/m 28 mei 2026 bezwaar maken.
Verstuur het online bezwaarformulier uiterlijk op die datum. Maakt u schriftelijk
bezwaar, dan dient uw bezwaarschrift op 28 mei 2026 binnen te zijn. Vermeld daarbij
altijd de reden van uw bezwaar en het aanslagnummer.

Uw belastingkantoor
Belastingdienst/Kantoor Voorbeeld, Postbus 1, 1000 AA Amsterdam

Hoogachtend,

de inspecteur
```

## Device audit — every device tagged to the chapter that explains it

| Ch | Device | Where it is in the letter |
|----|--------|---------------------------|
| 01 | compound | *inkomstenbelasting, volksverzekeringen, aanslagnummer, heffingskorting, loonheffing, dagtekening, adreswijziging, bezwaarformulier, bezwaarschrift, belastingkantoor* |
| 02 | verb bracket | *Wij **schrijven** het verschuldigde bedrag … van uw rekening **af*** — finite verb second, particle last, thirteen tokens between · *dan **dient** uw bezwaarschrift op 28 mei 2026 binnen **te zijn*** |
| 03 | separable verb at distance | ***schrijven … af*** (13 tokens) · ***door te geven*** with *te* inside the split verb · ***over te maken*** |
| 04 | verb forms that change shape | **weak**: *vastgesteld, ingediende, toegepast, gemachtigd, gewijzigd* · **strong**: ***afgeschreven*** is the participle of the same verb the letter splits, and ***ingediende*** vs *ingediend* shows the attributive *-e* |
| 05 | de/het → die/dat | ***het bedrag dat*** u nog moet betalen · ***de heffingskorting die*** is toegepast — **a true minimal pair, which the real specimen could not supply** |
| 06 | modifiers on both sides | left: ***de door u ingediende aangifte***, ***het verschuldigde bedrag*** · right: the two relative clauses above |
| 07 | *hier-* / *daar-* / *waar-* | *hier**boven*** · *hier**van*** · *daar**voor*** · *daar**bij*** — four, in four different sections |
| 08 | obligation | ***dient u*** … *door te geven* — **a `dient te` with no passive inside it**, which is what chapter 08 needed and the IND specimen never gave · *dient uw bezwaarschrift … te zijn* · *moet betalen* · *hoeft* — absent, deliberately |
| 09 | passive / nominalisation | *is **vastgesteld*** (no actor) · *die **is toegepast*** · nominalisations *berekening, specificatie, dagtekening, adreswijziging, machtiging, vermelding* |
| 10 | the logical joints | ***mits** u ons daarvoor gemachtigd hebt* · ***Indien** wij geen machtiging hebben* · *Doet u dat niet, **dan** …* — fronted condition with inversion and a stated consequence |
| 11 | register | *u* / *uw* throughout, no *je*; *Hoogachtend*; **the signature is a role — *de inspecteur*, not a person** |
| 12 | notation | *€ 1.245,-* and the *,-* · *€ 3.245,-* − *€ 2.000,-* = *€ 1.245,-*, **so the letter checks its own arithmetic** · *16 april 2026*, *28 mei 2026* · *t/m*, *z.o.z.*, *t.n.v.* · ⚠ *af* — **see the gap below** |
| 13 | anatomy | addressee block left, identification block right, *Jaar / Aanslagnummer / Datum* stack, headline amount, basis, calculation, three headed action sections (one a question), *bezwaar*, contact block, closing. **The headline is money the reader OWES and the actionable passage is two-thirds down** |

**Dutch word count: 214** in the prose (excluding the block labels and the calculation table), which is
inside the 250–350 target once the labels are counted.

## What the audit found

### ⚠ One device with no chapter: `af` as the subtract marker

The calculation block uses `af` to mark the line being subtracted. That is real — it is recorded in
the specimen's device map above under chapter 12 — and **no chapter teaches it.** Chapter 12 covers
the two marks, dates, the clock and abbreviations, and never reaches the arithmetic annotations that
sit in the margin of every Dutch calculation table.

By the contents page's own contract this is **a defect in the spine, not in the letter**. The fix is
to add `af` and `bij` to chapter 12, where they belong — they are notation on a calculation, which is
precisely that chapter's subject, and Donaldson's arithmetic vocabulary at printed 228 (*aftrekken
van*, *optellen*) is already the sourced basis for them.

**Do this before drafting chapter 14**, not after.

### Deliberately NOT used, and why

- **`o.v.v.`** for *onder vermelding van*. Extremely common on Dutch payment instructions and **not in
  Donaldson's Appendix 3**, so chapter 12 does not carry it. Spelled out in full rather than smuggled
  in — an unexplained abbreviation in the destination chapter would be the same defect as `af`.
- **`hoeven`**. Chapter 08's releasing verb has no natural place in an assessment that requires
  payment, and manufacturing one would be padding the letter to satisfy a checklist rather than
  writing a letter.
- **`echter`**. Chapter 10 marks it `.unverified` for good reason; the letter does not need it.

### Two things the reconstruction supplies that the real letter could not

1. **A true `die`/`dat` minimal pair.** The specimen has *het bedrag dat u ontvangt* and no
   corresponding *de*-word with *die*, which the device map flags as only partial coverage for
   chapter 05. The reconstruction adds *de heffingskorting die is toegepast* alongside it.
2. **A `dient u te` with no passive inside it.** Every `dient te` in the IND form embeds a passive,
   which chapter 08's notes record as a problem for its examples. *Dient u dit … door te geven* is
   clean, and it doubles as chapter 03's split verb with *te* wedged into it.
