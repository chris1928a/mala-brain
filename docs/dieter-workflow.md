# Dieter Workflow

Wie Dieter im mala-brain Repo arbeitet. Format: was wo liegt, was Dieter bewegt, wie ein PR aussieht. Lehnt sich an wie Chris den RC-Brain für Raphael strukturiert hat.

## Wo Dieter arbeitet (Dieter-Bereiche)

| Folder | Was Dieter da macht | Wer reviewed |
|---|---|---|
| `customers/<kunde>/` | Pro Mandat ein Folder. Status, Capa, Decisions, Risk-Flags. | Lars für Pricing-Themen, Matteo für Execution |
| `playbooks/` | Operative Standards. Onboarding-Flow, PPC-Bid-Strategy, Reporting-Template. | Matteo |
| `docs/sprints/` | Sprint-Stand aktualisieren, Mid-Check, Retro | Lars + Matteo |
| `docs/meetings/` | Meeting-Notes nach jedem Termin | wer dabei war |
| `decisions/` | Decision-Logs für PM-Themen (Capa, Hire, Customer-Escalation) | Lars |

## Wo Dieter NICHT direkt schreibt

- `skills/` (das ist Brain-Code, da arbeiten Junior Dev und Chris)
- `scripts/` (Automation, Junior Dev plus Chris)
- `CLAUDE.md` (Founder-Approval)
- `decks/` (Pitches, Chris-Owner)
- Finance-Pages in Notion (Lars exklusiv)

## Standard-Workflow für jede Dieter-Aktion

```
1. git checkout main && git pull
2. git checkout -b pm/<kurzes-thema>
3. Datei editieren oder neu anlegen im Dieter-Bereich
4. git add <datei>
5. git commit -m "pm: <was sich geaendert hat>"
6. git push origin pm/<kurzes-thema>
7. PR auf GitHub eröffnen, Reviewer aus Permissions-Tabelle setzen
```

Wenn Dieter ein Mandat-Update macht:
- Branch: `customer/<kundenname>`
- Reviewer: Lars (Pricing) plus Matteo (Execution)

## Was Dieter in Notion macht

Notion ist die Lese-und-Schreib-Schicht für PM-Sachen. Dieter editiert direkt im Notion-Mala-Workspace folgende Bereiche:

- PM-Page (Mandate-Stand pro Kunde, Capa-Auslastung)
- Mandate-Sub-Pages (eine pro aktiven Kunden, gespiegelt aus customers/)
- Meeting-Notes (kommen via Mirror aus dem Repo, Dieter kann ergänzen)

Notion-Mirror wird sobald Schritt 1 durch via `scripts/notion_mirror_push.py` automatisch synct. Dieter muss nicht manuell spiegeln.

## Erste 3 Test-PRs für Dieter

Damit klar wird ob das System für Dieter funktioniert:

### PR 1, eigener customer-Folder anlegen

1. Such dir einen aktiven Mandat aus
2. Branch `customer/<kundenname>` anlegen
3. Folder `customers/<kundenname>/` mit `profile.md` (Template in `customers/_TEMPLATE/profile.md`) ausfüllen
4. PR mit Matteo als Reviewer

### PR 2, Playbook ergänzen

1. Such dir einen Mala-Standard-Prozess aus (z. B. Client-Onboarding)
2. Branch `pm/playbook-client-onboarding`
3. `playbooks/client-onboarding.md` füllen mit dem Schritt-für-Schritt wie ihr es heute macht
4. PR mit Matteo als Reviewer

### PR 3, eigene Capa-Auslastung als Decision-Log

1. Branch `pm/capa-week-21`
2. `decisions/2026-05-23-capa-week-21.md` mit kurzem Update: wer ist diese Woche an welchem Mandat
3. PR mit Lars als Reviewer

Wenn diese 3 PRs in KW21 mergen, ist das System für Dieter live.

## Bei Problemen

- Merge-Konflikte: nicht selber lösen, kurz Chris pingen
- Permissions stimmen nicht: Lars fragen, oder Issue im Repo
- Notion-Mirror zeigt alten Stand: `scripts/notion_mirror_push.py` neu laufen lassen
- Branch-Namen verwirrend: in diesem Doc oben nachschauen

Stand: 19.05.2026.
