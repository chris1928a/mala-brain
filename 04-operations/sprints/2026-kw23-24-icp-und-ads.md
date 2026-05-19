# Sprint KW23 + KW24, 02.06. bis 15.06.2026

**Eine Hauptmission:** ICP finalisiert plus erste 2 Marketing-Ads-Skills im Repo. Damit der neue KI-Experte bei mala markets sofort produktiv ist wenn er onboarded.

**Sprint-Owner:** Lars (ICP), Matteo (Ads + Voice), Chris (Skill-Bau, KI-Experte-Onboarding)
**Dauer:** 2 Wochen
**Start:** Mo 02.06.2026
**Mid-Check:** Fr 06.06.
**Sprint-Review:** Mo 16.06.

**Vorbedingung:** Sprint KW21+22 (Brain-Setup plus Dieter-Test) ist Done. Notion-Mirror laeuft, Dieter hat 3 PRs gemerged.

## Die EINE Mission

Bis Ende KW24 hat mala markets:
- Ein finales ICP-Doc im Repo plus in Notion
- Den `mala-icp` Claude-Skill der jeden Lead automatisch klassifiziert
- Die ersten beiden Marketing-Skills (`google-ads-mala`, `meta-retargeting-mala`)
- Die Voice-Library fuer Lars plus Matteo (Pflicht-Read vor jedem Outbound)
- Eine Onboarding-Strecke fuer den neuen KI-Experten so dass er Tag 1 produktiv ist

## Definition of Done

- [ ] `01-strategy/icp/icp-mala-v1.md` finalisiert von Lars (basiert auf Founder-Interviews)
- [ ] `07-tech/skills/mala-icp/SKILL.md` mit Trigger-Words, klassifiziert P1/P2/P3/OUT
- [ ] `07-tech/scripts/icp_match.py` matched neue Leads gegen ICP, Daily-Run auf Hetzner geplant
- [ ] `07-tech/skills/google-ads-mala/SKILL.md` mit Keyword-Logik, Ad-Copy-Generator, Negative-Listen
- [ ] `07-tech/skills/meta-retargeting-mala/SKILL.md` mit Video-Ad-Patterns, CEO-Gesichter-Strategie, Custom-Audience-Setup
- [ ] `03-marketing/voice/lars.md` mit 20 LinkedIn plus 10 Email Beispielen
- [ ] `03-marketing/voice/matteo.md` mit Voice-Pattern plus Sperrwoertern
- [ ] `00-start-here/ki-experte-onboarding.md` ready (siehe naechsten Sprint-Plan)
- [ ] Mid-Check Fr 06.06.: ICP-Draft v1 reviewen
- [ ] Sprint-Review Mo 16.06.: was laeuft, was bricht, KW25+26 scopen

## Wochenaufteilung

### KW23 (02.06. bis 08.06.) - ICP Final plus erste Skill-Skeleton

| Tag | Aktivitaet | Owner |
|---|---|---|
| Mo 02.06. | Sprint-Kickoff plus Review KW21+22 plus Plan-Lock | Group |
| Di 03.06. | Lars finalisiert ICP-Doc aus Founder-Interviews | Lars |
| Mi 04.06. | Chris baut `mala-icp` Skill-Skeleton plus `icp_match.py` | Chris |
| Do 05.06. | Matteo schreibt `google-ads-mala` Skill-Skeleton plus Ad-Copy-Templates | Matteo, Chris |
| Fr 06.06. | Mid-Check Friday-Cowork: ICP plus Skill-Skeletons reviewen | Group |

### KW24 (09.06. bis 15.06.) - Skills auspolstern plus KI-Experte Onboarding

| Tag | Aktivitaet | Owner |
|---|---|---|
| Mo 09.06. | Voice-Library Lars (20 LinkedIn plus 10 Email) | Lars |
| Di 10.06. | Voice-Library Matteo plus `meta-retargeting-mala` Skill | Matteo |
| Mi 11.06. | KI-Experte-Onboarding-Doc finalisieren plus 5 First-Week-Tasks fuer ihn | Chris |
| Do 12.06. | Plan-Run-Through mit Lars plus Matteo (alles ready fuer KI-Experte) | Group |
| Fr 13.06. | Sprint-Vorbereitung Retro plus KW25+26 Pre-Scope | Group |

## Parallele Tracks

- KI-Experte (Marcel?) Hire-Entscheidung. Ziel: Vertrag Ende KW24
- Dieter laeuft mit KW21+22 Workflow weiter im Daily-Use
- Notion-PM-Page wird parallel zum GitHub-Mirror aktiv genutzt

## Sprint-Risiken

- **ICP-Founder-Interviews nicht durch.** Mitigation: Lars priorisiert 3 Top-Mandate als Quelle, Rest in KW25+26
- **Voice-Library braucht zu lange.** Mitigation: 10 Beispiele reichen fuer Skeleton, Rest wird iterativ erweitert
- **KI-Experte nicht ready zum Hire.** Mitigation: Onboarding-Doc liegt trotzdem als Asset, sobald Hire da, sofort verwendbar

## Nach diesem Sprint

KI-Experte ist Tag 1 produktiv. Sprint KW25+26 startet mit Cron-Jobs plus Sales-Automation. Volldetail in `04-operations/sprints/2026-kw25-26-cron-und-sales.md`.
