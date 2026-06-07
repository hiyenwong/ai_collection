# kg.db State Report (2026-05-27) — Updated 13:00 hourly run

## Workspace kg.db (/Users/hiyenwong/.openclaw/workspace/kg.db)
- **kg_entities**: 1,821 rows (as of 13:00 hourly run)
- **Schema**: id, title, url, content, authors, published_date, category, source, created_at, updated_at
- **arxiv_papers**: 169 rows
- **kg_vectors**: 1,632 rows (embedding generation has known AttributeError bug — `'bytes' object has no attribute 'tolist'` in kg_tool source)
- **pagerank**: 1,588 rows
- **kg_relations**: exists (source, target, type, weight)
- **kg_relationships**: 706,521 rows (note: both `kg_relations` and `kg_relationships` exist)

## Wiki kg.db (/Users/hiyenwong/wiki/kg.db → symlink → /Users/hiyenwong/.openclaw/workspace/scripts/kg.db)
- **entities**: different schema (id, name, type, category, description, source, created_date)
- Used by kg_tool binary
- **kg_tool import-paper bug**: tries to query `kg_entities` table but wiki kg.db only has `entities` — import always fails

## Confirmed Import Workaround
Import into BOTH databases manually via sqlite3:
```python
# Workspace kg.db
cursor.execute("INSERT INTO kg_entities (title, url, content, authors, published_date, category, source, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", ...)
cursor.execute("INSERT INTO arxiv_papers (id, title, authors, published, categories, summary, pdf_url, abs_url) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", ...)

# Wiki kg.db
cursor.execute("INSERT INTO entities (id, name, type, category, description, source, created_date) VALUES (?, ?, ?, ?, ?, ?, ?)", ...)
```

## arxiv API Confirmed Failure Modes (2026-05-27)
- HTTP 429 "Rate exceeded." on export.arxiv.org
- Connection timeout after 30s even through proxy
- ALL clients affected: curl, httpx, urllib.request
- Do NOT retry in a loop — switch fallback immediately
- PREFERRED: Query kg.db first, then curl single-shot, then web_search

## kg_tool Bug Notes (2026-05-27)
- `generate-embeddings`: crashes with `AttributeError: 'bytes' object has no attribute 'tolist'` — the tool reads blob data but calls `.tolist()` on bytes instead of unpacking first
- `search --query`: returns empty results (embeddings not properly generated)
- `pagerank`: works correctly
- `communities`: works correctly
- `stats`: works correctly
- **Fix needed**: In generate_embeddings(), convert BLOB bytes to float array using `struct.unpack('<128f', blob)` before calling `.tolist()`
