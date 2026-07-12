# kg.db Vector Embedding Dimension Mismatch

## Issue (Confirmed 2026-05-29)

Existing embeddings in `kg.db` have wildly inconsistent dimensions — now confirmed across **6 different sizes**:
- 22-dim (3 entries)
- 32-dim (73 entries)
- 60-dim (259 entries — most common)
- 128-dim (105 entries)
- 256-dim (94 entries)
- 384-dim (6 entries)
- Total: 540+ vectors with mixed dimensions

This causes `ValueError: shapes (256,) and (32,) not aligned` during vector similarity search.

## Root Cause

The `_text_to_embedding()` function generates embeddings with `dim=EMBEDDING_DIM` which defaults to 256. However, some existing embeddings were generated with `dim=32`. The column stores embeddings as JSON arrays (TEXT), not BLOBs, so dimension is not enforced.

## Detection

```python
import sqlite3, json
conn = sqlite3.connect('/Users/hiyenwong/.openclaw/workspace/scripts/kg.db')
c = conn.cursor()
c.execute("SELECT id, embedding FROM kg_vectors LIMIT 20")
for eid, emb_str in c.fetchall():
    emb = json.loads(emb_str)
    print(f"{eid}: dim={len(emb)}")
```

## Fix Options

1. **Regenerate all embeddings** to consistent dimension (256-dim):
   ```python
   c.execute("DELETE FROM kg_vectors")  # Clear all
   # Re-run embedding generation for all entities
   ```

2. **Standardize the embedding function** to always use `dim=128` as compromise, then regenerate.

3. **Store dimension with embedding** — add a `dimension` column to `kg_vectors`.

## Recommendation

**For cron jobs**: Before running vector similarity search, always verify embedding dimensions:
```python
dims = {}
for row in c.execute('SELECT id, embedding FROM kg_vectors'):
    try:
        dims[len(json.loads(row[1]))] = dims.get(len(json.loads(row[1])), 0) + 1
    except: pass
if len(dims) > 1:
    print(f"WARNING: {len(dims)} different dimensions: {dims}")
    # Skip vector search — fall back to text-based filtering
```

**Best practice**: Always generate new embeddings at a single target dimension (recommend 128 as compromise between quality and storage). Periodically audit kg.db dimensions to catch drift.
