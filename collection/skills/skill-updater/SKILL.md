---
name: skill-updater
description: 自动更新 AI 编码工具技能（Claude Code, OpenCode, Copilot CLI）。检查官方文档、GitHub releases、博客更新，使用 Claude Code 提炼技能，同步到 ai_collection 项目。
---

# Skill Updater

## 描述
自动更新 AI 编码工具技能，包括 Claude Code、OpenCode、Copilot CLI。定期检查官方文档、GitHub releases、博客更新，使用 Claude Code 进行技能提炼和开发，同步到 ai_collection GitHub 项目。

## 激活关键词
- skill-updater
- update coding skills
- sync skills
- skill maintenance

## 目标技能

| 技能 | GitHub 仓库 | 官方文档 | 博客 |
|------|------------|---------|------|
| claude-code | anthropics/claude-code | platform.claude.com/docs | claude.com/blog |
| opencode | anomalyco/opencode | opencode.ai/docs | - |
| copilot-cli | github/copilot-cli | docs.github.com/copilot | github.blog |

## 工作流程

### 阶段 1: 检查更新（自动化）

**数据源：**
1. GitHub Releases API
2. 官方文档变更
3. 博客 RSS/API

**检查频率：** 每日 02:00

### 阶段 2: 技能提炼（使用 Claude Code）

**触发条件：**
- 检测到版本更新
- 文档有重大变更
- 新功能发布

**提炼流程：**
1. 收集变更内容
2. 使用 Claude Code 分析变更
3. 更新 SKILL.md
4. 添加示例和最佳实践

### 阶段 3: 同步到 GitHub

**目标项目：** `/Users/hiyenwong/projects/ai_projects/ai_collection`

**同步步骤：**
1. 检查项目结构
2. 复制更新的技能文件
3. 使用 Claude Code 进行数据迁移
4. Commit 并 push

## 配置

### Cron 定时任务

```bash
# 每日 02:00 检查技能更新
0 2 * * * ~/.openclaw/cron/skill-updater-check.sh >> ~/.openclaw/logs/skill-updater.log 2>&1

# 每周日 03:00 完整同步
0 3 * * 0 ~/.openclaw/cron/skill-updater-sync.sh >> ~/.openclaw/logs/skill-updater.log 2>&1
```

### 环境变量

```bash
SKILL_UPDATE_DIR="$HOME/.openclaw/workspace/skill-updates"
AI_COLLECTION_DIR="$HOME/projects/ai_projects/ai_collection"
CLAUDE_CODE_CMD="claude-code"
```

## 使用方法

### 手动检查更新

```bash
# 检查单个技能
python3 ~/.openclaw/scripts/skill-updater.py check claude-code

# 检查所有技能
python3 ~/.openclaw/scripts/skill-updater.py check --all
```

### 手动触发同步

```bash
# 使用 Claude Code 提炼并同步
python3 ~/.openclaw/scripts/skill-updater.py sync claude-code --use-claude-code

# 同步所有技能到 ai_collection
python3 ~/.openclaw/scripts/skill-updater.py sync --all --push
```

### 查看更新日志

```bash
python3 ~/.openclaw/scripts/skill-updater.py log --days 7
```

## 输出文件

### 更新检查结果
```
~/.openclaw/workspace/skill-updates/
├── check-results.json      # 检查结果
├── claude-code/
│   ├── changes.md          # 变更摘要
│   ├── new-version.txt     # 新版本号
│   └── skill-update.md     # 技能更新内容
├── opencode/
│   └── ...
└── copilot-cli/
    └── ...
```

### 同步日志
```
~/.openclaw/logs/skill-updater.log
```

## 错误处理

### GitHub API 限流
- 使用 GH_TOKEN 提高限额
- 缓存结果避免重复请求
- 降级到网页抓取

### Claude Code 不可用
- 回退到手动编辑
- 记录待处理变更
- 稍后重试

### 同步失败
- 保留本地变更
- 记录冲突
- 提示手动解决

## 相关技能
- skill-extractor: 技能提取
- claude-code: Claude Code CLI
- github: GitHub 操作