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

1. Search arXiv, identify new papers
2. Check if corresponding skill exists in any of: main, ai_collection, ai-collection
3. Create new skills if needed (prefer ai_collection as canonical)
4. Sync ai_collection → ai-collection (recent/high-value only)
5. Sync ai-collection → ai_collection (backfill)
6. Sync ai_collection → main (standalone-useful skills)
7. Update ai_collection/INDEX.md
8. Update Obsidian wiki notes
