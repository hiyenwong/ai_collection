# kg.db schema corrections (2026-07-04)

**Workspace root kg.db (`~/.openclaw/workspace/kg.db`) — PRAGMA verified 2026-07-04:**

`kg_relations` table columns: `source INT, target INT, type TEXT, weight REAL`

**NOT** `source_id`/`target_id` as previously documented. The column names `source`/`target` are the actual schema. The automated-research-workflow.md file contains an incorrect claim that `kg_relations` uses `source_id`/`target_id` — that is WRONG for this environment. Always `PRAGMA table_info(kg_relations)` before INSERT.
