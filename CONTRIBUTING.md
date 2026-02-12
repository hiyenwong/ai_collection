# Contributing to AI Collection

Thank you for your interest in contributing to the AI Collection! This repository is a community-driven collection of OpenClaw agents and skills.

## Types of Contributions

We welcome contributions in the following areas:

### 1. Adding New Agents
- Create a new agent with a specific purpose
- Document its capabilities and usage
- Provide examples and configuration

### 2. Adding New Skills
- Create a skill that extends OpenClaw capabilities
- Write comprehensive SKILL.md documentation
- Include examples and reference materials

### 3. Improving Documentation
- Fix typos or clarify existing docs
- Add tutorials or guides
- Translate documentation to other languages

### 4. Bug Reports
- Report issues with existing agents or skills
- Suggest improvements or new features

### 5. Examples and Templates
- Add real-world usage examples
- Create new templates for common use cases

## Getting Started

### 1. Fork and Clone

```bash
# Fork the repository on GitHub
git clone https://github.com/YOUR_USERNAME/ai_collection.git
cd ai_collection
```

### 2. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-fix-name
```

### 3. Make Your Changes

Follow the [Agent Creation Guide](./docs/agents/creation-guide.md) or [Skill Creation Guide](./docs/skills/creation-guide.md).

### 4. Commit Your Changes

```bash
git add .
git commit -m "feat: add new data-analysis agent"

# Or for fixes
git commit -m "fix: correct skill activation keywords"
```

### 5. Push and Create PR

```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub.

## Contribution Guidelines

### Agents

**What makes a good agent contribution:**

- ✅ Clear, specific purpose
- ✅ Well-documented system prompt
- ✅ Tested with multiple tasks
- ✅ Examples of usage
- ✅ Appropriate model selection
- ✅ Error handling strategies

**Agent Checklist:**

- [ ] Created directory in `collection/agents/agent-name/`
- [ ] Created `AGENT.md` with all required sections
- [ ] Added usage examples in `examples/`
- [ ] Tested agent with `sessions_spawn`
- [ ] Updated main `AGENTS.md` with entry
- [ ] Added references if needed

### Skills

**What makes a good skill contribution:**

- ✅ Specific, uncommon activation keywords
- ✅ Comprehensive, step-by-step instructions
- ✅ Error handling for common issues
- ✅ Multiple usage examples
- ✅ Reference documentation
- ✅ Tested with various prompts

**Skill Checklist:**

- [ ] Created directory in `collection/skills/skill-name/`
- [ ] Created `SKILL.md` with all required sections
- [ ] Added usage examples in `examples/`
- [ ] Added reference docs in `references/` if needed
- [ ] Added helper scripts in `scripts/` if applicable
- [ ] Updated main `SKILLS.md` with entry
- [ ] Tested skill activation with trigger keywords

## Code Style

### Markdown

- Use consistent heading hierarchy
- Include code fences for code blocks
- Add alt text for images
- Keep lines under 100 characters

### Python/Script Files

- Follow PEP 8 style guide
- Use descriptive variable names
- Add docstrings to functions
- Include error handling

### Comments

- Explain "why", not "what"
- Keep comments concise
- Use `#` for single-line comments
- Use `"""` for multi-line docstrings

## Documentation Standards

### AGENT.md Must Include

```markdown
# Agent Name

## Purpose
[Clear description]

## Model
- Primary: [model]
- Alternative: [model]

## Tools
- [tool]: [usage]

## Skills
- [skill]: [description]

## System Prompt
```
[Detailed prompt]
```

## Activation
[How agent is activated]

## Usage Examples
[Examples]

## Configuration
[JSON config]

## Best Practices
[List]
```

### SKILL.md Must Include

```markdown
# Skill Name

## Description
[Brief description]

## Activation Keywords
- [keyword1]
- [keyword2]

## Tools Used
- [tool]: [usage]

## Installation
[If applicable]

## Usage Patterns
[Examples]

## Instructions for Agents
[Step-by-step]

## Error Handling
[Common errors]

## Examples
[Real-world examples]

## Resources
[Links]
```

## Testing

### Testing Agents

1. **Manual Testing:**
```python
# Test with simple task
sessions_spawn(task="test task", agentId="your-agent")

# Test with complex task
sessions_spawn(task="complex task with parameters", agentId="your-agent", thinking="high")
```

2. **Check:**
- Agent follows system prompt
- Appropriate tools are used
- Results are delivered correctly
- Errors are handled gracefully

### Testing Skills

1. **Trigger Testing:**
```
User: "[use trigger keyword]"
```
2. **Verify:**
- Agent reads SKILL.md
- Instructions are followed
- Tools are used correctly
- Common errors are handled

## Pull Request Process

### PR Title Format

- **New Agent:** `feat(agent): add new data-analysis agent`
- **New Skill:** `feat(skill): add new slack-integration skill`
- **Bug Fix:** `fix(agent): resolve timeout issue in research-agent`
- **Documentation:** `docs: update agent creation guide`
- **Refactoring:** `refactor(skills): improve error handling`

### PR Description

```markdown
## Description
[Brief description of changes]

## Changes
- [ ] Added new agent/skill
- [ ] Updated documentation
- [ ] Added examples
- [ ] Fixed bugs

## Testing
[Describe how you tested your changes]

## Screenshots (if applicable)
[Attach screenshots]

## Related Issues
Closes #123
```

## Review Process

1. **Automated Checks:**
   - CI/CD tests pass
   - No linting errors

2. **Manual Review:**
   - Code quality
   - Documentation completeness
   - Examples accuracy
   - Overall usefulness

3. **Approval:**
   - At least one maintainer approval
   - Address all review comments

## Community Guidelines

### Be Respectful

- Welcome new contributors
- Provide constructive feedback
- Acknowledge good work
- Help others learn

### Be Collaborative

- Discuss ideas openly
- Seek consensus on big changes
- Credit contributors
- Share knowledge

### Be Patient

- Review may take time
- Maintainers are volunteers
- Ask questions if unclear

## Getting Help

If you need help contributing:

1. **Check Documentation:**
   - [Agent Creation Guide](./docs/agents/creation-guide.md)
   - [Skill Creation Guide](./docs/skills/creation-guide.md)
   - Existing examples in `collection/`

2. **Open an Issue:**
   - Describe your question clearly
   - Include what you've tried
   - Reference existing agents/skills

3. **Join the Community:**
   - [OpenClaw Discord](https://discord.gg/clawd)
   - Open an issue labeled "question"

## Recognition

All contributors will be credited in:

- This CONTRIBUTING.md file
- Project README.md
- Individual agent/skill documentation

## License

By contributing, you agree that your contributions will be licensed under the same license as the repository (MIT).

---

Thank you for contributing! 🚀
