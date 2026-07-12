# Arxiv Rate Limit Fallback: Use kg.db as Primary Source

## Date: 2026-06-12
## Session: Friday Cron (Number Theory, Statistics, Advanced Mathematics + Daily Quantum)

## Pattern Confirmed

When arxiv.org API returns "Rate exceeded" (HTTP 429) even after retries and delays, and `curl --proxy` also fails, **working with papers already in kg.db is a productive alternative**.

## Workflow

### Step 1: Detect Rate Limiting
```bash
# Test arxiv API
curl -s --proxy http://127.0.0.1:7890 --connect-timeout 15 --max-time 30 "https://export.arxiv.org/api/query?search_query=cat:quant-ph&max_results=3"
# Returns: "Rate exceeded."
```

### Step 2: Query kg.db for Papers Without Skills
```bash
# Find papers by category that lack skills
sqlite3 kg.db "SELECT arxiv_id, title, categories FROM papers WHERE skill_name IS NULL AND (categories LIKE '%math%' OR categories LIKE '%stat%') ORDER BY created_at DESC LIMIT 10;"
```

### Step 3: Create Skills from Existing Papers
```bash
# Write skill creation script to /tmp
# Execute with terminal
python3 /tmp/create_skill.py
```

### Step 4: Update kg.db and Sync
```bash
# Update papers table with skill names
sqlite3 kg.db "UPDATE papers SET skill_name='new-skill-name' WHERE arxiv_id='XXXX.XXXXX';"
# Add to kg_entities
sqlite3 kg.db "INSERT INTO kg_entities (title, url, content, published_date, category, source) VALUES (?, ?, ?, ?, ?, ?);"
# Sync to ai_collection and git commit
```

## Verified Results (2026-06-12)

- 3 papers extracted from kg.db (no arxiv API calls needed)
- 3 new skills created: degree-tensor-train-varieties, data-driven-sde-subsampling-rates, random-grover-search
- All synced to ai_collection and pushed successfully
- kg.db had 85 papers with 42 already having skills (51% coverage)

## When to Use This Pattern

- Arxiv API returns "Rate exceeded" consistently
- Multiple retry attempts have failed
- kg.db has recent papers (within last 7 days)
- Some papers lack skills (check `skill_name IS NULL`)

## Benefits

- No dependency on external API availability
- Faster execution (local DB queries vs network calls)
- Can still produce valuable skills from previously discovered but unprocessed papers
- Reduces rate limit pressure on arxiv API
