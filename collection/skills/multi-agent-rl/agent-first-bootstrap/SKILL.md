---
name: agent-first-bootstrap
description: Initialize projects with Agent-First methodology. Supports Codex, Claude Code, Qwen Code, GitHub Copilot, Gemini CLI. Generates AGENTS.md, tool-specific configs, and documentation structure.
---

# Agent-First Project Bootstrap

## Description

A comprehensive toolkit for initializing projects with Agent-First methodology. Enables seamless integration with multiple AI coding tools (Codex, Claude Code, Qwen Code, GitHub Copilot, Gemini CLI) by generating structured documentation, architecture guides, and tool-specific configuration files.

**Key Features:**
- Interactive project interview protocol
- Automatic generation of AGENTS.md and tool-specific configs
- Validation checklist for Agent-First readiness
- Support for 5 AI coding tools

## Overview

**Source:** OpenAI "Harness Engineering" + Best Practices
**Purpose:** Initialize projects with Agent-First methodology
**Supports:** Codex, Claude Code, Qwen Code, GitHub Copilot, Gemini CLI

## Activation Keywords

- agent-first bootstrap
- harness engineering init
- project bootstrap
- agent kickoff

---

## Core Principle

> **"Humans steer. Agents execute."**

Before any code is written, establish:
1. **Environment** - Repository structure, tools, constraints
2. **Intent** - Goals, requirements, success criteria
3. **Feedback Loops** - Tests, reviews, observability

---

## Quick Start

### Interactive Bootstrap

```bash
# Run the bootstrap interview
agent-bootstrap init

# Or with specific tool
agent-bootstrap init --tool codex
agent-bootstrap init --tool claude
agent-bootstrap init --tool qwen
agent-bootstrap init --tool copilot
agent-bootstrap init --tool gemini
```

---

## Project Interview Protocol

### Phase 1: Vision & Goals

```markdown
## Project Vision Interview

1. **What are we building?**
   - [ ] One-line description
   - [ ] Target users
   - [ ] Core value proposition

2. **What does success look like?**
   - [ ] Key metrics
   - [ ] User outcomes
   - [ ] Business goals

3. **What are the constraints?**
   - [ ] Time constraints
   - [ ] Resource constraints
   - [ ] Technical constraints
   - [ ] Must-have vs nice-to-have

4. **What is out of scope?**
   - [ ] Explicit non-goals
   - [ ] Future phases
```

### Phase 2: Architecture & Domain

```markdown
## Architecture Interview

1. **What are the core domains?**
   Example: User Management, Payments, Notifications

2. **What are the layers per domain?**
   Recommended: Types → Config → Repo → Service → Runtime → UI

3. **What are the cross-cutting concerns?**
   - Authentication
   - Logging/Observability
   - Feature Flags
   - Error Handling

4. **What external dependencies exist?**
   - Databases
   - APIs
   - Services
```

### Phase 3: Agent Configuration

```markdown
## Agent Configuration Interview

1. **What coding conventions?**
   - Naming patterns
   - File organization
   - Logging format

2. **What constraints to enforce?**
   - Layer boundaries
   - Dependency rules
   - Test requirements

3. **What agent capabilities needed?**
   - UI testing (Chrome DevTools)
   - API testing
   - Database migrations

4. **What feedback loops?**
   - Agent-to-agent review
   - Automated tests
   - Performance gates
```

### Phase 4: Documentation Structure

```markdown
## Documentation Interview

1. **Design docs location?**
   - docs/design/

2. **Architecture docs?**
   - docs/architecture/

3. **Quality tracking?**
   - docs/quality/

4. **Plans location?**
   - docs/plans/
```

---

## Generated Artifacts

### 1. AGENTS.md (~100 lines)

```markdown
# Agent Guide: [Project Name]

## Quick Start
- Run tests: `npm test` / `cargo test` / `pytest`
- Open PR: [instructions]
- Get help: [link to docs]

## Architecture
- See: docs/architecture/README.md
- Layers: Types → Config → Repo → Service → Runtime → UI
- Cross-cutting: Providers (auth, telemetry, flags)

## Key Domains
| Domain | Docs | Owner |
|--------|------|-------|
| [Domain1] | docs/design/domain1.md | @agent |
| [Domain2] | docs/design/domain2.md | @agent |

## Conventions
- Naming: [patterns]
- Logging: structured JSON via logger
- Tests: required for all new code

## Constraints (Enforced)
- Layer dependencies: forward only
- Max file size: 300 lines
- Test coverage: >80%

## Where to Learn More
- Design: docs/design/
- Quality: docs/quality/
- Plans: docs/plans/
- Debt: docs/debt.md

## Agent Workflow
1. Read this file first
2. Check docs/design/ for context
3. Write code following conventions
4. Run tests locally
5. Open PR for agent review
6. Iterate until all reviewers pass
```

