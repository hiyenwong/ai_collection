---
name: ai-collection-research-sync
description: Automated research pipeline for searching papers, extracting patterns, creating class-level skills, and syncing to ai_collection project + Obsidian + knowledge graph
version: 1.0.0
author: agent
created: 2026-05-29
tags:
  - research-automation
  - arxiv
  - skill-creation
  - knowledge-management
  - neuroscience
  - cron-job
activation:
  - "neuroscience paper automation"
  - "arxiv research sync"
  - "create skills from papers"
  - "sync to ai_collection"
  - "research pipeline"
  - "automated paper research"
---

# AI Collection Research Sync Pipeline

## Overview

Automated end-to-end pipeline for discovering research papers, extracting reusable patterns, creating **class-level** skills, and synchronizing across multiple knowledge systems (ai_collection GitHub repo, Obsidian wiki, kg.db knowledge graph).

**Trigger**: Scheduled cron job OR manual research session for domain-specific paper discovery.

## Pipeline Steps

### 1. Search Papers

**Tool**: `arxiv-search` skill or direct arXiv API/RSS

**Parameters**:
- Keywords: domain-specific (neuroscience → "brain network, neural dynamics, spiking neural network, computational neuroscience, EEG, fMRI")
- Categories: q-bio.NC, cs.AI, cs.LG, cs.NE
- Time window: last 24 hours (for cron) OR last week (for manual)
- Proxy: http://127.0.0.1:7890 (if needed for RSS feeds)

**Output**: List of relevant papers with metadata (title, abstract, arXiv ID, link, published date)

### 2. Filter & Select

**Criteria**:
- Keyword match score (count of relevant terms in title/abstract)
- Technical innovation (novel methods, not just applications)
- Relevance to existing skill coverage (prioritize gaps)

**Selection**: Top 1-2 papers for deep analysis

**Save intermediate**: `/tmp/selected_papers.json` for pipeline continuity

### 3. Create Class-Level Skills

**CRITICAL**: Skills must be **class-level**, not paper-specific.

#### ❌ Wrong Pattern (to AVOID):
```
skill-name: "eeg-transformer-positional-encoding-benchmark-arxiv-2605-29754"
Description: "Paper arXiv:2605.29754 on EEG positional encoding"
```
This creates narrow session-specific entries that clutter the library.

#### ✓ Correct Pattern:
```
skill-name: "benchmarking-positional-encoding-strategies"
Description: "Methodology for systematically comparing positional encoding approaches in transformer-based neural signal models"
```
- **Broad enough** to cover similar future papers
- **Technique-focused** (the method class, not the paper)
- **Reusable** for future sessions encountering similar work

**Skill Content Requirements**:
- Core methodology/technique (abstracted from paper)
- Step-by-step implementation guidance
- Code examples or pseudo-code
- Pitfalls and limitations
- Related skills cross-links
- Activation keywords (domain terms, not paper IDs)

**Support Files** (optional but recommended):
- `references/arxiv-{id}-notes.md`: Paper-specific details, experimental setup, key findings (session detail)
- `scripts/`: Reproducible analysis scripts if applicable
- `templates/`: Configuration templates if method requires setup

**Location**: `~/.hermes/skills/ai_collection/{skill-name}/SKILL.md`

### 4. Sync to ai_collection Project

**Destination**: `/Users/hiyenwong/ai_github/ai_collection`

**Steps**:
1. Copy skill directory:
   ```bash
   cp -r ~/.hermes/skills/ai_collection/{skill-name} /Users/hiyenwong/ai_github/ai_collection/collection/skills/
   ```

2. Update INDEX.md (prepend new entry):
   ```markdown
   ## YYYY-MM-DD - {Domain} Research (Cron Job)

   ### {Technique Class Name}
   - [[{skill-name}]] - One-line description (arXiv: {id})
     - Core insight 1
     - Core insight 2
     - **Activation**: keyword1, keyword2, keyword3
   ```
   
   **Format**:
   - Chinese description for readability
   - English Activation tags for searchability
   - Link to skill via `[[skill-name]]` Obsidian-style link

3. Git operations:
   ```bash
   cd /Users/hiyenwong/ai_github/ai_collection
   git add collection/skills/{skill-name}/ INDEX.md
   git commit -m "feat: add {skill-name} from arXiv {id}"
   git push origin main
   ```

### 5. Sync to Obsidian

**Destination**: `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/`

**Note Structure**:
- Filename: `{Technique Name} - arXiv {id}.md`
- Tags: `#neuroscience #domain #method`
- Sections:
  - Abstract (brief)
  - Key Insights (bullet points)
  - Implementation Notes (code snippets)
  - Applications
  - Related Skills (links)
  - References (arXiv link, paper cite)

**Purpose**: Quick reference for manual review, not full skill content

### 6. Update Knowledge Graph

**Database**: `~/.hermes/knowledge-graph/kg.db`

**Table**: `arxiv_papers` (create if needed)

**Schema**:
```sql
CREATE TABLE IF NOT EXISTS arxiv_papers (
    id TEXT PRIMARY KEY,
    title TEXT,
    abstract TEXT,
    link TEXT,
    published TEXT,
    keywords TEXT,
    category TEXT,
    skill_name TEXT,
    created_at TEXT
);
```

**Insert**: Link arXiv ID to skill-name for future reference

