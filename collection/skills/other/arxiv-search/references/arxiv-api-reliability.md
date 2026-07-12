# arXiv API Reliability Notes (2026-05)

## Rate Limiting Behavior

The arXiv API at `export.arxiv.org` is **extremely aggressive** with rate limiting:
- Returns `"Rate exceeded."` (HTTP 429) on most consecutive requests
- Even with proxy (`127.0.0.1:7890`), rate limits fire after ~1 request
- `sleep 3-4` between requests is NOT enough — triggers rate limit immediately
- `sleep 10` is the minimum viable delay

## httpx Parameter Gotcha

```python
# BROKEN — 'proxies' doesn't exist in recent httpx
httpx.Client(proxies={"https": "http://127.0.0.1:7890"})
# Error: Client.__init__() got an unexpected keyword argument 'proxies'

# CORRECT — use Proxy + HTTPTransport
proxy = httpx.Proxy("http://127.0.0.1:7890")
transport = httpx.HTTPTransport(proxy=proxy)
with httpx.Client(transport=transport, timeout=120, follow_redirects=True) as client:
    ...
```

## 301 Redirect

`http://export.arxiv.org/api/query` → `https://export.arxiv.org/api/query` (301)
Always use `https://` URL. Add `follow_redirects=True` if using http://.

## Tool Reliability Ranking for arXiv (most → least reliable)

1. **`web_search`** — No rate limits, works for finding papers by ID/keywords
2. **`curl -x proxy`** — Works but rate-limited after 1-2 requests
3. **`browser_navigate`** — Works for individual paper pages, slow for bulk
4. **`web_extract`** — Blocks arxiv.org as "private/internal network"
5. **`execute_code` + httpx** — Rate-limited, parameter quirks (see above)

## Recommended Fallback Chain

```
1. Try arXiv API via curl (max 1-2 requests, save to file)
2. If rate-limited → web_search("arxiv {id}")
3. If need full text → browser_navigate("https://arxiv.org/html/{id}v1")
4. If need listing → curl to /list/{category}/new (HTML parse)
```
