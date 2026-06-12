# kg.db Corrected Schema — Verified 2026-06-08

**Database**: `~/.hermes/kg.db`

## Verified Tables and Columns

### entities
```
id TEXT PRIMARY KEY
name TEXT NOT NULL
type TEXT NOT NULL
attributes TEXT
created_at TEXT
last_accessed TEXT
importance_score REAL DEFAULT 0.5
category TEXT
description TEXT
source TEXT
created_date TEXT
```
Insert pattern:
```python
cursor.execute(
    """INSERT INTO entities (name, type, attributes, importance_score, category, description, source, created_date)
       VALUES (?, ?, ?, ?, ?, ?, ?, datetime('now'))""",
    (name, type, json.dumps(attributes), score, category, desc, source)
)
```

### vectors (WORKING vector table — NOT kg_vectors)
```
id TEXT PRIMARY KEY
embedding BLOB
metadata TEXT
```
Insert pattern:
```python
blob = struct.pack('f' * 128, *embedding_values)
cursor.execute("INSERT INTO vectors (id, embedding, metadata) VALUES (?, ?, ?)",
    (entity_id, blob, json.dumps({"type": "paper"})))
```

### kg_vectors (STALE — do NOT use)
```
id TEXT
embedding TEXT
```
This table exists but is not the working vector storage. Use `vectors` instead.

### relationships
```
id TEXT PRIMARY KEY
source_id TEXT NOT NULL
target_id TEXT NOT NULL
relation_type TEXT NOT NULL
strength REAL DEFAULT 0.5
created_at TEXT
```

### skills
```
id INTEGER PRIMARY KEY AUTOINCREMENT
name TEXT NOT NULL
description TEXT
category TEXT
paper_id INTEGER
created_at TEXT
path TEXT
```

### relations (ALTERNATIVE — also exists)
```
id INTEGER PRIMARY KEY AUTOINCREMENT
from_entity TEXT
to_entity TEXT
relationship_type TEXT
description TEXT
source TEXT
created_at TEXT DEFAULT CURRENT_TIMESTAMP
```

## Critical Notes
- Always `PRAGMA table_info(table)` before INSERT — schema has been corrected multiple times
- `vectors` NOT `kg_vectors` is the working table for embeddings
- `id` is TEXT in vectors, maps to entity name (e.g., arXiv ID)
- Embedding stored as BLOB via `struct.pack('f' * dim, *values)`
- `entities.id` is TEXT (usually arXiv ID or skill name)
