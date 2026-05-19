# Shared Voice Rules - alle Skills

Geteilte Voice-Rules die JEDER Skill beim Start lädt. Identisch zu `07-tech/voice-rules.md`, aber Skill-fokussiert.

## Imports in jeden Skill

Im SKILL.md-Frontmatter:

```yaml
voice_rules: ../_shared/voice-rules.md
```

Cloud lädt die Voice-Rules automatisch beim Skill-Trigger.

## Hard-Rules (no exceptions)

1. Deutsche Umlaute (ä ö ü ß) PFLICHT, nie ae oe ue ss
2. Keine Em-Dashes (-)
3. Keine AI-Phrasen ("sicherlich", "großartig", "absolut")
4. mala kleinschreiben

## Channel-Tonalitaet

| Channel | Tonalitaet |
|---|---|
| Email-Kunden | formal, Sie-Form |
| Email-intern (Lars/Matteo) | direkt, Du-Form |
| Notion | strukturiert, voller Inhalt |
| WhatsApp | plain text, KEIN Bold-Markup, kann lowercase |
| Slack | knapp, Markdown ok |
| Code-Commits | englisch ok, präsens |

## Skill-spezifische Overrides

Wenn ein Skill abweichende Voice-Rules braucht (z. B. Cold-Call-Skript braucht Verkaufs-Tonalität), kommt das in `<skill>/voice-overrides.md`. Default = Shared Voice Rules.

## Self-Check vor jedem Skill-Output

1. Umlaute korrekt
2. Keine Em-Dashes
3. Keine AI-Phrasen
4. mala kleingeschrieben
5. Channel-Tonalität passt
6. Voice-Override (falls vorhanden) angewendet

Wenn alle 6 ja: Output. Sonst: Korrigieren.
