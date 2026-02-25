# Copilot CLI

## Description
GitHub Copilot CLI is a terminal-native agent experience that lets you chat with GitHub Copilot directly in your shell to plan, edit, run, and review code. It understands repository context, GitHub issues/PRs, and can automate multi-step workflows (autopilot, plan mode, delegated tasks) while keeping you in control of every command.

## Activation Keywords
- copilot cli
- github copilot cli
- copilot terminal
- copilot autopilot
- copilot shell agent

## Tools Used
- exec: Launch `copilot`, run slash commands, or execute helpers like `copilot update`
- read: Inspect generated plan files, configs (e.g., `.copilot` directory)
- write: Create/update skill frontmatter, MCP configs, or CLI instruction files
- edit: Patch Copilot-generated code or configuration snippets referenced in the session
- process: Keep long-running Copilot CLI sessions or delegated tasks in the background

## Installation (if applicable)
```bash
# macOS / Linux (Homebrew)
brew install copilot-cli
# or prerelease
brew install copilot-cli@prerelease

# Windows (WinGet)
winget install GitHub.Copilot
# or prerelease
winget install GitHub.Copilot.Prerelease

# Cross-platform npm
yarn global add @github/copilot
npm install -g @github/copilot

# Official install script (macOS/Linux)
curl -fsSL https://gh.io/copilot-install | bash
# optional custom directory / version
curl -fsSL https://gh.io/copilot-install | VERSION="v0.0.369" PREFIX="$HOME/custom" bash

# Verify
copilot --version
```

### Prerequisites
- Linux, macOS, or Windows (PowerShell ≥ v6). 
- Active GitHub Copilot subscription (personal or org-level with CLI enabled).
- Git configured to access the target repository.
- Optional: `GH_TOKEN`/`GITHUB_TOKEN` PAT with **Copilot Requests** permission for non-browser auth.

## Usage Patterns

### Interactive Pairing Session
```bash
cd /path/to/repo
copilot
/login          # if prompted
/model          # pick Sonnet 4.5, Opus 4.6, GPT-5, etc.
```
Guide Copilot with natural language, approve tool calls, use `@` to mention files, `/diff` to inspect edits, and `Ctrl+S` to send slash commands while typing.

### Autopilot / Plan Mode Loop
```
# Toggle modes (Shift+Tab) or commands
/plan           # structured implementation plan panel
/autopilot      # or select "Autopilot" mode; keeps iterating until task done
/tasks          # monitor background agents
```
Use autopilot for end-to-end execution (with `/allow-all` or `/yolo` when appropriate), then switch back to interactive mode for fine control.

### Delegated Background Workflows
```
/delegate "Add OAuth login"
# CLI branches, runs tasks, optionally opens PRs
/tasks          # view progress, resume, or cancel
/fleet          # orchestrate multiple specialized sub-agents
```
Combine with `/review`, `/usage`, `/context`, `/diff`, `/compact`, `/share`, `/theme`, `/changelog`, `/mcp reload`, `/experimental`, `/streamer-mode`, `/cd`, `/cwd`, `/init`, `/skills add|list`, and shell escapes (`!npm test`).

## Instructions for Agents

### Step 1: Check Access & Install
1. Confirm user has Copilot access. If blocked by org policy, link to enterprise settings docs.
2. Install via preferred package manager (Homebrew, WinGet, npm, or `gh.io/copilot-install`).
3. Ensure `copilot` binary is on PATH; if not, append `export PATH="$INSTALL_DIR:$PATH"` to shell rc.

### Step 2: Authenticate
1. Run `copilot` in the target repository.
2. Use `/login` (OAuth device flow) or set `GH_TOKEN`/`GITHUB_TOKEN` with Copilot Requests permission.
3. `copilot login` CLI subcommand also works outside the TUI.
4. Switch accounts via `/user list|switch`; `/logout` to clear.

### Step 3: Initialize Project Context
1. Run `/init` to generate repo instructions and recommended slash commands.
2. Configure MCP + skills:
   - `~/.copilot/skills/` or `.agents/skills/` for custom skills.
   - `~/.copilot/agents/`, `.github/agents/`, or org `.github` for custom agents.
   - `/skills add path/to/skill` or `/skills enable <name>` to activate.
3. Set up LSP:
   - Install language servers (e.g., `npm install -g typescript-language-server`).
   - Configure user-level `~/.copilot/lsp-config.json` or repo-level `.github/lsp.json`.
4. Optional CLI flags: `--experimental`, `--alt-screen on`, `--config-dir`, `--additional-mcp-config`, `--bash-env`.

