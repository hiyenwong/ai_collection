# GEMINI.md

This file provides guidance to Gemini CLI when working with code in this repository.

## Language & Communication
- Respond to the user in **Chinese (简体中文)**.
- Technical terms and code-related discussions can remain in English.

## Tech Stack & Commands
- **Environment**: Use `conda` to manage Python environments.
- **Package Manager**: Use `uv` for dependency management.
  - Install: `uv pip install -r requirements.txt` or `uv pip install <package>`
- **Linting**: Use `ruff`.
  - Command: `ruff check --fix` and `ruff format`
- **Testing**: Use `pytest`.
  - Command: `pytest tests/`

## Git Behavior
- **Commit Style**: Conventional Commits (e.g., `feat:`, `fix:`, `chore:`).
- **Atomic Commits**: Keep changes small and focused.

## Coding Standards
- **Type Hints**: Mandatory for all function signatures.
- **Documentation**: Use Google-style docstrings.

## Project Overview
This repository is a **collection of AI Agent skills and configurations**.
- **Skills**: Located in `collection/skills/`. Each skill has a `SKILL.md` file defining activation keywords, tools, and workflow.
- **Agents**: Located in `collection/agents/`. Each agent has an `AGENT.md` file defining purpose and persona.

## Skill Activation
When user mentions keywords matching a skill's activation keywords, load the corresponding SKILL.md and follow its workflow.

## Gemini CLI Specific
- Use `gemini` command to invoke Gemini models
- Context file: `GEMINI.md` provides project-specific guidance
- Skills are discovered via keyword matching in SKILL.md files