# KG Schema Reference (2026-05-20)

## Tables

### entities
- `id` INTEGER PRIMARY KEY AUTOINCREMENT
- `name` TEXT NOT NULL  ← **Note: paper title stored here, not 'title'**
- `type` TEXT NOT NULL  ← Values: 'paper', 'concept', 'coding_principle', 'circuit_motif', 'metric', 'neuron_type', 'architecture', 'paper_id'
- `description` TEXT
- `metadata` TEXT
- `created_at` TEXT DEFAULT CURRENT_TIMESTAMP

### relationships
- `id` INTEGER PRIMARY KEY AUTOINCREMENT
- `source_id` INTEGER NOT NULL → entities.id
- `target_id` INTEGER NOT NULL → entities.id
- `relationship` TEXT NOT NULL  ← Values: 'uses', 'discusses', 'extends', etc.
- `metadata` TEXT
- `created_at` TEXT DEFAULT CURRENT_TIMESTAMP

### paper_concepts
- `paper_id` INTEGER
- `concept` TEXT

### kg_vectors
- `entity_id` INTEGER PRIMARY KEY → entities.id
- `vector` BLOB NOT NULL  ← 256-dim float32 via struct.pack('256f', ...)

## Notes
- `kg_tool` binary uses hardcoded path `/Users/hiyenwong/wiki/kg.db`
- Workspace copy at `/Users/hiyenwong/.hermes/hermes-agent/kg.db` must use `sqlite3` directly
- `kg_relations` and `kg_relationships` are DIFFERENT tables (former used by kg_tool, latter is the main one)
- Vector embeddings: deterministic hash-based generation works when no ML embedding model available
