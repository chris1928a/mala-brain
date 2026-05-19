---
name: call-analytics
description: Skill für automatische Bewertung von Kundengesprächen. Liest Transkripte (Fireflies, tl;dv, Otter, Gemini-Notes), bewertet auf 1-5 Skala über 4 Dimensionen, gibt Feedback an Mitarbeiter. Triggert auf Call-Recordings, Transkripte, Mitarbeiter-Coaching.
voice_rules: ../_shared/voice-rules.md
notion_pages:
  - title: Call-Analytics-Framework
    url: TBD-after-notion-setup
  - title: Mitarbeiter-Bewertungs-Dimensionen
    url: TBD-after-notion-setup
related_skills:
  - icp-extractor
  - sales-coaching
---

# Call Analytics Skill

Owner: Matteo Giazzi (entwickelt im April 2026)

## Trigger Keywords

- "Call analysieren"
- "Transkript bewerten"
- "Mitarbeiter-Coaching"
- "Account Manager Feedback"
- "Customer Call Score"
- "Discovery-Call Review"
- "Demo-Call Score"
- "1-5 Bewertung Call"

## Was dieser Skill kann

1. **Transcript-Analyse:** Liest Transkripte aus Fireflies, tl;dv, Otter, Gemini-Notes
2. **Bewertung auf 4 Dimensionen** (1-5 Skala):
   - Discovery-Tiefe
   - Einwand-Behandlung
   - Closing-Stärke
   - Tonalität / Empathie
3. **Mitarbeiter-Feedback:** Generiert konkrete Coaching-Hinweise pro Dimension
4. **Bulk-Scoring:** Mehrere Transkripte parallel scoren mit Aggregation pro Mitarbeiter

## Bewertungs-Dimensionen Detail

### 1. Discovery-Tiefe (1-5)
- 1 = nur oberflächliche Fragen
- 3 = SPIN/Challenger-Fragen, aber nicht konsistent
- 5 = strukturiertes Discovery mit Pain-Identifikation und Quantifizierung

### 2. Einwand-Behandlung (1-5)
- 1 = Einwände werden ignoriert oder argumentiert
- 3 = LARC-Framework (Listen, Acknowledge, Restate, Confirm) teilweise
- 5 = Empathie + Reframe + konkrete Lösung

### 3. Closing-Stärke (1-5)
- 1 = kein klares Next-Step, "we'll think about it"
- 3 = klares Next-Step aber kein Commitment
- 5 = konkretes Commitment mit Datum + Owner + Stakeholder

### 4. Tonalität / Empathie (1-5)
- 1 = monoton, distanziert
- 3 = freundlich aber nicht engaged
- 5 = aktiv zuhörend, Pacing matched dem Kunden

## Disclaimer (PFLICHT mit jedem Output)

> "Die Bewertung basiert nur auf Transkript-Text. Emotionale Nuancen, Pausen, Tonfall sind nicht zu 100 % erfasst. Die Bewertung ist ein Coaching-Hinweis, kein finales Performance-Urteil."

## Trigger-Verhalten

Wenn aktiviert:
1. User uploaded Transkript (oder gibt File-Path)
2. Skill liest Voice-Rules
3. Skill scored auf 4 Dimensionen
4. Skill generiert konkrete Coaching-Hinweise
5. Output in standardisiertem Format mit Disclaimer

## Beispiel-Output

```
Mitarbeiter: <Name>
Datum: <Call-Datum>
Kunde: <Kunde>

Discovery-Tiefe: 3/5
- Strukturiertes Discovery zu Anfang (+)
- Pain-Quantifizierung fehlt (-)
- Coaching-Hinweis: Frag konkret nach Cost-of-Inaction

Einwand-Behandlung: 4/5
- Einwand "zu teuer" gut gehandhabt (+)
- LARC-Framework angewendet (+)
- Coaching-Hinweis: Reframe noch stärker auf ROI

Closing-Stärke: 2/5
- Kein klares Next-Step (-)
- Coaching-Hinweis: Beim Closing immer konkretes Datum + Owner verlangen

Tonalität: 4/5
- Freundlich, aktiv zuhörend (+)
- Coaching-Hinweis: Pacing kann am Anfang langsamer sein

Gesamt: 13/20

Disclaimer: Bewertung basiert nur auf Transkript-Text. Emotionale Nuancen sind nicht zu 100 % erfasst.
```

## Beispiel-Prompts

- "Score den Call mit Mueller GmbH von letzter Woche"
- "Bulk-Analyse alle AM-Calls aus dem letzten Monat"
- "Wer im Team braucht das meiste Coaching auf Closing?"
- "Vergleiche Mitarbeiter X vs Y über die letzten 10 Calls"

## Referenz-Files

- `references/scoring_rubric.md` - detaillierte 1-5-Skala pro Dimension
- `references/coaching_patterns.md` - typische Coaching-Hinweise pro Schwäche
- `references/disclaimer.md` - Standard-Disclaimer-Texte
