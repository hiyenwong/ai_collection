# Web Search + Browser Navigate Fallback (Verified 2026-05-30)

## Session Context
Cron job searching for neuroscience papers. All primary methods failed:
- RSS feeds: Rate limited or connection errors
- arXiv API: 429 "Rate exceeded" via proxy
- `browser_navigate` to category listings: 60s timeouts
- `web_search` with `site:arxiv.org`: NoneType errors

## Verified Working Pattern

### Discovery Phase
```python
# Use web_search with broad keywords (NOT site:arxiv.org)
results = web_search(query="neuroscience brain network spiking neural network computational neuroscience 2026")

# Extract arxiv URLs from results
arxiv_urls = [r['url'] for r in results['data']['web'] if 'arxiv.org' in r['url']]
```

### Paper Detail Extraction
Two working approaches:

**Approach A: browser_navigate to arXiv search UI**
```
browser_navigate("https://arxiv.org/search/?query=neuroscience+spiking&searchtype=all&start=0&order=-submitted_date")
browser_snapshot(full=false)  # Parse IDs from snapshot
```

**Approach B: browser_navigate to individual paper pages**
```
browser_navigate("https://arxiv.org/abs/2605.22523")
browser_snapshot(full=true)   # Abstract in <blockquote>
```

**Key insight**: Individual paper pages (`arxiv.org/abs/{id}`) load reliably (~10-15s). Category listing pages (`arxiv.org/list/{cat}/recent`) may timeout.

### Session Outcome
Successfully processed 2 neuroscience papers:
- arXiv:2605.22523 — "Learning sequence timing and control of replay speed" (sTM model)
- arXiv:2604.05251 — "Lattice Field Theory for a network of real neurons" (LFT framework)

Both skills created, synced to ai_collection, Obsidian notes written, kg.db updated.

## Lessons Learned

1. **web_search works** for arXiv discovery when used with broad keywords, not `site:` operator
2. **browser_navigate to paper pages** (`/abs/{id}`) is reliable — listing pages are unreliable
3. **Fallback chain is non-linear** — skip failing tiers, jump to whatever works
4. **Pivot is valid** — session had months of accumulated skills; new discovery is incremental

## When to Use This Pattern

- RSS feeds return connection errors or empty results
- arXiv API returns 429 or SSL errors through proxy
- `browser_navigate` to listing pages hangs (60s timeout)
- Urgent cron job deadline — cannot wait for rate limit cooldown

## Anti-Patterns to Avoid

- Do NOT retry failing methods multiple times (burns time, may hit rate limits harder)
- Do NOT assume `site:arxiv.org` in web_search will work
- Do NOT wait for browser listing page loads that consistently timeout
- Do NOT skip kg.db pivot option when all external access fails