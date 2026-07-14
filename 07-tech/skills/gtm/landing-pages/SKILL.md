---
name: gtm-landing-pages
description: >
  Erzeugt Niche-spezifische HTML Landing Pages plus zweite Signup-Page mit
  progressiver Email-Capture. Pain-First Hero, deutsche SMB-Optik, "kein
  IT-Projekt / kein technisches Wissen" Sprache, DSGVO-konforme Daten-Strecke.

  Verwende bei: Landing Page bauen, LP für Niche, Hero Section, Pain Story,
  Signup-Flow, progressive Email-Capture, Hook Page, Sales Page, "schreib
  mir Landing Page für X", "LP für recruitmentcircle.de", "Hook Page für
  Ads-Traffic", "bessere Conversion auf bestehender Page".
---

# Landing Page Builder

## Voraussetzung

Asset Foundation CSV für die Niche existiert. Wenn nicht: `asset-foundations/SKILL.md` zuerst.

## Output

Zwei HTML-Files:
- `{niche}.html` (Landing Page mit Hero, Pain, Features, Social Proof, Exit-Popup)
- `{niche}-signup.html` (Signup-Flow mit progressiver Email-Capture)

Single HTML Files, kein Build-Tool, Google Fonts (DM Sans + Caveat), CSS-Variablen für Theming, IntersectionObserver für Scroll-Animations, Mouseout für Exit-Intent.

## Architektur

- **Page 1**: `{niche}.html` ist die Conversion-Page mit Hero, Pain Story, Stats, Features, How-It-Works, Daily Example, Case Study, Testimonials, Objection-FAQ, Comparison, Guarantee, Team, Exit-Popup.
- **Page 2**: `{niche}-signup.html` ist der Signup-Flow mit Email-First-Capture und progressiv aufgebauten Datenfeldern. Email triggert Backend bei Step 1 sofort, alles andere ist optional.

## Step-by-Step

### Schritt 1: Top-Pains der Niche recherchieren

Aus Asset Foundation Rows 3-5 plus optional Web-Recherche:
- Top 5 größte Pains der Zielgruppe.
- Quellen: YouTube-Kommentare, Branchenstudien, Foren, Innungen, LinkedIn-Posts in der Niche.
- **Hard Data Points** (Prozente, Costs, Stunden) sind die Basis für Stats-Bar und Hooks.
- Frage: Was haelt den Geschäftsführer nachts wach? Was ist die Number-1 Beschwerde?

### Schritt 2: Hook (Hero-Section)

- **Urgency Badge**: Lead mit der schockierendsten Stat (z.B. "73% nennen Fachkraeftemangel als #1 Problem").
- **Headline**: Pain in konkreten Zahlen, dann Versprechen: "So loesen es die Besten der Branche."
- **Sub-Headline**: Top 2-3 Pains explizit. Emphasize: kein IT-Projekt, kein technisches Wissen, aus der Branche.
- **CTA**: Curiosity-driven, NICHT Produkt-driven. Pattern: "Jetzt herausfinden wie [Niche] unter [Größe] [Pain] loesen."
- **Trust Line**: "Kein IT-Projekt | Kein technisches Wissen nötig | Von [Niche] für [Niche] | Server in Deutschland."

### Key CTA-Prinzipien

- **Treibe Neugier, nicht Pitch**: "Jetzt herausfinden wie..." nicht "Kostenlos testen".
- **Keine AI-Sprache**: "Automatisierung", "Entlastung", "Assistent" statt "KI" oder "AI".
- **Frame als Geheim-Wissen**: "Wie es die Besten machen" laesst Leute hinter den Vorhang schauen wollen.
- **Low Commitment**: "herausfinden", "ansehen", "erfahren" statt "anfragen", "buchen", "kaufen".

### Schritt 3: Pain Story Section

- Schreibe eine Narrative "Montagmorgen" Story mit echtem Daily-Pain der Niche.
- Spezifische Szenarien (Namen, Adressen, Situationen).
- Ende mit Pullquote der den emotionalen Kern fasst.
- Transition: "Trotzdem gibt es [Niche] die es anders machen..."

### Schritt 4: Stats Bar

- 4 Datenpunkte aus Recherche, mit Quellen zitiert.
- Schockierendste oder relateableste Zahlen.
- Format: Big Number plus kurze Erklärung.

### Schritt 5: Feature Cards (Pain-Driven)

- 6 Cards, jede benannt nach einem PAIN der geloest wird (nicht nach einem Feature).
- Pattern: "[Pain] baendigen / beenden / im Griff" nicht "AI Email Triage".
- Pro Card: Pain Description plus Vorher / Nachher Vergleich.
- Echte Industry-Terminologie die Niche taeglich verwendet.

### Schritt 6: How It Works

- 4 simple Steps: Check machen → Gespräch → Verbinden → Läuft.
- Emphasize: kein IT, kein technisches Wissen, kein Team-Training nötig.
- Position Founder als "selbst Unternehmer", nicht "Tech Expert".

