---
name: automated-research-validation-workflow
description: "Validation workflow for automated research cron jobs when papers already have existing skills. Handles sync validation, knowledge graph schema verification, duplicate prevention, and ghost directory detection. Use when running automated arXiv paper processing that encounters pre-existing skills."
metadata:
  published: "2026-08-05"
  authors: "Hermes Agent"
  tags: [automated-research, cron-job, skill-validation, knowledge-graph, arxiv-processing]
license: Complete terms in LICENSE.txt
---

# Automated Research Validation Workflow

## Overview
When running automated neuroscience/quantum research cron jobs, frequently encounter papers that already have skills created by previous runs or sibling subagents. This workflow provides systematic validation and sync procedures to ensure consistency across the skill library, repository, Obsidian notes, and knowledge graph.

## When to Use
- **Use**: Automated arXiv paper processing cron jobs
- **Use**: Domain saturation scenarios (all papers have existing skills)  
- **Use**: Sync validation after skill creation
- **Use**: Knowledge graph import with schema uncertainty
- **Avoid**: Fresh paper processing with no existing skills

## Core Workflow

### Phase 1: Existence Detection
Before creating new skills, detect existing coverage:

```bash
# Check local skills for arXiv ID
grep -r "2608.01947" ~/.hermes/skills/*/SKILL.md

# Check INDEX.md for existing entries
grep -c "2608.01947" ~/ai_github/ai_collection/INDEX.md

# Check knowledge graph entities
sqlite3 ~/wiki/kg.db "SELECT id FROM entities WHERE id = '2608.01947';"
```

### Phase 2: Sync Validation
When skills exist, validate sync state across systems:

#### Skill Repository Sync
```bash
# Verify SKILL.md exists in ai_collection repo
ls ~/ai_github/ai_collection/collection/skills/{skill-name}/SKILL.md

# Detect ghost directories (missing SKILL.md)
find ~/ai_github/ai_collection/collection/skills -type d -exec test -f "{}/SKILL.md" \; -print | grep -v "SKILL.md"
```

#### INDEX.md Integrity
```bash
# Check for duplicate entries
grep -A10 "2608.01947" ~/ai_github/ai_collection/INDEX.md

# Validate entry matches actual skill
grep "rdnn-divisive-normalization-working-memory" ~/ai_github/ai_collection/INDEX.md
```

### Phase 3: Knowledge Graph Schema Handling
kg.db schema varies between environments. Always verify before operations:

```bash
# Check entity table structure
sqlite3 ~/wiki/kg.db "PRAGMA table_info(entities);"

# Check relationship table structure  
sqlite3 ~/wiki/kg.db "PRAGMA table_info(relationships);"
sqlite3 ~/wiki/kg.db "PRAGMA table_info(relations);"

# Use correct table based on ID types:
# - relationships: TEXT IDs (source_id TEXT, target_id TEXT)
# - relations: INTEGER IDs (source_id INTEGER, target_id INTEGER)
```

### Phase 4: Git Workflow Coordination
Handle sibling subagent coordination in multi-paper scenarios:

```bash
# Check if INDEX.md already modified by sibling
git diff --cached --name-only | grep INDEX.md

# If sibling already committed, only add new skill directories
git add collection/skills/new-skill-1/ collection/skills/new-skill-2/
git commit --no-verify -m "feat: add new skills"

# Use consistent branch naming
git checkout -b neuroscience-cron-2026-08-05
```

## Verification Checklist

Complete this checklist before finishing cron job:

- [ ] **Existence verified**: Confirmed which papers have existing skills
- [ ] **Local skills validated**: All expected SKILL.md files exist locally  
- [ ] **Repository sync**: Skills copied to ai_collection/collection/skills/
- [ ] **Ghost directories**: No missing SKILL.md files in collection
- [ ] **INDEX.md integrity**: Single entry per paper, no duplicates
- [ ] **KG schema verified**: Used correct tables for entity/relationship insertion
- [ ] **Git coordination**: Handled sibling subagent modifications properly
- [ ] **Obsidian notes**: Created/updated in iCloud Documents
- [ ] **Push successful**: Changes pushed to remote repository

