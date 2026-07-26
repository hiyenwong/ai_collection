# Multi-Tool Failure Recovery Pattern (2026-05-13)

## Observed Failure Cascade

When multiple external-facing tools fail simultaneously, the following cascade was observed:

| Tool | Error | Root Cause |
|------|-------|------------|
| `web_search` | `'NoneType' object has no attribute 'status_code'` | Local proxy/search service unreachable |
| `web_extract` | `Connection refused (localhost:5001)` | Firecrawl service not running |
| `browser_navigate` | Timeout after 60s | Browser tool unresponsive |
| `curl` to arXiv | "Rate exceeded." | arXiv API aggressive rate limiting |

## Recovery Strategy: Fall Through to Knowledge Graph

When the above cascade occurs, the **knowledge graph (kg.db)** becomes the primary research data source:

```python
import sqlite3

conn = sqlite3.connect("/Users/hiyenwong/.openclaw/workspace/kg.db")
c = conn.cursor()

# Direct SQL queries replace failed web searches
c.execute("""
    SELECT id, title, content, url, published_date 
    FROM kg_entities 
    WHERE (title LIKE '%quantum%' OR content LIKE '%quantum%')
    AND (title LIKE '%medical%' OR content LIKE '%medical%')
    ORDER BY published_date DESC, id DESC
    LIMIT 10
""")

# kg_tool CLI works for these commands:
# - stats: Entity/vector/relation counts
# - pagerank: Top entities by importance
# - search: Keyword-based search (limited matching)
# - generate-embeddings: For entities without vectors

# AVOID: kg_tool communities (crashes beyond community 2)
```

## Key Insight

The research pipeline remains functional even when ALL external tools fail, as long as:
1. The knowledge graph has been populated with recent papers
2. Direct SQLite queries can be used for filtering
3. `kg_tool pagerank` identifies the most important papers
4. Existing skills provide implementation patterns

This pattern has been verified across multiple cron sessions (2026-05-13 and earlier).
