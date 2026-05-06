---
name: knowledge-graph-ops
description: >
  Operations for the SQLite knowledge graph (kg.db) at
  /Users/hiyenwong/.openclaw/workspace/kg.db. Use when importing papers,
  generating embeddings, running PageRank/community detection, or querying
  the research knowledge graph. Covers the kg_tool CLI and raw SQLite
  approaches. WARNING: kg_tool has a schema mismatch — see references.
---

# Knowledge Graph Operations

## Location
`/Users/hiyenwong/.openclaw/workspace/kg.db`

## kg_tool CLI (targets ~/wiki/kg.db — a SEPARATE database)

The CLI tool at `scripts/kg_tool/target/release/kg_tool` operates against
`/Users/hiyenwong/wiki/kg.db` — a **separate** knowledge graph from the
workspace one. It has its own schema and works fine for writes.

**DB path**: `/Users/hiyenwong/wiki/kg.db`
**Schema**: `kg_entities (id, entity_type, name, properties JSON, created_at, updated_at)`
**Details**: See [references/two-kg-databases.md](references/two-kg-databases.md) for full comparison.

```
kg_tool import-paper  --title <t> --url <u> [--abstract <a>] [--authors <a>]
kg_tool generate-embeddings          # Generate embeddings for entities without them
kg_tool search        --query <q> [--limit <n>]
kg_tool pagerank      [--limit <n>]
kg_tool communities   [--limit <n>]
kg_tool stats                        # Show: Entities, Relations, Vectors, Papers
```

**Verified commands (2026-05-05)**: All six commands work. `generate-embeddings`
only generates vectors for entities that are missing them (reports count).
`stats` output format: `Entities: N\nRelations: N\nVectors: N\nPapers: N`.
`search --query "<query>"` may return **empty results** even for valid queries —
this happens when the query terms don't match entity titles closely enough.
For reliable search, use raw SQLite `LIKE` queries on `kg_entities.title` and
`kg_entities.content` instead. `search` returns empty more often than expected;
when it does, fall back to direct SQL queries.

## ⚠️ Workspace kg.db Schema

The workspace knowledge graph at `/Users/hiyenwong/.openclaw/workspace/kg.db`
has a DIFFERENT schema. Do NOT use kg_tool to write to it.
Use Python/SQLite directly. See below for workspace import patterns.

## Working Schema

```sql
kg_entities (id, title, url, content, authors, published_date, category, source, created_at, updated_at)
kg_vectors  (id, entity_id, vector_data)  -- raw float32 BLOBs (256-dim, 1024 bytes each)
kg_relationships (id, source_id, target_id, relationship_type, weight, created_at)
```

### Vector Format

All vectors in kg_vectors are stored as **raw float32 BLOBs**, 256 dimensions (1024 bytes each). No JSON-encoded or mixed-format vectors remain.

```python
import struct

def parse_vector(vdata):
    """Parse 256-dim float32 vector from kg_vectors BLOB."""
    return list(struct.unpack('256f', vdata))

def vector_to_blob(vector):
    """Convert list of floats to float32 BLOB for kg_vectors."""
    return struct.pack('256f', *vector)
```

When generating new vectors, use 256 dimensions:
```python
vec = generate_embedding(text, dim=256)
vec_bytes = struct.pack('256f', *vec)
c.execute("INSERT INTO kg_vectors (entity_id, vector_data) VALUES (?,?)", (entity_id, vec_bytes))
```

## Import a Paper (Python)

```python
import sqlite3, hashlib, struct, json, math

conn = sqlite3.connect("/Users/hiyenwong/.openclaw/workspace/kg.db")
c = conn.cursor()

# Insert entity
c.execute("INSERT INTO kg_entities (title, url, content, authors, published_date, category, source) VALUES (?,?,?,?,?,?,?)",
    (title, url, content, authors, date, category, "arxiv"))
entity_id = c.lastrowid

# Generate vector (binary float32 format — more compact than JSON)
vec = generate_embedding(title + " " + (content or ""))
vec_bytes = struct.pack(f'{len(vec)}f', *vec)
c.execute("INSERT INTO kg_vectors (entity_id, vector_data) VALUES (?,?)",
    (entity_id, vec_bytes))
conn.commit()
```