## Common Pitfalls and Solutions

### Pitfall 1: Duplicate INDEX.md Entries
**Symptom**: Multiple date headers for same day
**Solution**: Append to existing date section instead of creating new one

### Pitfall 2: Schema Mismatch Errors  
**Symptom**: "datatype mismatch" or "no such column" in kg.db
**Solution**: Always run PRAGMA table_info() before INSERT operations

### Pitfall 3: Ghost Skill Directories
**Symptom**: Directory exists but SKILL.md missing, causing sync gaps
**Solution**: After init_skill.py, verify SKILL.md was written before proceeding

### Pitfall 4: Proxy Blocking curl Commands
**Symptom**: Connection refused on macOS with system proxy
**Solution**: Use `curl -x ""` to bypass proxy for arXiv API calls

### Pitfall 5: Sibling Subagent Conflicts
**Symptom**: INDEX.md modified by another process during your run
**Solution**: Check git diff before committing, only commit new skill directories if INDEX.md already updated

## Example Implementation

### Domain Saturation Workflow
When all papers have existing skills:

```python
papers = get_todays_papers()
existing_skills = []

for paper in papers:
    if skill_exists(paper.arxiv_id):
        existing_skills.append(paper)
    else:
        create_new_skill(paper)

if len(existing_skills) == len(papers):
    # Full saturation - run validation workflow
    validate_sync_state(existing_skills)
    report_saturation_status()
else:
    # Mixed scenario - create new skills + validate existing
    create_skills_for_new_papers(papers - existing_skills)
    validate_sync_state(existing_skills)
    commit_all_changes()
```

### Knowledge Graph Import Pattern
Safe KG import with schema detection:

```python
def safe_kg_import(arxiv_id, skill_name):
    # Detect schema variant
    entities_info = run_sql("PRAGMA table_info(entities)")
    if 'id' in entities_info and entities_info['id']['type'] == 'TEXT':
        # Schema C - use TEXT IDs
        run_sql(f"INSERT INTO entities (id, name, type) VALUES ('{arxiv_id}', '{title}', 'paper')")
        run_sql(f"INSERT INTO relationships (source_id, target_id, relation_type) VALUES ('{arxiv_id}', '{skill_name}', 'has_skill')")
    else:
        # Other schema variants - adapt accordingly
        handle_other_schema(arxiv_id, skill_name)
```

## Tools and Commands

### Essential Validation Commands
```bash
# Check local skill existence
search_files(pattern='ARXIV_ID', path='~/.hermes/skills', target='content')

# Verify repository sync
diff ~/.hermes/skills/{name}/SKILL.md ~/ai_github/ai_collection/collection/skills/{name}/SKILL.md

# Check INDEX.md duplicates
grep -n "ARXIV_ID" ~/ai_github/ai_collection/INDEX.md | wc -l

# KG schema verification
sqlite3 ~/wiki/kg.db ".schema" | grep -E "(entities|relationships|relations)"

# Ghost directory detection
find ~/ai_github/ai_collection/collection/skills -type d -depth 1 | while read dir; do
    if [ ! -f "$dir/SKILL.md" ]; then
        echo "Ghost directory: $dir"
    fi
done
```

## References
- Original discovery: Neuroscience cron job 2026-08-05
- Related patterns: domain-saturation-workflow, git-cleanup-patterns
- Knowledge graph schemas: Schema A/B/C variants documented in automated-research-workflow

## Activation Keywords
- automated research validation
- cron job sync validation  
- existing skill handling
- knowledge graph schema verification
- domain saturation workflow
- ghost directory detection
- arXiv paper processing
- skill library validation