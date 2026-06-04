# kg.db Schema (Verified 2026-05-22)

Verified against running database at `/Users/hiyenwong/.openclaw/workspace/kg.db`

## Tables

### kg_entities
```sql
CREATE TABLE kg_entities (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    url TEXT NOT NULL UNIQUE,
    content TEXT,
    authors TEXT,
    published_date TEXT,
    category TEXT,
    source TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
- `url` has UNIQUE constraint → use INSERT OR REPLACE for upserts
- `id` is auto-increment INTEGER → do NOT pass string IDs

### kg_relations
```sql
CREATE TABLE kg_relations (
    source INT NOT NULL,
    target INT NOT NULL,
    type TEXT NOT NULL,
    weight REAL DEFAULT 1.0
);
```
- Column names: `source`, `target`, `type` — NOT `source_id`, `target_id`, `rel_type`
- No `id` or `properties` column

### kg_vectors
```sql
CREATE TABLE kg_vectors (
    entity_id INTEGER PRIMARY KEY,
    vector BLOB NOT NULL,
    dimension INTEGER NOT NULL,
    created_at INTEGER
);
```

### arxiv_papers
```sql
CREATE TABLE arxiv_papers (
    id TEXT PRIMARY KEY,
    title TEXT,
    authors TEXT,
    published TEXT,
    categories TEXT,
    summary TEXT,
    pdf_url TEXT,
    abs_url TEXT
);
```
- Note: `id` is TEXT here (arxiv ID like "2605.22770")
- Separate from kg_entities — import to BOTH

### pagerank
```sql
CREATE TABLE pagerank (
    entity_id INTEGER PRIMARY KEY,
    score REAL
);
```

## Insert Patterns

### Import to kg_entities (auto-increment id)
```python
c.execute("INSERT INTO kg_entities (title, url, content, authors, published_date, category, source) VALUES (?,?,?,?,?,?,?)",
    (title, url, content, authors, published_date, category, source))
entity_id = c.lastrowid
```

### Import to arxiv_papers (text id)
```python
c.execute("INSERT OR REPLACE INTO arxiv_papers (id, title, authors, published, categories, summary, pdf_url, abs_url) VALUES (?,?,?,?,?,?,?,?)",
    (arxiv_id, title, authors, published, categories, summary, pdf_url, abs_url))
```

### Import to pagerank
```python
c.execute("INSERT OR REPLACE INTO pagerank (entity_id, score) VALUES (?, ?)", (entity_id, score))
```

### Import to kg_relations
```python
c.execute("INSERT OR REPLACE INTO kg_relations (source, target, type, weight) VALUES (?,?,?,?)",
    (source_entity_id, target_entity_id, relation_type, weight))
```

## Verified Stats (2026-05-22)
- arxiv_papers: 74 entries
- kg_entities: 1600+ entries
- kg_relations: 3401 entries
- kg_vectors: 1427 entries
- pagerank: 1600+ entries
