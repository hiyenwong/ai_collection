# OpenClaw Skills

## What is a Skill?

An OpenClaw **skill** is a reusable capability package that defines specialized behavior, tools, and instructions for handling specific types of tasks. Skills act as "plugins" that extend an agent's capabilities.

## How Skills Work

Skills are automatically activated when:
1. **Trigger keywords** match in the user's message
2. The agent reads the skill's `SKILL.md` file
3. The agent follows the skill's instructions for the task
4. The agent uses skill-defined tools and workflows

### Skill Activation

When a user message contains trigger keywords:
```
User: "Create a note about my meeting"
```

The system:
1. Detects "note" as a trigger keyword
2. Activates the `apple-notes` skill
3. Loads `/path/to/skill/apple-notes/SKILL.md`
4. Agent follows skill instructions to create the note

## Skill Structure

```
skill-name/
├── SKILL.md              # Main skill documentation and instructions
├── references/           # Reference documentation (optional)
│   ├── api-docs.md
│   └── examples.md
├── examples/            # Usage examples (optional)
│   └── example-1.md
├── scripts/             # Helper scripts (optional)
│   └── setup.sh
└── assets/              # Images, diagrams, etc. (optional)
    └── screenshot.png
```

### SKILL.md Format

The `SKILL.md` file must contain:

```markdown
# Skill Name

## Description
Brief description of what this skill does.

## Activation Keywords
- keyword1
- keyword2
- keyword3

## Instructions
How the agent should use this skill.
```

### Example SKILL.md

```markdown
# Apple Notes

## Description
Manage Apple Notes via the `memo` CLI on macOS (create, view, edit, delete, search, move, and export notes).

## Activation Keywords
- create a note
- list notes
- add note
- search notes
- apple notes
- memo

## Instructions
When a user asks to work with notes, use the `memo` CLI:

### Creating Notes
```bash
memo create "Note title" "Note content"
```

### Listing Notes
```bash
memo list
memo list --folder "Work"
```

### Searching Notes
```bash
memo search "keyword"
```

### Editing Notes
```bash
memo edit <note-id> "New content"
```

## Tools Used
- exec: Run memo CLI commands

## Notes
- Ensure `memo` is installed and configured
- Notes are stored in user's Apple Notes app
```

## Skill Capabilities

### 1. Specialized Instructions
Skills provide detailed, domain-specific instructions that override general behavior.

### 2. Tool Preferences
Skills define which tools to use and how:
```markdown
## Tools Used
- exec: Run commands
- web_fetch: Get data
- read: Read files
```

### 3. Workflow Automation
Skills can define multi-step workflows:
```markdown
## Workflow
1. Search for existing notes
2. If found, offer to edit
3. If not found, create new note
4. Verify note was created successfully
```

### 4. Context Management
Skills can specify what context to load:
```markdown
## Context Files
- Read NOTES_SETTINGS.md for user preferences
- Check notes-template.md for formatting
```

### 5. Error Handling
Skills define how to handle errors:
```markdown
## Error Handling
If memo command fails:
1. Check if memo is installed
2. Verify macOS accessibility permissions
3. Try alternative method or report error
```

## Skill Types

### 1. Tool Wrappers
Wrappers around external tools/CLIs:
- `apple-notes`: Memo CLI for notes
- `apple-reminders`: remindctl CLI for reminders
- `sonoscli`: Sonos speaker control

### 2. Service Integrations
Integrations with external services:
- `feishu-doc`: Feishu document operations
- `feishu-drive`: Feishu cloud storage
- `feishu-wiki`: Feishu knowledge base

### 3. Task-Specific
Specialized task capabilities:
- `coding-agent`: Run Codex CLI, Claude Code
- `video-frames`: Extract frames from videos
- `gifgrep`: Search and download GIFs

### 4. Information Retrieval
Get specific types of information:
- `weather`: Weather and forecasts
- `summarize`: Summarize content
- `model-usage`: Model usage statistics

