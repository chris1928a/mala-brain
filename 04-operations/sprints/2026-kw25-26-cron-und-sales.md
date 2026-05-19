# Sprint KW25 + KW26, 16.06. bis 29.06.2026

**Eine Hauptmission:** Hetzner-Cron-Stack live, Sales-Automation läuft, ICP-Match-Daily und Pipeline-Tracking automatisch.

**Sprint-Owner:** Chris plus KI-Experte (sobald hired), Matteo (Sales-Operationalisierung)
**Dauer:** 2 Wochen
**Start:** Mo 16.06.2026
**Mid-Check:** Fr 20.06.
**Sprint-Review:** Mo 30.06.

**Vorbedingung:** Sprint KW23+24 ist Done. ICP final, erste Marketing-Skills da, KI-Experte ist onboarded.

## Die EINE Mission

Hetzner-Server arbeitet ab jetzt für mala markets. Bis Ende KW26 läuft:
- Daily Sales-Pipeline-Snapshot
- Daily Marketplace-Pull (Amazon, Otto, Kaufland)
- Daily ICP-Match auf neue Leads
- Daily Brief Slack-Notification Mo-Fr 07:00
- Weekly Executive Report Mo 06:00 an Lars plus Matteo
- Stress-Detector vor jeder Decision-Push

## Definition of Done

- [ ] Hetzner-SSH-Zugang für Chris plus KI-Experte aktiv
- [ ] `07-tech/scripts/sales_bridge.py` läuft stündlich gegen das CRM
- [ ] `07-tech/scripts/marketplace_pull.py` läuft alle 6h gegen Amazon SP-API plus Otto plus Kaufland
- [ ] `07-tech/scripts/icp_match.py` klassifiziert neue Leads alle 12h
- [ ] `07-tech/scripts/daily_brief.py` schickt Slack-Brief Mo-Fr 07:00
- [ ] `07-tech/scripts/pipeline_daily.py` läuft Mo-Fr 18:30 mit Diff plus Risk-Flags
- [ ] `07-tech/scripts/weekly_exec_report.py` Mo 06:00 an Lars plus Matteo
- [ ] `07-tech/scripts/stress_detector.py` on-demand integriert in Decision-Workflow
- [ ] Slack-Bot fuer mala markets verknüpft mit Brain (Channel `#mala-brain`)
- [ ] Cron-Schedule dokumentiert in `07-tech/architecture.md`
- [ ] Mid-Check Fr 20.06.
- [ ] Sprint-Review Mo 30.06.

## Wochenaufteilung

### KW25 (16.06. bis 22.06.) - Hetzner-Setup plus 3 erste Skripte

| Tag | Aktivität | Owner |
|---|---|---|
| Mo 16.06. | Hetzner-SSH-Zugang plus Python-Env setup | Chris, KI-Experte |
| Di 17.06. | `sales_bridge.py` plus CRM-API-Anbindung | KI-Experte |
| Mi 18.06. | `marketplace_pull.py` Amazon SP-API plus Otto Partner | KI-Experte, Matteo |
| Do 19.06. | `icp_match.py` Skripten gegen finales ICP | KI-Experte, Lars |
| Fr 20.06. | Mid-Check plus Cron-Schedule erste 3 Jobs live | Group |

### KW26 (23.06. bis 29.06.) - Brief plus Reports plus Stress

| Tag | Aktivität | Owner |
|---|---|---|
| Mo 23.06. | `daily_brief.py` Slack-Integration | KI-Experte |
| Di 24.06. | `pipeline_daily.py` Diff plus Risk-Flag-Logik | KI-Experte, Matteo |
| Mi 25.06. | `weekly_exec_report.py` an Lars plus Matteo | KI-Experte, Lars |
| Do 26.06. | `stress_detector.py` Trigger-Liste plus Pause-Templates | KI-Experte, Chris |
| Fr 27.06. | Friday-Cowork Demo plus Retro-Vorbereitung | Group |

## Parallele Tracks

- Asset Foundation für Meta-Test wird Sprint KW27+28 weiter ausgebaut (Vorbereitung läuft parallel von Matteo)
- Dieter operiert weiter im Customer-Folder, neue PRs jede Woche
- ICP-Iteration: Lars schaut wöchentlich ob `icp_match.py` Output mit Realität übereinstimmt

## Sprint-Risiken

- **Hetzner-Zugang verzögert sich.** Mitigation: Skripte können lokal laufen, Cron später migrieren
- **Amazon SP-API Setup länger als geplant** (App-Approval kann 2-3 Wochen dauern). Mitigation: Otto plus Kaufland zuerst, Amazon nachziehen
- **CRM-API-Limits.** Mitigation: Cache-Layer einbauen, nicht jedes Skript-Run live pullen

## Nach diesem Sprint

Mala-Brain läuft autonom Daily. Lars plus Matteo bekommen morgens den Brief, abends das Pipeline-Update. Asset Foundation Sprint KW27+28 startet. Volldetail in `04-operations/sprints/2026-kw27-28-asset-foundation-meta-test.md`.
