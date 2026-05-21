---
name: arxiv-neuroscience-research
description: "End-to-end workflow for discovering, selecting, and archiving neuroscience papers from arXiv into skills, ai_collection, Obsidian, and kg.db."
---

# arXiv Neuroscience Research Workflow

Cron-driven pipeline for scanning arXiv neuroscience papers, selecting the most valuable, and archiving them across multiple systems.

## Workflow Steps

### 1. Discovery (Browser-based, zero rate limits)

arXiv API aggressively rate-limits (HTTP 429). Use browser navigation:
- `browser_navigate` → `https://arxiv.org/list/{category}/recent` for today's papers
- Key categories: `q-bio.NC`, `cs.NE`, `cs.AI`, `cs.LG`
- Extract paper IDs, titles, categories from snapshot

### 2. Selection Criteria

Select 1-2 papers based on:
- **Novelty**: New framework/methodology vs. incremental improvement
- **Cross-domain relevance**: Bridges neuroscience + AI/ML
- **Practical impact**: Enables new BCI capabilities, improves model-brain alignment
- **Data quality**: Applied to established datasets (NSD, BCI competitions)

### 3. Paper Reading

- `browser_navigate` → `https://arxiv.org/abs/{id}` for abstract
- `browser_navigate` → `https://arxiv.org/html/{id}v1` for full paper content
- Extract: title, authors, abstract, key findings, methodology, applications

### 4. Skill Creation

Create SKILL.md at `~/.hermes/skills/ai_collection/{skill-name}/SKILL.md` containing:
- Paper metadata (title, authors, arXiv ID, date, categories)
- Problem statement
- Methodology (step-by-step)
- Key findings/results
- Applications
- Implementation considerations
- Pitfalls
- Activation keywords

### 5. Sync to ai_collection

```bash
cp -r ~/.hermes/skills/ai_collection/{skill-name}/ ~/ai_github/ai_collection/collection/skills/{skill-name}/
# Update INDEX.md with new entry at top
cd ~/ai_github/ai_collection && git add collection/skills/{skill-name}/ INDEX.md
git commit -m "feat: add {skill-name} from arXiv {id}"
git push
```

### 6. Sync to Obsidian

Update notes at `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/`:
- Paper-specific note with full abstract, findings, methodology
- Daily research log with summary

### 7. Update Knowledge Graph (kg.db)

Database: `/Users/hiyenwong/.openclaw/workspace/kg.db`
- Check by URL before inserting (dedup)
- UPDATE existing entries with richer content
- Generate hash-based embedding vector (256-dim, struct.pack float32)
- Create relationships with existing neuroscience papers

## ⚠️ Critical Pitfalls

### Skill Dedup
- **ALWAYS check skills_list for existing skills before creating new ones**
- Many papers have existing skills from prior cron sessions
- Creating duplicates wastes effort and requires cleanup (delete from both `~/.hermes/skills/` AND `~/ai_github/ai_collection/collection/skills/` AND git revert)
- If a duplicate is accidentally created: delete immediately and consolidate into the existing skill

### arXiv API Rate Limiting
- `urllib.request.urlopen`, `requests`, `httpx` all get HTTP 429
- `web_search` returns NoneType errors
- **Browser navigation is the most reliable discovery method** — zero rate limits

### kg.db Multiple Files
- Main workspace: `/Users/hiyenwong/.openclaw/workspace/kg.db` (1,300+ entities) — USE THIS ONE
- Scripts mini-KG: `~/.openclaw/workspace/scripts/kg.db` — different schema, don't use
- kg_tool DB: `~/.openclaw/workspace/scripts/kg_tool/kg.db` — kg_tool's own database

### Vector Format
- Use `struct.pack(f'{dim}f', *vec)` for binary float32
- Hash-based embeddings (deterministic, keyword-level similarity)
- Base 16 for hex parsing: `int(h[:8], 16)` NOT `int(h[:8], 0xFFFFFFFF)`

### Obsidian Path
- iCloud synced: `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/`
- Check if note already exists before writing (update vs. create)

## Related Files

- [references/pending-cleanup.md](references/pending-cleanup.md) — Pending git cleanup for duplicate skill removed from this session