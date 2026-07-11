# Skill Naming Collisions

## Problem

Skills may exist in multiple locations simultaneously:
- `~/.hermes/skills/<name>/` (local)
- `~/.hermes/skills/ai_collection/<name>/` (ai_collection external_dir)
- `~/.hermes/skills/openclaw-imports/<name>/` (openclaw-imports external_dir)

When `skill_view(name='<name>')` is called, Hermes refuses to guess and returns an error with 2-3 matching paths. This blocks the skill loading step entirely.

## Impact

- Cron research pipelines fail when trying to load `skill-creator`, `research-skill-extractor`, or domain skills that exist in multiple locations
- Ambiguous skills cannot be loaded by bare name — must use full categorized path

## Mitigation

1. **Use categorized paths**: `skill_view(name='ai_collection/skill-creator')` instead of bare name
2. **Consolidation**: The curator handles de-duplication at scale. Individual agents should NOT delete skills from external directories
3. **Workaround**: When `skill_view` fails with "ambiguous", fall back to reading the SKILL.md directly via the file path from the error message

## Known Collisions (as of 2026-06-11)

- `skill-creator` — 3 locations
- `research-skill-extractor` — 3 locations
- `skill-extractor` — multiple locations
- `quantum-system-engineering` — 3 locations
- `quantum-error-correction-methods` — 2 locations
- `skill-creator` — 3 locations
