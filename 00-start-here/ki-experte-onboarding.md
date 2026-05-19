# KI-Experte Onboarding bei mala markets

Hi, willkommen bei mala markets. Du bist der neue KI-Experte (Werkstudent oder Junior Dev, je nach Vertrag). Diese Datei ist deine erste Woche im Detail.

**Ziel:** du bist Tag 1 produktiv. Keine 4 Wochen Onboarding, keine schwammigen Aufgaben. Klar definierte Tasks die direkt Wert schaffen.

**Zeit für Onboarding:** circa 2 bis 3 Tage. Danach normales Daily-Doing.

---

## Wer du bist und wer dein Team ist

- **Du:** KI-Experte, neue Stelle bei mala markets seit KW24-25 2026. Profil GitHub plus Python plus Claude Code.
- **Lars Seuß:** Co-Founder, Strategie plus Sales plus Finanzen. Dein Approver für strategische Sachen.
- **Matteo Giazzi:** Co-Founder, Operations plus Marketing. Dein direkter operativer Sparring-Partner.
- **Dieter:** PM, Controlling. Du arbeitest mit ihm an Customer-Performance-Pulls.
- **Marketplace Manager (Jerome, Clarissa, Nick, Leon):** sie nutzen das was du baust für ihre Mandate.
- **Laureen:** Marketing plus Website. Du baust ihre Skripte für Content-Automation.
- **Chris Erler:** externer Architekt (Erler Ventures). Friday-Cowork plus Architektur-Reviews. Slack-DM für Fragen.

## Erste 3 Tage, Schritt-für-Schritt

### Tag 1, Setup und Repo-Tour

