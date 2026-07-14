---
name: gtm-asset-foundations
description: >
  Erzeugt das 12-row Asset Foundations CSV pro Niche aus Call-Transkripten.
  Quelle des kompletten GTM Funnels. Dan Kennedy Sales Letter Spine. Output
  ist Pflicht-Input für landing-pages, outbound und ads Sub-Skills.

  Verwende bei: Asset Foundations bauen, 12-row CSV, ICP aus Calls, Niche
  definieren, Pain Mining, Customer Voice Extraction, Bodacious Claim
  formulieren, Foundation für Funnel, Dan Kennedy Spine, Position-Desire-Pain
  Stack, Call-Transcripte zu Foundation umwandeln.
---

# Asset Foundations Builder

## Kern

Du kannst keine Conversion-Copy schreiben bevor du die Foundation gemacht hast. Das CSV ist die Quelle, alles andere ist Ableitung. Eine Spalte pro Niche, 12 Reihen pro Spalte, jede Zelle aus dem Transkript zitiert oder mit `[unbekannt]` markiert. Null Erfindung.

## Wann ausführen

- Du hast Call-Aufnahmen oder Transkripte (Sales, Qualification, Design-Partner Interviews, Customer Success). Ein gut qualifizierter Call funktioniert. Fuenf bis zehn ist solide. Zehn bis zwanzig macht das Foundation kompoundierend stark.
- Du bist im Begriff Conversion-Copy zu schreiben (Landing Page, Email, Ad, Sales Script).
- Deine Positionierung fühlt sich generisch an und du sprichst über den Kunden statt als der Kunde.

## Inputs

1. **Transkripte**: Plain Text, Markdown oder VTT. Multiple Files okay. Anonymisieren wenn Output extern geteilt wird.
2. **Qualification Question Set**: Die Fragen die du im Discovery Call stellst. Wenn keins existiert, draftet der Skill eine aus BANT, MEDDIC, Mom Test und gibt sie zur Review.
3. **Niche Hypothese (optional)**: Wenn du 3-5 Buyer Segmente vermutest, nenne sie. Sonst clustered der Skill die Transkripte und schlaegt Niches vor.

## Output

CSV (Paste-Ready in Google Sheets oder Excel):

| Field | Niche 1 | Niche 2 | Niche 3 |
|---|---|---|---|
| Position (Standort, Einkommen, Teamgröße, Budget, Vertical, Job-Title, Familienstand, Jahre in Position) | | | |
| Deepest Desires des Prospects | | | |
| Was haelt sie nachts wach, Augen offen, Decke anstarrend? | | | |
| Worüber sind sie frustriert? Warum? Wie fühlen sie sich? | | | |
| Worüber sind sie verärgert? Warum? | | | |
| Was haben sie probiert und ist gescheitert? | | | |
| Welche Trends laufen im Markt? Wie schadet das wenn sie nicht adaptieren? | | | |
| Was passiert wenn sie nichts ändern? Wieviel Zeit haben sie? | | | |
| Solution / Vehicle | | | |
| Bodacious Claim (welche Behauptung trifft Row 2 ins Mark?) | | | |
| Secondary Benefits (welche anderen Metriken werden bewegt? Welche Frustrationen verschwinden? Wieviel Zeit bei welcher Taetigkeit?) | | | |
| Auxiliary Benefits (wie fühlen sie sich? Welcher Stress weg? Welche Lebensbereiche ändern sich?) | | | |

Speichern als `asset-foundations-{venture}-{YYYY-MM-DD}.csv`. UTF-8, Comma-delimited, double-quoted Strings, Line-Breaks innerhalb Zellen mit `\n`.

## Methodology (Dan Kennedy Spine)

Die 12 Felder sind nicht beliebig. Sie sind die Wirbelsäule eines Kennedy Long-Form Sales Letters:

