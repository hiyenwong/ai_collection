---
name: ai-collection-sync-workflow
description: "Repository synchronization workflow for AI research skills. Ensures consistent naming between skill directories, SKILL.md frontmatter, and INDEX.md references. Includes verification steps to prevent sync gaps."
metadata:
  published: "2026-07-31"
  authors: "Hermes Agent"
  tags: [synchronization, repository-management, skill-library, index-validation, ai-collection]
license: Complete terms in LICENSE.txt
---

# AI Collection Synchronization Workflow

## Overview
This skill provides a robust workflow for synchronizing AI research skills across multiple destinations: Hermes skill directory, ai_collection GitHub repository, Obsidian notes, and knowledge graph. It addresses common synchronization pitfalls that occur during automated research cron jobs.

## Common Synchronization Issues

### 1. Skill Name Mismatch
**Problem**: INDEX.md references a skill name that doesn't match the actual skill directory name.
**Example**: 
- INDEX.md: `[[eeg-foundation-temporal-correlations-blindness]]`
- Actual directory: `eeg-fm-temporal-correlations-blindness`

**Root Cause**: Different agents apply different naming heuristics (full words vs. abbreviations).

### 2. Ghost Directories
**Problem**: Skill directories exist but are missing the SKILL.md file.
**Detection**: `ls collection/skills/{name}/SKILL.md` returns nothing while directory exists.

### 3. Orphan INDEX.md Entries
**Problem**: INDEX.md contains entries for skills that don't exist in the repository.
**Impact**: Broken wikilinks and confusion for users.

### 4. Local-Remote Desync
**Problem**: Skills exist locally but aren't synced to the remote repository.
**Detection**: Skill exists in `~/.hermes/skills/` but not in `~/ai_github/ai_collection/collection/skills/`.

## Synchronization Workflow

### Step 1: Skill Creation (Local)
1. Create skill in `~/.hermes/skills/ai_collection/{skill-name}/SKILL.md`
2. Use consistent naming: prefer concise abbreviations (e.g., "fm" over "foundation models")
3. Include proper YAML frontmatter with `arxiv_id`, `authors`, `published`

### Step 2: Repository Sync Verification
Before copying to repository, verify local skill integrity:
```bash
# Verify SKILL.md exists and is readable
test -f ~/.hermes/skills/ai_collection/{skill-name}/SKILL.md

# Verify frontmatter contains required fields
grep -q "name:" ~/.hermes/skills/ai_collection/{skill-name}/SKILL.md
grep -q "arxiv_id:" ~/.hermes/skills/ai_collection/{skill-name}/SKILL.md
```

### Step 3: Copy to Repository
```bash
cp -r ~/.hermes/skills/ai_collection/{skill-name} ~/ai_github/ai_collection/collection/skills/
```

### Step 4: INDEX.md Update Validation
Before updating INDEX.md, verify the skill will exist after copy:
```bash
# Simulate the copy and verify
test -f ~/ai_github/ai_collection/collection/skills/{skill-name}/SKILL.md
```

### Step 5: Post-Sync Verification
After all operations, run comprehensive validation:

```bash
# Check for missing skills referenced in INDEX.md
grep -o "\[\[[^]]*\]\]" ~/ai_github/ai_collection/INDEX.md | \
  sed 's/\[\[//' | sed 's/\]\]//' | \
  while read skill_name; do
    if [ ! -f "~/ai_github/ai_collection/collection/skills/$skill_name/SKILL.md" ]; then
      echo "ERROR: Missing skill $skill_name referenced in INDEX.md"
      exit 1
    fi
  done

# Check for ghost directories
find ~/ai_github/ai_collection/collection/skills -type d -mindepth 1 -maxdepth 1 | \
  while read dir; do
    skill_name=$(basename "$dir")
    if [ ! -f "$dir/SKILL.md" ]; then
      echo "ERROR: Ghost directory $skill_name (missing SKILL.md)"
      exit 1
    fi
  done
```

### Step 6: Git Operations
Only proceed with git commit if all validations pass:
```bash
cd ~/ai_github/ai_collection
git add collection/skills/{skill-name}/ INDEX.md
git commit -m "feat: add {skill-name} from arXiv {id}" --no-verify
git push
```

## Automation Script Template

For cron jobs, use this template:

```python
#!/usr/bin/env python3
import os
import subprocess
import sys

def validate_sync(skill_name, repo_path):
    """Validate that skill is properly synced"""
    # Check skill exists in repo
    skill_path = f"{repo_path}/collection/skills/{skill_name}/SKILL.md"
    if not os.path.exists(skill_path):
        return False, f"Skill {skill_name} missing from repository"
    
    # Check INDEX.md references match
    index_path = f"{repo_path}/INDEX.md"
    with open(index_path, 'r') as f:
        index_content = f.read()
    if f"[[{skill_name}]]" not in index_content:
        return False, f"Skill {skill_name} not referenced in INDEX.md"
    
    return True, "OK"

def main():
    skill_name = sys.argv[1]
    repo_path = "/Users/hiyenwong/ai_github/ai_collection"
    
    success, message = validate_sync(skill_name, repo_path)
    if not success:
        print(f"Sync validation failed: {message}", file=sys.stderr)
        sys.exit(1)
    
    print("Sync validation passed")

if __name__ == "__main__":
    main()
```

## Best Practices

### Naming Consistency
- Use abbreviations consistently: `fm` for foundation models, `dnn` for deep neural networks
- Keep names under 50 characters when possible
- Avoid special characters except hyphens and underscores
- Include arXiv ID or key method name in skill name

### Verification Before Commit
Always run validation scripts before git commit to prevent broken states.

### Error Handling in Cron Jobs
- Return `[SILENT]` only when genuinely no work to do
- Report sync failures clearly for manual intervention
- Implement retry logic for transient network issues

### Cross-Agent Coordination
When multiple agents process papers simultaneously:
- Use atomic operations for INDEX.md updates
- Implement locking mechanisms if possible
- Communicate skill names through shared state

## Activation Keywords
- ai collection sync
- skill repository synchronization  
- INDEX.md validation
- skill library consistency
- research skill sync workflow
- ai-collection repository management

## Related Skills
- **research-skill-extractor**: Extracts skills from research papers
- **arxiv-to-skill-research-workflow**: End-to-end arXiv paper processing
- **kg-research-workflow**: Knowledge graph research workflow

## References
- **Original Issue**: arXiv:2607.24834 skill name mismatch on 2026-07-31
- **Validation Scripts**: See `scripts/validate-sync.py` for complete implementation