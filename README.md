# mala brain - v3 Cloud-Architektur Template

Brain-Architektur-Template für mala markets, abgeleitet aus Christoph Erlers Brain v3 Setup. Single Source of Truth für alle AI-Assistenten, Skills und Workflows.

## Was ist das?

Dieses Repository ist die zentrale Architektur für mala. Alle AI-Outputs, Skills, Memories und Cloud-Code-Workflows laufen über diese Struktur. Ziel: 20–30 % höhere AI-Effizienz durch saubere Architektur.

## Why & How (Garry Tan Architektur-Pattern)

Die Architektur folgt dem von Garry Tan (Y Combinator) im April 2026 öffentlich validierten 3-Layer-Pattern: **Fat Skills + Thin Harness + Deterministic Glue**.

Quelle: https://x.com/garrytan/status/2042925773300908103

**Die fünf Definitionen:**

1. **Fat Skills:** Domänen-Logik, Voice-Rules, Decision-Frameworks leben in Skills (in `skills/`). Jeder Skill ist ein eigenständiges, wiederverwendbares Modul mit klaren Triggern und Outputs.
2. **Thin Harness:** Cloud Code ist der minimale Orchestrator. Er lädt Skills nur on-demand, verkettet sie nicht, hält keinen Eigenstate. Was Cloud kann, kommt aus den Skills.
3. **Deterministic Glue:** Verbindungen zwischen Skills (GitHub-Repo, Notion-Pages, Drive-Files) sind explizit, dokumentiert, reproduzierbar. Keine versteckten Cloud-Memorys oder ChatGPT-Conversations als Knowledge-Layer.
4. **Single Source of Truth:** Pro Information genau ein Speicherort. GitHub für Architektur, Notion für Wissen, Drive für Long-Form. Keine Duplikate, keine parallelen Wahrheiten.
5. **Modell-Agnostik:** Skills und Memory sind unabhängig vom AI-Modell. Wenn Sonnet 5.0 kommt, switchen wir das Modell, nicht die Skills.

**Warum dieser Pattern für mala?**

- Verhindert Vendor-Lock-in (kein WeWeb/Xano-Hostage)
- Ermöglicht Skill-Sharing über das Team (war vorher das Problem: Lars und Matteo hatten Skills nur lokal in Cloud-Webapp)
- Macht AI-Modell-Upgrades trivial (in 30 Min statt 3 Wochen)
- Skaliert mit Junior-Hires (sie lesen `CLAUDE.md` + `docs/architecture.md` und können sofort starten)
- 20–30 % höhere AI-Effizienz durch sauberen Kontext (Cloud bekommt nur was relevant ist, kein Müll)

**EO Exchange 11.05.2026:** Christoph hält dazu einen Vortrag mit dem Garry-Tan-Pattern als Backbone. Live-Demo mit Brain v3.

## Drei-Ebenen-Architektur

```
GitHub (Datenspeicher / Architektur)
   ↓
Notion (Wissens- und Informationsspeicher)
   ↓
Drive (nur Dateien / Long-Form Content)
```

**Flow für jeden Skill:**
1. Skill startet in Cloud Code
2. Cloud liest GitHub (diese Repo), findet Notion-Page-Link
3. Cloud liest Notion-Page, findet Drive-File-Link (wenn nötig)
4. Cloud arbeitet mit nur den relevanten Files, ohne Müll-Kontext

## Folder-Struktur

| Folder | Zweck |
|---|---|
| `docs/` | Architektur-Doku, Voice-Rules, Linking-Konventionen |
| `skills/` | Alle mala-Skills, jeder Skill hat eigenes Folder mit `SKILL.md` |
| `skills/_shared/` | Geteilte Voice-Rules und Notion-Defaults für alle Skills |
| `scripts/` | Python/Shell-Scripts für Automation |
| `memory/` | Cross-Session Memory-Files (MEMORY.md als Index) |
| `workflows/` | Wiederverwendbare AI-Workflows (z. B. Call-Analytics) |
| `.claude/` | Cloud Code Settings + Project-Level CLAUDE.md |

## Setup-Schritte für Lars und Matteo

1. Diesen Folder als GitHub-Repo nach `mala-markets/mala-brain` pushen (private)
2. Notion-Workspace strukturieren nach `docs/notion-linking.md`
3. Drive-Folder strukturieren nach `docs/drive-linking.md`
4. Cloud Code Setup: bei jedem mala-Repo `CLAUDE.md` referenzieren
5. Voice-Rules aus `docs/voice-rules.md` in alle AI-Skills übernehmen
6. Skill-Templates in `skills/relevio-dashboard/` und `skills/call-analytics/` als Vorlage nutzen

## Quick-Reference

- **Voice-Rules (für jeden AI-Output):** [docs/voice-rules.md](docs/voice-rules.md)
- **Architektur-Doku:** [docs/architecture.md](docs/architecture.md)
- **Notion-Verlinkung:** [docs/notion-linking.md](docs/notion-linking.md)
- **Drive-Verlinkung:** [docs/drive-linking.md](docs/drive-linking.md)
- **Memory-Index:** [memory/MEMORY.md](memory/MEMORY.md)

## Wichtige Voice-Rules (Auszug)

- Deutsche Umlaute Pflicht: ä ö ü ß. NIE ae oe ue ss als Ersatz.
- Keine Em-Dashes (-). Stattdessen Komma, Punkt, Gedankenstrich (–).
- "mala markets" immer kleingeschrieben.
- Keine AI-Phrasen ("sicherlich", "zweifellos", "großartige Frage").
- Direkt, knapp, natürlich. Wie ein Mensch schreiben.

Volle Voice-Rules: [docs/voice-rules.md](docs/voice-rules.md)

## Updates

Diese Architektur ist Living-Doc. Updates kommen über GitHub-Pull-Requests, größere Strukturänderungen via Notion-Decision-Page mit Co-Sign Lars + Matteo.

---

**Aufgesetzt:** 27.04.2026 von Christoph Erler für mala markets
**Owner:** Lars Seuß + Matteo Giazzi
**Aktuell:** v3 (Cloud Code Era, post-N8N)
