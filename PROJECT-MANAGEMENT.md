# Mala Project Management Plan

Master-Plan für mala markets Brain plus Operations. Alles was wir vorhaben tracken wir hier in diesem File. Status pro Item, Owner, Deadline, Link zu Detail-Files.

**Single Source of Truth für PM ist Notion** (siehe `00-start-here/notion-token-setup.md`), aber dieser Plan ist die GitHub-Spiegel-Version damit alles diff-bar und versioniert ist.

**Gesamtplan-Vision:** [Mala Digital Company Twin Deck](https://chris1928a.github.io/mala-brain/decks/digital-twin/) (16 Slides, 2-Jahres-Roadmap zum 500k-Mandat)

---

## Aktueller Sprint: KW21 plus KW22 (19.05. bis 01.06.2026)

**Mission:** Lars plus Matteo plus Dieter arbeiten zwei Wochen lang produktiv im Shared-Repo. Das ist der einzige Erfolgs-Test diese Sprint. Wenn die Kollab läuft, geht Phase 1 live.

### Phase 0.1, Dieter GitHub Collaboration Test (PRIORITY)

Das ist der kritische Test. Wenn Dieter das System eigenständig benutzen kann, läuft die Kollab. Wenn nicht, fixen wir die Bruchstellen vor allem anderen.

| Task | Owner | Status | Link |
|---|---|---|---|
| Dieter installiert Claude Code auf seinem PC | Dieter (Setup von Matteo begleitet) | open | [00-start-here/dieter-claude-code-setup.md](00-start-here/dieter-claude-code-setup.md) |
| Dieter erstellt GitHub-Account (falls noch nicht da) | Dieter | open | [00-start-here/dieter-claude-code-setup.md](00-start-here/dieter-claude-code-setup.md) |
| Dieter akzeptiert mala-brain Repo-Invite | Dieter | open | github.com/chris1928a/mala-brain/invitations |
| Dieter klont das Repo lokal mit GitHub Desktop | Dieter | open | [00-start-here/dieter-claude-code-setup.md](00-start-here/dieter-claude-code-setup.md#schritt-4) |
| Dieter macht erste Test-Branch und PR 1 (customer profile) | Dieter | open | [00-start-here/dieter-workflow.md](00-start-here/dieter-workflow.md#pr-1-eigener-customer-folder-anlegen) |
| Dieter macht PR 2 (playbook client-onboarding) | Dieter | open | [00-start-here/dieter-workflow.md](00-start-here/dieter-workflow.md#pr-2-playbook-ergänzen) |
| Dieter macht PR 3 (capa-week-21 Decision) | Dieter | open | [00-start-here/dieter-workflow.md](00-start-here/dieter-workflow.md#pr-3-eigene-capa-auslastung-als-decision-log) |
| Sprint-Mid-Check Fr 23.05.: was funktioniert, was hakt | Group | open | TBD 05-meetings/2026-05-23-mid-check.md |

### Phase 0.2, Lars plus Matteo geben Chris vollen Zugriff

Damit Chris den vollen Stand sehen und Notion-Mirror bauen kann.

| Task | Owner | Status |
|---|---|---|
| Lars added `chris1928a` als Admin im Repo (Settings → Collaborators) | Lars | open |
| Lars added `chris@erlerventures.org` als Editor in Notion-PM-Page | Lars | open |
| Lars erstellt Internal Connection Token für Claude in Mala-Notion ([00-start-here/notion-token-setup.md](00-start-here/notion-token-setup.md)) | Lars | open |
| Token via Slack-DM an Chris (nicht in Gruppe) | Lars | open |
| Lars plus Matteo committen alle lokalen Mala-Sachen ins Repo (falls Local-State ≠ Repo) | Lars, Matteo | open |
| Hetzner-Zugang an Chris teilen (aus Call 10:02) | Lars | open |

### Phase 0.3, Notion-Mirror live

Sobald Phase 0.2 durch.

| Task | Owner | Status |
|---|---|---|
| Chris pushed via `07-tech/scripts/notion_mirror_push.py` mit Token | Chris | open, blockt auf Phase 0.2 |
| 6 Notion-Pages unter PM-Page erstellt (Permissions, Sprint, Onboarding, ICP, Meeting, Decisions) | Chris | open |
| URLs in `07-tech/scripts/.notion_mirror_log.json` geloggt | Chris | open |

### Phase 0.4, Sprint-Review KW22

| Task | Owner | Datum |
|---|---|---|
| Mid-Sprint-Cowork Fr 23.05. | Lars, Matteo, Chris | 23.05.2026 |
| Mid-Sprint-Cowork Fr 30.05. | Lars, Matteo, Chris | 30.05.2026 |
| Sprint-Review Mo 02.06. plus Empfehlung System produktionsreif Ja/Nein | Group | 02.06.2026 |
| Sprint KW23+24 Plan ([04-operations/sprints/2026-kw23-24-*.md](04-operations/sprints/)) gescoped | Chris | 02.06.2026 |

---

## Phase 1, KW23 plus KW24 (02.06. bis 15.06.2026), ICP plus Marketing-Ads-Skills

**Conditional:** geht live wenn Sprint KW21+22 erfolgreich war.

**Mission:** ICP finalisieren plus erste Marketing-Ads-Skills im Repo damit der KI-Experte sofort produktiv ist.

Plan: [04-operations/sprints/2026-kw23-24-icp-und-ads.md](04-operations/sprints/2026-kw23-24-icp-und-ads.md)

Aus Call 19.05.: "ICP - Founder Interview Leitfaden von Lars einfach weitermachen dann ueber Skill laufen lassen" plus "Asset Foundation - kann mein komplettes skill set mit euch teilen Ads, outbound, Content leadership".

## Phase 2, KW25 plus KW26 (16.06. bis 29.06.2026), Cron Jobs auf Hetzner

**Mission:** Hetzner-Cron-Stack live (Sales plus Marketing plus Lead-Gen Automation). Daily Brief plus Pipeline-Tracking laufen autonom. KI-Experte hat Build-Lead.

Plan: [04-operations/sprints/2026-kw25-26-cron-und-sales.md](04-operations/sprints/2026-kw25-26-cron-und-sales.md)

Aus Call 19.05.: "Cron jobs: Sales /Marketing automation. Sales: GTM Skills exekutern. ICP updates kommen aus founder interviews. Copy fuer Landing pages, Ads, Content fuer Knowledge leadership. Sales und marketing lassen wir automatische updates laufen um zahlen conversion (aus CRM) mit den Performances der Lead gen aktivitaeten zu matchen. Lead Gen per se ueber cron job automatisieren fuer Outbound (Email etc.)".

## Phase 3, KW27 plus KW28 (30.06. bis 13.07.2026), Asset Foundation plus Meta Test

**Mission:** Hook-Page live, erster Meta-Test mit 3-5k EUR Budget, Cost-per-Booked-Meeting klar gemessen.

Plan: [04-operations/sprints/2026-kw27-28-asset-foundation-meta-test.md](04-operations/sprints/2026-kw27-28-asset-foundation-meta-test.md)

Aus Call 19.05.: "Channels: Google Ads als basis fuer inbound perfekt in google ergebnissen. Websites visits - retargeting Meta, Video ads display geschichten - CEO bekommt gesichter auf Meta (FB & IG). Probleme adressieren. Video setup teilen mit Jungs. Cron Jobs dann fuer best converting assets in outbound".

## Phase 4, ab KW29, 3-Level GitHub-Architektur ausrollen

Aus Call 19.05.: "wir erstellen einen shared github folder Founder PM Dieter dann zweiter level Github fuer controlling Capa auslastung, alles resourcen kunden. Dritter level dann den Rest. Wir setzen 3 shared githubs auf, ich gebe euch anleitung auf die Architektur".

Volldetail: [07-tech/3-level-github-architecture.md](07-tech/3-level-github-architecture.md)

- Level 1 (Founder + PM + Dieter): existiert (dieses Repo)
- Level 2 (Controlling + Kunden + Ressourcen): TBD `chris1928a/mala-team-controlling`
- Level 3 (Rest): TBD `chris1928a/mala-team`
- Cron-Sync wöchentlich Rechner zu GitHub
- Notion-Mirror laeuft kontinuierlich

---

## Backlog (geplant, nicht jetzt)

| Thema | Wann ungefähr | Owner |
|---|---|---|
| 3-Level GitHub-Architektur ausrollen (Founder+PM / Controlling+Kunden / Rest) | Phase 4, ab KW29 (siehe [07-tech/3-level-github-architecture.md](07-tech/3-level-github-architecture.md)) | Chris |
| Marcel Interview KI-Werkstudent | KW21 oder KW22 (parallel) | Lars, Matteo |
| Grafikdesigner-Replacement screenen | KW21 oder KW22 (parallel) | Lars, Matteo |
| Hetzner Cron-Setup live | Phase 1 (KW23+24) | Chris plus Junior Dev |
| Customer Maturity Cockpit pro Mandat (Pilot) | 2027 H1 | Chris plus Lars |
| 500k-Mandat Workshop-Lizenz | 2028 | Lars, Matteo, Chris |
| Retainer-Anpassung Chris (10-20h/Woche statt 1k Retainer) | Separater Slot, prioritär | Lars, Chris |
| Website-Migration WordPress nach Astro plus GitHub plus Render plus Posthog | Phase 2 | Laureen plus Junior Dev |
| n8n plus Airtable Migration nach Python plus Claude (für Brain-Pfad) | Phase 2 | Junior Dev plus Chris |

---

## Locked Decisions

- [19.05.2026 Sprint-Kickoff (8 Decisions)](01-strategy/decisions/2026-05-19-sprint-kickoff.md)

Neue Decisions immer als File in `01-strategy/decisions/YYYY-MM-DD-thema.md`. 30-Tage-Outcome-Review-Datum nicht vergessen.

## Meeting-Log

- [19.05.2026 Sprint-Kickoff Call](05-meetings/2026-05-19-sprint-kickoff.md) plus [Raw Gemini-Notes](05-meetings/raw/2026-05-19-gemini-notes.md)
- Mid-Sprint-Check Fr 23.05. (TBD)
- Mid-Sprint-Check Fr 30.05. (TBD)
- Sprint-Review Mo 02.06. (TBD)

---

## Status-Update-Konvention

Jeden Montag pro offenem Task ein kurzes Update als Kommentar in der Task-Zeile ergänzen. Format in der `Status`-Spalte:

- `open` = noch nicht angefangen
- `in progress` = jemand arbeitet dran
- `blockt auf <Owner>` = wartet auf Input von jemandem
- `done` = abgeschlossen (Checkbox abhaken)

Bei Done: dazu auch das Datum in Klammern, z. B. `done (23.05.)`.

## Wer trackt was

- **Chris:** dieser Plan plus Notion-Mirror plus alles unter `07-tech/`
- **Lars:** Strategische Decisions plus ICP plus Sales plus Finanzen
- **Matteo:** Operations plus Marketing plus Team-Onboarding (treibt Dieter)
- **Dieter:** PM-Status pro Mandat plus Capa-Auslastung plus Customer-Map
- **Marketplace Manager:** Mandate-Execution
- **Laureen:** Marketing-Output plus Website
- **Junior Dev (sobald hired):** Brain-Maintenance plus Skripte plus n8n-Migration

Stand: 19.05.2026.
