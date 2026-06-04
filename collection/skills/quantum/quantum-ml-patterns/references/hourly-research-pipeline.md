# Hourly Research Cron Pipeline

## Overview
Automated research pipeline: topic rotation → arXiv search → KG import → analysis → skill creation.

## Step 1: Get Today's Topic
```bash
python3 scripts/weekly_topics.py
# Output: "Today is weekday N (DayName)\n今日主题: Topic\nToday's topic: Topic\nKeywords: ..."
# Day mapping: 0=Mon(Neuroscience), 1=Tue(CS), 2=Wed(Medicine), 3=Thu(Systems), 4=Fri(Math), 5=Sat(Econ), 6=Sun(Info)
# Daily: always quantum mechanics
```

## Step 2: Search arXiv
```python
# Use https://export.arxiv.org/api/query (NOT http:// — security blocks plain HTTP)
# Add 3.5s sleep between requests to avoid 429 rate limits
# Never pipe curl to python — save to file first

import httpx, time
def search_arxiv(query, max_results=5):
    for attempt in range(3):
        r = httpx.get("https://export.arxiv.org/api/query",
            params={"search_query": query, "max_results": max_results,
                    "sortBy": "submittedDate", "sortOrder": "descending"},
            timeout=30)
        if r.status_code == 429:
            time.sleep(5 * (attempt + 1))
            continue
        return parse_xml(r.text)
    return []
```

Recommended query combinations:
- `all:"quantum" AND (all:"medical" OR all:"healthcare")` — medicine+quantum intersection
- `cat:quant-ph` — quantum physics latest
- `all:"medical" AND all:"deep learning"` — medical AI latest
- `all:"quantum machine learning"` — quantum ML latest

## Step 3: Import to KG
```python
# Database: /Users/hiyenwong/.openclaw/workspace/scripts/kg.db
# Tables: entities(id, name, type, category, description, source, created_date)
#         kg_vectors(id, embedding)  # JSON array of floats
#         relationships(id, source, target, relation, description, created_date)
#         research_log(id, date, topic, arxiv_id, skill_name, summary, status)
# NOTE: There is NO kg_entities table — the table is called 'entities'.
# Type values: 'paper', 'skill', 'author', 'category', 'tag', 'abstract'

import sqlite3, struct, hashlib, math

def generate_embedding(text, dim=256):
    vector = []
    for i in range(dim):
        h = hashlib.md5(f"seed_{i}_{text}".encode()).hexdigest()
        val = (int(h[:8], 16) / 0xFFFFFFFF) * 2 - 1
        vector.append(val)
    norm = math.sqrt(sum(v*v for v in vector))
    return [v/norm for v in vector] if norm > 0 else vector

def vec_to_blob(vec):
    return struct.pack('256f', *vec)

# Dedup first: SELECT LOWER(TRIM(title)) FROM kg_entities
# Then INSERT entity → INSERT vector → CREATE relationships (keyword overlap > 5)
```

## Step 4: Analysis
- **PageRank**: Build adjacency from kg_relationships, damping=0.85, 50 iterations
- **Community detection**: Union-find with threshold weight > 0.3
- **Vector similarity**: Cosine similarity on 256-dim float32 vectors (note: hash-based, low scores 0.05-0.26)

## Step 5: Skill Creation
Analyze papers for reusable patterns → create SKILL.md at `/Users/hiyenwong/.hermes/skills/<name>/SKILL.md`
Focus on class-level patterns, not single-paper summaries.

## Pitfalls
- arXiv API returns 429 aggressively — sleep 3.5s minimum between requests
- Security guardrail blocks `curl | python3` — save to file first
- `web_search` tool blocks arxiv.org — use httpx in Python scripts instead
- kg_tool CLI operates on `~/wiki/kg.db` symlink — use raw SQLite for workspace kg.db
