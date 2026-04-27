# Scripts Folder

Python und Shell Scripts für Automation, Dev-Tooling, einmalige Migrationen.

## Konvention

- Python: 3.11+ mit Type-Hints
- Shell: Bash (Linux/Mac), PowerShell (Windows)
- Jedes Script: Header-Kommentar mit Zweck, Usage, Author
- Argumente via `argparse` (Python) oder `getopts` (Shell)

## Aktuelle Scripts

(Wird gefüllt sobald Scripts existieren. Beispiele:)

- `scripts/sync_dropbox_to_notion.py` - Dropbox-Files in Notion-Pages embedden
- `scripts/migrate_n8n_to_code.py` - N8N-Workflows zu Python-Code (one-time)
- `scripts/score_call_transcript.py` - Call-Analytics-Bot CLI

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
