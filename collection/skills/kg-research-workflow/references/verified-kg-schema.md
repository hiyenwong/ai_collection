# Knowledge Graph — Verified Schema & Operations (2026-05-14)

## Actual Database: `~/.hermes/kg.db`

This is the primary knowledge graph used by the Hermes Agent cron jobs.

### Tables

#### `papers` — Paper storage
```sql
CREATE TABLE papers (
    arxiv_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    authors TEXT,
    skill TEXT,           -- associated skill name
    date_added TEXT       -- YYYY-MM-DD
);
```

#### `entities` — General KG entities
```sql
CREATE TABLE entities (
    id TEXT PRIMARY KEY,           -- text IDs: 'arxiv:2605.12999', 'concept:mamba-spike-forecasting', 'topic:neuropixels'
    name TEXT NOT NULL,
    type TEXT NOT NULL,            -- 'research_paper', 'methodology', 'topic', 'skill', 'concept', 'model_architecture'
    attributes TEXT,               -- JSON with metadata
    created_at TEXT,
    last_accessed TEXT,
    importance_score REAL
);
```

#### `relations` — Entity relationships
```sql
CREATE TABLE relations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_id TEXT,                -- matches entities.id
    target_id TEXT,                -- matches entities.id
    relation_type TEXT NOT NULL,   -- 'uses_methodology', 'uses_data', 'uses_architecture', 'addresses_task', 'studies_phenomenon', 'complementary_to'
    strength REAL DEFAULT 1.0,
    created_at TEXT
);
```

#### `paper_tags` — Paper tagging
```sql
CREATE TABLE paper_tags (
    paper_id TEXT,
    tag TEXT
);
```

#### Other tables: `memories`, `sessions`

### Common Entity ID Patterns
| Pattern | Example | Type |
|---------|---------|------|
| `arxiv:2605.XXXXX` | `arxiv:2605.12999` | research_paper |
| `concept:<slug>` | `concept:mamba-spike-forecasting` | methodology |
| `topic:<slug>` | `topic:neuropixels` | topic |
| `skill_<name>` | `skill_warped-hierarchical` | skill |
| `model_<name>` | `model_qrenn-2026-04-26` | model_architecture |

### Common Relation Types
- `uses_methodology` — paper uses a methodology
- `uses_data` — paper uses a data source
- `uses_architecture` — paper uses an architecture
- `addresses_task` — paper addresses a task
- `studies_phenomenon` — paper studies a phenomenon
- `complementary_to` — methodologies complement each other

### Python Insert Example
```python
import sqlite3, json
from datetime import datetime

conn = sqlite3.connect(os.path.expanduser("~/.hermes/kg.db"))
c = conn.cursor()

# Insert paper
c.execute("INSERT OR REPLACE INTO papers (arxiv_id, title, authors, skill, date_added) VALUES (?,?,?,?,?)",
    ("2605.12999", "Paper Title", "Authors", "skill-name", "2026-05-14"))

# Insert entity
c.execute("INSERT OR REPLACE INTO entities (id, name, type, attributes, created_at, last_accessed, importance_score) VALUES (?,?,?,?,?,?,?)",
    ("concept:my-method", "My Method", "methodology", json.dumps({"key": "value"}),
     datetime.now().isoformat(), datetime.now().isoformat(), 0.75))

# Insert relation
c.execute("INSERT INTO relations (source_id, target_id, relation_type, strength, created_at) VALUES (?,?,?,?,?)",
    ("arxiv:2605.12999", "concept:my-method", "uses_methodology", 0.95, datetime.now().isoformat()))

conn.commit()
conn.close()
```

### Notes
- The schema in `kg-research-workflow` SKILL.md references **different** tables (kg_entities, kg_relations, kg_vectors) — those belong to other kg.db instances (workspace/wiki). Always use `~/.hermes/kg.db` for Hermes cron job operations.
- Entity IDs are **text** strings (not integers), allowing semantic naming.
- Attributes are JSON text (not BLOB).
- No `kg_tool` binary needed — direct SQLite operations work fine.
