# OPENCODE.md

This file provides guidance to OpenCode when working with code in this repository.

## Language & Communication
- Respond to the user in **Chinese (简体中文)**.
- Technical terms and code-related discussions can remain in English.

## Tech Stack & Commands
- **Environment**: Use `conda` to manage Python environments.
- **Package Manager**: Use `uv` for dependency management.
  - Install: `uv pip install -r requirements.txt`
- **Linting**: Use `ruff check --fix` and `ruff format`
- **Testing**: Use `pytest tests/`

## Git Behavior
- **Commit Style**: Conventional Commits (e.g., `feat:`, `fix:`, `chore:`)

## Coding Standards
- **Type Hints**: Required for all function signatures
- **Documentation**: Google-style docstrings

## Project Structure
- **Skills**: `collection/skills/` - Each skill has `SKILL.md`
- **Agents**: `collection/agents/` - Each agent has `AGENT.md`

## Skill Activation
When user mentions skill keywords, read the corresponding `SKILL.md` and execute the workflow.

## OpenCode Specific
- OpenCode reads `OPENCODE.md` for project context
- Skills in `collection/skills/` are available for activation
- Use `opencode` CLI command to invoke OpenCode models