---
name: gemini-cli
description: **Source:** Google AI Gemini CLI
---

# Gemini CLI

**Source:** Google AI Gemini CLI
**Version:** Latest (2026-03-30)
**Homepage:** https://ai.google.dev/

---

## Description

Gemini CLI for one-shot Q&A, summaries, and generation. Use Gemini in one-shot
mode with a positional prompt (avoid interactive mode).

---

## Tools Used

- `exec` - Run gemini CLI commands
- `read` - Read files for context
- `write` - Write outputs

---

## Installation

### Install via Homebrew
```bash
brew install gemini-cli
```

### Verify Installation
```bash
gemini --version
```

### Authentication
Run `gemini` once interactively and follow the login flow.

---

## Instructions for Agents

1. **Use one-shot mode** - Pass prompt as positional argument
2. **Avoid interactive mode** - No PTY required
3. **Specify model if needed** - Use `--model <name>`
4. **Format output** - Use `--output-format json` for structured output

---

## Quick Start Commands

```bash
# Basic Q&A
gemini "Answer this question..."

# Specify model
gemini --model gemini-2.0-flash "Prompt..."

# JSON output
gemini --output-format json "Return JSON"

# Summarize file
gemini "Summarize this: $(cat file.txt)"
```

---

## Examples

### Example 1: Quick Question

**User:** 用 Gemini 解释一个概念

**Agent:**
```bash
gemini "Explain the concept of transformer attention mechanism"
```

### Example 2: Summarize Content

**User:** 总结这段文字

**Agent:**
```bash
gemini "Summarize the following text in Chinese: <text>"
```

---

## Activation Keywords

- gemini
- gemini-cli
- google ai
- gemini flash
- gemini pro

---

## Model Options

| Model | Speed | Quality | Use Case |
|-------|-------|---------|----------|
| gemini-2.0-flash | Fast | Good | Quick Q&A |
| gemini-2.0-pro | Medium | Best | Complex reasoning |

---

## Extensions

- List: `gemini --list-extensions`
- Manage: `gemini extensions <command>`

---

## Safety Notes

- Avoid `--yolo` for safety
- Use structured prompts for better results
- Check output before using in production

---

## Related Skills

- `claude-code` - Anthropic coding agent
- `opencode` - Open source coding agent
- `codex` - OpenAI coding agent
- `coding-agent` - Multi-agent orchestration