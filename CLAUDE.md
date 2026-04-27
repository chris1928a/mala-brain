# CLAUDE.md - mala markets Project Rules

Project-level Cloud-MD für mala markets. Wird bei jedem Cloud Code Start automatisch geladen.

## Sprache und Umlaute (PFLICHT)

- IMMER deutsche Umlaute: ä ö ü Ä Ö Ü ß
- NIE ae oe ue ss als Ersatz
- Gilt für ALLE Outputs: Text, Code-Kommentare, Emails, Drafts, Notion-Pages, GitHub-Commits
- Texte ohne Umlaute = unprofessionell und sofort als AI erkennbar

## Anti-AI-Schreibstil (PFLICHT)

- KEINE Em-Dashes (-). Stattdessen Komma, Punkt oder Gedankenstrich (–)
- KEINE AI-Phrasen: "sicherlich", "zweifellos", "durchaus", "gewiss", "in der Tat", "großartige Frage"
- KEINE Wiederholung des User-Inputs als Einleitung
- KEIN Enthusiasmus ("Großartige Frage!", "Absolut!")
- Direkt, knapp, natürlich. Wie ein Mensch.

## Brand

- "mala markets" immer kleingeschrieben (auch am Satzanfang in Lauftexten, soweit grammatikalisch möglich)
- "Relevio" ist ein interner Tool-Name, mit Großbuchstaben
- "Brain v3" ist die aktuelle Architektur-Version

## Architektur-Hierarchie (für Cloud)

Bei jedem Skill und Workflow:

1. Lese GitHub-Repo Struktur (dieses Repo)
2. Folge Notion-Page-Links für Wissen und Prozesse
3. Greife Dropbox-Files nur wenn explizit verlinkt

NIE alle Dropbox-Files in den Kontext laden. NIE Notion-Pages dupliziert in GitHub. NIE GitHub-Code in Notion kopieren.

## Memory

Cross-Session Memory liegt in `memory/MEMORY.md` (Index) plus einzelne Memory-Files. Keine Memories über Code-Patterns, Git-History, oder ephemeral Tasks. Fokus: User-Profile, Feedback, Project-State, External-References.

## Notion-Schreiben

- IMMER mit echten Newlines (NIE \n als Escape)
- IMMER voller Inhalt (NIE Verweise auf lokale .md Dateien)
- NIE archivieren oder löschen ohne explizite User-Anweisung
- NIE allow_deleting_content ohne explizite User-Bestätigung

## Decisions

Große Entscheidungen via Big Decision Framework (Six Thinking Hats + Strategic Reflection). Template in `docs/decision-framework.md`.

## Skill-Konvention

Jeder Skill hat:
- `SKILL.md` (Trigger-Beschreibung + Voice-Reference)
- `references/` (optionale Referenz-Files)
- Eindeutige Notion-Page als Knowledge-Anker
- Eindeutige Dropbox-Folder wenn Long-Form Content nötig

Skills triggern auf Keywords. Triggers stehen im Frontmatter der SKILL.md.

## Stack

- AI-Models: Claude Sonnet 4.6 (default), Claude Opus 4.7 (für komplexe Decisions)
- Backend (P03 Phase 1): VM-Stack-Skelett (WeWeb + Xano + n8n zu Full-Code), Phase 2 Custom-Stack TBD
- Frontend (P03): TBD nach VM-Phase-1
- Memory: GitHub + Notion (Open API) + Dropbox (files only)
- Automation: NICHT N8N (deprecated). Server-gehostete Cloud-Code-Workflows.

## Out-of-Scope für AI

- Keine Investment- oder Finanzberatung
- Keine Trades, Käufe, Money-Transfers
- Keine destructive Git-Operations ohne User-Approval
- Keine permanenten Löschungen (Notion-Archive, Dropbox-Trash)
- Keine Modifikation von Security-Permissions ohne explizite User-Anweisung
