# arXiv API Rate Limit Recovery (Verified 2026-06-05)

## Problem
arXiv API returns "Rate exceeded." in response body under high-frequency access, especially from cron jobs and proxy environments.

## Recovery Strategy

### 1. Sleep + Retry
```bash
sleep 10 && curl -s --noproxy "*" "https://export.arxiv.org/api/query?..."
```
Usually succeeds after 1-2 retries. The rate limit window is short (~10 seconds).

### 2. Query Narrowing
Broad queries hit rate limits faster. Use AND instead of OR:
- **BAD**: `all:quantum OR all:statistics OR all:learning` (triggers 1M+ results, heavy query)
- **GOOD**: `all:quantum+AND+all:statistics+AND+all:machine+learning` (1847 results, focused)

### 3. Sequential Delays
When running multiple queries, insert `sleep 5` between each. The arXiv API rate limit appears to be per-window, not per-request.

### 4. Direct HTTPS Without Proxy
In this environment, direct HTTPS (no proxy) was more stable than proxy-based access for arXiv.

## Working Pattern
```bash
# First attempt
curl -s --noproxy "*" "https://export.arxiv.org/api/query?search_query=all:quantum+AND+all:statistics+AND+all:learning&start=0&max_results=5&sortBy=submittedDate&sortOrder=descending"

# If "Rate exceeded." → wait 10s → retry
sleep 10 && curl -s --noproxy "*" "https://export.arxiv.org/api/query?search_query=all:quantum+AND+all:statistics+AND+all:learning&start=0&max_results=5&sortBy=submittedDate&sortOrder=descending"

# If still failing → narrow query further or use browser fallback
```

## Browser Fallback (Last Resort)
If API continues to fail after 3 retries, use browser_navigate to arXiv search page and extract results from HTML.
