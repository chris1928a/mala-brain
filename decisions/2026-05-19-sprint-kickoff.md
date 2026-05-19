# Decisions Sprint-Kickoff, 19.05.2026

8 strategische Decisions im Call gelockt. Jede mit 30-Tage Outcome-Review.

## D1, Notion ist Single Source of Truth für PM

- **Wer:** Lars, Matteo, Chris
- **Wann:** 19.05.2026
- **Kontext:** Chris hatte shared GitHub-Repo als To-Do-System vorgeschlagen. Lars plädierte für Notion wegen Übersichtlichkeit plus dynamischer To-Do-Verwaltung.
- **Decision:** Notion = PM-Single-Source-of-Truth. GitHub = Backend für Code, Skripte, Decisions, Architektur. Notion-Pages und GitHub-Files spiegeln sich nicht 1:1, sondern haben klar getrennte Rollen.
- **Outcome-Review-Date:** 18.06.2026
- **Owner für Review:** Chris (Architektur-Audit)

## D2, 2-Wochen-Sprints mit einem Thema pro Sprint

- **Wer:** Lars, Matteo, Chris
- **Wann:** 19.05.2026
- **Kontext:** Multi-Topic-Vergangenheit hatte zu Ablenkung und unklaren Outcomes geführt. Klassische Mala-Pain: viele parallele Themen, keines wirklich done.
- **Decision:** 2-Wochen-Sprints. Ein Hauptthema pro Sprint. Mid-Sprint-Check Freitag, Sprint-Review Montag der dritten Woche.
- **Outcome-Review-Date:** 18.06.2026 (nach Sprint 1 + Start Sprint 2)
- **Owner für Review:** Matteo (Operations)

## D3, Sprint KW21+22 Thema = ICP + Kunden-Prozess-Automatisierung

- **Wer:** Lars, Matteo, Chris
- **Wann:** 19.05.2026
- **Kontext:** Zwei höchste Prios aus Impact-Effort-Matrix vom 21.04. (A2 Client Onboarding plus B1 Marketplace Content) plus ICP-Definition als Foundation für alles Marketing.
- **Decision:** Sprint KW21+22 fokussiert ICP-Final plus Top-3-Prozesse-Automatisierung.
- **Outcome-Review-Date:** 02.06.2026 (Sprint-Review)
- **Owner für Review:** Lars (ICP), Matteo (Prozesse)

## D4, Nächster Sprint KW23+24 = Werbemassnahmen wenn Brain-Test erfolgreich

- **Wer:** Lars, Matteo, Chris
- **Wann:** 19.05.2026
- **Kontext:** Werbung nur sinnvoll wenn ICP + Targeting auf Brain-Basis funktioniert. Conditional Trigger.
- **Decision:** KW23+24 wird Google Ads plus Meta-Retargeting starten, conditional auf erfolgreichen Brain-Test mit Dieter in KW21.
- **Outcome-Review-Date:** 16.06.2026 (nach Sprint 2)
- **Owner für Review:** Matteo

## D5, Hetzner ersetzt Make plus n8n im kritischen Brain-Pfad

- **Wer:** Lars, Matteo, Chris
- **Wann:** 19.05.2026
- **Kontext:** Mala zahlt seit 2-3 Monaten Hetzner-Hosting ohne Nutzung. Make plus n8n haben Vendor-Lock-in und sind teurer. Cloud-Code statt SaaS-Workflows.
- **Decision:** Hetzner wird Cron-Host für mala-brain Skripte. n8n bleibt für Listings-Workflows, aber raus aus dem kritischen Brain-Pfad. Make-Migration in Phase 2.
- **Outcome-Review-Date:** 18.06.2026
- **Owner für Review:** Junior Dev (sobald hired), bis dahin Matteo

## D6, Rollen-Lock

- **Wer:** Lars, Matteo, Chris
- **Wann:** 19.05.2026
- **Kontext:** Rollen-Drift in den vergangenen Wochen, vor allem im PM-Bereich.
- **Decision:**
  - Lars = Strategie + Sales + Finanzen + Cashflow
  - Matteo = Operations + Marketing + Funnel
  - Dieter = PM + Controlling + Kapazitätsplanung + Projekt-Budgets
- **Outcome-Review-Date:** 30.06.2026
- **Owner für Review:** Lars

## D7, KI-Werkstudent Kandidat Marcel

- **Wer:** Lars, Matteo
- **Wann:** 19.05.2026
- **Kontext:** KI-Stelle ausgeschrieben seit 11.05. Marcel als heißer Kandidat aus dem Netzwerk identifiziert.
- **Decision:** Marcel-Interview prioritär in Sprint KW21+22. Profil-Anforderung: GitHub-Workflow plus Python plus Claude Code (nicht reiner n8n-Background).
- **Outcome-Review-Date:** 02.06.2026 (Sprint-Review)
- **Owner für Review:** Lars

## D8, Digital Twins als zentrale Brain-Architektur

- **Wer:** Lars, Matteo, Chris
- **Wann:** 19.05.2026
- **Kontext:** Founder Twin (Lars + Matteo) plus Team Twin auf shared GitHub-Brain. Synct ueber Dropbox plus Cloud-Systeme.
- **Decision:** Twin-Architektur ist gelockt. Founder Twin ab Sprint KW21+22 implementieren, Team Twin ab Sprint KW23+24.
- **Outcome-Review-Date:** 16.06.2026 (nach Sprint 2)
- **Owner für Review:** Chris (Architektur)

## Outcome-Review-Template

Bei jedem Outcome-Review-Date wird pro Decision festgehalten:
1. Hat die Decision das erwartete Outcome erzeugt?
2. Welche Annahmen waren richtig, welche falsch?
3. Decision behalten, anpassen oder reverten?
4. Folge-Decision falls nötig.

Logging als neuer Markdown-File in `decisions/YYYY-MM-DD-review-D<n>.md`.
