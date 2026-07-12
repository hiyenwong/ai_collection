# arXiv Research Cron Job — Session Notes & Verified Patterns

## 2026-05-14 Session Summary

### arXiv API Behavior Observed
- **Initial queries**: 429 errors on ALL queries (likely from previous cron runs)
- **After waiting ~60s**: Single broad query with 20 results succeeded
- **RSS feed**: Available at `https://rss.arxiv.org/rss/q-bio.NC` but requires XML parsing
- **Rate limit recovery**: 30+ seconds between batches is reliable; 5 seconds is NOT enough

### Working Query Pattern

```python
# SINGLE combined query to minimize API hits
combined_query = 'all:"neuroscience" OR all:"spiking neural network" OR all:"neural dynamics" OR all:"brain network"'

# Use httpx 0.28+ with transport-based proxy
proxy_transport = httpx.HTTPTransport(proxy="http://127.0.0.1:7890")
with httpx.Client(transport=proxy_transport, timeout=120) as client:
    resp = client.get(ARXIV_API, params=params, headers={'User-Agent': 'HermesAgent/1.0'})
```

### Paper Scoring for Selection

Simple keyword scoring works well for picking the most innovative papers:

```python
innovation_keywords = [
    'novel', 'new framework', 'transformer', 'attention', 'foundation model',
    'spiking', 'neuromorphic', 'quantum', 'brain-machine', 'BCI',
    'continual learning', 'meta-learning', 'generative', 'diffusion',
    'mechanistic', 'interpretability', 'causal', 'dynamics',
    'hierarchical', 'multi-scale', 'self-organized', 'emergent',
    'plasticity', 'synaptic', 'astrocyte', 'connectome'
]

score = sum(1 for kw in innovation_keywords if kw.lower() in (title + ' ' + abstract).lower())
```

### Skill Duplication Check

The paper 2605.12485 ("Letting the neural code speak") was already processed by a previous cron run:
- Skill existed: `automated-neural-characterization-language`
- INDEX.md already had entry
- Obsidian note already existed
- kg.db already had entity (ID 911)

**Recommendation**: Before creating new skills, always check if the paper was already processed by:
1. `skill_manage(action='create')` → if error "already exists", skip
2. Search INDEX.md for arXiv ID
3. Check kg.db for duplicate titles

### Obsidian Vault Structure

```
~/Library/Mobile Documents/iCloud~md~obsidian/Documents/
├── Neuroscience/
│   ├── arxiv/
│   │   ├── 2026-05/          # Monthly subdirectories
│   │   └── 2026-04/
│   └── papers/               # Topic-organized notes
├── Research/
├── arXiv_*.md                # Root-level single papers
└── ai_collection/            # Synced notes
```

Save path pattern: `Neuroscience/arxiv/YYYY-MM/{arxiv_id} {short_title}.md`

### ai_collection Sync Pattern

```bash
cd /Users/hiyenwong/ai_github/ai_collection
git add collection/skills/{skill-name}/ INDEX.md
git commit -m "feat: add {skill-name} from arXiv {id}"
git push
```

INDEX.md format:
```markdown
## YYYY-MM-DD - Neuroscience Research (Cron Job)

### {Paper Title}
- [[{skill-name}]] - One-sentence description (arXiv: {id})
  - Core insight 1
  - Core insight 2
  - **Activation**: keyword1, keyword2
```
