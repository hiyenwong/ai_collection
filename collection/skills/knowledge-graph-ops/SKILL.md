---
name: knowledge-graph-ops
description: >
  Operations for the SQLite knowledge graph (kg.db) at
  /Users/hiyenwong/.openclaw/workspace/kg.db. Use when importing papers,
  generating embeddings, running PageRank/community detection, or querying
  the research knowledge graph. Covers the kg_tool CLI and raw SQLite
  approaches. NOTE: ~/wiki/kg.db is a symlink to the workspace kg.db —
  approaches. WARNING: kg_tool has a schema mismatch — see references.
  NOTE: vectors contain mixed dimensions (256-dim and 384-dim) — see Vector Format.
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

## ⚠️ Database Identity

`~/wiki/kg.db` is a **symlink** to `~/.openclaw/workspace/kg.db` — they are the same database.
Both `kg_tool` (which targets `~/wiki/kg.db`) and direct Python/SQLite (targeting workspace path)
operate on the SAME data. Use whichever is convenient.

## Working Schema

```sql
kg_entities (id, title, url, content, authors, published_date, category, source, created_at, updated_at)
kg_vectors  (id, entity_id, vector_data)  -- raw float32 BLOBs (256-dim, 1024 bytes each)
kg_relationships (id, source_id, target_id, relationship_type, weight, created_at)
```

### Vector Format

### Vector Format

All vectors in kg_vectors are stored as **raw float32 BLOBs**, 256 dimensions (1024 bytes each). No JSON-encoded or mixed-format vectors remain.

**⚠️ Mixed dimensions (2026-05-07)**: The database contains some 384-dim vectors (1536 bytes) created by sessions using a different embedding function. Always derive dimension from blob length: `dim = len(vdata) // 4` rather than hardcoding 256.

**⚠️ sqlite3 BLOB-as-string**: sqlite3 may return `vector_data` as `str` instead of `bytes`. Convert with `vdata.encode('latin-1')` before `struct.unpack`.

```python
import struct

def parse_vector(vdata):
    """Parse float32 vector from kg_vectors BLOB. Handles both str/bytes."""
    if isinstance(vdata, str):
        vdata = vdata.encode('latin-1')
    dim = len(vdata) // 4
    return struct.unpack(f'{dim}f', vdata)

def vector_to_blob(vector):
    """Convert list of floats to float32 BLOB for kg_vectors."""
    return struct.pack(f'{len(vector)}f', *vector)
```

When generating new vectors, use **256 dimensions** to match the established schema:
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

When importing new papers, create relationships with existing entities based on keyword overlap.
For the full batch-creation script (tested on 410 entities, creates ~1,800 relationships),
## Creating Relationships Between Papers

When importing new papers, create relationships based on **category match** OR **high keyword overlap**:

```python
STOP_WORDS = {'the', 'a', 'an', 'is', 'are', 'was', 'were', 'for', 'and', 'of',
    'in', 'to', 'with', 'on', 'by', 'from', 'at', 'that', 'this', 'it', 'as'}

def keywords(text):
    return {w for w in (text or '').lower().split() if w not in STOP_WORDS and len(w) > 2}

# Build keyword map
keywords_map = {}
for eid, title, content, cat in all_entities:
    keywords_map[eid] = (keywords(title + ' ' + (content or '')), cat)

for eid1, (kw1, cat1) in keywords_map.items():
    for eid2, (kw2, cat2) in keywords_map.items():
        if eid1 >= eid2:
            continue
        overlap = len(kw1 & kw2)
        # Connect if same category OR very high overlap (>8 words)
        if cat1 and cat1 == cat2:
            weight = min(0.9, overlap / 15.0)
            rel_type = 'same_category'
        elif overlap > 8:
            weight = min(0.7, overlap / 25.0)
            rel_type = 'related_to'
        else:
            continue
        # Cross-domain detection
        if cat1 != cat2 and any(w in kw1 for w in {'quantum'}) and \
           any(w in kw2 for w in {'neural', 'brain', 'spiking'}):
            rel_type = 'cross_domain'
            weight = min(0.9, weight + 0.2)
        try:
            c.execute("INSERT INTO kg_relationships (source_id, target_id, relationship_type, weight) VALUES (?,?,?,?)",
                (eid1, eid2, rel_type, round(weight, 2)))
        except sqlite3.IntegrityError:
            pass
```

## Deduplication Before Import

**URL-based dedup is more reliable than title-based** (titles may vary slightly between sources; URLs are canonical):

