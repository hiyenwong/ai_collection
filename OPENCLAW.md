# OPENCLAW.md

This file provides guidance to OpenClaw when working with code in this repository.

## Language & Communication
- Respond to the user in **Chinese (简体中文)**.
- Technical terms and code-related discussions can remain in English.

## OpenClaw Configuration
- **Skills Directory**: `~/.openclaw/skills/` (local) and `collection/skills/` (this repo)
- **Memory File**: `MEMORY.md` for long-term memory
- **Workspace**: `/Users/hiyenwong/.openclaw/workspace/`

## Skill Activation
- Skills are activated by keyword matching from SKILL.md `description` field
- Skills from this repo should be symlinked or copied to `~/.openclaw/skills/`

## Tools Available
- `exec`: Execute shell commands
- `read/write/edit`: File operations
- `web_search/web_fetch`: Web access
- `memory_search/memory_get`: Memory retrieval
- `sessions_spawn`: Spawn sub-agents
- `cron`: Schedule automated tasks

## Project Overview
This repository contains AI agent skills for OpenClaw:
- Each skill in `collection/skills/` has a `SKILL.md` file
- Follow the skill workflow when activation keywords match

## Integration
- Skills from this collection can be imported to OpenClaw via symlink
- Command: `ln -s /path/to/ai_collection/collection/skills/[skill] ~/.openclaw/skills/[skill]`

## Git Behavior
- **Commit Style**: Conventional Commits
- Use `exec` tool for git operations