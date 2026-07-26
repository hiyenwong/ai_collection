# kg_tool Binary Schema Bugs — Session 2026-06-08

## Pagerank Failure Chain

The `kg_tool` binary tries these fallback queries in order, ALL fail on current DB:

```
1. SELECT id FROM entities                    → OK (view exists)
2. SELECT source_id, target_id, rel_type, weight FROM relationships  → FAIL: no such table
3. SELECT source_id, target_id, rel_type, 1.0 as weight FROM relationships  → FAIL: no such table
4. SELECT source, target, type, weight FROM kg_relations  → FAIL: no such column "source"
5. SELECT source, target, type, 1.0 as weight FROM kg_relations  → FAIL: no such column "source"
```

**Actual table schema**: `kg_relations(source_id, target_id, relation_type, weight)` — none of the tool's queries match.

**Workaround**: Run pagerank/community detection manually via Python scripts written to `/tmp/` and executed via `terminal('python3 /tmp/script.py')`.

## generate-embeddings Failure

```
SELECT e.id, e.name, e.description, e.type, e.source, e.created_date FROM entities e
→ FAIL: no such column: e.source
```

**Actual table**: `kg_entities(id, name, type, description, metadata, created_at)` — no `source` or `created_date` columns.

**Workaround**: Generate embeddings manually via Python (keyword-frequency vectors packed as BLOB via `struct.pack('f' * dim, *vec)`).

## DB Location Reality

Three kg.db locations in use:
- `/Users/hiyenwong/.openclaw/workspace/scripts/kg_tool/kg.db` — kg_tool's hardcoded default
- `/Users/hiyenwong/.openclaw/workspace/scripts/kg.db` — workspace DB (cron workflow primary)
- `/Users/hiyenwong/wiki/kg.db` — symlink to workspace/scripts/kg.db

kg_tool uses `/Users/hiyenwong/wiki/kg.db` which symlinks to workspace. **Always copy between them** after direct inserts:
```bash
cp /Users/hiyenwong/.openclaw/workspace/scripts/kg_tool/kg.db /Users/hiyenwong/.openclaw/workspace/scripts/kg.db
```

## Views Created as Workarounds (2026-06-08)

```sql
CREATE VIEW IF NOT EXISTS entities AS SELECT id, name, type, description FROM kg_entities;
CREATE VIEW IF NOT EXISTS relationships AS SELECT id, source_id as source, target_id as target, relation_type as type, weight, metadata FROM kg_relations;
CREATE VIEW IF NOT EXISTS relationships_v2 AS SELECT source_id, target_id, relation_type, weight FROM kg_relations;
CREATE VIEW IF NOT EXISTS kg_relations_compat AS SELECT source_id as source, target_id as target, relation_type as type, weight, metadata FROM kg_relations;
CREATE VIEW IF NOT EXISTS documents AS SELECT * FROM kg_documents;
CREATE VIEW IF NOT EXISTS vectors AS SELECT * FROM kg_vectors;
```

Even with views, kg_tool's generate-embeddings still fails due to `e.source` column mismatch. Pagerank also fails because it queries `relationships` for `source_id, target_id, rel_type` (three different column name combos tried, none match).

## Recommendation

For cron workflows: bypass kg_tool binary entirely for pagerank, community detection, and embedding generation. Use direct sqlite3 or Python scripts for all kg.db operations. Only `search --query` (if it works) may be usable, but direct sqlite3 is more reliable.
