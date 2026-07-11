# arXiv Browser Extraction Reference

Proven techniques for extracting paper data from arXiv using browser automation when all other methods fail.

## When to Use

- `web_search` returns `NoneType` error (tool infrastructure broken)
- `web_extract` blocks arxiv.org URLs
- Target site is Cloudflare-protected (openai.com, etc.)
- Need recent papers by organization/topic

## arXiv Search URL Patterns

### By keyword (all fields, newest first):
```
https://arxiv.org/search/?query=KEYWORD&searchtype=all&order=-submitted_date&start=0
```

### By specific phrase:
```
https://arxiv.org/search/?query=all:%22OpenAI%22&searchtype=all&order=-submitted_date&start=0
```

### Results per page: change `start=0` to `start=50`, `start=100`, etc.

## JavaScript Extraction Snippets

### Extract paper list from search results:
```javascript
(() => {
  const items = document.querySelectorAll('.arxiv-result');
  let results = [];
  for (const item of items) {
    const title = item.querySelector('p.title')?.textContent?.trim();
    const authors = item.querySelector('p.authors')?.textContent?.trim();
    const date = item.querySelector('p.is-size-7')?.textContent?.trim();
    const arxivLink = item.querySelector('p.list-title a')?.href || '';
    if (title) results.push({title, authors: authors?.substring(0,100), date, arxivLink});
  }
  return JSON.stringify(results, null, 2);
})()
```

### Filter by organization (e.g., OpenAI):
```javascript
(() => {
  const items = document.querySelectorAll('.arxiv-result');
  let results = [];
  for (const item of items) {
    const title = item.querySelector('p.title')?.textContent?.trim();
    const authors = item.querySelector('p.authors')?.textContent?.trim();
    const date = item.querySelector('p.is-size-7')?.textContent?.trim();
    if (authors?.includes('OpenAI') || title?.includes('OpenAI')) {
      results.push({title, date: date?.substring(0,50), authors: authors?.substring(0,80)});
    }
  }
  return JSON.stringify(results, null, 2);
})()
```

### Extract abstract from individual paper page:
```javascript
(() => {
  const abstract = document.querySelector('blockquote.abstract');
  return abstract ? abstract.textContent.trim() : 'not found';
})()
```

## Known Gotchas

1. **`arxiv.org/search/?query=au:OpenAI` returns no results** — arXiv doesn't index "OpenAI" as an author name. Use `all:OpenAI` or specific paper titles instead.
2. **`web_extract` blocks ALL arxiv.org URLs** — always use browser_navigate + browser_console, never web_extract for arXiv.
3. **Google/Bing may block automated searches** — DuckDuckGo works but may show empty results for some queries.
4. **arXiv search is case-sensitive for exact phrase matching** — use `%22` for quoted phrases in URLs.
