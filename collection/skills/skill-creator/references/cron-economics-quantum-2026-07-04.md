# Cron Session Notes: 2026-07-04 Economics/Investment + Quantum

## kg.db Schema Findings (workspace root: `~/.openclaw/workspace/kg.db`)

**PRAGMA-verified schema for 2026-07-04 session:**

| Table | Columns |
|-------|---------|
| `kg_entities` | `id INTEGER PK AUTOINCREMENT, title TEXT, url TEXT UNIQUE NOT NULL, content TEXT, authors TEXT, published_date TEXT, category TEXT, source TEXT, created_at, updated_at` |
| `kg_vectors` | `id INTEGER PK AUTOINCREMENT, entity_id INTEGER FK, vector_data BLOB, created_at` |
| `kg_relations` | `source INT, target INT, type TEXT, weight REAL` |

**Critical correction**: `kg_relations` uses `source`/`target` (NOT `source_id`/`target_id`). Earlier docs in automated-research-workflow.md claimed `source_id`/`target_id` — that's WRONG for this environment. Always PRAGMA-verify.

## git push to existing branch

When pushing to a branch already on remote, `git push origin <branch>` works fine. `--set-upstream` only needed for first push of new branch.