1. **Position**: Der Prospect muss sich im ersten Satz wiedererkennen. Spezifität (Standort, Rolle, Familienstand, Jahre in Position) signalisiert dass du seine Welt kennst. Generische ICPs ("SMB Founder") triggern keine Erkennung.
2. **Deepest Desires**: Kennedy: "Tritt ein in das Gespräch das schon in seinem Kopf läuft." Desire ist der Motor, alles andere verstärkt oder befreit.
3-5. **Up-at-Night / Frustrated / Angry**: Drei verschiedene emotionale Register. Angst (Up-at-Night), Hilflosigkeit (Frustrated), Wut/Schuld (Angry). Wenn du eines auslaesst, liest sich die Copy flach.
6. **Tried but Failed**: Eliminiert die Alternativen im Kopf des Prospects bevor du deine pitchst. Kennedys "False Solutions Audit".
7. **Trends + Threats**: Urgency ohne Apokalypse. Verbindet das Problem des Prospects mit einer beobachtbaren Marktverschiebung.
8. **Cost of Inaction + Time Horizon**: Schließt die Urgency-Schleife. Ohne Datum oder Deadline loest sich Urgency auf.
9. **Solution / Vehicle**: Erst JETZT betritt dein Produkt die Bühne. Die ersten 8 Reihen verdienen das Recht es zu erwaehnen.
10. **Bodacious Claim**: Kennedys Term. Ein einzelnes audacious Versprechen das direkt auf Row 2 mappt. Kein Tagline. Kein Feature. Das was, wenn wahr, sie heute kaufen laesst.
11. **Secondary Benefits**: Quantifizierbare Side-Effects. Zeit, Geld, Headcount, Errors. Quantifizieren wo möglich.
12. **Auxiliary Benefits**: Emotionaler Payoff. Wie sie sich nach der Transformation fühlen. Wie ihre Familie, ihr Team, ihr Status sich aendert.

Layer auslassen heißt: das daraus gebaute Asset blutet Conversion. Alle 12 sauber: Landing Page, Sales Script, Ad Copy schreiben sich fast von selbst.

## Step-by-Step

### Schritt 1: Cluster Transkripte zu Niches

- Jedes Transkript end-to-end lesen, nicht skimmen.
- Tag jeden Speaker: Vertical, Firmengröße, Rolle, Geographie, Buying-Urgency.
- Gruppiere Transkripte wo die **Sprache des Schmerzes** matched, nicht nur Demographics. Ein 10-Person Agency CEO und ein 50-Person SaaS Founder können in der gleichen Niche leben wenn sie ihren Pain identisch beschreiben.
- Schlage 3-5 Niches vor. Benenne jede nach dem definierenden Trait (Rolle plus Vertical plus Größe, z.B. "Mid-Market Manufacturing CEO, 50-250 Mitarbeiter, DACH").
- Flagge jedes einzelne Transkript das nicht in einen Cluster passt. Entweder eine sechste Niche oder ein misqualifizierter Prospect. Surface zum User.

### Schritt 2: Row 1 (Position) verbatim fuellen

- Pull jedes demographische Detail aus den Transkripten: Standort, Teamgröße, Revenue-Band wenn disclosed, Job Title, Familienstand, Jahre in Rolle, Vertical, Budget Signals.
- Kompakt schreiben. Line-Breaks innerhalb Zellen damit jedes Attribut scannbar ist.
- Wenn ein Detail in keinem Transkript erwaehnt wird: `[unbekannt - in nächstem Call fragen]`. Nicht raten.

### Schritt 3: Row 2 (Deepest Desires) fuellen

- Höre auf Aspirationen. Was sagen sie dass sie wollen, was beneiden sie, welches Status-Objekt referenzieren sie, was würden sie tun "wenn ich das im Griff hätte".
- In ihren Worten phrasieren, nicht in deinen. "Das Business aufs nächste Level bringen" schlaegt "scalable growth achieve".
- Suche nach was sie SEIN wollen, nicht nur was sie TUN wollen. Status, Anerkennung, Sicherheit, Ruhe.

### Schritt 4: Rows 3-5 (Up-at-Night / Frustrated / Angry) fuellen

Drei distinkte emotionale Register. Sauber halten:

- **Up at Night** = Angst vor Verlust, das Katastrophen-Szenario.
- **Frustrated** = Hilflosigkeit, Dinge bewegen sich nicht.
- **Angry** = Schuld, Verrat, Dinge sind aktiv falsch.

Jede Reihe muss den Test bestehen: "würde der Prospect das unterstreichen wenn er es liest?"

Direkte Quotes wo immer möglich. Mit Anführungszeichen markieren.

### Schritt 5: Row 6 (Tried but Failed) fuellen

