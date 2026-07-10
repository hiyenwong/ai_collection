---
name: research-literature-kg
description: "Build and analyze knowledge graphs from research literature. Automated pipeline: arxiv search → entity extraction → KG construction → vector embeddings → semantic search → skill pattern extraction. Use when user asks to analyze papers, build research knowledge bases, find related work, or extract reusable patterns from academic literature."
---

# Research Literature Knowledge Graph

## Description

Automated pipeline for building and analyzing knowledge graphs from academic research literature. Integrates arxiv search, entity extraction, vector embeddings, and graph algorithms to discover patterns and extract reusable skill patterns.

## Activation Keywords

- research literature KG
- build knowledge graph from papers
- paper analysis pipeline
- arxiv to KG
- 文献知识图谱
- 科研论文分析
- 论文知识库
- extract skills from papers

## Tools Used

- `exec`: Run Python scripts, kg_tool CLI, arxiv API queries
- `web_search`: Search for related research
- `web_fetch`: Fetch paper content from arxiv
- `read`: Read existing skills, KG schema
- `write`: Store results, update memory
- `feishu_bitable_app`: Store structured paper metadata (optional)

## Workflow

### Phase 1: Literature Collection

1. **Define research scope**:
   - Primary topic (daily focus)
   - Secondary topic (weekly theme)
   - Keywords for search

2. **Search arxiv** (HTTPS required, rate limit ~3 req/sec):
   ```python
   query = f'cat:{category}+AND+all:{keywords}'
   url = f'https://export.arxiv.org/api/query?search_query={query}&max_results=10&sortBy=submittedDate&sortOrder=descending'
   # Wait 3-5s between requests. On 429, wait 10s+ and retry.
   # Check cached JSON files first (e.g. scripts/*_papers.json) before hitting API.
   ```

3. **Parse results**: Extract title, authors, abstract, arxiv_id, category, published_date

### Phase 2: KG Construction

1. **Database**: `kg.db` at `/Users/hiyenwong/.openclaw/workspace/kg.db`
2. **Schema**: See [references/kg-db-schema.md](references/kg-db-schema.md) for verified column names and types
3. **Insert entities**: Use `execute_code` with `sqlite3` — columns are `title, url, content, authors, published_date, category, source`
4. **No `description` column** — use `content` for abstracts

### Phase 3: Vector Embeddings

1. **Generate embeddings** — 1024-byte BLOBs (256 float32 values) stored as `vector_data`
2. **Fallback: hash-based vectors** when embedding model unavailable:
   ```python
   import struct, hashlib
   values = [struct.unpack('f', hashlib.md5(f"{text}{i}".encode()).digest()[:4])[0] for i in range(256)]
   vector_bytes = struct.pack('256f', *values)
   ```

### Phase 4: Graph Analysis

1. **PageRank**: Find important papers
2. **Louvain**: Detect research clusters
3. **Semantic search**: Find related papers

### Phase 5: Pattern Extraction

1. **Identify patterns**: Look for recurring methods, frameworks, approaches
2. **Extract skills**: Use `skill-extractor` skill
3. **Create new skill**: Use `skill-creator` skill

## Database Schema (Actual — verified 2026-06-14)

**CRITICAL**: The schema evolved from earlier versions. The `kg_entities` table is now a generic entity table, NOT a flat paper table. There is also a separate `arxiv_papers` table.

```sql
-- kg_entities: generic entity table
CREATE TABLE kg_entities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    description TEXT,
    metadata TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    source TEXT DEFAULT '',
    created_date TEXT DEFAULT '',
    UNIQUE(name, type)
);

-- arxiv_papers: dedicated paper table
CREATE TABLE arxiv_papers (
    id TEXT PRIMARY KEY,
    title TEXT, url TEXT, abstract TEXT, authors TEXT,
    published TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- kg_vectors: embedding + text
CREATE TABLE kg_vectors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_id INTEGER,
    embedding BLOB,
    text TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (entity_id) REFERENCES kg_entities(id)
);

-- kg_edges: edge list
CREATE TABLE kg_edges (
    source TEXT, target TEXT, relation TEXT,
    weight REAL DEFAULT 1.0,
    PRIMARY KEY (source, target, relation)
);
```

⚠️ **No `title`, `content`, `url` columns in kg_entities.** Use `name`, `type`, `description`, `metadata`.
⚠️ **No `vector_data` column** — kg_vectors uses `embedding` BLOB + `text` TEXT.
⚠️ **kg_edges** uses TEXT source/target, not INTEGER foreign keys.

### Correct Insert Patterns

```python
# Into arxiv_papers (preferred for papers)
cursor.execute('INSERT OR IGNORE INTO arxiv_papers (id, title, url, abstract, published) VALUES (?,?,?,?,?)',
    (arxiv_id, title, url, abstract, published))

# Into kg_entities (generic)
cursor.execute('INSERT OR IGNORE INTO kg_entities (name, type, description, metadata, source, created_date) VALUES (?,?,?,?,?,?)',
    (title[:200], 'arxiv_paper', summary[:300],
     json.dumps({'category': cat, 'arxiv_id': arxiv_id}),
     'arxiv-cron', published[:10]))
```

Also see [references/kg-db-schema.md](references/kg-db-schema.md) for complete schema.

## Error Handling

### httpx Proxy Syntax
When using httpx with a proxy, use `proxy="http://..."` (singular, string). Do NOT use `proxies={}` dict syntax — it causes `Client.__init__() got an unexpected keyword argument 'proxies'`.
```python
with httpx.Client(timeout=30, proxy="http://127.0.0.1:7890") as client:
    resp = client.get(url)
```

### kg.db Schema Mismatch
The `kg_entities` table schema changed from a flat paper table to a generic entity table (`name`, `type`, `description`, `metadata` columns). Always `sqlite3 kg.db ".schema"` before inserting. There is now a separate `arxiv_papers` table for paper data. Insert into both for full integration.

### arxiv API Rate Limit (429)
- Always use HTTPS (HTTP may be blocked)
- Wait 3-5s between requests
- On 429: wait 10+ seconds before retry
- **Fallback**: Check for pre-cached JSON files in `scripts/` directory (cron jobs save results there)

### Embedding Generation Failure
- Fall back to hash-based 256-float vectors (see Phase 3)
- No `sentence-transformers` required for fallback

### Vector Dimension Mismatch
- kg.db vectors are 1024 bytes (256 float32)
- Ensure `struct.pack('256f', *values)` format matches

## Related Skills

- `arxiv-search`: Paper search details
- `skill-extractor`: Pattern extraction
- `skill-creator`: Skill creation
- `feishu-bitable`: Alternative storage

## Notes

- KG persists across sessions via SQLite
- Vectors enable semantic search
- Weekly topics rotate through domains
- Daily quantum mechanics focus
