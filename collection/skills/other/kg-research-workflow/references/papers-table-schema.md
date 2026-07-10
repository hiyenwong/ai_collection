# Papers Table Schema (Neuroscience Research)

**Database**: `/Users/hiyenwong/.hermes/knowledge_graph/kg.db` (Verified 2026-06-03)

## Verified Schema (2026-06-03 Cron Session)

### papers Table

```sql
CREATE TABLE papers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    arxiv_id TEXT UNIQUE,              -- arxiv ID (e.g. '2602.18690')
    title TEXT NOT NULL,               -- paper title
    authors TEXT,                      -- comma-separated author list
    published TEXT,                    -- publication date (YYYY-MM-DD)
    categories TEXT,                   -- arxiv categories (comma-separated)
    abstract TEXT,                     -- paper abstract
    keywords TEXT,                     -- comma-separated keywords
    created_at TEXT                    -- ISO timestamp of import
);
```

### relations Table

```sql
CREATE TABLE relations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_id INTEGER,                 -- papers.id
    target_id INTEGER,                 -- papers.id (citation), or keyword_id
    relation_type TEXT,               -- 'cites', 'similar_to', 'has_keyword', etc.
    created_at TEXT
);
```

## Key Differences from Previous Documentation

**2026-06-03 Session Findings**:
- Actual DB path: `/Users/hiyenwong/.hermes/knowledge_graph/kg.db` (NOT `/Users/hiyenwong/.hermes/kg.db`)
- Uses `papers` + `relations` tables (NOT `entities` + `kg_vectors`)
- Schema simpler than documented — no embeddings table, no importance_score
- Works reliably for cron imports with Python parameterized INSERTs

## Usage

This table is specifically for neuroscience paper imports from automated research workflows. It's a simpler alternative to the `entities` table when you only need paper metadata without full KG relationships.

**Use cases**:
- Quick paper tracking
- Cron job imports
- Neuroscience research logs
- Paper skill association tracking

## INSERT Pattern

```python
import sqlite3

conn = sqlite3.connect("/Users/hiyenwong/.hermes/hermes-agent/kg.db")
c = conn.cursor()

# Insert paper after skill creation
c.execute("""
    INSERT INTO papers (id, title, authors, date, categories, abstract, skill_name, created_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, datetime('now'))
""", (
    "2605.29591", 
    "Mind-Omni: Unified Brain-Vision-Language Multi-Task Framework", 
    "Author1, Author2, Author3", 
    "2026-05-30", 
    "q-bio.NC, cs.NE", 
    "First framework unifying seven brain encoding/decoding tasks...", 
    "mind-omni-brain-vision-language-unified"
))

conn.commit()
```

## Query Pattern

```python
# Get all neuroscience papers
c.execute("SELECT id, title, skill_name FROM papers ORDER BY created_at DESC LIMIT 10")
papers = c.fetchall()

# Get paper by skill name
c.execute("SELECT * FROM papers WHERE skill_name = ?", ("mind-omni-brain-vision-language-unified",))
paper = c.fetchone()

# Check if paper exists before import
c.execute("SELECT id FROM papers WHERE id = ?", ("2605.29591",))
exists = c.fetchone() is not None
```

## Current Status (2026-06-01)

- **Total papers**: 34 records
- **Recent imports**: Mind-Omni (2605.29591), Brain-IT-VQA (2605.29588)
- **Location**: Hermes agent workspace database

## Key Differences from entities Table

| papers table | entities table |
|--------------|----------------|
| Simple paper metadata | Full KG with relationships |
| Comma-separated authors | Authors as separate entities |
| No vector embeddings | Vector embeddings in kg_vectors |
| No PageRank score | importance_score column |
| Direct skill association | Requires relationship linking |

## When to Use

**Use papers table when**:
- Quick paper logging in automated workflows
- Don't need author/keyword relationships
- Just tracking skill-paper association

**Use entities table when**:
- Full KG analysis with graph algorithms
- Need author relationships and citations
- Vector similarity search across all entities