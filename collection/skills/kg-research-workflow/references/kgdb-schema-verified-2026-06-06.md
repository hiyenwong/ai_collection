# kg.db Schema - Fully Verified 2026-06-06

## Location
`/Users/hiyenwong/.hermes/knowledge_graph/kg.db`

## Tables

### papers
```sql
CREATE TABLE papers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    arxiv_id TEXT UNIQUE,              -- Bare ID: '2602.18690'
    title TEXT NOT NULL,
    authors TEXT,
    categories TEXT,                   -- Comma-separated: 'quant-ph, q-fin.PM'
    submitted_date TEXT,               -- '2026-05-17'
    doi TEXT,                          -- Can be empty string
    skill_name TEXT,                   -- Optional: associated skill name
    skill_path TEXT,                   -- Optional: skill directory path
    created_at TEXT,                   -- datetime('now')
    abstract TEXT                      -- Full abstract text
);
```

### relations
```sql
CREATE TABLE relations (
    source_id TEXT NOT NULL,           -- Paper arxiv_id or skill name
    target_id TEXT NOT NULL,           -- Paper arxiv_id or skill name
    relation_type TEXT NOT NULL,       -- 'cites', 'similar_to', 'has_keyword', 'skill_created'
    data TEXT,                         -- JSON blob for extra metadata
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (source_id, target_id, relation_type)  -- Composite key!
);
```

### entities (for kg_tool compatibility)
```sql
CREATE TABLE entities (
    id TEXT PRIMARY KEY,               -- arxiv_id like '2605.17628'
    type TEXT NOT NULL,                -- 'paper', 'skill', etc.
    data TEXT NOT NULL,                -- JSON blob with all metadata
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### tags
```sql
CREATE TABLE tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_id TEXT,                    -- References entities.id
    tag TEXT NOT NULL
);
```

## Important Notes
- **NO kg_vectors table** in this database
- Relations uses **composite TEXT primary key** - NOT auto-increment INTEGER
- Column is `submitted_date` NOT `published`
- Always verify with `PRAGMA table_info(papers)` before importing