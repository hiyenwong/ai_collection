# arXiv 429 Persistence & Crossref Primary Fallback

## Status (2026-06-07)
arXiv API returns HTTP 429 persistently across ALL cron sessions. Not intermittent — completely blocked. Crossref API has become the primary reliable source for paper discovery.

## arXiv 429 Pattern
- **Affected**: All queries, with or without proxy
- **With proxy (127.0.0.1:7890)**: HTTP 429
- **Without proxy**: HTTP 429 or timeout
- **Duration**: Since at least 2026-06-01, confirmed every cron session through 2026-06-07

## Working Pattern: Crossref as Primary
```
https://api.crossref.org/works?query=TOPIC+KEYWORDS&filter=from-pub-date:2025-01-01&rows=5&select=title,abstract,author,published,DOI,link
```

- Returns JSON directly — no XML parsing
- Works without proxy
- Includes bioRxiv preprints, SSRN, IEEE, Elsevier, etc.
- Query format: Use `+` for spaces, e.g. `quantum+economics+finance+portfolio`

## DOI as Paper ID
When no arXiv ID is available, use the DOI as the `arxiv_id` field in SKILL.md frontmatter metadata:
```yaml
metadata:
  arxiv_id: "10.1109/nqcomp68334.2026.11497725"
```

All downstream tools work identically with DOIs:
- Duplicate `grep -rl` works with DOIs
- INDEX.md entries use DOIs
- kg.db URL: `https://doi.org/{doi}`

## Papers from 2026-06-07 scan (DOI-based)
| DOI | Paper |
|-----|-------|
| 10.1109/nqcomp68334.2026.11497725 | Quantum-Enhanced SVM for Financial Markets |
| 10.1155/que2/3418300 | Enhancing QAOA Through Manifold Optimization |
| 10.1109/tqe.2026.3654930 | Equivariant QAOA |
| 10.1016/j.iref.2026.105244 | Bayesian NN Portfolio Management |
| 10.21203/rs.3.rs-9178752/v1 | BioQPSO Hybrid Optimization |
