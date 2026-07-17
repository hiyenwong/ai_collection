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