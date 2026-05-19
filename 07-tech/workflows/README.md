# Workflows Folder

Wiederverwendbare AI-Workflows für mala. Workflows = mehrstufige Cloud-Code-Pipelines, die mehrere Skills kombinieren.

## Konvention

Jeder Workflow hat:
- `<workflow-name>.md` mit Beschreibung
- Optional `<workflow-name>.py` als Cloud-Code-Pipeline-Implementation
- Trigger-Bedingungen (Cron, manuell, Event-basiert)

## Aktuelle Workflows

(Wird gefüllt sobald Workflows existieren. Beispiele:)

- `weekly-call-analytics.md` - Wöchentliche Bulk-Analyse aller AM-Calls
- `monthly-listing-saving-report.md` - Monatlicher Saving-Report aus P03-Operations
- `lead-to-pilot-onboarding.md` - Workflow für neuen Pilot-Kunden Phase 1

## Workflow vs Skill

- **Skill:** Reaktiv, triggert auf User-Prompt, ein Step
- **Workflow:** Proaktiv, läuft auf Cron oder Event, mehrere Steps, kombiniert mehrere Skills

## Workflow-Trigger

| Trigger-Typ | Beispiel |
|---|---|
| Cron | "Jeden Montag 09:00: Wöchentlicher Call-Score" |
| Webhook | "Neuer Pilot-Kunde signed: Onboarding-Workflow startet" |
| Manual | "Chris triggert: Monatlicher Saving-Report" |

## Workflow-Engine

Workflows laufen auf:
- Server (DigitalOcean Droplet, AWS EC2) für Cron + Event
- Cloud Code lokal für manual Triggers
- NICHT N8N (deprecated)

Server-Setup in `07-tech/architecture.md`.

## Testing

Workflows haben Smoke-Tests vor Cron-Aktivierung. Run via `python workflows/<name>.py --dry-run`.
