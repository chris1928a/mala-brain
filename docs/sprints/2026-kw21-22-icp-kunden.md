# Sprint KW21 + KW22, 19.05. bis 01.06.2026

**Eine Hauptmission:** Shared Repo (chris1928a/mala-brain) plus Notion-Mirror testen. Lars, Matteo und Dieter kollaborieren zwei Wochen lang täglich darin. Ergebnis: wir wissen ob das System funktioniert oder wo es bricht.

**Sprint-Owner:** Matteo (treibt die Kollaboration), Lars (lädt Chris ein plus liefert Token), Chris (baut Notion-Mirror sobald Token da)
**Dauer:** 2 Wochen
**Start:** Mo 19.05.2026
**Mid-Check:** Fr 23.05.
**Sprint-Review:** Mo 02.06.

## Decisions im Sprint-Call 19.05.

1. Notion ist Single Source of Truth für PM. GitHub-Repo `mala-brain` bleibt Backend für Code, Daten und Skill-Definitionen.
2. 2-Wochen-Sprints, ein Thema pro Sprint, keine Multi-Tasking-Verteilung mehr.
3. Aktueller Sprint: Repo + Notion-Mirror Kollab-Test. Nächster Sprint (KW23+24): Werbemaßnahmen, falls dieser Test erfolgreich.
4. Hetzner ersetzt Make und n8n. Cloud-Code statt SaaS-Workflows.
5. Dieter = PM + Controlling, Lars = Finanzen + Cashflow, Matteo = Operations + Marketing.
6. KI-Werkstudent: Marcel als Kandidat, Screening läuft.

## Die EINE Mission

**Lars + Matteo + Dieter arbeiten 2 Wochen lang produktiv im Shared-Repo plus Notion-Mirror.** Das ist der einzige Erfolgs-Test. Wenn das funktioniert, geht der nächste Sprint live. Wenn es bricht, fixen wir die Bruchstellen vor allem anderen.

**Definition of Done für die Mission:**

- [ ] Lars hat Chris in `chris1928a/mala-brain` als Collaborator und in Mala-Notion mit Editor-Rechten
- [ ] Lars hat den Internal Connection Token an Chris übergeben
- [ ] Chris hat den Notion-Mirror live gepushed via `scripts/notion_mirror_push.py`
- [ ] Dieter hat mindestens 3 Pull Requests gegen das Repo gemacht
- [ ] Dieter hat mindestens 3 Edits in der Notion-PM-Page gemacht
- [ ] Matteo hat mindestens 1 Transkript automatisch ins Brain gefüttert
- [ ] Friday Cowork-Session in KW21 plus KW22 hat stattgefunden
- [ ] Sprint-Retro 02.06.: was läuft, was bricht, was nehmen wir in den nächsten Sprint mit

## Parallele Tracks (kein Sprint-Blocker, aber laufen weiter)

Diese laufen im Hintergrund. Wenn sie sich verzögern wegen der Mission, ist das OK.

- ICP-Definition (Lars arbeitet an Founder-Interviews, Skeleton liegt in `docs/icp/template.md`)
- Top-3 Kunden-Prozesse evaluieren für Sprint KW23+24 (Matteo plus Dieter scopen)
- Grafikdesigner-Ersatz screening (Lars plus Matteo)
- Marcel KI-Werkstudent Interview (Lars plus Matteo)

## Wochenaufteilung

### KW21 (19.05. bis 25.05.) - Setup + erste Pull Requests

| Tag | Aktivität | Owner |
|---|---|---|
| Mo 19.05. | Sprint-Kickoff Call, Chris zu GitHub + Notion einladen, Internal Connection Token an Chris | Lars, Matteo |
| Di 20.05. | Notion-Mirror live pushen sobald Token da, Dieter mit Repo-Clone live | Chris, Dieter |
| Mi 21.05. | Dieter macht erste 2 PRs gegen das Repo plus 2 Edits in Notion-PM-Page | Dieter |
| Do 22.05. | Matteo füttert erstes Transkript ins Brain, Lars macht ersten Strategy-PR | Matteo, Lars |
| Fr 23.05. | Mid-Check Friday-Cowork: läuft die Kollab? Wo bricht es? | Lars, Matteo, Chris |

### KW22 (26.05. bis 01.06.) - Stabilisieren + Retro

| Tag | Aktivität | Owner |
|---|---|---|
| Mo 26.05. | Bruchstellen vom Mid-Check fixen, Onboarding-Doku schärfen falls nötig | Chris |
| Di 27.05. | Dieter macht weitere 1-2 PRs, deckt schon einen echten PM-Use-Case ab | Dieter |
| Mi 28.05. | Lars plus Matteo nutzen Brain live im Tagesgeschäft (Pull-Anfragen via Claude Code) | Lars, Matteo |
| Do 29.05. | Friday-Cowork Vorbereitung, Retro-Punkte sammeln | Group |
| Fr 30.05. | Cowork-Session #2, Demo der Workflow-Beispiele | Group |
| Mo 02.06. | Sprint-Review plus Retro: was läuft, was bricht, was geht in Sprint 2 | Group |

## Definition of Done für die Mission (siehe oben, gesammelt)

1. Mission-Checkliste aus dem `## Die EINE Mission` Block alle abgehakt
2. Sprint-Review-Doc liegt in `docs/sprints/2026-06-02-review.md` mit klarer Empfehlung (System produktionsreif ja/nein, was als Nächstes)
3. Sprint KW23+24 ist im Repo gescoped (`docs/sprints/2026-kw23-24-*.md`)

## Pending Cross-Sprint

- Kooperationsmodell und Retainer-Anpassung: aktuell 1.000 EUR / Monat bei 10-20h/Woche Aufwand seitens Chris. Verhandlung in separatem Slot, nicht im Sprint.
- Notion-Permissions für Chris: Editor-Rechte plus Internal Connection Token. Blockiert die Mission bis durch.
- E-Commerce-Messe Köln im Juni: Lars positioniert. Kein Sprint-Item, aber Hintergrund.

## Sprint-Risiken

- **Notion-Permissions hängen länger.** Mitigation: GitHub-only-Pfad bleibt nutzbar, Dieter kann trotzdem PRs üben, aber Test wäre unvollständig.
- **Dieter findet das System sperrig.** Mitigation: Onboarding-Doku schärfen, Friday-Cowork bewusst auf Dieter-Pain-Points fokussieren.
- **Lars oder Matteo schaffen es nicht den Brain wirklich täglich zu nutzen.** Mitigation: minimaler Daily-Use-Case festlegen (z.B. 1 Pull-Anfrage pro Tag), damit Routine entsteht.
