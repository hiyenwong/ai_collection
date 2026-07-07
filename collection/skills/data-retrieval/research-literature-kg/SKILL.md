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

## Database Schema

See [references/kg-db-schema.md](references/kg-db-schema.md) for complete schema, column types, and common queries.

## Error Handling

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
