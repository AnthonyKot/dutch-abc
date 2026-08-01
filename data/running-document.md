# The running document — definitieve aanslag inkomstenbelasting

Chosen 2026-08-02. The letter chapters 01–13 keep returning to, and that chapter 14 reads end to end.

The specimen lives in `sources/specimen-aanslag.txt` (git-ignored, fully redacted, **every monetary
amount replaced with invented figures** — a person's income is private even with the name removed).
This file records what is structurally true about the genre. It contains terminology and section
headings, which are citable the way a chapter title is; it contains no reproduced exposition.

## Why this letter

It is the document a resident cannot ignore, it arrives annually, and it is dense: eleven distinct
devices from the fourteen chapters appear in a two-page letter. It also happens to be *available* —
the reader has two years of them.

## Device map — verified against the specimen

| Ch | Device | In this letter | Strength |
|----|--------|----------------|----------|
| 01 | compounds | *inkomstenbelasting, volksverzekeringen, loonheffing, heffingskortingen, arbeidskorting, aanslagnummer, bezwaarformulier, bezwaarschrift, rendementsgrondslag, spaartegoeden, verzamelinkomen, belastingconsulent, bronheffing, aftrekposten, rekeningnummer, inkomensafhankelijke regelingen* | **superb** |
| 02 | verb bracket | *Dan moet uw bezwaarschrift op 28 mei 2026 binnen **zijn** bij de Belastingdienst* · *Dan ontvangt u het bedrag meestal binnen 2 weken nadat wij uw rekeningnummer hebben **ontvangen*** | strong |
| 03 | separable verbs at distance | ***maken** het bedrag binnen 1 week na de datum van deze beschikking **over*** — ten words apart · *geeft uw rekeningnummer gemakkelijk **door*** · *hebt **ingevuld*** · *Log **in*** | **superb** |
| 04 | de/het → die/dat | *het bedrag **dat** u ontvangt* against *deze aanslag* / *de reden* — a clean minimal pair inside one letter | strong |
| 05 | relative clauses | *het bedrag dat u ontvangt* · *Aandeel rendementsgrondslag dat aan u wordt toegekend* (relative clause with a passive inside it) | good |
| 06 | *hier-* / *daar-* / *waar-* | ***hiermee** verrekenen* and ***Hierdoor** wordt het bedrag … lager* — two, in consecutive sentences | **superb** |
| 07 | the imperfect | ⚠ **absent** — see below | **none** |
| 08 | obligation | *Moet u nog aanslagen aan ons betalen?* · *U **hoeft** deze brief **niet af te wachten*** · *of u bezwaar moet maken* · *Kunt u* · *Wilt u* | strong, but no *dient u te* |
| 09 | passive / nominalisation | *is gebaseerd op* · *Het rendement … **is vastgesteld** op basis van forfaitair rendement* (no actor at all) · *wordt toegekend* · *Wordt het bedrag aan u uitbetaald* · nominalisations *de verrekening*, *de berekening*, *Vastgesteld vermogen* | **superb** |
| 10 | *echter / tenzij / mits* | ⚠ **absent** — see below | **none** |
| 11 | register | consistently *u* / *uw*; closes *Hoogachtend, de inspecteur*. But **no** *Geachte heer/mevrouw*, and nothing informal | half |
| 12 | numbers and furniture | **€ 5.000 — dot is the thousands separator**; *9,320%* — **comma is the decimal separator**; *af* and *bij* as subtract/add markers; *1e schijf*, *2e schijf*; dates as *16 april 2026*; postcode *1000 AA* | **superb** |
| 13 | anatomy | address block; right-hand metadata column (*Jaar*, *Aanslagnummer*, *Datum*); headline amount boxed at the top; explanation; calculation tables; then three action sections — *Is uw rekeningnummer niet bekend?*, *Aangifte wijzigen*, *Bezwaar maken*; *Uw belastingkantoor*; *Hoogachtend* | **superb** |

## Three findings that change the plan

### 1. The belastingdienst writes in deliberately plain language, and that is why 07 and 10 are missing

This letter has **no imperfect** (chapter 07) and **none of** *echter*, *tenzij*, *mits*, *indien*
(chapter 10). It also has no *dient u te* (chapter 08's headline form). It uses questions as section
headings, short sentences, and *moet* / *hoeft* rather than their formal equivalents.

That is not an accident of this one letter; it is the plain-language style the tax office adopted.
**So the running document sits at the easy end of officialese, not the hard end.**

Two consequences, both good:

- **The book gains a spectrum instead of a sample.** Chapters 07, 10 and the formal half of 11 need a
  second, un-modernised document as a foil. Candidates already in the user's Downloads: the
  huurcommissie or gemeente correspondence, the KvK *uittreksel*, the *toestemmingsverklaring*, the
  property *waardebepaling*. **Pick one before drafting 07.**
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
| 08 | ***dient … te*** | four times, and three of them stack a passive inside: *dient voor legalisatie van uw handtekening bij de gemeente **te worden aangeboden***. This is the form chapter 08 exists for, and the aanslag has none of it |
| 09 | passive, stacked with modals | *dient te worden aangeboden* · *kunnen worden gedeeld* · *wordt beoordeeld* · *worden opgeslagen* · *wat er met uw gegevens wordt gedaan* — five layers of actor deletion in one page |
| 10 | conditional joints | *In geval sprake is van…* · *Wanneer u … dan hoeft u…* · *voordat u begint* · *Daarnaast* · *tezamen met* · *ter onderbouwing van* |
| 05 | relative clauses | ***welke*** as the formal relative pronoun — *alle overige bescheiden **welke** kunnen dienen* — where a course teaches only *die/dat*; plus *personen … **aan wie** u logies wenst te verstrekken* |
| 06 | *waar-* / *daar-* | *de wijze **waarop** de visumaanvraag wordt beoordeeld* · *binnen de **daarvoor** geldende wet-en regelgeving* |
| 01 | compounds | *garantstelling, logiesverstrekking, visumplichtig, visumaanvraag, Vreemdelingenwet, garantsteller, logiesverstrekker, dataprotectie, wet-en regelgeving* — note the **suspended hyphen** in the last, which the aanslag also shows in *Bank- en spaartegoeden* |
| 11 | register | archaic formal vocabulary a course never mentions: *bescheiden* (documents), *geschiedt*, *tezamen*, *overige*, *Raadpleeg* |

### ⚠ A device this form exposes that the spine does not have

> ***Het door u ingevulde formulier*** dient … te worden aangeboden.
> *de **door u uitgenodigde** persoon*

An entire clause crammed between the article and its noun — *the by-you-filled-in form*. The
**extended attributive participle**. English cannot do this at all, so a reader has no instinct for
it, and formal Dutch uses it constantly. It is not in the fourteen-chapter spine.

**Decision needed before drafting Part II.** Options: fold it into chapter 05 (which already teaches
"what is attached to what", and this is the same question with the modifier on the left instead of the
right), or give it a chapter. Folding into 05 is the cheaper answer and probably correct — 05 becomes
*modifiers on both sides of the noun* — but it makes 05 the heaviest chapter in the book.

### Still missing after both documents: the imperfect (chapter 07)

Neither document contains one. Both are **procedural** — they describe standing rules and required
actions, which is present-tense work. The imperfect lives in **decision** letters that recount a
history: a rejection, an appeal outcome, an assessment that explains what was previously established.

Chapter 07 therefore still has no specimen. Two honest routes:

1. Get one — any *beschikking* or *besluit* with a *"U heeft op … verzocht / Wij hebben vastgesteld
   dat … Bij besluit van … werd…"* passage. Worth asking the user for.
2. Re-aim chapter 07 toward where the imperfect actually is for this reader: **news and narrative**
   (NOS, a company announcement, a Wikipedia paragraph) rather than post. That is a defensible
   reading target and arguably a more useful one — but it changes the chapter's premise from
   "documents run on the imperfect" to "everything except your post runs on it", and the spine note
   must be rewritten if we take it.

**Do not draft 07 before this is settled.**

## The thread through the book

One sentence from this letter carries four devices at once and should recur from chapter 01 onward,
gaining a layer each time:

> *We maken het bedrag binnen 1 week na de datum van deze beschikking over naar uw rekening.*

- **ch. 02** — where does the clause actually end?
- **ch. 03** — *maken … over* is one verb, ten words apart; neither half is findable alone
- **ch. 01** — *beschikking* is a nominalisation, *rekening* is not the *rekeningnummer* two paragraphs down
- **ch. 12** — *binnen 1 week na de datum* is a deadline expressed relatively, and the letter contains
  three different time windows (1 week, 2 weken, 4 weken) that mean different things

And the letter's actual point — the one line requiring action — is neither the amount at the top nor
anything in the tables. It is *Verstuur het online bezwaarformulier uiterlijk 28 mei 2026*, buried in
the last section. **That gap between what the letter leads with and what it requires is chapter 13's
whole lesson**, and this document demonstrates it without any help.
