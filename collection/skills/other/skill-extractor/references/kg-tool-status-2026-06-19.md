# kg_tool Operational Status — 2026-06-19

## Summary: ALL COMMANDS WORKING (2026-06-19 UPDATE)

Previous documentation (2026-06-08 through 2026-06-17) reported multiple kg_tool commands as broken. **All commands are now confirmed working as of 2026-06-19.**

## Verified Commands (2026-06-19)

| Command | Status | Notes |
|---------|--------|-------|
| `stats` | ✅ Working | Never broken |
| `import-paper` | ✅ Working | Successfully imported 4 papers |
| `generate-embeddings` | ✅ Working | Generated embeddings for 437 entities, 5781 total vectors |
| `pagerank` | ✅ Working | Returned top 10 entities by PageRank |
| `communities` | ✅ Working | Detected 10 communities |
| `search` | ✅ Working | Search by query string |

## Historical Error Log (RESOLVED)

The following errors were observed in previous sessions but are **no longer occurring**:

- **generate-embeddings** previously failed with `sqlite3.IntegrityError: datatype mismatch` on kg_vectors table — the tool's INSERT SQL targeted `kg_vectors(id, vector_data)` but `id` was INTEGER AUTOINCREMENT. **RESOLVED 2026-06-19**: embeddings generated successfully for 437 entities.
- **pagerank/communities/search** previously failed with `no such column: e.source` due to schema/view mismatches. **RESOLVED**: all commands return results.
- **generate-embeddings** previously failed with `no such column: e.source` (2026-06-09), then evolved to `datatype mismatch` (2026-06-16/17). **RESOLVED 2026-06-19**.

## Target Database

kg_tool operates on `/Users/hiyenwong/wiki/kg.db` (wiki kg.db), NOT the workspace kg.db at `scripts/kg.db` or `/Users/hiyenwong/.openclaw/workspace/kg.db`.

## DB Schema Note (wiki kg.db)

`kg_entities`: `(id, title, url, content, authors, published_date, category, source, created_at, updated_at)`
`kg_vectors`: `(id, entity_id, embedding, text, created_at)` — column is `embedding` with TEXT column
`kg_relations`: uses `source/target` column names

## arXiv API Status (2026-06-19)

- **Direct API (curl)**: ✅ Works with HTTPS
- **urllib.request during cron**: ❌ Connection refused (proxy not available in cron Python subprocess)
- **web_search (Firecrawl)**: ❌ Returns NoneType errors
- **web_extract**: ❌ Blocks arxiv.org URLs ("private/internal network")
- **Recommended pattern**: Use `terminal` with `curl` to arXiv API for cron jobs
