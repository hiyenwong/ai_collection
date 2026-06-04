# Skill RAG Indexer

本地技能文档的 RAG 索引器，提供语义搜索和智能推荐功能。

## 功能特性

- 🔍 **语义搜索**: 使用向量嵌入进行智能搜索
- 🎯 **智能推荐**: 根据任务描述推荐相关技能
- 🔤 **关键词搜索**: 基于 FTS5 的全文搜索
- ⚡ **混合搜索**: 结合语义和关键词的最佳结果
- 📦 **本地优先**: SQLite + sqlite-vss，零外部依赖
- 🚀 **增量更新**: 只索引变更的内容

## 快速开始

### 1. 安装依赖

```bash
cd collection/skills/skill-rag-indexer
npm install
```

### 2. 配置环境变量

创建 `.env` 文件：

```bash
EMBEDDING_PROVIDER=openai
OPENAI_API_KEY=sk-your-api-key-here
```

或者使用 Cohere：

```bash
EMBEDDING_PROVIDER=cohere
COHERE_API_KEY=your-api-key-here
```

### 3. 构建索引

```bash
npm run build
npm run index:build
```

### 4. 开始使用

```bash
# 搜索技能
npm run search -- "股票分析"

# 推荐技能
npm run recommend -- "构建一个 Web 应用"

# 查看状态
npm run index:status
```

## 使用说明

### CLI 命令

```bash
# 索引管理
skill-rag index build    # 构建完整索引
skill-rag index update   # 增量更新
skill-rag index status   # 查看状态

# 搜索
skill-rag search <query> [options]
  -k, --keyword          # 仅关键词搜索
  -s, --semantic         # 仅语义搜索 (默认)
  -y, --hybrid           # 混合搜索
  -l, --limit <n>        # 结果数量

# 推荐
skill-rag recommend <task> [options]
  -l, --limit <n>        # 推荐数量
  --include <skills>     # 只包含指定技能
  --exclude <skills>     # 排除指定技能
```

### 搜索示例

```bash
# 语义搜索
skill-rag search "我需要分析金融数据"

# 关键词搜索
skill-rag search --keyword "python"

# 混合搜索
skill-rag search "web 开发" --hybrid --limit 5
```

### 推荐示例

```bash
# 为任务推荐
skill-rag recommend "创建一个新的 agent"

# 只包含特定技能
skill-rag recommend "编程" --include opencode,claude-code
```

## 项目结构

```
skill-rag-indexer/
├── SKILL.md              # 技能定义
├── README.md             # 本文件
├── package.json          # 依赖配置
├── tsconfig.json         # TypeScript 配置
├── .env.example          # 环境变量示例
├── src/
│   ├── index.ts          # CLI 入口
│   ├── core/             # 核心模块
│   │   ├── database.ts   # SQLite + sqlite-vss
│   │   ├── embeddings.ts # 嵌入生成
│   │   ├── parser.ts     # SKILL.md 解析
│   │   ├── indexer.ts    # 索引构建
│   │   └── searcher.ts   # 搜索和推荐
│   ├── cli/              # CLI 命令
│   ├── types/            # TypeScript 类型
│   └── utils/            # 工具函数
└── examples/             # 使用示例
```

## 技术栈

- **Node.js 20+**: 运行时
- **TypeScript**: 类型安全
- **better-sqlite3**: SQLite 驱动
- **sqlite-vss**: 向量搜索扩展
- **OpenAI/Cohere API**: 嵌入生成
- **Commander.js**: CLI 框架
- **marked**: Markdown 解析

## 配置

### 环境变量

| 变量 | 说明 | 默认值 |
|------|------|--------|
| `EMBEDDING_PROVIDER` | 嵌入提供商 | `openai` |
| `OPENAI_API_KEY` | OpenAI API 密钥 | - |
| `COHERE_API_KEY` | Cohere API 密钥 | - |
| `EMBEDDING_MODEL` | 嵌入模型 | `text-embedding-3-small` |
| `SKILL_RAG_DB_PATH` | 数据库路径 | `./skills-index.db` |
| `SKILL_RAG_DEFAULT_LIMIT` | 默认结果数 | `10` |
| `SKILL_RAG_MIN_SCORE` | 最低分数 | `0.5` |
| `SKILL_RAG_HYBRID_WEIGHT` | 混合权重 | `0.7` |

### 配置文件

可选的 `.skill-rag-indexer.json`:

```json
{
  "databasePath": "./skills-index.db",
  "embeddingsProvider": "openai",
  "embeddingsModel": "text-embedding-3-small",
  "skillsRoot": "../../collection/skills",
  "search": {
    "defaultLimit": 10,
    "minScore": 0.5,
    "hybridWeight": 0.7
  }
}
```

## 开发

```bash
# 构建
npm run build

# 监听模式
npm run dev

# 测试
npm test

# 手动测试
npm run index:status
```

## 常见问题

### sqlite-vss 加载失败

```bash
npm rebuild sqlite-vss
```

### 数据库被锁定

检查并终止挂起的进程：

```bash
ps aux | grep node
pkill -f "skill-rag"
```

### 找不到技能

检查 `skillsRoot` 路径配置，确保 `collection/skills/` 目录存在。

## License

MIT
