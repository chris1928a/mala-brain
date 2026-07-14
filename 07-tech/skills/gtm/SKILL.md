---
name: gtm
description: >
  GTM Funnel Cluster für Chris (Erler Ventures). Vier verzahnte Sub-Skills die
  zusammen einen Niche-zu-Asset Funnel bilden: Call-Transkripte werden zu Asset
  Foundations (12-row CSV), aus denen dann Landing Pages, Cold Email Sequences
  und Meta/Google Ads gebaut werden. Adaption der EO GTM Skills (pas-ventures/eo-gtm-skills-public)
  in deutscher Voice mit DACH-Compliance und Anbindung an Chris' Sales Leadership
  Board und Sherpa Sales Brain.

  Verwende diesen Skill IMMER bei: GTM, Go-to-Market, Asset Foundation, Asset
  Foundations, 12-row CSV, Bodacious Claim, Dan Kennedy Sales Letter, Landing
  Page bauen, LP für Niche, Cold Email Sequence, 3-Email Sequence, Outbound
  Cadence, Meta Ads aus Calls, Facebook Ads aus Transcripts, Google Ads aus
  Calls, Niche-Funnel, Customer Voice Mining, Hook Body CTA, Sales Letter
  Spine, EO GTM Skills, Phil Strohemann, Manuel Hartmann, PAS Ventures, GTM
  Funnel.

  Auch bei: "bau mir einen Funnel für X", "Landing Page für RC/Mala/Valtis/
  Best Guy", "Cold Outreach für Niche Y", "Meta Kampagne für Z", "Asset
  Foundations bauen", "12-row CSV aus diesen Calls", "Hook aus Transcripts",
  "ICP Niche definieren für Funnel".

  Routet zu Sub-Skills je nach Asset-Typ. Asset Foundations sind IMMER zuerst,
  dann erst Landing Page / Outbound / Ads.
---

# GTM Funnel Cluster

Master für den kompletten GTM-Stack von Chris. Vier Sub-Skills die ein durchgaengiges Funnel-Pattern abbilden, von Call-Transkript bis zu fertigem Conversion-Asset.

