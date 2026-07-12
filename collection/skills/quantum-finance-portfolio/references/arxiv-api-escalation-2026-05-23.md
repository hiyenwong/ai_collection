# arXiv API Escalation (2026-05-23)

## Current Status
The arXiv API is now **completely unusable** from cron/sandbox sessions. HTTP 429 is returned on the VERY FIRST request — even via `urllib.request` which previously succeeded for one call per session.

## What No Longer Works
- `urllib.request` — 429 on first request (was working for 1 request)
- `httpx` with proxy — 429 immediately
- `web_search` (Firecrawl backend) — `'NoneType' object has no attribute 'status_code'` in cron sessions
- Retry patterns (wait 10s, change User-Agent) — all fail

## What Still Works
1. **Browser search on arxiv.org** — MOST RELIABLE. Use `browser_navigate` with the search URL pattern:
   ```
   https://arxiv.org/search/?searchtype=all&query=<url_encoded_query>&start=0&order=-announced_date_first
   ```
   Extract data via `browser_console` JavaScript querying the DOM.
   
2. **Local kg.db queries** — 1440+ entities with full metadata.
   ```sql
   SELECT id, title, content, category FROM kg_entities 
   WHERE title LIKE '%quantum%' AND title LIKE '%finance%'
   ORDER BY published_date DESC LIMIT 10;
   ```

3. **Browser category pages** — for browsing new submissions:
   ```
   https://arxiv.org/list/q-fin.PM/new  (Portfolio Management)
   https://arxiv.org/list/quant-ph/new  (Quantum Physics)
   ```

## Recommendation
Do NOT attempt arXiv API calls in cron jobs. Start directly with browser search. This is not a transient issue — it has been escalating since 2026-05-20 and is now consistent.
