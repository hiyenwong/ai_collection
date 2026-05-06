# arXiv Access Failure Modes (2026-05)

## Documented failure modes observed in production cron sessions

### 1. HTTP 429 Rate Limits (arXiv API)
- **Symptom**: `export.arxiv.org/api/query` returns 429 on ALL queries
- **Observed**: 2026-04, worsened 2026-05
- **Mitigation**: Skip API entirely; use browser navigation to category pages

### 2. web_extract "Blocked" (arXiv URLs)
- **Symptom**: `web_extract` returns "Blocked: URL targets a private or internal network"
- **Observed**: 2026-05, both `/abs/` and `/pdf/` URLs
- **Mitigation**: Use `browser_navigate` + `browser_snapshot` instead

### 3. httpx Empty Responses (in execute_code sandbox)
- **Symptom**: `httpx.get()` returns 0-byte response with no HTTP error
- **Observed**: 2026-05-02
- **Mitigation**: Never trust `httpx` response length < 100 for arXiv API; use `web_search` + `curl` fallback

### 4. curl HTTP vs HTTPS
- **Symptom**: `curl http://export.arxiv.org/api/query` triggers interactive security approval
- **Mitigation**: Always use `https://` prefix

### 5. JS Extraction Garbled (category listing pages)
- **Symptom**: `browser_console` JS on `/list/{category}/recent` produces garbled output
- **Cause**: dt/dd DOM structure differs from `/search/?query=...` pages
- **Mitigation**: Use `browser_snapshot(full=True)` text parsing for category pages

### 6. 400 Bad Request on Search URLs with + (2026-05-06)
- **Symptom**: `https://arxiv.org/search/?query=neuroscience+brain+network&...` returns **400 Bad Request**
- **Affected**: All multi-word keyword searches where spaces are encoded as `+`
- **Not affected**: Single-word queries, category listing pages, individual `/abs/` pages
- **Mitigation**: 
  - Use `%20` instead of `+` for spaces in search URLs
  - Prefer category listing pages (`/list/{category}/recent`) — fully reliable, pre-structured
  - Individual paper pages (`/abs/XXXX.XXXXX`) — fully reliable

## Recommendation hierarchy (most reliable → least)

1. ✅ **Category listing pages** (`/list/q-bio.NC/recent`, `/list/cs.NE/recent`) — always works
2. ✅ **Individual paper pages** (`/abs/XXXX.XXXXX`) — always works
3. ⚠️ **Search result pages** (`/search/?query=...`) — works with `%20` encoding, broken with `+`
4. ❌ **arXiv API** (`export.arxiv.org/api/query`) — 429 rate limited
5. ❌ **web_extract** — blocked for arXiv URLs
6. ❌ **httpx in execute_code** — empty responses
