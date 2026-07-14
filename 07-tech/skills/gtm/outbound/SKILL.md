---
name: gtm-outbound
description: >
  Erzeugt 3-Email Cold-Outbound-Sequences pro Niche. Email 1 mit fuenf Varianten
  A-E (Lang, Mittel, Kurz, Feedback, Provokant) für A/B Test, Email 2 als
  Follow-up mit Reply-Threading, Email 3 als Breakup. Plus 5 alternative Subject
  Lines pro Niche.

  Verwende bei: Cold Email, Cold Sequence, Outbound, 3-Email Sequence, Opener-
  Varianten, Subject Line Test, A/B Test, HeyReach Cadence, Outreach-Cadence,
  Email-Sequence aus Foundation, "schreib mir Cold Mails für Niche X",
  "Outreach für DACH SMB", "Email-Kampagne aus Foundation".
---

# Outbound Copy Manager

## Wann nutzen

- "Schreib Outbound Emails für [Niche]"
- "Erstell eine Cold Email Sequence für [Zielgruppe]"
- "Adde eine neue Niche zu unserem Outbound"
- "Iterate die Email Copy basierend auf [A/B Test Results / Feedback]"

## Voraussetzung

Asset Foundation CSV für die Niche existiert (siehe `asset-foundations/SKILL.md`). Wenn nicht: erst dort, dann hier.

## Output

Markdown-File: `outbound-{niche-slug}.md` mit:
- Header-Block (Niche-Daten)
- Email 1, fuenf Varianten A-E, jede mit eigenem Subject
- Email 2 als Follow-up (Reply-Threading)
- Email 3 als Breakup
- 5 alternative Subject Lines für A/B Test

## Core Principles

### Tone

- **Pain-First**: Öffne mit Frage wie SIE das Problem loesen, nie mit Pitch.
- **Keine AI-Sprache**: Nutze "vereinfachte Automatisierung", "Entlastung", "Assistent". Nie "AI", "KI", "kuenstliche Intelligenz".
- **Peer Social Proof**: "50+ Gespräche letzte Woche, alle sehen die gleichen Muster."
- **Fear Removal**: Keine US-Cloud, kein IT-Projekt, Server in Deutschland, DSGVO-konform.
- **Feedback-Angle**: "Wie loesen Sie das intern? Mich würde ehrlich interessieren."
- **Soft CTA**: "Würde mich freuen kurz zu sprechen." Nie Hard Sell.
- **Unternehmer zu Unternehmer**: Peer-Framing, kein Vendor-zu-Buyer.

### Frameworks unter der Haube

- **Hormozi (100M Leads)**: Value-First, spezifische Zahlen, minimiere Effort/Sacrifice.
- **Belfort (Straight Line)**: Pattern Interrupt, Certainty Transfer, Urgency via Scarcity.
- **Brunson (DotCom Secrets)**: Hook-Story-Offer, Epiphany Bridge via Peer-Quotes.

### Ansprache (Du oder Sie)

- **Sie**: Hausverwaltungen, Steuerberater, Aerzte, Anwaelte, formale Branchen.
- **Du**: Handwerker, Schornsteinfeger, Gastro, Fitness, informelle Branchen.
- B2B Tech / SaaS Founder: tendenziell Du in DACH unter 40, Sie wenn unsicher.
- Match die natuerliche Kommunikation der Niche.

## Sequence-Struktur

### 3-Email Sequence

| Email | Timing | Zweck | Laenge |
|---|---|---|---|
| Email 1 (Opener) | Tag 0 | Frage nach ihrem Pain, etabliere Peer-Proof | 5 Varianten A-E |
| Email 2 (Follow-up) | Tag 3-4 | Vertiefe Pain, zeige konkrete Lösung, Quote vom Peer | 1 Version |
| Email 3 (Breakup) | Tag 8-9 | Last Chance, Results-Liste, soft Exit | 1 Version |

### Email 1 Varianten (immer alle 5 erstellen)

| Variante | Stil | Laenge |
|---|---|---|
| A | Lang: full Pain-Liste plus Peer-Proof | ~200 Worte |
| B | Mittel: Pain plus Peer-Proof, kompakt | ~100 Worte |
| C | Kurz: pure Pain-Frage, minimal | ~70 Worte |
| D | Feedback-Angle: Research-Framing | ~100 Worte |
| E | Provokant-kurz: Shocking Stat als Hook | ~80 Worte |

## Step-by-Step

### Schritt 1: Niche-Intel zusammenstellen

