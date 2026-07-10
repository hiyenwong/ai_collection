# Cron KG Operations Update - 2026-06-16

## kg_tool generate-embeddings: NEW error mode
- **Previous error**: `no such column: e.source` (schema mismatch)
- **Current error**: `sqlite3.IntegrityError: datatype mismatch` on `kg_vectors` table
- **Root cause**: `kg_vectors` schema has `entity_id INTEGER FK` + `vector_data BLOB`. The tool's SQL attempts to insert `INSERT OR IGNORE INTO kg_vectors (id, vector_data)` — the `id` column is INTEGER AUTOINCREMENT but the tool may be passing TEXT, OR the `vector_data` BLOB is receiving incompatible data type
- **Schema verified**: `kg_vectors(id INTEGER AUTOINCREMENT, entity_id INTEGER, vector_data BLOB, created_at TIMESTAMP)`
- **Working alternative**: Direct sqlite3 for all kg.db operations

## Skill overlap detected
- `qml-mutation-testing` and `qml-model-testing` are significantly overlapping
- Both cover arxiv:2605.00107 (Mutation Testing of QML Models)
- `qml-model-testing` is the more comprehensive umbrella (includes mutation testing + accuracy/robustness + hardware readiness)
- `qml-mutation-testing` is a subset of `qml-model-testing`'s mutation testing section
- Needs curator consolidation

## New class-level skill created
- `quantum-continual-plasticity-preservation` (arxiv:2511.17228)
- Class-level: covers quantum continual learning and plasticity preservation patterns
- Genuinely new territory — no existing skill covered quantum plasticity in continual learning
