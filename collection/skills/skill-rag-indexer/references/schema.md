# 数据库 Schema

## 表结构

### skills 表

主技能信息表。

```sql
CREATE TABLE skills (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  description TEXT,
  path TEXT NOT NULL,
  content_hash TEXT NOT NULL,
  created_at INTEGER NOT NULL,
  updated_at INTEGER NOT NULL,
  metadata TEXT NOT NULL
);
```

**字段说明**:
- `id`: 技能 ID（目录名）
- `name`: 技能名称
- `description`: 技能描述
- `path`: 文件系统路径
- `content_hash`: 内容 SHA-256 哈希（用于变更检测）
- `created_at`: 创建时间戳
- `updated_at`: 更新时间戳
- `metadata`: JSON 格式的元数据

### skill_chunks 表

技能内容分块表（用于更细粒度的搜索）。

```sql
CREATE TABLE skill_chunks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  skill_id TEXT NOT NULL,
  chunk_type TEXT NOT NULL,
  content TEXT NOT NULL,
  chunk_index INTEGER NOT NULL,
  FOREIGN KEY (skill_id) REFERENCES skills(id)
);
```

**字段说明**:
- `skill_id`: 关联的技能 ID
- `chunk_type`: 分块类型（description, instructions, keywords 等）
- `content`: 分块内容
- `chunk_index`: 分块索引

**索引**:
- `idx_chunks_skill_id`: 按 skill_id 加速查询

### vss_skills 虚拟表

技能向量表（sqlite-vss）。

```sql
CREATE VIRTUAL TABLE vss_skills
USING vss0(embedding(1536));
```

**维度**:
- OpenAI text-embedding-3-small: 1536
- OpenAI text-embedding-3-large: 3072
- Cohere embed-v3.0: 1024

### vss_chunks 虚拟表

分块向量表（sqlite-vss）。

```sql
CREATE VIRTUAL TABLE vss_chunks
USING vss0(embedding(1536));
```

### fts_skills 虚拟表

全文搜索表（FTS5）。

```sql
CREATE VIRTUAL TABLE fts_skills
USING fts5(
  name,
  description,
  instructions,
  activation_keywords,
  content = skills,
  content_rowid = rowid
);
```

## 查询示例

### 向量搜索

```sql
SELECT
  skills.*,
  vss_skills.distance
FROM vss_skills
JOIN skills ON vss_skills.rowid = skills.rowid
WHERE vss_search(vss_skills.embedding, vss_query_embedding(?))
ORDER BY distance ASC
LIMIT ?;
```

### 关键词搜索

```sql
SELECT
  skills.*,
  rank
FROM fts_skills
JOIN skills ON fts_skills.rowid = skills.rowid
WHERE fts_skills MATCH ?
ORDER BY rank ASC
LIMIT ?;
```

### 获取技能内容哈希

```sql
SELECT content_hash FROM skills WHERE id = ?;
```

### 获取索引统计

```sql
SELECT COUNT(*) as count FROM skills;
SELECT MAX(updated_at) as max_updated FROM skills;
```
