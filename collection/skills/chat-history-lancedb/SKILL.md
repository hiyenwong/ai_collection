---
name: chat-history-lancedb
description: "LanceDB-based chat history system with message storage, semantic search, and RAG context retrieval."
---

# Chat History LanceDB

## Description

基于 LanceDB 的聊天历史数据库系统，提供完整的消息存储、会话管理、向量语义搜索和 RAG 上下文检索功能。支持智谱AI/火山引擎嵌入向量，本地嵌入式存储，零外部服务依赖。

## Activation Keywords

- chat history
- 聊天历史
- chat history db
- lancedb
- 会话管理
- session management
- 语义搜索
- semantic search
- RAG
- 上下文检索
- 保存对话
- save conversation
- 搜索历史
- search history
- 导出对话
- export conversation

## Tools Used

- exec: 运行 CLI 命令进行数据库操作
- read: 读取导出的对话历史和配置文件
- write: 保存配置和导出的对话
- glob: 查找导入文件

## Installation

### Prerequisites

```bash
# Node.js 20.0+
node --version

# Install dependencies
cd collection/skills/chat-history-lancedb
npm install

# Build TypeScript
npm run build
```

### Configure Environment

Copy `.env.example` to `.env` and configure:

```bash
cp .env.example .env
# Edit .env with your API keys
```

**Required for vector search:**
- `ZHIPU_API_KEY`: 智谱AI API Key (for embeddings-2)

**Optional:**
- `CHAT_HISTORY_DB_PATH`: 数据库存储路径 (默认: `~/.chat-history-lancedb`)
- `CHAT_HISTORY_EMBEDDING_PROVIDER`: `zhipu` 或 `volcengine`

### Verify Installation

```bash
# Show help
node dist/index.js --help

# Create a test session
node dist/index.js session create "Test Session"
```

## Usage Patterns

### Save a Message

```bash
chat-history save --session <session-id> --role user --content "Hello, how are you?"
```

### Search Chat History

```bash
# Semantic search (default)
chat-history search "how to use Python"

# Keyword search
chat-history search "how to use Python" --keyword

# Filter by session
chat-history search "how to use Python" --session <session-id>
```

### List Sessions and Messages

```bash
# List sessions
chat-history list sessions

# List messages in a session
chat-history list messages --session <session-id>
```

### Session Management

```bash
# Create a new session
chat-history session create "My Project"

# Rename a session
chat-history session rename <session-id> "New Title"
```

### Export and Import

```bash
# Export session to JSON
chat-history export <session-id> --format json > session.json

# Export session to Markdown
chat-history export <session-id> --format markdown > session.md
```

### RAG Context Retrieval

```bash
# Get RAG context for a query
chat-history rag "how do I fix this bug?" --format text
```

### Statistics

```bash
# Overall stats
chat-history stats

# Session-specific stats
chat-history stats --session <session-id>
```

## Instructions for Agents

When user requests chat history operations:

### Step 1: Parse Request

Identify the operation type:
- **Save/Store**: User wants to save messages/conversations
- **Search**: User wants to find past messages
- **Retrieve/RAG**: User wants context for LLM
- **Manage**: Create/list/rename/delete sessions
- **Export/Import**: Transfer chat history

### Step 2: Check Configuration

Verify setup before proceeding:

```bash
# Check if skill directory exists
cd collection/skills/chat-history-lancedb

# Check if node_modules exists
ls -la node_modules

# If not installed:
npm install && npm run build
```

### Step 3: Execute Operation

Based on the request type:

#### Save Messages

1. Create a session if needed:
   ```bash
   node dist/index.js session create "Session Title"
   ```

2. Save each message:
   ```bash
   node dist/index.js save \
     --session <session-id> \
     --role user|assistant|system \
     --content "Message content"
   ```

#### Search History

1. Choose search mode based on query:
   - **Semantic**: For conceptual queries ("how do I...", "what is...")
   - **Keyword**: For exact terms (error messages, function names)
   - **Hybrid**: Best of both (default)

