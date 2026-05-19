# customers/

Ein Folder pro aktiven Mandat. Dieter pflegt diesen Bereich als PM.

## Konvention

- Folder-Name: kebab-case, sprechend (z. B. `audiomarke-ebay/`, `kunde-xy-amazon/`)
- Pro Folder mindestens eine `profile.md` (siehe `_TEMPLATE/profile.md`)
- Optional: `meetings/`, `decisions/`, `playbooks-custom/` als Sub-Folder

## Permission

- **Lesen:** Founder + Dieter + zugeordneter Marketplace Manager
- **Schreiben:** Dieter + zugeordneter Marketplace Manager
- **Mergen:** Lars (Pricing) plus Matteo (Execution)

Volle Permissions-Map in `docs/team-permissions.md`.

## Notion-Mirror

Jeder customer-Folder wird in Notion gespiegelt unter PM-Page → Mandate. Mirror via `scripts/notion_mirror_push.py` (TBD ab Schritt 2 nächste Woche).

## Wenn ein Mandat endet

- `profile.md` Status auf `Abgeschlossen` setzen
- Folder NICHT löschen
- Letztes Performance-Review als Datum dokumentieren
- Renewal-Outreach-Datum setzen (für Reaktivierung in 6-12 Monaten)
