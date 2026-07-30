---
name: ghost-directory-detection-pattern
description: "Methodology for detecting and resolving 'ghost directories' in ai_collection skill synchronization where skill directories exist but SKILL.md files are missing. This pattern addresses a chronic sync failure mode observed in automated research cron jobs."
license: Complete terms in LICENSE.txt
---

# Ghost Directory Detection Pattern

## Problem Description

A subtler sync failure occurs when the skill DIRECTORY exists in the ai_collection repo (`collection/skills/{name}/` with subdirs like `assets/`, `references/`, `scripts/`) but the `SKILL.md` file itself is MISSING — creating a "ghost" directory that passes `ls -d` but fails `ls SKILL.md`.

This happens when:
1. `init_skill.py` creates the directory structure with nested subdirectories  
2. The SKILL.md write was interrupted or failed
3. The copy operation missed the top-level SKILL.md file
4. Only the inner directory structure was copied

## Detection Pattern

```bash
# Bulk ghost detection
for d in ~/ai_github/ai_collection/collection/skills/*/; do
  name=$(basename "$d")
  if [ -d "$d" ] && [ ! -f "$d/SKILL.md" ]; then
    echo "GHOST DIR: $name"
    # Fix by copying from local skills
    cp ~/.hermes/skills/ai_collection/$name/SKILL.md $d/SKILL.md
  fi
done
```

## Real-World Examples

This pattern found 5 ghost dirs in a single sweep on 2026-07-03:
- membrane-potential-alignment  
- rats-register-attention
- brainworld-4d-fmri
- boosting-brain-to-image-tribe-v2
- braindyn-sheaf-neural-ode

## Integration with Domain Saturation Workflow

When domain saturation is detected (all papers have local skills), run ghost directory detection as part of the validation workflow:

1. Check for missing skill files: `[ -f ~/ai_github/ai_collection/collection/skills/$name/SKILL.md ]`
2. Check for ghost directories: `[ -d ~/ai_github/ai_collection/collection/skills/$name/ ] && [ ! -f ~/ai_github/ai_collection/collection/skills/$name/SKILL.md ]`
3. Fix both cases by copying from local skills
4. Verify INDEX.md entries exist for all skills
5. Commit fixes with message: "fix: resolve ghost directories and sync gaps"

## Prevention

After any `init_skill.py` run, verify the SKILL.md was actually written before proceeding to sync:
```bash
if [ ! -f ~/.hermes/skills/ai_collection/$name/SKILL.md ]; then
  echo "ERROR: SKILL.md not created - aborting sync"
  exit 1
fi
```

This prevents ghost directories from being created in the first place.

## When to Use This Skill

Use this methodology when:
- Running automated research cron jobs that create and sync skills
- Validating ai_collection repository integrity
- Debugging missing skill content despite directory existence
- Performing bulk sync gap detection and resolution

## Related Skills

- `domain-saturation-workflow` - Overall validation workflow for saturated domains
- `automated-research-workflow` - Complete cron job automation patterns
- `git-cleanup-patterns` - Git workflow patterns for skill synchronization