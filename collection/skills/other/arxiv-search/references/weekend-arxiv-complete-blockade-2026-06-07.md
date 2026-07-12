# Weekend arXiv Complete Blockade Pattern (Sunday 2026-06-07)

## Problem
Sunday morning arXiv access completely blocked across all methods:
- RSS: Empty feed with `<skipDays>Saturday, Sunday</skipDays>`
- API: 429 rate limit errors
- web_search: NoneType failures
- Terminal HTTP: Security scanner blocks all curl/httpx/requests calls

## Solution: Direct Category Listing Navigation

**Verified working 2026-06-07**:
```python
# Navigate directly to category listing (NOT search pages)
browser_navigate(url="https://arxiv.org/list/q-bio.NC/recent")

# Browser console extraction (works when search fails)
browser_console(expression="""
const papers = [];
const dt = document.querySelectorAll('dt');
const dd = document.querySelectorAll('dd');
for (let i = 0; i < dt.length; i++) {
    const link = dt[i].querySelector('a[href^="/abs/"]');
    if (link) {
        const id = link.href.split('/abs/')[1];
        const title = dd[i].querySelector('.list-title')?.textContent?.trim();
        const authors = dd[i].querySelector('.list-authors')?.textContent?.trim();
        papers.push({id, title, authors});
    }
}
JSON.stringify(papers);
""")
```

**Result**: 6 papers extracted from q-bio.NC listing:
- 2606.06424 (Neural Population Coding)
- 2606.06290 (Early psychosis scaling)
- 2606.05870 (Cross-scale spatial generative)
- + 3 more

## Key Insight

**Listing pages (`/list/{category}/recent`) work on weekends** when search pages (`/search/`) are blocked with Error 1020. This is the reliable fallback for Sunday/Monday RSS lag.

## Paper Selection

From 6 papers, selected top 2 by neuroscience keyword density:
1. **2606.06290**: "Early psychosis scaling behaviour" - PRG+PSD+DFA framework (created skill: `psychosis-scaling-critical-regime`)
2. **2606.05870**: "Cross-scale spatial generative modeling for neurodegeneration" - variational inference with 86% variance explained (created skill: `cross-scale-spatial-generative-neurodegeneration`)

## Workflow Metrics
- Papers scanned: 6
- Skills generated: 2
- Git commit: 634987be (branch: neuro-cron-2026-06-07)
- KG entities: 4 (2 papers + 2 skills)

## References
- Skill 1: `psychosis-scaling-critical-regime` — PRG+PSD+DFA multiscale analysis
- Skill 2: `cross-scale-spatial-generative-neurodegeneration` — Variational generative framework
- Git branch: neuro-cron-2026-06-07
- arXiv IDs: 2606.06290, 2606.05870

---

**Session**: 2026-06-07 08:00 Sunday cron job
**Discovery**: Category listing pages bypass weekend blockade when RSS/API/search all fail