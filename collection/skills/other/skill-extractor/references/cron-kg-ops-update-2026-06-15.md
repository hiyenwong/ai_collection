# Cron Knowledge Graph Operations — Update 2026-06-15

## INDEX.md Path (CORRECTED)
The INDEX.md for ai_collection is at the **repo root**:
`/Users/hiyenwong/ai_github/ai_collection/INDEX.md`
NOT at `collection/skills/INDEX.md`. Always use `find /Users/hiyenwong/ai_github/ai_collection -name "INDEX.md"` to confirm.

## kg_tool Binary Status (2026-06-15)
- **stats**: ✅ Always works
- **generate-embeddings**: ✅ Works (after VIEW fix)
- **pagerank**: ✅ Works on workspace kg.db (316 relations in kg_relations)
- **communities**: ❌ Returns "No relations in graph" — reads kg_edges which has 0 rows despite kg_relations having 316. Need to sync: `INSERT OR IGNORE INTO kg_edges (source, target, relation, weight) SELECT s.name, t.name, r.relation_type, r.weight FROM kg_relations r JOIN kg_entities s ON r.source_id = s.id JOIN kg_entities t ON r.target_id = t.id;`
- **search**: ✅ Likely works after VIEW fix
- **import-paper**: ❌ Still broken (INSERT into read-only VIEW) — use direct sqlite3 INSERT into base tables

## Domain Saturation (Confirmed 2026-06-15)
- Neuroscience + Quantum: ~85% saturated (1 of 15 papers genuinely new)
- CS + Quantum: ~85%
- Medicine + Quantum: ~60%
- Number Theory + Quantum: low genuine cross-domain yield
- Economics + Quantum: ~75%
- Information Science + Quantum: ~60%
- Systems Engineering + Quantum: ~60%

## kg.db File Locations
- **Workspace**: `/Users/hiyenwong/.openclaw/workspace/scripts/kg.db` — used by kg_tool binary
- **Wiki**: `/Users/hiyenwong/wiki/kg.db` — symlink → scripts/kg.db
- **Hermes-internal**: `~/.hermes/kg.db` — completely different schema

## Duplicate Detection Pattern (2026-06-15)
For each paper from arXiv search, check existence in kg.db:
```bash
sqlite3 /Users/hiyenwong/.openclaw/workspace/scripts/kg.db "SELECT name FROM kg_entities WHERE metadata LIKE '%{arxiv_id}%';"
```
Also check skills:
```bash
grep -rl "{arxiv_id}\|{concept-keywords}" ~/.hermes/skills/ 2>/dev/null
```
