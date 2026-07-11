# Workspace kg.db Dual-Table Import Pattern (2026-06-25 Confirmed)

## The Problem
Workspace root kg.db (`~/.openclaw/workspace/kg.db`) has **two separate paper tables**:
- `kg_entities` — stores paper metadata (title, url, content, authors, etc.)
- `papers` — stores paper metadata + `skill_name` for tracking

Importing into `kg_entities` does **NOT** automatically populate `papers`. A direct `UPDATE papers SET skill_name='...' WHERE arxiv_id='...'` will affect **0 rows** if the paper was never inserted into `papers`.

## Correct Import Workflow

```python
# Step 1: Insert into kg_entities (for knowledge graph)
INSERT OR IGNORE INTO kg_entities (title, url, content, authors, published_date, category, source)
VALUES (?, ?, ?, ?, ?, ?, 'arxiv')

# Step 2: Insert into papers (for skill tracking) — MUST do this BEFORE updating skill_name
INSERT OR IGNORE INTO papers (arxiv_id, title, authors, published_date, categories, abstract, skill_name)
VALUES (?, ?, ?, ?, ?, ?, ?)

# Step 3: Now UPDATE works (or set skill_name directly in the INSERT)
UPDATE papers SET skill_name='skill-name' WHERE arxiv_id='2606.xxxxx'
```

## Why This Matters
- `kg_entities` is the primary table for vector embeddings, PageRank, and KG analysis
- `papers` is used for cross-referencing which papers have skills (`skill_name IS NULL` queries)
- They share NO foreign key relationship — they are independent tables

## Common Pitfall
```sql
-- This affects 0 rows if paper only exists in kg_entities:
UPDATE papers SET skill_name='foo' WHERE arxiv_id='2606.26090';

-- Fix: INSERT first, then UPDATE, or set skill_name in the INSERT:
INSERT OR IGNORE INTO papers (arxiv_id, ..., skill_name) VALUES ('2606.26090', ..., 'foo');
```
