# kg.db Dual Schema Reference

Two separate kg.db files exist on this system with DIFFERENT schemas. Do not mix them up.

## Workspace kg.db
**Path**: `/Users/hiyenwong/.openclaw/workspace/kg.db`

Used by: `scripts/kg_tool/target/release/kg_tool` (workspace-local binary)

### kg_entities table
```
id INTEGER (PK), title TEXT, url TEXT, content TEXT, 
authors TEXT, published_date TEXT, category TEXT, 
source TEXT, created_at TIMESTAMP, updated_at TIMESTAMP
```

### kg_relations table
```
source TEXT, target TEXT, type TEXT, weight REAL
```

### Other tables
- `pagerank(entity_id INTEGER, score REAL)`
- `arxiv_papers(id TEXT, title TEXT, authors TEXT, published TEXT, categories TEXT, summary TEXT, pdf_url TEXT, abs_url TEXT)`
- `kg_vectors(id INTEGER, entity_id INTEGER, vector_data BLOB, created_at TIMESTAMP)` — `vector_data` is BLOB (raw float32 bytes, NOT TEXT comma-separated floats). `id` is INTEGER (PK), `entity_id` is INTEGER (FK to kg_entities.id). Insert with `INSERT INTO kg_vectors (id, entity_id, vector_data) VALUES (?, ?, ?)` where vector_data = `numpy.array(...).astype(np.float32).tobytes()`.
- `sqlite_sequence`

## Wiki kg.db
**Path**: `/Users/hiyenwong/wiki/kg.db`

Used by: Hermes skill system, some external scripts

### entities table
```
id TEXT (arXiv ID), name TEXT (title), type TEXT, 
category TEXT, description TEXT (abstract), source TEXT, created_date TEXT
```

### relationships table
```
source_id TEXT, target_id TEXT, relation TEXT, weight REAL
```

## Key Differences
| Aspect | Workspace kg.db | Wiki kg.db |
|--------|----------------|------------|
| Entity ID | INTEGER | TEXT (arXiv ID) |
| Title column | `title` | `name` |
| Content column | `content` | `description` |
| Entity table name | `kg_entities` | `entities` |
| Relation table name | `kg_relations` | `relationships` |
| Relation columns | `source, target` | `source_id, target_id` |
| Relation type column | `type` | `relation` |

## Usage
- For arXiv paper lookup by ID: use wiki/kg.db `entities` table
- For workspace skill tool operations: use workspace kg.db `kg_entities` table
- For PageRank on workspace DB: `pagerank` table with `entity_id` (INTEGER)
- For PageRank on wiki DB: query via `kg_tool pagerank` command
