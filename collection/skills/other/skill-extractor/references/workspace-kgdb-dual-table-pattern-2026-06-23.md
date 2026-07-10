# Workspace Root kg.db Dual-Table Import Pattern (2026-06-23)

## Two-Table Reality

The workspace root kg.db (`~/.openclaw/workspace/kg.db`) has TWO distinct paper storage tables with different schemas and purposes:

### `arxiv_papers` — Staging Table
```sql
CREATE TABLE arxiv_papers (
    id TEXT PRIMARY KEY,      -- arXiv ID as text (e.g., '2606.23678')
    title TEXT,
    authors TEXT,
    published TEXT,
    categories TEXT,
    summary TEXT,
    pdf_url TEXT,
    abs_url TEXT
);
```
- **Purpose**: Raw paper metadata from arXiv API fetch
- **Key column**: `id` is TEXT PRIMARY KEY (the arXiv ID itself)
- **Use**: INSERT papers immediately after fetching from arXiv API

### `papers` — Skill-Tracking Table
```sql
CREATE TABLE papers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    arxiv_id TEXT,           -- links to arxiv_papers.id
    title TEXT,
    authors TEXT,
    published_date TEXT,
    categories TEXT,
    abstract TEXT,           -- note: 'abstract' not 'summary'
    skill_name TEXT,         -- links to created skill
    created_at TEXT
);
```
- **Purpose**: Track which papers have been processed into skills
- **Key column**: `skill_name` — NULL means unprocessed, filled means skill exists
- **Use**: Cross-reference for finding papers that need skill creation

## Correct Import Workflow

```python
# Step 1: Import raw paper into staging table
sqlite3 kg.db "INSERT OR IGNORE INTO arxiv_papers (id, title, authors, published, categories, summary, pdf_url, abs_url) VALUES ('2606.23678', 'Paper Title', 'Authors', '2026-06-22', 'cs.AI,cs.LG', 'Abstract text...', 'https://arxiv.org/pdf/2606.23678', 'https://arxiv.org/abs/2606.23678');"

# Step 2: After skill created, add to tracking table with skill_name
sqlite3 kg.db "INSERT OR IGNORE INTO papers (arxiv_id, title, authors, published_date, categories, abstract, skill_name) VALUES ('2606.23678', 'Paper Title', 'Authors', '2026-06-22', 'cs.AI,cs.LG', 'Abstract text...', 'skill-name-here');"

# Step 3: Find unprocessed papers
sqlite3 kg.db "SELECT arxiv_id, title FROM papers WHERE skill_name IS NULL ORDER BY published_date DESC LIMIT 20;"
```

## Column Name Mismatches Between Tables

| Concept | arxiv_papers | papers |
|---------|-------------|--------|
| Abstract | `summary` | `abstract` |
| arXiv ID | `id` (TEXT PK) | `arxiv_id` (TEXT) |
| Date | `published` | `published_date` |

**Critical**: Do NOT use `summary` column name when inserting into `papers` table — it will fail. Use `abstract`.

## Cross-Reference Query Pattern

```sql
-- Find papers in staging but not yet tracked
SELECT a.id, a.title FROM arxiv_papers a
LEFT JOIN papers p ON a.id = p.arxiv_id
WHERE p.arxiv_id IS NULL;

-- Find tracked papers without skills
SELECT arxiv_id, title FROM papers WHERE skill_name IS NULL;
```
