# GitHub Conventions

## Repository-Struktur

`mala-markets` GitHub-Org hat mehrere Repos:

| Repo | Zweck |
|---|---|
| `mala-brain` | Architektur, Skills, Voice-Rules, Memory (DIESE Repo) |
| `mala-relevio` | P03 Dashboard Code (Phase 2 Inhouse-Build) |
| `mala-website` | mala-markets.com Frontend |
| `mala-internal-tools` | Interne Mini-Tools (z. B. Call-Analytics-Bot) |

## Branch-Strategie

- `main` = Production (protected)
- `develop` = Integration-Branch
- `feature/<name>` = Features
- `fix/<name>` = Bug-Fixes
- `chore/<name>` = Refactor, Doku, Wartung

## Commit-Message-Convention

Format: `<type>: <description>`

Types:
- `feat`: Neues Feature
- `fix`: Bug-Fix
- `docs`: Doku-Änderung
- `refactor`: Code-Restrukturierung
- `chore`: Wartung, Setup, Config
- `test`: Tests

Beispiel:
- `feat: add Amazon SP-API OAuth flow`
- `fix: resolve token refresh race condition`
- `docs: update voice rules with WhatsApp special-case`

Sprache: Englisch ok, präsens, kurz (50 Zeichen Subject-Limit).

## PR-Konvention

- 1 PR = 1 Feature/Fix
- Title = Commit-Style
- Description: Was, Warum, Wie getestet
- Min 1 Reviewer (Lars review für Matteo, Matteo für Lars, Chris für beide)
- Squash-Merge auf main

## Secrets-Management

NIE Secrets im Code. Immer:
- GitHub Secrets für CI/CD
- `.env.local` für lokale Dev (gitignored)
- Secret-Manager für Production (z. B. GitHub Secrets, AWS SSM)

Secrets die mala braucht:
- `NOTION_TOKEN` (Notion-Integration)
- `DRIVE_SERVICE_ACCOUNT_KEY` (Drive-MCP)
- `AMAZON_SP_API_CLIENT_ID` (für P03)
- `AMAZON_SP_API_CLIENT_SECRET` (für P03)
- `ANTHROPIC_API_KEY` (Claude API)

## .gitignore

Standard-Ignores:
- `.env*`
- `node_modules/`
- `*.pyc` `__pycache__/`
- `.DS_Store`
- `*.log`
- `dist/` `build/`
- `.idea/` `.vscode/` (außer settings.json wenn shared)

## Linting

- Markdown: Prettier (Linewidth 100)
- Python: Black + Ruff
- TypeScript: ESLint + Prettier
- Pre-commit Hooks für alle drei

## Issue-Templates

In `.github/ISSUE_TEMPLATE/`:
- `bug_report.md`
- `feature_request.md`
- `decision_needed.md` (für Architektur-Decisions)

## Owner-Roles

| Role | GitHub-Permission | Wer |
|---|---|---|
| Admin | Full | Lars, Matteo, Chris |
| Maintainer | Push to main | Junior-Hire (later) |
| Contributor | PR-Submission | Externer Senior-Reviewer (later) |

VM bekommt eigenen Branch oder eigenes Sub-Repo, NICHT direkt Push auf `main` der mala-Repos.
