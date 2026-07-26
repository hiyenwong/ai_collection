# Workspace kg.db Schema — Verified 2026-06-11

**Path**: `/Users/hiyenwong/.openclaw/workspace/scripts/kg.db`

## Tables

### kg_entities
| Col | Type | PK |
|-----|------|----|
| id | INTEGER | Yes (autoincrement) |
| name | TEXT | No |
| type | TEXT | No |
| description | TEXT | No |
| metadata | TEXT | No |
| created_at | TIMESTAMP | No |

**CRITICAL**: `id` is INTEGER autoincrement. `name` is the human-readable name. `metadata` is a JSON string. **DO NOT** use columns like `title`, `url`, `published` — those are in `kg_documents`.

### kg_documents
| Col | Type | PK |
|-----|------|----|
| id | INTEGER | Yes (autoincrement) |
| arxiv_id | TEXT | Yes (unique) |
| title | TEXT | No |
| authors | TEXT | No |
| abstract | TEXT | No |
| categories | TEXT | No |
| pdf_url | TEXT | No |
| abs_url | TEXT | No |
| published | TEXT | No |
| created_at | TIMESTAMP | No |

### kg_relations
| Col | Type | PK |
|-----|------|----|
| id | INTEGER | Yes (autoincrement) |
| source_id | INTEGER FK | No |
| target_id | INTEGER FK | No |
| relation_type | TEXT | No |
| weight | REAL | No |
| metadata | TEXT | No |
| created_at | TIMESTAMP | No |

### kg_vectors
| Col | Type | PK |
|-----|------|----|
| id | INTEGER | Yes (autoincrement) |
| entity_id | INTEGER FK | No |
| embedding | BLOB | No |
| text | TEXT | No |
| created_at | TIMESTAMP | No |

**Inserting embeddings**: `struct.pack(f'{len(vec)}f', *vec)` → BLOB (float32, NOT float64). 128-dim vector = 512 bytes. Query: `struct.unpack('128f', row[0])` → list[float].

**Mixed format reality**: ~188 entries are binary BLOB (128-dim float32, 512 bytes). ~13 entries are JSON TEXT keyword dicts like `{"quantum":1,"error_correction":0,"network":1,...}` — older keyword-tag format from early sessions. When doing vector similarity search, handle both formats — parse JSON dicts as value arrays for cosine sim, unpack BLOB as float32 for binary entries.

### pagerank
| Col | Type | PK |
|-----|------|----|
| entity_id | INTEGER | Yes |
| score | REAL | No |

## Verified INSERT Patterns

### Paper Entity
```python
conn.execute(
    'INSERT INTO kg_entities (name, type, description, metadata, created_at) VALUES (?, ?, ?, ?, datetime("now"))',
    (arxiv_id, 'paper', title, json.dumps({'categories': cats, 'published': date, 'authors': authors}))
)
entity_id = conn.execute('SELECT last_insert_rowid()').fetchone()[0]
```

### Document
```python
conn.execute(
    'INSERT INTO kg_documents (arxiv_id, title, authors, abstract, categories, published, created_at) VALUES (?, ?, ?, ?, ?, ?, datetime("now"))',
    (arxiv_id, title, authors, abstract, categories, published)
)
```

### Relation
```python
conn.execute(
    'INSERT INTO kg_relations (source_id, target_id, relation_type, created_at) VALUES (?, ?, ?, datetime("now"))',
    (entity_id, target_id, 'relates_to')
)
```

### Embedding (float32 BLOB)
```python
import struct
emb_bytes = struct.pack(f'{len(vec)}f', *vec)
conn.execute(
    'INSERT INTO kg_vectors (entity_id, embedding, text, created_at) VALUES (?, ?, ?, datetime("now"))',
    (entity_id, emb_bytes, query_text)
)
```

## Dual DB Reality

**TWO kg.db files exist with COMPLETELY DIFFERENT schemas**:
- **`/Users/hiyenwong/.openclaw/workspace/scripts/kg.db`** — This file (verified schema above). Used by cron jobs.
- **`/Users/hiyenwong/.openclaw/workspace/kg.db`** — Different schema entirely (2215 entities). Different tables.
- **`~/.hermes/kg.db`** — Symlinks to `scripts/kg.db`
- **`/Users/hiyenwong/wiki/kg.db`** — Symlinks to `scripts/kg.db`, used by kg_tool binary

ALWAYS verify which kg.db you're operating on.
