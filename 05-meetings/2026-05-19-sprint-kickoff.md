# Sprint-Kickoff Call, 19.05.2026

**Teilnehmer:** Christoph Erler, Lars Seuß, Matteo Giazzi
**Anlass:** Wochenstart KW21, Sprint-Kickoff für ICP + Kunden-Prozesse
**Quelle:** Gemini-Notes plus Sprint-Setup-Diskussion

## Zusammenfassung in einem Satz

Team einigt sich auf Notion als Single Source of Truth für PM, GitHub als Backend für Mala-Brain, 2-Wochen-Sprints, und startet Sprint KW21+22 mit Fokus ICP plus Kunden-Prozess-Automatisierung.

## Decisions (im Call gelockt)

1. **Notion = Single Source of Truth für PM.** GitHub bleibt Backend für Code, Skripte und Architektur. Notion ist die Team-Lese-und-Schreib-Schicht.
2. **2-Wochen-Sprints.** Ein Thema pro Sprint, kein Multi-Tasking mehr.
3. **Sprint KW21+22 Thema:** ICP-Definition plus Kunden-Prozess-Optimierung.
4. **Nächster Sprint KW23+24:** Werbemaßnahmen (Google Ads plus Meta-Retargeting), falls Brain-Test mit Dieter erfolgreich.
5. **Hetzner ersetzt Make plus n8n** im kritischen Brain-Pfad. n8n + Airtable bleiben für Listings-Workflows.
6. **Rollen-Lock:** Lars = Strategie + Sales + Finanzen + Cashflow. Matteo = Operations + Marketing. Dieter = PM + Controlling + Kapazitätsplanung.
7. **KI-Werkstudent:** Marcel als heißer Kandidat, Screening läuft.
8. **Digital Twins:** Founder-Twin (Lars + Matteo) plus Team-Twin auf shared GitHub-Brain, über Dropbox synct.

## Action Items

### Chris Erler
- [x] Projektstruktur GitHub aufgesetzt: docs/team-permissions.md, docs/sprints/2026-kw21-22-icp-kunden.md, docs/onboarding.md committed (commit fe81e5c)
- [ ] Notion-Mirror für Dieter aufbauen (blockiert auf Lars' Internal Connection Token)
- [ ] Notion-Folder für Meeting-Transkripte strukturieren
- [ ] Sprint-Plan in Notion mit To-Do-Boxes pro Owner

### Lars Seuß
- [ ] Chris zu mala-brain GitHub-Repo einladen mit Editor-Rechten (Email-Invite an chris@erlerventures.org)
- [ ] Internal Connection Token für Claude im Mala-Notion erstellen plus an Chris übergeben
- [ ] ICP basierend auf Founder-Interviews ausarbeiten
- [ ] Bewerber Grafikdesign screenen (Position frei zum Monatsende)

### Matteo Giazzi
- [ ] Mala-Brain mit GitHub verknüpfen für Transkripte-Automation
- [ ] Bewerber Grafikdesign screenen
- [ ] Test mit Dieter im Brain-Workflow durchspielen

### Group
- [ ] Dieter onboarden plus Zusammenarbeit testen (Sprint KW21 Fokus)
- [ ] Kooperationsmodell plus Retainer neu verhandeln in separatem Slot

## Kontext-Updates

### Personal
- Grafikdesigner geht zum Monatsende, Probezeit-Kündigung überraschend.
- Volumen im Grafikdesign-Sales gestiegen, schneller Ersatz nötig.
- Interview-Leitfaden für Screening etabliert.
- Marcel als potenzieller KI-Werkstudent identifiziert.

### Sales Pipeline
- Inbound: Anfrage für eBay-Projekt von hochwertiger Audiomarke. Kanal: Website-SEO. Lars sieht Positionierung als eBay-Agentur als Treiber.
- Strategie-Workshops als Basisangebot zum Kunden-Onboarding.
- E-Commerce-Messe Köln im kommenden Monat, Lars positioniert.
- Inbound-Hauptquelle aktuell: Google Ads.
- Plan: Meta-Retargeting-Kampagnen mit problem-spezifischen Creatives.

### Mala-Brain Architektur (final geframed im Call)
- Hetzner = Compute, Cron-Host (statt Make + n8n im kritischen Pfad)
- GitHub `chris1928a/mala-brain` = Master Truth, Skripte, Architektur, Decisions
- Notion = Read-und-Write UI für Team, Single Source of Truth für PM
- Dropbox = Bulk-Files, Recordings, Briefings, Customer-Files
- Claude Code = Instrument-Layer für Synthesis
- Lars-Twin plus Matteo-Twin plus Team-Twin sind die drei Digital-Twins

### Kooperation
- Aktueller Retainer: 1.000 EUR pro Monat
- Realer Aufwand seitens Chris: 10-20 Stunden pro Woche
- Anpassung diskutiert, separater Slot für Verhandlung

### Diskussion Notion vs GitHub für PM
- Chris-Initial-Vorschlag: shared GitHub-Repo als To-Do-System
- Lars-Plädoyer: Notion für Übersichtlichkeit plus dynamische To-Do-Verwaltung
- Final-Decision: Notion = PM-SSOT, GitHub = Backend für Brain-Skripte und Decisions

## Pending Cross-Sprint Decisions

| Thema | Stand |
|---|---|
| Retainer-Anpassung | Aktuell 1k EUR / Monat. 10-20h/Woche Aufwand. Separater Slot nötig. |
| Notion-Permissions für Chris | Internal Connection Token von Lars ausstehend. Blockiert Notion-Mirror. |
| Grafikdesigner-Replacement | Position frei zum Monatsende, Screening läuft. |
| Marcel KI-Werkstudent | Kandidat identifiziert, Interview ausstehend. |
| Junior Dev / KI-Stelle | Äuschreibung online seit 11.05., Profil-Shape auf GitHub + Python + Claude Code. |

## Sprint KW21+22 Fokus

Volldetails in docs/sprints/2026-kw21-22-icp-kunden.md. Highlights:

- Sprint-Ziele: ICP final, Top-3 Kunden-Prozesse automatisiert, Dieter eingebunden, Chris-Onboarding in Mala-Notion durch, Grafikdesigner gescreent.
- Mid-Sprint-Check Fr 23.05.
- Sprint-Review Mo 02.06.

## Nächster Call

- Mid-Sprint-Check Fr 23.05.
- Sprint-Review Mo 02.06.
- Wöchentliche Friday Cowork-Sessions ab KW21.
