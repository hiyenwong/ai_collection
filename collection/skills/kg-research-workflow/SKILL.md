---
name: kg-research-workflow
description: "End-to-end academic research workflow using knowledge graphs. Searches papers from arxiv/web, imports to KG database, generates embeddings, runs graph algorithms (PageRank, Louvain, vector search), and extracts patterns for skill creation. Use for: automated research workflows, paper analysis pipelines, KG-based literature review."
---

# KG Research Workflow

Complete workflow for academic research using knowledge graphs with sqlite-knowledge-graph.

## Features

- **Paper Acquisition**: Search arxiv, web sources, Anthropic research
- **KG Import**: Import papers as entities with keyword relations
- **Embedding Generation**: Create vector embeddings for similarity search
- **Graph Algorithms**: PageRank for importance, Louvain for communities
- **Pattern Extraction**: Identify skill patterns from research papers
- **Skill Creation**: Transform patterns into reusable skills

## Activation Keywords

- kg research
- knowledge graph workflow
- paper analysis workflow
- 学术研究知识图谱
- KG研究流程
- 知识图谱研究
- automated literature review
- 研究自动化

## Tools Used

- `web_search`: Search arxiv and other sources for papers
- `exec`: Run Python scripts for KG operations
- `read`: Read paper abstracts and skill templates
- `write`: Create import scripts and skill files
- `sqlite3`: Direct database operations via exec

## Prerequisites

```bash
# Required files
- kg.db: SQLite knowledge graph database at /Users/hiyenwong/wiki/kg.db (symlink to workspace kg.db)
- kg_tool: Rust binary at scripts/kg_tool/target/release/kg_tool

# Weekly topics (for scheduled research)
- scripts/weekly_topics.py — outputs daily topic and keywords
```

## Actual Schema & Tool Reference

**See `references/operational-notes.md`** for the current database schema, kg_tool commands, arxiv access patterns, and operational details. This file is kept up-to-date with each session's findings.

## Usage Patterns

### Pattern 1: Full Research Pipeline

Complete automated workflow from search to skill creation:

```
执行 KG 研究流程：搜索 arxiv SNN 论文，导入知识图谱，生成嵌入，提取技能模式
```

### Pattern 2: Paper Import Only

Import papers to KG without full analysis:

```
导入这些论文到知识图谱：[paper list]
```

### Pattern 3: KG Analysis Only

Run algorithms on existing KG data:

```
分析知识图谱：运行 PageRank 和向量搜索，找相关论文
```

## Instructions for Agents

**First**: Read `references/operational-notes.md` for current DB schema, kg_tool commands, and access patterns.

### Step 1: Get Today's Topic

```bash
cd /Users/hiyenwong/.openclaw/workspace && python3 scripts/weekly_topics.py
```

Output gives weekday number, topic name, and keywords for targeted search.

### Step 2: Paper Acquisition

Search papers from multiple sources:

```python
# Use web_search for arxiv papers (direct arxiv API/browsing is blocked)
keywords = ["quantum computing", "machine learning", "distributed systems"]
for kw in keywords:
    papers = web_search(f"arxiv {kw} 2025", count=5)
```

**IMPORTANT (2026-05)**: `web_extract` blocks ALL arxiv URLs. Use `browser_navigate` + `browser_snapshot` to read paper abstracts from arxiv pages.

### Step 3: Import to KG

Two options:

**Option A — kg_tool**:
```bash
cd /Users/hiyenwong/.openclaw/workspace
scripts/kg_tool/target/release/kg_tool import-paper --title "Paper Title" --url "https://arxiv.org/abs/XXXX.XXXXX" --abstract "..." --authors "Name1, Name2"
```

**Option B — Direct SQL** (when more control needed):
```bash
sqlite3 kg.db "INSERT OR IGNORE INTO kg_entities (title, url, content, authors, published_date, category, source) VALUES ('Title', 'URL', 'abstract', 'Authors', 'date', 'category', 'arxiv');"
```

### Step 4: Generate Embeddings

```bash
scripts/kg_tool/target/release/kg_tool generate-embeddings
```

