---
name: codex-cli
description: **Source:** OpenAI Codex CLI
---

# Codex CLI

**Source:** OpenAI Codex CLI
**Version:** v0.117.0 (2026-03-30)
**Homepage:** https://github.com/openai/codex

---

## Description

OpenAI's official AI coding agent CLI. Codex helps with code generation,
debugging, and understanding codebases using OpenAI's latest models.

---

## Tools Used

- `exec` - Run codex CLI commands
- `process` - Manage background sessions
- `read` - Read code files
- `write` - Write code files

---

## Installation

### Install via npm
```bash
npm install -g @openai/codex
```

### Verify Installation
```bash
codex --version
```

### Authentication
Set `OPENAI_API_KEY` environment variable or run `codex auth`.

---

## Version Check

**Skill Version:** v0.117.0 (2026-03-30)
**Latest Release:** [Check GitHub](https://github.com/openai/codex/releases/latest)

### Update Codex
```bash
npm update -g @openai/codex
```

---

## Instructions for Agents

1. **Use PTY mode** - Codex requires interactive terminal
2. **Background execution** - Use `background: true` for long tasks
3. **Set working directory** - Use `workdir` parameter

---

## Usage Patterns

### Basic Command
```bash
codex exec "Your prompt here"
```

### With PTY (Required)
```bash
# Use exec tool with pty: true
codex exec "Explain this codebase"
```

### Background Mode
```bash
# For long-running tasks
codex exec --background "Implement feature X"
```

---

## Examples

### Example 1: Code Generation

**User:** 用 Codex 生成一个函数

**Agent:**
```bash
codex exec "Write a Python function that calculates fibonacci numbers"
```

### Example 2: Code Review

**User:** 让 Codex 审查代码

**Agent:**
```bash
codex exec "Review the code in src/main.py and suggest improvements"
```

---

## Activation Keywords

- codex
- openai codex
- codex cli
- @openai/codex

---

## Model Options

Codex uses OpenAI's latest reasoning models:
- GPT-4o
- o1-mini
- o1

---

## CLI Commands

| Command | Description |
|---------|-------------|
| `codex exec <prompt>` | Execute a prompt |
| `codex --version` | Check version |
| `codex auth` | Authenticate |
| `codex --help` | Show help |

---

## PTY Mode Note

**Codex requires PTY mode** because it's an interactive terminal application:

```javascript
// Correct usage in OpenClaw
exec({
  command: "codex exec 'Your task'",
  pty: true,
  workdir: "/path/to/project"
})
```

---

## Safety Notes

- Review generated code before using
- Use `--dry-run` if available to preview changes
- Set appropriate file permissions

---

## Related Skills

- `claude-code` - Anthropic coding agent
- `opencode` - Open source coding agent
- `gemini-cli` - Google Gemini CLI
- `coding-agent` - Multi-agent orchestration