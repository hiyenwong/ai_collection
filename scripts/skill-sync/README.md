# Skill Sync Tool

AI 编码工具 Skills 同步工具，支持多平台 skills 的收集、合并和分发。

## 功能特性

- ✅ **收集**: 扫描所有平台的 skills
- ✅ **合并**: 支持主导模式（以某平台为准）或合并模式
- ✅ **分发**: 同步到各目标工具
- ✅ **格式转换**: 自动转换 SKILL.md 到各工具格式
- ✅ **增量同步**: 基于修改时间智能合并

## 支持的工具

| 工具 | 状态 | 同步方式 |
|------|------|---------|
| OpenClaw | ✅ | 符号链接 |
| Claude Code | ✅ | 复制 + 转换 |
| OpenCode | ✅ | 复制 + 转换 |
| Cursor | ⏳ | 符号链接 (需启用) |
| Gemini | ⏳ | 符号链接 (需启用) |

## 快速开始

```bash
cd ~/projects/ai_collection/scripts/skill-sync

# 查看状态
python3 sync.py status

# 收集所有 skills
python3 sync.py collect

# 同步所有（以中央仓库为主导）
python3 sync.py sync --all --master central

# 同步到特定工具
python3 sync.py sync --target openclaw

# 合并所有平台（无主导）
python3 sync.py sync --all --merge
```

## 配置

编辑 `config.json`:

```json
{
  "source": "~/projects/ai_collection/collection/skills",
  "targets": [
    {
      "name": "openclaw",
      "path": "~/.agents/skills",
      "format": "openclaw",
      "mode": "symlink",
      "enabled": true
    }
  ]
}
```

## 同步模式

### 主导模式 (--master)
以指定平台的 skills 为准，其他平台的独有 skills 会被添加进来。

```bash
python3 sync.py sync --all --master central
```

### 合并模式 (--merge)
所有平台的 skills 合并，相同 skill 以最新修改时间为准。

```bash
python3 sync.py sync --all --merge
```

## 目录结构

```
skill-sync/
├── config.json       # 配置文件
├── sync.py           # 主脚本
├── converters/       # 格式转换器
│   ├── claude.py     # Claude Code 格式
│   └── opencode.py   # OpenCode 格式
├── sync.log          # 同步日志
└── README.md         # 本文档
```

## 扩展

添加新的目标工具：

1. 编辑 `config.json`，添加新目标
2. 如需格式转换，在 `converters/` 添加转换器
3. 运行 `python3 sync.py sync --target <name>`

## 注意事项

- 符号链接模式：修改会直接影响中央仓库
- 复制模式：目标文件独立，不会影响源
- 建议定期运行 `sync.py status` 检查差异