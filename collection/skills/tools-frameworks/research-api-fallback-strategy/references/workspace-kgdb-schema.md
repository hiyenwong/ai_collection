# Workspace kg.db Schema Reference (Verified 2026-05-28)

## File Location
`/Users/hiyenwong/.openclaw/workspace/scripts/kg.db`

## Schema

### entities
| Column | Type | Notes |
|--------|------|-------|
| id | TEXT | Primary key (e.g., `paper-2605.17156v1`) |
| name | TEXT | Paper title or entity name |
| type | TEXT | `paper`, `author`, `concept`, `category`, `keyword`, `skill` |
| category | TEXT | Category label (e.g., `quant-ph`) |
| description | TEXT | Abstract or entity description |
| source | TEXT | URL or arXiv ID |
| created_date | TEXT | Date string |

### relationships
| Column | Type | Notes |
|--------|------|-------|
| id | TEXT | |
| source | TEXT | Source entity ID |
| target | TEXT | Target entity ID |
| relation | TEXT | `authored_by`, `belongs_to`, `uses_concept`, `relates_to` |
| description | TEXT | |
| created_date | TEXT | |

### kg_vectors
| Column | Type | Notes |
|--------|------|-------|
| id | TEXT | |
| entity_id | TEXT | References entities.id |
| vector_data | TEXT | JSON array of floats |
| created_at | TEXT | |

### research_log
| Column | Type | Notes |
|--------|------|-------|
| id | INTEGER | Autoincrement |
| date | TEXT | |
| topic | TEXT | |
| arxiv_id | TEXT | |
| skill_name | TEXT | |
| summary | TEXT | |
| status | TEXT | |

## Verified Working Queries

```python
import sqlite3
db = sqlite3.connect('/Users/hiyenwong/.openclaw/workspace/scripts/kg.db')
c = db.cursor()

# Find papers by keyword
c.execute('''SELECT id, name, description, source FROM entities 
    WHERE type = 'paper' AND (LOWER(name) LIKE ? OR LOWER(description) LIKE ?) 
    ORDER BY id DESC LIMIT 20''', ('%quantum%', '%quantum%'))

# Find papers by category
c.execute('''SELECT id, name, description, source FROM entities 
    WHERE type = 'paper' AND category LIKE ? 
    ORDER BY id DESC LIMIT 20''', ('%quant%',))

# Entity type distribution
c.execute('SELECT type, count(*) FROM entities GROUP BY type ORDER BY count(*) DESC')

# Relationship type distribution  
c.execute('SELECT relation, count(*) FROM relationships GROUP BY relation ORDER BY count(*) DESC LIMIT 10')

# Recent papers (by id sort)
c.execute('''SELECT id, name, description FROM entities 
    WHERE type = 'paper' ORDER BY id DESC LIMIT 30''')

# Check if specific paper exists
c.execute('SELECT id, name FROM entities WHERE id = ?', ('paper-2605.17156v1',))

# Count totals
c.execute('SELECT count(*) FROM entities')  # 690 as of 2026-05-28
c.execute('SELECT count(*) FROM relationships')  # 604
c.execute('SELECT count(*) FROM kg_vectors')  # 630
c.execute('SELECT count(*) FROM research_log')  # 111
```

## kg_tool Binary
- Path: `/Users/hiyenwong/.openclaw/workspace/scripts/kg_tool/target/release/kg_tool`
- Note: kg_tool uses a DIFFERENT DB path (reported in `kg_tool stats` output)
- As of 2026-05-28: `kg_tool stats` reports `DB path: /Users/hiyenwong/wiki/kg.db` (wiki path, NOT workspace)
- **Use sqlite3 directly for workspace kg.db**, use kg_tool for wiki kg.db analysis

## Common Pitfalls
1. `SELECT title FROM entities` → "no such column: title" (use `name`)
2. `SELECT content FROM entities` → "no such column: content" (use `description`)  
3. `SELECT url FROM entities` → "no such column: url" (use `source`)
4. `SELECT published_date FROM entities` → "no such column: published_date" (use `created_date`)
5. `SELECT entity_type FROM entities` → "no such column: entity_type" (use `type`)
6. kg_tool binary points to wiki kg.db, not workspace — verify with `kg_tool stats`
