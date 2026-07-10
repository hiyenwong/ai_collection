# kg_tool VIEW Fix — 2026-06-12

## Problem
`kg_tool generate-embeddings` failed with `no such column: e.source` because the `entities` VIEW in wiki/kg.db was missing columns that the tool's SQL queries reference.

## Root Cause
The `entities` VIEW was defined as:
```sql
CREATE VIEW entities AS SELECT id, name, type, description FROM kg_entities
```

But kg_tool's SQL queries reference: `id, name, description, type, source, created_date, category`

## Fix
Recreate the VIEW with all required columns:
```sql
DROP VIEW IF EXISTS entities;
CREATE VIEW entities AS SELECT id, name, type, description, source, created_date, metadata, created_at, metadata as category FROM kg_entities;
```

After this fix, `kg_tool generate-embeddings` succeeded (14 entities, 461 total vectors).

## Scope
- This fixes the VIEW-level column mismatch for `generate-embeddings`
- The `search` command had a similar issue (needed `category` column) — same VIEW fix resolves it
- The `import-paper` command still fails (tries to INSERT into a read-only VIEW — must use base table directly)
- The `pagerank` and `communities` commands depend on a `relations` VIEW with `(from_id, to_id, relation_type, weight)` — create similarly if needed

## Status (2026-06-12)
- `generate-embeddings`: ✅ Works after VIEW fix
- `search`: ✅ Should work after VIEW fix (not retested)
- `pagerank`: ⚠️ Needs `relations` VIEW fix
- `communities`: ⚠️ Needs `relations` VIEW fix
- `import-paper`: ❌ Still broken (INSERT into VIEW)
- `stats`: ✅ Always worked
