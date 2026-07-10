# Workspace kg.db Schema (scripts/kg.db) — Verified 2026-06-11

## Tables

### kg_entities
```sql
(id INTEGER PRIMARY KEY, name TEXT, type TEXT, description TEXT, metadata TEXT, created_at TIMESTAMP)
```
- `type`: 'paper', 'skill', etc.
- `metadata`: JSON blob with arxiv_id, title, authors, category, topic, skill_name, source_arxiv

### kg_relations
```sql
(id INTEGER PRIMARY KEY, source_id INTEGER, target_id INTEGER, relation_type TEXT, weight REAL, metadata TEXT, created_at TIMESTAMP)
```
- Links entities by integer ID (not TEXT IDs)

### kg_vectors
```sql
(id INTEGER PRIMARY KEY, entity_id INTEGER, embedding BLOB, text TEXT, created_at TIMESTAMP)
```
- `embedding`: BLOB — struct-packed float64 array via `struct.pack('128d', *vec)`
- `entity_id`: FK to kg_entities.id

### arxiv_papers
```sql
(id TEXT PRIMARY KEY, title TEXT, url TEXT, abstract TEXT, authors TEXT, published TEXT, created_at TIMESTAMP)
```
- `id`: arxiv ID as TEXT (e.g. '2606.09773', NOT prefixed with 'arxiv:')

## Import Pattern

```python
import sqlite3, json, struct

db = sqlite3.connect('scripts/kg.db')
c = db.cursor()

# 1. Insert paper to arxiv_papers
c.execute("INSERT INTO arxiv_papers (id, title, url, abstract, authors, published) VALUES (?, ?, ?, ?, ?, ?)",
    (arxiv_id, title, f"https://arxiv.org/abs/{arxiv_id}", abstract, authors, published))

# 2. Insert entity to kg_entities
c.execute("INSERT INTO kg_entities (name, type, description, metadata) VALUES (?, ?, ?, ?)",
    (arxiv_id, 'paper', description, json.dumps({'arxiv_id': arxiv_id, 'title': title, ...})))
entity_id = c.lastrowid

# 3. Insert embedding to kg_vectors (128-dim)
vec = [0.0] * 128  # your embedding
blob = struct.pack('128d', *vec)
c.execute("INSERT INTO kg_vectors (entity_id, embedding, text) VALUES (?, ?, ?)",
    (entity_id, blob, f"{title} {description}"))

db.commit()
```

## Web Search Fallback

Firecrawl web_search fails with `'NoneType' object has no attribute 'status_code'`. Use direct curl:

```bash
curl -s "https://export.arxiv.org/api/query?search_query=QUERY&max_results=10&sortBy=submittedDate"
# Parse XML: grep -E '<id>|<title>|<summary>|<published>|<link.*abs'
```

For complex OR queries, URL-encode carefully: `all:%22quantum+control%22+AND+all:systems`.