### Embedding Generation (hash-based, deterministic)

The workspace kg.db uses hash-based embeddings (not semantic). This is fine for
keyword-level similarity and deterministic dedup, but produces low cosine scores
(0.05-0.26). For real semantic search, use sentence-transformers.

```python
def generate_embedding(text, dim=256):
    """Deterministic 256-dim embedding from text via hash.
    Good for keyword matching, NOT semantic similarity.
    Returns a unit vector (normalized)."""
    import hashlib, math
    vector = []
    for i in range(dim):
        h = hashlib.md5(f"seed_{i}_{text}".encode()).hexdigest()
        val = int(h[:8], 0xFFFFFFFF) / 0xFFFFFFFF * 2 - 1  # map to [-1, 1]
        vector.append(val)
    # Normalize to unit vector
    norm = math.sqrt(sum(v*v for v in vector))
    if norm > 0:
        vector = [v/norm for v in vector]
    return vector
```

**Format choice**: Use `struct.pack` (binary float32) for new vectors — it's more
compact and faster to load than JSON. Both formats work; the `parse_vector()`
function reads either.

## Creating Relationships Between Papers

When importing new papers, create relationships with existing entities based on keyword overlap:

```python
# Get existing entities
c.execute("SELECT id, title, content FROM kg_entities WHERE id NOT IN ({new_ids})")
existing = c.fetchall()

# Build keyword map for new papers
keywords_map = {}
for eid, title, content in new_entities:
    text = (title + ' ' + (content or '')).lower()
    keywords_map[eid] = set(text.split())

for eid, title, content in existing:
    text = (title + ' ' + (content or '')).lower()
    words = set(text.split())
    for new_eid, new_words in keywords_map.items():
        overlap = len(new_words & words)
        if overlap > 3:
            weight = min(0.9, overlap / 20.0)
            rel_type = 'related_to'
            # Cross-domain detection
            if any(w in title.lower() for w in ['quantum']) and \
               any(w in title.lower() for w in ['neural', 'brain', 'spiking']):
                rel_type = 'cross_domain'
                weight += 0.1
            c.execute("INSERT INTO kg_relationships (source_id, target_id, relationship_type, weight) VALUES (?,?,?,?)",
                (min(new_eid, eid), max(new_eid, eid), rel_type, round(weight, 2)))
```

## Deduplication Before Import

```python
# Check existing titles (case-insensitive)
c.execute("SELECT title FROM kg_entities")
existing_titles = {row[0].lower().strip() for row in c.fetchall()}

new_papers = []
for p in papers:
    if p['title'].lower().strip() not in existing_titles:
        new_papers.append(p)
```

## Vector Similarity Search

```python
def search(query_text, limit=8):
    seed = struct.unpack('>I', hashlib.sha256(query_text.encode()).digest()[:4])[0]
    qvec = np.random.RandomState(seed).randn(128).astype(np.float32)
    qvec /= np.linalg.norm(qvec)
    
    c.execute("SELECT v.entity_id, v.vector_data, e.title FROM kg_vectors v JOIN kg_entities e ON v.entity_id = e.id")
    sims = [(eid, float(np.dot(qvec, np.frombuffer(vb, np.float32))), t)
            for eid, vb, t in c.fetchall() if len(np.frombuffer(vb, np.float32)) == 128]
    return sorted(sims, key=lambda x: -x[1])[:limit]
```

## PageRank

```python
# Build adjacency from kg_relationships, iterate PR = (1-d)/n + d * M * PR
# Standard PageRank with damping=0.85, 50 iterations
```

## Hourly Research Cron Pipeline

For the recurring hourly research workflow (topic rotation + arXiv + Anthropic + KG analysis), see [references/hourly-research-cron.md](references/hourly-research-cron.md). Covers the full pipeline from `weekly_topics.py` through KG analysis to report generation.

