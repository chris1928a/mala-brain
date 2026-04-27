# Memory Index - mala Brain v3

Memory-Files für persistente Kontext-Information über Sessions hinweg. Pro Memory ein eigenes Markdown-File. Hier nur der Index, max 200 Zeilen.

## Wie der Index funktioniert

Jede Zeile: `- [Title](file.md) - One-line hook`

Memory-Files sind in der gleichen Folder. Index wird automatisch von Cloud Code geladen, einzelne Memory-Files nur wenn Skill triggered.

## User Profile (1 File pro Person)

(Wird gefüllt sobald User-Sessions starten. Beispiel:)

- [user_lars_seuss.md](user_lars_seuss.md) - Lars Seuß: Co-Founder mala, Tech-Lead, Cloud-Code-affin
- [user_matteo_giazzi.md](user_matteo_giazzi.md) - Matteo Giazzi: Co-Founder mala, Operations-Lead, Strukturiertes Denken via Miro

## Feedback (Korrekturen + Confirmations)

(Wird gefüllt sobald User Feedback gibt. Beispiel:)

- [feedback_voice_rules.md](feedback_voice_rules.md) - PFLICHT: Umlaute + Anti-AI-Schreibstil
- [feedback_notion_full_content.md](feedback_notion_full_content.md) - Notion = voller Inhalt, nie Verweise auf lokale Files

## Project (aktuelle Initiativen)

- [project_p03_relevio_dashboard.md](project_p03_relevio_dashboard.md) - P03 Listing-Optimierung Build, Phase 1 mit VM (35k Funding), Start Mai 2026
- [project_brain_v3_setup.md](project_brain_v3_setup.md) - mala-brain Repo Setup, Lieferung von Chris bis 04.05.2026
- [project_messe_juni_2026.md](project_messe_juni_2026.md) - Messe Juni 2026, Banner ready, Broschüren in Arbeit

## Reference (External Systems)

- [reference_notion_workspace.md](reference_notion_workspace.md) - mala Notion-Workspace-Struktur (5 Top-Level-Departments)
- [reference_drive_folders.md](reference_drive_folders.md) - Drive-Folder-Struktur (Customer-Files + Internal + Assets)
- [reference_vm_contacts.md](reference_vm_contacts.md) - Visual Makers GmbH Köln, Lead Luka Weingärtner
- [reference_funding_details.md](reference_funding_details.md) - Förder-Funding ~25-30k EUR übrig, extern Pflicht

## Was NICHT in Memory

- Code-Patterns (im Code)
- Git-History (in Git)
- Architektur-Konventionen (in CLAUDE.md + docs/)
- Voice-Rules (in CLAUDE.md + docs/voice-rules.md)
- Ephemeral Tasks (in Todo-Listen, nicht Memory)
- Documented Processes (in Notion)

## Memory-Lifecycle

1. **Save:** Bei User-Feedback, neuen Project-Facts, External-References
2. **Update:** Wenn Memory falsch oder outdated wird
3. **Delete:** Wenn Memory irrelevant geworden ist (z. B. Projekt abgeschlossen)
4. **Reorganize:** Wenn Index zu lang wird (>150 Zeilen), Memory-Files konsolidieren

## Format einer Memory-Datei

```markdown
---
name: <kurzer-name>
description: <one-line-description>
type: <user|feedback|project|reference>
---

<Inhalt>

**Why:** <Begründung warum diese Memory wichtig ist>
**How to apply:** <Wann diese Memory abgerufen werden soll>
```
