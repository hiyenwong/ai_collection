# arXiv API Pitfalls (Session Learnings)

## Query Syntax — Critical Rules

The arXiv API has **strict syntax requirements** that differ from typical search engines:

| Pattern | Result | Notes |
|---------|--------|-------|
| `all:quantum statistics` | ✅ Works | Space-separated keywords |
| `all:quantum AND all:statistics` | ❌ "syntax error" | AND operator rejected |
| `all:"quantum statistics"` | ❌ "syntax error" | Quotes rejected |
| `cat:quant-ph AND all:algorithm` | ❌ "syntax error" | AND rejected in any form |
| `all:quantum cat:quant-ph` | ⚠️ Unreliable | Category mixing may fail |

**Rule of thumb**: Use `all:keyword1 keyword2` — simple, space-separated, no operators, no quotes.

## Connection Requirements

1. **Always HTTPS**: `https://export.arxiv.org/api/query` — HTTP triggers security scan blocks
2. **Proxy**: In sandboxed environments, add `--proxy http://127.0.0.1:7890` (curl) or `proxy="http://127.0.0.1:7890"` (httpx)
3. **Timeout**: Use ≥30 seconds — API can be slow
4. **Rate limits**: "Rate exceeded" on burst requests — wait 5-10s between queries

## Python httpx Example (Working)

```python
import httpx

proxy = "http://127.0.0.1:7890"
with httpx.Client(proxy=proxy, timeout=30) as client:
    resp = client.get(
        "https://export.arxiv.org/api/query",
        params={
            "search_query": "all:quantum statistics",  # NO AND, NO quotes
            "max_results": 5,
            "sortBy": "submittedDate",
            "sortOrder": "descending"
        }
    )
```

## Curl Example (Working)

```bash
curl -s --proxy http://127.0.0.1:7890 \
  "https://export.arxiv.org/api/query?search_query=all:quantum+statistics&max_results=5"
```

## Error Responses

| Response | Cause | Fix |
|----------|-------|-----|
| "syntax error" | AND operator or quotes in query | Use simple space-separated keywords |
| "Rate exceeded" | Too many requests | Wait 5-10s, retry |
| Timeout (124) | No proxy or slow API | Add proxy, increase timeout |
| Security scan block | HTTP (not HTTPS) | Use HTTPS URL |
