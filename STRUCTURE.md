# Project Structure

This document provides a visual and detailed overview of the AI Collection project structure.

## Visual Overview

```
ai_collection/
├── 📄 README.md                    # Project overview and quick start
├── 📄 AGENTS.md                    # Agent documentation index
├── 📄 SKILLS.md                    # Skill documentation index
├── 📄 CONTRIBUTING.md               # Contribution guidelines
├── 📄 STRUCTURE.md                 # This file - project structure
│
├── 📁 docs/                        # General documentation
│   ├── 📁 agents/                  # Agent-specific guides
│   │   └── creation-guide.md        # How to create agents
│   │
│   ├── 📁 skills/                  # Skill-specific guides
│   │   └── creation-guide.md        # How to create skills
│   │
│   └── 📁 integration/             # Integration guides
│       └── agents-skills.md         # How agents and skills work together
│
├── 📁 collection/                  # Collected agents and skills
│   ├── 📁 agents/                  # Agent packages
│   │   ├── 📁 research-agent/       # Example: Research agent
│   │   │   ├── AGENT.md           # Agent definition
│   │   │   ├── 📁 examples/        # Usage examples
│   │   │   ├── 📁 references/      # Reference docs
│   │   │   └── 📁 assets/         # Images, diagrams
│   │   │
│   │   ├── 📁 data-analyst/        # Example: Data analyst
│   │   └── 📁 [your-agent]/        # Add your agents here
│   │
│   └── 📁 skills/                  # Skill packages
│       ├── 📁 apple-notes/          # Example: Apple Notes skill
│       │   ├── SKILL.md            # Skill definition
│       │   ├── 📁 examples/        # Usage examples
│       │   ├── 📁 references/      # API docs, guides
│       │   ├── 📁 scripts/         # Helper scripts
│       │   └── 📁 assets/         # Screenshots, diagrams
│       │
│       ├── 📁 weather/             # Example: Weather skill
│       └── 📁 [your-skill]/        # Add your skills here
│
├── 📁 templates/                   # Templates for creating new items
│   ├── agent-template.md           # Agent template
│   └── skill-template.md           # Skill template
│
└── 📁 resources/                   # External resources and links
    ├── external-links.md           # Curated external resources
    ├── tools-directory.md          # List of useful tools
    └── community.md              # Community resources
```

## Directory Details

### Root Files

#### README.md
- Project overview
- What's inside
- Quick start guide
- Contributing info

#### AGENTS.md
- Agent concept explained
- How agents work
- Agent types and characteristics
- When to use agents
- Agent configuration reference

#### SKILLS.md
- Skill concept explained
- How skills work
- Skill types and activation
- When to create skills
- Skill best practices

#### CONTRIBUTING.md
- Contribution guidelines
- How to add agents/skills
- Code style and documentation standards
- Testing guidelines
- PR process
- Community guidelines

### docs/ - Documentation

#### docs/agents/creation-guide.md
Complete guide for creating agents:
- Step-by-step process
- Agent structure
- System prompt writing
- Model selection
- Configuration
- Testing
- Examples

#### docs/skills/creation-guide.md
Complete guide for creating skills:
- Step-by-step process
- Skill structure
- Trigger keywords
- Instruction writing
- Error handling
- Testing
- Examples

#### docs/integration/agents-skills.md
How agents and skills work together:
- Relationship diagram
- Integration patterns
- Best practices
- Complete workflow examples
- Advanced patterns

### collection/ - Agent and Skill Packages

#### collection/agents/
Contains agent packages, each with:

**Required:**
- `AGENT.md` - Main agent definition

**Optional:**
- `examples/` - Usage examples
- `references/` - Reference documentation
- `assets/` - Images, diagrams

#### collection/skills/
Contains skill packages, each with:

**Required:**
- `SKILL.md` - Main skill definition

**Optional:**
- `examples/` - Usage examples
- `references/` - API docs, guides
- `scripts/` - Helper scripts
- `assets/` - Screenshots, diagrams

### templates/ - Templates

#### agent-template.md
Template for creating new agents with all required sections.

#### skill-template.md
Template for creating new skills with all required sections.

### resources/ - External Resources

#### external-links.md
Curated list of:
- OpenClaw documentation
- Related tools and libraries
- Community resources

#### tools-directory.md
Directory of:
- Useful CLI tools for agents
- APIs commonly used
- Libraries and frameworks

#### community.md
Community resources:
- Discord servers
- Forums
- Contributing organizations

## File Formats

### AGENT.md Format

```markdown
# Agent Name

## Purpose
[Description]

## Model
- Primary: [model]
- Alternative: [model]

## Tools
- [tool]: [usage]

## Skills
- [skill]: [description]

## System Prompt
```
[Prompt]
```

## Activation
[How activated]

## Usage Examples
[Examples]

## Configuration
[JSON config]

## Best Practices
[List]
```

### SKILL.md Format

```markdown
# Skill Name

## Description
[Brief description]

## Activation Keywords
- [keyword]
- [keyword]

## Tools Used
- [tool]: [usage]

## Installation
[Commands]

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

## Adding New Items

### Adding a New Agent

1. Create directory: `collection/agents/your-agent/`
2. Copy template: `templates/agent-template.md`
3. Edit as `AGENT.md`
4. Add examples in `examples/`
5. Update `AGENTS.md`

### Adding a New Skill

1. Create directory: `collection/skills/your-skill/`
2. Copy template: `templates/skill-template.md`
3. Edit as `SKILL.md`
4. Add examples in `examples/`
5. Update `SKILLS.md`

## Naming Conventions

### Directories
- **Agents:** Lowercase with hyphens: `research-agent`, `data-analyst`
- **Skills:** Lowercase with hyphens: `apple-notes`, `feishu-doc`

### Files
- **Agent ID:** Same as directory: `research-agent`
- **Skill name:** Same as directory: `apple-notes`

### Markdown
- **Headings:** Title Case
- **Code blocks:** Lowercase for code
- **Filenames:** Lowercase with hyphens

## Git Workflow

### Branch Naming
- New agent: `feat(agent): add research-agent`
- New skill: `feat(skill): add weather-skill`
- Bug fix: `fix(agent): resolve timeout issue`
- Documentation: `docs: update creation guide`

### Commit Messages
```
type(scope): subject

body

footer
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance

## Quick Reference

| Task | Command/Action |
|------|---------------|
| List available agents | See AGENTS.md |
| List available skills | See SKILLS.md |
| Create new agent | Use templates/agent-template.md |
| Create new skill | Use templates/skill-template.md |
| Learn about agents | Read docs/agents/creation-guide.md |
| Learn about skills | Read docs/skills/creation-guide.md |
| Understand integration | Read docs/integration/agents-skills.md |
| Contribute | Read CONTRIBUTING.md |

## Next Steps

1. **Learn the basics:** Read README.md, AGENTS.md, SKILLS.md
2. **Explore examples:** Check collection/agents/ and collection/skills/
3. **Create your first:** Use templates to create agent or skill
4. **Integrate them:** Read docs/integration/agents-skills.md
5. **Contribute:** Follow CONTRIBUTING.md guidelines

---

For more information, see the [README.md](./README.md).