2. Execute search:
   ```bash
   node dist/index.js search "your query" [--semantic|--keyword]
   ```

#### RAG Context Retrieval

1. For LLM context requests:
   ```bash
   node dist/index.js rag "user's question" --format text
   ```

2. Include the output in your LLM prompt as context.

#### Session Management

```bash
# List sessions
node dist/index.js list sessions

# View session messages
node dist/index.js list messages --session <id>

# Export for backup
node dist/index.js export <id> --format json > backup.json
```

### Step 4: Format Output

Present results in user-friendly format:

- **Search results**: Show score, role, and content snippet
- **Session lists**: Show title, last updated, message count
- **RAG context**: Present in clear, structured format for LLM
- **Exports**: Offer JSON (for machines) and Markdown (for humans)

### Step 5: Handle Errors

Common issues and fixes:

- **Embedding provider error**: Check API key in .env
- **Database not found**: Initialize by creating a session first
- **Permission denied**: Check db_path permissions
- **Node not found**: Ensure node_modules installed and built

## Context Files

The skill uses these context files when available:

### .env

```bash
# Database path
CHAT_HISTORY_DB_PATH=~/.chat-history-lancedb

# Embedding provider
CHAT_HISTORY_EMBEDDING_PROVIDER=zhipu

# Zhipu AI
ZHIPU_API_KEY=your_api_key_here
ZHIPU_EMBEDDING_MODEL=embeddings-2

# Search defaults
CHAT_HISTORY_SEARCH_LIMIT=10
CHAT_HISTORY_SEARCH_MIN_SCORE=0.5
```

### CHAT_HISTORY_PREFERENCES.md (Optional)

```markdown
# Chat History Preferences

## Default Session
# Auto-save to this session
default_session: <session-id>

## Auto-Save
auto_save: true
auto_save_interval: 5m

## Search Preferences
default_search_mode: hybrid
default_limit: 15
```

## Error Handling

### Embedding Provider Errors

```
If you see "Embedding provider required" or API errors:
  1. Check that .env file exists in the skill directory
  2. Verify ZHIPU_API_KEY is set correctly
  3. Try keyword search as fallback: add --keyword flag
  4. Fallback to basic CRUD without vector search
```

### Database Initialization Errors

```
If you see "Database not initialized":
  1. Create a session first to initialize:
     node dist/index.js session create "First Session"
  2. Verify db_path is writable
  3. Check that node_modules are installed: npm install
```

### Module Not Found Errors

```
If you see "Cannot find module" errors:
  1. cd to collection/skills/chat-history-lancedb
  2. Run: npm install
  3. Run: npm run build
  4. Retry the command
```

## Configuration

### CLI Options

**Global Options:**
- `--db-path <path>`: Override database path
- `--env-file <path>`: Path to .env file

**Search Options:**
- `--semantic`: Force semantic search
- `--keyword`: Force keyword search
- `--session <id>`: Filter by session
- `--limit <n>`: Max results (default: 10)
- `--min-score <0-1>`: Minimum relevance score

**Export Options:**
- `--format json|markdown`: Output format
- `--output <path>`: Save to file

## Advanced Usage

### Batch Import Conversations

```bash
# Import from JSON file
node dist/index.js import conversations.json

# The JSON format should be:
# {
#   "session": { "title": "Imported Session", ... },
#   "messages": [
#     { "role": "user", "content": "...", ... },
#     ...
#   ]
# }
```

### Semantic Search with Filtering

```bash
# Search within a specific session
chat-history search "how to debug" --session <id> --limit 20

# Filter by minimum score
chat-history search "how to debug" --min-score 0.7
```

### RAG Integration Pattern

When using with an LLM:

```javascript
// 1. Get RAG context
const context = await exec(`chat-history rag "${userQuery}" --format text`);

// 2. Build prompt
const prompt = `
Context from past conversations:
${context}

User question: ${userQuery}

Please answer based on the context above.
`;

// 3. Send to LLM
```

## Limitations