- Liste spezifische Tools, Agenturen, Hires, Frameworks, Channels die sie schon probiert haben.
- Notiere **warum** jedes scheiterte. Meist eines von: zu teuer, zu langsam, hat die Niche nicht verstanden, fehlende Accountability, Founder hat nicht durchgezogen.
- Diese Reihe ist die Quelle für dein "warum das anders ist" Messaging.

### Schritt 6: Rows 7-8 (Trends + Cost of Inaction) fuellen

- **Trends**: Welche Verschiebungen im Markt sind beobachtbar und beschleunigen sich? Pull aus dem was sie selbst genannt haben, nicht was du für wahr haeltst.
- **Cost of Inaction**: Ihr genannter Worst Case. Wenn nicht genannt: surface als Follow-up Frage für nächsten Call.

### Schritt 7: Row 9 (Solution / Vehicle) fuellen

- Dein Produkt oder Service, präzise benannt.
- Wenn verschiedene Niches verschiedene Framings desselben Produkts brauchen, schreibe die Framings pro Niche, nicht nur den Namen.

### Schritt 8: Rows 10-12 (Bodacious Claim + Secondary + Auxiliary)

- **Bodacious Claim**: Ein Satz der, wenn bewiesen, den Prospect heute kaufen laesst. Direkt auf Row 2 zurück-mappen. Zahlen helfen, Spezifität hilft mehr.
- **Secondary Benefits**: Aufzaehlen jeden quantifizierbaren Side-Effect. Zeit gespart, Geld gespart, Headcount vermieden, Errors reduziert.
- **Auxiliary Benefits**: Emotionaler und Lifestyle Payoff. Wie sie schlafen. Wie sie zuhause auftreten. Was sie aufhören zu sorgen.

### Schritt 9: Quality Pass

Vor Delivery durchlaufen:

- [ ] Jede Zelle traced zurück zu etwas im Transkript Gesagtem, oder ist `[unbekannt]` markiert. Null Erfindung.
- [ ] Keine GPT-Sprache (kein "leverage", "unlock", "streamline", "delve", "harness", "empower", "seamless").
- [ ] Direkte Quotes erscheinen in mindestens Rows 3-5. Customer Voice ist nicht verhandelbar.
- [ ] Bodacious Claim ist keine Feature-Liste. Wenn es nach Tagline klingt, schärfen bis es nach Bet klingt.
- [ ] Keine zwei Niches haben identischen Content in einer Reihe. Wenn doch: eine Niche, nicht zwei. Mergen.
- [ ] Anonymisieren: Ersetze persönliche Namen mit Rollen-Labels (`Founder 1`, `Head of Sales 2`).

### Schritt 10: Deliver

- CSV schreiben. UTF-8, Comma-delimited, double-quoted Strings, Line-Breaks innerhalb Zellen mit `\n` preserved.
- Hand back: CSV-Pfad plus ein-paragraph Summary pro Niche damit User scannen kann bevor er die Datei öffnet.
- Empfehle den nächsten Sub-Skill basierend auf was User zuerst braucht:
  - Landing Page → `landing-pages/SKILL.md`
  - Outbound Copy → `outbound/SKILL.md`
  - Meta/Google Ads → `ads/SKILL.md`

## Was eine gefuellte Zelle wirklich aussehen muss

Spezifisch, transkript-basiert, customer-voiced. Generische SaaS-Marketing-Sprache ist der Failure Mode.

- **Position (Row 1)**: 6-9 Attribute reinpacken: Standort, Teamgröße, Revenue oder Budget Band, Rolle, Familienstand, Jahre in Rolle, Vertical. Line-Breaks für Scannability. "Generic Founder" ist keine Position.
- **Deepest Desires (Row 2)**: In ihren Worten phrasieren. "Den Admin vom Tisch bekommen damit ich endlich die Arbeit machen kann für die ich studiert habe" schlaegt "operational efficiency achieve".
- **Up-at-Night / Frustrated / Angry (Rows 3-5)**: Drei distinkte emotionale Register. Angst, Hilflosigkeit, Schuld. Direkte Quotes wo möglich.
- **Tried but Failed (Row 6)**: Spezifische Tools, Agenturen, Hires, Frameworks namentlich. Warum jedes scheiterte: Cost, Speed, Fit, Accountability, Follow-Through.
- **Trends + Cost of Inaction (Rows 7-8)**: Aus dem ziehen was sie selbst nannten. Worst Case notieren oder `[unbekannt - im nächsten Call fragen]`.
- **Solution / Vehicle (Row 9)**: Dein Produkt oder Service, benannt. Verschiedene Niches brauchen evtl. verschiedene Framings desselben Produkts.
- **Bodacious Claim (Row 10)**: Ein Satz der, wenn bewiesen, heute kaufen laesst. Maps direkt auf Row 2. Klingt wie Wette, nicht wie Tagline.
- **Secondary Benefits (Row 11)**: Quantifizierbare Side-Effects. Zeit, Cost, Errors, Headcount.
- **Auxiliary Benefits (Row 12)**: Emotionaler und Lifestyle Payoff. Wie sie schlafen. Wie sie zuhause auftreten. Was sie aufhören zu sorgen.

