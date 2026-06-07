# Dual-Keyword Scoring for Cross-Domain arXiv Discovery

## Scoring Formula (Verified 2026-06-05)

When discovering papers at the intersection of two domains (e.g., Systems Engineering + Quantum), use **weighted dual-keyword scoring** rather than requiring both keyword sets to match:

```python
score = count(domain_A_keywords) + 2 * count(domain_B_keywords)
```

The **2× multiplier** on the narrower/more specific domain (quantum) ensures papers that strongly match both domains are ranked highest, while papers that heavily match only the broader domain (systems engineering) still get moderate scores.

## Why This Matters

- Simple boolean matching (requires BOTH quantum AND syseng keywords) yields **too few results** for sparse intersections
- Simple union matching (requires EITHER) yields **too many irrelevant results**
- Weighted scoring creates a **continuous relevance spectrum** — papers scoring ≥7 are high-relevance, ≥5 are moderate, ≥3 are borderline

## Browser Extraction Pattern (Verified 2026-06-05)

```javascript
var results = document.querySelectorAll('li.arxiv-result');
var papers = [];
results.forEach(function(item) {
  var idLink = item.querySelector('p:first-of-type a');
  var id = idLink ? idLink.textContent.trim() : '';
  var titleEl = item.querySelectorAll('p');
  var title = titleEl[1] ? titleEl[1].textContent.trim() : '';
  var authors = item.querySelector('p:nth-of-type(3)');
  var auth = authors ? authors.textContent.replace('Authors:', '').trim() : '';
  if (id && id.length > 5) {
    papers.push({id: id, title: title, authors: auth});
  }
});
JSON.stringify(papers.slice(0, 30));
```

**Important**: On arXiv search results pages (NOT category listing pages), `p:nth-of-type(3)` contains authors. On category listing pages, the structure differs. Always verify the HTML structure before using positional selectors.

## Yield Results

Using `query=quantum+systems+engineering+OR+quantum+control+OR+quantum+error+correction`:
- 1,922 total results
- Top 30 extracted via browser console
- 12 papers scored ≥5 (moderate+ relevance)
- 4 papers scored ≥7 (high relevance)
- 3 new skills created from papers scoring ≥6
