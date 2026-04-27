# Big Decision Framework Template

Für strategische Entscheidungen, die mehr als nur eine schnelle Bauchentscheidung brauchen. Basis: Edward de Bono's Six Thinking Hats + Strategic Reflection.

## Wann nutzen

- Investments > 10k EUR
- Architektur-Entscheidungen (z. B. VM vs Inhouse)
- Hire-Entscheidungen
- Pivot oder Repositioning
- Vendor-Auswahl
- Pricing-Strategie

## Template

```markdown
# Big Decision: <Topic>

**Datum:** YYYY-MM-DD
**Owner:** <Wer entscheidet>
**Co-Sign:** <Wer mitstimmt>
**Big Decision?** YES / NO und Begründung

---

## 1. Context / Category

### Why
- Wo kommt die Entscheidung her?
- Was ist die treibende Kraft?
- Welcher Pain-Point oder Opportunity?

### What
| Wissen | Nicht-Wissen |
|---|---|
| ... | ... |

### Who
- Decision: <Name>
- Co-Sign: <Name(n)>
- Stakeholder: <Liste>
- Expertise: <Externer Advisor wenn nötig>

### How
- Quick Gut-Feel: <ja/nein und kurze Begründung>
- Deeper Exploration nötig?

---

## 2. Six Thinking Hats

- **Facts (Weißer Hut):** Harte Daten, Zahlen, Constraints
- **Possibilities (Grüner Hut):** Kreative Optionen, Hybriden
- **Optimism (Gelber Hut):** Best-Case-Szenarien, Upsides
- **Caution (Schwarzer Hut):** Risiken, Downsides, was kann schiefgehen
- **Feeling (Roter Hut):** Bauchgefühl, Intuition, Sorgen
- **Process (Blauer Hut):** Wie kommen wir zur Entscheidung, Timeline, Gates

---

## 3. Alternatives

| ID | Alternative | Pro | Con |
|---|---|---|---|
| A | ... | ... | ... |
| B | ... | ... | ... |
| C | ... | ... | ... |

---

## 4. Decision

**Gewählt:** <Alternative-ID>

**Why:** Begründung in 2-3 Sätzen.

**How:**
- Schritt 1
- Schritt 2
- ...

**What:**
- Konkrete Deliverables
- Konkrete Constraints

**Who:**
- Owner
- Stakeholder
- Reviewer

**Values-Check:**
1. Vision: ... ✅/⚠️/❌
2. Cash-Disziplin: ...
3. IP-Eigentum: ...
4. Risiko-Streuung: ...

---

## 5. Verification

**Wie wir prüfen, dass die Decision funktioniert hat:**
- Metric 1: ...
- Metric 2: ...
- Review-Datum: ...

**Was passiert wenn Metric verfehlt:**
- Re-Decision-Trigger
- Eskalation an ...
```

## Beispiel-Decisions (mala 2026)

- 27.04.2026: VM vs Inhouse für P03 zu Decision B (VM Skelett + Inhouse Phase 2)
- 27.04.2026: Tech-Team-Komposition zu Decision W7 (VM + Junior + Senior-Reviewer)
- 27.04.2026: Founder-Build? zu Decision F4 (Pairing, nicht Solo-Build)

Volle Beispiele in Dropbox: `mala P03 Big Decision Framework - VM/Inhouse + Tech-Team + Founder-Build (27.04.2026)`

## Notion-Page-Konvention für Decisions

Pro Decision eine Notion-Page in `01 Strategy / Big Decisions / <Datum> – <Topic>`.
Inhalt = ausgefülltes Template oben.
Nach Decision: Status-Tag "Decided" + Verification-Datum als Reminder.
