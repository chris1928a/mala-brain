# 3-Level GitHub-Architektur

Aus Call 19.05.2026 zwischen Chris, Lars und Matteo. Wortlaut Chris im Chat 09:40:

> wir erstellen einen shared github folder Founder PM Dieter dann zweiter level Github fuer controlling Capa auslastung, alles resourcen kunden. Dritter level dann den Rest. Wir setzen 3 shared githubs auf, ich gebe euch anleitung auf die Architektur.

Drei separate Repos mit gestaffelten Zugriffsrechten. Jedes Level enthält was die Personen mit Zugriff brauchen, nicht mehr.

## Level 1, Founder plus PM

**Repo:** `chris1928a/mala-brain` (das hier, aktuell)
**Zugriff:** Lars, Matteo, Dieter, Chris

**Inhalt:**
- Strategie (ICP, Vision, Positioning, Decisions)
- PM (Sprints, Customers, Playbooks)
- Finance (P&L, Margin, Retainer)
- Tech-Architektur, Skripte, Skills
- Meetings, Decisions, Knowledge

Das ist die heute existierende 9-Folder-Struktur (00-start-here bis 08-knowledge plus decks).

## Level 2, Controlling plus Kunden plus Ressourcen

**Repo:** `chris1928a/mala-team-controlling` (neu, Phase 2 ab KW25)
**Zugriff:** Lars, Matteo, Dieter, alle Marketplace Manager (Jerome, Clarissa, Nick, Leon), Laureen

**Inhalt:**
- Kunden-Mandate-Details ohne Pricing (Marketplace Manager sehen Mandate, nicht P&L)
- Capa-Auslastung pro Marketplace Manager
- Ressourcen (Tool-Accounts, Logins, Templates ohne sensitive Daten)
- Playbooks fuer operative Standards
- Shared Marketing-Assets

**Permissions:**
- Marketplace Manager schreiben in eigene Mandate-Folder
- Dieter schreibt cross-Mandate fuer Capa-Tracking
- Founder approven Pricing-relevante Aenderungen

## Level 3, Rest

**Repo:** `chris1928a/mala-team` (neu, Phase 2 ab KW25)
**Zugriff:** alle 9 Rollen inkl. Praktikant Fabian

**Inhalt:**
- Team-Wide Knowledge (was alle wissen sollen)
- Onboarding-Materialien fuer neue Hires
- Allgemeine Voice-Rules
- Public Content-Library
- Non-sensitive Workflows

Hier landen Sachen die nicht confidential sind. Read-Default fuer alle, Write nach Permission.

## Cron-Sync zwischen den Levels

Aus Call 09:40:
> zweiter Schritt Cron jobs automation fuer updates euer Rechner github - (weekly). 1.1 Notion mirror - fuer transparenz und dass mitarbeiter lesen können was abgeht

Architektur Cron-Sync:
- **Lokale Rechner zu GitHub:** wöchentlicher Sync von Lars, Matteo, Dieter zum Master-Brain (Phase 1+2)
- **GitHub zu Notion:** Mirror via `07-tech/scripts/notion_mirror_push.py` (Cron auf Hetzner)
- **Level 1 zu Level 2 zu Level 3:** redaktioneller Sync, nicht automatisch (Founder entscheiden was sichtbar wird)

## Aktueller Stand (19.05.2026)

- Level 1: existiert (das hier, `chris1928a/mala-brain`)
- Level 2: TBD, Aufbau Phase 2 ab KW25
- Level 3: TBD, Aufbau Phase 2 ab KW25

Diese Woche (KW21) fokussieren wir nur Level 1 plus Dieter-Onboarding. Level 2 und 3 kommen wenn Level 1 sauber laeuft.

## Warum 3 Levels und nicht 1 Repo mit Permissions

Chris-Argument im Call:
- Klare Sichtbarkeits-Trennung statt "alles in einem Repo mit komplexen CODEOWNERS"
- Marketplace Manager sollen nicht versehentlich P&L-Daten sehen
- Praktikant Fabian soll nur das Team-Wide sehen
- Beim Hire-Onboarding klarer: ein Repo pro Berechtigungs-Stufe

Alternativ (Backup-Plan): wenn 3 Repos zu komplex, Level 2 und 3 als Sub-Folder im Hauptrepo mit harten CODEOWNERS-Permissions. Decision dazu im Sprint-Review KW22 oder Phase 2 Start.

## Permission-Matrix

| Rolle | Level 1 | Level 2 | Level 3 |
|---|---|---|---|
| Chris (extern) | Admin | Admin | Read |
| Lars (Founder) | Admin | Admin | Admin |
| Matteo (Founder) | Admin | Admin | Admin |
| Dieter (PM) | Write | Admin | Write |
| Junior Dev (KI-Stelle) | Write | Read | Write |
| Marketplace Manager (4x) | Kein Access | Write auf eigene Mandate | Read |
| Fabian (Praktikant) | Kein Access | Read | Read |
| Laureen (Marketing) | Read | Write auf Marketing-Bereich | Write |

Stand: 19.05.2026.
