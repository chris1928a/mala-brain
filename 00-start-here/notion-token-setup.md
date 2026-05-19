# Notion Internal Connection Token, Setup für Lars

10 Minuten, Lars als Workspace-Owner. Notwendig damit Claude im Mala-Notion lesen und schreiben kann.

## Warum nicht OAuth wie bei einzelnen Pages

Notion-Connections sind workspace-spezifisch. Chris hat schon eine Claude-Connection in seinem Notion-Workspace, aber die funktioniert nicht über Workspaces hinweg. Mala braucht eine eigene Internal Connection im Mala-Notion.

## 4 Schritte

1. **Workspace-Owner Check:** In Notion einloggen mit dem Account, der Owner-Rechte im Mala-Workspace hat (Lars).

2. **Integrations-Page öffnen:**
   - Direkt: `https://www.notion.so/profile/integrations/internal`
   - Oder: `Settings` → `Connections` → unten `Develop your own connections`

3. **Neue Connection erstellen:**
   - `+ New connection` klicken
   - Name: `mala-brain-claude`
   - Logo: optional, das mala-Logo
   - Associated workspace: `mala markets` auswählen
   - Capabilities:
     - Read content
     - Write content
     - Insert content
     - Read user information (without email)
   - Submit

4. **Token kopieren und Pages verbinden:**
   - Auf die fertige Connection klicken
   - `Internal Connection Token` kopieren (fängt mit `ntn_` oder `secret_` an)
   - **Pages mit der Connection verbinden:** Für jede Page die Claude lesen/schreiben können soll:
     - Page öffnen
     - `...` oben rechts
     - `+ Add Connections`
     - `mala-brain-claude` auswählen
   - **Vererbung:** Sub-Pages erben die Connection automatisch. Es reicht die Top-Level-PM-Page zu verbinden.

## Token sicher an Chris

- **Nicht** in Slack-Channel posten
- **Nicht** per Mail unverschlüsselt
- Slack-DM an Chris, oder per 1Password Share

Sobald Chris den Token hat:
- Notion-Mirror geht live via `07-tech/scripts/notion_mirror_push.py`
- Brain kann automatisch Transkripte lesen, Decisions ablegen, Sprint-Plans synchronisieren

## Bei Fehlern

- `401 Unauthorized` beim Skript-Lauf: Token falsch oder PM-Page nicht mit der Connection verbunden
- Connection-Liste leer: Workspace-Owner-Rechte fehlen, dann ist nicht Lars sondern Matteo der Workspace-Owner und sollte das machen
- `Develop your own connections` nicht sichtbar: kommt erst nach `Settings → Connections`, manchmal hinter `Browse connections`

Stand: 19.05.2026.