### Schritt 7: Daily Example / Chat Mock

- Zeige realistische Morning-Briefing Konversation.
- Niche-spezifische Szenarien (z.B. WEGs für Verwalter, Feuerstaetten für Schornsteinfeger, Tickets für SaaS Founder, Pipeline für Sales-Leader).
- Soll sich anfühlen wie "jemand hat schon meine Morgen-Arbeit gemacht".

### Schritt 8: Case Study ("Stell dir vor")

- Aspirationale Narrative: Wie ein guter Tag mit dem Produkt aussieht.
- Ende mit 4 Result-Boxen (Zeit gespart, Tasks automatisiert, keine Systemwechsel, dein Tempo).

### Schritt 9: Testimonials

- 3 Testimonials: 2 aus der Niche, 1 cross-Niche für Credibility.
- Frame als Operational Relief, NICHT Technology Praise.

### Schritt 10: Objections (FAQ)

- 5-6 Objections, reframed aus Niche-Perspektive.
- Lead mit "Ich bin kein Technik-Mensch" - immer der #1 Fear.
- Adressieren: Implementation-Zeit, Datenschutz, falsche Aktionen, Kompatibilitaet mit existierender Software.

### Schritt 11: Comparison (Produkt vs Klassisch)

- Side-by-side: "Klassische Software" vs "{Produkt}".
- Emphasize: keine Migration, kein Training, kein Team-Involvement.

### Schritt 12: Guarantee

- 90-Tage Pilot, null Risiko.
- "10 Pilotplaetze" erzeugt Knappheit (nur wenn echt).

### Schritt 13: Team Section

- Frame Founder als Industry-People, NICHT Tech-People.
- "Selbst Unternehmer, verwaltet eigene [Objekte/Betrieb]."
- "In Familienbetrieb aufgewachsen" relate zur Audience.

### Schritt 14: Exit-Intent Popup

- "5 Fehler die [Niche] unter [Größe] am meisten kosten."
- Pain-fokussierte Mistakes (auf Personal warten, große Software-Projekte, denken Automation ist nur für große Firmen).
- CTA: gleicher Curiosity-driven Pattern.

### Schritt 15: Signup Page bauen (Progressive Capture)

**Flow: Email wird IMMER zuerst gecaptured.**

| Step | Felder | Pflicht? | Skip? |
|---|---|---|---|
| 1 | Email + Name | Email only | Nein |
| 2 | Telefon | Nein | Ja |
| 3 | Position + Teamgröße | Nein | Ja |
| 4 | Quiz: Org-Größe | Klick = Advance | Auto |
| 5 | Quiz: Größter Zeitfresser | Klick = Advance | Auto |
| 6 | Quiz: Was hielt euch zurück | Multi-Select | Submit |

**Key Rules:**

- Email feuert ans Backend SOFORT bei Step 1.
- `beforeunload` saved was bisher gecaptured wenn Tab geschlossen wird.
- Keine Pflichtfelder ausser Email, nichts blockiert den Flow.
- Enter-Taste funktioniert auf jedem Step.
- Success-Screen zeigt Booking-Link (z.B. Calendly).
- Landing Page muss zu `{niche}-signup.html` linken in allen CTAs.

## Sprach-Regeln

- Deutsch (Du-Form oder Sie-Form je nach Niche), professionell aber warm.
- KEIN "AI", "KI", "kuenstliche Intelligenz" in Headlines oder CTAs.
- Stattdessen: "Automatisierung", "Entlastung", "Assistent", "übernimmt für dich".
- Industry-Jargon: nutze die exakten Begriffe der Niche (WEG, ETV, Kehrbezirk, Angebot, Ticket, Pipeline).
- Pain-First, Solution-Second in jeder Section.

## Worked Example (illustrativ)

Für ein fiktionales Recruitment-Circle-LP zur Niche "DACH B2B SaaS Series-A Founder". Lies für strukturelle Moves.

### Hero (Schritt 2 Output)

```
Badge:        78% der Series-A B2B SaaS Founder verlieren mindestens
              einen Senior-Hire pro Jahr in den ersten 14 Wochen.
              Branchendaten DACH.

Headline:     Senior Engineering darf nicht jeden Quartal von vorne anfangen.
              So loesen es die Series-A Teams die ihre Roadmap halten.

Sub-Line:     Kein neues Tool für dein Team. Kein IT-Projekt.
              Topgrading-basiertes Vertical-Recruiting für DACH B2B SaaS.
              Server in Deutschland.

CTA:          Jetzt herausfinden wie 12 Series-A Teams ihre Senior-Retention
              auf 95 Prozent gehoben haben.

Trust:        Kein IT-Projekt | Kein technisches Wissen nötig
              Von Founder für Founder | Server in Deutschland
```

### Pain Story (Schritt 3 Output)

