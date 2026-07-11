# arXiv Research Fallback Strategies

## arXiv API Rate Limiting

- **Symptom:** HTTP 429 "Rate exceeded" or connection timeouts through proxy
- **Mitigation:** 
  - `time.sleep(3-4)` between queries minimum
  - Retry once on 429 with 10s backoff
  - Use narrow queries: `all:"exact phrase" AND cat:quant-ph`
  - Prefer `execute_code` with `httpx` over `terminal` for API calls

## Web Extract Blocks

- `web_extract` blocks arxiv.org URLs (flagged as "private/internal network")
- `web_search` (Firecrawl) may fail with `'NoneType' object has no attribute 'status_code'`
- **Fallback:** Use arXiv API XML directly via `httpx` in `execute_code`

## Knowledge Graph as Primary Data Source

When arXiv is unavailable, query existing papers from `kg.db`:

```sql
-- Find papers by topic keywords
SELECT id, title, content, published_date, category 
FROM kg_entities 
WHERE title LIKE '%quantum%' AND source LIKE 'arxiv%'
ORDER BY published_date DESC;

-- Check if paper already exists
SELECT id FROM kg_entities WHERE url = 'https://arxiv.org/abs/2605.XXXXX';

-- Count papers by source
SELECT source, COUNT(*) FROM kg_entities GROUP BY source ORDER BY COUNT(*) DESC;
```

### KG Schema Reference
| Table | Key Columns | Purpose |
|-------|------------|---------|
| `kg_entities` | id, title, url, content, authors, published_date, category, source | Paper/article storage |
| `kg_vectors` | id, entity_id, vector_data | Embedding vectors (1581 vectors) |
| `pagerank` | entity_id, score | PageRank scores (848 entities) |
| `kg_relations` | source_id, target_id, relation_type | Semantic relations (3658 types) |
| `kg_relationships` | id, source_id, target_id, relation_type | Edge table (310K+ edges) |
