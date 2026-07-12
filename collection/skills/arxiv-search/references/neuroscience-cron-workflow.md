# Neuroscience Cron Research Workflow

Complete workflow for scheduled neuroscience paper discovery, analysis, and synchronization.

## Trigger
- Cron job: scheduled neuroscience research automation
- Keywords: `neuroscience`, `brain network`, `neural dynamics`, `spiking neural network`, `computational neuroscience`
- Target: 1-2 most innovative papers per session

## Search Strategy

### 1. RSS Discovery (Primary - Most Reliable)
```python
import urllib.request, ssl, re

feeds = [
    'https://rss.arxiv.org/rss/q-bio.NC',     # Neurons and Cognition
    'https://rss.arxiv.org/rss/cs.NE',        # Neural and Evolutionary Computing
    'https://rss.arxiv.org/rss/cs.AI+cs.LG',  # AI + ML cross-domain
    'https://rss.arxiv.org/rss/q-bio.NC+cs.NE', # Neuroscience + Neural Computing
]

# Parse: <item> → <title>, <link>, <description>, <pubDate>
# arxiv_id from link: re.search(r'arxiv\\.org/abs/([\\d.]+)', link)
# Keyword filter on title+desc
```

### 2. Browser Category Listing (Fallback)
```python
browser_navigate("https://arxiv.org/list/q-bio.NC/new")
browser_snapshot(full=true)  # Extract titles, IDs, abstracts
```

### 3. Individual Paper Details
```python
browser_navigate("https://arxiv.org/abs/{id}")
# Abstract: <blockquote class="abstract mathjax">
# Authors: linked author names
# Categories: Subjects table cell
```

## Paper Selection Criteria

Innovation keyword scoring:
```python
keywords = [
    'novel', 'new framework', 'transformer', 'foundation model',
    'spiking', 'neuromorphic', 'quantum', 'BCI',
    'continual learning', 'meta-learning', 'diffusion',
    'mechanistic', 'interpretability', 'causal', 'dynamics',
    'hierarchical', 'multi-scale', 'emergent',
    'plasticity', 'synaptic', 'astrocyte', 'connectome'
]
score = sum(1 for kw in keywords if kw in (title + abstract).lower())
```

Select papers with highest scores (typically 4-8 keywords match).

## Duplicate Check (4 Levels)

Before creating any skill:

```bash
# Level 0: Name search across all categories
ls -d ~/.hermes/skills/*/potential-skill-name*

# Level 1: arXiv ID search across ALL SKILL.md files
grep -rl "2605.XXXXX" ~/.hermes/skills/*/SKILL.md

# Level 2: ai_collection project copy
grep -rl "2605.XXXXX" ~/ai_github/ai_collection/collection/skills/*/SKILL.md

# Level 3: INDEX.md entries
grep "2605.XXXXX" ~/ai_github/ai_collection/INDEX.md
```

If duplicate exists, UPDATE the existing skill (patch/edit), do NOT create new one.

## Skill Creation

### Skill Location
- **Hermes profile**: `~/.hermes/skills/ai_collection/{skill-name}/SKILL.md`
- **ai_collection sync**: `/Users/hiyenwong/ai_github/ai_collection/collection/skills/{skill-name}/`

### Skill Naming Convention
- Use paper's core contribution (not paper title or arXiv ID)
- Examples: `spiking-transformer-continual-learning`, `brain-network-control-nodes`, `astrocyte-3body-plasticity`
- Avoid: `arxiv-2605-xxxxx`, `paper-title-exactly`

### Required Frontmatter
```yaml
---
name: {skill-name}
description: "{one-line summary from paper abstract}"
---
```

### Body Structure
1. **Title**: Paper title and arXiv ID
2. **Background**: Problem/motivation (1-2 sentences)
3. **Methodology**: Core approach (key equations if applicable)
4. **Key Findings**: Main results
5. **Applications**: Use cases, triggers
6. **Pitfalls**: Limitations, edge cases
7. **References**: Link to paper, related skills

## ai_collection Sync

### 1. Copy Skill Directory
```bash
cp -r ~/.hermes/skills/ai_collection/{skill-name}/ ~/ai_github/ai_collection/collection/skills/
```

### 2. Update INDEX.md
Append at top:
```markdown
## YYYY-MM-DD - Neuroscience Research (Cron Job)

### {Paper Title}
- [[{skill-name}]] - One-line description (arXiv: {id})
  - Core insight 1
  - Core insight 2
  - **Activation**: keyword1, keyword2, keyword3
```

### 3. Git Sync
```bash
cd /Users/hiyenwong/ai_github/ai_collection
git add collection/skills/{skill-name}/ INDEX.md
git commit -m "feat: add {skill-name} from arXiv {id}"
git push
```

## Obsidian Sync

### Save Location (Verified 2026-06-03)
```
~/Library/Mobile Documents/iCloud~md~obsidian/Documents/{YYYY-MM-DD} Neuroscience Research (Cron Job).md
```

