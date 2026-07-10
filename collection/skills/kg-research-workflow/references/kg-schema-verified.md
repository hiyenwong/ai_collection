# Verified Database Schema for kg.db

**Path**: `/Users/hiyenwong/.openclaw/workspace/kg.db`
**Verified**: 2026-05-14

## kg_entities

```sql
CREATE TABLE kg_entities (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    url TEXT UNIQUE NOT NULL,
    content TEXT,
    authors TEXT,
    published_date TEXT,
    category TEXT,
    source TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

- **No `name` column** — use `title`
- **No `entity_type` column** — infer from `source`/`category`

## kg_relations

```sql
CREATE TABLE kg_relations (
    source INT NOT NULL,
    target INT NOT NULL,
    type TEXT NOT NULL,
    weight REAL DEFAULT 1.0
);
```

- **No `id` column** — use `rowid` for existence checks
- **Column is `type`**, not `rel_type`
- No `properties` or `metadata` column

## kg_vectors

```sql
CREATE TABLE kg_vectors (
    entity_id INTEGER PRIMARY KEY,
    vector_data BLOB NOT NULL,
    created_at TIMESTAMP
);
```

- Vectors are 256-dim float32 binary (1024 bytes)
- Read/write with `struct.pack('256f', *vec)` / `struct.unpack('256f', data)`

## Keyword Entity Pattern

URL must be unique. Use `keyword://` prefix:
```python
kw_url = f"keyword://{kw.replace(' ', '-').lower()}"
cursor.execute("SELECT id FROM kg_entities WHERE url = ?", (kw_url,))
```

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `no such column: name` | Used `name` instead of `title` | Use `title` |
| `no such column: entity_type` | Column doesn't exist | Use `source`/`category` |
| `no such column: id` (kg_relations) | No `id` column | Use `rowid` |
| `UNIQUE constraint failed: kg_entities.url` | Empty/duplicate URL | Use unique `keyword://` URLs |

## kg_tool Available Commands

Only 3 commands exist:
- `kg_tool stats {db_path}` — DB statistics
- `kg_tool pagerank {db_path} {limit}` — PageRank ranking
- `kg_tool search --query "topic" --limit N` — vector similarity search

NOT available: `louvain`, `communities`, `list`, `--help`
