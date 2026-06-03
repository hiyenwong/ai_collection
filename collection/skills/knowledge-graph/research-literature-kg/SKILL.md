---
name: research-literature-kg
description: "Build and analyze knowledge graphs from research literature. Automated pipeline: arxiv search → entity extraction → KG construction → vector embeddings → semantic search → skill pattern extraction. Use when user asks to analyze papers, build research knowledge bases, find related work, or extract reusable patterns from academic literature."
---

# Research Literature Knowledge Graph

## Description

Automated pipeline for building and analyzing knowledge graphs from academic research literature. Integrates arxiv search, entity extraction, vector embeddings, and graph algorithms to discover patterns and extract reusable skill patterns.

## Activation Keywords

- research literature KG
- build knowledge graph from papers
- paper analysis pipeline
- arxiv to KG
- 文献知识图谱
- 科研论文分析
- 论文知识库
- extract skills from papers

## Tools Used

- `exec`: Run Python scripts, kg_tool CLI, arxiv API queries
- `web_search`: Search for related research
- `web_fetch`: Fetch paper content from arxiv
- `read`: Read existing skills, KG schema
- `write`: Store results, update memory
- `feishu_bitable_app`: Store structured paper metadata (optional)

## Workflow

### Phase 1: Literature Collection

1. **Define research scope**:
   - Primary topic (daily focus)
   - Secondary topic (weekly theme)
   - Keywords for search

2. **Search arxiv**:
   ```python
   query = f'cat:{category}+AND+all:{keywords}'
   url = f'http://export.arxiv.org/api/query?search_query={query}&max_results=10&sortBy=submittedDate&sortOrder=descending'
   ```

3. **Parse results**: Extract title, authors, abstract, arxiv_id, category, published_date

### Phase 2: KG Construction

1. **Initialize KG** (if needed):
   ```bash
   kg_tool init <db_path>
   ```

2. **Add entities**:
   ```bash
   kg_tool add-entity <db_path> paper <arxiv_id>
   ```

3. **Store metadata**: JSON properties with title, authors, abstract, category

### Phase 3: Vector Embeddings

1. **Generate embeddings**:
   - Model: `all-MiniLM-L6-v2` (384 dimensions)
   - Text: `{title}. {abstract}` (max 500 chars)

2. **Store vectors**:
   ```sql
   INSERT INTO kg_vectors (entity_id, vector, dimension, created_at)
   VALUES (?, ?, 384, ?)
   ```

### Phase 4: Graph Analysis

1. **PageRank**: Find important papers
   ```bash
   kg_tool pagerank <db_path>
   ```

2. **Louvain**: Detect research clusters
   ```bash
   kg_tool louvain <db_path>
   ```

3. **Semantic search**: Find related papers
   ```bash
   kg_tool search <db_path> <query>
   ```

### Phase 5: Pattern Extraction

1. **Identify patterns**: Look for recurring methods, frameworks, approaches
2. **Extract skills**: Use `skill-extractor` skill
3. **Create new skill**: Use `skill-creator` skill

## Output Format

```markdown
# Research Literature KG Report

**Date**: YYYY-MM-DD
**Topics**: Primary + Secondary

## Statistics
- Papers collected: N
- Entities in KG: M
- Vectors generated: K

## Top Papers (PageRank)
1. [ID] Title - score
2. ...

## Semantic Search Results
### Query: "quantum computing"
- Top matches with similarity scores

## Research Clusters (Louvain)
- Community 0: Topic A papers
- Community 1: Topic B papers

## Extracted Patterns
- Pattern 1: [Description]
- Pattern 2: [Description]

## New Skills Created
- skill-name: Description
```

## Database Schema

```sql
-- kg_entities
CREATE TABLE kg_entities (
    id INTEGER PRIMARY KEY,
    entity_type TEXT,  -- 'paper', 'author', 'keyword', 'topic'
    name TEXT,
    properties TEXT,   -- JSON: {title, authors, abstract, category}
    created_at INTEGER
);

-- kg_vectors
CREATE TABLE kg_vectors (
    entity_id INTEGER,
    vector BLOB,       -- float32 array
    dimension INTEGER, -- 384 for all-MiniLM-L6-v2
    created_at INTEGER
);

-- kg_relations
CREATE TABLE kg_relations (
    id INTEGER PRIMARY KEY,
    source_id INTEGER,
    target_id INTEGER,
    rel_type TEXT,     -- 'cites', 'related', 'same_author'
    weight REAL
);
```

## Error Handling

### arxiv API Timeout
- Retry after 5 seconds
- Use backup search via web_search

### Embedding Generation Failure
- Check sentence-transformers installed
- Fall back to simpler model if memory limited

### Dimension Mismatch
- Check vector dimensions match (384)
- Re-generate mismatched vectors

## Instructions for Agents

### Step 1: Define Research Scope
Identify primary topic, secondary topic, and search keywords from user request.

### Step 2: Collect Literature
Search arxiv API with category and keyword filters; parse title, authors, abstract, arxiv_id.

### Step 3: Build Knowledge Graph
Initialize kg.db if needed; add papers as entities; store JSON metadata.

### Step 4: Generate Embeddings and Analyze
Generate 384-dim embeddings via `all-MiniLM-L6-v2`; run PageRank and Louvain algorithms.

### Step 5: Extract Patterns and Report
Use skill-extractor to identify reusable patterns; output Research Literature KG Report.

## Examples

### Example 1: Build Brain Research KG

```
User: "Build a knowledge graph from recent brain connectivity papers"

Agent:
1. Search arxiv: cat:q-bio.NC AND all:brain connectivity, max 10 results
2. Add papers to kg.db with metadata
3. Generate vector embeddings
4. Run PageRank to find most influential papers
5. Run Louvain to detect research clusters
6. Output report with top papers and patterns
```

### Example 2: Semantic Search in Research

```
User: "Find quantum finance papers related to portfolio optimization"

Agent:
1. Initialize search query: "quantum portfolio optimization"
2. Fetch papers from arxiv quant-ph category
3. Add to kg.db and generate embeddings
4. Run similarity search for related papers
5. Report top matches with similarity scores
```

## Related Skills

- `arxiv-search`: Paper search details
- `skill-extractor`: Pattern extraction
- `skill-creator`: Skill creation
- `feishu-bitable`: Alternative storage

## Notes

- KG persists across sessions via SQLite
- Vectors enable semantic search
- Weekly topics rotate through domains
- Daily quantum mechanics focus