**Note**: The actual Obsidian vault uses flat structure at Documents root — not nested subdirectories like `Neuroscience/arxiv/YYYY-MM/`. Check existing files with:
```bash
ls ~/Library/Mobile Documents/iCloud~md~obsidian/Documents/*.md | grep -i neuroscience
```

### Note Format
```markdown
# {Paper Title}

**arXiv**: [{id}](https://arxiv.org/abs/{id})
**Date**: YYYY-MM-DD
**Categories**: {cats}

## Abstract
{abstract}

## Key Insights
1. {insight}
2. {insight}

## Methodology
{methodology summary}

## Applications
{use cases}

## Related
- [[{skill-name}]] (ai_collection skill)
- [[Related Paper 1]]
```

## kg.db Update

### DB Paths (Verified 2026-06-03)
- **Primary**: `/Users/hiyenwong/.hermes/knowledge_graph/kg.db` — papers + relations tables
- **Legacy Wiki**: `/Users/hiyenwong/wiki/kg.db` — entities + kg_vectors (older schema)
- **Workspace**: `/Users/hiyenwong/.openclaw/workspace/scripts/kg.db` — legacy workspace KG

**CRITICAL**: The active knowledge graph for neuroscience cron jobs is `/Users/hiyenwong/.hermes/knowledge_graph/kg.db` with simplified schema:

### Active Schema (kg.db at knowledge_graph/)
```sql
CREATE TABLE papers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    arxiv_id TEXT UNIQUE,              -- '2602.18690'
    title TEXT NOT NULL,
    authors TEXT,
    published TEXT,
    categories TEXT,
    abstract TEXT,
    keywords TEXT,
    created_at TEXT
);

CREATE TABLE relations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_id INTEGER,
    target_id INTEGER,
    relation_type TEXT,               -- 'cites', 'similar_to', 'has_keyword'
    created_at TEXT
);
```

**Key differences from old schema**:
- INTEGER auto-increment IDs (not TEXT arxiv IDs)
- No `kg_vectors` table — embeddings not used
- No `importance_score` — simpler schema
- `relation_type` column for flexible relation types

### Import Pattern
```python
import sqlite3, json, hashlib, struct, numpy as np

def text_to_embedding(text, dim=256):
    seed_bytes = hashlib.sha256(text.encode("utf-8")).digest()[:4]
    seed = struct.unpack(">I", seed_bytes)[0]
    rng = np.random.RandomState(seed)
    vec = rng.randn(dim).astype(np.float32)
    return json.dumps((vec / np.linalg.norm(vec)).tolist())

papers = [
    ('arxiv_2605.XXXXX', 'Title', 'paper', 'q-bio.NC,cs.NE', 
     'Abstract...', 'arxiv', '2026-05-28'),
]

for db_path in ['/Users/hiyenwong/wiki/kg.db', 
                '/Users/hiyenwong/.openclaw/workspace/scripts/kg.db']:
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    for paper in papers:
        c.execute('INSERT OR IGNORE INTO entities VALUES (?,?,?,?,?,?,?)', paper)
        vec = text_to_embedding(f"paper {paper[1]} {paper[4]}")
        c.execute('INSERT OR IGNORE INTO kg_vectors VALUES (?,?)', (paper[0], vec))
    conn.commit()
```

**CRITICAL**: Never use `sqlite3` CLI with inline INSERT strings containing quotes/LaTeX — silently fails. Always use Python parameterized queries.

## Session Failure Handling

When ALL discovery methods fail:
1. **Check existing skills** — thousands of neuroscience skills in library
2. **Query kg.db** — `sqlite3 wiki/kg.db "SELECT * FROM entities WHERE type='paper'"`
3. **Review reference files** — skills have paper excerpts, domain notes
4. **Synthesize existing content** — update, cross-link existing skills
5. **Log failure** — update skill with new failure patterns

This is NOT failure — library has months of accumulated research.

## Timing

- **RSS fetch**: ~30 seconds for 4 feeds
- **Paper reading**: ~2-5 minutes per paper (abstract + key sections)
- **Skill creation**: ~3-5 minutes
- **Full sync**: ~10-15 minutes total

## Pitfalls

1. **API rate limits** — Use RSS/browser first, API last
2. **Duplicate skills** — Always check all 4 levels before creating
3. **sqlite3 CLI silent failures** — Use Python with parameterized queries
4. **INDEX.md escaping** — Use simple format, avoid special characters
5. **kg.db schema mismatch** — Use `entities` table, NOT `kg_entities`
6. **Cross-domain sparse intersection** — 0 RSS matches is expected for narrow topics

## Related References

- [references/neuroscience-research-pattern.md](references/neuroscience-research-pattern.md) — multi-query API pattern
- [references/arxiv-cron-research-notes.md](references/arxiv-cron-research-notes.md) — session notes
- [references/medical-quantum-rss-discovery.md](references/medical-quantum-rss-discovery.md) — cross-domain RSS
- [references/kg-vector-dimension-mismatch.md](references/kg-vector-dimension-mismatch.md) — embedding dimension
- [references/sqlite3-insert-pitfall.md](references/sqlite3-insert-pitfall.md) — silent INSERT failures