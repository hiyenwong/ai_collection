# [Agent Name]

## Purpose
[Clear, concise description of what this agent does and why it exists]

## Model
- **Primary:** [Default model, e.g., claude-sonnet-4.5]
- **Alternative:** [Alternative model, optional]
- **Fallback:** [Fallback model, optional]

## Tools
- [tool1]: [Description of usage]
- [tool2]: [Description of usage]
- [tool3]: [Description of usage]

## Skills
- [skill1]: [Description]
- [skill2]: [Description]

## System Prompt
```
[Detailed system prompt describing agent's role, behavior, and instructions]
```

## Activation
[How this agent is activated - manual spawn, automatic trigger, etc.]

## Usage Examples

### Basic Usage
```python
sessions_spawn(
    task="[Task description]",
    agentId="[agent-id]",
    model="claude-sonnet-4.5",
    thinking="medium"
)
```

### Advanced Usage
```python
sessions_spawn(
    task="""
    [Detailed task description with parameters]
    """,
    agentId="[agent-id]",
    model="claude-opus-4.5",
    thinking="high",
    deliver=true,
    cleanup="keep"
)
```

## Configuration
```json
{
    "agentId": "[agent-id]",
    "model": "default",
    "thinking": "medium",
    "timeoutSeconds": 300,
    "tools": ["tool1", "tool2", "tool3"],
    "skills": ["skill1", "skill2"],
    "deliver": true,
    "cleanup": "delete"
}
```

## Best Practices
- [Best practice 1]
- [Best practice 2]
- [Best practice 3]

## Examples
See `examples/` directory for detailed examples.

## Notes
[Any important notes, limitations, or special considerations]
