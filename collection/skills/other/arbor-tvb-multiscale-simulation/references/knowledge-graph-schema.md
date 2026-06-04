# Knowledge Graph Schema Reference

## Verified Schema (2026-05-28 Production Check)

```sql
CREATE TABLE papers (
    arxiv_id TEXT PRIMARY KEY,
    title TEXT,
    authors TEXT,
    skill TEXT,
    date_added DATE DEFAULT CURRENT_DATE
);
```

**CRITICAL**: This schema was verified via direct sqlite3 query. The following columns DO NOT exist:
- `id` (INTEGER PRIMARY KEY) 
- `abstract`
- `keywords`
- `tags`
- `rowid`

Always verify schema before assuming structure:
```bash
sqlite3 ~/.hermes/kg.db ".schema papers"
```

## Correct Insert Pattern

Use `INSERT OR REPLACE` with explicit column names (handles duplicates gracefully):

```bash
sqlite3 ~/.hermes/kg.db "INSERT OR REPLACE INTO papers (arxiv_id, title, authors, skill, date_added) VALUES ('2505.16861', 'Arbor-TVB: A Novel Multi-Scale Co-Simulation Framework...', 'Thorsten Hater, Juliette Courson, Han Lu, Sandra Diaz-Pier, Thanos Manos', 'ai_collection/arbor-tvb-multiscale-simulation', '2026-05-28');"
```

Example output:
```
# Success - no output
# Check: sqlite3 ~/.hermes/kg.db "SELECT COUNT(*) FROM papers;"
141
```

## Common Pitfalls

1. **Wrong column names**: Previous sessions assumed `id`, `abstract`, or `keywords` columns — these don't exist
2. **Missing OR REPLACE**: Using just `INSERT` fails on duplicate arxiv_id
3. **Missing date_added**: Defaults to CURRENT_DATE but explicit value safer
4. **Quoting**: Use single quotes for string values in SQL
5. **Skill path format**: Use format `ai_collection/{skill-name}` not full filesystem path

## Verification Queries

```bash
# Count total papers
sqlite3 ~/.hermes/kg.db "SELECT COUNT(*) FROM papers;"

# Check recent entries
sqlite3 ~/.hermes/kg.db "SELECT * FROM papers ORDER BY date_added DESC LIMIT 5;"

# Search by arxiv_id  
sqlite3 ~/.hermes/kg.db "SELECT * FROM papers WHERE arxiv_id='2505.16861';"

# Search by skill
sqlite3 ~/.hermes/kg.db "SELECT arxiv_id, title FROM papers WHERE skill LIKE '%arbor-tvb%';"
```

## Integration with arXiv Workflow

When completing the arXiv-to-skill workflow, always:

1. Create skill (SKILL.md)
2. Copy to ai_collection git repo
3. Update INDEX.md
4. Git commit + push
5. Write Obsidian note
6. **Insert into kg.db using verified pattern above**

This step was added after discovering the schema mismatch in session 2026-05-28.