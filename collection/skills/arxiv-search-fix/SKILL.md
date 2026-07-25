---
name: arxiv-search-fix
description: Workaround for arxiv-search SSL issues when using python httpx
category: ai_collection
---

# arxiv-search-fix

## Problem
The arxiv-search skill's internal httpx method fails with SSL errors:
```
[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1032)
```
This happens both with and without the HTTP proxy.

## Solution
Use curl with the HTTP proxy explicitly as shown below. This bypasses the problematic httpx usage.

```bash
curl -x http://127.0.0.1:7890 -G "https://export.arxiv.org/api/query" \
  --data-urlencode "search_query=all:\"neuroscience\" AND submittedDate:[202607150000 TO 202607162359]" \
  --data-urlencode "start=0" \
  --data-urlencode "max_results=50"
```

Replace the search query and date range as needed.

## Usage
When the arxiv-search skill fails due to SSL errors, fall back to the above curl command to fetch arXiv API results directly.

## Extended Guidance for Automated Workflows

For scheduled cron jobs and automated research pipelines, consider these additional strategies:

### Rate Limiting Mitigation
- **Category-based queries**: Use `cat:q-bio.NC OR cat:cs.NE` instead of keyword searches to reduce request complexity
- **Exponential backoff**: Implement delays between retry attempts (start with 30s, double each retry)
- **Local fallback**: Check existing local repository INDEX.md files when live fetching fails
- **Publishing cycles**: Account for academic publishing patterns (fewer papers on weekends/holidays)

### Security and Environment Compliance
- **Always use HTTPS**: Plain HTTP requests may be blocked by security scanners
- **Explicit proxy configuration**: Include `-x http://proxy:port` or set `http_proxy`/`https_proxy` env vars
- **Cron job constraints**: In scheduled contexts, `execute_code` is typically disabled; rely on terminal-based approaches

### Monitoring Strategy
- **Multi-source verification**: Cross-check results across different query methods
- **Graceful degradation**: Design workflows that can proceed with partial data when full retrieval fails
- **Error pattern recognition**: Distinguish between transient errors (retryable) and systematic failures (require workflow changes)