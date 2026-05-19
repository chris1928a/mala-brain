# mala-brain Struktur

Master-Mapping der Repo-Struktur. Diese Datei ist die Quelle für den Notion-Mirror. Pro Top-Level-Ordner im Repo gibt es eine Top-Level-Page in Notion.

## Top-Level Ordner

| Ordner | Notion-Page | Was lebt hier | Hauptverantwortlich |
|---|---|---|---|
| `00-start-here/` | **00 Start Here** | Onboarding für neue Team-Mitglieder, Setup-Anleitungen, Team-Permissions | Chris pflegt |
| `01-strategy/` | **01 Strategy** | Vision, ICP, Strategy Decisions, Positioning, Marketplace Leadership Framework | Lars |
| `02-sales/` | **02 Sales** | Sales-Pipeline, Outbound, CRM-Bridges, ICP-Match | Lars |
| `03-marketing/` | **03 Marketing** | Content, Ads, Voice-Library, Landing Pages, Substack, LinkedIn | Matteo + Laureen |
| `04-operations/` | **04 Operations** | Customers (pro Mandat), Playbooks, Sprints | Dieter + Matteo |
| `05-meetings/` | **05 Meetings** | Alle Meeting-Notes plus Raw-Transkripte | Wer dabei war |
| `06-finance/` | **06 Finance** | P&L, Margin pro Mandat, Retainer-Tracking, Förderbudgets (restricted) | Lars |
| `07-tech/` | **07 Tech** | Brain-Architektur, Skripte, Skills, Workflows, Memory, Voice-Rules | Chris + Junior Dev |
| `08-knowledge/` | **08 Knowledge** | Externes Wissen, Mentor-Referenzen, Industry-Patterns | offen |
| `decks/` | **Decks** | Pitches, Praesentationen, Live unter chris1928a.github.io/mala-brain/decks/ | Chris |

## Root-Files (immer sichtbar in GitHub-Page)

| File | Zweck |
|---|---|
| `README.md` | Erste Lese-Datei, Pointer zu Deck + PM-Plan + Setup |
| `PROJECT-MANAGEMENT.md` | Master Project Management Plan, alle Tasks, Status, Owner |
| `STRUCTURE.md` | Diese Datei, Mapping Repo zu Notion |
| `CLAUDE.md` | Claude Code Project-Rules (wird automatisch geladen) |
| `CODEOWNERS` | GitHub Permission-Map |

## Detaillierte Folder-Struktur

### 00-start-here/

Single Entry Point für jedes neue Team-Mitglied. Was hier liegt, lesen Lars, Matteo, Dieter, Junior Dev als erstes.

- `onboarding.md` Schritt-für-Schritt Setup-Anleitung allgemein
- `dieter-claude-code-setup.md` Anfänger-Anleitung Claude Code plus GitHub
- `dieter-workflow.md` Wie Dieter im Repo arbeitet, 3 Test-PRs
- `team-permissions.md` 9-Rollen-Matrix aus Mail 07.05.
- `notion-token-setup.md` Lars 4-Schritte für Internal Connection Token

### 01-strategy/

Alles Strategische. Wo Lars die ICP-Entscheidung trifft, wo Vivid Vision liegt, wo strategische Decisions geloggt werden.

- `icp/template.md` Skeleton für ICP basierend auf Founder-Interviews
- `decisions/` Strategische Decisions mit 30-Tage Outcome-Review
- TBD: `vivid-vision-2028.md`, `strategic-marketplace-framework.md`, `positioning.md`

### 02-sales/

Sales-Pipeline, Outbound, CRM. Skripte für Pipeline-Pulls. ICP-Match-Logik.

- TBD: `pipeline.md`, `crm-bridge/`, `outbound-templates/`, `icp-match/`

### 03-marketing/

Content, Ads, Voice. Substack-Drafts, LinkedIn-Posts, Ad-Creatives, Landing-Pages.

- TBD: `voice/lars.md`, `voice/matteo.md`, `content/`, `ads/google/`, `ads/meta/`, `landing-pages/`

### 04-operations/

PM, Capa, Customers, Playbooks. Dieter-Hauptbereich plus Sprint-Plaene.

