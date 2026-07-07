# Workspace kg.db Schema — Verified 2026-06-06

## Location
`/Users/hiyenwong/.openclaw/workspace/kg.db` (50MB, 2052+ rows, 138527+ relations)

**This is the main workspace knowledge graph** — distinct from:
- `workspace/scripts/kg_tool/kg.db` (421KB, different schema — has `kg_documents`)
- `.hermes/knowledge_graph/kg.db` (JSON blob schema with papers/relations tables)
- `.hermes/kg.db` (JSON blob schema, prefixed IDs)

## kg_entities (INTEGER id, UNIQUE url)
```sql
CREATE TABLE kg_entities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- AUTO-INCREMENT INTEGER
    title TEXT NOT NULL,
    url TEXT NOT NULL UNIQUE,              -- UNIQUE constraint!
    content TEXT,
    authors TEXT,
    published_date TEXT,
    category TEXT,
    source TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**INSERT** — omit id, check url first:
```python
c.execute("SELECT id FROM kg_entities WHERE url=?", (url,))
existing = c.fetchone()
if existing:
    eid = existing[0]  # Use existing
else:
    c.execute("INSERT INTO kg_entities (title, url, content, authors, published_date, category, source) VALUES (?, ?, ?, ?, ?, ?, ?)",
             (title, url, content, authors, date, category, source))
    eid = c.lastrowid
```

## kg_vectors (entity_id INTEGER → kg_entities.id)
```sql
CREATE TABLE kg_vectors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_id INTEGER,    -- References kg_entities.id
    vector_data BLOB,     -- JSON array stored as BLOB
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**INSERT**: `c.execute("INSERT INTO kg_vectors (entity_id, vector_data) VALUES (?, ?)", (eid, json.dumps(vec)))`

## kg_relations (source/target as TEXT)
```sql
CREATE TABLE kg_relations (
    source TEXT, target TEXT, type TEXT, weight REAL
);
```

## pagerank (entity_id TEXT)
```sql
CREATE TABLE pagerank (
    entity_id TEXT, score REAL
);
```
**INSERT**: `c.execute("INSERT INTO pagerank (entity_id, score) VALUES (?, ?)", (str(eid), score))`

## arxiv_papers (id TEXT = arxiv ID)
```sql
CREATE TABLE arxiv_papers (
    id TEXT PRIMARY KEY, title TEXT, authors TEXT, published TEXT,
    categories TEXT, summary TEXT, pdf_url TEXT, abs_url TEXT
);
```

## Common Pitfalls
1. **UNIQUE url constraint** — always check `SELECT id FROM kg_entities WHERE url=?` before insert
2. **INTEGER id** — not TEXT arxiv IDs; use `c.lastrowid` after insert
3. **pagerank uses entity_id TEXT** — convert integer id to str: `str(eid)`
4. **kg_vectors entity_id is INTEGER** — matches kg_entities.id
