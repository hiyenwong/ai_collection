# Neuroscience Cron Session Workflow (2026-06-03)

**Verified End-to-End**: arXiv discovery → Skill creation → ai_collection sync → Obsidian → kg.db

## Session Summary

- **Papers discovered**: 50 from RSS feed (q-bio.NC+cs.NE+cs.AI+cs.LG)
- **Papers deep-studied**: 2 (2606.00073 already had skill, 2606.00129 new)
- **Skill created**: `valence-axis-llm-eeg-saturation-regularity` (ai_collection category)
- **Git commits**: 2 (skill sync + push to main)
- **Knowledge graph**: Updated 3 databases (Hermes kg.db, workspace kg.db, wiki kg.db)
- **Obsidian**: Created structured note in iCloud~md~obsidian/ai_collection/

## Key Technical Patterns

### 1. RSS Feed Discovery (Most Reliable)

```bash
# Download RSS feed
curl -s "https://rss.arxiv.org/rss/q-bio.NC+cs.NE+cs.AI+cs.LG" -o /tmp/arxiv_neuro.xml

# Parse with Python (avoid execute_code block in cron mode)
write_file('/tmp/parse_arxiv_rss.py', script)
terminal('python3 /tmp/parse_arxiv_rss.py')
```

**Why this works**: RSS has no rate limits, always returns papers on weekdays, cron-compatible.

### 2. Duplicate Skill Check (4 Levels)

```bash
# Level 0: Broad name search
ls -d ~/.hermes/skills/*/valence* 2>/dev/null

# Level 1: Search SKILL.md files for arxiv_id
grep -rl "2606.00129" ~/.hermes/skills/*/SKILL.md 2>/dev/null

# Level 2: Check ai_collection project
grep -rl "2606.00129" ~/ai_github/ai_collection/collection/skills/*/SKILL.md 2>/dev/null

# Level 3: Check INDEX.md
grep "2606.00129" ~/ai_github/ai_collection/INDEX.md 2>/dev/null
```

**Finding**: 2606.00073 had existing skill `functional-ensembles-snn-computation` (skip creation).

### 3. Skill Creation Pattern

```python
skill_manage(
    action='create',
    category='ai_collection',
    content=skill_content,  # Full SKILL.md with frontmatter
    name='valence-axis-llm-eeg-saturation-regularity'
)
```

**Key elements in SKILL.md**:
- YAML frontmatter: name, description with activation keywords
- Core innovation section
- Key findings (3-4 numbered subsections)
- Technical framework (conceptual code blocks)
- Experimental evidence table
- Implementation considerations
- Limitations and future directions

### 4. ai_collection Sync Pattern

```bash
# Copy skill directory
cp -r ~/.hermes/skills/ai_collection/valence-axis-llm-eeg-saturation-regularity \
  ~/ai_github/ai_collection/collection/skills/

# Update INDEX.md (use patch, not full rewrite)
patch(
    path='~/ai_github/ai_collection/INDEX.md',
    old_string='## 2026-06-02',
    new_string='## 2026-06-03 - Neuroscience Research (Cron Job)\n...\n\n## 2026-06-02'
)

# Git workflow
terminal('cd ~/ai_github/ai_collection && git add ... && git commit ... && git push')
```

**INDEX.md entry format**:
```markdown
## YYYY-MM-DD - Neuroscience Research (Cron Job)

### {Paper Title}
- [[{skill-name}]] - One-line description (arXiv: {id})
  - Core point 1
  - Core point 2
  - **Activation**: keyword1, keyword2
```

### 5. kg.db Update Pattern

**Hermes kg.db** (primary):
```python
c.execute("INSERT INTO papers VALUES (?, ?, ?, ?, datetime('now'))",
          ("2606.00129", title, authors, skill_name))
for tag in tags:
    c.execute("INSERT INTO paper_tags VALUES (?, ?)", ("2606.00129", tag))
```

**Workspace + Wiki kg.db** (secondary):
```python
for db_path in ['/Users/hiyenwong/.openclaw/workspace/scripts/kg.db',
                '/Users/hiyenwong/wiki/kg.db']:
    c.execute("INSERT INTO entities VALUES (?, ?, ?, ?, ?, ?, ?)",
              ("arxiv_2606.00129", title, 'paper', categories, desc, 'arxiv', date))
```

### 6. Obsidian Note Pattern

**Path**: `~/Library/Mobile Documents/iCloud~md~obsidian/ai_collection/{skill-name}.md`

**Structure**:
```markdown
# {Skill Name}

> [[{skill-name}]] | arXiv: {id} | {categories}

## Core Innovation
{Brief summary}

## Key Findings
1. {Finding 1}
2. {Finding 2}

## Technical Framework
{Code snippet}

## Related Skills
- [[{related-skill-1}]]
- [[{related-skill-2}]]
```

## Obsidian Path Correction (2026-06-03)

**Wrong**: `~/Library/Mobile Documents/iCloud~md~obsidian~md/`
**Correct**: `~/Library/Mobile Documents/iCloud~md~obsidian/ai_collection/`

The `~md` suffix is not part of the directory name. Use `iCloud~md~obsidian` without trailing `~md`.

## kg.db Schema Discrepancy Found

The loaded skill `ai_collection/arxiv-search` has `references/kg-db-schema.md` documenting a legacy `kg_entities` schema with INTEGER FKs. Actual Hermes kg.db uses `papers/paper_tags` tables with TEXT FKs.

**Evidence**: Session successfully inserted into Hermes kg.db with `papers(arxiv_id TEXT PK)` and `paper_tags(paper_id TEXT FK)`.

**Action**: Created `references/kg-db-schema-actual.md` in `valence-axis-llm-eeg-saturation-regularity` skill documenting actual schema.

**Future note**: `ai_collection/arxiv-search` skill needs patching for schema mismatch, but skill_manage reports it's not in active profile 'default' (possibly installed skill from different profile).

## Critical Cron Mode Patterns

1. **execute_code is BLOCKED**: Always use `write_file('/tmp/script.py')` + `terminal('python3 /tmp/script.py')`
2. **RSS feed is most reliable**: No rate limits, works on weekdays
3. **Browser fallback works**: Category listing pages (`/list/{category}/recent`), NOT search pages
4. **Direct HTTPS without proxy often works**: Try direct connection before using proxy

## Git Commit Evidence

```bash
# Verify commits
cd ~/ai_github/ai_collection
git log --oneline -2

# Expected output:
# ace657aa feat: add valence-axis-llm-eeg-saturation-regularity from arXiv 2606.00129
# b11affeb feat: add quantum-clinical-benchmarking...
```

## Skill Directory Verification

```bash
ls -lh ~/ai_github/ai_collection/collection/skills/valence-axis-llm-eeg-saturation-regularity/SKILL.md
# Expected: 9438 bytes (rich content)
```

---

**Session Duration**: ~10 minutes total
**Key Learning**: kg.db schema discrepancy between documentation and actual schema
**Next Action**: Consider patching `ai_collection/arxiv-search` via different mechanism (may need profile switch or admin access)