### 2. Directory Structure

```
project/
├── AGENTS.md              # ~100 lines, table of contents
├── CLAUDE.md              # Claude Code specific (optional)
├── COPILOT.md             # GitHub Copilot specific (optional)
├── GEMINI.md              # Gemini CLI specific (optional)
├── docs/
│   ├── design/            # Design documents
│   │   ├── README.md      # Index of all designs
│   │   └── [domain].md    # Per-domain designs
│   ├── architecture/      # Architecture docs
│   │   ├── README.md      # Layer map
│   │   └── domains.md     # Domain breakdown
│   ├── quality/           # Quality tracking
│   │   └── domains.md     # Per-domain quality grades
│   ├── plans/             # Execution plans
│   │   ├── active/        # Current work
│   │   └── completed/     # Done work
│   └── debt.md            # Known technical debt
├── .github/
│   └── workflows/         # CI/CD (agent-generated)
├── src/
│   └── [domains]/         # Domain-organized code
└── tests/                 # Test suite
```

### 3. Tool-Specific Configs

#### Claude Code (CLAUDE.md)

```markdown
# Claude Code Instructions

## Project Context
This project follows Agent-First methodology.
Read AGENTS.md first, then docs/architecture/README.md.

## Workflow
1. Understand goal from user
2. Check docs/design/ for relevant context
3. Follow layer constraints strictly
4. Write tests before implementation
5. Self-review changes
6. Open PR for review

## Constraints
- Max file size: 300 lines
- Test coverage: >80%
- Use structured logging
- Follow naming conventions in AGENTS.md
```

#### GitHub Copilot (COPILOT.md)

```markdown
# GitHub Copilot Instructions

## Project Context
Agent-First project. See AGENTS.md for conventions.

## Coding Standards
- Follow layer architecture
- Use structured logging
- Write tests for new code
- Keep files under 300 lines

## Architecture
See docs/architecture/README.md
```

#### Gemini CLI (GEMINI.md)

```markdown
# Gemini CLI Instructions

## Project Context
This project follows Agent-First methodology.
Read AGENTS.md first, then docs/architecture/README.md.

## ReAct Workflow
Gemini CLI uses Reason-and-Act loop:
1. **Reason**: Understand the task and plan approach
2. **Act**: Execute file operations, shell commands, web fetch
3. **Iterate**: Refine based on results

## Available Tools
- `read_file` / `write_file` - File operations
- `run_shell_command` - Execute shell commands
- `web_fetch` - Fetch web content
- `google_web_search` - Search the web
- `save_memory` - Persist context across sessions

## MCP Server Integration
Gemini CLI supports MCP servers for extended capabilities.
Configure in `~/.gemini-cli/config.json`:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/project"]
    }
  }
}
```

## Workflow
1. Read AGENTS.md for project context
2. Check docs/design/ for domain details
3. Use `read_file` to understand existing code
4. Plan changes following layer architecture
5. Use `write_file` to implement
6. Run tests via `run_shell_command`
7. Iterate until tests pass

## Constraints
- Max file size: 300 lines
- Test coverage: >80%
- Use structured logging
- Follow naming conventions in AGENTS.md

## Extensions
Install useful extensions:
```bash
gemini-cli extension install @google/gemini-cli-extension-filesystem
gemini-cli extension install @google/gemini-cli-extension-web
```

## Architecture
See docs/architecture/README.md
```

---

## Bootstrap CLI Tool

### Installation

```bash
# Install globally
npm install -g agent-bootstrap

# Or use directly
npx agent-bootstrap init
```

### Commands

```bash
# Initialize new project
agent-bootstrap init

# Interactive interview
agent-bootstrap interview

# Generate AGENTS.md
agent-bootstrap generate agents

# Generate docs structure
agent-bootstrap generate docs

# Add domain
agent-bootstrap add-domain <name>

# Validate structure
agent-bootstrap validate

# Check agent readiness
agent-bootstrap readiness
```

### Interactive Mode

```bash
$ agent-bootstrap init

🚀 Agent-First Project Bootstrap

Phase 1: Vision & Goals
━━━━━━━━━━━━━━━━━━━━━━━

? What are we building? (one-line description)
> A task management API with real-time collaboration

? Who are the target users?
> Small teams, remote workers

? What does success look like?
> 1. < 200ms API response time
> 2. Real-time sync < 1s latency
> 3. 99.9% uptime

