# Distributing Hermes Skills to Claude Code

## Problem
Hermes skills in `~/.hermes/skills/` are Hermes-only. Claude Code reads `CLAUDE.md` files but has no access to Hermes skill directory.

## Solution
Write a condensed CLAUDE.md (either global `~/.claude/CLAUDE.md` or project-level) containing the skill's core technical content.

## Key Decisions
- Use `cat << 'EOF' > path` heredoc, NOT write_file (hermes write_file adds line-number prefixes in execute_code)
- Global scope (`~/.claude/CLAUDE.md`) = all Claude Code sessions see it
- Project scope (`<project>/CLAUDE.md`) = only that project
- Keep it 200-500 lines max, dense bullet format
- Include: architecture, algorithms, benchmark headlines, pitfalls, source link

## Obsidian Sync
If user wants the skill also recorded to Obsidian wiki, write to:
`~/Library/Mobile Documents/iCloud~md~obsidian/Documents/AI Research/<topic>.md`

## Checklist
- [ ] Load source skill via skill_view
- [ ] Condense to CLAUDE.md format
- [ ] Write via heredoc to target path
- [ ] Verify file content
- [ ] Update Obsidian if requested
