# Git Cleanup Patterns for ai_collection Repo

Session-tested patterns for cleaning up unwanted changes in the ai_collection repo during cron skill sync operations.

## Problem

When copying skills into the ai_collection repo, many unrelated `example.py` files and scripts get marked as modified. `git add -A` captures all of them, leading to bloated commits.

## Clean-Reset Pattern

```bash
# 1. Stash everything (including untracked new skill dirs)
git stash --include-untracked

# 2. Restore to clean state
git checkout -- .

# 3. Restore stash (brings back new skill SKILL.md files)
git stash pop

# 4. Verify: only new skill files should remain staged
git status --short

# 5. Add only what you want
git add collection/skills/{skill-name}/SKILL.md INDEX.md

# 6. Verify staged files before commit
git diff --cached --stat
```

## Alternative: Direct Checkout

```bash
git checkout -- collection/skills/*/scripts/ collection/skills/*/references/ collection/skills/*/assets/ scripts/
# Also reset subdirectory variants
git checkout -- collection/skills/quantum-neural-architecture-search/scripts/ collection/skills/quantum-neural-barren-plateau/scripts/
```

## Commit Safety Check

Always run `git diff --cached --stat` before committing. If more than ~5 files appear (when you only meant to add 2-3 skill files), reset and redo:

```bash
git reset HEAD -- collection/skills/*/scripts/ collection/skills/*/references/ scripts/
git checkout -- collection/skills/*/scripts/ collection/skills/*/references/ scripts/
```