> Donnerstagmorgen, 9:15. Du startest in den vierten Senior-Engineer-Loop in
> 12 Monaten. Drei Recruiter haben Profile geliefert. Keiner hat verstanden
> warum euer Stack Rust ist und nicht Python. Du sitzt zwischen Investor-Call
> und Produkt-Review und jonglierst Calendly-Slots für Profile die nach
> Jahresgehalt fragen, nicht nach Mission. Vor zwei Wochen hat dein
> Lead-Architekt zurückgezogen. Burn steigt. Series-B Window schließt sich.
>
> *"Ich habe das Unternehmen gegründet um nicht der HR-Mensch zu werden.
> Und jetzt bin ich's wieder."*

Trotzdem gibt es Series-A Teams die das anders loesen.

### Was das Beispiel zeigt (strukturelle Moves)

- **Stat-led Hero** mit konkretem Prozentwert und zitierter Quelle.
- **Niche-spezifisches Szenario**: Senior-Engineer-Loop, Stack-Rust, Investor-Call, Calendly. Prospect erkennt seine Welt im ersten Absatz.
- **Pullquote**: Customer-Voice in italics endet die Pain-Section.
- **CTA ist Curiosity, nicht Sale**: "Jetzt herausfinden..." nicht "Demo buchen".
- **Trust Line** adressiert die drei größten Aengste der Niche explizit: technische Komplexität, fremde Software, Datenort.

## Anti-Patterns

- **Hero-Copy redet über Produkt, nicht über Pain des Prospects.** Hero-Headline muss echo'n was der Prospect schon sagt, nicht wie dein Team das Feature nennt.
- **Stock-Bilder statt Niche-spezifischer Szenarien.** Eine Recruiting-Page mit Stock-Office-Photos konvertiert schlechter als die gleiche Page mit echtem Founder-Standup.
- **Mehr als ein primaerer CTA auf der Page.** Hirn friert ein wenn es waehlen muss. Ein Headline-CTA, ein sekundaerer, kein dritter.
- **Signup-Form mit mehr als 3 Pflichtfeldern beim ersten Capture.** Jedes Extra-Feld schneidet Conversion ca 7%. Email zuerst, alles andere kommt später.
- **Kein Commitment-Ladder hinter "Mehr erfahren".** "Mehr erfahren" ist kein CTA, ist Stall. Immer eskalieren zu Datum, Download oder Calendar-Slot.
- **Long-Form Copy ohne scannbare Subheadings.** Reader sind weg in 8 Sekunden ohne Subheadings. Subheadings lassen sie sich selbst qualifizieren.

## Technical

- Single HTML Files, kein Build-Tool.
- Google Fonts: DM Sans + Caveat.
- CSS-Variablen für Theming (Accent-Color pro Niche swappen falls nötig).
- Scroll-Animations via IntersectionObserver.
- Exit-Intent via Mouseout auf Document.
- Form-Daten loggen zu Console mit TODO für Webhook-Endpoint.
- Booking-Link als Placeholder: `{BOOKING_LINK}`.

## File Naming

- `{niche}.html` Landing Page
- `{niche}-signup.html` Signup-Flow
- Storage: `{project-root}/landing-pages/`

## Customization Checklist

Vor Verwendung ersetzen:
- `{PRODUCT_NAME}`
- `{BOOKING_LINK}`
- `{FOUNDER_NAME}`
- `{DOMAIN}`
- `{WEBHOOK_URL}` (Form-Submission Endpoint, z.B. Zapier, Make, custom API)

## Hand-off (Foundation Konsumption)

| Foundation Row | Wo es in LP fliesst |
|---|---|
| Row 1 (Position) | Sub-Headline Niche-Description, Trust-Line Geographie |
| Row 2 (Deepest Desires) | Headline (mapped auf Row 10), Daily-Example aspirational Frame |
| Rows 3-5 (Pain Layer) | Pain Story, direkte Quotes als Pullquotes |
| Row 6 (Tried but Failed) | Comparison Section, Objection FAQ |
| Row 7 (Trends) | Stats Bar, Urgency Hint |
| Row 8 (Cost of Inaction) | Exit-Popup Mistakes, Time-Sensitive Framing |
| Row 9 (Vehicle) | How-It-Works, Comparison Right Column |
| Row 10 (Bodacious Claim) | Headline, Guarantee-Section Headline |
| Row 11 (Secondary) | Stats Bar Numbers, Feature Cards Outcomes |
| Row 12 (Auxiliary) | Daily-Example identity-level, Case Study Schluss |

Run `asset-foundations/SKILL.md` first wenn CSV nicht existiert.

## Voice Rules

Deutsche Umlaute ä ö ü ß im finalen HTML. Keine Em-Dashes. Keine AI-Phrasen ("KI", "AI", "kuenstliche Intelligenz"). Pain-First Sprache. Sie-Form bei formalen Niches, Du-Form bei informalen Niches.