### Step 4: Day-to-Day Flow
1. Launch `copilot`, pick model via `/model` (supports Claude Sonnet 4.6, Opus 4.6, GPT-5.2 Codex, GPT-4.1, Opus 4.5, Haiku 4.5, etc.).
2. Use `/terminal-setup` if multiline input glitches (non-kitty terminals).
3. Combine prompt text with `@`-mentioned files and `/` commands:
   - `/diff`, `/review`, `/context`, `/usage`, `/theme`, `/streamer-mode`, `/experimental`, `/tasks`, `/delegate`, `/fleet`, `/share`, `/cd`, `/cwd`, `/mcp reload`, `/changelog`.
4. Approve tool calls selectively; `--allow-all`, `/allow-all`, `/yolo`, `/reset-allowed-tools`, `--available-tools`, and `--excluded-tools` fine-tune permissions. Glob patterns work for shell commands.
5. Use autopilot or plan mode for large efforts; use `Ctrl+O` (expand timeline), `Ctrl+S` (slash command), `Ctrl+Z` (suspend), `Ctrl+D` (send / queue), `Ctrl+N/P` (history), `!` prefix for raw shell.
6. Monitor background tasks via `/tasks`, `/fleet`, `/delegate`, `&prompt` prefix, or autop-run statuses. Cancel stuck work with `/tasks cancel <id>`.
7. Regularly `/diff`, approve changes, and run local tests (Copilot requests permission for `npm test`, `pytest`, etc.).

### Step 5: Handoff & Cleanup
1. `/usage` for premium request counts and token totals (sub-agent usage included).
2. `/share` or `copilot --share` to export transcripts; `--share-gist` for gists.
3. `/compact` (auto at 95%) keeps session small; `/new` or `/clear` resets while retaining mode.
4. Keep CLI current: `copilot update`, `copilot version`, watch `changelog.md` or `/changelog`.

## Context Files

### ~/.copilot/config
```json
{
  "model": "anthropic/claude-sonnet-4.6",
  "altScreen": true,
  "log_level": "info",
  "include_coauthor": true
}
```
Stores global defaults (model, theme, log level, co-author trailers, experimental flags).

### ~/.copilot/lsp-config.json or .github/lsp.json
```json
{
  "lspServers": {
    "typescript": {
      "command": "typescript-language-server",
      "args": ["--stdio"],
      "fileExtensions": {".ts": "typescript", ".tsx": "typescript"}
    }
  }
}
```
Defines language servers used by Copilot CLI.

### ~/.copilot/skills/ / .agents/skills/
Skill frontmatter + markdown instructions auto-load on startup. Use `/skills add`, `/skills remove`, `/skills list` to manage.

### ~/.copilot/agents/ / .github/agents/
Custom agent YAML files discovered by `/agent` or `--agent`. Skills can reference them or spawn via `/delegate`/`/fleet`.

### .claude/commands/ or ~/.copilot/commands/
Single-file slash commands (no frontmatter required) for lightweight automations.

## Error Handling

### `copilot: command not found`
```
# Ensure binary is installed and on PATH
which copilot || echo "Add install dir to PATH"
```
Add PATH export to `.zshrc` / `.bashrc`, rerun shell.

### Login blocked / policy errors
- Run `/login` again; if blocked, confirm Copilot CLI enabled in org/enterprise settings.
- For headless servers, use PAT with Copilot Requests permission and set `GH_TOKEN`.

### Permissions pop up repeatedly
- Use `/allow-all`, `/yolo`, or `--allow-tool shell(npm run test:*)` to pre-approve safe commands.
- `/reset-allowed-tools` clears incorrect grants.

### Large paste / memory warnings
- CLI automatically tokenizes `[Paste #]`. Accept suggestion to start new session when ≤20% context remains.
- Use `/compact` or `/new` if context truncated.

### Model unavailable or errors
- `/model` only lists accessible models; ensure subscription tier. If API blocked, check proxy vars `HTTPS_PROXY`/`HTTP_PROXY`.

### CLI crashes / UI glitches
- Update via `copilot update`.
- Toggle alt-screen with `--alt-screen off` or `/experimental` for fixes.
- On Windows, use PowerShell ≥ v6 and run `copilot /terminal-setup`.

## Configuration

### Environment Variables (Optional)
```bash
export GH_TOKEN="ghp_xxx"          # Fine-grained PAT with Copilot Requests
export HTTPS_PROXY="https://proxy" # Proxy support (Node ≥ 24)
export COPILOT_CLI_CONFIG="$HOME/.copilot" # via --config-dir
export BASH_ENV="$HOME/.copilot/bash"      # works with --bash-env
```

### Configuration File (Optional)
```json
// ~/.copilot/config
{
  "theme": "github-dark",
  "experimental": true,
  "altScreen": true,
  "enable_autopilot": true,
  "include_coauthor": false,
  "launch_messages": ["Remember to run pytest"],
  "permissions": {
    "allowTools": ["shell(npm run test:*)"],
    "denyTools": ["shell(rm -rf *)"]
  }
}
```