Aus Asset Foundation CSV:
- [ ] **Niche-Name** und Marktgröße (Anzahl Betriebe in DE/DACH).
- [ ] **Entscheider-Rolle** (Inhaber, Geschäftsführer, Meister, Bezirksinhaber, VP, CTO).
- [ ] **Top 3 Pains** mit spezifischen Zahlen aus Rows 3-5 (Stunden, Euros, Prozente).
- [ ] **Ansprache** (Du oder Sie).
- [ ] **Industry-Jargon** aus Row 1 (WEG, ETV, Kehrbezirk, Stack-Begriffe).
- [ ] **Produktname plus was es tut** (Row 9, Solution / Vehicle).
- [ ] **Differentiator** aus Row 6 (was haben sie probiert und warum nicht funktioniert).

### Schritt 2: Header Block schreiben

```markdown
# Outbound: {Niche Name}

**Markt:** {X} Betriebe in DE | {Entscheider-Rolle} = Entscheider
**Ansprache:** {Du / Sie}
**Top Pain:** {Pain 1}, {Pain 2}, {Pain 3}
**Foundation Quelle:** asset-foundations-{venture}-{date}.csv, Niche {N}
```

### Schritt 3: Email 1, alle 5 Varianten

Pro Variante:
- **Betreff** (4-6 Worte, Pain-getrieben oder Stat-getrieben)
- Body
- Sign-off (gleich für alle Emails): `{SENDER_NAME}\n{COMPANY} | {DOMAIN}`

Key Elements je Variante:

**A (Lang)**: "Ich suche den Ansprechpartner..." → 4-Bullet Pain-Liste mit `→` → Peer-Proof Sentence → Fear Removal → Feedback-Frage → Soft CTA.

**B (Mittel)**: Pain-Summary in 2 Sätzen → Peer-Proof → "passt nicht bei jedem" → CTA.

**C (Kurz)**: Direkte Frage → 2-Satz Pain → Peer-Proof Oneliner → "10 Minuten?".

**D (Feedback)**: "Ich arbeite an einer Lösung für..." → Pain-Summary → Peer-Proof → "Ihr Feedback wäre wertvoll".

**E (Provokant)**: Stat im Subject → "Kennen Sie das?" → Number-heavy Pain → Peer-Proof → CTA.

### Schritt 4: Email 2 (Follow-up, ca. 100-150 Worte)

- Subject: `Re: {Email 1 Betreff}` (Reply-Threading)
- Acknowledge dass sie busy sind (niche-spezifisch: "als Meister sitzt man nicht am Rechner" / "als Verwalter hat man keine Zeit" / "als Founder bist du in 12 Investor-Calls die Woche").
- Eine kraftvolle Stat oder Peer-Quote.
- Konkrete Lösungsbeschreibung (was es konkret tut, NICHT Features).
- Upgrade CTA: "15 Minuten zeigen wie das konkret aussieht."

### Schritt 5: Email 3 (Breakup, ca. 80-120 Worte)

- "Zwei Nachrichten, keine Antwort, alles gut."
- Erwaehnung Pilot/Trial-Angebot wenn applicable (z.B. "90 Tage, kein Risiko").
- Results-Liste mit `→` Bullets: Zeit gespart, Geld gewonnen, spezifische Outcomes.
- Binary Close: "Falls nicht passt, melde mich nicht wieder. Falls doch, kurze Antwort oder {BOOKING_LINK}."

### Schritt 6: 5 alternative Subject Lines

Coverage:
- Pain-getrieben (Row 3-5)
- Stat-getrieben (Row 7 Trend oder Row 11 quantifizierter Benefit)
- Peer-Proof getrieben ("Wie [peer firm] X 60% reduzierte")
- Frage-getrieben ("11 Uhr abends Reconciliations?")
- Bodacious-Claim getrieben (Row 10)

### Schritt 7: Output

- Schreibe nach `{project-root}/outbound/outbound-{niche-slug}.md`.
- Optional: Sync zu Google Doc oder Push zu Repo.

## Quality Checklist

Vor Delivery:

