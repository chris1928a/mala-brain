# Diese Woche, 2 Schritte

Hi Lars und Matteo. Das ist die einzige Datei die ihr diese Woche braucht. Zwei Schritte, mehr nicht. Rest kommt nächste Woche.

> **Der Gesamtplan ist das Mala Digital Company Twin Deck:** [chris1928a.github.io/mala-brain/decks/digital-twin/](https://chris1928a.github.io/mala-brain/decks/digital-twin/)
>
> Was unten kommt ist Schritt 1 davon. Das volle Bild plus 2-Jahres-Roadmap zum 500k-Mandat steht im Deck.

## Schritt 1, Chris vollen Zugriff geben

Damit Chris den aktuellen Stand sehen und reviewen kann.

### GitHub

1. Geht auf https://github.com/chris1928a/mala-brain/settings/access (Lars als Owner oder Matteo als Admin)
2. Schaut ob `chris1928a` als Collaborator drauf ist mit Admin-Rechten. Falls nicht, klickt `Add people` → `chris1928a` → Role: `Admin` → `Add`
3. Falls ihr lokal auf eurem Rechner einen `mala-brain` Folder habt, in dem Sachen liegen die noch NICHT im GitHub sind: einmal alles committen und pushen, damit Chris den vollen Stand sehen kann.

```bash
cd <pfad-zum-mala-brain-lokal>
git status         # zeigt was lokal ist, aber nicht im Repo
git add .
git commit -m "sync local state for chris review"
git push origin main
```

### Notion

1. Geht in den Mala-Notion-Workspace
2. Die PM-Page öffnen die wir im Call besprochen haben (https://www.notion.so/9899204b3b2340f2abca8d17355bff97)
3. Oben rechts `Share` → Chris (chris@erlerventures.org) als Editor adden
4. Plus: Internal Connection Token erstellen, damit Claude für euch arbeiten kann. Anleitung in `docs/notion-token-setup.md`. Token via Slack-DM an Chris.

**Done wenn:** Chris kann sowohl GitHub-Repo als auch die Notion-PM-Page öffnen ohne 404.

## Schritt 2, Dieter ins Spiel bringen

Sobald Schritt 1 durch ist, Dieter starten lassen.

1. Dieter bekommt GitHub-Account-Invite (falls nicht da, schickt ihr Lars per Mail über `https://github.com/chris1928a/mala-brain/settings/access` → `Add people` → Dieter's GitHub-Username → Role: `Write`)
2. Dieter installiert GitHub Desktop (`https://desktop.github.com`) und klont `mala-brain`
3. Dieter liest `docs/dieter-workflow.md` (im Repo, ein A4-Seite)
4. Dieter macht seine ersten 3 Test-PRs in seinem Bereich (Details in `docs/dieter-workflow.md`)

**Done wenn:** Dieter hat 3 PRs gemerged. Dann wissen wir dass das System für ihn funktioniert.

## Was diese Woche NICHT passiert

Damit Matteo nicht überrennt: alles unten kommt nächste Woche oder später.

- ICP-Definition aus Founder-Interviews (Lars sammelt Material weiter, aber kein Druck)
- Cron Jobs auf Hetzner
- Asset Foundation + Meta Test
- Mala-Brain Mirror in Notion automatisch
- 3-Level GitHub-Architektur (das machen wir wenn Schritt 1+2 läuft)
- Marcel Interview KI-Werkstudent
- Grafikdesigner-Bewerber screenen (parallel, eigener Track)

## Bei Fragen

- Setup hängt: kurz an Chris (chris@erlerventures.org oder Slack)
- Anleitung unklar: PR mit Verbesserung gegen diese Datei, Chris merged

Stand: 19.05.2026. Updated wenn Schritt 1+2 durch.
