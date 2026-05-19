# mala brain - v3 Cloud-Architektur Template

> **Gesamtplan-Vision:** [Mala Digital Company Twin Deck](https://chris1928a.github.io/mala-brain/decks/digital-twin/) (16 Slides, 2-Jahres-Roadmap zum 500k-Mandat)
>
> **Master Project Management Plan:** [PROJECT-MANAGEMENT.md](PROJECT-MANAGEMENT.md) (alles was wir tracken, Status pro Task, Owner, Deadlines)
>
> **Repo-Struktur und Notion-Mapping:** [STRUCTURE.md](STRUCTURE.md) (9 Top-Level-Ordner, jeder spiegelt sich in Notion)
>
> **Neu im Team? Start hier:** [00-start-here/](00-start-here/) (Onboarding, Claude-Code-Setup, Workflow, Permissions)

---

## Hauptstruktur

| Ordner | Was lebt hier | Notion |
|---|---|---|
| [`00-start-here/`](00-start-here/) | Onboarding, Setup, Permissions | 🚀 00 Start Here |
| [`01-strategy/`](01-strategy/) | Vision, ICP, Strategy Decisions, Positioning | 🎯 01 Strategy |
| [`02-sales/`](02-sales/) | Pipeline, Outbound, CRM-Bridges, ICP-Match | 💼 02 Sales |
| [`03-marketing/`](03-marketing/) | Content, Ads, Voice-Library, Landing-Pages | 📣 03 Marketing |
| [`04-operations/`](04-operations/) | Customers, Playbooks, Sprints (Dieter-Hauptbereich) | ⚙️ 04 Operations |
| [`05-meetings/`](05-meetings/) | Meeting-Notes plus Raw-Transkripte | 📝 05 Meetings |
| [`06-finance/`](06-finance/) | P&L, Margin, Retainer (restricted) | 💰 06 Finance |
| [`07-tech/`](07-tech/) | Brain-Architektur, Skripte, Skills, Workflows | 🔧 07 Tech |
| [`08-knowledge/`](08-knowledge/) | Externes Wissen, Mentor-Referenzen, Frameworks | 📚 08 Knowledge |
| [`decks/`](decks/) | Pitches plus Praesentationen | 🎤 Decks |

---


Brain-Architektur-Template für mala markets, abgeleitet aus Christoph Erlers Brain v3 Setup. Single Source of Truth für alle AI-Assistenten, Skills und Workflows.

## Was ist das?

Dieses Repository ist die zentrale Architektur für mala. Alle AI-Outputs, Skills, Memories und Cloud-Code-Workflows laufen über diese Struktur. Ziel: 20–30 % höhere AI-Effizienz durch saubere Architektur.

## Why & How (Garry Tan Architektur-Pattern)

Die Architektur folgt dem von Garry Tan (Y Combinator) im April 2026 öffentlich validierten 3-Layer-Pattern: **Fat Skills + Thin Harness + Deterministic Glue**.

Quelle: https://x.com/garrytan/status/2042925773300908103

**Die fünf Definitionen:**

1. **Fat Skills:** Domänen-Logik, Voice-Rules, Decision-Frameworks leben in Skills (in `skills/`). Jeder Skill ist ein eigenständiges, wiederverwendbares Modul mit klaren Triggern und Outputs.
2. **Thin Harness:** Cloud Code ist der minimale Orchestrator. Er lädt Skills nur on-demand, verkettet sie nicht, hält keinen Eigenstate. Was Cloud kann, kommt aus den Skills.
3. **Deterministic Glue:** Verbindungen zwischen Skills (GitHub-Repo, Notion-Pages, Dropbox-Files) sind explizit, dokumentiert, reproduzierbar. Keine versteckten Cloud-Memorys oder ChatGPT-Conversations als Knowledge-Layer.
4. **Single Source of Truth:** Pro Information genau ein Speicherort. GitHub für Architektur, Notion für Wissen, Dropbox für Long-Form. Keine Duplikate, keine parallelen Wahrheiten.
5. **Modell-Agnostik:** Skills und Memory sind unabhängig vom AI-Modell. Wenn Sonnet 5.0 kommt, switchen wir das Modell, nicht die Skills.

**Warum dieser Pattern für mala?**

- Verhindert Vendor-Lock-in (kein WeWeb/Xano-Hostage)
- Ermöglicht Skill-Sharing über das Team (war vorher das Problem: Lars und Matteo hatten Skills nur lokal in Cloud-Webapp)
- Macht AI-Modell-Upgrades trivial (in 30 Min statt 3 Wochen)
- Skaliert mit Junior-Hires (sie lesen `CLAUDE.md` + `07-tech/architecture.md` und können sofort starten)
- 20–30 % höhere AI-Effizienz durch sauberen Kontext (Cloud bekommt nur was relevant ist, kein Müll)

**EO Exchange 11.05.2026:** Christoph hält dazu einen Vortrag mit dem Garry-Tan-Pattern als Backbone. Live-Demo mit Brain v3.

## Drei-Ebenen-Architektur

```
GitHub (Datenspeicher / Architektur)
   ↓
Notion (Wissens- und Informationsspeicher)
   ↓
Dropbox (nur Dateien / Long-Form Content)
```

**Flow für jeden Skill:**
1. Skill startet in Cloud Code
2. Cloud liest GitHub (diese Repo), findet Notion-Page-Link
3. Cloud liest Notion-Page, findet Dropbox-File-Link (wenn nötig)
4. Cloud arbeitet mit nur den relevanten Files, ohne Müll-Kontext

## Stand 19.05.2026

Aktueller Sprint: KW21+22, Repo plus Notion-Mirror Kollab-Test mit Dieter. Sprint-Plan in [04-operations/sprints/2026-kw21-22-icp-kunden.md](04-operations/sprints/2026-kw21-22-icp-kunden.md).

Letzter Call: [05-meetings/2026-05-19-sprint-kickoff.md](05-meetings/2026-05-19-sprint-kickoff.md). Decisions in [01-strategy/decisions/2026-05-19-sprint-kickoff.md](01-strategy/decisions/2026-05-19-sprint-kickoff.md).

## Quick-Reference

- **Onboarding für neue Team-Member:** [00-start-here/onboarding.md](00-start-here/onboarding.md)
- **Dieter Setup (Anfänger):** [00-start-here/dieter-claude-code-setup.md](00-start-here/dieter-claude-code-setup.md)
- **Dieter Workflow:** [00-start-here/dieter-workflow.md](00-start-here/dieter-workflow.md)
- **Team-Permissions (9 Rollen):** [00-start-here/team-permissions.md](00-start-here/team-permissions.md)
- **Notion-Token Setup (Lars):** [00-start-here/notion-token-setup.md](00-start-here/notion-token-setup.md)
- **ICP-Template (Lars):** [01-strategy/icp/template.md](01-strategy/icp/template.md)
- **Decisions-Log:** [01-strategy/decisions/](01-strategy/decisions/)
- **Aktueller Sprint:** [04-operations/sprints/2026-kw21-22-icp-kunden.md](04-operations/sprints/2026-kw21-22-icp-kunden.md)
- **Meeting-Notes:** [05-meetings/](05-meetings/)
- **Architektur:** [07-tech/architecture.md](07-tech/architecture.md)
- **Voice-Rules:** [07-tech/voice-rules.md](07-tech/voice-rules.md)
- **Notion-Verlinkung:** [07-tech/notion-linking.md](07-tech/notion-linking.md)
- **Dropbox-Verlinkung:** [07-tech/dropbox-linking.md](07-tech/dropbox-linking.md)
- **Memory-Index:** [07-tech/memory/MEMORY.md](07-tech/memory/MEMORY.md)
- **Notion-Push-Skript:** [07-tech/scripts/notion_mirror_push.py](07-tech/scripts/notion_mirror_push.py)
- **Pitch-Deck:** [chris1928a.github.io/mala-brain/decks/digital-twin/](https://chris1928a.github.io/mala-brain/decks/digital-twin/)

## Wichtige Voice-Rules (Auszug)

- Deutsche Umlaute Pflicht: ä ö ü ß. NIE ae oe ue ss als Ersatz.
- Keine Em-Dashes. Stattdessen Komma, Punkt, Bindestrich.
- "mala markets" immer kleingeschrieben.
- Keine AI-Phrasen ("sicherlich", "zweifellos", "großartige Frage").
- Direkt, knapp, natürlich. Wie ein Mensch schreiben.

Volle Voice-Rules: [07-tech/voice-rules.md](07-tech/voice-rules.md)

## Updates

Diese Architektur ist Living-Doc. Updates kommen über GitHub-Pull-Requests, größere Strukturänderungen via Notion-Decision-Page mit Co-Sign Lars + Matteo.

---

**Aufgesetzt:** 27.04.2026 von Christoph Erler für mala markets
**Owner:** Lars Seuß + Matteo Giazzi
**Aktuell:** v3 (Cloud Code Era, post-N8N)
