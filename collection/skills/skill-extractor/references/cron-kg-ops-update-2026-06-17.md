# kg_tool Operational Status - 2026-06-17 Final Update

## kg_tool Binary Status (Confirmed 2026-06-17)

**Target database**: `/Users/hiyenwong/wiki/kg.db` (NOT workspace `scripts/kg.db`)

| Command | Status | Notes |
|---------|--------|-------|
| `stats` | ✅ Works | |
| `import-paper` | ✅ Works | Recovered 2026-06-17. Successfully imported 2606.16722. |
| `generate-embeddings` | ❌ Broken | `sqlite3.IntegrityError: datatype mismatch` on kg_vectors table. Error evolved from `no such column: e.source` (2026-06-09) → `datatype mismatch` (2026-06-16). Persists 2026-06-17. Tool's INSERT SQL targets `kg_vectors(id, vector_data)` but `id` is INTEGER AUTOINCREMENT and `vector_data` is BLOB, causing type mismatch. |
| `pagerank` | ✅ Works | Pre-computed pagerank table. Use JOIN: `SELECT e.id, e.title, p.score FROM kg_entities e JOIN pagerank p ON e.id = p.entity_id` |
| `communities` | ✅ Works | Returns community detection results. |
| `search` | ✅ Works | May return empty for narrow queries. |

## Workspace kg.db Verified Schemas (scripts/kg.db, 2026-06-17)

**kg_relations columns**: `(source INT, target INT, type TEXT, weight REAL)` — NOT `source_id`/`target_id`

**kg_vectors columns**: `(id INTEGER PK AUTOINCREMENT, entity_id INTEGER FK, vector_data BLOB, created_at TIMESTAMP)` — NOT `vector_data` named differently, but kg_tool generates SQL for `kg_vectors(id, vector_data)` which fails because `id` is AUTOINCREMENT

**pagerank table**: `(entity_id TEXT PK, score REAL)` — JOIN with kg_entities: `kg_entities.id = pagerank.entity_id`

**kg_documents**: Does NOT exist in workspace kg.db. Only `kg_entities` for paper storage.

## Domain Saturation Levels (Updated 2026-06-17)

| Domain | Saturation | Notes |
|--------|-----------|-------|
| Neuroscience+Quantum | ~90%+ | ALL arXiv papers covered by existing skills |
| CS+Quantum | ~85% | Most papers have dedicated skills |
| Medicine+Quantum | ~70% | Rapidly approaching saturation; 10 papers searched → all had skills |
| Economics+Quantum | ~75% | |
| Systems Engineering+Quantum | ~60% | |
| Information Science+Quantum | ~60% | |

**Pattern for saturated domains (>70%)**: Focus on enhancing existing skills with cross-references and new experimental results. Do NOT create new skills for papers already covered. Add "Cross-References" sections to umbrella skills linking complementary methodologies.

## Recommended Pattern for Cron Jobs

1. Use `kg_tool import-paper` for importing papers ✅
2. Use `kg_tool pagerank` and `kg_tool communities` for analysis ✅
3. Use `kg_tool search` for vector-based queries ✅
4. Skip `generate-embeddings` — confirmed broken across multiple sessions ❌
5. For saturated domains: grep for arXiv ID in existing skills before creating new ones