Adaption von [pas-ventures/eo-gtm-skills-public](https://github.com/pas-ventures/eo-gtm-skills-public) in deutscher Voice. Companion Repo ist Chris' eigener [sales-leadership-board](https://github.com/chris1928a/sales-leadership-board).

## Kern-Idee

Du kannst keine Conversion-Copy schreiben bevor du die Foundation-Arbeit gemacht hast. Dan Kennedy: "Don't write to people. Listen to people, then echo what they already said." Heißt konkret: Call-Transkripte sind die Quelle, alles andere ist Ableitung.

```
Call-Transkripte
    │
    ▼
asset-foundations  ──►  12-row CSV pro Niche
    │                   (ICP, Pains, Bodacious Claim, Benefits)
    │
    ├──►  landing-pages   (HTML LP + Signup-Flow)
    ├──►  outbound        (3-Email Cold Sequence + 5 Opener)
    └──►  ads             (Meta + Google Hooks/Bodies/CTAs)
```

Jeder Sub-Skill konsumiert spezifische Rows aus dem CSV. Die Hand-off-Tables in den Sub-Skill-Files zeigen welche Row in welche Asset-Stelle fliesst.

## Routing

| User-Frage enthaelt | Lade |
|---|---|
| Asset Foundations, 12-row CSV, ICP aus Calls, Niche definieren, Pain Mining, Customer Voice Extract, Bodacious Claim formulieren | `asset-foundations/SKILL.md` |
| Landing Page bauen, LP für Niche, Hero Section, Pain Story, Signup-Flow, progressive Email-Capture | `landing-pages/SKILL.md` |
| Cold Email, Cold Sequence, Outbound, 3-Email, Opener-Varianten A-E, Subject Line Test, HeyReach Cadence | `outbound/SKILL.md` |
| Meta Ads, Facebook Ads, Instagram Ads, Google Ads, Hook/Body/CTA, Ad-Varianten aus Calls, Creative Brief | `ads/SKILL.md` |

## Sub-Skills

### `asset-foundations/`
Quelle des Funnels. 12-row CSV pro Niche aus Call-Transkripten. Dan Kennedy Sales Letter Spine: Position, Deepest Desires, Up-at-Night, Frustrated, Angry, Tried-but-Failed, Trends, Cost-of-Inaction, Solution, Bodacious Claim, Secondary Benefits, Auxiliary Benefits.

Output: `asset-foundations-{venture}-{YYYY-MM-DD}.csv` mit einer Spalte pro Niche.

### `landing-pages/`
Niche-spezifische HTML Landing Pages plus zweite Signup-Page mit progressiver Email-Capture. Pain-First Hero, deutsche SMB-Optik, "kein IT-Projekt / kein technisches Wissen / Server in Deutschland" Sprache. Konsumiert Rows 2, 3-5, 6, 7, 11, 12 aus dem Foundation CSV.

Output: `{niche}.html` plus `{niche}-signup.html`.

### `outbound/`
3-Email Cold Sequence in Markdown. Email 1 mit fuenf Varianten A-E (Lang, Mittel, Kurz, Feedback, Provokant), Email 2 als Follow-up mit Reply-Threading, Email 3 als Breakup. Plus fuenf alternative Subject Lines pro Niche für A/B Testing.

Output: `outbound-{niche-slug}.md`.

### `ads/`
10 Hooks plus 5 Bodies plus 5 CTAs aus Customer-Quotes. Plus "do not use" Liste mit Insider-Jargon der im Feed nicht funktioniert. Plus Creative Brief für Visuals. Funktioniert für Meta (Facebook, Instagram) und Google Ads (RSA, PMax, Display).

Output: `ads-{niche-slug}.md`.

## Quick Facts

- **Ursprung**: pas-ventures/eo-gtm-skills-public (Phil Strohemann + Manuel Hartmann + Chris, EO MyEO Lunch & Learn 24.04.2026)
- **Companion Repo**: github.com/chris1928a/sales-leadership-board (Chris' Sales Brain Pipeline)
- **Frameworks**: Dan Kennedy (Sales Letter, Magnetic Marketing), Alex Hormozi ($100M Offers/Leads), Robert Cialdini (Influence), Russell Brunson (DotCom Secrets, Expert Secrets), Jordan Belfort (Way of the Wolf), Noah Kagan (Million Dollar Weekend)
- **Voice**: deutsche Umlaute Pflicht, keine Em-Dashes, keine AI-Phrasen, DACH-Compliance (DSGVO, Sie/Du, deutsche Server)

## Niche-Anwendung

Der Stack ist Niche-agnostisch. Pro Venture wird einmal das Foundation CSV gebaut, dann werden die anderen drei Sub-Skills mit dem CSV gefuettert.

Aktive Anwendungen im Erler Brain:

| Venture | Playbook |
|---|---|
| Recruitment Circle | `skills/people/rc/playbooks/gtm-rc.md` (DACH B2B Tech Recruiting, HeyReach Cadence) |
| Mala / Relevio | TBD bei Bedarf |
| Best Guy | TBD bei Bedarf |
| Valtis | TBD bei Bedarf |
| Solvera | TBD bei Bedarf |

## Verhältnis zu User-Global anthropic-skills

User-Global hat bereits ads-generator, landing-page-optimizer, icp-extractor, sales-script-rewriter. Diese laufen parallel. Der `gtm` Cluster im erler-brain Repo überschreibt nichts, sondern ergaenzt:

- Lokale Voice Rules (Notion ist Single Source of Truth)
- DACH-Compliance Layer
- Anbindung an Chris' Sherpa-Pipeline (Call-Transkripte aus Close.com via Deepgram)
- Anbindung an Sales Leadership Board (Score-Daten als Foundation-Input)

Bei Frage "Meta Ads" ohne Kontext zuerst prüfen ob Niche bereits ein Foundation CSV hat. Wenn ja, gtm/ads. Wenn nein, gtm/asset-foundations zuerst.

## Anti-Patterns

- **Asset bauen ohne Foundation**: Landing Page oder Ad ohne 12-row CSV ist Vermutung. Erst CSV, dann Asset.
- **Eine Niche ist keine Niche**: Wenn "alle Kunden" als eine Spalte gefuellt werden, konvertiert nichts. 3-5 Niches pro Foundation, jede separat.
- **AI-Phrasen im Output**: KI, AI, kuenstliche Intelligenz tauchen in Hero/CTA nicht auf. Stattdessen: Automatisierung, Entlastung, Assistent.
- **Em-Dashes im Output**: Voice Rule Verstoss. Nutze Komma, Punkt, Klammer, Doppelpunkt.
- **Erfundene Pains**: Rows 3-5 müssen aus Transkripten kommen. Wenn nichts da ist, mark als `[unbekannt - in nächstem Call fragen]`.

## Datenquellen-Reihenfolge für Foundations

1. Sherpa Call-Scoring (sales-leadership-board, bot_new.py Output, Deepgram-Transkripte)
2. Close.com Call-Transcripte direkt
3. Fireflies / tl;dv / Otter Exports
4. Manuell gepasted Transcripte vom User

Bei RC-Niches: Foundation darf an die ICP v2 P1/P2/P3 Tiers aus Close anknuepfen (siehe `rc_icp_close_match_apr28` Memory).

## Boundary Protocol

- **Lesen**: Call-Transkripte, Notion-Daten, Sales Board Sheets sind okay zu lesen.
- **Schreiben**: Foundation CSVs und Asset-Files lokal okay. Notion nicht beschreiben ausser explizit angefragt. Email-Drafts nie automatisch senden.
- **Externe Sichtbarkeit**: Landing Pages und Ads nie publishen ohne Chris-Approval pro Asset. Gilt besonders für Meta/Google Ads die Geld kosten.

## Migrations-Status

- [x] Phase 1: Cluster-Build (diese Datei plus 4 Sub-Skills)
- [x] Phase 2: RC-Playbook in `skills/people/rc/playbooks/gtm-rc.md`
- [x] Phase 3: Source-Map Update für `gtm` Cluster
- [ ] Phase 4: Erste Foundation-Runs RC P1/P2/P3 (wartet auf Close-Call-Pulls)

## Voice Rules

Siehe `skills/_meta/voice-rules.md`. Alle Outputs aus diesem Cluster müssen Umlaute korrekt nutzen, keine Em-Dashes enthalten, keine AI-Phrasen verwenden.
