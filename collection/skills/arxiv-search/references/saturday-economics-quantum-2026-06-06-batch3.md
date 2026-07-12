# Saturday Economics/Quantum Pipeline — 2026-06-06 Batch 3

## Context

Saturday cron run with topic: Economics/Investment + daily Quantum Mechanics.

## Discovery Results

- **RSS arxiv**: 0 items (Saturday skipDays — expected)
- **arxiv API (browser)**: "Rate exceeded" — both browser_navigate and terminal curl blocked
- **arxiv API (terminal urllib)**: Timeout on all 3 queries
- **Crossref API**: ✅ 15 papers returned, 10 with "quantum" in title/abstract

## Crossref Fallback Pattern (Confirmed 2026-06-06)

When arxiv is rate-limited (both RSS and API), Crossref API provides reliable fallback:

```python
url = "https://api.crossref.org/works?query=quantum+portfolio+OR+quantum+finance+OR+quantum+trading+OR+qaoa+portfolio&filter=from-pub-date:2026-01-01&rows=15&select=title,abstract,author,published,DOI,link"
req = urllib.request.Request(url, headers={'User-Agent': 'ResearchBot/1.0'})
resp = urllib.request.urlopen(req, timeout=20)
data = json.loads(resp.read().decode('utf-8'))
items = data.get('message', {}).get('items', [])
```

**Key findings**:
- Crossref returns papers with DOIs (not arxiv IDs)
- Abstracts are often HTML-encoded (`<jats:p>...</jats:p>`) or empty
- Some results are book chapters (e.g., `10.1002/9781394347070.ch16` — Wiley book chapter)
- SSrn preprints common (e.g., `10.2139/ssrn.6293058`)
- Quality varies more than arxiv — more filtering needed

## Papers Found (Top Crossref Results)

| DOI | Title | Quantum? |
|-----|-------|----------|
| 10.1002/9781394347070.ch16 | Quantum Machine Learning Model for Finance | ✅ Book chapter |
| 10.1016/j.qref.2026.102140 | Portfolio optimization with mean-variance-spectrum preferences |  Pure finance |
| 10.2139/ssrn.6293058 | Portfolio Selection is More of a Belle Art Than Economics or Finance | ❌ Pure finance |
| 10.1016/j.iref.2026.105244 | Robust investment portfolio management... Bayesian neural networks |  Pure finance |
| 10.2139/ssrn.6529019 | AI-Driven Quantitative Trading System for Portfolio Optimization | ❌ Pure finance |

**Note**: Only 1 out of 15 Crossref results was genuinely quantum+finance. The rest are pure finance/investment papers. This is a lower yield than arxiv RSS on weekdays.

## INDEX.md Pitfall: Crossref Papers Have Minimal Entries

When creating INDEX.md entries from Crossref papers (not arxiv):
- No arxiv ID available — use DOI as identifier
- Abstracts are often empty or HTML-encoded
- Skill descriptions may be minimal (just title, no abstract-based key points)
- **Fix**: When creating skills from Crossref papers, manually write richer descriptions since auto-extraction from HTML abstracts is unreliable

## Lessons

1. **Saturday Crossref yield is lower than weekday arxiv RSS**: Only ~7% of Crossref results were genuinely quantum+finance vs. ~30-40% from arxiv RSS on weekdays
2. **Crossref abstracts need HTML stripping**: `<jats:p>` tags common — use `re.sub(r'<[^>]+>', '', abstract)` before processing
3. **Book chapters in Crossref**: Crossref returns book chapters (Wiley, Springer) that arxiv RSS doesn't — these may have less novel methodology
4. **arxiv rate limiting is severe on Saturday**: Both browser and terminal blocked simultaneously — Crossref is the only reliable fallback
