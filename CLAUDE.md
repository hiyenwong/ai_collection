# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Language & Communication
- Respond to the user in **Chinese (简体中文)**.
- Technical terms and code-related discussions can remain in English.

## Tech Stack & Commands
- **Environment**: Use `conda` to manage the base environment.
- **Package Manager**: Use `uv` for dependency management.
  - Install: `uv pip install -r requirements.txt` or `uv pip install <package>`
- **Linting**: Use `ruff`.
  - Command: `ruff check --fix` and `ruff format`
- **Testing**: Use `pytest`.
  - Command: `pytest tests/`
  - Run single test: `pytest tests/path/to/test_file.py::test_function`

## Git Behavior
- **Commit Style**: Conventional Commits (e.g., `feat:`, `fix:`, `chore:`).
- **Atomic Commits**: Keep changes small and focused.
- **Pre-flight Check**: Before any commit, ensure `ruff` passes and `pytest` succeeds.

## Coding Standards
- **Type Hints**: Mandatory for all function signatures.
- **Documentation**: Use Google-style docstrings for complex logic.
- **Skills**: Follow the agentskills.io specification for any new agent capabilities.

## Project Overview

This is a curated collection of **OpenClaw agents** and **skills** - a documentation and configuration repository for the OpenClaw AI agent framework. The repository contains definitions, templates, and examples for extending OpenClaw's capabilities.

### Key Concepts

**Agents** (代理): Autonomous AI assistants that run in isolated sessions via OpenClaw's `sessions_spawn` system. Each agent has:
- A dedicated system prompt defining its role and behavior
- Specific model selection optimized for its tasks
- Optional access to specialized skills
- Ability to spawn sub-agents for complex workflows

**Skills** (技能): Reusable capability packages that extend agent behavior. Skills are:
- Activated automatically by trigger keywords in user messages
- Define specialized workflows and tool usage patterns
- Contain step-by-step instructions for agents to follow
- Independent of any specific agent

**Relationship**: Agents provide the "persona" and high-level behavior; skills provide specific, repeatable workflows. An agent can use multiple skills, and skills can be shared across different agents.

## Repository Structure

```
collection/
├── agents/          # Agent packages (each with AGENT.md)
└── skills/          # Skill packages (each with SKILL.md)

docs/
├── agents/          # Agent creation guides
├── skills/          # Skill creation guides
└── integration/     # How agents and skills work together

templates/           # Templates for creating new agents/skills
```

## Adding New Content

### Creating a New Agent

1. Create directory: `collection/agents/your-agent-name/`
2. Copy `templates/agent-template.md` to `AGENT.md`
3. Fill in required sections: Purpose, Model, Tools, System Prompt, Activation, Usage Examples, Configuration
4. Add optional subdirectories: `examples/`, `references/`, `assets/`
5. Update `AGENTS.md` with an entry for the new agent

### Creating a New Skill

1. Create directory: `collection/skills/your-skill-name/`
2. Copy `templates/skill-template.md` to `SKILL.md`
3. Fill in required sections: Description, Activation Keywords, Tools Used, Instructions for Agents, Error Handling, Examples
4. Add optional subdirectories: `examples/`, `references/`, `scripts/`, `assets/`
5. Update `SKILLS.md` with an entry for the new skill

## Conventions

### Naming
- **Directories**: lowercase with hyphens (`research-agent`, `apple-notes`)
- **Agent IDs**: Match directory name exactly
- **Markdown headings**: Title Case