## Worked Example (illustrativ, eine Niche, voll gefuellt)

Für ein fiktionales Recruiting-Tech Produkt, das DACH B2B Tech-Startups mit Senior Engineering-Hires versorgt. Lies für die strukturellen Moves, nicht den Content. Dein gefuelltes CSV muss aus deinen eigenen Transkripten kommen.

| Field | Niche A: Series-A B2B SaaS Founder, DACH, 20-80 Mitarbeiter |
|---|---|
| **Position** | Series-A B2B SaaS Founder. Berlin / Muenchen / Hamburg / Wien / Zuerich. 20-80 Mitarbeiter. ARR 2-8M EUR. Verheiratet, 32-42, oft mit Kleinkindern. 3-7 Jahre im eigenen Business. Letzte Runde 4-12M EUR Series-A. |
| **Deepest Desires** | "Endlich einen Senior Engineer der nicht nach 8 Wochen wieder geht." Status: das Team haben das Tier-1 VCs Top-Quartile nennen. Sicherheit: Hiring-Risiko nicht mehr persönlich tragen müssen. |
| **Up at Night** | Der Lead-Architekt der vor zwei Wochen unterschrieben hat zieht zurück. Burn weiter steigt. Nächste Bridge wird notwendig 9 Monate vor Plan. |
| **Frustrated by** | "Drei Recruiter parallel und keiner versteht warum unser Stack Rust und nicht Python ist." Calendly-Slots verbrannt mit Senior-Profilen die nach Jahresgehalt und nicht Mission kommen. *"Ich habe das Unternehmen gegründet um nicht der HR-Mensch zu werden. Und jetzt bin ich's wieder."* |
| **Angry at** | Standard-Recruiter die 25 Prozent Fee nehmen und nach drei Monaten den gleichen Pool aus LinkedIn-Recruiting-Tools nochmal liefern. Mid-Market Recruiting-Agenturen die mit Tier-1 Erfolgs-Cases pitchen aber Tier-3 Profile schicken. |
| **Tried but Failed at** | Internes Recruiting-Team aufgebaut (zwei Hires in 9 Monaten weg). Drei Standard-Recruiter parallel (4 Senior-Hires in 18 Monaten, alle wieder weg). LinkedIn Recruiter Lite (1500 InMails, 4 Antworten). Headhunter Personal-Empfehlung über Investor (war nur Generalist). |
| **Trends + Threats** | Offshore Engineering Hubs (Lissabon, Krakau, Buenos Aires) machen Senior-Talent in DACH knapper, nicht weniger. AI-Tools die Recruiting beschleunigen aber Fit nicht verbessern. Founder-Burnout-Rate in DACH B2B SaaS bei 40 Prozent in Jahr 4. |
| **Cost of Inaction** | "Wenn wir die nächsten zwei Senior-Hires verbocken, ist das Series-B Fenster zu." Worst Case Window 6-9 Monate. |
| **Solution / Vehicle** | Recruitment Circle. Vertical Tech-Recruiting für DACH B2B SaaS Series-A bis B. Topgrading-basierte Discovery, A-Player-Filter über Track Record statt Pedigree, 12 Monate Replacement-Garantie. |
| **Bodacious Claim** | "Senior Engineering Hire mit 18+ Monaten Retention oder wir arbeiten kostenlos bis es passt." |
| **Secondary Benefits** | Hiring Cycle 12 Wochen statt 24. Replacement-Rate unter 8 Prozent statt Marktstandard 30. Founder-Stunden in Hiring runter von 12 auf 2 pro Woche. Keine drei parallelen Recruiter mehr zu koordinieren. |
| **Auxiliary Benefits** | Wieder Zeit für Produkt-Strategie statt Interviews. Team das ohne dich operiert weil A-Player A-Player anziehen. Investor-Calls die über Roadmap reden statt über Hiring-Probleme. Du wirst wieder der Founder den du sein wolltest, nicht der Personalleiter. |

