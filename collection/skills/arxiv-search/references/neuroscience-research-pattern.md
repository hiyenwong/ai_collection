# Neuroscience Paper Research Pattern (Verified 2026-05-21)

## Multi-Query API Search Strategy

When searching across multiple neuroscience categories simultaneously:

```python
import urllib.request, ssl, xml.etree.ElementTree as ET
from urllib.parse import quote

queries = [
    'all:"neural dynamics" cat:q-bio.NC',
    'all:"brain network" cat:q-bio.NC',
    'all:"spiking neural" cat:cs.NE',
    'all:"computational neuroscience" cat:q-bio.NC',
]

for query in queries:
    encoded_query = quote(query)  # REQUIRED — arXiv API rejects unencoded spaces
    url = f'http://export.arxiv.org/api/query?search_query={encoded_query}&sortBy=submittedDate&sortOrder=descending&max_results=3'
    # Parse with ET...
```

## Browser-Based Multi-Category Scanning (Verified 2026-05-25)

When the arXiv API returns 429 for neuroscience-specific categories (q-bio.NC, cs.NE) but works for cs.LG, use this tiered approach:

### Tier 1: Category listing pages (zero rate limits)
Navigate to each category's `/new` listing page via `browser_navigate`. The snapshot includes:
- **New submissions**: papers submitted directly to this category
- **Cross-lists**: papers from other categories cross-listed here
- **Replacements**: updated versions of existing papers
- Full abstracts for most entries

```python
# Categories to check for neuroscience research:
# q-bio.NC -> https://arxiv.org/list/q-bio.NC/new
# cs.NE  -> https://arxiv.org/list/cs.NE/new
# cs.LG  -> https://arxiv.org/list/cs.LG/new
```

### Tier 2: Individual paper details
```python
# Navigate to arxiv.org/abs/{id} for full metadata:
# - Abstract: <blockquote class="abstract mathjax">
# - Authors: linked author names
# - Categories: in the Subjects table cell
# - Submit date: [Submitted on DD Month YYYY]
```

### Tier 3: API supplementation (when it works)
`cs.LG` queries via urllib + proxy + SSL bypass tend to succeed (max_results=25) even when `q-bio.NC` and `cs.NE` get 429'd. Use for bulk text search across categories.

### Skill duplicate check before creation
Before creating skills for discovered papers, scan ALL skill directories (not just ai_collection):
```bash
grep -rl "{arxiv_id}" ~/.hermes/skills/*/SKILL.md 2>/dev/null
grep "{arxiv_id}" ~/ai_github/ai_collection/INDEX.md 2>/dev/null
# Also check by title keywords across all category dirs
grep -ril "keyword" ~/.hermes/skills/*/ 2>/dev/null
```

The SpikingMoE paper (arXiv:2605.23188) already had skill `spikingmoe-sdprompt-snn` in `ai_collection` — always scan all category directories.

## Key Verified Findings (2026-05-21)

### urllib.request + SSL bypass + proxy = MOST RELIABLE
```python
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
proxy_handler = urllib.request.ProxyHandler({'http': 'http://127.0.0.1:7890', 'https': 'http://127.0.0.1:7890'})
opener = urllib.request.build_opener(proxy_handler)
urllib.request.install_opener(opener)

url = 'http://export.arxiv.org/api/query?search_query=cat:q-bio.NC&sortBy=submittedDate&max_results=25'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'})
resp = urllib.request.urlopen(req, timeout=60, context=ctx)
```

### web_search (Firecrawl) NoneType Error
Returns `'NoneType' object has no attribute 'status_code'` — transient Firecrawl infrastructure failure. Immediately fall back to browser or API. Do NOT retry web_search multiple times.

### kg.db Sync Pattern (Verified Schema 2026-05-21)

The main kg.db at `~/.hermes/kg.db` has schema:

```sql
CREATE TABLE papers (
    arxiv_id TEXT PRIMARY KEY,
    title TEXT,
    authors TEXT,
    skill TEXT,
    date_added TEXT
);
CREATE TABLE paper_tags (
    paper_id TEXT,
    tag TEXT,
    FOREIGN KEY(paper_id) REFERENCES papers(arxiv_id)
);
CREATE TABLE sessions (
    id TEXT PRIMARY KEY,
    date TEXT,
    papers_scanned INTEGER,
    new_skills INTEGER,
    coverage_rate REAL,
    notes TEXT
);
CREATE TABLE entities (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    attributes TEXT,
    created_at TEXT,
    last_accessed TEXT,
    importance_score REAL DEFAULT 0.5
);
CREATE TABLE relations (
    id TEXT PRIMARY KEY,
    source_id TEXT NOT NULL,
    target_id TEXT NOT NULL,
    relation_type TEXT,
    strength REAL,
    created_at TEXT
);
```

**Correct insert patterns:**
```python
# Add paper
cursor.execute(
    "INSERT OR REPLACE INTO papers (arxiv_id, title, authors, skill, date_added) VALUES (?, ?, ?, ?, datetime('now'))",
    (paper_id, title, authors, skill_name)
)

# Add entity (for graph queries)
import json
cursor.execute(
    "INSERT OR IGNORE INTO entities (id, name, type, attributes, created_at, importance_score) VALUES (?, ?, 'paper', ?, datetime('now'), 0.8)",
    (paper_id, title, json.dumps({"arxiv_id": arxiv_id, "categories": cats, "authors": authors, "skill": skill_name, "url": url}))
)

# Add relationship between related papers
cursor.execute(
    "INSERT INTO relations (source_id, target_id, relation_type, strength, created_at) VALUES (?, ?, 'related_topic', 0.6, datetime('now'))",
    (paper_id_1, paper_id_2)
)

# Record session
cursor.execute(
    "INSERT INTO sessions (id, date, papers_scanned, new_skills, coverage_rate, notes) VALUES (?, ?, ?, ?, ?, ?)",
    (session_id, date_str, scanned_count, new_count, coverage_rate, notes)
)
```

⚠️ There are ~12 kg.db files scattered across `~/.hermes/` subdirectories. The canonical one for paper tracking is `~/.hermes/kg.db` (has `papers` + `entities` + `relations` + `sessions` tables). Do NOT accidentally use the `workspace/scripts/kg.db` or `data/kg.db` which have different schemas.**

### Browser Console Listing Extraction (Verified 2026-05-21)

The fastest way to extract all papers from a category listing page in one shot (no scrolling, no snapshot parsing):

```javascript
(() => {
  const dts = document.querySelectorAll('dt');
  const dds = document.querySelectorAll('dd');
  const results = [];
  for (let i = 0; i < Math.min(dts.length, 50); i++) {
    const dt = dts[i];
    const dd = dds[i];
    const link = dt.querySelector('a[href*=\"/abs/\"]');
    const id = link ? link.textContent.trim().split('[ ').pop().split(' ]')[0].trim() || link.textContent.trim().replace('arXiv:', '') : '';
    const titleText = dd ? dd.firstChild.textContent.trim() : '';
    if (id && titleText) results.push(id + ': ' + titleText);
  }
  return results.slice(0, 50).join('\n');
})()
```

Use via `browser_console(expression=...)` after navigating to `https://arxiv.org/list/{category}/recent`. Returns `id: title` lines for up to 50 papers. Much faster than iterating over browser_snapshot elements. For full abstracts, navigate to individual abs pages afterward.

### Duplicate Skill Naming
Cron jobs may create skills with slightly different names. Always check for near-duplicates:
```bash
ls ~/.hermes/skills/ai_collection/ | grep -i "{keyword}"
```
Clean up duplicates after creation.
