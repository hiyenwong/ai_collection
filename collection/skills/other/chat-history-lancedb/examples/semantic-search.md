# Semantic Search Examples

## Prerequisites

Make sure you have configured your ZHIPU_API_KEY in `.env`:

```bash
ZHIPU_API_KEY=your_api_key_here
```

## Semantic Search

```bash
# Save some test data first
SESSION_ID=$(node dist/index.js session create "Tech Questions")

node dist/index.js save \
  --session $SESSION_ID \
  --role user \
  --content "How do I connect to PostgreSQL in Python?"

node dist/index.js save \
  --session $SESSION_ID \
  --role assistant \
  --content "Use psycopg2 or sqlalchemy libraries."

node dist/index.js save \
  --session $SESSION_ID \
  --role user \
  --content "What's the best way to handle database connections?"

node dist/index.js save \
  --session $SESSION_ID \
  --role assistant \
  --content "Use connection pools and context managers."
```

Now search semantically:

```bash
# Semantic search (default)
node dist/index.js search "postgres database connection"

# Force semantic search
node dist/index.js search "postgres database connection" --semantic

# Keyword search
node dist/index.js search "psycopg2" --keyword

# Hybrid search (best of both)
node dist/index.js search "database best practices"
```

## With Filters

```bash
# Search within a specific session
node dist/index.js search "database" --session $SESSION_ID

# Limit results
node dist/index.js search "database" --limit 5

# Minimum relevance score
node dist/index.js search "database" --min-score 0.7
```
