---
name: openclaw
version: v1.0.0
last_updated: 2026-05-17
description: OpenClaw AI agent framework — session-based multi-agent orchestration, skills system, and tool-calling runtime. Use when user mentions openclaw, claw, sessions_spawn, or needs help with the OpenClaw agent collection.
platforms: [claude-code, codex, hermes, opencode, openclaw]
---

# OpenClaw

## Description

OpenClaw is an AI agent framework that runs Claude-powered autonomous sessions. It provides a
skills system, multi-agent orchestration via `sessions_spawn`, and a curated collection of agents
and skills for coding, research, finance, and more. OpenClaw sessions have full tool access:
`exec`, `read`, `write`, `web_search`, and `process`.

Key features:
- **Skills** — reusable capability packages that activate on trigger keywords
- **Agents** — specialized autonomous assistants spawned via `sessions_spawn`
- **Multi-agent** — orchestrate parallel sub-sessions for complex workflows
- **Tool-native** — agents interact with files, shell, and web natively

## Activation Keywords

- openclaw
- open claw
- claw
- sessions_spawn
- openclaw agent
- openclaw skill

## Tools Used

- exec: Run shell commands and CLI tools
- read: Read files and documentation
- write: Create and update files
- process: Manage long-running background sessions
- web_search: Search the web for information

## Installation

OpenClaw runs as a session runtime — no local install required. To use the agent collection:

```bash
# Clone the collection
git clone https://github.com/hiyenwong/ai_collection

# Browse available skills
ls collection/skills/

# Browse available agents
ls collection/agents/
```

## Version Status

**Skill Version:** v1.0.0 (2026-05-17)
**Collection:** https://github.com/hiyenwong/ai_collection
**Docs:** https://docs.openclaw.ai

## Instructions for Agents

1. Identify the user's task and select the appropriate skill or agent
2. To spawn a sub-agent: use `sessions_spawn(task, agentId, model, thinking)`
3. Skills auto-activate when user messages match their trigger keywords
4. Use `exec` for shell operations, `read`/`write` for file operations
5. For long tasks, spawn a background session and poll for results
6. Report results clearly and suggest follow-up actions

### Spawning an Agent

```python
sessions_spawn(
    task="Analyze this dataset and create visualizations",
    agentId="data-analyst",
    model="claude-sonnet-4-6",
    thinking="high",
    runTimeoutSeconds=300
)
```

### Available Agent IDs

| Agent | Purpose |
|-------|---------|
| `fullstack-engineer` | Web development and architecture |
| `tech-cofounder` | Startup technical strategy |
| `research-agent` | Deep research and synthesis |
| `stock-analyst` | Financial data analysis |

## Examples

### Example 1: Spawn a Research Agent

**User:** Use OpenClaw to research quantum computing trends

**Agent:**
```python
sessions_spawn(
    task="Research the latest trends in quantum computing and summarize key findings",
    agentId="research-agent",
    model="claude-sonnet-4-6",
    thinking="high"
)
```

### Example 2: Use a Skill Directly

**User:** Use the stock-analysis skill to analyze AAPL

**Agent:**
```
# Activate stock-analysis skill
# Trigger: "stock analysis"
Analyze AAPL using technical indicators for the past 6 months
```

### Example 3: Multi-Agent Orchestration

**User:** Build a feature with parallel agents

**Agent:**
```python
# Spawn planner agent
sessions_spawn(task="Plan the feature architecture", agentId="tech-cofounder")

# Spawn implementer agent
sessions_spawn(task="Implement the feature", agentId="fullstack-engineer")
```

## Related Skills

- `claude-code` - Anthropic official coding agent
- `codex` - OpenAI Codex CLI
- `hermes-agent` - Nous Research multi-platform agent
- `opencode` - Open source coding agent
- `security-guardrails` - Prevents credential exposure (always active)
