# SKILL.md Template

This is the standard template for creating new skills in the collection.

## Required Sections

Every SKILL.md must include:

1. **# Skill Name** - Title with English name
2. **## Description** - 1-2 sentence summary
3. **## Activation Keywords** - List of trigger phrases
4. **## Tools Used** - Required tools with descriptions
5. **## Instructions for Agents** - Step-by-step workflow
6. **## Examples** - Usage examples

## Optional Sections

Include when applicable:

- **## Installation** - Setup instructions
- **## Usage Patterns** - Common use cases
- **## Context Files** - Related configuration files
- **## Error Handling** - Error recovery
- **## Configuration** - Settings and env vars
- **## Advanced Features** - Expert usage
- **## Best Practices** - Recommendations
- **## Limitations** - Known constraints
- **## Resources** - External references
- **## Related Skills** - Complementary skills
- **## Notes** - Additional information

---

# [Skill Name]

## Description
[Brief description (1-2 sentences) of what this skill does]

## Activation Keywords
- [keyword1]
- [keyword2]
- [keyword3]

## Tools Used
- [tool1]: [Description of usage]
- [tool2]: [Description of usage]

## Installation (if applicable)
```bash
# Installation commands
```

### Prerequisites
- [Requirement 1]
- [Requirement 2]

## Usage Patterns

### Operation 1
```bash
# Command example
```
[Description of operation]

### Operation 2
```bash
# Command example
```
[Description of operation]

## Instructions for Agents

[Step-by-step instructions for agents to follow when this skill is activated]

### Step 1: [Action]
[Detailed instructions]

### Step 2: [Action]
[Detailed instructions]

### Step 3: [Action]
[Detailed instructions]

## Context Files

The skill uses these context files when available:

### [FILENAME].md
```markdown
# [Context file description]

[Content or structure]
```

## Error Handling

### [Error Type]
```
If you see "[error message]":
  [Recovery step 1]
  [Recovery step 2]
  [Fallback action]
```

## Configuration

### Environment Variables (Optional)
```bash
export [VARIABLE_NAME]="value"
```

### Configuration File (Optional)
```bash
# Config file location
/path/to/config
```

## Advanced Usage

[Advanced patterns, tips, and tricks]

## Limitations

- [Limitation 1]
- [Limitation 2]

## Best Practices

1. [Best practice 1]
2. [Best practice 2]
3. [Best practice 3]

## Examples

### Example 1: [Scenario]
```
User: "[User request]"

Agent Process:
1. [Step 1]
2. [Step 2]
3. [Step 3]

[Executes: command]

Agent: [Confirmation message]
```

## Troubleshooting

### [Issue 1]
```bash
# Solution
```

### [Issue 2]
```bash
# Solution
```

## Resources

- [Documentation URL]
- [API Reference URL]
- [Related Tools/Projects]

## Related Skills
- [skill1]: [Brief description]
- [skill2]: [Brief description]

## Notes

[Additional information not covered above]
