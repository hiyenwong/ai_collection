# Basic Usage Examples

## Creating a Session and Saving Messages

```bash
# Create a new session
SESSION_ID=$(node dist/index.js session create "My Project")
echo "Created session: $SESSION_ID"

# Save messages
node dist/index.js save \
  --session $SESSION_ID \
  --role user \
  --content "How do I read a CSV file in Python?"

node dist/index.js save \
  --session $SESSION_ID \
  --role assistant \
  --content "You can use pandas.read_csv():"

node dist/index.js save \
  --session $SESSION_ID \
  --role assistant \
  --content "import pandas as pd\n\ndf = pd.read_csv('data.csv')"
```

## Listing and Viewing

```bash
# List all sessions
node dist/index.js list sessions

# List messages in a session
node dist/index.js list messages --session $SESSION_ID

# View statistics
node dist/index.js stats
node dist/index.js stats --session $SESSION_ID
```

## Exporting

```bash
# Export as JSON
node dist/index.js export $SESSION_ID --format json > my-session.json

# Export as Markdown
node dist/index.js export $SESSION_ID --format markdown > my-session.md
```
