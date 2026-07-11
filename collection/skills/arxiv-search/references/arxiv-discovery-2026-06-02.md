# arXiv Discovery Patterns — 2026-06-02 Session Findings

## API Failure Mode: Plain Text "Rate exceeded." (not HTTP 429)

When using `curl -s --noproxy "*" "https://export.arxiv.org/api/query?..."`, the API returns the plain text string `Rate exceeded.` (14 bytes) — NOT an HTTP 429 with JSON. This is a hard rate limit that doesn't recover within seconds. Even `sleep 4` and `sleep 10` between requests still gets rate-limited.

**Detection**: `wc -c` returns 14 and `cat` shows `Rate exceeded.`

**Immediate pivot**: Browser category listing (`https://arxiv.org/list/cs/new`) works immediately with zero rate limits.

## Browser Extraction: Scan `main.innerText` Instead of DOM Selectors

The documented JS selector patterns (`document.querySelectorAll('li.arxiv-result')`, `#content dl dt`) may not match current arXiv HTML structure. Instead of fighting DOM selectors:

```javascript
// Reliable: scan full text of main content area
const allText = document.querySelector('main')?.innerText || '';
const lines = allText.split('\n').filter(l => l.trim());
const quantumLines = lines.filter(l => /quantum|quant-ph|QASM|qubit/i.test(l));
// Returns context-rich lines including titles, abstracts, subjects
```

This approach:
- Works regardless of HTML structure changes
- Returns titles, abstracts, subject categories in one pass
- No selector debugging needed
- Returns 30+ lines of context for keyword-filtered results

## web_extract Failure: Firecrawl Connection Refused

`web_extract` failed with `HTTPConnectionPool(host='localhost', port=5001): Connection refused` — the local firecrawl service wasn't running. This is different from the documented "private/internal network" blocking. When firecrawl is down, `web_extract` fails silently on all URLs.

**Pivot**: Use `browser_navigate` for individual paper pages or rely on browser-scraped abstracts from category listings.
