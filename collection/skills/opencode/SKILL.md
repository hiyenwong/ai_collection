# OpenCode + Oh My OpenCode

## Description
Open source AI coding agent with a powerful plugin system. Oh My OpenCode transforms OpenCode into a full-fledged agent harness with multi-agent orchestration, background tasks, LSP integration, and "ultrawork" mode for relentless task completion.

## Activation Keywords
- opencode
- open code
- oh-my-opencode
- ultrawork
- ultrawork mode
- ulw
- opencode agent
- coding agent

## Tools Used
- exec: Run opencode CLI
- read: Read code files
- write: Write code files
- edit: Edit code files
- process: Manage background opencode sessions

## Installation

### Install OpenCode

**Easy install:**
```bash
curl -fsSL https://opencode.ai/install | bash
```

**Via npm:**
```bash
npm install -g opencode-ai
```

**Via Homebrew (macOS/Linux):**
```bash
brew install anomalyco/tap/opencode
```

### Verify Installation
```bash
opencode --version
```

### Configure OpenCode
```bash
# Start OpenCode
opencode

# Connect to provider
/connect
# Select opencode, then go to opencode.ai/auth to get API key
```

### Initialize Project
```bash
# Navigate to your project
cd /path/to/project

# Start OpenCode
opencode

# Initialize project (creates AGENTS.md)
/init
```

### Install Oh My OpenCode

**For Humans (Recommended):**
Let an LLM agent handle this. Paste this prompt to Claude Code / AmpCode / Cursor:
```
Install and configure oh-my-opencode by following the instructions here: https://raw.githubusercontent.com/code-yeongyu/oh-my-opencode/refs/heads/master/docs/guide/installation.md
```

**Manual Install:**
See full installation guide: https://github.com/code-yeongyu/oh-my-opencode/blob/dev/docs/guide/installation.md

## Usage Patterns

### Basic OpenCode Usage

**Start a session:**
```bash
cd /path/to/project
opencode
```

**Common commands:**
- `/init` - Initialize project
- `/undo` - Revert changes
- `/redo` - Re-apply changes
- `/plan` - Switch to planning mode
- `/build` - Switch to build mode
- `/share` - Share conversation link

### Using Oh My OpenCode - Ultrawork Mode

The magic word: **ultrawork** (or **ulw**)

**Enable for any task:**
```
Add this feature with ultrawork enabled
```

**Short version:**
```
Implement this feature ulw
```

**With specific model:**
```
Debug the authentication issue ultrawork with model sonnet
```

### Multi-Agent Orchestration

Oh My OpenCode automatically coordinates multiple agents:

**Sisyphus (Main Agent):** Orchestrator, uses Opus 4.5 High
**Prometheus:** Planner, breaks down complex tasks
**Oracle:** Design, debugging, high-IQ strategy (GPT 5.2 Medium)
**Frontend Engineer:** UI/UX development (Gemini 3 Pro)
**Librarian:** Official docs, codebase exploration (Claude Sonnet 4.5)
**Explore:** Fast codebase search (Claude Haiku 4.5)

## Instructions for Agents

When user mentions OpenCode or Oh My OpenCode:

### 1. Verify Installation
Check if opencode is installed:
```bash
opencode --version
```

If not installed, guide user:
```bash
curl -fsSL https://opencode.ai/install | bash
opencode
/connect
```

### 2. Navigate to Project
Always work in the project directory:
```bash
cd /path/to/project
opencode
```

### 3. Initialize Project (if needed)
```bash
/init
```

This creates AGENTS.md with project context.

### 4. Use Ultrawork for Complex Tasks
When user requests complex work, enable ultrawork:
```
Task description here ultrawork
```

Ultrawork automatically:
- Spawns background agents for parallel exploration
- Uses LSP for surgical refactoring
- Delegates to specialized agents (UI, debugging, etc.)
- Continues until 100% complete

### 5. Use LSP for Safe Refactoring
When refactoring, leverage LSP:
```
Refactor the auth module using LSP. Follow the pattern in user.service.ts
```

