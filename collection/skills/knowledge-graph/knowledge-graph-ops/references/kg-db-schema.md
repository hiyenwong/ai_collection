# kg.db Schema — Reality vs kg_tool Expectation

## ⚠️ SCHEMA MISMATCH

`scripts/kg_tool/target/release/kg_tool` was written against a DIFFERENT schema than what exists in `kg.db` at `/Users/hiyenwong/.openclaw/workspace/kg.db`.

### Actual kg.db Schema

```sql
CREATE TABLE kg_entities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    url TEXT UNIQUE NOT NULL,
    content TEXT,
    authors TEXT,
    published_date TEXT,
    category TEXT,
    source TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE kg_vectors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_id INTEGER,
    vector_data BLOB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (entity_id) REFERENCES kg_entities (id)
);

CREATE TABLE kg_relationships (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_id INTEGER,
    target_id INTEGER,
    relationship_type TEXT,
    weight REAL DEFAULT 1.0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (source_id) REFERENCES kg_entities (id),
    FOREIGN KEY (target_id) REFERENCES kg_entities (id)
);
```

### kg_tool Expects

```sql
kg_entities (id, entity_type TEXT, name TEXT, properties TEXT, ...)
kg_relations (source_id, target_id, rel_type, weight, ...)     -- WRONG table name
kg_vectors (entity_id PK, vector BLOB, dimension INTEGER)      -- WRONG schema
arxiv_papers (arxiv_id UNIQUE, title, authors, abstract, ...)  -- extra table
```

### Differences

| Aspect | Actual | kg_tool expects |
|--------|--------|----------------|
| Entity cols | `title, url, content, authors, published_date, category, source` | `entity_type, name, properties (JSON)` |
| Relations | `kg_relationships` with `relationship_type` | `kg_relations` with `rel_type` |
| Vector PK | Auto-increment `id` | `entity_id` as PK |
| Vector dim | Mixed: 8 (ids 1-3), 128 (ids 4-32, 37+), 512 (ids 33-36) | 256 |
| Vector type | BLOB (some were TEXT, fixed 2026-05-04) | BLOB |

### Vector Generation (128-dim matching existing)

```python
import hashlib, struct, numpy as np

def generate_vector(text: str, dim: int = 128) -> bytes:
    seed_bytes = hashlib.sha256(text.encode('utf-8')).digest()[:4]
    seed = struct.unpack('>I', seed_bytes)[0]
    rng = np.random.RandomState(seed)
    vec = rng.randn(dim).astype(np.float32)
    vec /= np.linalg.norm(vec)
    return vec.tobytes()
```

### Vector Quality Note

Hash-based vectors are deterministic but NOT semantic. Cosine similarity: 0.05-0.18 range. Suitable for basic keyword matching only. For production, replace with sentence-transformers or OpenAI embeddings.
