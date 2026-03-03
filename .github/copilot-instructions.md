# 项目指南 (Project Guidelines)

## 代码风格 (Code Style)
- **环境与包管理**: 使用 `conda` 管理基础环境，使用 `uv` 进行依赖管理。
- **Linting & 格式化**: 使用 `ruff`。在提交代码前需运行 `ruff check --fix` 和 `ruff format`。
- **类型提示 (Type Hints)**: 所有函数签名强制要求包含类型提示。
- **文档规范**: 对于复杂逻辑，强制使用 Google 风格的 docstrings。

## 架构 (Architecture)
此项目是 **OpenClaw 代理 (Agents) 和技能 (Skills)** 的集合库。
- **代理 (Agents)** 存放在 `collection/agents/` 目录中。每个代理必需包含 `AGENT.md`，定义其目的、模型、工具及系统提示词。
- **技能 (Skills)** 存放在 `collection/skills/` 目录中。每个技能必需包含 `SKILL.md`，定义触发关键词、使用工具及详细指令。
- 遵循 `templates/agent-template.md` 和 `templates/skill-template.md` 创建新内容。

## 构建与测试 (Build and Test)
- **依赖安装**: `uv pip install -r requirements.txt` 或 `uv pip install <package>`
- **测试执行**: 运行 `pytest tests/`。在提交代码 (Commit) 之前，必须确保 `ruff` 检查通过且 `pytest` 测试成功。

## 项目约定 (Project Conventions)
- **Git 提交**: 严格遵循 Conventional Commits 规范 (例如 `feat:`, `fix:`, `chore:`)。保持提交原子化，精简并聚焦。
- **内容语言**: 向用户回复时优先使用 **中文 (简体中文)**，技术术语和代码相关讨论可保持英文。
- **上下文管理**: 使用 `.claudeignore` (参考根目录配置) 排除不需要被索引的文件 (如 `__pycache__/`, `node_modules/` 等) 以优化 Token 使用。新任务应该在干净的环境中开启以避免上下文污染。
- **代理开发准则**: 任何新的代理能力均需要遵循 [agentskills.io](https://agentskills.io) 的规范。

## 继承与集成说明 (Integration Points)
- 代理与技能通过 `sessions_spawn` 机制进行多代理协同。代理负责“人设”和高层决策，技能通过关键词触发具体工作流。