- `customers/` Pro Mandat ein Folder mit `profile.md`, geschrieben von Dieter plus Marketplace Manager
- `04-operations/customers/_TEMPLATE/profile.md` Skeleton für neue Mandate
- `04-operations/playbooks/` Operative Standards (Onboarding, PPC, Reporting, Handover, Escalation)
- `sprints/` 2-Wochen-Sprint-Plaene
- `sprints/2026-kw21-22-icp-kunden.md` Aktueller Sprint

### 05-meetings/

Alle Meeting-Notes. Strukturiert (von Chris oder Owner) plus Raw-Transkripte (Gemini/Otter).

- `2026-05-19-sprint-kickoff.md` Strukturierte Notes Sprint-Kickoff
- `raw/2026-05-19-gemini-notes.md` Original Gemini-Output zum Archivieren
- Konvention: `YYYY-MM-DD-thema.md` für strukturierte, `raw/YYYY-MM-DD-source.md` für Originale

### 06-finance/

P&L, Margin pro Mandat, Retainer-Tracking, Förderbudgets. **Restricted Bereich.**

- Lesen: Lars, Chris
- Schreiben: Lars
- Sub-Folder TBD

### 07-tech/

Brain-Architektur, Skripte, Skills, Workflows. Wo Chris plus Junior Dev arbeiten.

- `architecture.md` Drei-Ebenen-Architektur (GitHub plus Notion plus Dropbox)
- `github-conventions.md` Branch-Names, Commit-Messages, PR-Flow
- `notion-linking.md` Wie Notion-Pages strukturiert sind
- `dropbox-linking.md` Wie Dropbox-MCP verbindet
- `voice-rules.md` Globale Voice-Rules für alle AI-Outputs
- `decision-framework.md` Big-Decision-Framework
- `scripts/` Python-Skripte (notion_mirror_push.py, icp_match.py TBD, etc.)
- `skills/` Claude-Skills (relevio-dashboard, call-analytics, weitere TBD)
- `workflows/` AI-Workflow-Templates
- `memory/` Cross-Session Memory (MEMORY.md als Index)

### 08-knowledge/

Externes Wissen. Mentor-Referenzen, Industry-Patterns, Frameworks die Mala adaptiert.

- TBD: `marketplace-mentors/`, `industry-trends/`, `frameworks/`

### decks/

Pitches plus Praesentationen. Live-Deck unter https://chris1928a.github.io/mala-brain/decks/digital-twin/.

## Notion-Mirror Logik

Pro Top-Level-Ordner im Repo entsteht eine Top-Level-Page in Notion mit gleichem Namen plus Emoji. Sub-Folders werden zu Sub-Pages. Markdown-Files werden zu Notion-Pages mit dem File-Inhalt als Body.

Mirror-Skript: `07-tech/scripts/notion_mirror_push.py`. Erwartet `NOTION_TOKEN` (von Lars) plus `NOTION_PARENT_PAGE_ID` (PM-Page in Mala-Notion).

| Repo-Ordner | Notion-Emoji | Notion-Title |
|---|---|---|
| `00-start-here/` | 🚀 | 00 Start Here |
| `01-strategy/` | 🎯 | 01 Strategy |
| `02-sales/` | 💼 | 02 Sales |
| `03-marketing/` | 📣 | 03 Marketing |
| `04-operations/` | ⚙️ | 04 Operations |
| `05-meetings/` | 📝 | 05 Meetings |
| `06-finance/` | 💰 | 06 Finance |
| `07-tech/` | 🔧 | 07 Tech |
| `08-knowledge/` | 📚 | 08 Knowledge |
| `decks/` | 🎤 | Decks |
| `PROJECT-MANAGEMENT.md` | 📋 | Project Management Plan |

## Wenn etwas neu dazu kommt

1. Erst in `STRUCTURE.md` aufnehmen
2. Dann den passenden Folder befüllen (oder neuen Folder mit nächster Nummer)
3. PR machen, Chris reviewed Architektur-Fragen, Lars/Matteo reviewen Content
4. Nach Merge: `notion_mirror_push.py` rerun, damit Notion-Mirror auf neuestem Stand

Stand: 19.05.2026.
