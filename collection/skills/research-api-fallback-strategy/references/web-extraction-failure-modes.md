# Web Extraction & Search Failure Modes — Observed 2026-05-11

## Failure Mode 1: web_search `NoneType` Crash

**Symptom**: `web_search()` returns `{'error': "Error searching web: 'NoneType' object has no attribute 'status_code'"}` consistently across all queries.

**Root cause**: The underlying HTTP client object is `None` — likely a configuration or credential issue with the search provider. Not a network timeout or rate limit.

**Detection**: Error mentions `NoneType` + `status_code` — this is distinct from timeout or rate-limit errors.

**Action**: Do not retry the same query — it will fail identically. Pivot to:
- `terminal` + `curl` for direct HTTP requests
- `browser_navigate` for JS-rendered pages (but see Failure Mode 3)
- Filesystem analysis of existing knowledge base

---

## Failure Mode 2: web_extract Proxy Connection Refused

**Symptom**: `web_extract()` returns `HTTPConnectionPool(host='localhost', port=5001): Max retries exceeded with url: /v2/scrape (Caused by NewConnectionError("[Errno 61] Connection refused"))`

**Root cause**: The web extraction proxy service (running on localhost:5001) is not running or crashed. This is a local infrastructure failure, not a remote site issue.

**Detection**: Error mentions `localhost`, `port=5001`, `Connection refused`, `Errno 61`.

**Action**: 
- Fall back to `terminal` + `curl` with proper headers
- Or `browser_navigate` for JavaScript-rendered content
- Do not retry web_extract until proxy is confirmed running

---

## Failure Mode 3: Browser Cloudflare Managed Challenge

**Symptom**: `browser_navigate` to research sites returns page title "Just a moment..." with Cloudflare challenge iframe. Even headless browsers get blocked.

**Sites affected**: openai.com/research/, openai.com/blog, and other Cloudflare-protected sites.

**Action**:
- This cannot be bypassed with standard browser automation
- For RSS feeds: also blocked (same Cloudflare challenge)
- Only viable approaches: Firecrawl API (if configured with residential proxies) or Google search for `site:` queries
- If all extraction fails, fall back to filesystem verification of existing knowledge base

---

## Cross-Check: INDEX.md vs Filesystem Count Mismatch

**Issue**: INDEX.md reported `总文章数: 60` but the actual script only checked 20 known articles against the Obsidian directory. There are actually 60 `.md` files on disk (excluding INDEX.md), but the script's hardcoded article list only contains 20 entries.

**Lesson**: When the fetcher script uses a static article list rather than dynamically discovering new articles (due to Cloudflare blocking), it cannot detect articles outside that list. INDEX.md stats may become misleading if the static list and filesystem diverge.

**Fix for future runs**: After checking the known list, also do a filesystem scan (`ls -1 *.md | wc -l`) to detect files created outside the script's awareness. Report both counts: "known articles checked" vs "total files on disk".
