# Skill Directory Sync Pattern

## Problem

The skill library has **two parallel directories** that should contain overlapping content:
- `~/.hermes/skills/ai_collection/` (underscore) — 700+ skills, the main collection
- `~/.hermes/skills/ai-collection/` (hyphen) — ~27 skills, a curated subset

Skills created in one directory don't automatically appear in the other.

## Sync Strategy

### ai_collection → ai-collection (populate curated subset)
Only sync high-value, recent papers:
```python
recent_to_sync = [
    "free-energy-moe-routing",
    "multiplication-free-spike-time-fpga",
    "neurobiological-craving-signature-social",
    "mle-toolbox-eeg-meg",
    "triple-configuration-brain-network-rnn",
    # Add others as needed
]
for s in recent_to_sync:
    src = f"ai_collection/{s}"
    dst = f"ai-collection/{s}"
    if exists(src) and not exists(dst):
        copytree(src, dst)
```

### ai-collection → ai_collection (backfill missing)
New skills added to ai-collection should be copied to ai_collection:
```python
skills_to_sync = [
    "subclinical-anxiety-brain-networks",
    "evolutionary-snn-classifier",
    "eeg-channel-adaptation-benchmark",
    # ... check what's missing
]
```

### ai_collection → main skills dir
Skills in ai_collection that are also useful standalone:
```python
for s in new_skills:
    src = f"ai_collection/{s}"
    dst = f"skills/{s}"
    if exists(src) and not exists(dst):
        copytree(src, dst)
```

## Cron Job Checklist

1. Search arXiv (browser fallback preferred — `https://arxiv.org/list/{category}/recent`), identify new papers
2. **MANDATORY duplicate check**: Search existing skills by arXiv ID AND keywords across **ALL** category directories (`ai_collection/`, `neuroscience/`, `systems-engineering/`, etc.), not just `ai_collection/`. See main SKILL.md "Duplicate Skill Naming & Multi-Category Detection Pitfall" for the 4-level check.
3. Create new skills if needed (prefer `ai_collection` as canonical source)
4. **Sync skill to git repo — VERIFIED PATTERNS (2026-05-21)**:

   **Pattern A — mkdir -p + individual file copy (MOST RELIABLE)**:
   ```bash
   mkdir -p ~/ai_github/ai_collection/collection/skills/{skill-name}
   cp ~/.hermes/skills/ai_collection/{skill-name}/SKILL.md ~/ai_github/ai_collection/collection/skills/{skill-name}/SKILL.md
   ```
   This pattern was verified working when `cp -r` silently failed to create the target directory.

   **Pattern B — cp -r (works when target parent exists)**:
   ```bash
   cp -r ~/.hermes/skills/ai_collection/{skill-name}/ ~/ai_github/ai_collection/collection/skills/
   ```
   May silently fail if the target directory structure doesn't exist. Always verify with `ls` after.

   **Verification step** (always do after sync):
   ```bash
   ls ~/ai_github/ai_collection/collection/skills/{skill-name}/SKILL.md
   ```

5. Update `~/ai_github/ai_collection/INDEX.md` with paper summary — see [index-md-maintenance.md](index-md-maintenance.md) for the correct insertion approach (use Python `readlines`/`writelines`, NOT `sed`).
6. `cd ~/ai_github/ai_collection && git add collection/skills/{skill}/ INDEX.md && git commit -m "..." && git push`
7. Save Obsidian note: `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/`
8. Update both kg.db instances:
   - `~/ai_github/ai_collection/kg.db` (entities, relationships, research_log tables)
   - `~/.openclaw/workspace/kg.db` (kg_entities, kg_vectors, kg_relationships tables)
   - See `references/kg-db-schema.md` for schema differences
