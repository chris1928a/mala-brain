---
name: gtm-ads
description: >
  Erzeugt Meta (Facebook/Instagram) und Google Ads Varianten aus Customer-
  Transkripten. 10 Hooks plus 5 Bodies plus 5 CTAs in der Sprache des Kunden,
  plus "do not use" Liste mit Insider-Jargon der im Feed nicht funktioniert,
  plus Creative Brief für Visuals.

  Verwende bei: Meta Ads, Facebook Ads, Instagram Ads, Google Ads, Search Ads,
  Performance Max, PMax, Display Ads, Hook Body CTA, Ad-Varianten aus Calls,
  Ad Copy, Werbeanzeigen, Anzeigentexte, Werbetexte, Creative Brief, "schreib
  mir Ads aus den Calls", "Ads für Niche X", "Meta Kampagne aus Foundation",
  "Hook Variation Test".
---

# Ads from Customer Transcripts

## Voraussetzung

Asset Foundation CSV für die Niche existiert. Alternativ: 5+ Customer-Interview-Transkripte. Wenn nichts da ist: erst `asset-foundations/SKILL.md`.

## Wann ausführen

- Du startest eine Meta-, Facebook-, Instagram- oder Google-Ad-Kampagne.
- Du hast 5+ Customer-Interviews oder Stack von Sales-Call-Transkripten.
- Du willst Ad-Copy die nach deinem Kunden klingt, nicht nach deinem Marketing-Team.

## Inputs

1. **5-20 Customer-Interview-Transkripte oder Sales-Call-Transkripte oder schriftliche Testimonials**. Roher und laenger ist besser.
2. **Produkt / Offer Oneliner** was beworben wird.
3. **Target Audience Definition**: Wer sieht die Ad (Demographics, Interests, Behaviors, Custom Audiences).
4. **Landing Page URL oder Headline** damit Ad-Copy zur Click-Destination matcht.
5. **Desired Conversion Event**: Lead-Form, Kauf, Trial-Signup, Book-a-Call, Newsletter-Signup.
6. **Plattform**: Meta (Facebook + Instagram + Reels) oder Google (RSA Search, Display, PMax) oder beides.

## Output

Ein Markdown-Dokument mit:

1. **10 Hooks**: Erste 3-7 Worte die Scroll stoppen. Aus echten Customer-Quotes wo möglich.
2. **5 Ad Bodies**: Jede 40-90 Worte, in Customer-Voice, endet mit klarem CTA.
3. **5 CTA-Varianten**: Direct, Benefit-led, Soft-Invite, Urgency, Specific.
4. **"Do not use" Liste**: Worte oder Phrasen die im Call okay sind aber im Feed sterben (Industry-Jargon, Insider-Language).
5. **Creative Brief**: Was Visuals zeigen sollen, basiert auf Kontext den Customers beschrieben haben.
6. **Plattform-Mapping**: Welche Hook/Body/CTA-Combo für welches Format (Image, Carousel, Video, RSA, Display, PMax).

## Step-by-Step

### Schritt 1: Transkripte minen

Pull diese vier Quote-Kategorien:

- **Problem Statements**: Wie der Kunde den Pain in eigenen Worten beschreibt. Extrahiere 20-30.
- **Failed Attempts**: Was sie probiert haben und warum es nicht funktionierte. Extrahiere 10-15.
- **Outcome Language**: Wie sie das Leben nach dem geloesten Problem beschreiben. Extrahiere 10-15.
- **Surprise Moments**: Wo sie realisierten dass dein Produkt die Antwort ist. Extrahiere 5-10.

### Schritt 2: Hooks aus Problem-Statements bauen

Hook-Regeln:

- 3-7 Worte.
- Spezifische Zahl oder konkretes Nomen.
- Ich-Form wenn möglich ("Ich kriege es nicht hin...", "Mein Team haut staendig...").
- Wenn Hook zu jedem Produkt der Kategorie passen könnte: rewrite.

Bau 10. Variiere zwischen:
- Direkter Pain-Quote
- Stat-led Hook
- Frage-Hook
- Pattern-Interrupt Hook (Anti-These zu Common Belief)

### Schritt 3: Bodies bauen

Jede Body folgt:
1. Das Problem (Customer-Worte).
2. Der Failed Attempt (was sonst probiert).
3. Der Pivot (was tatsaechlich funktioniert).
4. Der CTA (konkreter nächster Schritt, gemtached zum Conversion-Event).

Schreib 5. Variiere Opening: einige starten mit Pain, einige mit Frage, einige mit Zahl.

### Schritt 4: CTA-Varianten testen

Fuenf Varianten:
- **Direct Command**: "Demo buchen."
- **Benefit-led**: "In Aktion sehen."
- **Soft Invite**: "Mal schauen ob's passt."
- **Urgency**: "Nur diesen Monat."
- **Specific**: "15 Min mit dem Founder kostenlos."

### Schritt 5: "Do not use" Liste