## When to Create a Skill

Create a skill when:
- ✅ Task type is repeated frequently
- ✅ Task requires specialized knowledge or workflow
- ✅ Task uses specific tools or APIs consistently
- ✅ You want to document best practices
- ✅ Task requires multiple steps that should be standardized

Don't create a skill when:
- ❌ Task is one-time or very rare
- ❌ Instructions are simple enough to be general knowledge
- ❌ Task varies significantly each time
- ❌ Existing tools handle it well without guidance

## Creating a Skill

### Step 1: Define Purpose
What does this skill do? What problems does it solve?

### Step 2: Identify Triggers
What keywords or phrases should activate this skill?

### Step 3: Document Instructions
Write clear, step-by-step instructions for the agent.

### Step 4: Add References
Include API docs, guides, and examples.

### Step 5: Test Thoroughly
Test with various prompts and edge cases.

### Step 6: Iterate
Refine based on usage and feedback.

## Skill Best Practices

### 1. Clear Activation Keywords
- Use specific, uncommon phrases
- Avoid words used in general conversation
- Include variations (synonyms, abbreviations)

**Good:** `"create a note"`, `"list my reminders"`
**Bad:** `"create"`, `"list"`

### 2. Comprehensive Instructions
- Cover common use cases
- Address edge cases
- Provide examples
- Include error handling

### 3. Tool Specifications
List tools explicitly:
```markdown
## Tools Used
- exec: Run commands with pty for CLIs
- read: Read skill-specific config files
```

### 4. Context Awareness
Specify what context to load:
```markdown
## Context
- Read TOOLS.md for device settings
- Check USER.md for user preferences
```

### 5. Maintainability
- Keep SKILL.md focused
- Put detailed docs in references/
- Use examples/ for illustration

## Skill Discovery

### Finding Available Skills
```python
agents_list()  # List available agents (also checks skills)
```

### Checking Active Skill
```
User: What skill are you using?
Agent: I'm using the apple-notes skill to manage your notes.
```

## Advanced Skills

### Multi-Tool Skills
Skills can combine multiple tools:
```markdown
## Tools Used
- exec: Run CLIs
- web_search: Find information
- write: Save results
```

### Chained Skills
Skills can reference other skills:
```markdown
## Related Skills
- feishu-doc: For document operations
- obsidian: For vault management
```

### Conditional Behavior
Skills can have conditional logic:
```markdown
## Conditional Behavior
IF user has multiple folders:
  - Ask which folder to use
ELSE:
  - Use default folder
```

## Skill Examples

### Weather Skill
```markdown
# Weather

## Description
Get current weather and forecasts (no API key required).

## Activation Keywords
- weather
- forecast
- temperature
- raining
- sunny

## Instructions
Use the weather CLI:
```bash
weather
weather forecast
weather --location "Beijing"
```

## Tools Used
- exec: Run weather CLI
```

### Feishu Doc Skill
```markdown
# Feishu Document

## Description
Feishu document read/write operations.

## Activation Keywords
- feishu doc
- feishu document
- cloud doc
- docx link

## Instructions
Use the feishu_doc tool:

### Reading Documents
```python
feishu_doc(
    action="read",
    doc_token="..."
)
```

### Writing Documents
```python
feishu_doc(
    action="write",
    doc_token="...",
    content="..."
)
```

## Tools Used
- feishu_doc: Document operations
- read: Read local templates
```

## Troubleshooting

### Skill Not Activating
- Check activation keywords in user message
- Verify SKILL.md path is correct
- Check skill is in skill directories

### Agent Not Following Instructions
- Ensure instructions are clear and explicit
- Check for conflicting skills
- Verify tool permissions

### Skill Tools Failing
- Check if external tools are installed
- Verify API keys or credentials
- Test tool usage manually

## Resources

