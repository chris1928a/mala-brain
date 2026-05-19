# Scripts Folder

Python und Shell Scripts für Automation, Dev-Tooling, einmalige Migrationen.

## Konvention

- Python: 3.11+ mit Type-Hints
- Shell: Bash (Linux/Mac), PowerShell (Windows)
- Jedes Script: Header-Kommentar mit Zweck, Usage, Author
- Argumente via `argparse` (Python) oder `getopts` (Shell)

## Aktuelle Scripts

- `scripts/notion_mirror_push.py` - Pushed mala-brain Docs (Team-Permissions, Sprints, Onboarding, ICP-Template, Meeting-Notes, Decisions) als Notion-Pages in den Mala-Workspace. Erwartet `NOTION_TOKEN` und `NOTION_PARENT_PAGE_ID` als Env-Vars. Wartet auf Lars' Internal Connection Token (Stand 19.05.2026).

### Geplant

- `scripts/sync_dropbox_to_notion.py` - Dropbox-Files in Notion-Pages embedden
- `scripts/migrate_n8n_to_code.py` - n8n-Workflows zu Python-Code (one-time)
- `scripts/score_call_transcript.py` - Call-Analytics-Bot CLI
- `scripts/icp_match.py` - ICP-Klassifikation P1/P2/P3/OUT auf neue Leads (Adaption von RC tools/icp_match_close.py)

## Setup

```bash
# Python
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Mac/Linux
pip install -r requirements.txt

# Run
python scripts/<script>.py --help
```

## Secrets

Scripts laden Secrets aus `.env.local` (gitignored) oder GitHub-Secrets bei CI/CD.

```bash
# .env.local Beispiel
NOTION_TOKEN=secret_xxx
DROPBOX_APP_KEY=xxx
DROPBOX_APP_SECRET=xxx
DROPBOX_REFRESH_TOKEN=xxx
ANTHROPIC_API_KEY=sk-ant-xxx
```

## Testing

Scripts haben Unit-Tests in `scripts/tests/`. Run via `pytest scripts/tests/`.

## CI/CD

GitHub Actions führt Scripts bei Bedarf aus (z. B. wöchentliche Dropbox-Notion-Sync). Definitions in `.github/workflows/`.
