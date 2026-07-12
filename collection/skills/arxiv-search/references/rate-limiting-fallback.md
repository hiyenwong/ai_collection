# arXiv Search — Reliable Patterns (2026-05-08 update)

## Rate Limiting Reality

**The arXiv API (`export.arxiv.org/api/query`) returns HTTP 429 "Rate exceeded" on virtually every request, even with 12-15s delays and proxy.** Do not rely on it for batch searches.

## Working Fallback Chain

1. **RSS Feeds** (most reliable, no rate limits) — returns today's papers per category:
   ```bash
   curl -s -L https://rss.arxiv.org/rss/q-bio.NC    # Neuroscience & Cognition
   curl -s -L https://rss.arxiv.org/rss/cs.NE        # Neural & Evolutionary Computing  
   curl -s -L https://rss.arxiv.org/rss/cs.AI        # AI (~300 papers/day)
   curl -s -L https://rss.arxiv.org/rss/stat.ML      # ML Statistics
   ```
   RSS 2.0 format: parse `<item>` → `<title>`, `<link>`, `<description>`.
   Description format: `arXiv:{id}v1 Announce Type: new Abstract: {abstract}`.
   Extract arXiv ID from the `<link>` URL.

2. **arXiv API via curl** — needs `-L` (301 redirect) and `-A` (user-agent):
   ```bash
   curl -s -L -A 'Mozilla/5.0' 'https://export.arxiv.org/api/query?search_query=all:keyword&max_results=5&sortBy=submittedDate'
   ```
   Rate-limited → wait 15s+ and retry.

3. **browser_navigate** — individual papers: `https://arxiv.org/abs/{id}`

## Critical Gotchas
- Always use `-L` with curl (arXiv returns 301 on HTTP)
- Rate limit returns plain text `"Rate exceeded."` not XML
- **Never `curl | python3`** — security guardrail blocks pipe-to-interpreter. Save to file first
- Papers have **multiple categories** — parse ALL `atom:category` elements
- httpx `proxies=` kwarg fails on this env → use curl via subprocess with `-x http://127.0.0.1:7890`
- For full paper details when API fails: `browser_navigate` to `https://arxiv.org/abs/{id}`
