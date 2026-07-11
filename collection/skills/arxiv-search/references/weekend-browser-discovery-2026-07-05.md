# arxiv-search: Weekend & Browser Discovery Notes (2026-07-05)

## arxiv.org advanced search returns 400
**Problem**: Navigating to arXiv advanced search URLs (`/search/advanced?...` or `/search/?query=...`) returns 400 Bad Request. Simple list/browse URLs (`/list/quant-ph/recent`) work fine.

**Fix**: Use `/list/{category}/recent` for browsing (e.g., `/list/quant-ph/recent`). For paper details, use `/abs/{id}` or `/html/{id}`. Avoid the advanced search URL pattern with query parameters — it consistently 400s in browser mode.

## RSS feeds empty on weekends
**Problem**: `curl -sL "https://rss.arxiv.org/rss/quant-ph"` returns an empty channel on Saturdays and Sundays. arXiv RSS feeds have `<skipDays><day>Saturday</day><day>Sunday</day></skipDays>` — no content published weekends.

**Fix**: On weekends, rely on `browser_navigate` to `/list/{category}/recent` for paper discovery, or use kg.db as the primary source. RSS is only productive Monday-Friday.

## Reliable browser URL patterns
- ✅ `/list/{category}/recent` — browse recent papers
- ✅ `/abs/{id}` — paper abstract page
- ✅ `/html/{id}` — HTML version (if available)
- ❌ `/search/advanced?...` — 400 Bad Request
- ❌ `/search/?query=...&searchtype=...` — 400 Bad Request
