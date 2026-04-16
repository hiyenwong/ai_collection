---
name: skill-collection-sync
description: Sync skills between Hermes agent and ai_collection repository. Use when user asks to submit skills to ai_collection, sync skills to GitHub, or push skill updates.
triggers:
  - "submit to ai_collection"
  - "sync skills"
  - "push skills"
  - "commit skills"
  - "skills to collection"
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [Skills, Sync, GitHub, ai_collection, Git]
    related_skills: [github-repo-management, ai-agent-data-migration]
---

# Skill Collection Sync

Sync skills from Hermes agent to the ai_collection GitHub repository.

## Overview

This skill handles the workflow of:
1. Comparing skills between Hermes (`~/.hermes/skills/`) and ai_collection (`collection/skills/`)
2. Copying missing skills from Hermes to ai_collection
3. Committing and pushing changes to GitHub

## Prerequisites

- ai_collection repository cloned at `~/Documents/projects/ai_projects/ai_collection/`
- Git configured with GitHub authentication
- Write access to the ai_collection repository

## Workflow

### Step 1: Analyze Skills

First, discover all skills in both locations:

```python
from pathlib import Path

hermes_skills_dir = Path("~/.hermes/skills").expanduser()
ai_collection_skills_dir = Path("~/Documents/projects/ai_projects/ai_collection/collection/skills").expanduser()

# Get Hermes skills (recursive search for SKILL.md)
hermes_skills = {}
for skill_md in hermes_skills_dir.rglob("SKILL.md"):
    skill_dir = skill_md.parent
    skill_name = skill_dir.name
    # Skip backup files
    if "_backup" in skill_name:
        continue
    hermes_skills[skill_name] = skill_dir

# Get ai_collection skills
ai_collection_skills = set()
if ai_collection_skills_dir.exists():
    for item in ai_collection_skills_dir.iterdir():
        if item.is_dir() and not item.name.startswith('.'):
            ai_collection_skills.add(item.name)

# Find skills to sync
skills_to_sync = set(hermes_skills.keys()) - ai_collection_skills

print(f"Hermes skills: {len(hermes_skills)}")
print(f"ai_collection skills: {len(ai_collection_skills)}")
print(f"Skills to sync: {len(skills_to_sync)}")
```

### Step 2: Copy Skills

Copy missing skills to ai_collection:

```python
import shutil

copied = []
failed = []

for skill_name in sorted(skills_to_sync):
    src = hermes_skills[skill_name]
    dst = ai_collection_skills_dir / skill_name
    
    try:
        shutil.copytree(src, dst)
        copied.append(skill_name)
        print(f"✓ Copied: {skill_name}")
    except Exception as e:
        failed.append((skill_name, str(e)))
        print(f"✗ Failed: {skill_name}: {e}")

print(f"\nTotal copied: {len(copied)}")
```

### Step 3: Git Operations

Add, commit, and push changes:

```bash
# Navigate to repository
cd ~/Documents/projects/ai_projects/ai_collection

# Check status
git status --short

# Add all new skills
git add collection/skills/

# Commit
git commit -m "Add X new skills from Hermes agent collection"

# Handle remote updates if needed
git pull origin main --rebase

# Push
git push origin main
```

### Step 4: Verify

Confirm the push was successful:

```bash
# Check recent commits
git log --oneline -3

# Count total skills
ls collection/skills/ | wc -l
```

## Handling Conflicts

If push is rejected due to remote changes:

```bash
# Stash local changes
git stash

# Pull and rebase
git pull origin main --rebase

# Restore stashed changes
git stash pop

# Push again
git push origin main
```

## Complete Script

```python
#!/usr/bin/env python3
"""Sync skills from Hermes to ai_collection"""

from pathlib import Path
import shutil
import subprocess

def sync_skills():
    # Paths
    hermes_skills_dir = Path("~/.hermes/skills").expanduser()
    ai_collection_dir = Path("~/Documents/projects/ai_projects/ai_collection").expanduser()
    ai_collection_skills_dir = ai_collection_dir / "collection/skills"
    
    # Get Hermes skills
    hermes_skills = {}
    for skill_md in hermes_skills_dir.rglob("SKILL.md"):
        skill_dir = skill_md.parent
        skill_name = skill_dir.name
        if "_backup" in skill_name:
            continue
        hermes_skills[skill_name] = skill_dir
    
    # Get ai_collection skills
    ai_collection_skills = set()
    if ai_collection_skills_dir.exists():
        for item in ai_collection_skills_dir.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                ai_collection_skills.add(item.name)
    
    # Find skills to sync
    skills_to_sync = set(hermes_skills.keys()) - ai_collection_skills
    
    if not skills_to_sync:
        print("All skills already synced!")
        return
    
    # Copy skills
    for skill_name in sorted(skills_to_sync):
        src = hermes_skills[skill_name]
        dst = ai_collection_skills_dir / skill_name
        shutil.copytree(src, dst)
        print(f"✓ {skill_name}")
    
    # Git operations
    subprocess.run(["git", "add", "collection/skills/"], cwd=ai_collection_dir)
    subprocess.run([
        "git", "commit", "-m", 
        f"Add {len(skills_to_sync)} new skills from Hermes agent collection"
    ], cwd=ai_collection_dir)
    
    # Try to push (handle conflicts)
    result = subprocess.run(
        ["git", "push", "origin", "main"],
        cwd=ai_collection_dir,
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0 and "rejected" in result.stderr:
        # Handle conflict
        subprocess.run(["git", "stash"], cwd=ai_collection_dir)
        subprocess.run(["git", "pull", "origin", "main", "--rebase"], cwd=ai_collection_dir)
        subprocess.run(["git", "stash", "pop"], cwd=ai_collection_dir)
        subprocess.run(["git", "push", "origin", "main"], cwd=ai_collection_dir)
    
    print(f"\n✅ Synced {len(skills_to_sync)} skills successfully!")

if __name__ == "__main__":
    sync_skills()
```

## Best Practices

1. **Always check before syncing** - Verify which skills will be copied
2. **Skip backup files** - Exclude `*_backup` directories
3. **Handle git conflicts** - Remote may have updates, use rebase strategy
4. **Verify after push** - Confirm commit is on remote
5. **Keep categories** - Hermes organizes skills in category folders, ai_collection flattens them

## Pitfalls

- **Don't overwrite existing skills** - Only copy missing ones
- **Don't forget git pull** - Remote may have changes
- **Don't ignore errors** - Some skills may fail to copy
- **Don't push credentials** - Ensure no API keys in skill files

## When to Use

- User asks to "submit skills to ai_collection"
- User wants to "sync skills to GitHub"
- User requests "push skills to collection"
- Periodic sync of new Hermes skills to central repository
