# sqlite3 CLI vs Python INSERT for kg.db

## Problem (2026-05-27 Confirmed)

`sqlite3 db "INSERT INTO entities VALUES ('...')"` **silently fails** when paper titles/descriptions contain:
- Single quotes / apostrophes (`'`)
- Backslashes (`\`)
- LaTeX math notation (`10^{-27}`, `$\rho_1$`)
- Dollar signs, percent signs

**Symptom**: exit code 0, no stderr, zero rows inserted. Verification `SELECT` returns empty.

## Working Pattern

Always use Python with parameterized queries via `execute_code`:

```python
from hermes_tools import write_file, terminal

script = '''
import sqlite3

db_paths = [
    '/Users/hiyenwong/wiki/kg.db',
    '/Users/hiyenwong/.openclaw/workspace/scripts/kg.db',
]

papers = [
    ('arxiv_ID', 'Title', 'paper', 'category', 'Description', 'arxiv', 'date'),
]

for db_path in db_paths:
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    for paper in papers:
        c.execute('INSERT OR IGNORE INTO entities (id, name, type, category, description, source, created_date) VALUES (?, ?, ?, ?, ?, ?, ?)', paper)
    conn.commit()
    conn.close()
'''

write_file('/tmp/import_papers.py', script)
terminal('python3 /tmp/import_papers.py')
```

## Verification

Always verify after insert:
```python
result = terminal("sqlite3 /Users/hiyenwong/wiki/kg.db \"SELECT id, name FROM entities WHERE id='arxiv_XXXX.XXXXX';\"")
if not result['output'].strip():
    # INSERT silently failed — use Python parameterized queries
```

## Why sqlite3 CLI Fails

The sqlite3 CLI shell interprets the entire string as a shell command first, then passes it to SQLite. Even with careful quoting, complex strings with mixed quotes, LaTeX, or Unicode can cause the shell to mangle the input before it reaches SQLite. Parameterized queries in Python bypass this entirely.
