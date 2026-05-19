# Dropbox Linking Convention

## Dropbox-Folder-Struktur (mala)

```
mala markets Dropbox
├── 01 Customer-Files (pro Kunde)
│   ├── Kunde A
│   │   ├── Briefings
│   │   ├── Listings (CSV-Rohdaten)
│   │   ├── Reports
│   │   └── Verträge
│   └── Kunde B
│       └── ...
├── 02 Internal
│   ├── Förder-Dokumente
│   ├── Verträge (VM, Subscriptions, etc.)
│   ├── Finance (DATEV-Belege)
│   └── HR
├── 03 Sales-Assets
│   ├── Pitch-Decks
│   ├── Case-Studies
│   ├── Sales-Skripte (Long-Form)
│   └── Lead-Gen-Templates
├── 04 Marketing-Assets
│   ├── Brand-Files
│   ├── Messe-Materialien
│   ├── Content (Substack-Drafts, LinkedIn)
│   └── Visuals
└── 05 Tech-Files
    ├── Briefings (z. B. VM_Briefing_v1.docx)
    ├── Spec-Drafts
    └── Architektur-Docs
```

## Was gehört in Dropbox (nicht in Notion)

- Long-Form Copy (Pitch-Decks, Case-Studies)
- PDFs (Verträge, Briefings, Förder-Dokumente)
- Bilder, Slides, Videos
- Excel-Tabellen mit Rohdaten
- DOCX-Drafts
- Audio/Video-Aufzeichnungen

## Was NICHT in Dropbox

- Strukturiertes Wissen (geht in Notion)
- Code (geht in GitHub)
- AI-Prompts (gehen in Skills)
- Meeting-Notes (gehen in Notion)
- Process-Docs (gehen in Notion)

## Verlinkungs-Regel

**Dropbox-File wird in Notion-Page eingebettet:**
- Eine Notion-Page pro Topic
- Dropbox-Shared-Link als Embed in dieser Notion-Page
- Cloud findet Dropbox-File nur über Notion, nicht direkt

**Skill referenziert Dropbox nur über Notion:**
```
Skill SKILL.md
   ↓ referenziert
Notion Page (z. B. "P03 Listing-Optimierung")
   ↓ enthält Link zu
Dropbox File (z. B. "VM_Briefing_v1.docx")
```

NIE Skill direkt zu Dropbox-File. Sonst ist Cloud blind, wenn Dropbox-Struktur sich ändert.

## File-Naming-Convention

- **Briefings:** `<Topic>_Briefing_v<Version>.docx` (z. B. `VM_Relevio_Briefing_v1.docx`)
- **Reports:** `<Kunde>_<Monat>_Report.pdf` (z. B. `Mueller_2026-04_Report.pdf`)
- **Verträge:** `Vertrag_<Partner>_<Datum>.pdf` (z. B. `Vertrag_VM_2026-05-01.pdf`)
- **Listings (Rohdaten):** `<Kunde>_<Datum>_Listings.csv` (z. B. `Mueller_2026-04-15_Listings.csv`)

## DSGVO-Regel

- Customer-Data nur in Dropbox (nicht in Code, nicht in GitHub)
- Folder-Permissions: nur autorisierte Mitarbeiter sehen Customer-Folders
- Kein Public-Sharing von Customer-Files (Shared-Links nur intern, mit Passwort wenn extern nötig)
- Dropbox Business Plan wird empfohlen, AVV mit Dropbox Inc. PFLICHT (siehe Dropbox-DPA)
- Datenlöschung auf Anfrage: Folder löschen, Notion-Verlinkung kappen, Dropbox-Trash leeren

## Dropbox-API-Setup für Cloud

Dropbox bietet einen offiziellen Remote-MCP-Server (Beta, Stand April 2026). Setup:

1. Dropbox-App registrieren auf https://www.dropbox.com/developers/apps
   - App-Type: Scoped Access
   - Access-Type: App Folder (empfohlen, sandboxed) oder Full Dropbox (wenn cross-folder Access nötig)
   - App-Name: `mala-cloud-integration`
2. Permissions setzen: `files.content.read`, `files.metadata.read`, optional `files.content.write` für Sync-Workflows
3. App-Key + App-Secret in GitHub Secrets ablegen (`DROPBOX_APP_KEY`, `DROPBOX_APP_SECRET`)
4. Refresh-Token via OAuth-Flow generieren, in GitHub Secrets ablegen (`DROPBOX_REFRESH_TOKEN`)
5. Cloud nutzt Dropbox-MCP-Server für File-Read

## Cloud-Lesen von Dropbox

Pattern (analog zu Notion-MCP):

```
1. Skill braucht Dropbox-File
2. Skill liest Notion-Page für Dropbox-Shared-Link
3. Skill extrahiert File-Path oder File-ID aus Link
4. Skill liest File via Dropbox-MCP (https://mcp.dropbox.com/mcp)
5. Skill verarbeitet Inhalt
```

Nie ganze Dropbox-Folders in Cloud-Kontext laden. Nie alle Dropbox-Files vorab indexieren.

**Fallback ohne MCP:** Direkter REST-Call gegen Dropbox API v2:
- `POST /2/files/download` mit Header `Dropbox-API-Arg: {"path": "/path/to/file"}`
- Bearer-Token aus Refresh-Token-Flow
- Response = File-Content im Body

## Sync-Strategie

Dropbox-Files können wochenweise zu Notion gesynced werden (z. B. neue Briefings automatisch in passender Notion-Page als Embed). Sync-Workflow liegt in `workflows/dropbox-notion-sync.md` (TBD).
