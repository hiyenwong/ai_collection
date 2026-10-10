---
name: domain-saturation-validation
description: "Complete validation workflow for automated research when domain saturation is detected (>80% paper coverage). Verifies synchronization across local skills, repository, INDEX.md, knowledge graph, and Obsidian notes. Activation: domain saturation, research validation, sync verification, complete validation"
---

# Domain Saturation Validation

## Overview

When automated research cron jobs detect domain saturation (typically >80% of discovered papers already have skills), the workflow should pivot from skill creation to complete synchronization validation. This ensures all components are properly synced across the entire system rather than assuming partial completion.

## When to Use This Skill

- **Domain saturation detected**: >80% of discovered papers already have existing skills
- **Cron job research**: Automated paper discovery finds mostly covered papers  
- **Sync validation needed**: Verify complete integration across all systems
- **Gap remediation**: Fix missing components in partially-synced papers

## Complete Validation Checklist

For each paper with an existing skill, verify ALL of the following components:

### 1. Local Skill Existence
Verify the skill exists in the local Hermes directory:
```bash
ls ~/.hermes/skills/ai_collection/{skill-name}/SKILL.md
```

### 2. Repository Skill Existence  
Verify the skill is synced to the ai_collection GitHub repository:
```bash
ls ~/ai_github/ai_collection/collection/skills/{skill-name}/SKILL.md
```

### 3. INDEX.md Entry
Verify the paper entry exists in the main index:
```bash
grep -q "{skill-name}" ~/ai_github/ai_collection/INDEX.md
```

### 4. Knowledge Graph Entity
Verify the paper entity exists in the knowledge graph database:
```sql
SELECT arxiv_id FROM papers WHERE arxiv_id = '{arxiv_id}';
```

### 5. Obsidian Note
Verify the research note exists in the Obsidian vault:
```bash
ls "~/Library/Mobile Documents/iCloud~md~obsidian/Documents/neuroscience-research/"*{date}*"{paper-title}".md
```

## Gap Remediation Patterns

### Missing Repository Skill
Copy from local to repository:
```bash
cp ~/.hermes/skills/ai_collection/{skill-name}/SKILL.md ~/ai_github/ai_collection/collection/skills/{skill-name}/SKILL.md
```

### Missing Knowledge Graph Entry
Insert paper entity with proper relationships:
```sql
INSERT INTO papers (arxiv_id, title, authors, published_date, categories, abstract, skill_name, created_at) 
VALUES ('{arxiv_id}', '{title}', '{authors}', '{date}', '{categories}', '{abstract}', '{skill_name}', '{current_date}');
```

### Missing Obsidian Note
Create comprehensive research note including:
- Paper information (title, authors, arXiv ID, date, categories)
- Core problem statement and key innovations
- Experimental results and applications  
- Skill integration details (name, activation keywords)
- Key insights and future directions

## Ghost Directory Detection

A subtle failure mode occurs when the skill directory exists but SKILL.md is missing, creating "ghost directories":

```bash
# Detect ghost directories
for dir in ~/ai_github/ai_collection/collection/skills/*/; do
  if [ ! -f "$dir/SKILL.md" ]; then
    echo "Ghost directory detected: $dir"
    # Fix by copying from local
    skill_name=$(basename "$dir")
    cp ~/.hermes/skills/ai_collection/"$skill_name"/SKILL.md "$dir"/SKILL.md
  fi
done
```

## Workflow Steps

### Step 1: Detect Domain Saturation
- Calculate coverage rate: `(papers with skills) / (total papers discovered)`
- If coverage > 80%, execute validation workflow

### Step 2: Validate Each Paper
- For each paper with existing skill, run complete validation checklist
- Log any missing components

### Step 3: Remediate Gaps
- Apply appropriate remediation pattern for each missing component
- Verify fixes after application

### Step 4: Report Status
- If all papers fully validated: respond with `[SILENT]`
- If gaps found and fixed: report remediation summary
- If critical failures: report specific issues for manual intervention

## Real-World Example

**Session**: August 5, 2026  
**Paper**: "Divisive Normalization Shapes Low-Rank Slow Manifolds for Continuous Working Memory" (2608.01947)  
**Issue**: Skill existed locally and in repository, INDEX.md entry present, Obsidian note created, but missing from knowledge graph  
**Resolution**: Added paper entity to kg.db `papers` table with proper skill relationship  
**Lesson**: Always verify knowledge graph sync even when other components appear complete

## Best Practices

1. **Always run complete validation** when domain saturation is detected
2. **Fix gaps immediately** rather than waiting for batch processing  
3. **Document remediation** in session notes for future reference
4. **Prefer verification over assumption** - automated systems can have partial failures
5. **Use systematic checklist** to avoid missing any component

## Tools Used

- **terminal**: File system operations and git commands
- **sqlite3**: Knowledge graph database queries and updates  
- **read_file/write_file**: Obsidian note creation and management
- **search_files**: Pattern matching for existing skills and files

## Activation Keywords

- domain saturation
- research validation  
- sync verification
- complete validation
- gap remediation
- knowledge graph sync
- repository validation
- Obsidian sync
- INDEX.md verification
- ghost directory detection

## Related Skills

- **research-paper-pattern-extractor**: Extracts patterns from knowledge graph analysis
- **automated-research-cron-workflow**: End-to-end automated research pipeline
- **skill-creator**: Creates new skills from research papers
- **kg-operations**: Knowledge graph database operations