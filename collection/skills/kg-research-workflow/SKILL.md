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
- kg.db: SQLite knowledge graph database
- kg_tool: Rust binary for KG operations (pagerank, louvain, search)

# Python dependencies (install if needed)
pip install numpy
```

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

### Step 1: Paper Acquisition

Search papers from multiple sources:

```python
# Use web_search for arxiv papers
keywords = ["neural network", "brain connectivity", "spiking neural network"]
for kw in keywords:
    papers = web_search(f"arxiv {kw} 2026", count=10)
```

**Important**: arxiv API requires proxy. Use web_search instead of direct curl to arxiv API.

### Step 2: Prepare Import Script

Create Python script to import papers:

```python
# scripts/import_papers.py template
PAPERS = [
    {
        "arxiv_id": "2603.xxxxx",
        "title": "...",
        "abstract": "...",
        "category": "cs.NE",
        "keywords": ["keyword1", "keyword2"]
    }
]

# Import to arxiv_papers table
# Import to kg_entities table (entity_type='paper')
# Create keyword entities (entity_type='keyword')
# Create HAS_KEYWORD relations
```

### Step 3: Import to KG

Execute import script:

```bash
python3 scripts/import_papers.py
```

### Step 4: Generate Embeddings

Create embeddings for KG entities:

```python
# scripts/generate_embeddings.py
# Use consistent dimension (256 recommended)
# Generate from: name + keywords
# Store in kg_vectors table
```

```bash
python3 scripts/generate_embeddings.py
```

### Step 5: Run Graph Algorithms

Use kg_tool for analysis:

```bash
# PageRank - find important papers
kg_tool pagerank kg.db

# Stats - check KG state
kg_tool stats kg.db

# List entities
kg_tool list kg.db
```

### Step 6: Vector Similarity Search

Create and run vector search:

```python
# scripts/vector_search.py
queries = ["spiking neural network", "brain connectivity"]
for q in queries:
    # Calculate cosine similarity
    # Return top_k results
```

```bash
python3 scripts/vector_search.py
```

### Step 7: Pattern Analysis

Analyze top papers from PageRank and vector search:

1. Read abstracts of high-PageRank papers
2. Identify common themes in vector search clusters
3. Extract reusable patterns (methods, workflows, architectures)

### Step 8: Skill Extraction

Use skill-extractor pattern:

1. Identify domain-specific patterns from papers
2. Document workflow steps
3. List activation keywords
4. Specify tools used

### Step 9: Skill Creation

Create SKILL.md following skill-creator guidelines:

```markdown
---
name: extracted-skill-name
description: "Clear description with activation triggers"
---

# [Skill Name]

[Concise instructions, examples, error handling]
```

### Step 10: Record Results

Update memory/YYYY-MM-DD.md:

```markdown
## KG Research Summary

**Papers Imported**: X new papers
**KG Stats**: X entities, X relations
**Top PageRank**: [list top papers]
**Vector Search Results**: [relevant clusters]
**Skills Extracted**: [skill names]
```

## Database Schema

### kg_entities
```sql
CREATE TABLE kg_entities (
    id INTEGER PRIMARY KEY,
    entity_type TEXT NOT NULL,  -- 'paper', 'keyword', 'author', etc.
    name TEXT NOT NULL,
    properties TEXT,  -- JSON with keywords, category, etc.
    created_at INTEGER,
    updated_at INTEGER
);
```

### kg_relations
```sql
CREATE TABLE kg_relations (
    id INTEGER PRIMARY KEY,
    source_id INTEGER NOT NULL,
    target_id INTEGER NOT NULL,
    rel_type TEXT NOT NULL,  -- 'HAS_KEYWORD', 'CITES', 'AUTHORED_BY'
    weight REAL DEFAULT 1.0,
    properties TEXT
);
```

### kg_vectors
```sql
CREATE TABLE kg_vectors (
    entity_id INTEGER PRIMARY KEY,
    vector BLOB NOT NULL,  -- numpy float32 array
    dimension INTEGER NOT NULL,
    created_at INTEGER
);
```

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

### Embedding Dimension Mismatch

```
If embeddings have different dimensions:
1. Check dimension with: SELECT dimension, COUNT(*) FROM kg_vectors GROUP BY dimension;
2. Regenerate all embeddings with consistent dimension
3. Use scripts/regenerate_embeddings.py
```

### Louvain Algorithm Failure

```
If Louvain fails:
1. Check kg_relations weight column type (should be REAL, not BLOB)
2. Use alternative: manual clustering via vector similarity
3. Group entities by keyword relations instead
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

- **kg_tool**: `/Users/hiyenwong/.openclaw/workspace/scripts/kg_tool/target/release/kg_tool`
- **kg.db**: `/Users/hiyenwong/.openclaw/workspace/kg.db`
- **skill-extractor**: Use for pattern extraction
- **skill-creator**: Use for skill creation

## Related Skills

- **arxiv-search**: For detailed arxiv searching
- **skill-extractor**: Extract patterns from conversations
- **skill-creator**: Create new skills
- **memory-retrieval**: For storing research results

## Notes

- This workflow is designed for automated hourly research
- Proxy required for arxiv API (use web_search as alternative)
- Embeddings are hash-based (upgrade to sentence-transformers for production)
- KG algorithms require Rust kg_tool binary
- Always test new skills after creation