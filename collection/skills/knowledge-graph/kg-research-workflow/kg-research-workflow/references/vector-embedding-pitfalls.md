# Knowledge Graph Vector Embedding Pitfalls

## Vector Size Inconsistency

**Date observed:** 2026-05-21

The `kg_vectors.vector_data` column contains BLOBs of wildly varying sizes:

| Size (bytes) | Count | Notes |
|---|---|---|
| 64 | 10 | |
| 120 | 8 | |
| 128 | 4 | |
| 208 | 2 | |
| 400-442 | 4 | |
| 512 | 79 | |
| 1024 | 1198 | Most common (keyword-based embeddings) |
| 1200-1216 | 2 | |
| 1536 | 51 | Likely OpenAI/compatible embeddings |
| 1920 | 1 | |
| 2635 | 1 | |
| 4096 | 3 | |
| 6144 | 2 | Largest observed |

### Implications

1. **Cannot assume uniform vector dimension** — cosine similarity requires same-length vectors
2. **Must filter by size before computing similarity** — check `length(vector_data)` first
3. **New embeddings should declare their dimension** — store dimension as metadata or use consistent sizing

### Safe cosine similarity pattern

```python
import sqlite3, struct, math

# Check size first
cursor.execute("SELECT length(vector_data), COUNT(*) FROM kg_vectors GROUP BY length(vector_data)")

# Only compare vectors of the same size
target_size = 1024  # or whatever your query vector size is
cursor.execute("SELECT entity_id, vector_data FROM kg_vectors WHERE length(vector_data) = ?", (target_size,))

# Unpack safely
def unpack_vector(blob, dim):
    return struct.unpack(f'{dim}f', blob)

def cosine_sim(v1, v2):
    dot = sum(a*b for a,b in zip(v1,v2))
    n1 = math.sqrt(sum(a*a for a in v1))
    n2 = math.sqrt(sum(a*a for a in v2))
    return dot/(n1*n2) if n1>0 and n2>0 else 0
```

### Recommended: Normalize on creation

When creating new embeddings, always:
1. Decide on a fixed dimension (e.g., 512 or 1024)
2. Document the embedding method in the SKILL.md
3. Consider storing dimension as a separate column for future-proofing
