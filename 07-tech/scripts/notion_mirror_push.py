#!/usr/bin/env python3
"""
mala-brain Notion Mirror Push

Pushed die Kern-docs aus dem Repo als Notion-Pages in den Mala-Workspace.
Wartet auf den Internal Connection Token von Lars (siehe docs/onboarding.md).

Usage:
    export NOTION_TOKEN=ntn_xxxxxxxxxxxxxxxxxxxxxxxxx
    export NOTION_PARENT_PAGE_ID=9899204b3b2340f2abca8d17355bff97
    python3 scripts/notion_mirror_push.py

Was passiert:
1. Liest die docs aus dem lokalen Repo
2. Erstellt eine Sub-Page pro Doc unter NOTION_PARENT_PAGE_ID
3. Konvertiert Markdown zu Notion-Blocks
4. Logged Page-URLs in scripts/.notion_mirror_log.json
"""

import os
import json
import sys
from pathlib import Path
from datetime import datetime

try:
    import requests
except ImportError:
    print("requests fehlt. Installiere mit: pip install requests")
    sys.exit(1)

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
LOG_FILE = REPO_ROOT / "07-tech" / "scripts" / ".notion_mirror_log.json"
NOTION_API = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"

# Welche Docs werden gemirrort, mit Notion-Titel.
# Nach Refactor 19.05.2026: Pfade alle aus den numbered top-level Folders.
DOCS_TO_MIRROR = [
    {
        "path": "00-start-here/team-permissions.md",
        "title": "Team-Permissions (mala markets)",
        "icon": "🔑",
    },
    {
        "path": "04-operations/sprints/2026-kw21-22-icp-kunden.md",
        "title": "Sprint KW21+22, ICP + Kunden-Prozesse",
        "icon": "🏃",
    },
    {
        "path": "00-start-here/onboarding.md",
        "title": "Mala-Brain Onboarding",
        "icon": "📘",
    },
    {
        "path": "01-strategy/icp/template.md",
        "title": "ICP-Template (Skeleton für Lars)",
        "icon": "🎯",
    },
    {
        "path": "05-meetings/2026-05-19-sprint-kickoff.md",
        "title": "Sprint-Kickoff Call, 19.05.2026",
        "icon": "📝",
    },
    {
        "path": "01-strategy/decisions/2026-05-19-sprint-kickoff.md",
        "title": "Decisions Sprint-Kickoff, 19.05.2026",
        "icon": "⚖️",
    },
]


def get_env(name: str) -> str:
    val = os.environ.get(name)
    if not val:
        print(f"FEHLER: {name} ist nicht gesetzt.")
        print(f"  export {name}=...")
        sys.exit(1)
    return val


def md_to_blocks(md_text: str) -> list:
    """
    Konvertiert Markdown zu Notion-Blocks. Bewusst simpel.
    Unterstützt: Headings H1-H3, Paragraphs, Bullet-Lists, Numbered-Lists, Code-Blocks.
    Komplexere Tabellen werden als Paragraph rendered mit Pipe-Trennung.
    """
    blocks = []
    in_code = False
    code_buffer = []
    code_lang = "plain text"

    for line in md_text.split("\n"):
        stripped = line.strip()

        # Code-Block toggle
        if stripped.startswith("```"):
            if in_code:
                blocks.append({
                    "object": "block",
                    "type": "code",
                    "code": {
                        "rich_text": [{"type": "text", "text": {"content": "\n".join(code_buffer)}}],
                        "language": code_lang,
                    },
                })
                code_buffer = []
                in_code = False
            else:
                code_lang = stripped[3:].strip() or "plain text"
                in_code = True
            continue
        if in_code:
            code_buffer.append(line)
            continue

        # Headings
        if stripped.startswith("# "):
            blocks.append(rich("heading_1", stripped[2:]))
            continue
        if stripped.startswith("## "):
            blocks.append(rich("heading_2", stripped[3:]))
            continue
        if stripped.startswith("### "):
            blocks.append(rich("heading_3", stripped[4:]))
            continue

        # Bullets
        if stripped.startswith("- ") or stripped.startswith("* "):
            blocks.append(rich("bulleted_list_item", stripped[2:]))
            continue

        # Numbered
        if len(stripped) > 2 and stripped[0].isdigit() and stripped[1:3] in [". ", ".)"]:
            blocks.append(rich("numbered_list_item", stripped[3:]))
            continue

        # Empty line
        if not stripped:
            continue

        # Default paragraph
        blocks.append(rich("paragraph", stripped))

    # Falls Code-Block nicht geschlossen
    if in_code and code_buffer:
        blocks.append({
            "object": "block",
            "type": "code",
            "code": {
                "rich_text": [{"type": "text", "text": {"content": "\n".join(code_buffer)}}],
                "language": code_lang,
            },
        })

    return blocks


