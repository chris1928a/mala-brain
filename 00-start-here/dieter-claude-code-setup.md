# Dieter, Claude Code plus GitHub Setup auf dem PC

Diese Anleitung ist für jemanden, der noch nie mit GitHub oder Claude Code gearbeitet hat. Schritt für Schritt. Wenn etwas hängt, lies den Hinweis unter dem Schritt oder ping Chris.

**Zeit:** circa 30 bis 45 Minuten beim ersten Mal.

**Was du am Ende kannst:**
- Mala-Brain Repo auf deinem PC haben
- Claude Code lokal nutzen (das ist der KI-Assistent der das ganze Brain kennt)
- Eine Änderung machen und sie ins GitHub pushen
- Den aktuellen Stand jederzeit syncen

---

## Was du brauchst, bevor du anfängst

- Ein eigener Computer (Windows oder Mac)
- Eine E-Mail-Adresse (mala-markets oder privat)
- Internet
- Ein Slack oder WhatsApp offen für Rückfragen an Matteo oder Chris

---

## Schritt 1, GitHub-Account erstellen (falls noch nicht da)

1. Geh auf https://github.com/signup
2. Gib deine E-Mail ein (am besten deine mala-markets E-Mail)
3. Wähle ein Passwort, schreib es dir auf
4. Wähle einen Username, kurz und ohne Sonderzeichen (z. B. `dieter-mala` oder dein Nachname)
5. Bestätige die E-Mail-Verifizierung über dein Postfach
6. Skip die Personalisierungs-Fragen, du brauchst keine Subscription, der Free-Plan reicht

**Falls du schon einen GitHub-Account hast:** überspringen, mit Schritt 2 weiter.

**Hilfe:** wenn die E-Mail nicht ankommt, im Spam-Ordner schauen. Sonst Chris pingen.

---

## Schritt 2, GitHub-Account-Username an Matteo geben

Damit wir dich als Collaborator in den Mala-Brain Repo einladen können.

1. Geh auf https://github.com/<dein-username> (oder klick oben rechts auf dein Profilbild → `Your profile`)
2. Kopiere deinen Username aus der URL oder vom Profil
3. Schick ihn an Matteo per Slack oder Mail

Matteo (oder Lars) lädt dich dann via GitHub als Collaborator ein. Du bekommst eine E-Mail.

**Hilfe:** wenn keine Mail kommt, einmal auf https://github.com/chris1928a/mala-brain/invitations schauen. Falls die Page leer ist, war die Einladung noch nicht raus, Matteo pingen.

---

## Schritt 3, GitHub Desktop installieren

GitHub Desktop ist die einfache App um mit GitHub zu arbeiten ohne Terminal-Befehle.

1. Geh auf https://desktop.github.com
2. Klick auf den grossen `Download for Windows` (oder `Download for macOS`) Button
3. Öffne die heruntergeladene Datei (`GitHubDesktopSetup-x64.exe` auf Windows, oder `.dmg` auf Mac)
4. Folge dem Installer (Standard-Optionen reichen, einfach durchklicken)
5. Nach der Installation öffnet sich GitHub Desktop automatisch
6. Klick `Sign in to GitHub.com`
7. Im Browser-Fenster das aufgeht: mit deinem GitHub-Account einloggen
8. Zurück in GitHub Desktop: dein Username sollte oben rechts erscheinen

**Hilfe:** wenn das Browser-Login nicht funktioniert, in GitHub Desktop unten `Sign in with browser` versuchen. Oder Username und Passwort direkt eintippen.

---

## Schritt 4, Mala-Brain Repo klonen

Klonen heisst: den ganzen Ordner aus dem Internet auf deinen PC kopieren.

1. In GitHub Desktop, oben links auf `File` → `Clone a repository...`
2. Tab `URL` auswählen
3. Im Feld `Repository URL`: `https://github.com/chris1928a/mala-brain` einfügen
4. Im Feld `Local Path`: wähle einen Ordner auf deinem PC wo der Repo landen soll. Empfehlung: `C:\Code\mala-brain` (Windows) oder `~/Code/mala-brain` (Mac)
5. Klick `Clone`
6. Warte 30 Sekunden bis 2 Minuten, je nach Internet
7. Fertig, der ganze Mala-Brain-Ordner ist jetzt auf deinem PC

**Hilfe:** wenn `Repository not found` kommt, dann ist deine Einladung noch nicht durch. Zurück zu Schritt 2.

**Wo ist der Ordner jetzt?** Auf Windows: `C:\Code\mala-brain` (oder wo du es hingelegt hast). Du kannst da im Datei-Explorer reingucken und siehst alle Files.

---

## Schritt 5, Claude Code installieren

Claude Code ist der KI-Assistent der das Mala-Brain kennt. Er liest die Files im Repo und hilft dir bei allem.

### Option A, einfach (Empfehlung für Dieter)

