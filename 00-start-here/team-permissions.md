# Team-Permissions mala markets

Basiert auf Lars' Berechtigungs-Mail vom 07.05.2026. Gilt für GitHub-Repo (`chris1928a/mala-brain`), Notion-Workspace und alle Brain-Outputs.

## Rollen-Matrix

| Person | Rolle | GitHub | Notion | Brain-Output | Kunden-Zahlen |
|---|---|---|---|---|---|
| **Lars Seuß** | Co-Founder, Strategie + Sales + Finanzen | Admin | Full Edit | Voll | Voll |
| **Matteo Giazzi** | Co-Founder, Operations + Marketing | Admin | Full Edit | Voll | Voll |
| **Dieter** | PM, Controlling, Kapazitätsplanung | Write | Full Edit auf Kunden-Pages | Voll auf Mandate | Voll |
| **Jerome** | Marketplace Manager | Write auf eigene Mandate | Edit auf Kunden-Pages | Mandate-spezifisch | Nein |
| **Clarissa** | Marketplace Manager | Write auf eigene Mandate | Edit auf Kunden-Pages | Mandate-spezifisch | Nein |
| **Nick** | Marketplace Manager | Write auf eigene Mandate | Edit auf Kunden-Pages | Mandate-spezifisch | Nein |
| **Leon** | Marketplace Manager | Write auf eigene Mandate | Edit auf Kunden-Pages | Mandate-spezifisch | Nein |
| **Fabian** | Praktikant Marketplace Manager | Read-only auf Mandate | Read auf Kunden-Pages | Read | Nein |
| **Laureen** | Assistentin + Marketing Manager | Write auf Marketing-Branches | Full Edit auf Marketing-Pages | Marketing-Output voll | Nein |
| **Junior Dev (TBD)** | KI-Stelle, Brain-Maintenance | Write | Read + Brain-Schreiben | Schreibrechte auf Skripte und Workflows | Read |
| **Chris Erler** | Externer Architekt | Admin | Full Edit | Voll | Voll (für Architektur-Audit) |

## GitHub-Branchen-Regeln

- `main`: Lars und Matteo dürfen mergen. Chris darf reviewen + mergen für Architektur-PRs.
- `feature/<name>`: Jede Rolle darf eigene Feature-Branches anlegen.
- `customer/<kundenname>`: nur Marketplace Manager der dem Kunden zugeordnet ist plus PM Dieter.
- `marketing/<thema>`: nur Laureen plus Co-Founder.
- Reviews: 1-Reviewer-Minimum für `main`-Merges. Architektur-Reviews durch Chris.

## Notion-Bereichs-Regeln

- **Strategie**: Co-Founder + Chris voll. Dieter Read.
- **Vertrieb**: Co-Founder + Dieter voll. Marketplace Manager Read.
- **Marketing**: Co-Founder + Laureen voll. Andere Read.
- **Operations**: Co-Founder + Dieter voll. Marketplace Manager Edit auf eigene Bereiche.
- **Finance**: nur Lars + Chris.
- **Kunden-Mandate**: nur zugeordnete Marketplace Manager + Dieter + Co-Founder. Zahlen sind versteckt für Marketplace Manager und Praktikanten.

## Brain-Output-Sichtbarkeit

Twin-Outputs (Founder-Twin oder Team-Twin) zeigen Zahlen je nach Permission der anfragenden Person. Dieter sieht alle Kunden-Zahlen. Marketplace Manager sehen ihre Mandate ohne Margin- und P&L-Daten. Praktikant Fabian sieht nichts mit Zahlen.

Implementierung über `stress_detector.py` plus Permission-Check-Layer im Brain-Pull-Skript (TBD Phase 1).

## Audit

Permission-Änderungen werden als PR gegen diese Datei vorgeschlagen. Lars merged. Chris kann via GitHub-Audit-Log jederzeit nachvollziehen wer wann was geändert hat.

Letzter Stand: 19.05.2026.
