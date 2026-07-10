# arXiv API Error Patterns and Recovery

## Observed Error Patterns (May 2026)

### Pattern 1: 429 → 503 Escalation

The arXiv API at `export.arxiv.org` exhibits a two-stage failure:

1. **Stage 1 (429)**: "Rate exceeded" — returned by curl when rate limit hit
2. **Stage 2 (503)**: Full service unavailable — the API stops responding entirely

**Critical observation**: Once 503 starts, sleeping 30-60s does NOT help. The service remains unavailable for extended periods (10+ minutes observed).

### Pattern 2: Python httpx Timeout

When using `httpx` library:
- `httpx.get(..., proxy=PROXY)` → returns `TimeoutError: The read operation timed out`
- Even with `timeout=60`, connection never completes during 503 state

### What Does NOT Work

| Strategy | Result |
|----------|--------|
| Sleep 30s | Still 429/503 |
| Sleep 60s | Still 503 |
| Use proxy | No effect (server-side rate limit) |
| Different Python library (urllib vs httpx) | Same failure |
| curl instead of httpx | Same 429/503 |

### What DOES Work

| Strategy | Result |
|----------|--------|
| Query kg.db directly | ✅ Full metadata available |
| Use kg_tool pagerank | ✅ Influence ranking |
| Use kg_tool communities | ✅ Research clustering |
| web_search with specific terms | ✅ Sometimes works |
| Wait 15+ minutes then retry | ✅ Usually resolves eventually |

### Retry Strategy Recommendation

```python
def resilient_arxiv_search(query, max_retries=3):
    for attempt in range(max_retries):
        try:
            result = call_arxiv_api(query)
            return result
        except (RateLimitError, ServiceUnavailableError) as e:
            wait = 3 * (2 ** attempt)  # 3s, 6s, 12s
            time.sleep(wait)
    
    # If still failing after exponential backoff, 
    # DON'T keep sleeping — switch to fallback immediately
    return activate_kg_fallback(query)
```

**Key lesson**: Exponential backoff is for transient errors. arXiv's 429/503 cascade is NOT transient — it's a persistent block. After 3 quick retries (≤15s total), abandon the API and use fallback.
