# Hermes Agent Instructions

This agent is designed to work with Hermes Agent.

## Agent Details

- **Agent Name**: algorithm-engineer
- **Purpose**: AI agent for specialized tasks
- **Key Tools**: exec, read, write, edit

## Architecture

Hermes Agent uses this agent as a specialized worker. The agent should:

1. **Read the AGENT.md file** for context
2. **Read soul.md** for personality and voice
3. **Follow task instructions** from the planner

## Integration

This agent is part of the AI Collection. To integrate:

```bash
# The agent is available at:
/path/to/ai_collection/collection/agents/algorithm-engineer/

# Add to Hermes config:
{
  "agents": {
    "algorithm-engineer": {
      "system_prompt": "Read /path/to/ai_collection/collection/agents/algorithm-engineer/AGENT.md"
    }
  }
}
```

## Best Practices

1. **Always read AGENT.md first** for context
2. **Use soul.md** to maintain consistent personality
3. **Check examples/** for task patterns
4. **Use read/write tools** for file operations

---

*For more information, see the AI Collection README*