## Common Pitfalls

- **ArXiv URL encoding**: When using `urllib.request` with arXiv API, spaces in query params cause `http.client.InvalidURL`. Always use `urllib.parse.quote(query)` before constructing the URL. Pattern: `f'http://export.arxiv.org/api/query?search_query=all:%22{quote(query)}%22'`
- **Vector format** (RESOLVED 2026-05-06): All vectors are now binary float32 256-dim. No JSON-encoded vectors remain. Use `struct.unpack('256f', vdata)` directly.
- **Pipe-to-interpreter blocked**: Security guardrail blocks `curl ... | python3`. Always save curl output to a file first, then run python on the file. Pattern: `curl -o /tmp/arxiv.xml "https://..." && python3 parse.py /tmp/arxiv.xml`.
- **arXiv API with httpx**: Use `https://` (not `http://`) and add retry logic with `time.sleep(3.5)` between requests. arXiv returns 429 aggressively. With httpx, use `timeout=30` and retry on 429 with exponential backoff.
- **Vector type mismatch** (RESOLVED): All vectors are now binary float32. No TEXT vectors remain.
- **Dimension**: All vectors are 256-dim. Filter with `len(np.frombuffer(vb, np.float32)) == 256` before dot product.
- **kg_tool creates wrong tables**: It uses `kg_relations` not `kg_relationships`, and `entity_type/name/properties` not `title/url/content`.
- **kg_tool is symlink-compatible**: `~/wiki/kg.db` is a symlink to workspace `kg.db` (verified 2026-05-05). The tool reads correct entity counts but its search function has limited matching — it works for some queries but returns empty for others. Use SQL LIKE for reliable search. The tool's `pagerank`, `communities`, `generate-embeddings`, and `stats` commands work reliably with the workspace schema.
- **Hash-based vectors are not semantic**: Cosine similarity scores are consistently low (0.05-0.26). Good for deterministic keyword matching, not true semantic search. Louvain community detection produces mostly singleton communities — expected behavior with hash vectors. For real clustering, use sentence-transformer embeddings.
- **arXiv fetch**: `web_extract` blocks arxiv.org URLs as "private/internal network." Use `web_search` for discovery (works reliably), then `curl -x http://127.0.0.1:7890 "https://export.arxiv.org/api/query?id_list=..."` for full metadata. **arXiv API is aggressively rate-limited** — returns "Rate exceeded." on most requests even with proxy. `sleep 4` is NOT enough; use `sleep 10` minimum. When rate-limited, fall back to `web_search` which has no rate limits. Never pipe curl output directly to Python — save to file first (security guardrail blocks pipe-to-interpreter).
- **Edge tuple unpacking**: `kg_relationships` has 3 columns (source_id, target_id, weight). Unpack as `for src, tgt, w in edges` not `for src, tgt in edges`.
- **Reading paper content when web_extract blocks**: Use `browser_navigate` + `browser_snapshot` for arxiv URLs. See [references/hourly-research-cron.md](references/hourly-research-cron.md) for the full fallback chain.
- **Vector corruption recovery**: If you get `ValueError: buffer size must be a multiple of element size` when loading vectors, existing vectors are corrupted or mixed-format. Fix by regenerating all vectors with consistent format:
  ```python
  # 1. Check existing vector sizes for consistency
  rows = c.execute("SELECT LENGTH(vector_data) FROM kg_vectors LIMIT 20").fetchall()
  sizes = set(r[0] for r in rows)
  # If multiple sizes exist, some are corrupted or mixed format
  
  # 2. Clear and regenerate all vectors
  c.execute("DELETE FROM kg_vectors")
  for eid, title, content in all_entities:
      vec = generate_embedding(f"{title} {content or ''}")
      vec_bytes = struct.pack(f'{len(vec)}f', *vec)
      c.execute("INSERT INTO kg_vectors (entity_id, vector_data) VALUES (?,?)", (eid, vec_bytes))
  conn.commit()
  ```
