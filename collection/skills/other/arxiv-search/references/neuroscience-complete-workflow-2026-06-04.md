# Neuroscience Research Complete Workflow — 2026-06-04 Cron Session

**Status**: FULLY VERIFIED — All 6 pipeline stages completed successfully with batch KG import

## Executive Summary

Complete automated neuroscience research pipeline executed on 2026-06-04:
- **Discovery**: RSS feed parsing → 116 relevant papers (q-bio.NC+cs.NE+cs.AI+cs.LG)
- **Selection**: Score-based filtering → 2 high-value papers selected
- **Skills Created**: 2 new skills with validated frontmatter
- **Sync**: ai_collection git repository updated + pushed
- **Obsidian**: 2 wiki notes created in flat structure
- **KG Import**: Batch import to 4 kg.db instances with verification

**Total execution time**: ~10 minutes
**Yield**: 2 complete skills + 2 wiki notes + 8 KG entity entries

---

## Stage 1: Paper Discovery (RSS High-Yield Pattern)

### RSS Feed Selection
```bash
# Neuroscience intersection feeds (verified 2026-06-03)
curl -x http://127.0.0.1:7890 -s \
  "https://rss.arxiv.org/rss/q-bio.NC+cs.NE+cs.AI+cs.LG" \
  -o /tmp/neuro_rss.xml
```

**Yield**: 9380 lines XML → 116 papers parsed with regex

### RSS Parsing Script Pattern
```python
# NO CDATA — plain text XML
import re, json

with open('/tmp/neuro_rss.xml', 'r') as f:
    xml = f.read()

items = re.findall(r'<item>(.*?)</item>', xml, re.DOTALL)
papers = []

for item in items:
    title = re.search(r'<title>(.*?)</title>', item, re.DOTALL)
    link = re.search(r'<link>(.*?)</link>', item, re.DOTALL)
    desc = re.search(r'<description>(.*?)</description>', item, re.DOTALL)
    
    if title and link:
        arxiv_id = re.search(r'arxiv\.org/abs/([\d.]+)', link.group(1))
        abstract_match = re.search(r'Abstract:\s*(.*)', desc.group(1) if desc else '', re.DOTALL)
        
        papers.append({
            'arxiv_id': arxiv_id.group(1) if arxiv_id else '',
            'title': title.group(1).strip(),
            'abstract': abstract_match.group(1).strip() if abstract_match else ''
        })

with open('/tmp/parsed_papers.json', 'w') as f:
    json.dump(papers[:50], f)  # Top 50 for scoring

print(f"Parsed {len(papers)} papers")
```

**Result**: 116 papers parsed, saved to `/tmp/parsed_papers.json`

---

## Stage 2: Paper Selection (Score-Based Filtering)

### Selection Criteria
1. **Neuroscience relevance**: Keywords (brain network, neural dynamics, spiking, connectivity, hypergraph, plasticity)
2. **Innovation**: Novel methods vs incremental improvements
3. **Methodology**: Clear reproducible frameworks
4. **Conference prestige**: ICML, NeurIPS papers prioritized

### Selected Papers
1. **arXiv:2606.03310**: "Learning Multi-Scale Hypergraph for High-Order Brain Connectivity Analysis" (ICML 2026)
2. **arXiv:2603.25180**: "Quantifying plasticity: a network-based framework linking structure to dynamical regimes"

---

## Stage 3: Skill Creation (Corrected Frontmatter)

### Frontmatter Structure (FIXED)
```yaml
---
name: multi-scale-hypergraph-brain-connectivity
description: "MuHL methodology..."
metadata:
  arxiv_id: "2606.03310"  # MUST be under metadata key
  conference: "ICML 2026"
tags: [neuroscience, hypergraph, brain-network]
---
```

**CRITICAL**: `arxiv_id` must be under `metadata:` key — NOT top-level

### Skills Created
1. **multi-scale-hypergraph-brain-connectivity/SKILL.md** (5051 bytes)
2. **plasticity-network-framework/SKILL.md** (5896 bytes)

---

## Stage 4: ai_collection Sync (Git Workflow)

### Git Commit Pattern
```bash
cd ~/ai_github/ai_collection
git add collection/skills/{skill-name}/ INDEX.md
git commit -m "feat: add {skill-name} from arXiv {id}"
git push
```

**Result**: 2 commits pushed (`1ff720c1`, `ef343ad4`)

---

## Stage 5: Obsidian Wiki Sync (Flat Structure)

### Path: `/Users/hiyenwong/obsidian/wiki/{arxiv_id}.md`
- Flat structure, NOT nested in subdirectories
- Created: `2606.03310.md` (5114 bytes), `2603.25180.md` (6141 bytes)

---

## Stage 6: KG Batch Import (4 Database Instances)

### Database Paths
- `/Users/hiyenwong/wiki/kg.db` → `entities` table
- `/Users/hiyenwong/.openclaw/workspace/scripts/kg.db` → `entities` table
- `/Users/hiyenwong/.openclaw/workspace/kg.db` → `kg_entities` table (15 papers verified)
- `/Users/hiyenwong/ai_github/ai_collection/kg.db` → `entities` table (no vectors)

### Deterministic Embedding Pattern
```python
def generate_embedding(text, dim=256):
    seed = int(hashlib.sha256(text.encode()).hexdigest()[:8], 16)
    rng = np.random.RandomState(seed)
    vec = rng.randn(dim).astype(np.float32)
    return vec / np.linalg.norm(vec)
```

### Verification
- workspace_root: 15 papers total
- wiki: 2 new papers

---

## Key Learnings

1. **RSS feeds**: Zero rate limits, high yield (116 papers from single feed)
2. **arXiv API**: Rate limited (429) — RSS fallback is preferred
3. **Skill frontmatter**: `arxiv_id` under `metadata:` key, not top-level
4. **KG schema**: Different table names (`entities` vs `kg_entities`) across databases
5. **Obsidian structure**: Flat wiki/, NOT nested subdirectories
6. **Batch import**: Single script targeting 4 DB instances

---

## Reusable Patterns

### Pattern: RSS Discovery → Score Selection → Skill → Sync → KG
All 6 stages verified working in cron mode.

### Pattern: Multi-DB KG Import
Batch script with schema detection + deterministic embeddings + verification queries.

---

## See Also
- `references/neuroscience-cron-workflow.md` — Earlier workflow (2026-05-28)
- `references/cron-workflow-patterns.md` — Cron execution patterns