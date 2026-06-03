---
name: hourly-research-automation
description: "Automated hourly research task execution with weekly topic rotation and daily quantum mechanics learning. Cron-driven workflow - search arxiv, import to knowledge graph, generate embeddings, analyze with PageRank/Louvain, extract patterns, create skills. Activates on cron triggers or manual execution of weekly_topics.py."
---

# Hourly Research Automation

Automated research workflow for weekly topics with knowledge graph integration and skill extraction.

## Description

This skill orchestrates the entire hourly research process:
- **Weekly Topic Rotation**: Neuroscience (Mon), CS (Tue), Medicine (Wed), Systems (Thu), Math (Fri), Economics (Sat), Information (Sun)
- **Daily Quantum Mechanics**: Every execution includes quantum topics
- **Full Workflow**: arXiv search → KG import → embedding generation → graph analysis → skill creation

## Activation Keywords

- hourly research task
- weekly topics
- cron research
- 每小时研究任务
- 每周主题
- quantum mechanics daily
- research automation
- run weekly_topics.py

## Tools Used

- **exec**: Run Python scripts (weekly_topics.py, arxiv_search.py, import_papers_to_kg.py)
- **read**: Load skill templates, memory files, existing skills
- **write**: Create SKILL.md files, update memory
- **sqlite3**: Query kg.db for statistics and analysis
- **kg_tool**: Graph algorithms (PageRank, Louvain, similarity search)
- **cron**: Schedule hourly execution

## Instructions for Agents

### Step 1: Determine Today's Topic
Run `weekly_topics.py` to get the current day's research theme and quantum keywords.

### Step 2: Search ArXiv
Execute `arxiv_search.py` with topic-specific keywords plus quantum mechanics terms.

### Step 3: Import Papers
Run `import_papers_to_kg.py` to add papers to the knowledge graph with embeddings.

### Step 4: Analyze Graph
Use kg_tool commands (stats, pagerank, louvain) to analyze the knowledge graph structure.

### Step 5: Extract Patterns
Identify recurring research patterns from graph analysis results.

### Step 6: Create Skills
Use skill-extractor and skill-creator to generate new skills from discovered patterns.

### Step 7: Record Results
Update memory file with execution details, papers imported, and skills created.

## Examples

### Example 1: Monday Neuroscience Research

```
Cron triggers hourly research task:

Agent:
1. Run weekly_topics.py → "今日主题: 神经科学"
2. Search arxiv for "brain network, neural dynamics, quantum mechanics"
3. Import 5 papers to kg.db
4. Run pagerank → Entity 343 most influential
5. Run louvain → Identify 3 research clusters
6. Extract pattern: "spiking neural networks + brain connectivity"
7. Create skill: brain-connectivity-analysis
8. Update memory file with results
```

### Example 2: Manual Research Execution

```
User: "Run research task now for medicine topic"

Agent:
1. Override weekday → Medicine
2. Search arxiv for "medical imaging, drug discovery, quantum"
3. Import papers and generate embeddings
4. Analyze with PageRank and Louvain
5. Report top papers and research clusters
6. Suggest skill creation opportunities
```

## Research Workflow

### Step 1: Get Today's Topic

```bash
python3 scripts/weekly_topics.py
```

Output:
```
今日主题: [Weekday Topic]
每日必学: 量子力学 (Quantum Mechanics)
搜索关键词: [keyword list]
```

### Step 2: Search ArXiv

**Primary method:**
```bash
python3 scripts/arxiv_search.py
```

**Fallback (if arXiv API fails):**
- Use Semantic Scholar API
- Create sample data from memory
- Note: Handle rate limits with 3-second delays

### Step 3: Import to Knowledge Graph

```bash
python3 scripts/import_papers_to_kg.py
```

Imports papers to kg_entities, creates relations, generates embeddings.

### Step 4: Graph Analysis

