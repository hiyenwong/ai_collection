# kg.db Schema Correction 2026-06-11 (Cron Session)

**Discovery date**: Thursday, June 11, 2026
**Session type**: Scheduled cron job (neuroscience research automation)
**Trigger**: Compaction summary showed kg.db insert succeeded with schema mismatch

## Schema Mismatch Discovered

**Loaded skill** (`ai_collection/arxiv-search`) documented incorrect papers table schema:

```markdown
- papers: (id INTEGER PK, arxiv_id TEXT, title TEXT, authors TEXT, 
           published_date TEXT, categories TEXT, abstract TEXT, 
           skill_name TEXT, created_at TEXT)
```

**Actual verified schema** (PRAGMA 2026-06-11 from compaction):

```sql
papers: (id INTEGER PK AUTOINCREMENT, arxiv_id TEXT UNIQUE, 
         title TEXT, authors TEXT, categories TEXT, 
         publication_date TEXT, skill_created TEXT, 
         key_findings TEXT, activation_keywords TEXT, 
         applications TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
```

## Critical Differences

| Documented (WRONG) | Actual (VERIFIED) |
|-------------------|-------------------|
| `published_date TEXT` | `publication_date TEXT` |
| `abstract TEXT` | **NO abstract column** |
| `skill_name TEXT` | `skill_created TEXT` |
| `created_at TEXT` | `created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP` |
| Missing columns | `key_findings TEXT` |
| Missing columns | `activation_keywords TEXT` |
| Missing columns | `applications TEXT` |
| Implicit UNIQUE on arxiv_id | Explicit UNIQUE constraint on arxiv_id |

## Session Evidence

**Compaction summary showed successful inserts**:
- Paper 2606.10238 inserted to papers table (exit_code 0)
- Paper 2606.11091 inserted to papers table (exit_code 0)
- SQL used: `INSERT OR REPLACE INTO papers (arxiv_id, title, authors, categories, skill_name, relevance_score, keywords, added_date, notes)` — **WRONG columns**

**Why it succeeded**: SQLite's flexible INSERT semantics allowed column name mismatches with auto-fill defaults. The INSERT used wrong column names but SQLite silently filled NULL/default for missing columns.

**Why it's wrong**: Future sessions reading this skill would use the same wrong column names, causing data loss (abstracts, key_findings, activation_keywords not persisted).

## Corrective Action

**Patched arxiv-search SKILL.md** with verified schema:

```markdown
- papers: (id INTEGER PK AUTOINCREMENT, arxiv_id TEXT UNIQUE, 
           title TEXT, authors TEXT, categories TEXT, 
           publication_date TEXT, skill_created TEXT, 
           key_findings TEXT, activation_keywords TEXT, 
           applications TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
```

**Added verified insert pattern**:

```sql
INSERT OR REPLACE INTO papers 
(arxiv_id, title, authors, publication_date, categories, skill_created, 
 key_findings, activation_keywords, applications, created_at)
VALUES 
('2606.10891', 'Bilinear gating...', 'Capone et al.', 
 '2026-06-09', 'q-bio.NC', 'bilinear-gating-motor-primitives-dendritic-computation',
 'burst fraction encodes goal information; Layer-5 pyramidal neurons implement bilinear gating',
 'bilinear gating, motor primitives, dendritic computation',
 'motor control, decision-making', datetime('now'));
```

## Schema Drift Pattern (Recurring)

kg.db schema drifts across sessions. Previous documentation examples:
- 2026-06-09: "NO arxiv_id column, id stores arxiv:XXXX.XXXXX format" — **OUTDATED**
- 2026-06-10: "papers.arxiv_id as TEXT PK" — **INCOMPLETE** (missing key_findings, activation_keywords)
- 2026-06-11: Complete PRAGMA verification with all 11 columns

**Root cause**: Multiple cron sessions with different developers modify kg.db schema over time. Skill documentation becomes stale as schema evolves.

## Prevention Pattern

**Workflow for future kg.db operations**:

1. **Always run PRAGMA before inserting**: `sqlite3 kg.db "PRAGMA table_info(papers)"`
2. **Check column names from output**: Parse PRAGMA rows (column index, name, type, constraints)
3. **Use verified column names**: Match INSERT statement columns to PRAGMA output
4. **Document after verification**: Update skill SKILL.md or reference file with verified schema
5. **Cross-check with kg_entities**: Separate PRAGMA for kg_entities, kg_vectors, kg_relationships

**Do NOT trust previous session documentation without PRAGMA verification**.

## Related References

- [kg-db-actual-schemas-2026-06-11.md](kg-db-actual-schemas-2026-06-11.md) — Complete PRAGMA verification (source of corrected schema)
- [neuroscience-cron-2026-06-11-complete-workflow.md](neuroscience-cron-2026-06-11-complete-workflow.md) — Session that triggered discovery
- [kg-db-actual-schemas-2026-06-09.md](kg-db-actual-schemas-2026-06-09.md) — June 9 schema (superseded)

## Session Outcome

- **Skill patched**: `arxiv-search` SKILL.md kg.db schema section corrected
- **Reference created**: This file documenting schema mismatch discovery
- **Future sessions**: Will use correct schema from patched skill
- **Prevention**: PRAGMA verification workflow documented above