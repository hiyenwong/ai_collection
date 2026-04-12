# GitHub Copilot CLI Instructions

This agent is designed to work with GitHub Copilot CLI. Follow these instructions when using this agent with Copilot CLI:

1. **Agent Name**: {agent_name}
2. **Purpose**: {agent_purpose}
3. **Key Tools**: {tool_list}

## Usage

When user wants to use this agent with Copilot CLI:

```
copilot "{task_description} using {agent_name}"
```

## Configuration

Add this agent to Copilot CLI configuration:

```json
{
  "agents": {
    "{agent_name}": {
      "description": "{agent_purpose}",
      "tools": "{tool_list}"
    }
  }
}
```

## Best Practices

1. **Use clear task descriptions**
2. **Reference agent purpose**
3. **Leverage agent's specialized tools**

---

*For more information, see the AI Collection README*
