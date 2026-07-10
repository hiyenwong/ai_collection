### arXiv Paper Extraction — Mature Library Pattern

**IMPORTANT**: The ai_collection skill library now has 1657+ kg_entities and hundreds of skills. ~70-80% of newly scanned papers already have corresponding skills. Efficient duplicate detection is now the most critical step.

#### Tiered Duplicate Detection (MANDATORY)
1. **Tier 1 (arXiv ID in SKILL.md)**: Search for `"{arxiv_id}"` across all `*/SKILL.md` files. If found, the paper already has a skill. **Do NOT create a new one.**
2. **Tier 2 (concept keyword in SKILL.md)**: Search for key methodology terms across `*/SKILL.md`. If found, compare the frameworks. If overlapping, **enhance the existing skill** instead of creating.
3. **Tier 3 (reference files — NOT duplicates)**: Matches in `references/`, `memory/`, or `.hub/` directories are session logs, caches, or discovery notes. These are **NOT** true skill-level duplicates. Only SKILL.md matches count.

**Working example from 2026-05-31 session**: Paper 2605.27416 (Quantum Federated Learning Backdoors) returned matches in `ai_collection/memory/`, `arxiv-search/references/`, `quantum-federated-learning-security/SKILL.md`, `qml-adversarial-robustness-sok/SKILL.md`, `quantum-federated-backdoor-cult/SKILL.md`, and `quantum-federated-security-cult/SKILL.md`. The SKILL.md matches (tiers 1-2) confirmed the paper already had skills, while the reference/memory matches were just session logs. The agent correctly skipped creation.

**arXiv API access**: Rate limiting is now severe (immediate 429 even with custom User-Agent). **kg.db-first approach**: Query `arxiv_papers` and `kg_entities` tables in `/Users/hiyenwong/.openclaw/workspace/kg.db` as primary source. Only attempt arXiv API if the specific paper is not in kg.db. When using API: Python `urllib.request.urlopen` with `User-Agent: 'ResearchBot/1.0'`, 4-second delays, category-scoped queries only (`cat:quant-ph AND all:finance`). If 429, wait 30s and retry once, then fall back to kg.db.

**web_search (Firecrawl)**: Returns NoneType errors — use urllib or kg.db as primary source.
**web_extract**: Blocks arxiv.org URLs — extract from kg.db entities table instead.
