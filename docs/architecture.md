# mala Brain v3 Architektur

## Vision

Saubere, modulare AI-Architektur für mala markets. Single Source of Truth für alle Skills, Workflows und Memories. Vermeidet Vendor-Lock-in, ermöglicht schnelles AI-Modell-Upgrade (Sonnet 4.6 zu 4.7 zu 5.0).

## Drei-Ebenen-System

```
                    ┌──────────────────────────────────┐
                    │   GitHub (mala-markets/mala-brain)│
                    │   = Architektur + Skills + Code  │
                    │   = Single Source of Truth       │
                    └──────────────┬───────────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────────────┐
                    │   Notion (mala Workspace)        │
                    │   = Wissen + Prozesse + Meetings │
                    │   = Living Documentation         │
                    └──────────────┬───────────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────────────┐
                    │   Dropbox (mala Dropbox)         │
                    │   = nur Long-Form Files          │
                    │   = Copy, Briefings, PDFs        │
                    └──────────────────────────────────┘
```

## Ebene 1: GitHub

**Was lebt hier:**
- Diese gesamte Architektur-Repo (`mala-brain`)
- Cloud Code Skills (`skills/`)
- Project-Level CLAUDE.md
- Voice-Rules
- Workflows
- Scripts
- Memory-Files
- Settings

**Was NICHT hier lebt:**
- Long-Form Copy (geht in Dropbox)
- Meeting-Notes (gehen in Notion)
- Kundendaten (gehen in Notion oder Dropbox je nach Sensitivität)

**Regel:** GitHub ist die Architektur, nicht der Inhalt. Inhalte werden über Links (Notion-URL, Dropbox-URL) referenziert.

## Ebene 2: Notion

**Was lebt hier:**
- Meeting-Notes (mit Datum-Subseiten)
- Prozess-Dokumentation (P01–P08)
- Strategische Docs (BHAG, VVM, Jahresplan)
- Kunden-Onboarding-Pages
- Team-Knowledge-Base
- Decision-Frameworks (gefüllte Templates)
- Training Materials

**Verlinkungs-Regel:**
- Skills in GitHub referenzieren Notion-Pages über URL
- Notion-Pages referenzieren Dropbox-Files über URL
- KEIN Inhalt wird über mehrere Ebenen dupliziert

**Notion-Konvention:**
- Top-Level: Departments (Sales, Marketing, Operations, Tech, Strategy)
- Subseiten: Konkrete Prozesse, Meetings, Projekte
- Tags: Status (Active, Archived, Decision Pending)

## Ebene 3: Dropbox

**Was lebt hier:**
- Long-Form Copy (Sales-Pitches, Case-Studies)
- Kunden-Briefings
- PDFs (Verträge, Förder-Dokumente)
- Bilder, Slides, Videos
- Excel-Tabellen mit Rohdaten

**Was NICHT hier lebt:**
- Strukturierte Wissens-Pages (gehen in Notion)
- Code (geht in GitHub)
- AI-Prompts (gehen in Skills)

**Regel:** Dropbox ist nur für Files, die Notion nicht halten kann. Jeder Dropbox-File wird in einer Notion-Page verlinkt, sonst ist er nicht auffindbar für Cloud.

## Cloud-Code-Flow

```
User: "Optimiere Listing für Produkt XYZ"
  ↓
Cloud Code (in mala-brain Repo)
  ↓ liest CLAUDE.md, Voice-Rules
  ↓ findet Skill: skills/relevio-dashboard/SKILL.md
  ↓ liest Skill-Frontmatter
  ↓ findet Notion-Page-Link für P03-Prozess-Doku
  ↓ liest Notion-Page für aktuelle Spec + Edge-Cases
  ↓ findet Dropbox-File-Link für Briefing-Vorlage
  ↓ liest Dropbox-File NUR wenn nötig
  ↓
  Output mit Voice-Rules zu User
```

## Memory-System

Cross-Session Memory liegt in `memory/`. Index ist `MEMORY.md` (max 200 Zeilen). Pro Memory-Topic ein eigenes Markdown-File.

**Memory-Typen:**
- `user_*.md`: User-Profile, Preferences
- `feedback_*.md`: Korrekturen, Confirmations
- `project_*.md`: Aktuelle Initiativen, Deadlines, Stakeholder
- `reference_*.md`: Pointer auf externe Systeme (Notion-Page-IDs, Dropbox-Folder-Paths)

**Was NICHT in Memory:**
- Code-Patterns (sind im Code)
- Git-History (sind in Git)
- Ephemeral Tasks (gehen in Todos, nicht Memory)
- Bereits in CLAUDE.md dokumentierte Regeln

## AI-Model-Wahl

| Use-Case | Model |
|---|---|
| Standard-Tasks (Email-Drafts, Notion-Notes, Listing-Optimierung) | Claude Sonnet 4.6 |
| Big Decisions, Code-Reviews, Architektur-Entscheidungen | Claude Opus 4.7 |
| Schnelle Bulk-Operations | Claude Haiku 4.5 |

Switch-Logik liegt in `skills/_shared/model-selection.md` (TBD).

## Upgrade-Pfad

Wenn neues Claude-Model rauskommt (Sonnet 5.0 etc.):
1. Update Frontmatter in betroffenen Skills
2. Test-Run mit Sample-Input
3. Wenn Output-Qualität ok: Default-Switch
4. Memory bleibt unverändert (modell-agnostisch)
5. Notion-Pages bleiben unverändert

Architektur ist so designed, dass AI-Model-Switch < 30 Min Migration kostet.

## Sicherheit

- Alle Token (Amazon SP-API, Notion, Dropbox) im GitHub Secrets, NICHT im Code
- DSGVO: Customer-Data in Notion oder Dropbox, nicht im Code
- 2FA für GitHub, Notion, Dropbox Accounts der Founders
- Repo ist private, nur Lars + Matteo + Chris haben Zugriff (+ ggf. Junior-Hire later)
