# kg_tool Schema Reality Check (Updated 2026-05-27)

## Table Name Mismatch

The kg_tool source code declares tables `kg_entities`, `kg_relations`, `kg_vectors`.
The **actual** `/Users/hiyenwong/wiki/kg.db` uses: `entities`, `relationships`, `kg_vectors`.

**Fix pattern**: `sed -i '' 's/kg_entities/entities/g; s/kg_relations/relationships/g' kg_tool`

## Column Name Mismatch (kg_tool source vs actual entities table)

| kg_tool declares | Actual DB column | Fix applied |
|---|---|---|
| `e.title` | `e.name` | sed replace |
| `e.content` | `e.description` | sed replace |
| `e.authors` | `e.category` | sed replace |
| `e.published_date` | `e.created_date` | sed replace |
| `e.url` | `e.source` | sed replace |
| `source_id, target_id` | `source, target` | sed replace |
| `title` (SELECT) | `name` (SELECT) | sed replace |
| `kg_relations` | `relationships` | sed replace |

## Relationships Table Schema

```sql
CREATE TABLE relationships (
    id TEXT PRIMARY KEY,
    source TEXT,      -- NOT source_id
    target TEXT,      -- NOT target_id
    relation TEXT,    -- NOT weight
    description TEXT,
    created_date TEXT
);
```

## kg_vectors Table

- Column name: `embedding` (128-dim float32 as BLOB, 512 bytes)
- Verify with: `SELECT length(embedding) FROM kg_vectors LIMIT 1`

## Safe Operations (AFTER column fixes)
- `stats` ✓
- `pagerank` ✓ — works after fixing title→name and relations column names
- `communities` ✓ — works after fixing title→name
- `search` ✓ — works after fixing title→name, content→description
- `import-paper` ✓

## Fix Workflow (tested 2026-05-27)

```python
with open('kg_tool', 'r') as f:
    content = f.read()
content = content.replace('kg_entities', 'entities')
content = content.replace('kg_relations', 'relationships')
content = content.replace('e.title', 'e.name')
content = content.replace('e.content', 'e.description')
content = content.replace('e.authors', 'e.category')
content = content.replace('e.published_date', 'e.created_date')
content = content.replace('e.url', 'e.source')
content = content.replace('SELECT title FROM entities', 'SELECT name FROM entities')
content = content.replace('source_id, target_id, weight', 'source, target, relation')
with open('kg_tool', 'w') as f:
    f.write(content)
```

## Two Separate kg.db Instances

| Path | Schema | Tables | Used by |
|---|---|---|---|
| `/Users/hiyenwong/wiki/kg.db` (symlink) | `entities`, `relationships`, `kg_vectors`, `research_log` | 566 entities, 479 relations | `kg_tool` binary |
| `/Users/hiyenwong/.openclaw/workspace/kg.db` | `kg_entities` (title, url, content, ...) | Different | Legacy/direct SQL |

Always verify with `kg_tool stats` first — the binary path is hardcoded.
