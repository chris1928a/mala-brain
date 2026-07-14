# Skills Folder - mala Brain v3

Cloud Code Skills für mala. Jeder Skill hat eigenes Folder mit `SKILL.md` + optional `references/`.

## Aktuelle Skills

| Skill | Zweck | Owner |
|---|---|---|
| `relevio-dashboard` | P03 Listing-Optimierung Dashboard Build + Review | Tech (Lars) |
| `call-analytics` | Mitarbeiter-Call-Bewertung 1-5 auf 4 Dimensionen | Operations (Matteo) |
| `gtm/` | GTM Funnel Cluster (ICP zu Landing/Ad/Cold-Email). Master + 4 Sub-Skills: asset-foundations, landing-pages, ads, outbound. Roh-Mirror aus Chris' master-knowledge-base, Stand 2026-07-14, noch nicht an mala-Voice angepasst und ohne Claim/Deliverability-Gate | Marketing (Matteo/Lars) |
| `_shared/` | Geteilte Voice-Rules + Notion-Defaults | Alle |

## Skill-Konvention

Jeder Skill hat:
- `SKILL.md` mit Frontmatter (name, description, voice_rules, notion_pages, related_skills)
- Trigger-Keywords im Body
- Beschreibung was Skill kann / nicht kann
- Beispiel-Prompts
- Referenz-Files in `references/`

## Wie Skills triggern

Cloud Code lädt alle SKILL.md beim Start. Wenn User-Prompt Trigger-Keywords matched, wird Skill aktiviert. Aktiviert heißt:
1. Voice-Rules aus `_shared/` werden geladen
2. Notion-Pages aus Frontmatter werden geladen
3. Memory aus `memory/` wird geladen wenn relevant
4. Skill-Body wird in Cloud-Kontext eingefügt

## Neue Skills hinzufügen

1. Folder in `skills/` erstellen
2. `SKILL.md` aus Template kopieren
3. Frontmatter ausfüllen
4. Trigger-Keywords definieren
5. Voice-Rules referenzieren (Default = `../_shared/voice-rules.md`)
6. PR mit `feat: add skill <name>` 

## Skill-Naming

- Lowercase, mit Bindestrich getrennt
- Verb oder Substantiv-Phrase (z. B. `relevio-dashboard`, `call-analytics`, `icp-extractor`)
- Keine Versioning im Namen (das ist Git)

## Skill-Sharing

Skills sind im GitHub-Repo, also automatisch teamweit verfügbar. KEINE Skills nur in Cloud-Webapp lokal speichern (das war das alte Problem).

Bei Personal-Skills: separates Private-Repo oder eigenes Subfolder mit klarem Hinweis.

## Skill-Update-Cycle

Wenn AI-Modell upgradet (Sonnet 4.6 zu 4.7):
1. Test-Run mit Sample-Input pro Skill
2. Wenn Output ok: kein Code-Update nötig (Skills sind Modell-agnostisch)
3. Wenn Output schlechter: Skill-Body anpassen

Wenn Notion-Workspace umstrukturiert wird:
1. URLs in Frontmatter aller Skills aktualisieren
2. Test-Run mit ersten Triggers

## Out-of-Scope für Skills

- Keine Skills die direkt Money-Transfers oder Trades machen
- Keine Skills die Notion archivieren/löschen ohne explizite User-Anweisung
- Keine Skills die Customer-Data exportieren ohne DSGVO-Check
- Keine Skills mit Hardcoded-Secrets
