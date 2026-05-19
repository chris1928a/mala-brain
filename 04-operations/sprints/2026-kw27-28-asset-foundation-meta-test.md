# Sprint KW27 + KW28, 30.06. bis 13.07.2026

**Eine Hauptmission:** Asset Foundation live, erster Meta-Test läuft mit 3-5k EUR Budget, Cost-per-Booked-Meeting klar gemessen.

**Sprint-Owner:** Matteo (Marketing-Execution), Lars (Sales-Folge-Up), KI-Experte (Tracking-Skripte), Laureen (Website-Migration)
**Dauer:** 2 Wochen
**Start:** Mo 30.06.2026
**Mid-Check:** Fr 04.07.
**Sprint-Review:** Mo 14.07.

**Vorbedingung:** Sprint KW25+26 ist Done. Hetzner-Cron läuft, Daily Brief landet, ICP-Match aktiv.

## Die EINE Mission

Bis Ende KW28 hat mala markets:
- Eine Hook-Page live (Marktplätze gehören auf C-Level)
- 3 Ad-Variationen auf Meta
- Custom Audience aus ICP-Daten
- 2-Wochen Meta-Test mit 3-5k EUR Budget durchgelaufen
- Cost-per-Booked-Meeting klar gemessen plus dokumentiert
- Sales-Folge-Up-Workflow fuer Inbound aus Meta-Test live

## Definition of Done

- [ ] `03-marketing/landing-pages/marktplaetze-c-level.md` als Hook-Page-Spec
- [ ] LP live unter passender URL (Astro plus GitHub plus Render via Laureen)
- [ ] 3 Ad-Variationen in `03-marketing/ads/meta/` mit Creatives plus Copy
- [ ] Custom-Audience auf Meta erstellt aus ICP-Daten (export aus `icp_match.py`)
- [ ] Test-Budget 3-5k EUR allokiert, Test-Start Di 01.07.
- [ ] Test-Laufzeit 2 Wochen
- [ ] Tracking via Posthog plus Meta-Pixel, Daily-Update via Hetzner-Cron
- [ ] Sales-Folge-Up-Workflow für gebuchte Meetings: Lars triggert binnen 24h
- [ ] Sprint-Review Mo 14.07. mit Cost-per-Booked-Meeting plus Recommendation Skalieren-ja-nein

## Wochenaufteilung

### KW27 (30.06. bis 06.07.) - Asset-Bau plus Test-Start

| Tag | Aktivität | Owner |
|---|---|---|
| Mo 30.06. | Sprint-Kickoff plus Asset-Brief-Lock | Group |
| Di 01.07. | Hook-Page-Spec plus Astro-Migration plus LP live | Laureen, Matteo |
| Mi 02.07. | 3 Ad-Variationen (Video plus Static plus Carousel) | Matteo, Laureen |
| Do 03.07. | Custom-Audience auf Meta erstellt, Test-Konfig durchgegangen | Matteo, KI-Experte |
| Fr 04.07. | Test-Start, Mid-Check Friday-Cowork | Group |

### KW28 (07.07. bis 13.07.) - Test läuft, Sales-Folge-Up plus Auswertung

| Tag | Aktivität | Owner |
|---|---|---|
| Mo 07.07. | Daily Brief jetzt mit Meta-Test-KPIs (CPM, CTR, CPL) | KI-Experte |
| Di 08.07. | Sales-Folge-Up-Playbook für Inbound-Meetings finalisiert | Lars |
| Mi 09.07. | Lars führt erste Folge-Up-Calls aus Meta-Test | Lars |
| Do 10.07. | Tracking-Diff plus Ad-Variante-Performance reviewen | Matteo, KI-Experte |
| Fr 11.07. | Test-Phase 1 Auswertung plus Skalierungs-Entscheidung | Group |

## Parallele Tracks

- Customer-Maturity-Cockpit Vorbereitung (für Sprint KW29+30)
- Erste Founder-Twin-Decisions live durch das Brain (Lars plus Matteo nutzen es täglich)
- Junior-Dev plus Marcel haben jetzt 2 Wochen Routine, Workflow ist sitzend

## Sprint-Risiken

- **LP-Migration zu Astro hängt** (WordPress Content schwierig zu portieren). Mitigation: Hook-Page kann auch als simple Astro-Subpage neben WordPress laufen
- **Meta-Pixel-Setup verzögert.** Mitigation: Test starten ohne Conversion-Tracking, manuelles Sales-Folge-Up zählen
- **Cost-per-Booked-Meeting höher als erwartet.** Mitigation: Test trotzdem laufen lassen, Daten sind wertvoller als 3k EUR

## Nach diesem Sprint

Mala-Brain ist voll im Tagesgeschäft, Marketing-Funnel läuft, erste Meta-Test-Learnings da. Sprint KW29+30 startet entweder Skalierung des Meta-Tests oder Pivot je nach CPL. Volldetail in `04-operations/sprints/2026-kw29-30-*.md`.
