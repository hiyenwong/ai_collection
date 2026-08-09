---
name: research-skill-duplicate-prevention
description: "Guidelines and patterns for preventing duplicate entries in INDEX.md during automated research workflows. Provides detection methods, prevention strategies, and resolution procedures for handling duplicate skill entries in knowledge repositories."
metadata:
  arxiv_id: ""
  published: "2026-08-08"
  authors: "Hermes Agent"
  tags: [research-workflow, duplicate-prevention, index-management, knowledge-repository]
license: Complete terms in LICENSE.txt
---

# Research Skill Duplicate Prevention

## Overview

This skill provides guidelines and patterns for preventing duplicate entries in INDEX.md during automated research workflows. It addresses the common problem of multiple entries for the same paper appearing in knowledge repositories due to concurrent processing, session overlaps, or manual intervention conflicts.

## Problem Statement

When processing arXiv papers automatically, duplicate entries can appear in INDEX.md when:
- The same paper is processed multiple times across different sessions
- Concurrent subagents create entries independently without coordination  
- Manual edits conflict with automated updates
- Batch processing workflows lack deduplication steps

## Detection Methods

### ArXiv ID Search Pattern
Always use the arXiv ID as the unique identifier for detection:

```bash
# Check if entry exists before creating
if grep -q "arXiv: {id}" INDEX.md; then
    echo "Entry already exists"
else
    echo "Safe to create new entry"
fi
```

### Duplicate Detection Command
After any INDEX.md modification, run this validation:

```bash
# Find duplicate arXiv IDs
grep -o "arXiv: [0-9]\{4\}\.[0-9]\{5\}" INDEX.md | sort | uniq -d
```

## Prevention Strategies

### 1. Pre-Creation Verification
Always verify existence before creating entries:

```python
def should_create_entry(arxiv_id, index_path):
    """Check if entry already exists in INDEX.md"""
    with open(index_path, 'r') as f:
        content = f.read()
    return f"arXiv: {arxiv_id}" not in content
```

### 2. Atomic Batch Processing
When processing multiple papers:
1. Collect all candidate entries
2. Deduplicate by arXiv ID  
3. Write all entries in single operation
4. Validate for duplicates

### 3. Consistent Entry Format
Use standardized format to make detection reliable:

```
### {Paper Title}
- [[{skill-name}]] - {one-sentence description} (arXiv: {id})
  - {core point 1}
  - {core point 2}  
  - **Activation**: {keyword1}, {keyword2}
```

## Resolution Procedures

### When Duplicates Are Found
1. **Compare entry quality**: Keep the more detailed/complete entry
2. **Verify placement**: Ensure entry is under correct topic section
3. **Remove simpler entry**: Delete the basic/duplicate version
4. **Commit fix**: Use descriptive commit message

### Example Resolution
From 2026-08-08 session:
- **Problem**: Two entries for "Layered Surprise Cascades" (arXiv: 2608.05481)
- **Analysis**: First entry was basic, second was detailed but misplaced
- **Solution**: Kept detailed entry, removed basic entry, verified proper placement
- **Validation**: Confirmed single entry exists with correct formatting

## Best Practices

### Single Source of Truth
- Each arXiv ID should have exactly one entry in INDEX.md
- Treat duplicate detection as mandatory validation step
- Log warnings when duplicates are detected during creation

### Error Handling
- If duplicate detected during automated creation, skip and log warning
- Never overwrite existing entries without quality comparison
- Implement rollback capability for batch operations

### Regular Maintenance
- Include duplicate check in cron job validation phase
- Periodically scan entire INDEX.md for historical duplicates
- Update this skill when new duplicate patterns emerge

## Related Skills
- `ai_collection/automated-research-workflow` - Overall research automation
- `ai_collection/skill-creator` - Skill creation guidelines  
- `research-literature-kg` - Knowledge graph management

## Activation Keywords
- duplicate prevention
- index management
- research workflow
- knowledge repository
- arXiv processing
- skill synchronization
- INDEX.md validation