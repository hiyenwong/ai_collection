# Claude Code

## Description
Anthropic's official AI-powered coding companion. A command-line tool that integrates with your Claude subscription and helps you write, debug, and understand code with natural language commands.

## Activation Keywords
- claude-code
- claude code
- @anthropic
- anthropic coding
- claude cli
- claude terminal

## Tools Used
- exec: Run claude-code CLI
- read: Read code files
- write: Write code files
- edit: Edit code files
- process: Manage long-running sessions

## Installation

### Install via npm
```bash
npm install -g @anthropic-ai/claude-code
```

### Verify Installation
```bash
claude-code --version
```

### Authentication
```bash
claude-code auth
```
Follow the instructions to sign in with your Claude account.

### Quick Start
```bash
# Navigate to your project
cd /path/to/project

# Start Claude Code
claude-code
```

## Usage Patterns

### Reading and Understanding Code

**Explain specific file:**
```
Explain how the authentication middleware works in src/middleware/auth.ts
```

**Understand project structure:**
```
Give me an overview of this project's architecture
```

**Explain complex logic:**
```
Walk me through the algorithm in src/utils/data-processing.js
```

### Writing Code

**Create new feature:**
```
Add error handling to the user authentication function in src/auth.js
```

**Implement specific functionality:**
```
Create a REST API endpoint for getting user profile
```

**Generate boilerplate:**
```
Create a React component for a user profile card with TypeScript
```

### Debugging

**Debug an error:**
```
I'm getting a 500 error when calling /api/users. Help me debug it.
```

**Fix a bug:**
```
The login form isn't submitting. Find and fix the issue.
```

**Investigate unexpected behavior:**
```
The data isn't rendering correctly in the dashboard. Help me troubleshoot.
```

### Refactoring

**Refactor code:**
```
Refactor the database connection logic to use a connection pool
```

**Improve code quality:**
```
Review and improve the code in src/services/api.ts
```

**Apply patterns:**
```
Refactor the authentication logic to follow the pattern used in src/middleware/auth.ts
```

### Testing

**Generate tests:**
```
Generate unit tests for the user service in src/services/user.service.ts
```

**Run tests:**
```
Run the test suite and fix any failing tests
```

**Debug test failures:**
```
The user login test is failing. Help me fix it.
```

## Instructions for Agents

When user mentions Claude Code or related tasks:

### 1. Verify Installation
Check if claude-code is installed:
```bash
claude-code --version
```

If not installed, guide user through:
```bash
npm install -g @anthropic-ai/claude-code
claude-code auth
```

### 2. Navigate to Project
Always work in the project directory:
```bash
cd /path/to/project
```

### 3. Start Claude Code
Start a session:
```bash
claude-code
```

For long-running tasks, consider using background mode:
```bash
claude-code &
```

### 4. Use Natural Language Commands
Claude Code understands natural language. Be specific:
- "What" questions: "What does this function do?"
- "How" questions: "How do I add error handling?"
- Action requests: "Add X to Y"
- Debugging: "Why is this happening?"

### 5. Iterate and Refine
Claude Code learns from context:
- Ask follow-up questions
- Provide feedback on results
- Request changes or alternatives

### 6. Manage Context
Claude Code maintains context:
- Mention relevant files
- Reference previous work
- Describe project structure

## Context Files

Claude Code automatically reads these when available:

### README.md
Project overview and setup instructions

### package.json
Dependencies and scripts

### tsconfig.json / jsconfig.json
TypeScript/JavaScript configuration

### AGENTS.md
Agent instructions (OpenCode format, also works)

### .clauderc / claude.json
Claude Code project configuration

## Configuration

### Project Config (.clauderc or claude.json)
```json
{
  "model": "claude-sonnet-4.5",
  "maxTokens": 200000,
  "temperature": 0.3,
  "tools": ["file_operations", "git", "testing"],
  "skills": ["typescript", "react"],
  "hooks": {
    "preToolUse": "hooks/pre-tool-use.js",
    "postToolUse": "hooks/post-tool-use.js"
  }
}
```

### Environment Variables
```bash
# Set default model
export CLAUDE_MODEL="claude-sonnet-4.5"

# Set API key (alternative to auth)
export ANTHROPIC_API_KEY="your-api-key"
```

## Advanced Features

### MCP (Model Context Protocol)
Extend Claude Code with MCPs:

**Tool MCP:**
```json
{
  "name": "my-tool",
  "type": "tool",
  "path": "./mcp/tools/my-tool.js"
}
```

