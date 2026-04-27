# Drive Linking Convention

## Drive-Folder-Struktur (mala)

```
mala markets Drive
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
│   ├── Vertraege (VM, Subscriptions, etc.)
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

## Was gehört in Drive (nicht in Notion)

- Long-Form Copy (Pitch-Decks, Case-Studies)
- PDFs (Verträge, Briefings, Förder-Dokumente)
- Bilder, Slides, Videos
- Excel-Tabellen mit Rohdaten
- DOCX-Drafts
- Audio/Video-Aufzeichnungen

## Was NICHT in Drive

- Strukturiertes Wissen (geht in Notion)
- Code (geht in GitHub)
- AI-Prompts (geht in Skills)
- Meeting-Notes (gehen in Notion)
- Process-Docs (gehen in Notion)

## Verlinkungs-Regel

**Drive-File wird in Notion-Page eingebettet:**
- Eine Notion-Page pro Topic
- Drive-File als Link oder Embed in dieser Notion-Page
- Cloud findet Drive-File nur über Notion, nicht direkt

**Skill referenziert Drive nur über Notion:**
```
Skill SKILL.md
   ↓ referenziert
Notion Page (z. B. "P03 Listing-Optimierung")
   ↓ enthält Link zu
Drive File (z. B. "VM_Briefing_v1.docx")
```

NIE Skill direkt zu Drive-File. Sonst ist Cloud blind, wenn Drive-Struktur sich ändert.

## File-Naming-Convention

- **Briefings:** `<Topic>_Briefing_v<Version>.docx` (z. B. `VM_Relevio_Briefing_v1.docx`)
- **Reports:** `<Kunde>_<Monat>_Report.pdf` (z. B. `Mueller_2026-04_Report.pdf`)
- **Verträge:** `Vertrag_<Partner>_<Datum>.pdf` (z. B. `Vertrag_VM_2026-05-01.pdf`)
- **Listings (Rohdaten):** `<Kunde>_<Datum>_Listings.csv` (z. B. `Mueller_2026-04-15_Listings.csv`)

## DSGVO-Regel

- Customer-Data nur in Drive (nicht in Code, nicht in GitHub)
- Folder-Permissions: nur autorisierte Mitarbeiter sehen Customer-Folders
- Kein Public-Sharing von Customer-Files
- Datenlöschung auf Anfrage: Folder löschen, Notion-Verlinkung kappen

## Drive-API-Setup für Cloud

1. Service-Account erstellen in Google Cloud Console (mala-cloud-drive-sa)
2. Service-Account-Email als Editor zu relevanten Folders adden
3. Service-Account-Key in GitHub Secrets (DRIVE_SERVICE_ACCOUNT_KEY)
4. Cloud nutzt MCP-Tool für Drive-Read

## Cloud-Lesen von Drive

Pattern:
```
1. Skill braucht Drive-File
2. Skill liest Notion-Page für Drive-URL
3. Skill extrahiert File-ID aus URL
4. Skill liest File via Drive-MCP
5. Skill verarbeitet Inhalt
```

Nie ganze Drive-Folders in Cloud-Kontext laden. Nie alle Drive-Files vorab indexieren.

## Sync-Strategie

Drive-Files können wochenweise zu Notion gesynced werden (z. B. neue Briefings automatisch in passender Notion-Page als Embed). Sync-Workflow liegt in `workflows/drive-notion-sync.md` (TBD).