Generates embeddings for entities missing vectors. No parameters needed.

### Step 5: Run Graph Algorithms

```bash
# PageRank - find important papers
scripts/kg_tool/target/release/kg_tool pagerank --limit 15

# Vector search
scripts/kg_tool/target/release/kg_tool search --query "quantum machine learning" --limit 10

# Community detection (Louvain)
scripts/kg_tool/target/release/kg_tool communities --limit 10

# Stats
scripts/kg_tool/target/release/kg_tool stats
```

### Step 6: Add Relationships

```bash
sqlite3 kg.db "INSERT OR IGNORE INTO kg_relationships (source_id, target_id, relationship_type, weight) VALUES (source_id, target_id, 'related_to', 0.9);"
```

### Step 7: Pattern Analysis & Skill Creation

Analyze top papers from PageRank and vector search. Extract reusable patterns. Create skills using `skill_manage(action='create')` or write SKILL.md directly.

### Step 8: Record Results

Save summary to `memory/YYYY-MM-DD.md`.

## Database Schema

**See `references/operational-notes.md`** — the schema documented here was based on an older version and is no longer accurate. The operational notes file has the current schema verified from the running database.

## Example Papers to Import

Typical research paper structure:

```python
{
    "arxiv_id": "2603.27589",
    "title": "An Energy-Efficient Spiking Neural Network Architecture",
    "abstract": "Spiking Neural Networks offer energy-efficient alternative...",
    "category": "cs.NE",
    "keywords": ["spiking neural network", "energy-efficient", "SNN"]
}
```

## Error Handling

### Critical Operational Pitfalls
See [references/pitfalls.md](references/pitfalls.md) for confirmed issues: arxiv API 429 rate limiting, web_extract blocked on arxiv.org, kg_tool DB path, and import command details.

### Embedding Dimension Mismatch

```
If embeddings have different dimensions:
1. Check dimension with: SELECT dimension, COUNT(*) FROM kg_vectors GROUP BY dimension;
2. Regenerate all embeddings with consistent dimension
3. Use scripts/regenerate_embeddings.py
```

### Louvain Algorithm Failure

```
If Louvain/community detection fails:
1. kg_tool v2.0 uses Union-Find connected components (not true Louvain)
2. Check kg_relations weight column type — some rows store blob data, not REAL
   kg_tool now handles this by converting non-float weights to 1.0
3. Use communities command as fallback: kg_tool communities --limit 10
```

### Arxiv API Timeout

```
If arxiv API fails:
1. Use web_search instead of direct API
2. Search "arxiv [keyword] 2026"
3. Extract paper IDs from URLs
```

## Best Practices

1. **Batch Import**: Import multiple papers at once, not one-by-one
2. **Consistent Dimensions**: Always use same embedding dimension (256)
3. **Keyword Extraction**: Include 3-5 keywords per paper for better search
4. **Regular Stats**: Run kg_tool stats after each import batch
5. **Memory Update**: Always record results in memory/YYYY-MM-DD.md

## Resources

- **kg_tool**: `/Users/hiyenwong/.openclaw/workspace/scripts/kg_tool/target/release/kg_tool` (v2.0)
- **kg.db**: `/Users/hiyenwong/wiki/kg.db` ← CORRECT PATH (not ~/.openclaw/workspace/kg.db)
- **skill-extractor**: Use for pattern extraction
- **skill-creator**: Use for skill creation

## Related Skills

- **arxiv-search**: For detailed arxiv searching
- **skill-extractor**: Extract patterns from conversations
- **skill-creator**: Create new skills
- **memory-retrieval**: For storing research results

## Notes

- **Empty tables removed (2026-05-04):** `kg_hyperedges`, `kg_hyperedge_entities`, `kg_turboquant_cache` — all had 0 rows, cleaned up with VACUUM
- **Embeddings:** Hash-based (SHA-256 seeded PRNG), deterministic but not semantic. For production use sentence-transformers.
- **kg_tool v2.0:** Full rewrite (was placeholder). Implements real PageRank, Union-Find communities, FTS search, auto-embedding.