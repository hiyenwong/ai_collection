# LanceDB Schema Reference

## Tables

### `messages` Table

Stores individual chat messages with vector embeddings.

| Column | Type | Description |
|--------|------|-------------|
| `message_id` | string | UUID primary key |
| `session_id` | string | Foreign key to sessions |
| `role` | string | user/assistant/system/tool |
| `content` | string | Message content |
| `timestamp` | int64 | Unix timestamp (ms) |
| `parent_message_id` | string | For threading (nullable) |
| `metadata` | json | Additional metadata (nullable) |
| `tags` | list<string> | Tags (nullable) |
| `content_hash` | string | SHA-256 of content |
| `embedding` | vector<float> | Vector embedding (dimension: 1024) |

### `sessions` Table

Stores chat session metadata.

| Column | Type | Description |
|--------|------|-------------|
| `session_id` | string | UUID primary key |
| `title` | string | Session title |
| `created_at` | int64 | Creation timestamp |
| `updated_at` | int64 | Last update timestamp |
| `metadata` | json | Additional metadata (nullable) |
| `tags` | list<string> | Tags (nullable) |
| `message_count` | int32 | Cached message count (nullable) |

## Indexing

### Vector Index

The `embedding` column uses LanceDB's IVF_PQ index for fast similarity search.

### Scalar Indexes

- `session_id` on messages table
- `timestamp` on messages table
- `created_at` / `updated_at` on sessions table

## Query Examples

### Vector Search

```typescript
// Semantic similarity search
const results = await messagesTable
  .search(embedding)
  .where(`session_id = '${sessionId}'`)
  .limit(10)
  .toArray();
```

### Filtered Query

```typescript
// Get session messages ordered by time
const messages = await messagesTable
  .where(`session_id = '${sessionId}'`)
  .sort([{ column: 'timestamp', order: 'asc' }])
  .limit(100)
  .toArray();
```
