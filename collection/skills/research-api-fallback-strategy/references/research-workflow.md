# Research Workflow Reference (2026-05-20)

## Workspace Paper Caches

Located at `/Users/hiyenwong/.openclaw/workspace/`:
- `new_papers.json` - Latest papers from cron job runs (18 papers, full metadata)
- `key_papers.json` - Curated important papers
- `neuro_quantum_papers.json` - Neuroscience + Quantum intersection papers
- `all_papers.json` - Cumulative paper collection (20+ papers)
- `arxiv_results_*.json` - Dated arxiv search results

## kg.db Schema

See `references/kg-schema.md` for full table definitions.

Quick queries:
```bash
# Recent papers by type
sqlite3 kg.db "SELECT id, name FROM entities WHERE type='paper' ORDER BY id DESC LIMIT 10;"

# Paper concepts (cross-reference)
sqlite3 kg.db "SELECT concept, COUNT(*) FROM paper_concepts GROUP BY concept ORDER BY 2 DESC LIMIT 10;"

# Vector count
sqlite3 kg.db "SELECT COUNT(*) FROM kg_vectors;"
```

## ai_collection Project

Located at `/Users/hiyenwong/ai_github/ai_collection/`:
- Skills stored in `collection/skills/{skill-name}/SKILL.md`
- INDEX.md at root tracks all skills with dates and arXiv IDs
- Git push may require proxy: `ALL_PROXY=http://127.0.0.1:7890 git push`

## Skill Sync Pattern

After creating a skill:
1. Copy to ai_collection: `cp -r ~/.hermes/skills/{name}/ ai_github/ai_collection/collection/skills/{name}/`
2. Update INDEX.md with entry format
3. Git add + commit + push