- [ ] Kein "AI", "KI", "kuenstliche Intelligenz" irgendwo.
- [ ] Pain ist erwaehnt bevor irgendeine Lösung.
- [ ] Spezifische Zahlen (Stunden, Euros, Prozente) in jeder Email.
- [ ] Peer-Proof ("50+ Gespräche", "Betriebe in deiner Region", "{Peer Firm}").
- [ ] Fear Removal (deutsche Server, kein IT-Projekt, DSGVO).
- [ ] Soft CTA, nie "Jetzt kaufen" oder "Demo buchen" in Email 1.
- [ ] Korrekte Ansprache (Du/Sie) konsistent durch.
- [ ] Industry-Jargon korrekt verwendet.
- [ ] `{SENDER_NAME}` und `{BOOKING_LINK}` als Placeholder.
- [ ] Alle 5 Email-1 Varianten enthalten.
- [ ] Subject-Lines unter 6 Worten.
- [ ] Keine Em-Dashes, keine AI-Phrasen.

## Worked Example (illustrativ)

Für ein fiktionales Recruiting-Tech-Produkt (Recruitment Circle) Richtung DACH B2B SaaS Founder, Series-A. Lies für strukturelle Moves, nicht Content.

### Email 1, Variante A (Pain-led, ~180 Worte)

```
Betreff: Senior Engineer wieder weg?

Hi {First Name},

bei {Firma} jetzt seit {N} Jahren am Aufbau, und in den meisten DACH B2B SaaS
Series-A Teams die wir treffen kommt das gleiche Pattern hoch:

→ Drei Recruiter parallel und keiner versteht warum der Stack Rust ist
→ Senior-Hires die nach 8-14 Wochen wieder gehen, oft zur Series-B Bühne
→ Burn steigt, nächste Bridge taucht 9 Monate vor Plan auf
→ Der Founder zurück im HR-Stuhl statt im Produktstuhl

Wir machen vertical Tech-Recruiting für genau diese Pattern. Topgrading-basiert,
A-Player über Track Record statt Pedigree, 12 Monate Replacement-Garantie. Drei
Pilot-Teams haben in den letzten 18 Monaten 0 Fehl-Hires gehabt.

Server in Deutschland, kein IT-Projekt, DSGVO-konform.

Wie loest ihr Senior-Tech aktuell? Würde mich ehrlich interessieren auch wenn
ihr gerade nichts braucht.

LG {SENDER_NAME}
{COMPANY} | {DOMAIN}
```

### Email 1, Variante C (Kurz, ~70 Worte)

```
Betreff: 8 Wochen, dann weg?

{First Name}, kurz: wieviele Senior-Engineering-Hires habt ihr in den letzten
12 Monaten gemacht und wieviele sind noch da?

Wenn die Antwort weniger als 70 Prozent Retention ist, lohnt sich vielleicht
ein 10-Minuten-Call. Drei Series-A Teams sind bei 0 Fehl-Hires seit Wechsel.

LG {SENDER_NAME}
```

### Email 1, Variante E (Provokant-kurz, ~80 Worte)

```
Betreff: 30% Senior-Hire Fluktuation in DACH SaaS

{First Name},

das ist die Marktdurchschnitts-Quote in Series-A. Bei {Firma} wahrscheinlich
auch nicht weit weg. Drei Pilot-Teams mit unserem Vertical-Recruiting sind
bei unter 5 Prozent. Topgrading + 12 Monate Garantie.

Mit oder ohne uns: das Problem geht nicht weg solange ihr Standard-Recruiter
nutzt die euren Stack nicht verstehen.

15 Minuten? {BOOKING_LINK}

LG {SENDER_NAME}
```

### Email 2 (Follow-up, Tag 4, ~120 Worte)

```
Betreff: Re: Senior Engineer wieder weg?

{First Name}, kurze Nachfasser. Spezifischer Punkt der bei den meisten Series-A
CTOs und Foundern ankommt:

Unser Topgrading-Filter eliminiert 80-90 Prozent der Profile bevor sie auf
deinem Tisch landen. Die übrig gebliebenen 10-20 Prozent sind die wo ein
20-Minuten-Gespräch sich lohnt. Punkt der gesamten Architektur: wir versuchen
nicht euer Hiring zu ersetzen, wir stoppen euch von 80 Prozent unprofitabler
Gespräche.

Wenn der Timing gerade nicht passt, vollkommen okay. Wenn der Wert nicht
durchkommt, würde ich gerne wissen was fehlt. Schriftliche Antwort reicht,
kein Call nötig.

LG {SENDER_NAME}
```

### Email 3 (Breakup, Tag 9, ~80 Worte)

```
Betreff: Letztes Mal

{First Name}, letzter Mail. Gehe davon aus dass es gerade nicht passt. Stoppe
hier damit ich nicht im Weg bin.

Falls sich was aendert in den nächsten 6-12 Monaten, du weißt wo du mich
findest. Und falls du jemanden in deiner Peer-Group kennst der besser passt,
freu mich über Intro jederzeit.

LG {SENDER_NAME}
```