- **No real-time sync**: Local file-based storage only
- **Keyword search limitations**: Simple substring matching (not full FTS5)
- **Embedding API required**: Vector search needs Zhipu/Volcengine API key
- **No built-in UI**: CLI-only interface
- **Single-user design**: Optimized for personal use, not multi-tenant

## Best Practices

1. **Use meaningful session titles**: Helps with organization and search
2. **Auto-generate embeddings**: Default behavior, better search results
3. **Regular exports**: Backup important conversations
4. **Archive old sessions**: Keep list clean, use tags
5. **Combine search modes**: Use hybrid search for best results
6. **Monitor API usage**: Embedding API calls have costs

## Examples

### Example 1: Save a Conversation

```
User: "Save this conversation:
User: How do I use Python for data analysis?
Assistant: You can use pandas and numpy..."

Agent Process:
1. Create a session
2. Save user message
3. Save assistant message
4. Output session ID for future reference

Executes:
cd collection/skills/chat-history-lancedb
npm run build  # if needed

SESSION_ID=$(node dist/index.js session create "Python Data Analysis")
node dist/index.js save --session $SESSION_ID --role user --content "How do I use Python for data analysis?"
node dist/index.js save --session $SESSION_ID --role assistant --content "You can use pandas and numpy..."

Agent: "Conversation saved! Session ID: $SESSION_ID"
```

### Example 2: Semantic Search

```
User: "Find past conversations about machine learning"

Agent Process:
1. Identify search mode: semantic (conceptual query)
2. Execute search
3. Present results with relevance scores

Executes:
node dist/index.js search "machine learning" --semantic

Agent:
"Found 5 relevant conversations:

[85%] User: How do I train a neural network...
[78%] Assistant: For classification tasks, you can use...
[72%] User: What's the difference between supervised...
..."
```

### Example 3: RAG Context Retrieval

```
User: "Help me fix that bug we discussed yesterday about database connections"

Agent Process:
1. Retrieve relevant context
2. Build prompt with context
3. Answer using the retrieved information

Executes:
node dist/index.js rag "database connection bug fix" --format text

Agent includes context in its response...
```

### Example 4: Export and Backup

```
User: "Export my 'Project Alpha' session as Markdown"

Agent Process:
1. Find session ID for "Project Alpha"
2. Export to Markdown
3. Save to file or display

Executes:
# First list sessions to find ID
node dist/index.js list sessions

# Then export
node dist/index.js export <session-id> --format markdown > project-alpha.md

Agent: "Exported to project-alpha.md"
```

## Troubleshooting

### Issue: npm install fails

```bash
# Try clearing cache
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

### Issue: Build fails with TypeScript errors

```bash
# Make sure you're using correct Node version
node --version  # Should be >= 20

# Reinstall dependencies
rm -rf node_modules
npm install
npm run build
```

### Issue: Can't connect to Zhipu API

```bash
# Verify API key is correct
echo $ZHIPU_API_KEY

# Test with curl
curl -X POST "https://open.bigmodel.cn/api/paas/v4/embeddings" \
  -H "Authorization: Bearer $ZHIPU_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "embeddings-2", "input": "test"}'
```

### Issue: Database is locked or corrupted

```bash
# Backup first
cp -r ~/.chat-history-lancedb ~/.chat-history-lancedb.backup

# Try creating a fresh database
# (export what you can first)
rm -rf ~/.chat-history-lancedb
# Re-initialize by creating a session
```

## Resources

- **LanceDB Documentation**: https://lancedb.com/docs
- **Zhipu AI Embeddings API**: https://open.bigmodel.cn/dev/api/vector-embeddings
- **Volcano Engine (火山引擎)**: https://www.volcengine.com/docs/6451
- **Project README**: See README.md in skill directory
- **LanceDB GitHub**: https://github.com/lancedb/lancedb

## Related Skills

- **skill-rag-indexer**: For indexing and searching skills (uses similar architecture)
- **stock-analysis**: For Python-based skill pattern reference
- **research-agent**: Can use chat history for context-aware research
