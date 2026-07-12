# kg_tool Binary Additional Bugs — Session 2026-06-09

## Additional Undiscovered Column Failures (2026-06-09)

Beyond bugs documented in `kg-tool-binary-bugs-2026-06-08.md`, these commands have additional schema mismatches:

### `search` command failure
```
SELECT e.id, e.name, e.description, e.type, e.category, e.source, e.created_date
FROM entities e WHERE e.name LIKE ? OR e.description LIKE ? OR e.type LIKE ?
→ FAIL: no such column: e.category
```
The `entities` view does NOT include `category` or `source`. View definition:
```sql
CREATE VIEW entities AS SELECT id, name, type, description FROM kg_entities;
```

### `generate-embeddings` (confirmed broken, same as before)
Queries `e.source` which doesn't exist in entities view.

### Full Bypass Recommendation
ALL kg_tool commands that read column names (`search`, `pagerank`, `generate-embeddings`, `communities`) are broken due to schema/view mismatches. Only `stats` and direct `import-paper` (if it works) are usable. For everything else, use direct sqlite3 on `/Users/hiyenwong/.openclaw/workspace/scripts/kg.db`.
