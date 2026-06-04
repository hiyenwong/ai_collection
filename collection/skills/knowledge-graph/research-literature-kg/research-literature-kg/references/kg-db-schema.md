# kg.db Schema Reference

Knowledge graph database at `/Users/hiyenwong/.openclaw/workspace/kg.db`.

## Tables

### kg_entities
| Column | Type | Notes |
|--------|------|-------|
| id | INTEGER PK | Auto-increment |
| title | TEXT NOT NULL | Paper/article title |
| url | TEXT NOT NULL | Absolute URL (arXiv abs URL) |
| content | TEXT | Abstract or summary |
| authors | TEXT | Comma-separated author names |
| published_date | TEXT | YYYY-MM-DD format |
| category | TEXT | Comma-separated categories |
| source | TEXT | `arxiv`, `arxiv-cron`, `anthropic`, `web_search`, etc. |
| created_at | TIMESTAMP | |
| updated_at | TIMESTAMP | |

**No `description` column** — use `content` for abstracts.

### kg_vectors
| Column | Type | Notes |
|--------|------|-------|
| id | INTEGER PK | |
| entity_id | INTEGER | FK to kg_entities.id |
| vector_data | BLOB | 1024 bytes = 256 float32 values |
| created_at | TIMESTAMP | |

Vector generation: `struct.pack('256f', *values)` — hash-based or embedding-based.

### kg_relationships / kg_relations
| Column | Type | Notes |
|--------|------|-------|
| source/source_id | INTEGER | FK to entity |
| target/target_id | INTEGER | FK to entity |
| type/relationship_type | TEXT | e.g. `related`, `cites`, `extends` |
| weight | REAL | Default 1.0 |

**Both tables exist** — `kg_relations` is the flat version, `kg_relationships` has its own PK.

**PITFALL (2026-05-23)**: `kg_relations` has historically accumulated corrupted entries where the `source`/`target` columns contain TEXT (paper titles) instead of INTEGER entity IDs. This causes `ValueError` when parsing for graph algorithms. **Always use `kg_relationships` for graph analysis** (PageRank, community detection) — it has proper `source_id`/`target_id` INTEGER columns. If you must query `kg_relations`, wrap ID parsing in try/except and skip non-integer rows.

### pagerank
| Column | Type | Notes |
|--------|------|-------|
| entity_id | INTEGER PK | FK to kg_entities.id |
| score | REAL | PageRank score |

**Only 2 columns** — no `computed_at` column. Insert only `(entity_id, score)` — do NOT pass timestamps.

**SQLite Pitfalls**

### Python tuple binding for single-parameter LIKE queries
When using sqlite3 with LIKE and a single parameter, the tuple MUST have a trailing comma:
```python
# WRONG — this is a string, not a tuple! Each char becomes a binding
cursor.execute("SELECT id FROM kg_entities WHERE url LIKE ?", (f'%{arxiv_id}%'))
# Error: ProgrammingError: Incorrect number of bindings supplied

# CORRECT — trailing comma makes it a tuple
cursor.execute("SELECT id FROM kg_entities WHERE url LIKE ?", ('%' + arxiv_id + '%',))
```
Or even simpler, avoid f-strings entirely:
```python
cursor.execute("SELECT id FROM kg_entities WHERE url LIKE ?", ('%' + arxiv_id + '%',))
```

**IMPORTANT**: `kg_relations` has historically accumulated corrupted entries where the `source`/`target` columns contain TEXT (paper titles) instead of INTEGER entity IDs. This causes `ValueError` when parsing. **Always use `kg_relationships` for graph analysis** (PageRank, community detection) — it has proper `source_id`/`target_id` INTEGER columns. If you must query `kg_relations`, wrap ID parsing in try/except.

### pagerank
| Column | Type | Notes |
|--------|------|-------|
| entity_id | INTEGER | FK to kg_entities.id |
| score | REAL | PageRank score |

**Only 2 columns** — no `computed_at` column. Insert only `(entity_id, score)`.

## Common Queries

```sql
-- Check if paper already exists
SELECT id FROM kg_entities WHERE url LIKE '%{arxiv_id}%';

-- Count by source
SELECT source, COUNT(*) FROM kg_entities GROUP BY source;

-- Insert new entity
INSERT INTO kg_entities (title, url, content, authors, published_date, category, source)
VALUES (?, ?, ?, ?, ?, ?, ?);

-- Insert vector
INSERT INTO kg_vectors (entity_id, vector_data) VALUES (?, ?);
```

## Common Sources
`arxiv` (973), `keyword` (54), `arxiv-cron` (53), `anthropic` (26), `generated` (6), `cron-job` (6)
