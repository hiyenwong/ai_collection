# openai-research-monitor - OpenAI Research 自动监控与技能创建

## Description

自动监控 OpenAI Research 网站，发现新内容后按照论文处理流程创建技能并加入知识库。

**位置：** `~/.openclaw/workspace/openai-research-monitor/`

## Activation Keywords

- openai research
- monitor openai
- openai 论文监控
- openai research monitor

## Core Concepts

### 工作流程

```
每小时检查 → 发现新内容 → 提取研究信息 → 创建技能 → 加入知识库
```

### 组件

| 组件 | 作用 |
|------|------|
| `openai_research_monitor.py` | 主监控脚本 |
| `state.json` | 状态记录（已知研究） |
| `browser-use` | 浏览器自动化 |
| `knowledge.db` | 知识库 |

## Step-by-Step Instructions

### 1. 运行监控（手动）

```bash
cd ~/.openclaw/workspace/openai-research-monitor
source .venv/bin/activate
python openai_research_monitor.py
```

### 2. 设置定时任务（每小时）

```bash
# 添加到 crontab
crontab -e

# 添加以下行（每小时执行）
0 * * * * cd /Users/hiyenwong/.openclaw/workspace/openai-research-monitor && source .venv/bin/activate && python openai_research_monitor.py >> /tmp/openai-monitor.log 2>&1
```

### 3. 检查监控结果

```bash
# 查看日志
tail -f /tmp/openai-monitor.log

# 查看状态
cat ~/.openclaw/workspace/openai-research-monitor/state.json
```

### 4. 手动添加研究为技能

```python
# 如果手动发现研究，可以用这个脚本
research = {
    "title": "GPT-5 Technical Report",
    "url": "https://openai.com/research/gpt-5",
    "date": "2026-03-29",
    "authors": ["OpenAI"],
    "description": "GPT-5 model architecture and training...",
    "key_points": [
        "Mixture of Experts architecture",
        "Chain-of-thought reasoning",
        "Multimodal capabilities"
    ]
}

skill_name = create_skill_from_research(research)
update_knowledge_db(research, skill_name)
```

## Tools Used

- `browser-use` - 浏览器自动化（访问 OpenAI 网站）
- `exec` - 运行监控脚本
- `read` - 查看状态和日志
- `sqlite3` - 操作知识库

## Configuration

### 代理设置

脚本已配置代理 `127.0.0.1:7890`，存储在 `MEMORY.md` 中。

### 检查频率

- 推荐：每小时一次
- 最小：每 30 分钟（避免被封）
- 最大：每天一次

## Example Use Cases

### 1. 手动触发一次监控

```bash
cd ~/.openclaw/workspace/openai-research-monitor
source .venv/bin/activate
python openai_research_monitor.py
```

### 2. 查看已发现的研究

```bash
cat ~/.openclaw/workspace/openai-research-monitor/state.json | jq .
```

### 3. 重置监控状态

```bash
rm ~/.openclaw/workspace/openai-research-monitor/state.json
```

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: 运行监控（手动）

## Examples

### Example 1: Basic Application

**User:** I need to apply openai-research-monitor - OpenAI Research 自动监控与技能创建 to my analysis.

**Agent:** I'll help you apply openai-research-monitor. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for openai-research-monitor?

**Agent:** Let me search for the latest research and best practices...

## Related Skills

- `arxiv-search` - arXiv 论文搜索
- `skill-creator` - 技能创建
- `sqlite-knowledge-graph` - 知识库管理

## Notes

- browser-use 需要 Chrome/Chromium 浏览器
- 首次运行会下载 Chromium
- OpenAI 网站可能有 Cloudflare 保护
- 如果被封，增加检查间隔

---

**Created:** 2026-03-29 12:15
**Author:** Aerial