Aus Transkripten identifizieren Worte oder Phrasen die:
- Industry-Jargon sind den nur Insider verstehen.
- Meta-Policy-Filter triggern (Health Claims, Financial Promises).
- Im Gespräch natuerlich klingen aber im Text awkward sind.

### Schritt 6: Creative Brief

Aus Kontext der Transkripte beschreiben:
- **Setting**: Office, Kueche, Baustelle, Auto, Standup-Meeting, Investor-Call.
- **Emotional State**: frustriert, erleichtert, skeptisch, confident.
- **Object oder Screen**: Auf was schaut der Kunde, was hat er in der Hand, welcher Bildschirm, welche App.

### Schritt 7: Plattform-Mapping

| Format | Hook-Stil | Body-Laenge | CTA |
|---|---|---|---|
| Meta Image (Static) | Pain-Quote oder Stat | 30-60 Worte | Direct oder Benefit |
| Meta Carousel (3-5 Cards) | Pain → Failed → Pivot → Benefit → CTA Storyflow | 8-12 Worte/Card | Specific |
| Meta Reels / Video | Pattern-Interrupt | 50-80 Worte voiceover | Soft-Invite |
| Google RSA Headline | Bodacious Claim Sub-Worte | n/a | n/a (Click) |
| Google Display | Pain-Statement | 30 Char | Direct |
| Google PMax Asset Group | Mix aller Hooks plus Bodies | mehrere | mehrere für Algorithm Test |

## Quality Bar

- Ein Scroller der dich nicht kennt versteht die Ad in 3 Sekunden.
- Jeder Hook und jede Body traced zurück zu spezifischer Transkript-Linie.
- Nichts ist erfunden. Wenn keine Source da: cut.
- CTAs matchen die Landing Page exakt.

## Plattform-Spezifika

### Meta (Facebook, Instagram, Reels)

- Hook-Laenge: 3-7 Worte first line, dann Cut bei "Mehr anzeigen".
- Visual: niche-spezifisch, kein Stock. Reels ohne Caption verlieren 60% Watch-Time.
- Audience: Lookalike auf Customer-List bessere als Interest-Targeting für B2B SMB.
- Compliance DACH: keine Health-Claims, keine Financial-Promises ohne Disclaimer, GDPR-konformer Lead-Form mit klarem Consent.

### Google (Search, Display, PMax)

- RSA: 15 Headlines, 4 Descriptions. Pflicht-Variation. Bodacious Claim als Headline 1, Pain als Headline 2, Vehicle als Headline 3.
- PMax: Asset Group pro Niche, kein gemischtes Mass-Audience.
- Quality Score-Drivers: Headline Match-zur-Query, Landing Page Relevance, CTR.
- DACH: Bot-Traffic in deutschen Search Ads ist hoch, regelmäßig negative Keywords pflegen (Stellenangebot, Job, Gehalt wenn nicht relevant).

## Worked Example (illustrativ)

Für ein fiktionales Recruitment-Circle-Asset zur Niche "DACH B2B SaaS Series-A Founder". Lies für strukturelle Moves.

### Drei Hook-Varianten (alle drei testen, Verlierer killen)

```
Hook A (Pain-Quote, mirrors Customer-Language):
"Vier Senior-Hires in einem Jahr. Drei sind weg.
Ich habe das Unternehmen gegründet um nicht der HR-Mensch zu werden."

Hook B (Stat-led):
"30 Prozent Senior-Hire-Fluktuation ist Marktdurchschnitt.
Drei Series-A Teams sind bei null."

Hook C (Pattern-Interrupt, Anti-These):
"Die meisten Series-A Founder denken sie brauchen mehr Recruiter.
Sie brauchen weniger. Aber bessere."
```

### Body (eine Variante, ~70 Worte)

```
Drei Recruiter parallel und keiner versteht warum euer Stack Rust ist.
Topgrading-basiertes Vertical-Recruiting für DACH B2B SaaS hat genau das
Problem geloest. Drei Series-A Pilot-Teams. 18-24 Monate Senior-Retention.
12 Monate Replacement-Garantie. Server in Deutschland, kein IT-Projekt.

Wenn ihr über Series-B redet aber Senior-Hiring euch zurückhaelt:

15 Minuten mit dem Founder. Kein Pitch.

{Founder Name}, Recruitment Circle
```

### CTA-Varianten

```
CTA A (Direct):       "15 Min Founder-Call buchen"
CTA B (Benefit):      "Vertical-Recruiting in Aktion sehen"
CTA C (Soft):         "Mal schauen ob's bei uns passt"
CTA D (Urgency):      "3 Pilot-Plaetze für Q3 frei"
CTA E (Specific):     "Topgrading-Filter live testen"
```

### "Do not use" Liste (Schritt 5 Output)

