---
name: template
description: "Template agent for rapid agent prototyping. Copy and customize this template to create new agents."
category: template
---

# Template Agent

## Purpose

A minimal template agent for rapid agent prototyping and development.

## Model

- **Primary:** claude-sonnet-4.5
- **Alternative:** claude-haiku-4.5
- **Fallback:** claude-sonnet-4

## Tools

- read: Read files and documentation
- write: Create new files
- edit: Modify existing files
- exec: Execute commands
- glob: Find files by pattern

## Skills

None (template agent)

## System Prompt

```
You are a helpful AI assistant. This is a template agent for prototyping.
Customize this system prompt for your specific use case.
```

## Activation

Manual spawn only - not automatically activated

## Usage Examples

### Basic Usage

```python
sessions_spawn(
    task="Example task",
    agentId="template",
    model="claude-sonnet-4.5",
    thinking="medium"
)
```

## Configuration

```json
{
    "agentId": "template",
    "model": "claude-sonnet-4.5",
    "thinking": "medium",
    "timeoutSeconds": 300,
    "tools": ["read", "write", "edit", "exec", "glob"],
    "skills": [],
    "deliver": true,
    "cleanup": "delete"
}
```

## Best Practices

- Copy this template to create new agents
- Customize the system prompt for your use case
- Define appropriate tools and skills
- Set appropriate model and thinking parameters

## Notes

This is a minimal template. Add content as needed for specific use cases.