### Was dieses Beispiel zeigt (strukturelle Moves)

- **Row 2 mappt auf Row 10**. "Endlich einen Senior Engineer der nicht nach 8 Wochen wieder geht" mappt auf "Senior Hire mit 18+ Monaten Retention oder wir arbeiten kostenlos". Same Idea, zwei Mal ausgedrückt.
- **Row 6 nennt spezifische gescheiterte Alternativen**: "Internes Team, drei Standard-Recruiter, LinkedIn Recruiter Lite, Headhunter über Investor." Nicht abstrakt.
- **Row 12 ist Identität, nicht Features**: "Du wirst wieder der Founder den du sein wolltest, nicht der Personalleiter."
- **Direkte Quotes** in Row 4 (`"Ich habe das Unternehmen gegründet um nicht der HR-Mensch zu werden..."`). Customer Voice ist nicht verhandelbar.

## Anti-Patterns

- **Cluster-Schritt skippen**: Wenn du eine große Spalte für "alle Kunden" fuellst, ist jedes downstream Asset vague. Der ganze Punkt: Copy konvertiert wenn sie zu einer Niche spricht, nicht zum Markt.
- **Pain erfinden der nicht gesagt wurde**: Rows 3-5 müssen aus Transkripten kommen. Wenn du fabricst, klingt das Asset wie das Marketing aller anderen.
- **Drei emotionale Register vermischen**: Up-at-Night ist nicht Frustrated ist nicht Angry. Sauber halten.
- **Bodacious Claim wie Tagline schreiben**: Tagline ist Vibe. Bodacious Claim ist Wette. Customer denkt "das ist ein großer Wurf, aber wenn es wahr ist will ich es".
- **Auxiliary Benefits als Wegwerf-Reihe behandeln**: Row 12 ist oft die Reihe die den Sale closed. Echte Zeit reinstecken.

## Hand-off (Was downstream fliesst)

Dies ist die Source-Skill im GTM Stack. Jeder andere Sub-Skill erwartet das Foundation CSV als Upstream-Input:

| Foundation Row | Wo es downstream fliesst |
|---|---|
| Row 1 (Position) | landing-pages Hero Context, outbound Email-1 Opener, ads Creative Brief, sherpa Call-Scoring ICP-Filter |
| Row 2 (Deepest Desires) | landing-pages Headline, ads Hooks, weekly-content-engine aspirational angles |
| Rows 3-5 (Pain Layer) | landing-pages Pain Story, outbound Email-1 Body, ads Problem-Hooks |
| Row 6 (Tried but Failed) | landing-pages "warum das anders ist", outbound Email-2 Objection Handling, ads "do not use" Inspiration |
| Rows 7-8 (Trends + CoI) | outbound Email-2 Urgency, ads Body Stat-led Hooks |
| Row 9 (Vehicle) | landing-pages Offer-Block, outbound Email-3 Close, ads CTAs |
| Row 10 (Bodacious Claim) | landing-pages Headline, ads Primary Hook, outbound Email-1 Subject |
| Rows 11-12 (Benefits) | landing-pages Feature Cards + Daily Example, outbound Results-List, ads Body |

## Tracking Impact

Wenn das CSV gefuellt ist und Assets daraus gebaut sind, log:
- Welches Asset (LP, Ad, Script) hat welche Reihe am stärksten genutzt.
- Conversion-Delta vs. das vorherige Asset ohne Foundation.
- Quote-Recognition-Rate vom Prospect ("ja, genau das ist es") in den nächsten 5 Sales Calls. Wenn Recognition unter 70 Prozent: Foundation ist falsch, zurück zu Transkripten.

## Re-Run Cadence

Einmal pro Niche. Quartalsweise re-run wenn neue Transkripte sich stapeln. Foundation kompoundiert mit jedem Call.

## Voice Rules

Output CSV in deutscher Voice mit echten Umlauten ä ö ü ß. Keine Em-Dashes. Keine AI-Phrasen wie "leverage", "unlock", "harness", "seamless". Customer-Voice in den Pain-Reihen, nicht Marketing-Voice.
