# kg.db Actual Schemas (Verified 2026-06-10 — CORRECTED)

**ALWAYS run `PRAGMA table_info({table})` before inserting.** Schemas have drifted multiple times.

## Confirmed Tables (2026-06-10 PRAGMA Verified)

### arxiv_papers
```
id TEXT PRIMARY KEY
title TEXT
authors TEXT
published TEXT
categories TEXT
summary TEXT
pdf_url TEXT
abs_url TEXT
```
**Insert**: `INSERT INTO arxiv_papers (id, title, authors, published, categories, summary, pdf_url, abs_url) VALUES ('2604.10487', 'Title...', '', '2026-04-12', 'quant-ph', 'Abstract...', 'https://arxiv.org/pdf/2604.10487', 'https://arxiv.org/abs/2604.10487');`

### kg_entities (VERIFIED 2026-06-10 — CURRENT)
```
id INTEGER PRIMARY KEY AUTOINCREMENT
title TEXT NOT NULL
url TEXT UNIQUE NOT NULL
content TEXT
authors TEXT
published_date TEXT
category TEXT
source TEXT
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
```
**NOT**: `name/type/description/metadata` columns — those were incorrect documentation.
**Insert**: `INSERT INTO kg_entities (title, url, content, authors, published_date, category, source) VALUES ('Title', 'https://arxiv.org/abs/X', 'summary', '', '2026-06-10', 'quantum-medical', 'arxiv');`
**entity_id** returned by `lastrowid` for use in kg_vectors.

### kg_vectors (VERIFIED 2026-06-10 — CURRENT)
```
id INTEGER PRIMARY KEY AUTOINCREMENT
entity_id INTEGER
vector_data BLOB
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
```
**Column is `vector_data`** — NOT `embedding`.
**Insert**: `INSERT INTO kg_vectors (entity_id, vector_data) VALUES (?, ?)` where vector_data is bytes from `struct.pack()`.

### kg_relationships (present but not used heavily)

### Other Tables (legacy/auxiliary — avoid using)
- `entities` (simplified aux table, id TEXT PRIMARY KEY)
- `vectors` / `vectors_v2` (legacy)
- `relationships` (legacy)
- `pagerank` (entity_id TEXT, score REAL)
- `papers` (AUTOINCREMENT, arxiv_id TEXT, skill_name TEXT — used by papers table tracking)

## Drift History
- 2026-06-06: Documented `kg_vectors.vector_data` (correct) but also `kg_vectors.embedding` (wrong) in different places
- 2026-06-09: Documented `kg_entities(name, type, description, metadata)` — WRONG, actual is `(title, url, content, authors, published_date, category, source)`
- 2026-06-10: Confirmed kg_entities schema via PRAGMA — corrected in this file
- Root cause: multiple scripts created/modified tables; ALWAYS PRAGMA verify before INSERT
