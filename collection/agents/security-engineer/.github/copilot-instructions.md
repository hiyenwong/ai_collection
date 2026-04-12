# GitHub Copilot CLI Instructions

This agent is designed to work with GitHub Copilot CLI.

## Agent Details

- **Agent Name**: security-engineer
- **Purpose**: AI agent for specialized tasks
- **Key Tools**: exec, read, write, edit

## Usage

When user wants to use this agent with Copilot CLI:

```bash
copilot "{task_description} using security-engineer"
```

## Configuration

Add this agent to Copilot CLI configuration:

```json
{
  "agents": {
    "security-engineer": {
      "description": "AI agent for specialized tasks",
      "tools": "exec, read, write, edit"
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