- Generische HR-Tech-Worte: "Hire fast", "scale your team", "world-class talent". Customers haben das nie gesagt.
- Process-Sprache: "proprietary methodology", "AI-driven matching algorithm". Customer interessiert sich für Outcomes, nicht Method-Names.
- Alles was in einer Stock-Photo-Recruiter-Werbung sein könnte. Wenn die gleiche Ad mit anderem Logo auch laufen könnte: kill.
- Buzzwords: "synergy", "leverage", "unlock potential", "harness AI". Sofort Trash-Flag.

### Creative Brief (Schritt 6 Output)

```
Setting:        Founder am Schreibtisch in Co-Working Space oder Home Office,
                Laptop mit Slack/Linear offen, Phone am Ohr (Call), Coffee-Mug,
                Kalender-View mit 11 Calendly-Slots dichten Tag.

Emotional:      Genervt aber nicht panisch. "Schon wieder das" Energy.

Object:         Slack-Channel mit "Hiring" Notifications. LinkedIn-Tab mit
                Recruiter-Message. Calendly-View mit Senior-Engineer-Loop
                Slots. Phone mit Investor-Call-ID.

Avoid:          Stock-Suit-Office-Bilder. High-Five Team Shots. "Diversity
                Lookbook" Stock. Whiteboard mit "STRATEGY" geschrieben.
```

### Was das Beispiel zeigt (strukturelle Moves)

- **Jeder Hook ist verbatim oder near-verbatim aus Customer-Call.** Hook A ist direkter Quote. Hook C ist Pattern-Interrupt der Customer-Belief negiert. Keiner erfindet Emotion die nicht gesagt wurde.
- **Die Body ist eine einzelne Customer-Story mit konkretem Recognition-Moment**: "drei Recruiter parallel die Stack nicht verstehen". Konkret, zeitgebunden, falsifizierbar.
- **CTAs laddern Commitment**: Soft → Specific → Urgency. Test alle, gewinnender CTA paart mit gewinnendem Hook.
- **"Do not use" Liste ist genauso wichtig wie Ad-Copy.** Die meisten gescheiterten Meta Ads sterben an Industry-Cliche-Vocabulary das Customer nie nutzte.

## Anti-Patterns

- **Hooks abstrakt** ("Unlock your potential"). Rewrite bis konkret.
- **Body klingt wie Landing Page.** Rewrite in Ich-Form mit Transkript-Sprache.
- **Keine "do not use" Liste.** Du shippst Jargon by accident.
- **Creative Brief geskippt.** Stock Images killen Ad-Performance.
- **Hook und CTA mismatch.** Wenn Hook Pain ist, CTA soll Relief versprechen, nicht "Demo buchen".
- **Jede Niche kriegt gleiche Ad.** Funktioniert nicht. Ein Foundation-Run pro Niche, ein Ad-Set pro Niche.

## Hand-off (Foundation Konsumption)

| Foundation Row | Wo es in Ads fliesst |
|---|---|
| Row 1 (Position) | Audience-Targeting, Creative-Brief Setting |
| Row 2 (Deepest Desires) | Hook-Varianten "Outcome", Body Schluss |
| Rows 3-5 (Pain Layer) | Hook-Varianten "Pain", Body Opening |
| Row 6 (Tried but Failed) | Body Failed-Attempt-Section, "do not use" Inspiration |
| Rows 7-8 (Trends + CoI) | Hook-Varianten "Stat", Urgency-CTA |
| Row 9 (Vehicle) | Body Pivot, CTA Specific |
| Row 10 (Bodacious Claim) | Hook-Varianten "Bold Claim", Google RSA Headline 1 |
| Rows 11-12 (Benefits) | Body Outcome, Creative-Brief Emotional State |

## DACH-Compliance

- **Datenschutz**: Lead-Form mit klarem Consent, kein Custom-Audience-Upload ohne Einwilligung.
- **Health/Finance/Recruiting**: kein Versprechen das Meta-Policy-Filter triggert ("guaranteed", "100% effective", "make money fast").
- **Recruiting-spezifisch**: Stellenanzeigen vs Werbung sauber trennen. Wer "Recruiting-Ad" schaltet ist nicht "Stellenanzeige" schalten, das hat unterschiedliche Compliance-Anforderungen.
- **B2B vs B2C**: B2B in Meta heißt Lookalike-Audience aus Customer-CRM, nicht Interest-Targeting. Interest-Targeting funktioniert in DACH B2B sub-optimal.

## Tracking

- Hook A/B/C: Reply-Rate, Click-Rate, CPL, CPM nach 3-5 Tagen Test.
- Body: Time-on-Landing-Page, Scroll-Depth, Form-Conversion.
- CTA: Click-to-Form-Submit Rate, Form-Completion-Rate.
- Verlierer killen, Gewinner skalieren. Niemals Hook und Body und CTA gleichzeitig changen, sonst weiß du nicht was wirkte.

## Voice Rules

Output mit echten Umlauten ä ö ü ß im finalen Ad-Text. Keine Em-Dashes. Keine "KI" oder "AI" in Hooks oder CTAs. Customer-Voice in Hooks und Body, nicht Marketing-Voice. Keine generischen HR-Tech / SaaS-Tech Buzzwords.
