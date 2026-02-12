# AI Collection

A curated collection of OpenClaw agents and skills for AI assistants.

## Overview

This repository serves as a knowledge base and showcase for OpenClaw's agent and skill ecosystem. It documents agents and skills that extend OpenClaw's capabilities, making them easy to discover, understand, and use.

## What's Inside

- **Agents**: Autonomous AI agents that can perform complex tasks using OpenClaw's `sessions_spawn` system
- **Skills**: Reusable capability packages that define specialized behaviors and tools

## Structure

```
ai_collection/
├── README.md              # This file
├── AGENTS.md              # Agent documentation overview
├── SKILLS.md              # Skill documentation overview
├── docs/                  # General documentation
│   ├── agents/            # Agent guides and best practices
│   ├── skills/            # Skill guides and best practices
│   └── integration/       # Integration docs
├── collection/            # Collected agents and skills
│   ├── agents/            # Agent packages
│   └── skills/            # Skill packages
├── templates/             # Templates for creating new items
├── resources/             # External resources and links
└── .gitignore            # Git ignore rules
```

## Documentation

- [Agent Overview](./AGENTS.md) - Learn about OpenClaw agents
- [Skill Overview](./SKILLS.md) - Learn about OpenClaw skills
- [Agent Creation Guide](./docs/agents/creation-guide.md) - How to create agents
- [Skill Creation Guide](./docs/skills/creation-guide.md) - How to create skills

## Quick Start

### Adding a New Agent

1. Create a new directory in `collection/agents/your-agent-name/`
2. Copy the agent template from `templates/agent-template.md`
3. Fill in the agent details and capabilities
4. Add examples and usage instructions
5. Update the main [AGENTS.md](./AGENTS.md) file

### Adding a New Skill

1. Create a new directory in `collection/skills/your-skill-name/`
2. Copy the skill template from `templates/skill-template.md`
3. Define the skill's description, triggers, and behavior
4. Add references, examples, and scripts
5. Update the main [SKILLS.md](./SKILLS.md) file

## Contributing

Contributions are welcome! Please see the [Contributing Guidelines](./CONTRIBUTING.md) for details.

## About OpenClaw

OpenClaw is a flexible AI agent framework that supports multiple channels (Feishu, Telegram, WhatsApp, etc.), extensible skills, and autonomous sub-agents through its `sessions_spawn` system.

- **OpenClaw Docs**: https://docs.openclaw.ai
- **GitHub**: https://github.com/openclaw/openclaw
- **Community**: https://discord.com/invite/clawd

## License

This repository is MIT licensed. Individual agents and skills may have their own licenses.

---

Maintained by the OpenClaw community 🤖