def rich(block_type: str, text: str) -> dict:
    """Notion-Block mit text content."""
    return {
        "object": "block",
        "type": block_type,
        block_type: {
            "rich_text": [{"type": "text", "text": {"content": text[:2000]}}],
        },
    }


def create_or_update_page(token: str, parent_id: str, doc: dict, headers: dict) -> dict:
    """Erstellt eine neue Sub-Page unter parent_id. Idempotency später ueber Log-File."""
    md_path = REPO_ROOT / doc["path"]
    if not md_path.exists():
        return {"ok": False, "error": f"File fehlt: {doc['path']}"}

    md_text = md_path.read_text(encoding="utf-8")
    blocks = md_to_blocks(md_text)

    # Notion API limit ist 100 children pro create call
    initial_blocks = blocks[:100]
    rest_blocks = blocks[100:]

    payload = {
        "parent": {"page_id": parent_id},
        "icon": {"type": "emoji", "emoji": doc.get("icon", "📄")},
        "properties": {
            "title": [{"type": "text", "text": {"content": doc["title"]}}],
        },
        "children": initial_blocks,
    }

    r = requests.post(f"{NOTION_API}/pages", headers=headers, json=payload, timeout=30)
    if r.status_code >= 400:
        return {"ok": False, "error": f"Notion API {r.status_code}: {r.text[:500]}"}

    page = r.json()
    page_id = page["id"]

    # Falls > 100 Blocks, Rest in chunks von 100 nachladen
    while rest_blocks:
        chunk = rest_blocks[:100]
        rest_blocks = rest_blocks[100:]
        append_payload = {"children": chunk}
        r2 = requests.patch(f"{NOTION_API}/blocks/{page_id}/children", headers=headers, json=append_payload, timeout=30)
        if r2.status_code >= 400:
            return {"ok": False, "error": f"Notion append {r2.status_code}: {r2.text[:300]}", "page_id": page_id}

    return {
        "ok": True,
        "page_id": page_id,
        "url": page.get("url", f"https://www.notion.so/{page_id.replace('-', '')}"),
        "title": doc["title"],
        "source": doc["path"],
        "pushed_at": datetime.utcnow().isoformat() + "Z",
    }


def main():
    token = get_env("NOTION_TOKEN")
    parent_id = get_env("NOTION_PARENT_PAGE_ID").replace("-", "")
    # Re-Hyphenate UUID-Format
    parent_id = f"{parent_id[:8]}-{parent_id[8:12]}-{parent_id[12:16]}-{parent_id[16:20]}-{parent_id[20:]}"

    headers = {
        "Authorization": f"Bearer {token}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }

    print(f"Push {len(DOCS_TO_MIRROR)} docs nach Notion parent {parent_id}\n")

    results = []
    for doc in DOCS_TO_MIRROR:
        print(f"  → {doc['path']}", end="", flush=True)
        result = create_or_update_page(token, parent_id, doc, headers)
        if result.get("ok"):
            print(f"  OK  {result['url']}")
        else:
            print(f"  FEHLER: {result.get('error')}")
        results.append(result)

    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    LOG_FILE.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nLog: {LOG_FILE}")

    failed = [r for r in results if not r.get("ok")]
    if failed:
        print(f"\n{len(failed)} Fehler. Siehe Log.")
        sys.exit(1)


if __name__ == "__main__":
    main()
