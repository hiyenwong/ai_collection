# Dual kg.db Reality — Verified 2026-06-09

## Two Separate Databases

### 1. `~/.hermes/kg.db` (Hermes internal)
Schema verified 2026-06-09 via cron job:

| Table | Key Columns |
|-------|-------------|
| `entities` | `id TEXT PK, name, type, attributes, ...` |
| `vectors` | `id TEXT PK, embedding BLOB, metadata TEXT` |
| `relationships` | `id INTEGER PK, from_entity TEXT, to_entity TEXT, relationship_type TEXT, description TEXT, source TEXT, created_at TEXT` |
| `skills` | `id INTEGER AUTOINCREMENT, name, description, category, paper_id INTEGER, created_at, path` |
| `pagerank` | `entity_id TEXT PK, score REAL` |

**Critical**: In `~/.hermes/kg.db`, the `relationships` table uses `from_entity` / `to_entity` / `relationship_type` — NOT `source_id`/`target_id`/`relation_type`.

### 2. `/Users/hiyenwong/.openclaw/workspace/kg.db` (workspace cron)
Different schema entirely:

| Table | Key Columns |
|-------|-------------|
| `kg_entities` | `id INTEGER AUTOINCREMENT, title, url UNIQUE, content, authors, published_date, category, source` |
| `kg_vectors` | `id INTEGER AUTOINCREMENT, entity_id INTEGER FK, vector_data BLOB, created_at` |
| `kg_relations` | `source INT, target INT, type TEXT, weight REAL` |
| `papers` | `id INTEGER AUTOINCREMENT, arxiv_id UNIQUE, title, authors, published_date, categories, abstract, skill_name, created_at` |
| `arxiv_papers` | `id TEXT PK, title, authors, published, categories, summary, pdf_url, abs_url` |
| `pagerank` | `id INTEGER PK, score REAL` (NOT `entity_id TEXT`) |

## Confusion History

The reference doc `references/cron-kg-schema-correction-2026-06-08.md` previously stated that `kg_relations` columns are `(source_id, target_id, relation_type)` for `~/.hermes/kg.db`. This was **incorrect** — the actual columns are `(from_entity, to_entity, relationship_type)`. The `source_id`/`target_id`/`relation_type` columns exist in a DIFFERENT table called `relations` (not `relationships`) that was seen in an older session or different database file.

## Corrected Insert Patterns for `~/.hermes/kg.db`

```python
# relationships table
c.execute('INSERT INTO relationships (from_entity, to_entity, relationship_type, description, source, created_at) VALUES (?, ?, ?, ?, ?, ?)',
    ('2606.05387', '2605.30866', 'related_methodology', 'Both about quantum data encoding', 'cron_job', '2026-06-09T...'))

# vectors table (embedding as BLOB)
import struct
vec = struct.pack('f' * 128, *embedding_values)
c.execute('INSERT INTO vectors (id, embedding, metadata) VALUES (?, ?, ?)',
    ('2606.05387', vec, json.dumps({'title': '...'})))

# entities table
c.execute('INSERT INTO entities (id, name, type, attributes) VALUES (?, ?, ?, ?)',
    ('2606.05387', 'Feature Encoding...', 'arxiv_paper', json.dumps({...})))
```

## Cron Workspace kg.db — Verified 2026-06-09

The cron job's actual kg.db is at `/Users/hiyenwong/.openclaw/workspace/scripts/kg_tool/kg.db` (NOT `/Users/hiyenwong/.openclaw/workspace/kg.db` as previously documented).

### Verified Schema (2026-06-09 via PRAGMA table_info)

| Table | Columns |
|-------|---------|
| `kg_documents` | `id INTEGER PK AUTOINCREMENT, arxiv_id TEXT UNIQUE, title, authors, abstract, categories, pdf_url, abs_url, published, created_at` |
| `kg_entities` | `id INTEGER PK AUTOINCREMENT, name TEXT, type TEXT, description TEXT, metadata TEXT, created_at` |
| `kg_relations` | `source INT, target INT, type TEXT, weight REAL` |
| `kg_vectors` | `id INTEGER PK AUTOINCREMENT, entity_id INTEGER FK, embedding BLOB, text TEXT, created_at` |
| `pagerank` | `entity_id TEXT PK, score REAL` |

**Critical differences from Hermes-internal kg.db:**
- `pagerank` uses `entity_id TEXT` (matches entity id as string), NOT `id INTEGER`
- `kg_vectors` uses `embedding` column (NOT `vector_data`)
- `kg_entities` has `name` column (NOT `title`)
- `kg_relations` has `source/target` (integers, FK to kg_entities.id)
- New table: `kg_documents` for paper-specific fields

### Insert Patterns for Workspace kg.db

```python
# kg_documents
cursor.execute("INSERT INTO kg_documents (arxiv_id, title, authors, abstract, categories, pdf_url, abs_url, published) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
    (arxiv_id, title, "", abstract, categories, pdf_url, abs_url, published))
doc_id = cursor.lastrowid

# kg_entities
cursor.execute("INSERT OR IGNORE INTO kg_entities (name, type, description, metadata) VALUES (?, ?, ?, ?)",
    (title, "paper", abstract[:200] + "...", json.dumps({"arxiv_id": arxiv_id, "doc_id": doc_id, "categories": categories})))

# kg_vectors (embedding as BLOB)
import struct
blob = struct.pack(f'{len(embedding)}f', *embedding)
cursor.execute("INSERT INTO kg_vectors (entity_id, embedding, text) VALUES (?, ?, ?)",
    (entity_id, blob, title[:100]))

# Pagerank query (entity_id is TEXT, join via CAST)
cursor.execute("SELECT e.name, p.score FROM pagerank p JOIN kg_entities e ON p.entity_id = CAST(e.id AS TEXT) ORDER BY p.score DESC LIMIT 5")
```

