# Cron Job Research Failures — 2026-05-26

## Simultaneous API Failures (2026-05-26)

All three external research sources failed simultaneously during a cron job run:

| Source | Error | Root Cause |
|--------|-------|------------|
| arXiv API (urllib) | HTTP 429 | Rate limited — too many requests |
| web_search (Firecrawl) | `'NoneType' object has no attribute 'status_code'` | Firecrawl backend unavailable/broken in cron env |
| web_extract (arxiv.org) | `Blocked: URL targets a private or internal network address` | Proxy/network resolves arxiv.org to blocked IP range |
| curl to arxiv.org | Security scan flagged plain HTTP | Hermes blocks plain HTTP URLs in commands |

## Successful Fallback

When all external APIs fail, the research workflow can still proceed using **local knowledge graph only**:

1. **Query kg.db** (`scripts/kg_tool/kg.db`) for existing papers matching the topic
2. **Run PageRank** on `kg_relations` to identify important papers
3. **Run Louvain community detection** on `kg_relations` to find research clusters
4. **Compute cosine similarity** on `kg_vectors` for vector search
5. Extract skills from existing papers that don't yet have corresponding skills
6. Create new skills and sync to ai_collection

### Key SQL Patterns

```sql
-- Find papers by topic
SELECT id, name, type, description FROM kg_entities 
WHERE type='paper' AND LOWER(description) LIKE '%quantum%'

-- PageRank: build adjacency from kg_relations
SELECT source_id, target_id, weight FROM kg_relations

-- Vector search: cosine similarity on kg_vectors
-- Note: embeddings stored as BLOB (128-dim float32)
SELECT v.entity_id, v.embedding, v.text, e.name, e.description 
FROM kg_vectors v JOIN kg_entities e ON v.entity_id=e.id
```

### Embedding Format Note

- `kg_vectors.embedding`: BLOB, 512 bytes = 128 float32 values
- Must set `conn.text_factory = lambda x: str(x, 'utf-8', errors='replace')` for blob handling
- `np.frombuffer(emb_bytes, dtype=np.float32)` for conversion

## Recommendation

For cron jobs, the knowledge graph fallback is the **primary** research method. External APIs (arXiv, web_search) should be treated as optional enrichment, not dependencies.
