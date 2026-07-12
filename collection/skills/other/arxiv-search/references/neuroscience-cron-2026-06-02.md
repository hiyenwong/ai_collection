# Neuroscience Literature Search Workflow (2026-06-02)

Session: Automated cron job for neuroscience paper discovery, skill creation, and knowledge graph sync.

## Problem Encountered
`web_search` tool failed with Firecrawl error when attempting to search arxiv.org.

## Successful Workaround
Used direct arXiv API via curl with proxy:
```bash
curl -x http://127.0.0.1:7890 "https://export.arxiv.org/api/query?search_query=all:neuroscience+AND+cat:q-bio.NC&start=0&max_results=50&sortBy=submittedDate&sortOrder=descending" > /tmp/arxiv_papers.xml
```

Parsed XML to extract: `<entry><id>`, `<title>`, `<summary>`, `<author><name>`, `<arxiv:doi>`

## Papers Discovered (2026-05)
1. **2605.30638** - "Score Broadcast and Decorrelation: A General Framework for Broadcast-Based Credit Assignment" (cs.LG)
   - Novel credit assignment framework for neural network training
   - Broadcast-based approach avoiding explicit gradient computation
   - Key insight: Decorrelation mechanism enables efficient credit propagation
   
2. **2605.31173** - "MindVoice: Reconstructing Intelligible Speech from Non-invasive Neural Signals with Pretrained Priors" (cs.NE)
   - Speech reconstruction from EEG/MEG using pretrained language priors
   - Zero-shot capability via pretrained TTS integration
   - Clinical potential for ALS patients
   
3. **2605.31473** - "The Metastable Mind: Neural Underpinnings of Naturalistic Cognition Through the Synthesis of Event Segmentation and Metastable Neural States" (q-bio.NC)
   - Unifies event segmentation theory with metastable neural dynamics
   - Naturalistic cognition modeling framework
   - Task-agnostic neural state characterization

## Skill Creation Workflow
1. Create skill via `skill_manage(action='create', category='ai_collection')`
2. Store at `~/.hermes/skills/ai_collection/{skill-name}/SKILL.md`
3. Copy to GitHub project:
   ```bash
   mkdir -p /Users/hiyenwong/ai_github/ai_collection/collection/skills/{skill-name}
   cp ~/.hermes/skills/ai_collection/{skill-name}/SKILL.md /Users/hiyenwong/ai_github/ai_collection/collection/skills/{skill-name}/
   ```
4. Update INDEX.md with activation keywords and core insights
5. Commit and push to ai_collection repository

## Obsidian Notes Workflow
Save to vault:
```bash
~/Library/Mobile Documents/iCloud~md~obsidian/Documents/{paper-title}.md
```
Structure: YAML frontmatter (arxiv_id, title, authors, date), followed by summary, key methods, clinical implications, skill links.

## Knowledge Graph Import
Batch import script pattern:
```python
import sqlite3, hashlib, json

# Generate deterministic 256-dim embedding from SHA256 seed
def generate_embedding(text):
    seed = hashlib.sha256(text.encode()).digest()
    # Use seed to initialize deterministic embedding generation
    # (matching kg-db-operations skill pattern)
    ...

# Import to all 3 kg.db instances
kg_paths = [
    '/Users/hiyenwong/wiki/kg.db',
    '/Users/hiyenwong/.openclaw/workspace/scripts/kg.db',
    '/Users/hiyenwong/ai_github/ai_collection/kg.db'
]
for db_path in kg_paths:
    conn = sqlite3.connect(db_path)
    conn.execute("INSERT INTO entities VALUES (?, ?, ?, ?, ?, ?)", ...)
    conn.commit()
```

Verified with:
```sql
SELECT id, name FROM entities WHERE name LIKE '%Score Broadcast%' OR name LIKE '%MindVoice%' OR name LIKE '%Metastable Mind%';
```

## Key Insights for Future Sessions
- When web_search fails, curl + proxy to arXiv API is reliable fallback
- arxiv-search skill already documents most pitfalls; use reference files for session-specific workflows
- Sync workflow: Hermes skills → ai_collection GitHub → Obsidian vault → kg.db (all 3 instances)
- Deterministic embeddings from SHA256 seed ensure reproducible kg_vectors

## Git Commits Generated
1. "feat: add score-broadcast-decorrelation-credit-assignment from arXiv 2605.30638"
2. "feat: update mindvoice-neural-speech-reconstruction and metastable-mind-event-segmentation"

Both pushed to origin/main successfully.