? Time constraints?
> MVP in 2 weeks

Phase 2: Architecture & Domains
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

? Core domains (comma-separated)
> Users, Tasks, Collaboration, Notifications

? Layers per domain
> Types, Config, Repo, Service, Runtime, UI

? Cross-cutting concerns
> Auth, Logging, Feature Flags

Phase 3: Agent Configuration
━━━━━━━━━━━━━━━━━━━━━━━━━━━

? Coding conventions file?
> Use defaults

? Enable agent-to-agent review?
> Yes

? Test coverage threshold?
> 80%

Phase 4: Documentation
━━━━━━━━━━━━━━━━━━━━━

? Docs location?
> docs/

? Generate all docs?
> Yes

✨ Generating project structure...

Created:
  ✓ AGENTS.md
  ✓ CLAUDE.md
  ✓ COPILOT.md
  ✓ GEMINI.md
  ✓ docs/design/README.md
  ✓ docs/architecture/README.md
  ✓ docs/quality/domains.md
  ✓ docs/plans/active/
  ✓ docs/debt.md
  ✓ .github/workflows/ci.yml
  ✓ tests/

🎯 Next steps:
  1. Review AGENTS.md
  2. Fill in docs/design/ for each domain
  3. Run: agent-bootstrap validate
  4. Start coding with your AI tool!
```

---

## Validation Checklist

```bash
$ agent-bootstrap validate

Checking Agent-First readiness...

✓ AGENTS.md exists (< 200 lines)
✓ AGENTS.md has architecture section
✓ AGENTS.md points to docs/
✓ docs/design/ exists
✓ docs/architecture/ exists
✓ docs/quality/ exists
✓ docs/plans/ exists
✓ CLAUDE.md, COPILOT.md, or GEMINI.md exists
✓ .github/workflows/ exists
✓ Test framework configured

Score: 10/10 - Ready for Agent-First development!
```

---

## Integration with AI Tools

### Codex CLI

```bash
# Initialize with Codex
codex --agents-md AGENTS.md "Build the Users domain"

# Codex will:
# 1. Read AGENTS.md
# 2. Check docs/design/users.md
# 3. Follow layer constraints
# 4. Generate tests
# 5. Open PR
```

### Claude Code

```bash
# Initialize with Claude
claude --model sonnet "Build the Users domain following AGENTS.md"

# Claude will:
# 1. Read AGENTS.md and CLAUDE.md
# 2. Check docs/design/
# 3. Follow conventions
# 4. Self-review
# 5. Open PR
```

### GitHub Copilot

```markdown
# In VS Code with Copilot Chat:

@workspace Build the Users domain following AGENTS.md architecture.
Ensure:
- Layer constraints (Types → Service → UI)
- Test coverage >80%
- Structured logging
```

### Qwen Code

```bash
# Initialize with Qwen
qwen-code "Build Users domain" --agents-md AGENTS.md
```

### Gemini CLI

```bash
# Initialize with Gemini CLI
gemini-cli "Build the Users domain based on docs/design/users.md"

# Gemini CLI ReAct workflow:
# 1. Read AGENTS.md and GEMINI.md for context
# 2. Use read_file to check docs/design/users.md
# 3. Use read_file to understand existing code
# 4. Plan approach following layer architecture
# 5. Use write_file to implement changes
# 6. Use run_shell_command to run tests
# 7. Iterate until all tests pass

# MCP server integration
gemini-cli --mcp-config ~/.gemini-cli/mcp-config.json "Build Users domain"

# Example ReAct session
$ gemini-cli

> Build the Users domain following AGENTS.md

[Reason]: I need to read AGENTS.md first, then docs/design/users.md,
          understand the layer architecture, and plan implementation.

[Act]: read_file AGENTS.md
       read_file docs/design/users.md
       read_file src/users/types.ts

[Reason]: I see the Users domain needs Types, Repo, and Service layers.
          Let me start with Types layer following existing patterns.

[Act]: write_file src/users/types/User.ts
       write_file src/users/types/UserRepository.ts

[Reason]: Now I need to implement the Repo layer with database operations.

[Act]: write_file src/users/repo/UserRepo.ts

[Reason]: Let me run tests to verify my implementation.

[Act]: run_shell_command npm test -- --grep "Users"

[Result]: Tests passed! Coverage: 85%

[Reason]: All tests pass with >80% coverage. Let me add more tests
          for edge cases.

[Act]: write_file tests/users/UserRepo.test.ts

[Reason]: Final verification.

[Act]: run_shell_command npm test

[Result]: All tests pass! Users domain complete.

