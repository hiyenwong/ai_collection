# Gemini CLI Instructions

This agent is designed to work with Google Gemini CLI. Follow these instructions when using this agent with Gemini CLI:

1. **Agent Name**: {agent_name}
2. **Purpose**: {agent_purpose}
3. **Key Tools**: {tool_list}

## Usage

Use Gemini in one-shot mode:

```
gemini "Use {agent_name} to {task_description}"
```

## Integration

This agent is part of the AI Collection. To integrate:

```bash
cd /path/to/ai_collection
# The agent is available at collection/agents/{agent_name}/
```

### System Prompt

For advanced Gemini CLI use, set system prompt from AGENT.md:

```bash
gemini --system-prompt "Read /path/to/ai_collection/collection/agents/{agent_name}/AGENT.md" -- "{task_description}"
```

---

*For more information, see the AI Collection README*
