# Two Knowledge Graph Databases

The project has **two separate** kg.db files. They are NOT the same database.

## Database 1: ~/wiki/kg.db (kg_tool's target)

**Path**: `/Users/hiyenwong/wiki/kg.db`
**Used by**: `scripts/kg_tool/target/release/kg_tool`
**Purpose**: Research paper knowledge graph with semantic embeddings

### Schema
```sql
kg_entities (id, entity_type TEXT, name TEXT, properties JSON, created_at, updated_at)
-- entity_type: "paper" | "concept" | "author" | etc.
-- properties: {"arxiv_id": "...", "url": "...", "authors": "..."}
```

### Verified kg_tool Commands (2026-05-05)
```
kg_tool import-paper  --title <t> --url <u> [--abstract <a>] [--authors <a>]
kg_tool generate-embeddings
kg_tool search        --query <q> [--limit <n>]
kg_tool pagerank      [--limit <n>]
kg_tool communities   [--limit <n>]
kg_tool stats                        # Entities, Relations, Vectors, Papers
```

### Observed Stats (2026-05-05)
- Entities: ~2218 | Relations: ~1875 | Vectors: ~2218 | Papers: ~192
- PageRank top: Quantum Algorithms (0.002247), quantum_physics_quantum (0.001704)
- Louvain communities: 309-entity SNN community, 189-entity quantum games community

## Database 2: workspace kg.db

**Path**: `/Users/hiyenwong/.openclaw/workspace/kg.db`
**Used by**: Python/SQLite scripts, arxiv fetch pipeline
**Purpose**: Alternative workspace-level knowledge graph

### Schema
```sql
kg_entities (id, title, url UNIQUE, content, authors, published_date, category, source)
kg_vectors  (id, entity_id FK, vector_data BLOB)
kg_relationships (id, source_id FK, target_id FK, relationship_type, weight)
```

**Use raw Python/SQLite for this one**, not kg_tool.

## Key Rule

If you want to use `kg_tool` CLI commands → operate on `~/wiki/kg.db`.
If you're writing Python scripts for the workspace pipeline → operate on `workspace/kg.db`.
Do NOT mix them.
