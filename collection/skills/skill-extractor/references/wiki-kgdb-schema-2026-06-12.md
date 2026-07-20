# Wiki kg.db Schema — Verified 2026-06-12 (CORRECTION)

**Path**: `/Users/hiyenwong/wiki/kg.db`

**CRITICAL**: This file has a DIFFERENT schema from both `scripts/kg.db` AND the previously documented schema in `workspace-kgdb-schema-2026-06-11.md`. The old reference file listed columns `(name, type, description, metadata)` for `kg_entities` — those are WRONG for this file.

## Verified Tables (via PRAGMA table_info)

### kg_entities
| Col | Type | PK |
|-----|------|----|
| id | INTEGER | Yes (autoincrement) |
| title | TEXT | No |
| url | TEXT | No (unique) |
| content | TEXT | No |
| authors | TEXT | No |
| published_date | TEXT | No |
| category | TEXT | No |
| source | TEXT | No |
| created_at | TIMESTAMP | No |
| updated_at | TIMESTAMP | No |

**IMPORTANT**: There is a `kg_entities` VIEW that exposes different column names (`name`, `type`, `description`) — this view is read-only and cannot be INSERTed into. All INSERTs must target the base table with correct column names: `title`, `content`, `category`, `authors`, etc.

### kg_documents
| Col | Type | PK |
|-----|------|----|
| id | INTEGER | Yes (autoincrement) |
| arxiv_id | TEXT | No |
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
| weight | REAL | No (default 1.0) |
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

**Column is `embedding` (NOT `vector_data`), and there IS a `text` column.** This differs from previously documented schemas for other kg.db files.

## Verified INSERT Patterns

### Entity (concept/method/researcher)
```python
conn.execute(
    'INSERT INTO kg_entities (title, url, content, category) VALUES (?, ?, ?, ?)',
    (name, url, description, category)
)
```

### Document (paper)
```python
conn.execute(
    'INSERT INTO kg_documents (arxiv_id, title, authors, abstract, categories, pdf_url, abs_url, published) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
    (arxiv_id, title, authors, abstract, categories, pdf_url, abs_url, published)
)
```

### Relation
```python
conn.execute(
    'INSERT INTO kg_relations (source_id, target_id, relation_type, weight) VALUES (?, ?, ?, ?)',
    (source_entity_id, target_entity_id, 'relates_to', 1.0)
)
```

### Embedding
```python
import struct
emb_bytes = struct.pack(f'{384}f', *embedding_vector)
conn.execute(
    'INSERT INTO kg_vectors (entity_id, embedding, text) VALUES (?, ?, ?)',
    (entity_id, emb_bytes, text)
)
```

## kg_tool Binary Status (2026-06-12 reconfirmed)

- `stats`: ✅ Works
- `import-paper`: ❌ Fails — tries to INSERT into `kg_entities` view which is read-only
- `generate-embeddings`: ❌ Fails — SQL references columns (`source`, `created_date`) not in the entities view
- `search`, `pagerank`, `communities`: ❌ All fail due to schema/view mismatches
- **Workaround**: Use direct sqlite3/python for all data operations. Only `stats` is usable.

## Three-Way kg.db Reality (2026-06-12 CORRECTED)

| File | Purpose | Schema |
|------|---------|--------|
| `scripts/kg.db` | Cron workspace | Different schema — see `workspace-kgdb-schema-2026-06-11.md` |
| `~/.hermes/kg.db` | Hermes internal | Symlinks to `scripts/kg.db` |
| `wiki/kg.db` | Wiki/kg_tool | **Different schema** — this file. `kg_entities` has `title/content/category` NOT `name/type/description` |
| `workspace/kg.db` | Old workspace | Yet another schema — 2215 entities, different tables entirely |

**ALWAYS verify with `PRAGMA table_info(table_name)` before operating on any kg.db file.**