1. **Onboarding-Reihenfolge im Repo lesen** (sollte 2h dauern):
   - [`00-start-here/onboarding.md`](onboarding.md) - generelle Mala-Brain-Idee
   - [`00-start-here/dieter-claude-code-setup.md`](dieter-claude-code-setup.md) - Setup Claude Code plus GitHub
   - [`00-start-here/dieter-workflow.md`](dieter-workflow.md) - taeglicher Workflow
   - [`00-start-here/team-permissions.md`](team-permissions.md) - 9-Rollen-Matrix
   - [`STRUCTURE.md`](../STRUCTURE.md) - Repo-Layout
   - [`PROJECT-MANAGEMENT.md`](../PROJECT-MANAGEMENT.md) - aktueller Master-Plan
   - [`07-tech/architecture.md`](../07-tech/architecture.md) - Drei-Ebenen-Architektur
   - [Mala Digital Twin Deck](https://chris1928a.github.io/mala-brain/decks/digital-twin/) - 16-Slide-Gesamtvision

2. **Setup-Workshop mit Matteo:** GitHub-Account, Claude Code, Repo-Clone, Hetzner-SSH-Zugang.

3. **Erste Hello-World-PR:** Branch `pm/onboarding-<deinName>`, Datei `00-start-here/<deinName>-notes.md` anlegen, kurze Notizen was du am Tag 1 gelernt hast. PR auf GitHub, Matteo merged.

### Tag 2, ICP-Match-Skript verstehen plus erweitern

1. **Lies das ICP-Doc:** [`01-strategy/icp/template.md`](../01-strategy/icp/template.md) plus das finale ICP-Doc von Lars in `01-strategy/icp/icp-mala-v1.md`.

2. **Lies das ICP-Match-Skript:** [`07-tech/scripts/icp_match.py`](../07-tech/scripts/icp_match.py) (sobald von Chris gebaut).

3. **First Real Task:** ICP-Match-Skript um 1 neues Buying-Signal erweitern aus den Founder-Interviews. Lars zeigt dir welches. PR mit Lars als Reviewer.

### Tag 3, Cron-Job-Setup auf Hetzner

1. **Hetzner-SSH-Zugang testen:** Zugangsdaten von Lars, einmal einloggen, schauen was schon läuft.

2. **Cron-Schedule lesen:** [`07-tech/architecture.md`](../07-tech/architecture.md), Section Cron-Jobs.

3. **First Real Task:** den daily_brief Slack-Bot um 1 KPI erweitern (z.B. ICP-Match-Counts der letzten 24h). PR mit Chris als Reviewer.

## Die ersten 5 echten Tasks (Sprint KW25+26 oder später)

Du bist hier nicht zum Lernen, sondern zum Bauen. Diese 5 Tasks sind dein Ramp-up:

1. **`07-tech/scripts/sales_bridge.py`** maintenance - stündliche CRM-Pulls, Stage-Stagnation-Detection
2. **`07-tech/scripts/marketplace_pull.py`** - Amazon SP-API plus Otto plus Kaufland Daily-Sync, Buy-Box-Tracking
3. **`07-tech/scripts/icp_match.py`** weiterentwickeln nach jedem Lars-Interview
4. **`07-tech/scripts/daily_brief.py`** plus Slack-Integration
5. **`07-tech/scripts/stress_detector.py`** - Pre-Decision Pause-Logik

## Wie du arbeitest

### Pull-Anfragen

Du machst alles via PRs. Niemals direkt auf `main`. Branch-Konvention:

- `tech/<thema>` für Skripte plus Skills
- `feature/<thema>` für größere neue Sachen
- `bugfix/<thema>` für Fixes
- `hotfix/<thema>` für Production-Notfall

Reviewer: Chris für Architektur, Matteo für Operations-Bezug, Lars für ICP plus Pricing.

### Tägliche Routine

- **Morgens 09:00:** Daily Brief in Slack lesen, schauen ob Risk-Flags da sind
- **Vormittags:** an aktuellem Skill oder Skript arbeiten
- **Mittags:** Quick-Sync mit Matteo (15 Min)
- **Nachmittags:** PR-Reviews, Skript-Maintenance, ad-hoc Tasks
- **Freitags 14:00:** Cowork-Session mit Chris (online), Reviews plus Next-Week-Planung

### Skill bauen

Wenn du einen neuen Claude-Skill baust, folge dem Template:

```
07-tech/skills/<skill-name>/
├── SKILL.md         (Trigger-Words, was er tut, Output-Format)
├── references/      (optionale Referenz-Files)
└── examples/        (Beispiel-Inputs plus Outputs)
```

Frontmatter in SKILL.md immer:
```yaml
---
name: skill-name
description: Kurz was der Skill tut und wann er triggert
type: utility / sales / marketing / operations
related_skills:
  - andere-skill-1
notion_pages:
  - title: Page-Titel
    url: notion-url
---
```

### Wenn du Fragen hast

1. Erst im Repo schauen (00-start-here, 07-tech, vorherige PRs)
2. Wenn nicht da, Matteo oder Chris pingen (Slack)
3. Wenn dringend, Slack-DM Chris direkt

Keine dummen Fragen. Lieber 5x fragen als 5 Tage verlieren.

## Voice-Rules

Pflicht-Read: [`07-tech/voice-rules.md`](../07-tech/voice-rules.md). Kurzversion:

- Deutsche Umlaute IMMER (ä ö ü ß), keine ae/oe/ue/ss als Ersatz
- Keine Em-Dashes
- "mala markets" immer kleingeschrieben
- Direkt, knapp, natürlich. Keine AI-Phrasen.

Gilt für: Code-Kommentare, Commit-Messages, PR-Descriptions, Slack, Notion, alles.

## Was am Ende Woche 1 stehen sollte

- [ ] Setup komplett, 1 Hello-World-PR gemerged
- [ ] ICP-Doc verstanden, 1 ICP-Match-Erweiterung als PR
- [ ] Hetzner-Zugang aktiv, 1 daily_brief-Erweiterung als PR
- [ ] Daily Brief landet bei dir, du kannst die KPIs interpretieren
- [ ] Du weißt wer welche Rolle hat und wen du wann pingen kannst

Wenn das stand am Freitag, bist du angekommen.

## Was die ersten 4 Wochen passieren

- Sprint KW25+26: Cron-Stack live (du baust mit)
- Sprint KW27+28: Asset Foundation plus Meta-Test (du baust Tracking)
- Sprint KW29+30: Voice-Library Ausbau plus Customer-Maturity-Pilot Start
- Sprint KW31+32: Customer-Maturity-Cockpit erste Iteration

Plan-Detail siehe [`PROJECT-MANAGEMENT.md`](../PROJECT-MANAGEMENT.md).

## Wenn etwas nicht passt

Du bist neu. Wenn die Doku unklar ist, Sachen nicht funktionieren, oder du anders arbeiten würdest, sag das. Mache PR gegen diese Datei mit Verbesserung. Chris merged.

Willkommen im Team.

Stand: 19.05.2026, kommt zum Einsatz mit KI-Experte-Hire ab KW23 oder später.
