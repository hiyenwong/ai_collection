# arXiv API Access — Fallback Strategy

## Problem

arXiv API (`export.arxiv.org/api/query`) aggressively rate-limits clients:
- **HTTP 429 "Rate exceeded"** is common, especially through proxy servers
- Direct HTTPS (without proxy) may time out if no direct route exists
- `web_search` and `web_extract` tools block arxiv.org URLs as "private/internal"
- Proxy IP pools are often shared and rate-limited across many users

## Observed Failure Modes (2026-05-16 session)

| Method | Result | Root Cause |
|--------|--------|------------|
| `curl --proxy http://127.0.0.1:7890` | HTTP 429 "Rate exceeded" | Shared proxy IP rate-limited |
| `httpx.get(..., proxy=...)` | HTTP 429 | Same |
| `httpx.get(..., no proxy, 15s timeout)` | Timeout | No direct route to arxiv.org |
| `web_search(query="site:arxiv.org ...")` | Empty results | Search engine index gap |
| `web_extract(urls=["https://arxiv.org/..."])` | "Blocked: private/internal" | Tool security policy |

## Working Fallback Chain

### 1. Knowledge Graph Cache (Preferred for recurring tasks)

If you have a local `kg.db` SQLite database with paper data, query it first:

```bash
sqlite3 kg.db "SELECT title, url, content, published_date, category
FROM kg_entities WHERE title LIKE '%{topic}%' AND category LIKE '%{field}%'
ORDER BY published_date DESC LIMIT 10;"
```

This works because hourly research sessions already populate the KG. The data is fresh enough for most research workflows.

### 2. kg_tool Search

```bash
./scripts/kg_tool/target/release/kg_tool search --query "{topic}" --limit 10
```

Uses vector similarity search on the knowledge graph.

### 3. arXiv API with Rate Limit Awareness

If you must use the API:
- **No proxy**: `httpx.get(url, timeout=15, follow_redirects=True)`
- **With proxy**: Accept 429, wait 3-5s, retry once
- **Max 1 request per 3 seconds** (arXiv's stated rate limit)
- Check HTTP 301 redirect — arxiv.org API moved from http to https

### 4. What Does NOT Work

- `web_search` for `site:arxiv.org` — search engine index has gaps for very recent papers
- `web_extract` for arxiv.org URLs — blocked by tool security policy
- `delegate_task` for arXiv search — will timeout trying the same failing approaches
