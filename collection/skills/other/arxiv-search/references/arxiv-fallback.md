# arXiv API Fallback Guide

## When API Fails

arXiv API aggressively rate-limits. HTTP 429 responses are common even with proper User-Agent headers.

### Browser Fallback Workflow

1. Navigate to `https://arxiv.org/search/`
2. Enter query in search box
3. Select field: All fields / Title / Author / Abstract
4. Click Search
5. Extract papers from result list (titles, IDs, authors visible without clicking)
6. For abstracts, click `arXiv:{id}` links → `https://arxiv.org/abs/{id}`
7. Sort by "Submission date (newest first)" for latest papers

### curl with Proxy

```bash
curl -s --proxy http://127.0.0.1:7890 -m 20 "https://export.arxiv.org/api/query?search_query=all:quantum+AND+all:control&max_results=5"
```

### Rate Limit Rules

- Always use HTTPS (not HTTP — triggers security scan warnings)
- Wait 3-4s between API calls
- On 429: wait 5s, retry with different query
- On timeout: switch to browser fallback immediately — don't retry API multiple times
- RSS feeds (`https://rss.arxiv.org/rss/quant-ph`) work when API is blocked — useful for category browsing
