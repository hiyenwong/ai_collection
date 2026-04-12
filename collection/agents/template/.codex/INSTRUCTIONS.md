# Codex Instructions

This agent is designed to work with OpenAI Codex. Follow these instructions when using this agent with Codex:

1. **Agent Name**: {agent_name}
2. **Purpose**: {agent_purpose}
3. **Key Tools**: {tool_list}

## Usage

When user wants to use this agent with Codex:

1. Use `codex` command with the agent's purpose
2. Reference AGENT.md for context
3. Use soul.md for personality guidance

## Example

```
codex "Use {agent_name} to {task_description}"
```

## Integration

This agent is part of the AI Collection. To integrate:

```bash
cd /path/to/ai_collection
# The agent is available at collection/agents/{agent_name}/
```

---

*For more information, see the AI Collection README*
