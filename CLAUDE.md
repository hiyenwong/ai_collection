# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

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

## References

- **OpenClaw Docs**: https://docs.openclaw.ai
- **Agent Guide**: `docs/agents/creation-guide.md`
- **Skill Guide**: `docs/skills/creation-guide.md`
- **Integration**: `docs/integration/agents-skills.md`
- **Contributing**: `CONTRIBUTING.md`
