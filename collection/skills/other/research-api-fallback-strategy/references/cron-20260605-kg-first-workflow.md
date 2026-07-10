# 2026-06-05: Successful KG-First Research Workflow

## Context
Friday topic: Number Theory, Statistics, Advanced Mathematics + Quantum Mechanics (daily).

## What happened
- arXiv API through httpx+proxy: first request succeeded (after 60s delay), all subsequent requests returned 429 immediately
- curl via terminal: also 429 after first success
- web_search: Firecrawl returned NoneType error
- web_extract: blocked arxiv.org URLs as "private/internal network"

## What worked
1. **First successful arXiv API request** returned 3 papers (2606.05005, 2606.04873, 2606.04794) — saved before rate limit kicked in
2. **kg.db sqlite3 direct queries** on workspace KG (`/Users/hiyenwong/.openclaw/workspace/scripts/kg.db`) — found 15+ additional relevant papers from today already imported by parallel cron workers
3. **kg_tool commands** (pagerank, communities, search) — all working, provided research clustering insights

## Workspace kg.db schema (confirmed 2026-06-05)
Two tables used:
- `entities(id TEXT PK, name TEXT, type TEXT, category TEXT, description TEXT, source TEXT, created_date TEXT)`
- `relationships(id TEXT PK, source TEXT, target TEXT, relation TEXT, description TEXT, created_date TEXT)`
- `relations(id INTEGER PK AUTO, source TEXT, target TEXT, relation_type TEXT, metadata TEXT)`
- `kg_vectors(id TEXT PK, embedding TEXT)`

Note: This is DIFFERENT from the wiki kg.db (`/Users/hiyenwong/wiki/kg.db`) which uses `kg_entities(title, url, content, ...)`.

## Successful paper import pattern
Direct sqlite3 INSERT works reliably (kg_tool import-paper has a bug with missing `url` column):
```bash
sqlite3 kg.db "INSERT INTO entities (id, name, type, category, description, source, created_date)
  VALUES ('2606.04176', 'Title...', 'paper', 'quantum-math', 'Abstract...', 'arxiv', date('now'));"
```

## New skill created
`distributional-matrix-completion` (arXiv: 2606.04176) — kernel mean embeddings + Tucker rank for distributional matrix completion.

## ai_collection sync
- Push to main blocked by PR requirement (GH013)
- Workaround: push to feature branch `cron/distributional-matrix-completion-20260605`