> Done! Users domain implemented following AGENTS.md architecture.
```

---

## Best Practices

### 1. Keep AGENTS.md Short

| ✅ Good | ❌ Bad |
|---------|--------|
| ~100 lines | 500+ lines |
| Links to docs | All rules inline |
| Table of contents | Encyclopedia |

### 2. Progressive Disclosure

```
AGENTS.md (entry point)
    ↓
docs/architecture/ (layer map)
    ↓
docs/design/[domain].md (detailed design)
```

### 3. Enforce Mechanically

```yaml
# .github/workflows/agent-check.yml
name: Agent Constraints
on: [pull_request]

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Check file sizes
        run: find src -name "*.ts" -exec wc -l {} \; | awk '$1 > 300 {exit 1}'
      - name: Check layer boundaries
        run: node scripts/check-layers.js
      - name: Check test coverage
        run: npm run coverage -- --min=80
```

### 4. Doc-Gardening Agent

```bash
# Run periodically
agent-bootstrap garden

# Checks:
# - Stale documentation
# - Missing cross-links
# - Outdated examples
# - Opens fix-up PRs
```

---

## Example: Full Bootstrap

```bash
# 1. Create project
mkdir my-project && cd my-project
git init

# 2. Run bootstrap
npx agent-bootstrap init

# 3. Fill interview
# [Answer questions about vision, architecture, etc.]

# 4. Validate
agent-bootstrap validate

# 5. Start with AI tool
codex "Implement the Users domain based on docs/design/users.md"
```

---

## Templates

### docs/design/[domain].md

```markdown
# [Domain] Design

## Overview
[What this domain does]

## User Stories
1. As a [user], I want to [action]
2. ...

## API Contracts
[Endpoints/Interfaces]

## Data Models
[Schemas/Types]

## Implementation Notes
[Agent-relevant context]

## Quality Gates
- [ ] Unit tests >80%
- [ ] Integration tests pass
- [ ] Performance <200ms
```

### docs/architecture/README.md

```markdown
# Architecture Overview

## Domains
| Domain | Description | Layers |
|--------|-------------|--------|
| Users | User management | All 6 |
| Tasks | Task CRUD | All 6 |
| ... | ... | ... |

## Layer Rules
```
Types → Config → Repo → Service → Runtime → UI
         ↑
    Providers (auth, telemetry)
```

## Dependency Rules
- Forward only within domain
- Cross-domain via Service layer only
- Providers inject at Config layer
```

---

## References

- OpenAI Blog: https://openai.com/index/harness-engineering/
- AGENTS.md Spec: https://agents.md/
- Architecture Docs: https://matklad.github.io/2021/02/06/ARCHITECTURE.md.html

---

## Tools Used

- `exec` - Run agent-bootstrap CLI commands
- `write` - Create AGENTS.md, GEMINI.md, docs structure
- `read` - Read existing project files for context
- `edit` - Modify generated configs
- `web_fetch` - Fetch Gemini CLI documentation
- `web_search` - Search for AI tool best practices

---

## Instructions for Agents

### When User Requests Bootstrap

1. **Ask clarifying questions** (if not provided):
   - What AI tool will be used? (codex, claude, copilot, gemini, qwen)
   - What is the project domain?
   - What are the core features?

2. **Generate project structure:**
   - Create AGENTS.md with architecture overview
   - Create tool-specific config (CLAUDE.md, GEMINI.md, etc.)
   - Create docs/design/, docs/architecture/, docs/quality/
   - Create .github/workflows/ci.yml

3. **Validate structure:**
   - Run agent-bootstrap validate (if available)
   - Check all required files exist

4. **Report to user:**
   - List created files
   - Provide next steps

### For Gemini CLI Specific

1. Include GEMINI.md with ReAct workflow instructions
2. Document MCP server integration options
3. List available tools (read_file, write_file, run_shell_command)
4. Provide extension installation examples

### For Other Tools

- Claude Code: CLAUDE.md with self-review workflow
- GitHub Copilot: COPILOT.md with @workspace instructions
- Codex: Direct AGENTS.md integration
- Qwen Code: Similar to Codex approach

---

**Created:** 2026-03-28
**Updated:** 2026-03-29 (Added Gemini CLI support)
**Purpose:** Universal Agent-First project bootstrap tool

## Examples

### Basic Agent First Bootstrap usage
```
User: "Help me with agent first bootstrap"
→ Understand requirements → Execute actions → Provide results
```

### Advanced usage
```
User: "I need detailed agent first bootstrap assistance"
→ Clarify scope → Provide comprehensive solution → Follow up
```