```bash
# Statistics
kg_tool stats kg.db

# Importance ranking
kg_tool pagerank kg.db

# Community detection
kg_tool louvain kg.db

# Similarity search
python3 scripts/vector_similarity.py kg.db [entity_id] [k]
```

### Step 5: Pattern Extraction

Analyze research patterns from:
- Import papers: Entity IDs, keywords, similarity scores
- PageRank results: Most influential papers
- Louvain results: Research clusters
- Vector similarity: Related work

### Step 6: Skill Creation

Use skill-extractor → skill-creator workflow:
1. Identify recurring patterns
2. Extract skill elements
3. Generate SKILL.md
4. Test new skill
5. Package if needed

### Step 7: Record Results

Update memory file with:
- Execution time
- Papers imported
- Analysis results
- Skills created/updated
- Issues encountered

## Weekly Topics

| Day | Topic | Keywords |
|-----|-------|----------|
| Mon | Neuroscience | brain network, neural dynamics, EEG, fMRI, computational neuroscience |
| Tue | Computer Science | machine learning, algorithms, distributed systems, software engineering |
| Wed | Medicine | medical imaging, drug discovery, diagnostics, genomics, clinical AI |
| Thu | Systems Engineering | control systems, robotics, optimization, signal processing |
| Fri | Mathematics | number theory, statistics, optimization, numerical methods |
| Sat | Economics | finance, investment, market analysis, portfolio optimization |
| Sun | Information Science | data mining, NLP, knowledge graphs, information retrieval |

**Daily Requirement:** Always include quantum mechanics keywords.

## Cron Configuration

**Execution frequency:** Every hour

**Session type:** Isolated (fresh session each run)

## Database Schema

**kg_entities:**
- `id`: INTEGER PRIMARY KEY
- `entity_type`: TEXT (paper, method, keyword)
- `name`: TEXT
- `properties`: JSON (authors, abstract, keywords)
- `created_at`, `updated_at`: INTEGER

**kg_vectors:**
- `entity_id`: INTEGER PRIMARY KEY
- `vector`: BLOB (float32 array)
- `dimension`: INTEGER (384 for new, 256 for legacy)
- `created_at`: INTEGER

**kg_relations:**
- `source_id`, `target_id`: INTEGER
- `rel_type`: TEXT (related, cites, uses_method)
- `weight`: REAL
- `properties`: JSON

## Error Handling

### ArXiv Rate Limit (HTTP 429)
```
If 429 error:
  1. Wait 3 seconds
  2. Retry with smaller query
  3. If 3 failures: Use sample data
  4. Log in memory file
```

### Missing Dependencies
```
If sentence-transformers missing:
  pip install sentence-transformers

If kg_tool missing:
  cd scripts/kg_tool && cargo build --release
```

### Vector Dimension Mismatch
```
If dimensions differ:
  1. Filter by dimension in SQL
  2. Use scripts/vector_similarity.py
  3. Query: WHERE dimension = [target_dim]
```

## Example Workflow

### Wednesday Medicine Task

```
Cron triggers at 3:00 AM Wednesday:

1. weekly_topics.py → "今日主题: 医学"
2. arxiv_search.py → 5 papers on quantum + medical
3. import_papers_to_kg.py → Entity IDs: 4237379260-4237379264
4. pagerank → Entity 343 most influential
5. louvain → Community detection
6. vector_similarity.py → Find similar papers
7. Extract pattern → Create skill
8. Update memory file
```

## Related Skills

- **quantum-medical-research**: Wednesday topic specialization
- **skill-extractor**: Pattern extraction
- **skill-creator**: Skill creation workflow
- **arxiv-search**: ArXiv search skill
- **vector-embedding-manager**: Vector operations

## Notes

- Cron runs hourly, but actual work may take <5 minutes
- Use isolated sessions to avoid context pollution
- Always record in memory file for continuity
- Handle rate limits gracefully
- Vector embeddings enable semantic search
- Knowledge graph provides persistent memory