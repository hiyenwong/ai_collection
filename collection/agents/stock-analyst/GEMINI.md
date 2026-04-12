# Gemini CLI Instructions

This agent is designed to work with Google Gemini CLI.

## Agent Details

- **Agent Name**: stock-analyst
- **Purpose**: AI agent for specialized tasks
- **Key Tools**: exec, read, write, edit

## Usage

Use Gemini in one-shot mode:

```bash
gemini "Use stock-analyst to {task_description}"
```

## Integration

This agent is part of the AI Collection. To integrate:

```bash
cd /path/to/ai_collection
# The agent is available at collection/agents/stock-analyst/
```

### System Prompt

For advanced Gemini CLI use, set system prompt from AGENT.md:

```bash
gemini --system-prompt "Read /path/to/ai_collection/collection/agents/stock-analyst/AGENT.md" -- "{task_description}"
```

---

*For more information, see the AI Collection README*
