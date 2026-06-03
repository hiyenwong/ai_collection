# agent-bootstrap

Agent-First Project Bootstrap CLI - Initialize projects with Harness Engineering methodology.

## Installation

```bash
# Clone or copy
git clone https://github.com/your-repo/agent-bootstrap.git
cd agent-bootstrap

# Install dependencies
pip install -e .

# Or use directly
python agent_bootstrap.py --help
```

## Quick Start

```bash
# Initialize new project
agent-bootstrap init

# Validate existing project
agent-bootstrap validate

# Run doc-gardening
agent-bootstrap garden
```

## Commands

| Command | Description |
|---------|-------------|
| `init` | Interactive project initialization with interview |
| `interview` | Run interview phases only |
| `validate` | Validate project structure for agent-readiness |
| `garden` | Run doc-gardening check |

## Interview Phases

### Phase 1: Vision & Goals
- Project description
- Target users
- Success metrics
- Constraints

### Phase 2: Architecture & Domain
- Core domains
- Layer structure
- Cross-cutting concerns
- External dependencies

### Phase 3: Agent Configuration
- Coding conventions
- Constraints to enforce
- Agent capabilities
- Feedback loops

### Phase 4: Documentation Structure
- Docs location
- Tool-specific configs

## Generated Artifacts

```
project/
├── AGENTS.md              # ~100 lines, table of contents
├── CLAUDE.md              # Claude Code instructions
├── COPILOT.md             # GitHub Copilot instructions
├── .agent-bootstrap.json  # Saved config
├── docs/
│   ├── design/            # Design documents
│   ├── architecture/      # Architecture overview
│   ├── quality/           # Quality tracking
│   ├── plans/             # Execution plans
│   └── debt.md            # Technical debt
└── .github/
    └── workflows/
        └── ci.yml         # CI workflow
```

## Usage with AI Tools

### Claude Code
```bash
claude --model sonnet "Build the Users domain following AGENTS.md"
```

### Codex CLI
```bash
codex "Implement the Users domain based on docs/design/users.md"
```

### GitHub Copilot
```
@workspace Build the Users domain following AGENTS.md architecture.
```

## Configuration

Saved in `.agent-bootstrap.json`:

```json
{
  "vision": {
    "description": "...",
    "target_users": "...",
    "success_metrics": [...]
  },
  "architecture": {
    "domains": [...],
    "layers": [...],
    "cross_cutting": [...]
  },
  "agent_config": {
    "conventions": {...},
    "constraints": [...]
  },
  "tools": ["codex", "claude", "copilot", "qwen"]
}
```

## Philosophy

Based on OpenAI's "Harness Engineering":

> "Humans steer. Agents execute."

Key principles:
1. AGENTS.md is a **map**, not encyclopedia
2. **Enforce constraints**, not implementations
3. **Repository** is single source of truth
4. **Agent-to-agent** review over human review
5. **Fast merges** > perfect code

## References

- [OpenAI: Harness Engineering](https://openai.com/index/harness-engineering/)
- [AGENTS.md Spec](https://agents.md/)
- [Architecture Docs](https://matklad.github.io/2021/02/06/ARCHITECTURE.md.html)

## License

MIT