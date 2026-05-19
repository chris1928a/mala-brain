# Matteos 5 Fragen vom Sprint-Kickoff, beantwortet

Stand 19.05.2026 abends. Jede Frage aus Matteos Agenda-Mail mit klarer Antwort und Verlinkung in den Mala-Brain Repo plus ins Deck.

Master-Plan-Verweise:
- [PROJECT-MANAGEMENT.md](../PROJECT-MANAGEMENT.md) - alle Tasks plus Status
- [STRUCTURE.md](../STRUCTURE.md) - Repo-Struktur 1:1 zu Notion gespiegelt
- [Mala Digital Twin Deck](https://chris1928a.github.io/mala-brain/decks/digital-twin/) - 16-Slide-Gesamtplan

---

## Frage 1: Team-Zugang Mala-Brain

> Wie schaffen wir es, dass jeder im Team unser Mala-Brain nutzen kann, damit alles funktioniert und alle das gleiche Setup haben und alles auf dem aktuellen Stand ist?

**Antwort:** GitHub-Repo `chris1928a/mala-brain` als Master Truth, Notion-Mirror fuers Team-Read, klare Onboarding-Strecke in `00-start-here/`. Diese Woche testen wir das mit Dieter.

Konkrete Files:
- [00-start-here/onboarding.md](../00-start-here/onboarding.md) - generelle Setup-Schritte
- [00-start-here/dieter-claude-code-setup.md](../00-start-here/dieter-claude-code-setup.md) - Anfaenger-Anleitung Claude Code plus GitHub auf dem PC, 8 Schritte
- [00-start-here/dieter-workflow.md](../00-start-here/dieter-workflow.md) - taegliche Arbeitsweise plus 3 Test-PRs als Erfolgskriterium
- [00-start-here/team-permissions.md](../00-start-here/team-permissions.md) - 9-Rollen-Matrix aus Mail 07.05.: wer darf was

Architektur: GitHub fuer Master Truth, Notion fuer Team-Read-und-Schreib, Dropbox fuer Bulk-Files. Drei-Ebenen-Doku in [07-tech/architecture.md](../07-tech/architecture.md).

**Status diese Woche:** Lars laedt Chris in GitHub plus Notion ein, uebergibt Token, Dieter macht 3 Test-PRs. Wenn das laeuft, ist das System produktionsreif.

---

## Frage 2: Cron Jobs

> Was koennen wir noch mit Cron Jobs umsetzen, gibts da Anwendungsfaelle die dir in den Sinn kommen?

**Antwort:** Cron Jobs leben auf eurem Hetzner-Server (der seit 2-3 Monaten ungenutzt bezahlt wird). Konkreter Stack im Mala Digital Twin Deck dokumentiert plus erste Skripte in `07-tech/scripts/`.

Geplante Cron Jobs (Phase 1, KW23+24):

| Job | Frequenz | Was es tut |
|---|---|---|
| `sales_bridge.py` | stuendlich | CRM-Pipeline-Snapshot |
| `marketplace_pull.py` | alle 6h | Amazon SP-API + Otto + Kaufland |
| `icp_match.py` | alle 12h | neue Leads P1/P2/P3/OUT klassifizieren |
| `daily_brief.py` | Mo-Fr 07:00 | Slack Morning Brief an Lars und Matteo |
| `pipeline_daily.py` | Mo-Fr 18:30 | Diff plus Risk-Flags |
| `weekly_exec_report.py` | Mo 06:00 | Wochen-Report an Lars und Matteo |
| `stress_detector.py` | on-demand | Pre-Decision Check |

Detail-Visualisierung: [Mala Digital Twin Deck, Slide 9 Architecture](https://chris1928a.github.io/mala-brain/decks/digital-twin/#9)

**Status:** erstes Skript [07-tech/scripts/notion_mirror_push.py](../07-tech/scripts/notion_mirror_push.py) ist ready, wartet auf den Notion-Token von Lars. Rest kommt ab Sprint KW23+24.

---

## Frage 3: ICP fuer mala markets ohne manuellen Aufwand

> ICP fuer mala markets muessen wir im naechsten Schritt erstellen, wie koennen wir das bestmoeglich machen ohne manuellen starken Aufwand?

**Antwort:** Lars macht Founder-Interviews weiter mit seinem bestehenden Leitfaden. Daraus bauen wir den ICP. Skeleton liegt im Repo, Lars fuellt mit den Interview-Erkenntnissen.

- [01-strategy/icp/template.md](../01-strategy/icp/template.md) - Skeleton mit 5-Layer-Anchors, Buying-Signals, Decision-Maker-Map, OUT-Kriterien

Manueller Aufwand bleibt minimal, weil:
- Template gibt die Struktur vor, Lars fuellt nur die Felder
- ICP-Match-Skript [07-tech/scripts/icp_match.py](../07-tech/scripts/) (TBD) klassifiziert dann automatisch neue Leads P1/P2/P3/OUT
- Matteo hat heute schon Email-Kampagne-Filterung als ersten Pilot gestartet

**Status:** Skeleton liegt im Repo, Lars startet Founder-Interviews diese und naechste Woche. Final ICP zum Sprint-Review 02.06.

---

## Frage 4: AI Training des ICP

> AI Training des ICP. Wie schaffen wir es, dass Claude immer unser ICP prueft und checkt?

**Antwort:** Das ist ein Claude-Skill, kein Training. Skill triggert bei jedem Lead-, Account- oder Opportunity-Thema automatisch.

Logik:
- `01-strategy/icp/icp-mala-v1.md` (sobald Lars fertig) ist Master Truth des ICP
- Skill `mala-icp` in `07-tech/skills/` mit Trigger-Words: Lead, Account, Opportunity, Bewerber, Customer-Profile
- Plus Competition- und Look-alikes-Abgleich (Layer 5 im Founder Twin)
- Skript matched neue Leads gegen ICP, gibt P1/P2/P3/OUT zurueck

**Status:** Skill-Folder existiert im Repo, der `mala-icp` Skill wird konkret sobald das ICP final ist. Detail im [Deck Slide 5+6](https://chris1928a.github.io/mala-brain/decks/digital-twin/#5).

---

## Frage 5: Asset Foundation plus erster Meta Test

> Sollten nochmal zum aktuellen Stand von Asset Foundation sprechen und definieren was da die klare Steps sind, damit wir mit den ersten Meta Test starten koennen.

**Antwort:** Asset Foundation Sprint laeuft KW23+24, conditional auf Sprint KW21+22 erfolgreich.

Konkreter Test-Vorschlag:
- **Sub-Segment:** Marken 5-50M EUR Umsatz, Amazon-aktiv, Otto/Kaufland-Wachstum gewollt
- **Hook:** "Marktplaetze gehoeren auf C-Level"
- **Setup:** 1 LP plus 3 Ad-Variationen
- **Budget:** 3-5k EUR, 2 Wochen Laufzeit
- **Audience:** ICP-Daten als Custom Audience auf Meta
- **KPI Lock:** Cost-per-Booked-Meeting

Channels-Strategie (aus Call):
- Google Ads als Inbound-Basis (perfekt in Google-Ergebnissen)
- Meta Retargeting plus Video Ads plus Display (CEO-Gesichter auf FB und IG, Probleme adressieren)
- LinkedIn Newsletter plus Substack fuer Content-Leadership
- Cron Jobs fuer best-converting Assets in Outbound

**Status:** Detail-Plan kommt am 02.06. als `04-operations/sprints/2026-kw23-24-asset-foundation.md`. Vorbedingung: Sprint KW21+22 (Brain-Setup plus Dieter-Test) ist erfolgreich.

---

## Zusammenfassung

Alle 5 Fragen sind:

1. **Im Mala-Brain Repo dokumentiert** mit konkreten Files pro Antwort
2. **Im Mala Digital Twin Deck visualisiert** als Gesamtplan
3. **Im PROJECT-MANAGEMENT.md getracked** mit Status pro Task
4. **Phasiert:** Phase 0 diese Woche (Brain-Setup), Phase 1 KW23+24 (Cron plus ICP plus Asset Foundation plus Meta Test), Phase 2 ab KW25 (Skalierung)

**Was diese Woche passiert:** Lars uebergibt Token, Dieter testet die Kollaboration. Mehr nicht. Wenn das laeuft, geht Phase 1 mit allen 5 Themen automatisch live.

Stand: 19.05.2026.