- [OpenClaw Docs - Skills](https://docs.openclaw.ai/skills)
- [OpenClaw Skill Hub](https://clawhub.com)
- [Skill Creator Guide](./docs/skills/creation-guide.md)

---

See the [skills-collection](https://github.com/your-org/skills-collection) repository for example skills.

## Available Skills

### OpenCode + Oh My OpenCode
- **Location:** `collection/skills/opencode/`
- **Purpose:** Open source AI coding agent with multi-agent orchestration and ultrawork mode
- **Triggers:** opencode, ultrawork, ulw, oh-my-opencode, coding agent
- **Tools:** exec, read, write, edit, process
- **Key Features:**
  - Multi-agent orchestration (Sisyphus, Oracle, Librarian, etc.)
  - Ultrawork mode for parallel execution
  - LSP/AST tools for surgical refactoring
  - MCP integration (Exa, Context7, Grep.app)

### Claude Code
- **Location:** `collection/skills/claude-code/`
- **Purpose:** Anthropic's official AI-powered coding companion
- **Triggers:** claude-code, claude code, @anthropic, anthropic coding
- **Tools:** exec, read, write, edit, process
- **Key Features:**
  - Native Claude integration
  - Privacy-first design
  - Context-aware project understanding
  - MCP, Hooks, Skills, and Agents support

### OpenSpec
- **Location:** `collection/skills/openspec/`
- **Purpose:** Specification-driven framework with Gherkin syntax for requirements
- **Triggers:** openspec, open spec, specification, gherkin, scenario, bdd
- **Tools:** read, write, edit, memory
- **Key Features:**
  - Spec deltas for change tracking
  - GIVEN-WHEN-THEN scenario format
  - Version control friendly
  - Perfect for TDD/BDD workflows
  - AI-friendly structured format

### AkShare
- **Location:** `collection/skills/akshare/`
- **Purpose:** Chinese financial data interface library
- **Triggers:** stock data, futures data, fund data, macro economics, akshare
- **Tools:** exec (Python), read, write
- **Key Features:**
  - Stock market data (A-shares, HK stocks, US stocks)
  - Futures market (all major Chinese exchanges)
  - Fund data (ETFs, open-end funds)
  - Macro economics indicators
  - Bond market, forex, cryptocurrency data
  - Options, movies, news, ESG ratings

### Stock Analysis
- **Location:** `collection/skills/stock-analysis/`
- **Purpose:** Comprehensive stock technical analysis with indicators, scoring, and visualization
- **Triggers:** stock analysis, 股票分析, technical analysis, 技术分析, stock indicators, kdj, macd, rsi, boll
- **Tools:** exec (Python), read, write
- **Key Features:**
  - Calculate technical indicators (MA, MACD, KDJ, RSI, BOLL, etc.)
  - Model-based scoring with weighted components
  - Chart generation (K-line, indicators)
  - Single stock and multi-stock comparison
  - Markdown analysis reports

### Skill Extractor
- **Location:** `collection/skills/skill-extractor/`
- **Purpose:** Meta-skill that identifies and extracts reusable skill patterns from conversations
- **Triggers:** 提炼技能, 提取 skill, 生成技能, skill extractor, create skill from conversation
- **Tools:** write, read, glob, memory
- **Key Features:**
  - Auto-detection of recurring patterns
  - Manual extraction trigger
  - Generates standard SKILL.md files
  - Red-highlighted suggestions with user confirmation
  - Cross-session memory integration

### Skill RAG Indexer
- **Location:** `collection/skills/skill-rag-indexer/`
- **Purpose:** RAG indexer for semantic search and intelligent recommendation of local skill documentation
- **Triggers:** skill rag search, search skills, find skill, recommend skill, 搜索技能, 推荐技能, 技能索引
- **Tools:** exec (TypeScript CLI), read, write, glob
- **Key Features:**
  - Semantic search using natural language
  - Task-based skill recommendations
  - Knowledge base management
  - Local-first with zero external dependencies
  - Multi-language support (Chinese/English)

---

See: [skills-collection](https://github.com/your-org/skills-collection) repository for more example skills.
