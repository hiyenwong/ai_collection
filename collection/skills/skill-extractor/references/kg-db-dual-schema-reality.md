# Dual kg.db Schema Reality — 2026-06-01 Update

## Workspace Schema (confirmed via PRAGMA table_info)

**Path**: `/Users/hiyenwong/.openclaw/workspace/kg.db`

### entities table
| Column | Type |
|--------|------|
| id | TEXT (PK) |
| name | TEXT |
| type | TEXT |
| category | TEXT |
| description | TEXT |
| source | TEXT |
| created_date | TEXT |

**entities.id** is TEXT (e.g., 'arxiv_2605_29557').

### kg_vectors table
| Column | Type |
|--------|------|
| id | INTEGER (PK) |
| entity_id | INTEGER (FK → entities.rowid) |
| vector_data | BLOB |
| created_at | TIMESTAMP |

**CRITICAL**: `kg_vectors.entity_id` is INTEGER → `entities.rowid`, NOT `entities.id` (TEXT). Source of `datatype mismatch` errors.

### pagerank table
| Column | Type |
|--------|------|
| entity_id | INTEGER (FK → entities.rowid) |
| score | REAL |

### arxiv_papers table
| Column | Type |
|--------|------|
| id | TEXT (PK, arxiv ID like '2605.29557') |
| title, authors, published, categories, summary, pdf_url, abs_url | TEXT |

### kg_entities table (SEPARATE from entities)
| Column | Type |
|--------|------|
| id | INTEGER (PK) |
| title | TEXT |
| url | TEXT |
| content, authors, published_date, category, source | TEXT |
| created_at, updated_at | TIMESTAMP |

## Two Separate kg.db Files

1. **Workspace** (`/Users/hiyenwong/.openclaw/workspace/kg.db`): Used by cron jobs. Contains `entities` (TEXT id), `kg_vectors`, `arxiv_papers`, `pagerank`, `kg_entities`.
2. **Wiki** (`/Users/hiyenwong/wiki/kg.db`): Used by `kg_tool` binary. Different schema.

## Common Error: `sqlite3.IntegrityError: datatype mismatch`

**Cause**: Inserting TEXT entity_id into INTEGER `kg_vectors.entity_id` or `pagerank.entity_id`.

**Fix**: Use `cursor.lastrowid` after inserting into `entities`:
```python
cursor.execute('INSERT OR IGNORE INTO entities (id, name, type, category, description, source, created_date) VALUES (?, ?, ?, ?, ?, ?, ?)', (entity_id, title, 'research_paper', cat, summary[:200], 'arXiv', datetime.now()))
rowid = cursor.lastrowid
cursor.execute('INSERT OR IGNORE INTO kg_vectors (entity_id, vector_data, created_at) VALUES (?, ?, ?)', (rowid, vec_blob, datetime.now()))
```

## Correct Join Pattern
```python
cursor.execute('SELECT e.name, kv.vector_data FROM kg_vectors kv JOIN entities e ON e.rowid = kv.entity_id WHERE e.type=?', ('research_paper',))
```

## Arxiv API (Working Pattern)
```python
import urllib.request
req = urllib.request.Request(url)
req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)')
response = urllib.request.urlopen(req, timeout=60)
```

**Known issues**: `web_search` (Firecrawl) returns NoneType for arxiv. `web_extract` blocks arxiv.org URLs. HTTP 429 — use 3-4s delays.