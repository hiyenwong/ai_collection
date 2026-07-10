# Dual kg.db Schema Reality — Verified 2026-06-09

## Database A: Hermes-Internal (~/.hermes/kg.db)
- Tables: `entities(id TEXT, name, type, attributes TEXT, ...)` | `relationships(from_entity, to_entity, relationship_type, strength, created_at)` | `vectors(id TEXT, embedding BLOB, metadata TEXT)` | `skills(id INTEGER AUTOINCREMENT, name, description, category, paper_id, created_at, path)`
- Used by Hermes profile internally

## Database B: Cron Workspace (/Users/hiyenwong/.openclaw/workspace/scripts/kg.db)
- **Actual verified tables** (via PRAGMA 2026-06-09):

### arxiv_papers
```
id TEXT | title TEXT | url TEXT | abstract TEXT | authors TEXT | published TEXT | created_at TIMESTAMP
```

### kg_entities (NOT entities — that's a view)
```
id TEXT PRIMARY KEY | name TEXT | type TEXT | description TEXT | metadata TEXT | created_at TIMESTAMP
```

### kg_relations
```
source_id INT | target_id INT | relation_type TEXT | weight REAL | metadata TEXT
```

### kg_vectors
```
id INTEGER PK | entity_id INTEGER FK | vector_data BLOB | created_at TIMESTAMP
```
**CRITICAL**: Column is `vector_data` NOT `embedding`. Column `entity_id` is INTEGER NOT TEXT.

### pagerank
```
entity_id TEXT PRIMARY KEY | score REAL
```

### documents
```
id TEXT | content TEXT | metadata TEXT | created_at TIMESTAMP
```

### Views (created as workarounds for kg_tool compatibility):
```sql
CREATE VIEW entities AS SELECT id, name, type, description FROM kg_entities;
CREATE VIEW relationships AS SELECT id, source_id as source, target_id as target, relation_type as type, weight, metadata FROM kg_relations;
CREATE VIEW kg_relations_compat AS SELECT source_id as source, target_id as target, relation_type as type, weight, metadata FROM kg_relations;
```

**Note**: `/Users/hiyenwong/wiki/kg.db` is a symlink → `/Users/hiyenwong/.openclaw/workspace/scripts/kg.db`

## Working INSERT Pattern (2026-06-09)
```sql
INSERT OR IGNORE INTO arxiv_papers (id, title, url, abstract, authors, published) VALUES
('2606.08758', 'Paper Title', 'https://arxiv.org/abs/2606.08758', 'Abstract text', 'Authors', '2026-06-07');
```

## kg_tool Binary — FULLY BROKEN (2026-06-09)
ALL commands except `stats` fail:
- `search` → `no such column: e.category`
- `pagerank` → schema mismatch on relationships
- `generate-embeddings` → `no such column: e.source`
- `communities` → no relations found
- `import-paper` → "cannot modify entities because it is a view"

Use direct sqlite3 for ALL operations.