## Advanced Usage
- **Autopilot mode**: Press `Shift+Tab` or `/autopilot`; encourages Copilot to keep iterating until completion. Combine with `/tasks` and `/fleet` for multi-agent work.
- **Plan mode**: `/plan` displays structured plan panel; `/delegate` & `/review` consume those plans.
- **Background delegation**: Prefix prompts with `&` or run `/delegate` to offload tasks; CLI commits changes, opens PRs, and updates timeline.
- **Custom agents**: Place definitions in `.copilot/agents` or repo `.github/agents`; invoke with `/agent <name>` or CLI flag `--agent <name>`.
- **Skills & plugins**: `/skills add`, `copilot plugin install <repo|url|path>`, `/plugin marketplace add <url>`; skills now support `disable-model-invocation` and uppercase names.
- **MCP servers**: Configure in `~/.copilot/mcp.json`, `.claude/mcp.json`, or `.vscode/mcp.json`; manage via `/mcp list|enable|disable|reload`. Supports OAuth, GitHub Spaces, remote servers, additional config overrides (`--additional-mcp-config`).
- **LSP tool**: Enable via experimental flag; CLI adds LSP-powered go-to-definition, diagnostics, inline refs.
- **Shell shortcuts**: `Ctrl+X /` (or `Ctrl+S`) runs slash commands without losing input; `Ctrl+O` expand timeline; `Ctrl+E/A/U/K` follow logical lines.
- **Sharing**: `copilot --share`, `/share gist`, `/streamer-mode` hides sensitive info; `/changelog` surfaces recent updates.

## Limitations
- Requires active Copilot subscription; org settings may disable CLI usage.
- Consumes premium request quota per prompt (autopilot/background work can increase usage).
- Needs explicit approvals for file edits/risky commands; cannot bypass security prompts.
- Depends on local Git workspace (no cloud editor UI) and currently optimized for English prompts.

## Best Practices
1. Keep CLI updated (`copilot update`) to pick up model, autopilot, and security fixes.
2. Accept `copilot` autop-run suggestions only after reviewing `/diff` output; revert via undo/rewind or Git if needed.
3. Use `/terminal-setup` on terminals lacking kitty protocol to enable multiline editing.
4. Store sensitive PATs in env managers; prefer `/login` device flow on shared systems.
5. For long tasks, run `/plan` → autopilot, track via `/tasks`, and capture final `/usage` metrics for audits.

## Examples

### Example 1: Build a CLI Feature with Autopilot
```
User: "Add a /metrics endpoint to our FastAPI app."
Agent Process:
1. exec → `copilot`
2. `/plan` to draft steps
3. Switch to Autopilot (Shift+Tab)
4. Approve shell commands (`pip install`, tests) via `/allow-all` for session
5. `/diff` to verify edits, `/review` for summary
6. `/usage` to log premium requests
```

### Example 2: Delegate Background Refactor
```
User: "& Refactor auth middleware to share JWT utilities"
Agent Process:
1. `copilot` running, prompt prefixed with `&`
2. CLI creates branch, runs plan in background
3. `/tasks` shows progress, `/delegate status <id>` gives details
4. `/diff` + `/review` once ready, merge via Git workflows
```

## Troubleshooting

### CLI Fails to Render Properly
```bash
copilot --alt-screen off --experimental
/terminal-setup        # reconfigure terminal sequences
```
Adjust theme via `/theme` and ensure terminal supports kitty protocol or run `copilot --screen-reader` for accessibility.

### OAuth Device Flow Hangs
```bash
copilot login --no-browser
# or
export GH_TOKEN="<fg-pat-with-copilot-requests>"
```
Check firewall/proxy settings (set `HTTPS_PROXY`).

### Permission Dialog Loops
- Press `Esc` to cancel, run `/reset-allowed-tools`, then re-issue command.
- For deterministic tasks, pre-authorize via CLI flags `--allow-tool shell(npm run test:*)`.

### MCP / Skill Not Loading
- Run `/skills` to inspect warnings; fix YAML frontmatter or invalid schema.
- `/mcp reload` reloads servers; check `.vscode/mcp.json` syntax (errors now surface instead of silent failure).

## Resources
- GitHub Copilot CLI README: https://github.com/github/copilot-cli#readme
- Official documentation: https://docs.github.com/copilot/concepts/agents/about-copilot-cli
- Installation script: https://gh.io/copilot-install
- Changelog: https://github.com/github/copilot-cli/blob/main/changelog.md

## Related Skills
- opencode: Full-featured open-source coding agent harness with ultrawork mode.
- claude-code: Anthropic coding companion skill for general IDE-based workflows.
- openspec: Specification-driven development skill that pairs well with Copilot CLI planning.