LSP provides:
- Symbol-aware renaming
- Safe extraction
- Inline functions
- Go-to-definition
- Find references

### 6. Leverage Specialized Agents
Different agents for different tasks:

**For documentation:**
```
Generate API documentation for the user module
```
→ Librarian agent handles this

**For debugging:**
```
Find and fix the authentication bug in auth.ts
```
→ Oracle agent handles this

**For UI work:**
```
Create a responsive dashboard component
```
→ Frontend Engineer agent handles this

### 7. Use MCP Integrations
Oh My OpenCode includes curated MCPs:

**Exa (Web search):**
```
Search for examples of JWT authentication best practices
```

**Context7 (Official docs):**
```
Look up the official React documentation for useEffect
```

**Grep.app (GitHub code search):**
```
Find examples of similar patterns in open source projects
```

## Context Files

OpenCode and Oh My OpenCode use these context files:

### AGENTS.md
Project-specific instructions for agents

### .opencode/oh-my-opencode.json
Oh My OpenCode configuration

### package.json
Dependencies and scripts

### tsconfig.json / jsconfig.json
Language configuration

## Configuration

### OpenCode Config (~/.config/opencode/opencode.json)
```json
{
  "defaultModel": "anthropic/claude-sonnet-4.5",
  "maxTokens": 200000,
  "temperature": 0.3,
  "plugins": ["oh-my-opencode"]
}
```

### Oh My OpenCode Config (~/.config/opencode/oh-my-opencode.json)
```json
{
  "agents": {
    "sisyphus": {
      "model": "anthropic/claude-opus-4.5",
      "temperature": 0.1
    },
    "oracle": {
      "model": "openai/gpt-5.2-medium",
      "temperature": 0.2
    }
  },
  "ultrawork": {
    "enabled": true,
    "parallelAgents": 3
  },
  "lsp": {
    "enabled": true,
    "timeout": 30000
  },
  "disabled_hooks": [
    "comment_checker"
  ]
}
```

### Project Config (.opencode/oh-my-opencode.json)
```json
{
  "agents": {
    "sisyphus": {
      "model": "anthropic/claude-sonnet-4.5"
    }
  },
  "skills": [
    "typescript",
    "react",
    "testing"
  ]
}
```

## Advanced Features

### LSP & AST Tools

**Surgical refactoring:**
```
Rename the User interface to UserProfile using LSP
```

**Safe code changes:**
```
Extract the validation logic into a separate function using LSP
```

**Code analysis:**
```
Find all references to the authenticate function using LSP
```

### Background Tasks
Run multiple agents in parallel:

```
Implement the feature ultrawork

This spawns:
- Agent 1: Explores codebase
- Agent 2: Reviews documentation
- Agent 3: Analyzes similar implementations
```

### Hooks System
Oh My OpenCode includes 25+ hooks:

**Productivity hooks:**
- `todo_continuation_enforcer`: Forces agents to finish tasks
- `comment_checker`: Prevents excessive AI comments
- `think_mode`: Deep analysis mode
- `ralph_loop`: Code iteration loop

**Git hooks:**
- `git_master`: Atomic commits
- `commit_message_generator`: Auto-generates commit messages

### MCP Integration

**Using Exa (Web search):**
```
Search for "best practices for API error handling"
```

**Using Context7 (Official docs):**
```
Look up the official documentation for React hooks
```

**Using Grep.app (GitHub search):**
```
Search GitHub for examples of similar authentication patterns
```

## Common Patterns

### Adding a Feature
```
When a user deletes a note, flag it as deleted in the database. Then create a screen showing recently deleted notes where users can undelete or permanently delete them. ultrawork
```

### Debugging Code
```
Find and fix the authentication bug in @packages/functions/src/api/index.ts ultrawork
```

### Refactoring
```
Refactor the authentication logic to follow the pattern used in @packages/functions/src/notes.ts. Use LSP for safe refactoring.
```

