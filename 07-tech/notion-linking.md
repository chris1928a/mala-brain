# Notion Linking Convention

## Notion-Workspace-Struktur (mala)

```
mala markets Workspace
├── 01 Strategy
│   ├── BHAG 2040
│   ├── Vivid Vision 2028
│   ├── Jahresplan
│   └── Big Decisions
├── 02 Sales
│   ├── ICP
│   ├── Pipeline
│   ├── Sales-Skripte
│   └── Lead-Gen
├── 03 Marketing
│   ├── Content
│   ├── Messe Juni 2026
│   └── Brand-Assets
├── 04 Operations
│   ├── Prozess-Dokumentation Master
│   │   ├── P01 Onboarding
│   │   ├── P02a Account-Analyse
│   │   ├── P02b Audit
│   │   ├── P03 Listing-Optimierung
│   │   ├── P04 Produktbilder
│   │   ├── P05 PPC
│   │   ├── P06 Account-Management
│   │   ├── P07 Reporting
│   │   └── P08 Support
│   └── Meeting-Notes
├── 05 Tech
│   ├── Brain v3 Architektur
│   ├── Relevio Spec
│   ├── VM-Verträge
│   └── Tech-Stack-Decisions
└── 06 People
    ├── Team-Liste
    ├── Hiring-Pipeline
    └── 1:1-Notes
```

## Verlinkungs-Regel zwischen GitHub und Notion

**Skill in GitHub referenziert Notion-Page:**

```yaml
---
name: relevio-dashboard
description: Listing-Optimierung Skill
notion_pages:
  - title: P03 Listing-Optimierung Prozess
    url: https://www.notion.so/mala/...
  - title: Relevio Spec v1
    url: https://www.notion.so/mala/...
---
```

Cloud lädt diese Notion-URLs nur wenn Skill aktiv triggered.

## Verlinkungs-Regel zwischen Notion und Dropbox

**Notion-Page referenziert Dropbox-File:**

In der Notion-Page ein Embed oder Link:
- Embed-Block für PDFs (Notion zeigt Preview)
- Dropbox-Shared-Link (Native-Preview wenn Domain whitelisted)
- Externer Link für andere Files

**Beispiel:**
> Briefing v1.0: [VM_Briefing_v1.docx](https://www.dropbox.com/scl/fi/.../VM_Briefing_v1.docx?dl=0)

## Notion-Page-Naming

- Strategische Pages: "Substantiv-Phrase" (z. B. "Vivid Vision 2028")
- Meeting-Pages: "Meeting <Datum> – <Teilnehmer-Kürzel>" (z. B. "Meeting 27.04.2026 – CEM Walk-Through")
- Prozess-Pages: "P<Nummer> <Prozess-Name>" (z. B. "P03 Listing-Optimierung")
- Decision-Pages: "Decision <Datum> – <Topic>" (z. B. "Decision 27.04.2026 – VM vs Inhouse")

## Schreibe-Regeln in Notion (für AI)

- IMMER mit echten Newlines (NIE \n als Escape)
- IMMER voller Inhalt, NIE Verweise auf lokale .md Dateien
- NIE archivieren oder löschen ohne explizite User-Anweisung
- NIE allow_deleting_content ohne explizite User-Bestätigung
- Subpages-Referenzen erhalten beim Update

## Notion-API-Setup für Cloud

1. Internal Integration erstellen in Notion (mala-cloud-integration)
2. Token in GitHub Secrets ablegen (NOTION_TOKEN)
3. Pages mit Integration sharen (jede Page einzeln, sonst kein Zugriff)
4. NIE Member-Account-Upgrade vorschlagen (kostet 12 EUR/User unnötig)

## Notion-Querying via Cloud

Cloud kann Notion über die Notion-MCP querien. Pattern:

```
1. Search Notion mit Keyword (z. B. "Listing-Optimierung")
2. Fetch Top-Result Page-ID
3. Lese Page-Inhalt
4. Finde verlinkte Dropbox-Files (wenn nötig)
5. Lese Dropbox-Files (nur wenn nötig)
```

NIE Dropbox-Files vorab laden. NIE Notion-Pages, die nicht im Skill referenziert sind, einlesen.
