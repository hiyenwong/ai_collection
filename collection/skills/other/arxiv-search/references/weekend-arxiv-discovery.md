# Weekend arXiv Discovery (Updated 2026-05-31)

**CONFIRMED**: arXiv RSS feeds return empty `<channel>` with zero items on weekends (Saturday + Sunday). The RSS header contains `<skipDays><day>Sunday</day><day>Saturday</day></skipDays>` confirming intentional skip.

## Sunday 2026-05-31 Session Evidence

- RSS feeds for neuroscience (`q-bio.NC`) and cross-domain categories returned empty XML
- **Browser fallback**: `browser_navigate("https://arxiv.org/list/q-bio.NC/recent")` returned structured paper listing
- Successfully extracted 2 neuroscience papers:
  - arXiv:2605.29677 — "Embodied Virtual Reality Feedback Reshapes Neural Representations"
  - arXiv:2605.28854 — "Large language models reorganize representational geometry during in-context learning"
- Full workflow completed: skill creation, ai_collection sync, Obsidian notes, kg.db import

## Verified Working Weekend Pattern

**Step 1**: Browser navigate to category recent listing
```
browser_navigate("https://arxiv.org/list/q-bio.NC/recent")
```
Returns structured text with paper IDs, titles, authors. Parse directly from snapshot.

**Step 2**: Navigate to individual papers for full details
```
browser_navigate("https://arxiv.org/abs/2605.29677")
```
Abstract in `<blockquote class="abstract mathjax">`, authors in `.authors` element.

**Step 3**: Extract paper metadata from browser snapshot

Snapshot format (parse directly):
```
arXiv:2605.29677 [pdf, other]
Title: Embodied Virtual Reality Feedback Reshapes Neural Representations for Continuous 3D Motor Imagery BCIs
Authors: Gao, Y., Wang, Z., et al.
Submitted: 27 May 2026
...
```

**Step 4**: Create skills, sync to ai_collection, push to GitHub
```bash
cd /Users/hiyenwong/ai_github/ai_collection
git add collection/skills/{skill-name}/ INDEX.md
git commit -m "feat: add {skill-name} (arXiv:{id})"
git -c http.proxy=http://127.0.0.1:7890 -c https.proxy=http://127.0.0.1:7890 push
```

**Step 5**: Import to Hermes kg.db with JSON attributes
```python
import sqlite3, json

attrs = {"arxiv_id": "2605.29677", "authors": [...], "categories": [...], "abstract": "..."}
conn = sqlite3.connect("/Users/hiyenwong/.hermes/kg.db")
c = conn.cursor()
c.execute("INSERT INTO entities (id, name, type, attributes, created_at) VALUES (?, ?, ?, ?, datetime('now'))",
    ("arxiv:2605.29677", title, "paper", json.dumps(attrs)))
conn.commit()
```

## Why Browser Works on Weekends

Browser navigation uses the arXiv web server's HTML rendering, which serves category listing pages 24/7. RSS feeds are explicitly disabled on weekends via `<skipDays>` configuration. The web server has no weekend restrictions.

## Alternative: kg.db Pivot

When browser navigation times out or fails:
```bash
sqlite3 /Users/hiyenwong/.hermes/kg.db "SELECT id, name, attributes FROM entities WHERE type='paper' LIMIT 20"
```
Work with existing indexed papers (36+ neuroscience papers as of 2026-05-31).

## Do NOT Retry RSS on Weekends

RSS empty is NOT a rate limit, timeout, or network error — it's **by design**. Retrying RSS on weekends wastes time. Pivot immediately to browser fallback or kg.db queries.

## Related References

- [neuroscience-cron-workflow.md](neuroscience-cron-workflow.md) — complete cron workflow
- [kg-db-schema-discovery-2026-05-31.md](kg-db-schema-discovery-2026-05-31.md) — Hermes kg.db schema verified
- [confirmed-curl-idlist-pattern.md](confirmed-curl-idlist-pattern.md) — alternative API pattern (may fail on weekends)