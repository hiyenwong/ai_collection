# Skill Structure Reference

This document defines the structure and conventions for SKILL.md files in the collection.

## Directory Structure

Each skill resides in its own directory:

```
collection/skills/
└── [skill-name]/
    ├── SKILL.md          # Required: Main skill definition
    ├── README.md         # Optional: User-friendly guide
    ├── examples/         # Optional: Usage examples
    │   └── usage-examples.md
    ├── references/       # Optional: Reference documentation
    │   └── api-reference.md
    ├── scripts/          # Optional: Helper scripts
    │   └── helper.py
    └── assets/           # Optional: Images, diagrams
        └── diagram.png
```

## SKILL.md Structure

### 1. Header

```markdown
# [Skill Name]

## Description
[1-2 sentences describing what the skill does]
```

**Rules:**
- Title uses English, PascalCase or kebab-case
- Description is concise and actionable
- Start with what it does, not how

### 2. Activation Keywords

```markdown
## Activation Keywords
- [keyword1]
- [keyword2]
- [keyword3]
```

**Rules:**
- 5-10 keywords recommended
- Include both Chinese and English
- Be specific enough to avoid false positives
- Use lowercase unless proper noun

**Good Examples:**
- "kdj indicator", "布林带", "gherkin syntax"

**Bad Examples:**
- "help", "do", "make" (too generic)
- "A", "The", "And" (not keywords)

### 3. Tools Used

```markdown
## Tools Used
- [tool1]: [Description of usage]
- [tool2]: [Description of usage]
```

**Available Tools:**
- `read`: Read files from filesystem
- `write`: Write/create files
- `edit`: Edit existing files
- `exec`: Execute shell commands
- `glob`: Pattern-based file search
- `grep`: Content search
- `memory`: Store/retrieve session memory

### 4. Instructions for Agents

```markdown
## Instructions for Agents

### Step 1: [Action Name]
[Detailed instructions for this step]

### Step 2: [Action Name]
[More instructions]

### Step 3: [Action Name]
[Final instructions]
```

**Guidelines:**
- Use imperative language ("Fetch data", not "Fetches data")
- Be specific about tool usage
- Include conditional logic
- Provide examples when helpful

### 5. Examples

```markdown
## Examples

### Example 1: [Scenario Name]
```
User: "[Actual user request]"

Agent Process:
1. [What agent does]
2. [Next action]
3. [Final action]

Agent: "[Agent response]"
```
```

**Rules:**
- Show realistic user requests
- Include agent's thought process
- Show the final output
- Cover common use cases

## Naming Conventions

### Skill Names
- Use lowercase with hyphens: `stock-analysis`, `api-tester`
- Use simple, descriptive names
- Avoid acronyms unless widely known

### File Names
- `SKILL.md` - Always capitalized
- `examples/usage-examples.md` - lowercase
- `references/api-docs.md` - lowercase

### Section Headers
- Use Title Case for main sections
- Use Sentence case for subsections

## Content Guidelines

### Description Format
```
[Action verb] [object] [prepositional phrase]

Examples:
- "Fetches stock data using AkShare API"
- "Generates tests from OpenAPI specifications"
- "Formats Markdown with consistent style"
```

### Instruction Format
```
[Action] + [Details] + [Expected Outcome]

Example:
"Fetch stock data using the AkShare library with the
specified symbol and period. Return a pandas DataFrame
with OHLCV data."
```

### Example Format
```
Context: [Brief scenario]

User: "[Input]"
Agent: [Process and output]
```

## Format Compliance

### Markdown Standards
- Use CommonMark syntax
- Headers: `##` for sections, `###` for subsections
- Code blocks: Specify language (```python, ```bash)
- Lists: Use `-` for unordered, `1.` for ordered
- Bold for emphasis: `**important**`
- Italic for terms: `*term*`

### Required Fields
| Field | Required? | Format |
|-------|-----------|--------|
| # Title | Yes | `# Skill Name` |
| Description | Yes | 1-2 sentences |
| Activation Keywords | Yes | List format |
| Tools Used | Yes | List with descriptions |
| Instructions | Yes | Step-by-step |
| Examples | Yes | At least 1 |

### Optional Fields
| Field | When to Include |
|-------|-----------------|
| Installation | External dependencies needed |
| Usage Patterns | Multiple common patterns |
| Context Files | Uses specific config files |
| Error Handling | Known error scenarios |
| Configuration | Settings or env vars |
| Advanced Features | Expert usage patterns |
| Best Practices | Recommendations |
| Limitations | Known constraints |
| Resources | External references |
| Related Skills | Complementary skills exist |

## Validation Checklist

Before submitting a skill, verify:

- [ ] SKILL.md exists in skill directory
- [ ] All required sections are present
- [ ] Activation keywords are specific
- [ ] Tools are correctly listed
- [ ] Instructions are step-by-step
- [ ] At least one example is included
- [ ] Markdown syntax is valid
- [ ] No broken code blocks
- [ ] File follows naming convention
- [ ] Links are valid (if any)

## Common Pitfalls

### 1. Vague Instructions
❌ Bad: "Analyze the data"
✅ Good: "Fetch data using API, calculate indicators, generate chart"

### 2. Generic Keywords
❌ Bad: "help", "do", "make"
✅ Good: "kdj indicator", "git commit", "api test"

### 3. Missing Examples
❌ Bad: No examples section
✅ Good: At least 2 realistic examples

### 4. Unclear Tool Usage
❌ Bad: "use tools to do stuff"
✅ Good: "Use `exec` to run Python script for data processing"

### 5. Incomplete Sections
❌ Bad: Empty or placeholder content
✅ Good: "N/A" or omit if truly not applicable

## Integration with Project

### Updating SKILLS.md
When adding a new skill, add an entry:

```markdown
### [Skill Name]
| **Skill** | **Location** | **Purpose** |
|-----------|--------------|-------------|
| **[skill-name]** | `collection/skills/[skill-name]/` | [Brief description] |
```

### Memory System
For cross-session learning, update memory:

```markdown
## Extracted Skills
| Date | Skill | Source |
|------|-------|--------|
| 2026-02-19 | stock-analysis | User requested stock analysis 3+ times |
```
