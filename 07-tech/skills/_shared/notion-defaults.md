# Notion Defaults für alle Skills

Default-Notion-Verlinkungen die jeder Skill kennen sollte. Wird aus `_shared/` geladen.

## mala Notion-Workspace Top-Level

(URLs werden eingetragen sobald Workspace strukturiert ist)

| Department | Notion-URL |
|---|---|
| 01 Strategy | TBD |
| 02 Sales | TBD |
| 03 Marketing | TBD |
| 04 Operations | TBD |
| 05 Tech | TBD |
| 06 People | TBD |

## Cross-Skill Pages

Pages die mehrere Skills referenzieren:

| Page | URL | Verwendet von |
|---|---|---|
| BHAG 2040 | TBD | strategy, decision |
| Vivid Vision 2028 | TBD | strategy, sales, marketing |
| ICP Master | TBD | sales, marketing, icp-extractor |
| P03 Listing-Optimierung | TBD | relevio-dashboard, operations |
| Brain v3 Architektur | TBD | tech, all skills |

## Setup-Schritte (einmalig nach Notion-Workspace-Aufbau)

1. Lars + Matteo strukturieren Notion-Workspace nach `07-tech/notion-linking.md`
2. URLs in dieses File eintragen
3. Skill-Frontmatter URLs aktualisieren (sed-replace TBD-URLs)
4. Test-Run mit einem Skill um Verlinkung zu validieren

## Notion-API-Token

Token liegt in GitHub Secrets als `NOTION_TOKEN`. Cloud nutzt MCP-Tool für Notion-Zugriff.

Wichtig: Internal-Integration in Notion erstellen, NICHT Member-Account-Upgrade.
- Settings, Integrations, New Integration
- Name: "mala-cloud-integration"
- Capabilities: Read content, Update content, Insert content, Read user info
- Token kopieren in GitHub Secrets
- Pages mit Integration sharen (jede Page einzeln)
