# arXiv API Rate Limiting: Patterns and Recovery

The arXiv API (`export.arxiv.org`) enforces strict rate limits (~3 requests per 30 seconds per IP). Both arXiv and Semantic Scholar share similar rate limiting behavior.

## Observed Behavior

- `HTTP 429 "Rate exceeded."` — immediate rate limit response
- `timeout` — connection timeout on subsequent attempts even after waiting 15-30s
- Repeated failed attempts extend the block period
- If one API (arXiv) is blocked, the other (Semantic Scholar) likely is too

## Successful Recovery Pattern

1. **Wait at least 60 seconds** before retrying (15s/30s/45s waits still fail)
2. **Use minimal query**: simple category filter like `cat:quant-ph` with `max_results=5`
3. **Single request only** — don't chain multiple queries immediately after success
4. If timeout occurs instead of 429, wait another 30s before retrying

## Minimal Working Query

```python
params = {
    'search_query': 'cat:quant-ph',   # Simple category, not complex boolean
    'max_results': 5,
    'sortBy': 'submittedDate',
    'sortOrder': 'descending'
}
r = httpx.get("https://export.arxiv.org/api/query", params=params, timeout=60, proxy="http://127.0.0.1:7890")
```

## Fallback When Both APIs Blocked

- Fall back to existing knowledge graph analysis (`kg.db`)
- Use `kg_tool` CLI for PageRank, community detection, and search
- Create skills from high-impact papers already in the KG
- Generate hash-based 384-dim vector embeddings for new entries if sentence-transformers unavailable
