# Mala-Brain Onboarding

Wie Lars, Matteo, Dieter und der Junior Dev mit dem Mala-Brain arbeiten. Schritt-für-Schritt.

## Was ist das Mala-Brain?

GitHub-Repo `chris1928a/mala-brain` als Master Truth für die Firma. Alle Decisions, Prozesse, Voice-Rules, Skripte, Architektur-Entscheidungen liegen hier versioniert. Notion ist das Spiegel-UI fürs Team, Dropbox ist Bulk-Storage für große Files.

Drei Schichten:

1. **GitHub** = Datenspeicher und Architektur. Hier passiert die Wahrheit.
2. **Notion** = Wissens- und PM-Speicher. Hier liest und schreibt das Team im Alltag.
3. **Dropbox** = Files und Long-Form-Content. Hier liegen Recordings, Briefings, Customer-Files.

## Setup pro Person

### Schritt 1, GitHub Repo lokal

1. Email-Einladung von GitHub annehmen (kommt von chris1928a)
2. GitHub Desktop installieren: https://desktop.github.com
3. Mit eurem GitHub-Account einloggen
4. `Clone Repository` → `chris1928a/mala-brain` auswählen → Ordner aussuchen → Clone

Wenn ihr lieber Terminal nutzt:

```bash
git clone https://github.com/chris1928a/mala-brain.git
cd mala-brain
```

### Schritt 2, Claude Code installieren

1. Claude Code aus dem Anthropic-Account oder lokal: https://claude.com/code
2. Im mala-brain Ordner Claude Code öffnen
3. Bei der ersten Frage: einmal `claude` tippen, dann Setup-Wizard durchklicken
4. CLAUDE.md im Repo wird automatisch geladen, das gibt Claude den ganzen Kontext

### Schritt 3, Notion-Workspace verbinden

1. Im Mala-Notion-Workspace die Hauptseite öffnen
2. Rechts oben `...` → `Connections` → `Add connections` → `Claude` auswählen
3. Bestätigen. Damit kann Claude lesen und schreiben in den Pages, die ihr explizit teilt.

Wenn `Claude` in der Connection-Liste fehlt: einmal `Settings` → `Connections` → `Browse connections` → Claude finden → `Connect`. Dann zurück zu Schritt 1.

### Schritt 4, Dropbox-Linking

Dropbox ist verbunden über Dropbox-MCP (Beta). Setup-Anleitung in `07-tech/dropbox-linking.md`.

## Tägliche Arbeitsweise

### Was ihr ins Brain einspielt (Push)

- **Pull Requests gegen `main`.** Jede Rolle macht eine Branch, pusht, öffnet einen PR. Lars merged. Audit-Trail bleibt.
- **Notion-Pages.** Schreibt direkt in eure Notion-Bereiche (Strategie / Vertrieb / Marketing / Operations). Claude liest sie ohne explizites Sync.
- **Meeting-Transkripte.** Werden im designierten Notion-Folder abgelegt (TBD nach Notion-Setup). Claude parst sie automatisch beim nächsten Sprint-Call.

### Was ihr aus dem Brain bekommt (Pull)

- **Frame-checked Antworten.** Fragt Claude direkt in Slack oder im Meeting: "Was sagt das Brain zu Kunde X?" Twin pullt alle Layer, antwortet in 20 Sekunden.
- **Drafts im Lars- oder Matteo-Voice.** Customer-Replies, LinkedIn-Posts, Website-Updates. Pattern-checked gegen die Voice-Library.
- **Daily Brief.** Morgens 7:00 Slack-Nachricht mit Pipeline-Stand, Risk-Flags, OKR-Drift, Decisions die heute anstehen.

## Wochenrhythmus

- **Montag:** Sprint-Call 9:00, Wochenfokus festlegen, Aktivitäten verteilen.
- **Mittwoch:** Mid-Week-Check, Brain-Pull für offene Decisions.
- **Freitag:** Cowork-Session mit Chris (für die Sprint-Dauer). Brain live, vergangene Woche reviewen, Risks dieser Woche surface, neuer Twin-Output gedraftet.

## Häufige Fragen

**Wie pushe ich eine Decision rein?**

1. Branch erstellen: `git checkout -b decision/<kurzes-thema>`
2. Markdown-File in `decisions/YYYY-MM-DD-<thema>.md` anlegen mit dem Frame-Output von Claude
3. Commit + Push
4. PR auf GitHub eröffnen, Lars als Reviewer

**Wie ändere ich eine Voice-Rule?**

PR gegen `07-tech/voice-rules.md`. Lars und Matteo beide reviewen. Nach Merge ist die Regel sofort aktiv für alle Drafts.

**Wie sehe ich was sich diese Woche im Brain geändert hat?**

```bash
git log --since="1 week ago" --oneline
```

Oder in GitHub: `Pulse` Tab vom Repo.

**Was wenn ich Notion-Edit-Rechte nicht habe?**

Frag Lars oder Matteo. Permissions stehen in `00-start-here/team-permissions.md`.

## Bei Problemen

- Setup hängt: kurz Chris pingen im Mala-Slack
- Claude antwortet seltsam: prüf ob CLAUDE.md geladen ist (sollte beim ersten Hello-Output sichtbar sein)
- GitHub-Permissions stimmen nicht: Lars fragen, oder Issue im Repo öffnen

## Pflichtlektüre vor erstem Push

1. `CLAUDE.md` (Sprache, Voice-Rules, Architektur-Hierarchie)
2. `07-tech/voice-rules.md` (Schreibstil)
3. `00-start-here/team-permissions.md` (was darf ich)
4. `04-operations/sprints/` (aktueller Sprint-Plan)

Letzter Stand: 19.05.2026.