1. Geh auf https://claude.com/code
2. Klick `Download for <dein OS>`
3. Öffne die Installer-Datei
4. Folge dem Installer mit Standard-Optionen
5. Nach Installation: Claude Code öffnen
6. Bei der ersten Frage: mit deinem Anthropic-Account einloggen (oder Account erstellen, falls noch nicht da)
7. Anthropic-Account brauchst du einen kostenpflichtigen Pro-Plan (20 USD pro Monat), oder Matteo gibt dir den Mala-Team-Zugang

### Option B, Terminal-Version (für später, falls Lust)

```
npm install -g @anthropic-ai/claude-code
```

(Braucht Node.js installiert. Erstmal Option A nehmen.)

**Hilfe:** wenn der Anthropic-Account-Plan nicht klar ist, Matteo fragen. Mala hat ein Team-Setup.

---

## Schritt 6, Claude Code mit dem Mala-Brain verbinden

1. Öffne Claude Code
2. Klick auf `Open folder` (oder ähnlich, je nach Version)
3. Wähle den Mala-Brain-Ordner (`C:\Code\mala-brain` oder wo du es hingelegt hast)
4. Claude Code lädt automatisch die `CLAUDE.md` Datei aus dem Repo, das gibt ihm den ganzen Kontext
5. Im Chat-Feld unten: tippe `Hi, was gibt es in diesem Repo?`
6. Claude sollte antworten und das Mala-Brain erklären

**Hilfe:** wenn Claude unsicher antwortet oder Files nicht findet, einmal Claude Code neu starten und Ordner nochmal öffnen.

---

## Schritt 7, deine erste Änderung machen und pushen

So machst du jetzt deine ersten Test-PRs. Anleitung was du konkret machst steht in [00-start-here/dieter-workflow.md](dieter-workflow.md). Hier der Mechanik-Teil:

### Eine Datei ändern

1. Geh in deinen Mala-Brain-Ordner im Datei-Explorer
2. Such die Datei die du ändern willst (z. B. `04-operations/customers/_TEMPLATE/profile.md` als Vorlage für deinen ersten Kunden)
3. Mach eine Kopie oder erstelle eine neue Datei mit dem Kundennamen
4. Öffne die Datei mit einem Text-Editor (Notepad reicht, besser Visual Studio Code oder die Claude-Code-Edit-Funktion)
5. Ändere oder ergänze Inhalt
6. Speichern

### Branch erstellen und Änderung pushen

GitHub Desktop:

1. Öffne GitHub Desktop
2. Oben: stelle sicher dass `Current repository` auf `mala-brain` zeigt
3. Klick auf `Current branch` oben (sollte `main` zeigen)
4. Klick auf `New branch`
5. Name: `pm/<kurzes-thema>` (z. B. `pm/customer-audiomarke`)
6. Klick `Create branch`
7. Du arbeitest jetzt auf dem neuen Branch, nicht mehr direkt auf `main`
8. Gehe zurück in den Datei-Explorer, mach deine Änderungen
9. Zurück in GitHub Desktop: links siehst du die geänderten Dateien
10. Im Feld unten links `Summary`: schreib was du gemacht hast, z. B. `customer profile audiomarke angelegt`
11. Klick `Commit to pm/customer-audiomarke`
12. Oben rechts: `Publish branch` (beim ersten Mal) oder `Push origin`
13. Klick im Banner der erscheint: `Create Pull Request`
14. Browser öffnet sich auf GitHub.com mit dem PR-Formular
15. Reviewer auswählen: Matteo (Operations) oder Lars (Pricing)
16. Klick `Create pull request`

**Fertig.** Matteo oder Lars sehen jetzt deinen PR, können kommentieren und mergen.

**Hilfe:** Fehler `Permission denied` heisst meist dass du nicht als Collaborator drin bist. Zurück zu Schritt 2.

---

## Schritt 8, regelmässig syncen

Wenn andere im Repo Änderungen gemacht haben, willst du die auf deinen PC ziehen.

1. GitHub Desktop öffnen
2. Stelle sicher du bist auf Branch `main`
3. Klick `Fetch origin` oben
4. Falls Änderungen da sind: `Pull origin`
5. Fertig, dein lokaler Ordner ist jetzt auf neuestem Stand

**Macht das mindestens einmal pro Tag,** sonst arbeitest du auf veralteten Files.

---

## Häufige Probleme und Lösungen

| Problem | Lösung |
|---|---|
| `Repository not found` beim Clone | Du bist noch nicht als Collaborator eingeladen, Schritt 2 |
| GitHub Desktop fragt nach Passwort | Logout in GitHub Desktop, Sign in mit Browser nochmal |
| `Permission denied (publickey)` beim Push | Nochmal ausloggen aus GitHub Desktop und neu anmelden |
| Claude Code findet die `CLAUDE.md` nicht | Falscher Ordner geöffnet, Schritt 6 nochmal |
| Anthropic-Account-Login geht nicht | Matteo fragen welches Mala-Team-Setup gilt |
| Merge-Konflikte nach Pull | Nicht selber lösen, Chris pingen |

---

## Was als nächstes

Jetzt wo das Setup steht, du machst deine 3 Test-PRs nach [00-start-here/dieter-workflow.md](dieter-workflow.md). Bei Fragen Matteo oder Chris pingen, kein Risiko zu fragen.

Stand: 19.05.2026.
