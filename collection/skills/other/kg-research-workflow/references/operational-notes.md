# kg.db Operational Notes — Verified 2026-05-10

## Actual Table Schemas

### kg_entities (607 rows)
| Col | Type | Notes |
|-----|------|-------|
| id | INTEGER PK | Auto-increment |
| title | TEXT NOT NULL | Paper title |
| url | TEXT NOT NULL | arXiv abs URL |
| content | TEXT | Abstract text |
| authors | TEXT | JSON array of names |
| published_date | TEXT | YYYY-MM-DD |
| category | TEXT | Comma-separated arXiv cats |
| source | TEXT | 'arxiv', 'web', etc. |
| created_at | TIMESTAMP | |
| updated_at | TIMESTAMP | |

### kg_relationships (150,868 rows)
| Col | Type | Notes |
|-----|------|-------|
| id | INTEGER PK | |
| source_id | INTEGER | → kg_entities.id |
| target_id | INTEGER | → kg_entities.id |
| relationship_type | TEXT | e.g. 'related_to', 'HAS_KEYWORD' |
| weight | REAL DEFAULT 1.0 | |
| created_at | TIMESTAMP | |

### kg_relations (2,084 rows)
| Col | Type | Notes |
|-----|------|-------|
| source | INT | → kg_entities.id |
| target | INT | → kg_entities.id |
| type | TEXT | |
| weight | REAL | |

### kg_vectors (607 rows)
| Col | Type | Notes |
|-----|------|-------|
| id | INTEGER PK | Surrogate key |
| entity_id | INTEGER | → kg_entities.id |
| vector_data | BLOB | numpy float32 array, dim=256 |
| created_at | TIMESTAMP | |

**Note**: `kg_relationships` and `kg_relations` are separate tables. PageRank uses `kg_relationships`.

## Import Pattern (Python)

```python
import sqlite3, json
conn = sqlite3.connect('kg.db')
c = conn.cursor()
c.execute("""INSERT INTO kg_entities (title, url, content, authors, published_date, category, source)
    VALUES (?, ?, ?, ?, ?, ?, ?)""", (
    title, abs_url, abstract, json.dumps(authors), date, ','.join(cats), 'arxiv'))
entity_id = c.lastrowid
c.execute("INSERT INTO kg_vectors (entity_id, vector_data) VALUES (?, ?)", (entity_id, vec_bytes))
conn.commit()
```

## Embedding Dimension
- **256** (confirmed from existing data)
- SHA-256 seeded numpy PRNG

## kg_tool v2.0 Commands
`import-paper`, `generate-embeddings`, `search`, `pagerank`, `communities`, `stats`

**DB path**: `/Users/hiyenwong/wiki/kg.db`

## Security Scanner Notes
- arXiv API must use `https://` (HTTP triggers HIGH severity)
- `curl | python3` pipes trigger HIGH severity — download to temp file first