### Code Review
```
Review the changes in src/api/ and provide improvement suggestions
```

### Documentation
```
Generate API documentation for the user module with examples
```

## Error Handling

### Agent Not Starting
```
If opencode won't start:
  1. Check installation: opencode --version
  2. Verify config: ~/.config/opencode/opencode.json
  3. Check API key is valid
  4. Try restarting: opencode --restart
```

### Ultrawork Not Working
```
If ultrawork doesn't activate:
  1. Verify oh-my-opencode is installed
  2. Check config has ultrawork.enabled = true
  3. Ensure plugin is loaded: /plugins list
  4. Try explicit mode: /ultrawork enable
```

### LSP Issues
```
If LSP tools fail:
  1. Check language server is installed
  2. Verify project has tsconfig.json/jsconfig.json
  3. Restart LSP: /lsp restart
  4. Check language server logs
```

### Agent Timeouts
```
If agents timeout:
  1. Increase timeout in config
  2. Break task into smaller chunks
  3. Use more efficient model (Sonnet vs Opus)
  4. Check for infinite loops in agent logic
```

## Best Practices

### 1. Use Ultrawork for Complex Tasks
Ultrawork is designed for complex work:
- ✅ Multi-file changes
- ✅ Codebase exploration
- ✅ Parallel execution
- ✅ Deep analysis
- ❌ Simple one-liners

### 2. Leverage Specialized Agents
Each agent has a specialty:
- **Sisyphus:** General orchestration
- **Prometheus:** Task planning
- **Oracle:** Debugging and design
- **Frontend Engineer:** UI/UX
- **Librarian:** Documentation
- **Explore:** Fast search

### 3. Use LSP for Refactoring
LSP ensures safe changes:
- ✅ Symbol-aware renaming
- ✅ Safe extraction/inline
- ✅ Find references
- ❌ Manual string replacement

### 4. Initialize Projects
Always run `/init` in new projects:
- Creates AGENTS.md
- Sets up context
- Configures agents

### 5. Share Conversation Links
Use `/share` to:
- Get help from others
- Document decisions
- Reference past work

## Examples

### Example 1: Feature with Ultrawork
```
User: "Add user authentication with JWT tokens ultrawork"

Oh My OpenCode:
1. Sisyphus (orchestrator) breaks down task:
   - Create user model
   - Implement JWT generation
   - Add authentication middleware
   - Create login endpoint
   - Add tests

2. Spawns parallel background agents:
   - Explore agent: Finds existing patterns
   - Librarian: Looks up JWT best practices
   - Prometheus: Plans implementation

3. Oracle designs authentication flow

4. Agents implement in parallel

5. Sisyphus coordinates and integrates

Result: Complete authentication system with tests
```

### Example 2: Debugging with Specialized Agent
```
User: "The login form shows 'invalid credentials' even with correct password"

Oh My OpenCode:
1. Sisyphus assigns to Oracle (debugging specialist)

2. Oracle investigates:
   - Reads login form code
   - Traces authentication flow
   - Identifies bug: Password comparison case-sensitive
   - Fixes by normalizing input

Result: Bug fixed with minimal changes
```

### Example 3: LSP Refactoring
```
User: "Refactor to rename User class to Customer using LSP"

Oh My OpenCode:
1. Uses LSP to find all references
2. Safely renames symbol
3. Updates all usages
4. Verifies no broken references

Result: Clean refactoring without manual search/replace
```

## Limitations

- Requires opencode.ai account or API keys
- Some features depend on LSP servers
- Ultrawork can be expensive (multiple model calls)
- Learning curve for configuration

## Resources

- **OpenCode Docs:** https://opencode.ai/docs
- **Oh My OpenCode Repo:** https://github.com/code-yeongyu/oh-my-opencode
- **Oh My OpenCode Guide:** https://github.com/code-yeongyu/oh-my-opencode/blob/dev/docs/guide/installation.md
- **Discord Community:** https://discord.gg/PUwSMR9XNk
- **Releases:** https://github.com/code-yeongyu/oh-my-opencode/releases

