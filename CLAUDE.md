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

Skills are organized into category subdirectories under `collection/skills/`. Each category contains fewer than 1,000 entries.

| Skill | Location | Purpose | Activation Keywords |
|-------|----------|---------|-------------------|
| **opencode** | `collection/skills/agent-tools/opencode/` | 开源AI编程代理，支持多代理编排和ultrawork模式 | opencode, ultrawork, ulw |
| **claude-code** | `collection/skills/agent-tools/claude-code/` | Anthropic官方AI编程助手 | claude-code, anthropic coding |
| **openspec** | `collection/skills/agent-tools/openspec/` | 规格驱动开发框架，使用Gherkin语法 | openspec, gherkin, bdd |
| **akshare** | `collection/skills/agent-tools/akshare/` | 中国金融数据接口库 | stock data, akshare |
| **stock-analysis** | `collection/skills/agent-tools/stock-analysis/` | 股票分析技能，提供技术指标和可视化 | stock analysis, technical indicators |
| **consulting-report-search** | `collection/skills/agent-tools/consulting-report-search/` | 咨询/行业报告搜索与问答，优先使用艾瑞咨询免费报告 | 咨询报告搜索, 行业报告问答, 艾瑞报告, iresearch report |
| **taiyi-jinhua-meditation** | `collection/skills/agent-tools/taiyi-jinhua-meditation/` | 指导基于《太乙金华宗旨》的道家冥想 | 冥想, meditation, 太乙金华宗旨, 回光守中 |
| **security-guardrails** | `collection/skills/agent-tools/security-guardrails/` | 防止暴露密码/API Key/数据库凭据等敏感信息，所有代理强制激活 | default on (all agents) |

### Skill Categories

| Category | Path | Description |
|----------|------|-------------|
| `agent-tools` | `collection/skills/agent-tools/` | Agent frameworks, CLI tools, workflow utilities |
| `ai-safety-eval` | `collection/skills/ai-safety-eval/` | AI safety, alignment, evaluation, benchmarks |
| `data-retrieval` | `collection/skills/data-retrieval/` | Data pipelines, search, retrieval, RAG |
| `deployment-optimization` | `collection/skills/deployment-optimization/` | MLOps, model serving, quantization, compression |
| `general-ml` | `collection/skills/general-ml/` | General ML/DL concepts, training, optimization |
| `healthcare-bio` | `collection/skills/healthcare-bio/` | Medical AI, bioinformatics, drug discovery |
| `knowledge-graph` | `collection/skills/knowledge-graph/` | KG construction, graph neural networks, ontology |
| `multi-agent-rl` | `collection/skills/multi-agent-rl/` | Multi-agent systems, reinforcement learning, robotics |
| `neuroscience` | `collection/skills/neuroscience/` | Brain networks, EEG, cognitive science, neuroimaging |
| `nlp-llm` | `collection/skills/nlp-llm/` | Language models, transformers, NLP tasks |
| `other` | `collection/skills/other/` | Uncategorized skills |
| `physics-math` | `collection/skills/physics-math/` | Physics-informed ML, mathematical methods |
| `quantum` | `collection/skills/quantum/` | Quantum computing, quantum ML, quantum sensing |
| `reasoning-bayesian` | `collection/skills/reasoning-bayesian/` | Bayesian inference, causal reasoning, uncertainty |
| `security-privacy` | `collection/skills/security-privacy/` | Cryptography, privacy, adversarial ML, compliance |
| `signal-control-systems` | `collection/skills/signal-control-systems/` | Signal processing, control theory, time series |
| `software-engineering` | `collection/skills/software-engineering/` | Code generation, dev tools, testing, infrastructure |
| `spiking-neuromorphic` | `collection/skills/spiking-neuromorphic/` | SNNs, neuromorphic computing, spike-based models |
| `vision-generative` | `collection/skills/vision-generative/` | Computer vision, generative models, GANs, diffusion |

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
    ├── agent-tools/          # Agent 框架、CLI 工具
    ├── ai-safety-eval/       # AI 安全、对齐、评估
    ├── data-retrieval/       # 数据管道、搜索、RAG
    ├── deployment-optimization/  # MLOps、模型服务
    ├── general-ml/           # 通用 ML/DL
    ├── healthcare-bio/      # 医疗 AI、生物信息学
    ├── knowledge-graph/      # 知识图谱、GNN
    ├── multi-agent-rl/       # 多智能体、强化学习
    ├── neuroscience/          # 神经科学、EEG
    ├── nlp-llm/              # 语言模型、NLP
    ├── other/                # 未分类
    ├── physics-math/         # 物理启发的 ML、数学方法
    ├── quantum/              # 量子计算、量子 ML
    ├── reasoning-bayesian/   # 贝叶斯推理、因果推理
    ├── security-privacy/     # 安全、隐私
    ├── signal-control-systems/ # 信号处理、控制理论
    ├── software-engineering/ # 软件工程
    ├── spiking-neuromorphic/ # 脉冲神经网络
    ├── vision-generative/    # 计算机视觉、生成模型
    ├── README.md             # 技能总览
    └── SKILL.md              # 技能规范
```

### Common Tasks

#### Adding a New Agent

1. 从模板创建目录结构
2. 填写 `AGENT.md` 的所有必需章节
3. 添加示例和参考资料
4. 更新 `AGENTS.md` 索引

#### Adding a New Skill

1. 从模板创建目录结构
2. 确定分类（参考上方 Skill Categories 表）
3. 在对应分类目录下创建：`collection/skills/<category>/<skill-name>/`
4. 定义具体的激活关键词（避免通用词汇）
5. 编写详细的分步指令
6. 添加错误处理策略
7. 更新 `SKILLS.md` 索引，并在需要时同步 `CLAUDE.md` 中的技能清单

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