### Git Workflow
- **Branch naming**: `feat(agent):`, `feat(skill):`, `fix:`, `docs:`
- **Commit format**: Conventional Commits (`type(scope): subject`)
- **Types**: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`

### File Formats

**AGENT.md** must include:
```markdown
# Agent Name
## Purpose
## Model (Primary/Alternative)
## Tools
## Skills
## System Prompt (code block)
## Activation
## Usage Examples
## Configuration (JSON)
## Best Practices
```

**SKILL.md** must include:
```markdown
# Skill Name
## Description
## Activation Keywords (specific phrases)
## Tools Used
## Installation (if applicable)
## Usage Patterns
## Instructions for Agents (step-by-step)
## Error Handling
## Examples
## Resources
```

## Integration Patterns

From `docs/integration/agents-skills.md`:

1. **Agent with Skills**: Agent uses specific skills for specialized tasks
2. **Tool Wrapper Skills**: Skills that wrap external CLI tools
3. **Skill Chaining**: Multiple skills used sequentially for complex workflows
4. **Agent Spawning Agents**: Multi-agent orchestration via `sessions_spawn`

## Key Architecture Notes

- Agents run in isolated sessions spawned via `sessions_spawn(task, agentId, ...)`
- Skills activate when user messages contain trigger keywords
- Both agents and skills can use built-in tools (exec, read, write, web_search, etc.)
- Skills are designed to be tool-agnostic - they instruct agents on which tools to use and how

## Existing Agents & Skills

### Agents in this Collection

| Agent | Location | Purpose | Key Skills |
|-------|----------|---------|-----------|
| **fullstack-engineer** | `collection/agents/fullstack-engineer/` | 高级全栈工程师，专注于现代Web开发、可扩展架构和生产级代码 | opencode, claude-code, openspec |
| **tech-cofounder** | `collection/agents/tech-cofounder/` | 技术联合创始人，提供创业项目的技术战略和执行指导 | - |
| **research-agent** | `collection/agents/research-agent/` | 研究专家，用于深度调研和信息综合 | - |
| **stock-analyst** | `collection/agents/stock-analyst/` | 股票分析师，专注于金融数据分析 | akshare, stock-analysis |

### Skills in this Collection

| Skill | Location | Purpose | Activation Keywords |
|-------|----------|---------|-------------------|
| **opencode** | `collection/skills/opencode/` | 开源AI编程代理，支持多代理编排和ultrawork模式 | opencode, ultrawork, ulw |
| **claude-code** | `collection/skills/claude-code/` | Anthropic官方AI编程助手 | claude-code, anthropic coding |
| **openspec** | `collection/skills/openspec/` | 规格驱动开发框架，使用Gherkin语法 | openspec, gherkin, bdd |
| **akshare** | `collection/skills/akshare/` | 中国金融数据接口库 | stock data, akshare |
| **stock-analysis** | `collection/skills/stock-analysis/` | 股票分析技能，提供技术指标和可视化 | stock analysis, technical indicators |

## Project Structure Deep Dive

### Key Files

- **`AGENTS.md`**: 代理的总体文档和使用指南
- **`SKILLS.md`**: 技能的总体文档和使用指南
- **`CONTRIBUTING.md`**: 贡献指南和检查清单
- **`templates/agent-template.md`**: 创建新代理的模板
- **`templates/skill-template.md`**: 创建新技能的模板

### Directory Organization

```
collection/
├── agents/
│   ├── agent-name/
│   │   ├── AGENT.md          # 代理定义（必需）
│   │   ├── README.md         # 用户友好的说明
│   │   ├── examples/         # 使用示例
│   │   ├── references/       # 参考文档
│   │   └── assets/           # 图片等资源
│   └── ...
└── skills/
    ├── skill-name/
    │   ├── SKILL.md          # 技能定义（必需）
    │   ├── examples/         # 使用示例
    │   ├── references/       # 参考文档（如API文档）
    │   ├── scripts/          # 辅助脚本（Python等）
    │   └── assets/           # 图片等资源
    └── ...
```

### Common Tasks

#### Adding a New Agent

1. 从模板创建目录结构
2. 填写 `AGENT.md` 的所有必需章节
3. 添加示例和参考资料
4. 更新 `AGENTS.md` 索引

#### Adding a New Skill

1. 从模板创建目录结构
2. 定义具体的激活关键词（避免通用词汇）
3. 编写详细的分步指令
4. 添加错误处理策略
5. 更新 `SKILLS.md` 索引

#### Working with Python Scripts

项目中的Python脚本（如 `stock-analysis/scripts/`）应遵循：
- 使用类型提示
- 使用 Google 风格文档字符串
- 通过 `ruff check --fix` 进行 linting
- 通过 `ruff format` 进行格式化

## References

- **OpenClaw Docs**: https://docs.openclaw.ai
- **Agent Guide**: `docs/agents/creation-guide.md`
- **Skill Guide**: `docs/skills/creation-guide.md`
- **Integration**: `docs/integration/agents-skills.md`
- **Contributing**: `CONTRIBUTING.md`
