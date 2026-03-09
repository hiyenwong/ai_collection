# AI 编码工具 Skill/Agent 格式对比 (2026-03-09)

## 版本信息

| 工具 | 当前版本 | 文档地址 |
|------|---------|---------|
| Claude Code | 最新 | https://code.claude.com/docs/en/skills.md |
| OpenCode | 1.2.22 | https://opencode.ai/docs |
| OpenClaw | 2026.3.8 | https://docs.openclaw.ai/tools/skills.md |

---

## Skill 格式对比

### 共同标准：AgentSkills

三个工具都遵循 **[AgentSkills](https://agentskills.io)** 开放标准。

### Skill 目录结构

```
skill-name/
├── SKILL.md           # 必需：主要指令文件
├── templates/         # 可选：模板文件
├── examples/          # 可选：示例文件
└── scripts/           # 可选：脚本文件
```

### SKILL.md Frontmatter 字段对比

| 字段 | Claude Code | OpenCode | OpenClaw | 说明 |
|------|-------------|----------|----------|------|
| `name` | ✅ | ✅ | ✅ | Skill 名称 |
| `description` | ✅ 推荐 | ✅ | ✅ | 描述，用于自动激活 |
| `argument-hint` | ✅ | ❓ | ❓ | 参数提示 |
| `disable-model-invocation` | ✅ | ✅ | ✅ | 禁止模型自动激活 |
| `user-invocable` | ✅ | ✅ | ✅ | 是否在 `/` 菜单显示 |
| `allowed-tools` | ✅ | ❓ | ❓ | 允许的工具列表 |
| `model` | ✅ | ❓ | ❓ | 使用的模型 |
| `context` | ✅ `fork` | ❓ | ❓ | 运行上下文 |
| `agent` | ✅ | ❓ | ❓ | Subagent 类型 |
| `hooks` | ✅ | ❓ | ❓ | 生命周期钩子 |
| `metadata` | ✅ | ✅ | ✅ | 元数据（JSON 对象）|

### OpenClaw 特有字段 (metadata.openclaw)

```yaml
metadata:
  {
    "openclaw": {
      "emoji": "♊️",
      "homepage": "https://example.com",
      "os": ["darwin", "linux"],
      "requires": {
        "bins": ["uv"],
        "env": ["GEMINI_API_KEY"],
        "config": ["browser.enabled"]
      },
      "primaryEnv": "GEMINI_API_KEY",
      "install": [
        {
          "id": "brew",
          "kind": "brew",
          "formula": "gemini-cli",
          "bins": ["gemini"]
        }
      ]
    }
  }
```

---

## Skill 存储位置

### Claude Code

| 位置 | 路径 | 范围 |
|------|------|------|
| Enterprise | 管理设置 | 组织级 |
| Personal | `~/.claude/skills/<name>/SKILL.md` | 用户级 |
| Project | `.claude/skills/<name>/SKILL.md` | 项目级 |
| Plugin | `<plugin>/skills/<name>/SKILL.md` | 插件级 |

优先级：Enterprise > Personal > Project > Plugin

### OpenCode

- 项目级：`AGENTS.md` (项目根目录)
- 配置文件：`~/.config/opencode/opencode.json`

### OpenClaw

| 位置 | 路径 | 范围 |
|------|------|------|
| Bundled | 内置 skills | 全局 |
| Managed | `~/.openclaw/skills/` | 用户级 |
| Workspace | `<workspace>/skills/` | 工作区级 |
| Extra | `skills.load.extraDirs` | 额外目录 |

优先级：Workspace > Managed > Bundled

---

## 创建 Skill 的最佳实践

### 1. 基础模板（通用）

```yaml
---
name: skill-name
description: 清晰描述 skill 的用途和触发条件
user-invocable: true
disable-model-invocation: false
---

# Skill 标题

主要指令内容...

## 使用方法

具体步骤...

## 示例

示例代码或用法...
```

### 2. OpenClaw 增强模板

```yaml
---
name: skill-name
description: 清晰描述 skill 的用途和触发条件
user-invocable: true
metadata:
  {
    "openclaw": {
      "emoji": "🔧",
      "homepage": "https://example.com",
      "requires": {
        "bins": ["required-cli"],
        "env": ["API_KEY"]
      },
      "install": [
        {
          "id": "brew",
          "kind": "brew",
          "formula": "package-name",
          "bins": ["cli-name"]
        }
      ]
    }
  }
---

# Skill 标题

主要指令内容...
```

### 3. Claude Code 增强模板

```yaml
---
name: skill-name
description: 清晰描述 skill 的用途和触发条件
user-invocable: true
allowed-tools: Read, Write, Edit, Bash
context: fork
---

# Skill 标题

主要指令内容...

## 支持文件

使用 `@path` 引用支持文件：
- @templates/example.md
- @scripts/validate.sh
```

---

## 同步注意事项

1. **核心字段兼容**：`name`, `description`, `user-invocable`, `disable-model-invocation` 在三个工具中都支持

2. **工具特定字段**：
   - Claude Code: `allowed-tools`, `context`, `agent`, `hooks`
   - OpenClaw: `metadata.openclaw.*`

3. **格式转换**：
   - Claude Code → OpenClaw：保持兼容
   - OpenClaw → Claude Code：忽略 `metadata.openclaw`
   - OpenCode：使用 AGENTS.md 格式

4. **文件引用**：
   - Claude Code: 使用 `@path` 语法
   - OpenClaw: 使用 `{baseDir}` 变量

---

## 更新日志

- **2026-03-09**: 初始创建，基于最新文档整理