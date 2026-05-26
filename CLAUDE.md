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

Große Entscheidungen via Big Decision Framework (Six Thinking Hats + Strategic Reflection). Template in `07-tech/decision-framework.md`.

## Skill-Konvention

Jeder Skill hat:
- `SKILL.md` (Trigger-Beschreibung + Voice-Reference)
- `references/` (optionale Referenz-Files)
- Eindeutige Notion-Page als Knowledge-Anker
- Eindeutige Dropbox-Folder wenn Long-Form Content nötig

Skills triggern auf Keywords. Triggers stehen im Frontmatter der SKILL.md.

## Stack (Stand 19.05.2026, im Sprint-Kickoff gelockt)

- AI-Models: Claude Sonnet 4.6 (default), Claude Opus 4.7 (komplexe Decisions)
- Compute: Hetzner-Server für Cron-Jobs (ersetzt Make + n8n im kritischen Pfad)
- Master Truth: GitHub `chris1928a/mala-brain`
- Read-und-Write-UI für Team: Notion (PM-SSOT seit 19.05.)
- Bulk-Files: Dropbox (ab 27.04. statt Google Drive)
- Website: Migration WordPress zu Astro + GitHub + Render + Posthog (EO-Empfehlung 11.05.)
- Legacy: n8n + Airtable bleiben für Listings-Workflows, aus dem Brain-Pfad raus

## Sprint-Rhythmus (seit 19.05.2026)

- 2-Wochen-Sprints, ein Thema pro Sprint
- Sprint-Kickoff Mo der ersten Woche
- Mid-Sprint-Check Fr der ersten Woche
- Sprint-Review Mo der dritten Woche (gleichzeitig nächster Kickoff)
- Sprint-Pläne in `04-operations/sprints/`
- Decisions in `decisions/` mit 30-Tage Outcome-Review
- Meeting-Notes in `05-meetings/`

## Team-Rollen (Stand 07.05.2026)

- Lars Seuss = Strategie + Sales + Finanzen + Cashflow
- Matteo Giazzi = Operations + Marketing + Funnel
- Dieter = PM + Controlling + Kapazitaetsplanung
- Jerome, Clarissa, Nick, Leon = Marketplace Manager (kundenspezifisch ohne Zahlen)
- Fabian = Praktikant Marketplace (Read-only)
- Laureen = Assistentin + Marketing Manager (eigene Bahn)
- Junior Dev (KI-Stelle) = TBD, Profil GitHub + Python + Claude Code, Marcel als Kandidat

Volle Permission-Matrix in `00-start-here/team-permissions.md`.

## Out-of-Scope für AI

- Keine Investment- oder Finanzberatung
- Keine Trades, Käufe, Money-Transfers
- Keine destructive Git-Operations ohne User-Approval
- Keine permanenten Löschungen (Notion-Archive, Dropbox-Trash)
- Keine Modifikation von Security-Permissions ohne explizite User-Anweisung

## Anti-Drift Regeln (PFLICHT, ergänzt 26.05.2026)

Adressiert das Drift-Problem aus dem Meeting Lars/Matteo/Chris 26.05.2026: Claude Code wich gelegentlich in veraltete Ordner ab und arbeitete in alten Strukturen.

**Regel 1: Single Source of Truth ist dieses Repo (`chris1928a/mala-brain`).**
Beim Session-Start dieses CLAUDE.md zuerst lesen. Niemals auf veraltete lokale Kopien, alte Notion-Pages oder Dropbox-Subfolder zurückfallen. Wenn unklar wo Master liegt, im Repo prüfen, nicht raten.

**Regel 2: Working Directory IMMER verifizieren.**
Vor dem ersten Schreiben in einer Session: aktuelle Folder-Struktur prüfen (Top-Level-Listing). Nicht auf Annahmen verlassen wo der User sitzt oder welche Struktur grade gilt.

**Regel 3: Folder-Struktur ist gesetzt.**
Die 9 nummerierten Top-Level-Folder (`00-start-here` bis `08-knowledge`) plus `decks/` sind die einzigen erlaubten Top-Level-Buckets. Niemals selbst neue Top-Level-Folder anlegen ohne expliziten User-Auftrag. Niemals Files in Alt-Folder schreiben wenn neue Struktur existiert.

**Regel 4: Notion ist Read-und-Write-UI für Team, GitHub ist Master.**
Wenn etwas in Notion landen soll, Plan ist: erst hier im Repo, dann via Sync rüber. Direktes Notion-Schreiben nur in expliziten Notion-Workflows (Sprint-Board, PM-SSOT, Live-Operations).

**Regel 5: Drift-Konflikte nicht silent lösen.**
Wenn Claude einen Konflikt findet (z.B. Notion-Stand weicht von GitHub-Stand ab, oder Folder-Struktur passt nicht zur Doku): User melden und entscheiden lassen, nicht selbst einen Side-Branch fahren.

## Verwandte Repos

- `chris1928a/mala-shared` (privat): Gemeinsamer Workspace mit Chris für Audits, Meeting Notes, Decisions, Strategie-Docs. Lars und Matteo sind dort Collaborators. Audit-Antworten landen dort, nicht hier.
- `chris1928a/erler-brain` (privat): Chris' eigener Master Knowledge Base, Vorbild für dieses Repo.