### 5 alternative Subject Lines für A/B Test

```
Subject 1 (Pain):       Senior Engineer wieder weg?
Subject 2 (Stat):       30% Senior-Hire Fluktuation in DACH SaaS
Subject 3 (Peer):       Wie {Peer Firm} 0 Fehl-Hires hatte
Subject 4 (Frage):      Wie loest ihr Senior-Tech?
Subject 5 (Claim):      18 Monate Retention oder kostenlos
```

### Was das Beispiel zeigt (strukturelle Moves)

- **Subject Lines nennen Pain in ihren Worten** ("Senior Engineer wieder weg") nicht generisch ("Quick Question").
- **Zwei Opener-Varianten testen verschiedene Winkel** (Pain-led vs Stat-led vs Peer-Social-Proof). Sende jede an Drittel der Liste, vergleiche Reply-Rate.
- **Vertical-Spezifität** ("DACH B2B SaaS Series-A 20-80 Mitarbeiter") rechtfertigt den Inbox-Platz. Generisches Outbound stirbt am Opener.
- **Email 2 führt konkreten Mechanismus ein** (Topgrading-Filter 80-90 Prozent Eliminierung). Move von "wir haben was" zu "hier ist warum es für deinen Workflow funktioniert".
- **Email 3 (Breakup) ist ehrlich, low-pressure, fragt nach Referral**. Höchst-yieldendes Cold-Breakup-Pattern in B2B.

## Anti-Patterns

- **Email öffnet mit "Ich hoffe es geht Ihnen gut".** Sofort Trash-Flag. Öffne mit spezifischer Beobachtung über ihre Welt, nicht Niceness-Ritual.
- **Produkt erwaehnt vor Paragraph 2.** Macht Email pitch-shaped vom ersten Satz. Prospect-Hirn pattern-matched "Werbung" und stoppt Lesen.
- **Generische Personalisations-Tokens ohne echte Spezifität.** `{Company}` täuscht niemand. Entweder mit echter Referenz personalisieren (ihr Post, ihr Hire, ihr Funding) oder Variable weglassen.
- **Tag-1 CTA fragt nach 30-Min Demo.** Eskalator zu steil. Tag-1 CTA ist Yes/No-Frage oder 5-Zeilen Content-Share. Demo-Close ist Email 3 frueheste.
- **Subject Lines über 6 Woerter.** Phone Preview cuts. 4-6 Worte, am Ende der höchste Curiosity-Load.
- **Email 2 ohne Referenz auf Email 1.** Fühlt sich an wie frischer Cold Blast. Immer threaden zur vorherigen Sendung damit Prospect Continuity sieht, nicht Noise.

## Customization Checklist

Bevor verwendet, ersetze:
- `{SENDER_NAME}` mit Sender-Person
- `{COMPANY}` mit Firma-Name
- `{DOMAIN}` mit Domain
- `{BOOKING_LINK}` mit Calendly oder Booking
- `{PRODUCT_NAME}` mit Produkt-Name

## Hand-off (Foundation Konsumption)

| Foundation Row | Wo es in Outbound fliesst |
|---|---|
| Row 1 (Position) | Email 1 Opener-Detail (Industry, Standort, Größe-Referenz) |
| Row 2 (Deepest Desires) | Email 1 Subject-Variation, Email 3 Results-Liste |
| Rows 3-5 (Pain Layer) | Email 1 Body verbatim wo möglich, vor allem Variante A und C |
| Row 6 (Tried but Failed) | Email 2 "warum das anders ist" |
| Rows 7-8 (Trends + CoI) | Subject Variante "Stat", Email 2 Urgency |
| Row 9 (Vehicle) | Email 1 Solution Sentence, Email 2 Konkretisierung |
| Row 10 (Bodacious Claim) | Subject Variante "Claim", Email 3 Headline |
| Rows 11-12 (Benefits) | Email 3 Results-Liste mit Bullets |

Run `asset-foundations/SKILL.md` first wenn CSV nicht existiert.

## Voice Rules

Output mit echten Umlauten ä ö ü ß. Keine Em-Dashes. Keine AI-Phrasen. Keine Enthusiasmus-Floskeln. Subject Lines unter 6 Worten. Kein "Ich hoffe es geht Ihnen gut" Opener jemals.