## Pitfalls & Corrections

### Pitfall 1: Creating Paper-Specific Skills

**Problem**: Naming skills after specific papers (e.g., "paper-2605-29754-eeg-pos-encoding") creates narrow entries that:
- Clutter skill library
- Can't be reused for similar future work
- Violate class-level skill architecture

**Fix**: Abstract the **technique class**:
- Paper about EEG positional encoding → skill "positional-encoding-strategies-for-neural-signals"
- Paper about multimodal fMRI → skill "multimodal-brain-encoding-methods"
- Focus on the *methodology*, not the *instance*

**Rule**: If skill name includes arXiv ID or paper title, it's wrong. Rename to technique class.

### Pitfall 2: Missing Support Files

**Problem**: SKILL.md alone lacks session-specific detail for reproduction

**Fix**: Use `references/` directory:
- `references/arxiv-{id}-session.md`: Full paper analysis, experimental setup, data sources
- `references/related-work.md`: Links to similar papers/methods
- Keep SKILL.md concise (methodology), put details in references

### Pitfall 3: arXiv RSS Feed Parsing Errors

**Problem**: XML parsing can fail due to datetime serialization issues

**Fix**: Use string format for dates in intermediate JSON, parse separately:
```python
# Don't serialize datetime objects directly
published_str = paper.get('published', '').strftime('%Y-%m-%d') if hasattr(...) else str(...)
```

### Pitfall 4: Git Push Without Pull

**Problem**: Push fails if remote has new commits

**Fix**: Always `git pull origin main` before push, or use `git pull --rebase`

## Technical Implementation

### arXiv RSS Feed URL

```
http://export.arxiv.org/api/query?search_query=cat:q-bio.NC+OR+cat:cs.AI+OR+cat:cs.LG&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending
```

Or RSS category feeds:
```
http://arxiv.org/rss/q-bio.NC
http://arxiv.org/rss/cs.AI
http://arxiv.org/rss/cs.LG
```

### Keyword Scoring

Weight keywords by domain importance:
- neuroscience domain: "brain network", "neural dynamics", "spiking", "EEG", "fMRI" → weight 2
- general ML: "transformer", "foundation model", "encoding", "multimodal" → weight 1
- negative: "review", "survey" (unless explicitly seeking surveys) → weight -1

Score = sum of keyword weights in title + abstract

### Proxy Configuration

If RSS feeds fail (network issues), use proxy:
```bash
export http_proxy=http://127.0.0.1:7890
export https_proxy=http://127.0.0.1:7890
```

In Python:
```python
import os
os.environ['http_proxy'] = 'http://127.0.0.1:7890'
```

## Example Output

### Session 2026-05-29

**Papers Selected**:
1. arXiv:2605.29754 - EEG Transformer Positional Encoding Benchmark
2. arXiv:2605.29850 - MIRAGE Multimodal fMRI Encoding

**Skills Created** (example correct naming):
- `benchmarking-positional-encoding-neural-signals` (covers positional encoding comparison methodology)
- `multimodal-brain-encoding-methods` (covers adaptive multimodal fusion for brain prediction)

**Git Commit**: `feat: add benchmarking-positional-encoding-neural-signals and multimodal-brain-encoding-methods from arXiv`

**Obsidian Notes**: Created for manual reference

**Knowledge Graph**: Updated with arXiv ID → skill-name mappings

## Related Skills

- `arxiv-search`: Paper discovery via arXiv API
- `skill-creator`: Skill template and creation guidance
- `obsidian`: Obsidian vault management
- `knowledge-graph-ops`: kg.db operations

## Future Improvements

1. **Automated skill naming**: LLM-based extraction of technique class from paper abstract
2. **Skill consolidation check**: Before creating new skill, check if existing umbrella can be extended
3. **Paper clustering**: Group related papers by technique, create single skill covering cluster
4. **Reference deduplication**: Track which papers contributed to each skill in `references/papers-covered.md`

## Support Files

**This skill includes**:

- **Session Logs**: `references/session-2026-05-29.md` - Complete execution log for May 29 cron run, including errors encountered, fixes applied, paper selection rationale, and pipeline execution details. Template for future session-specific logs.

- **Pitfall Documentation**: `references/datetime-json-serialization-pitfall.md` - Specific pitfall encountered when parsing arXiv RSS feeds with `xmltodict` — datetime objects cause JSON serialization errors. Includes 3 solutions for future pipeline runs.

- **Templates**: `templates/obsidian-note-template.md` - Reusable template for Obsidian wiki notes created by the pipeline. Includes Chinese/English bilingual structure, arXiv metadata, skill linking, and activation keywords.

- **Scripts**: `scripts/verify_pipeline.py` - Verification script to check pipeline completion. Validates: skill creation, ai_collection sync, INDEX.md updates, Obsidian notes, knowledge graph entries. Run after each cron execution.

## Cron Job Configuration

Schedule: Daily at specified time (user config)

Command:
```bash
hermes run "neuroscience paper automation" --cron
```

Or direct:
```bash
cd ~/.hermes && python scripts/arxiv_research_sync.py --domain neuroscience
```

---

**Remember**: The goal is a **library of class-level skills**, not a log of paper summaries. Each skill should be broad enough that encountering a similar paper next month doesn't create a duplicate skill—it extends or references the existing one.