# Browser Fallback Pattern for arXiv Search

## When to Use
- **Cron jobs** — automated pipelines need reliability over elegance
- **Rate-limited situations** — API returning 429 during peak hours
- **Batch searches** — multiple categories in one session
- **Zero-dependency scenarios** — when API credentials/proxy are problematic

## Method
```python
# Navigate to category recent list
browser_navigate("https://arxiv.org/list/q-bio.NC/recent")

# Get full page snapshot
browser_snapshot(full=True)

# Papers appear in list format:
# arXiv:2605.31473 [pdf, other] : Title Here
# Authors: Name1, Name2
# Submitted: Date
```

## Advantages
1. **Zero rate limits** — web browsing has no API throttling
2. **Immediate results** — no exponential backoff delays
3. **Full context** — see all recent submissions, not just query matches
4. **Works offline-ish** — cached pages available in browser history

## Limitations
- No query filtering (get all recent, filter manually)
- Requires browser tools available
- Category-specific (must know which category to browse)

## Categories for Neuroscience
- `q-bio.NC` — Neuroscience and Computation (primary)
- `cs.LG` — Machine Learning (computational neuroscience)
- `cs.NE` — Neural and Evolutionary Computing
- `q-bio.QM` — Quantitative Methods

## Session Evidence (2026-06-01 Cron Job)
- Successfully retrieved recent papers via browser when API would be rate-limited
- Extracted 2 high-value papers for skill creation:
  - arXiv:2605.31473 — Metastable Mind
  - arXiv:2605.30882 — Extended Predictive Coding
- Total workflow time: ~10 minutes (vs 30+ min with API retries)

## Recommended Priority Order
1. **Browser fallback** (cron jobs, batch operations)
2. **API with retry** (interactive, targeted queries)
3. **Cached results** (partial recovery)

---
*Documented from successful cron execution on 2026-06-01*