```python
# Preferred: URL-based dedup (canonical, avoids title variation false positives)
c.execute("SELECT url FROM kg_entities WHERE url IS NOT NULL AND url != ''")
existing_urls = {row[0].lower().strip() for row in c.fetchall()}

new_papers = []
for p in papers:
    if p['url'].lower().strip() not in existing_urls:
        new_papers.append(p)

# Fallback: title-based dedup (only if URLs unavailable)
c.execute("SELECT title FROM kg_entities")
existing_titles = {row[0].lower().strip() for row in c.fetchall()}
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
See [references/medical-quantum-session-notes.md](references/medical-quantum-session-notes.md) for Medicine+Quantum session results, successful web_search query patterns, and community detection observations.

## Common Pitfalls

- **RELATIONSHIP EXPLOSION (2026-05-07)**: The keyword-overlap approach with threshold >3 creates O(n²) relationships. With 417 entities, this produced 117,805 relationships — a nearly complete graph. PageRank becomes less discriminative, and community detection collapses to one giant cluster. **Fixes**: (a) Raise threshold to >8, (b) Remove stop words before splitting, (c) Only connect papers within same category, or (d) Cap relationships per entity. For batch imports, prefer `overlap > 8` and category-matching over raw keyword overlap.
- **Community detection collapse**: With dense relationships from keyword overlap, Louvain/label-propagation produces one giant community (415/417 papers observed). This is expected with the current relationship strategy. For meaningful clustering, use sparse relationships (category-matching only, or high overlap threshold) or sentence-transformer embeddings.
- **ArXiv API rate limiting (CONFIRMED 2026-05-07)**: Even with `http://127.0.0.1:7890` proxy, `curl` to `export.arxiv.org/api/query` returns "Rate exceeded." immediately. `web_search` remains the only reliable arXiv discovery method. When you need full metadata, `web_search` + extraction is more reliable than the arXiv API.
- **ArXiv URL encoding**: When using `urllib.request` with arXiv API, spaces in query params cause `http.client.InvalidURL`. Always use `urllib.parse.quote(query)` before constructing the URL. Pattern: `f'http://export.arxiv.org/api/query?search_query=all:%22{quote(query)}%22'`
- **Vector format** (RESOLVED 2026-05-06): All vectors are now binary float32 256-dim. No JSON-encoded vectors remain. Use `struct.unpack('256f', vdata)` directly.
- **Pipe-to-interpreter blocked**: Security guardrail blocks `curl ... | python3`. Always save curl output to a file first, then run python on the file. Pattern: `curl -o /tmp/arxiv.xml "https://..." && python3 parse.py /tmp/arxiv.xml`.
- **arXiv API with httpx**: Use `https://` (not `http://`) — the API returns 301 redirect from http. With httpx, use `follow_redirects=True` or `https://` directly. Add retry logic with `time.sleep(3.5)` between requests. arXiv returns 429 aggressively. With httpx, use `timeout=30` and retry on 429 with exponential backoff.
- **Vector type mismatch** (RESOLVED): All vectors are now binary float32. No TEXT vectors remain.
- **sqlite3 BLOB-as-string**: When reading `kg_vectors.vector_data` from SQLite, the column may be returned as Python `str` instead of `bytes`. This causes `struct.unpack` to fail with "a bytes-like object is required". Fix: `if isinstance(vdata, str): vdata = vdata.encode('latin-1')` before unpacking.
- **Dimension**: All vectors are 256-dim. Filter with `len(np.frombuffer(vb, np.float32)) == 256` before dot product.
- **kg_tool creates wrong tables**: It uses `kg_relations` not `kg_relationships`, and `entity_type/name/properties` not `title/url/content`.
- **kg_tool search unreliable**: `kg_tool search --query "..."` returns empty for most queries, even valid ones. **Use raw SQL LIKE queries instead**: `sqlite3 kg.db "SELECT id, title FROM kg_entities WHERE lower(title) LIKE '%quantum%'"`. The tool's `pagerank`, `communities`, `generate-embeddings`, and `stats` commands work reliably.
- **arXiv fetch**: `web_extract` blocks arxiv.org URLs as "private/internal network." Use `web_search` for discovery (works reliably), then `curl -x http://127.0.0.1:7890 "https://export.arxiv.org/api/query?id_list=..."` for full metadata. **arXiv API is aggressively rate-limited** — returns "Rate exceeded." on most requests even with proxy. `sleep 4` is NOT enough; use `sleep 10` minimum. **curl with proxy can also fully timeout (60s)** — if curl times out even with proxy, the API is completely inaccessible for that session. When rate-limited or timed-out, fall back to `web_search` which has no rate limits. `web_search` with `site:arxiv.org` query returns structured data (title, description/abstract, url) sufficient for direct KG import without needing the arXiv API at all. Never pipe curl output directly to Python — save to file first (security guardrail blocks pipe-to-interpreter).
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
- **sqlite3 BLOB returned as str**: `sqlite3` may return BLOB columns as Python `str` instead of `bytes` depending on version/connection. Always check: `if isinstance(vb, str): vb = vb.encode('latin-1')` before `struct.unpack`.
- **Variable vector dimensions**: Don't assume all vectors are 256-dim. Check `n_dims = len(vb) // 4` and use `struct.unpack(f'{n_dims}f', vb)`. Guard with `if len(vb) % 4 != 0: continue`.
