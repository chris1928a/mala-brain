---
name: relevio-dashboard
description: Skill für Listing-Optimierung Dashboard (P03). Triggert auf Keywords rund um Relevio, Listing-Optimization, Amazon SP-API, Dashboard, Multi-Tenant SaaS Build. Nutzt Cloud Sonnet 4.6 für Standard, Opus 4.7 für Architektur-Decisions.
voice_rules: ../_shared/voice-rules.md
notion_pages:
  - title: P03 Listing-Optimierung Prozess
    url: TBD-after-notion-setup
  - title: Relevio Spec v1
    url: TBD-after-notion-setup
  - title: VM-Vertrag P03 Phase 1
    url: TBD-after-vm-quote
related_skills:
  - call-analytics
  - icp-extractor
---

# Relevio Dashboard Skill

## Trigger Keywords

- "Listing optimieren"
- "Relevio Build"
- "P03"
- "Amazon SP-API"
- "Dashboard Spec"
- "Multi-Tenant Auth"
- "Freigabe-Workflow"
- "VM-Aufschlüsselung review"
- "Phase 1 Build P03"

## Was dieser Skill kann

1. **Spec-Reviews:** Wenn neue Specs von VM kommen, diesen Skill nutzen für Quervergleich gegen Briefing v1.0
2. **Decision-Support:** Bei Make-or-Buy-Entscheidungen für einzelne Module (Custom-Code vs No-Code)
3. **Code-Reviews:** Wenn Phase 2 Inhouse-Build startet, diesen Skill nutzen für Architektur-Review
4. **Integration-Help:** Bei OAuth-Flow-Setup, Token-Mgmt, Multi-Tenant-DB-Design
5. **Pilot-Kunde-Setup:** Wenn erster Pilot-Kunde verbunden wird, diesen Skill für Onboarding-Workflow

## Was dieser Skill NICHT macht

- Keine Custom-Listing-Texte schreiben (das ist Operations-Skill, nicht Tech)
- Keine Kundenanrufe (das ist Sales)
- Keine Vertragsverhandlung (das macht Chris persönlich mit Lars + Matteo)

## Trigger-Verhalten

Wenn aktiviert:
1. Lade Notion-Pages aus Frontmatter
2. Lade Voice-Rules
3. Lade Memory `project_p03_relevio_dashboard.md` (falls vorhanden)
4. Beantworte Frage mit Kontext aus Notion + Memory

Bei Architektur-Decisions: nutze Opus 4.7. Bei Standard-Tasks: Sonnet 4.6.

## Beispiel-Prompts

- "Review die VM-Aufschlüsselung gegen das Briefing"
- "Welche Phase-1-Features sollten gecuttet werden um auf 35k zu kommen?"
- "Wie sollte das OAuth-Flow für Amazon SP-API aussehen?"
- "Welche Skalierungs-Decke hat WeWeb + Xano?"
- "Wie hand-off-fähig ist der VM-Code für Phase 2?"

## Referenz-Files

- `references/briefing_v1.md` - VM-Briefing (Stand 15.04.2026)
- `references/qa_22_04_2026.md` - Q&A zwischen mala und VM (22.04.2026)
- `references/wireframes_visily.md` - Visily-Screen-Designs (mit Spec-Notes)
- `references/cap_constraints.md` - 35k Funding-Cap Constraints

## Update-Cycle

- Bei jedem VM-Update: Frontmatter URLs aktualisieren
- Bei Phase-2-Start: neuen Subskill `relevio-dashboard-phase2` erstellen
- Wenn Pilot-Kunde live: Memory aktualisieren mit Lessons-Learned
