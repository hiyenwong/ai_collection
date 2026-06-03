# Chat History LanceDB

基于 LanceDB 的聊天历史数据库系统，提供向量语义搜索和 RAG 上下文检索功能。

## Features

- 消息存储与会话管理
- 向量语义搜索（基于智谱AI/火山引擎）
- RAG 上下文检索
- 导出/导入（JSON/Markdown）
- 本地嵌入式存储（零外部服务依赖）
- 完整的 CLI 工具

## Quick Start

```bash
# 1. Install
cd collection/skills/chat-history-lancedb
npm install
npm run build

# 2. Configure
cp .env.example .env
# Edit .env with your ZHIPU_API_KEY

# 3. Use
node dist/index.js session create "My First Session"
node dist/index.js save --session <id> --role user --content "Hello!"
node dist/index.js search "Hello"
```

## Documentation

See [SKILL.md](./SKILL.md) for complete documentation.

## CLI Commands

```bash
chat-history save              # Save a message
chat-history search <query>    # Search history
chat-history list sessions     # List sessions
chat-history list messages     # List messages
chat-history session create    # Create session
chat-history export <id>       # Export session
chat-history stats             # Get statistics
chat-history rag <query>       # RAG context retrieval
```

## License

MIT
