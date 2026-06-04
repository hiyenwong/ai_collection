# kg_vectors Schema Reality — 2026-05-31 Audit

## Schema (confirmed via PRAGMA table_info)

**kg.db** workspace database (`/Users/hiyenwong/.openclaw/workspace/kg.db`):

### kg_entities
| Column | Type | Nullable |
|--------|------|----------|
| id | INTEGER | PK |
| title | TEXT | NOT NULL |
| url | TEXT | NOT NULL |
| content | TEXT | YES |
| authors | TEXT | YES |
| published_date | TEXT | YES |
| category | TEXT | YES |
| source | TEXT | YES |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP |
| updated_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP |

### kg_vectors
| Column | Type | Nullable |
|--------|------|----------|
| id | INTEGER | PK |
| entity_id | INTEGER | YES (FK to kg_entities.id) |
| vector_data | BLOB | YES |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP |

**Note**: `kg_vectors.vector_data` is BLOB (not TEXT). Embeddings stored as `struct.pack('f' * dim, *values)`.

**CRITICAL BUG (2026-06-01)**: `kg_vectors.entity_id` is INTEGER (maps to `entities.rowid`), NOT `entities.id` (TEXT). Attempting to use TEXT arxiv IDs like 'arxiv_2605_29557' as entity_id causes `sqlite3.IntegrityError: datatype mismatch`. Same issue with `pagerank.entity_id`. Always use `cursor.lastrowid` after inserting into `entities` for foreign key references. See `references/kg-db-dual-schema-reality.md`.

### vectors
| Column | Type | Nullable |
|--------|------|----------|
| id | TEXT | PK |
| embedding | BLOB | YES |
| metadata | TEXT | YES |

### pagerank
| Column | Type | Notes |
|--------|------|-------|
| entity_id | INTEGER | FK to kg_entities.id |
| score | REAL | PageRank score |

## Dual Schema Confusion

There are TWO kg.db files:
- **Workspace**: `/Users/hiyenwong/.openclaw/workspace/kg.db` — schema above, used by cron jobs
- **Wiki**: `/Users/hiyenwong/wiki/kg.db` — different schema (`entities`, `relationships`), used by `kg_tool` binary

## Import Pattern

```python
# Insert entity
cursor.execute('''
    INSERT INTO kg_entities (title, url, content, category, published_date, source)
    VALUES (?, ?, ?, ?, ?, ?)
''', (title, url, content, category, date, 'arxiv_cron'))

entity_id = cursor.lastrowid

# Insert vector (BLOB via struct.pack)
import struct
embedding = [...]  # list of floats
emb_blob = struct.pack('f' * len(embedding), *embedding)
cursor.execute('''
    INSERT INTO kg_vectors (entity_id, vector_data) VALUES (?, ?)
''', (entity_id, emb_blob))
```

## Arxiv API Notes
- HTTP 429 rate limits common — use 3-4 second delays between queries
- `User-Agent: 'ResearchBot/1.0'` works; default Python UA sometimes blocked
- `web_search` (Firecrawl) returns NoneType errors for arxiv
- `web_extract` blocks arxiv.org URLs — use kg.db or arxiv API directly