**Resource MCP:**
```json
{
  "name": "my-resource",
  "type": "resource",
  "path": "./mcp/resources/my-resource.js"
}
```

**Prompt MCP:**
```json
{
  "name": "my-prompt",
  "type": "prompt",
  "path": "./mcp/prompts/my-prompt.js"
}
```

### Hooks System
Extend behavior with hooks:

**PreToolUse:** Before tool execution
**PostToolUse:** After tool execution
**UserPromptSubmit:** Before sending user message
**Stop:** On session termination

### Skills
Create reusable skills for common tasks:

**Command skill:**
```javascript
// skills/create-component.js
module.exports = {
  name: "create-component",
  description: "Create a React component",
  execute: (context) => {
    // Component generation logic
  }
};
```

### Agents
Specialized agents for different tasks:

**Coding agent:** Write and implement code
**Review agent:** Review code quality
**Testing agent:** Generate and run tests

## Common Commands

### File Operations
- `@file.txt` - Read specific file
- "Create file X" - Create new file
- "Delete file X" - Remove file
- "Move file X to Y" - Move/rename file

### Git Operations
- "Create a commit" - Commit changes
- "Review changes" - Show git diff
- "Create a branch" - Create new branch
- "Merge X into Y" - Merge branches

### Testing
- "Run tests" - Execute test suite
- "Generate tests for X" - Create tests
- "Debug failing tests" - Fix test failures

### Build Process
- "Build the project" - Run build command
- "Fix build errors" - Resolve build issues

## Error Handling

### Authentication Issues
```
If you see "Not authenticated":
  1. Run: claude-code auth
  2. Follow browser authentication
  3. Retry your request
```

### API Errors
```
If you see API rate limit errors:
  1. Wait a moment and retry
  2. Reduce request frequency
  3. Consider using a different model
```

### Context Limit
```
If you see context limit errors:
  1. Ask Claude to summarize current context
  2. Focus on specific files
  3. Reduce prompt complexity
```

### Installation Issues
```
If claude-code won't install:
  1. Check Node.js version (requires Node 16+)
  2. Clear npm cache: npm cache clean --force
  3. Try with verbose: npm install -g @anthropic-ai/claude-code --verbose
```

## Best Practices

### 1. Be Specific
Clear, specific requests get better results:
- ✅ "Add error handling to the login function"
- ❌ "Make the code better"

### 2. Provide Context
Give Claude context about your code:
- Mention the programming language
- Reference related files
- Describe the project structure

### 3. Iterate Effectively
- Start with a simple request
- Review and provide feedback
- Ask for changes or improvements

### 4. Use Files
- Use @ to reference specific files
- Let Claude read code naturally
- Don't paste large code blocks

### 5. Review Before Committing
- Test generated code
- Review for security issues
- Check edge cases

## Examples

### Example 1: Adding a Feature
```
User: "Add error handling to the user authentication function in src/auth.js"

Claude Code:
1. Reads src/auth.js
2. Identifies the authentication function
3. Adds try-catch blocks
4. Adds logging for errors
5. Adds user-friendly error messages
6. Suggests testing approach

Result: Updated src/auth.js with comprehensive error handling
```

### Example 2: Debugging
```
User: "I'm getting a 500 error when calling /api/users. Help me debug it."

Claude Code:
1. Reads the API endpoint code
2. Checks database queries
3. Reviews error logs
4. Identifies missing error handling
5. Adds proper error handling
6. Suggests logging improvements

Result: Fixed API endpoint with proper error handling and logging
```

### Example 3: Understanding Code
```
User: "Explain how the middleware chain works in server.js"

Claude Code:
1. Reads server.js
2. Identifies middleware functions
3. Explains execution order
4. Describes what each middleware does
5. Provides examples of adding new middleware

Result: Clear explanation of middleware architecture with examples
```

## Limitations

- Requires active Claude subscription for full access
- Model choice is limited to Claude models
- Context window depends on model (up to 200K tokens for Opus)
- Some advanced features may require additional setup

## Resources

- **Official Docs:** https://platform.claude.com/docs
- **Pricing:** https://claude.com/pricing
- **Claude Website:** https://claude.com
- **GitHub:** https://github.com/anthropics/claude-code

## Related Skills
- **coding-agent:** Generic coding agent with multiple tool support
- **opencode:** Open source coding agent with plugin system
- **obsidian:** For documentation and note-taking in code projects

## Notes

- Claude Code uses your existing Claude subscription
- Usage counts towards your Claude API limits
- Best for users primarily using Claude models
- Integrates seamlessly with Claude's other tools and services