## Related Skills
- **claude-code:** Anthropic's official coding tool
- **coding-agent:** Generic coding agent
- **obsidian:** For documentation

## OpenClaw AI Collection Integration

OpenCode can work seamlessly with the **OpenClaw AI Collection** - a curated set of specialized agents and skills that extend your coding capabilities.

### Available Agents in the Collection

| Agent | Purpose | When to Use |
|-------|---------|-------------|
| **fullstack-engineer** | Senior full-stack development | Complete web applications, architecture |
| **algorithm-engineer** | Algorithm design & ML | Complex algorithms, data structures, ML models |
| **stock-analyst** | Financial data analysis | Stock analysis, trading strategies |
| **research-agent** | Deep research | Market research, technical investigations |
| **tech-cofounder** | Product building | MVP development, rapid prototyping |

### Available Skills in the Collection

| Skill | Purpose | Activation |
|-------|---------|-----------|
| **openspec** | Spec-driven development | Gherkin syntax, BDD requirements |
| **skill-extractor** | Extract skills from conversation | "提炼技能", "extract skill" |
| **skill-rag-indexer** | Semantic skill search | "搜索技能", "skill search" |
| **stock-analysis** | Technical stock analysis | "股票分析", MACD, KDJ |
| **akshare** | Chinese financial data | Stock market, futures data |

### Integrating with OpenCode

Add these agents to your `.opencode/oh-my-opencode.json` configuration:

```json
{
  "agents": {
    "sisyphus": {
      "model": "anthropic/claude-opus-4.5",
      "systemPrompt": "Read /path/to/collection/agents/fullstack-engineer/AGENT.md"
    },
    "algorithm_engineer": {
      "model": "anthropic/claude-opus-4.5",
      "systemPrompt": "Read /path/to/collection/agents/algorithm-engineer/AGENT.md"
    },
    "research_agent": {
      "model": "anthropic/claude-opus-4.5",
      "systemPrompt": "Read /path/to/collection/agents/research-agent/AGENT.md"
    },
    "stock_analyst": {
      "model": "anthropic/claude-sonnet-4.5",
      "systemPrompt": "Read /path/to/collection/agents/stock-analyst/AGENT.md"
    },
    "tech_cofounder": {
      "model": "anthropic/claude-sonnet-4.5",
      "systemPrompt": "Read /path/to/collection/agents/tech-cofounder/AGENT.md"
    }
  },
  "skills": [
    "openspec",
    "skill-extractor",
    "skill-rag-indexer"
  ]
}
```

### Example: Using Specialized Agent with OpenCode

```
Use the algorithm-engineer agent to optimize the sorting algorithm in this file ultrawork
```

This loads the algorithm-engineer's expertise while leveraging OpenCode's orchestration.

### Example: Combining Skills

```
Use openspec to define the requirements, then implement with ultrawork
```

First defines behavior with Gherkin syntax, then implements with full validation.

### Installation Path

The OpenClaw AI Collection is available at:
- **GitHub:** https://github.com/hiyenwong/ai_collection
- **Local:** `/path/to/ai_collection`

To integrate:
1. Clone or download the collection
2. Reference agent/skill paths in your OpenCode config
3. Use activation keywords to trigger specialized behavior

### Quick Reference

**Algorithm task:** "Use algorithm-engineer for this"
**Full-stack app:** "Use fullstack-engineer with ultrawork"
**Stock analysis:** "Use stock-analyst for financial data"
**Research task:** "Use research-agent for market analysis"
**Product build:** "Use tech-cofounder for MVP"

---

*For more information, see the [AI Collection README](https://github.com/hiyenwong/ai_collection)*

## Notes

- Ultrawork is the magic word - just add "ultrawork" or "ulw" to enable
- The author spent $24,000 worth of LLM tokens testing this setup
- Works with ChatGPT, Claude, Gemini, and more through OpenCode
- Oh My OpenCode provides Claude Code compatibility layer
