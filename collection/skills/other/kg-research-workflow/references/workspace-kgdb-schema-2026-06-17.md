# Workspace kg.db Corrected Schema Notes — 2026-06-17

## Critical FK Corrections (not in 2026-06-15 schema doc)

### kg_vectors.entity_id FK Target
- **`kg_vectors.entity_id` references `kg_documents.id`** (INTEGER), NOT `kg_entities.id`
- This means you MUST insert into BOTH tables for full paper registration:
  1. `kg_documents` first → get `doc_id` (for vector linkage)
  2. `kg_entities` → get `entity_id` (for graph relations)
  3. `kg_vectors(entity_id=doc_id, ...)` → vectors link to documents, not entities
  4. `kg_relations(source_id=entity_id, target_id=kw_entity_id, ...)` → relations use entity IDs

### kg_relations Column Names
- Actual columns: `source_id INTEGER`, `target_id INTEGER` (FKs to kg_entities.id)
- NOT `source`/`target` TEXT columns (some older docs are wrong)
- Always `PRAGMA table_info(kg_relations)` before inserting

### Complete Insert Order
```python
# 1. Paper metadata (for vector linkage)
cur.execute("INSERT INTO kg_documents (arxiv_id, title, ...) VALUES (...)")
doc_id = cur.lastrowid

# 2. Entity (for graph relations)  
cur.execute("INSERT INTO kg_entities (name, type, description, ...) VALUES (...)")
entity_id = cur.lastrowid

# 3. Vector (links to DOCUMENT id)
cur.execute("INSERT INTO kg_vectors (entity_id, embedding, text) VALUES (?, ?, ?)", (doc_id, packed, text))

# 4. Relations (link ENTITY ids)
cur.execute("INSERT INTO kg_relations (source_id, target_id, relation_type, ...) VALUES (?, ?, ?, ...)", (entity_id, kw_entity_id, "HAS_KEYWORD", ...))

# 5. Edge sync (for community detection)
cur.execute("INSERT OR IGNORE INTO kg_edges (source, target, relation, weight) VALUES (?, ?, ?, ?)", (arxiv_id, keyword, "HAS_KEYWORD", 1.0))
```

## Domain Saturation Levels (2026-06-17)
- Medicine+Quantum: ~90%
- Neuroscience+Quantum: ~95%
- CS+Quantum: ~85%
- Economics+Quantum: ~75%
- Information Science+Quantum: ~60%
- Systems Engineering+Quantum: ~60%

Rule: >80% duplicate hits → enhance existing skills, don't create new ones.
