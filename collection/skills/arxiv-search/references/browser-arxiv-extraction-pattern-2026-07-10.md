# Reliable Browser Extraction Pattern for arXiv (2026-07-10)

## Problem
As of 2026-07-10, ALL non-browser methods for accessing arXiv are broken:
- `arxiv` Python package → times out (60s+)
- `curl` with proxy → "Rate exceeded" or SSL EOF
- `urllib.request` → SSL: UNEXPECTED_EOF_WHILE_READING
- `web_search` (Firecrawl) → NoneType error
- `web_extract` → "Blocked: URL targets a private or internal network address"
- `execute_code` → BLOCKED in cron mode

## Working Pattern: browser_navigate + browser_console

### Step 1: Browse the arXiv listing page
```
browser_navigate("https://arxiv.org/list/quant-ph/new")
```
This returns a snapshot with paper IDs, titles, authors, and categories.

### Step 2: Browse individual paper abstract pages
```
browser_navigate("https://arxiv.org/abs/2607.XXXXX")
```
The snapshot contains:
- Paper title (h1)
- Authors (links)
- Abstract (blockquote)
- Categories (Subjects row in metadata table)
- Submission date

### Step 3: Extract structured data via browser_console
For bulk extraction from listing pages:
```javascript
// After navigating to a category listing page
const dls = document.querySelectorAll('dl');
let results = [];
for (const dl of dls) {
  const terms = dl.querySelectorAll('dt');
  const defs = dl.querySelectorAll('dd');
  for (let i = 0; i < terms.length; i++) {
    const idEl = terms[i].querySelector('a');
    const id = idEl ? idEl.textContent.trim() : '';
    const text = defs[i].textContent;
    // Extract title, authors, subjects from text
    results.push({id, text});
  }
}
JSON.stringify(results.slice(0, 80));
```

### Step 4: Browse individual papers for full abstracts
```
browser_navigate("https://arxiv.org/abs/2607.07801")
```
The snapshot's blockquote contains the full abstract.

### Step 5: Cross-lists section
After the new submissions section, click the "Cross-lists" link to find papers that bridge multiple categories (e.g., quant-ph + math, quant-ph + stat).

## Important Notes
- browser_navigate on `https://arxiv.org/list/{category}/new` shows today's new submissions
- Categories to check for quantum + math crossover: `quant-ph`, `math-ph`, `stat.ME`, `math.ST`
- The "Cross-lists" link on quant-ph page reveals papers also classified under math/stat/physics
- Each page load is independent — no rate limiting issues with browser
- Snapshot truncation at ~8000 chars means listing pages may need scrolling (browser_scroll down)

## Efficiency Tip
For cron jobs where you need to find specific papers:
1. Navigate to the category listing
2. Scan the snapshot for interesting titles (title + category visible without clicking)
3. Only navigate to individual papers for abstracts of candidates
4. This minimizes browser calls (each one takes several seconds)