## CS + Quantum Domain Saturation (2026-06-09)

CS + Quantum coverage is now ~85%+. Today's scan of 5 recent arXiv papers (2606.06941, 2606.06316, 2606.06543, 2606.06531, 2606.03517) found zero genuinely new skills — all 5 had existing class-level skills covering the same methodology. 

**Guidance for future cron sessions**: When scanning CS + Quantum, expect >80% of papers to be already covered. Focus on:
1. Enhancing existing skills with new algorithm variants or references
2. Expanding to less saturated domains (e.g., quantum + control systems, quantum + formal methods, quantum + distributed systems)
3. Broadening search queries beyond `cs.AI + quantum` to `cs.SE`, `cs.PL`, `cs.DC`, `cs.CR` + quantum

## arXiv API URL Encoding Pattern (Corrected 2026-06-09)

**Pitfall**: Using `urllib.parse.quote(q, safe=':+&=')` with `+` operators in arXiv queries fails with HTTP 400.

**Working pattern** (verified 2026-06-09):
```python
params = urllib.parse.urlencode({
    "search_query": "cat:cs.AI AND all:quantum",
    "max_results": 5,
    "sortBy": "submittedDate",
    "sortOrder": "descending"
})
url = f"http://export.arxiv.org/api/query?{params}"
```

This properly encodes spaces as `+` and handles `:` correctly without manual quote manipulation.

## Rule

**ALWAYS** run `PRAGMA table_info(table_name)` before INSERT. The two databases have diverged and will continue to diverge. Never assume column names from a previous session's notes without verification.

## Cron Workspace kg.db — Verified 2026-06-09

The cron job's actual kg.db is at `/Users/hiyenwong/.openclaw/workspace/scripts/kg_tool/kg.db` (NOT `/Users/hiyenwong/.openclaw/workspace/kg.db` as previously documented).

### Verified Schema (2026-06-09 via PRAGMA table_info)

| Table | Columns |
|-------|---------|
| `kg_documents` | `id INTEGER PK AUTOINCREMENT, arxiv_id TEXT UNIQUE, title, authors, abstract, categories, pdf_url, abs_url, published, created_at` |
| `kg_entities` | `id INTEGER PK AUTOINCREMENT, name TEXT, type TEXT, description TEXT, metadata TEXT, created_at` |
| `kg_relations` | `source INT, target INT, type TEXT, weight REAL` |
| `kg_vectors` | `id INTEGER PK AUTOINCREMENT, entity_id INTEGER FK, embedding BLOB, text TEXT, created_at` |
| `pagerank` | `entity_id TEXT PK, score REAL` |

**Critical differences from Hermes-internal kg.db:**
- `pagerank` uses `entity_id TEXT` (matches entity id as string), NOT `id INTEGER`
- `kg_vectors` uses `embedding` column (NOT `vector_data`)
- `kg_entities` has `name` column (NOT `title`)
- `kg_relations` has `source/target` (integers, FK to kg_entities.id)
- New table: `kg_documents` for paper-specific fields

### Insert Patterns for Workspace kg.db

```python
# kg_documents
cursor.execute("INSERT INTO kg_documents (arxiv_id, title, authors, abstract, categories, pdf_url, abs_url, published) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
    (arxiv_id, title, "", abstract, categories, pdf_url, abs_url, published))
doc_id = cursor.lastrowid

# kg_entities
cursor.execute("INSERT OR IGNORE INTO kg_entities (name, type, description, metadata) VALUES (?, ?, ?, ?)",
    (title, "paper", abstract[:200] + "...", json.dumps({"arxiv_id": arxiv_id, "doc_id": doc_id, "categories": categories})))

# kg_vectors (embedding as BLOB)
import struct
blob = struct.pack(f'{len(embedding)}f', *embedding)
cursor.execute("INSERT INTO kg_vectors (entity_id, embedding, text) VALUES (?, ?, ?)",
    (entity_id, blob, title[:100]))

# Pagerank query (entity_id is TEXT, join via CAST)
cursor.execute("SELECT e.name, p.score FROM pagerank p JOIN kg_entities e ON p.entity_id = CAST(e.id AS TEXT) ORDER BY p.score DESC LIMIT 5")
```

## CS + Quantum Domain Saturation (2026-06-09)

CS + Quantum coverage is now ~85%+. Today's scan of 5 recent arXiv papers (2606.06941, 2606.06316, 2606.06543, 2606.06531, 2606.03517) found zero genuinely new skills — all 5 had existing class-level skills covering the same methodology. 

**Guidance for future cron sessions**: When scanning CS + Quantum, expect >80% of papers to be already covered. Focus on:
1. Enhancing existing skills with new algorithm variants or references
2. Expanding to less saturated domains (e.g., quantum + control systems, quantum + formal methods, quantum + distributed systems)
3. Broadening search queries beyond `cs.AI + quantum` to `cs.SE`, `cs.PL`, `cs.DC`, `cs.CR` + quantum

## arXiv API URL Encoding Pattern (Corrected 2026-06-09)

**Pitfall**: Using `urllib.parse.quote(q, safe=':+&=')` with `+` operators in arXiv queries fails with HTTP 400.

**Working pattern** (verified 2026-06-09):
```python
params = urllib.parse.urlencode({
    "search_query": "cat:cs.AI AND all:quantum",
    "max_results": 5,
    "sortBy": "submittedDate",
    "sortOrder": "descending"
})
url = f"http://export.arxiv.org/api/query?{params}"
```

This properly encodes spaces as `+` and handles `:` correctly without manual quote manipulation.
