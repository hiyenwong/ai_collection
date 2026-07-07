---
name: claude-code-token-optimization
category: devops
description: Token optimization methodology for CLI coding agents (Claude Code, OpenCode, Gemini CLI, Codex). Reduces overhead 70%→35%, effectively 2-3x capacity increase. Covers CLAUDE.md bloat, session history, plugin hooks, cache expiry, skill/MCP overload, extended thinking, and wasted output.
triggers: claude code, opencode, gemini cli, codex, token optimization, quota limit, overhead, claude.md, session history, plugin hooks, cache, mcp, extended thinking, usage limit, codex-cli
---

# CLI Agent Token Optimization

## Core Mental Model

Every session is not a blank slate—it's an **invoice**. Before your prompt even arrives, the system has already charged:

- CLAUDE.md (always loaded)
- Every active plugin Hook (always injected)
- Every relevant Skill's SKILL.md (loaded on any "relevance" match)
- Every connected MCP's tool schema (always transmitted)
- Full conversation history (always re-read)
- Cache-expired re-tokenization (after 5 min idle)

**"Productive tokens" are what remains after overhead. You optimize overhead first, prompt second.**

## The 7 Traps (sorted by impact)

### Trap 1: CLAUDE.md Bloat

CLAUDE.md loads every single turn. A 5000-word CLAUDE.md at 200 turns/week = 1M tokens just on rules.

**Target:** Combined global + project CLAUDE.md ≤ 1200 English words (~1500 tokens).

**Fix:**
```bash
wc -w ~/.claude/CLAUDE.md 2>/dev/null  # global
wc -w .claude/CLAUDE.md 2>/dev/null     # project-level
```

Refactoring rules:
1. Framework-specific rules → project-level CLAUDE.md only (not global)
2. Recurring complex patterns → extract as Skills (zero cost when not invoked)
3. Delete rules you can't remember the reason for
4. Rewrite explanatory sentences into 3-word imperatives. Claude needs commands, not reasons.

Typical result: 4800 → 900 words, behavior unchanged, baseline cost drops 30%.

### Trap 2: Session History Exponential Re-reading

Each new message re-tokenizes the entire history. Message #60 costs 60x message #1.

**Fix:**
1. **Edit, don't append.** Arrow-up → edit → resend. Replaces the bad turn instead of stacking on top.
2. **Hard limit: 20 messages per session.** After that: ask the agent to summarize, open a new session, paste summary as first message.
3. **Use `/compact`, not `/clear`.** `/compact` summarizes and restarts (keeps essentials, drops fluff). `/clear` loses everything including useful context.

Typical result: 60 messages → 15 messages, history cost drops ~40%.

### Trap 3: Plugin Hooks Silently Injecting

Plugins with `UserPromptSubmit` hooks inject content before your prompt arrives. 4 plugins can silently add 6000+ tokens. `SessionStart` hooks add "I'm ready!" notifications (~1400 tokens from 9 plugins).

**Fix:**
```bash
# Check what's being injected
cat ~/.claude/settings.json | jq '.hooks.UserPromptSubmit' 2>/dev/null
cat ~/.claude/settings.json | jq '.hooks.SessionStart' 2>/dev/null

# Audit rule: if you can't explain WHY it needs to trigger every time, disable it
# /plugin disable <plugin-name>
```

Keep only `UserPromptSubmit` hooks you can justify (e.g., git branch info). Kill the rest.

Typical result: 4 → 1 UserPromptSubmit hook, 9 → 2 SessionStart hooks. Each prompt saves ~5800 tokens.

### Trap 4: Prompt Cache Expiry (5 minutes)

Prompt cache expires after 5 minutes of idle. Return after coffee → system prompt + CLAUDE.md + MCP schemas (~8000 tokens) all re-tokenize at full price instead of 10% cache-read price.

**Fix:**
- **Quick workaround:** Bind a hotkey to send a trivial "ping" before stepping away. Keeps cache alive.
- **Proper fix:** Upgrade to 1-hour cache (if available via API tier). Cache writes cost 2x base price (one-time), reads cost 0.1x. Breaks even after ~10 cache recoveries per session—easily exceeded in a workday.

Typical result: cache expiry cost drops ~80%.

### Trap 5: "Just in Case" Syndrome (Skills + MCP Overload)

Unused Skills load on any fuzzy relevance match (~1500 tokens each). All connected MCPs send their full tool schema every request (~7000 tokens for 12 MCPs, but you only use 3).

**Combined overhead: ~20,000 tokens per request, for nothing.**

**Fix:**
```bash
# 7-day audit: which Skills were actually invoked?
grep -h "skill_invoked" ~/.claude/logs/*.log | sort | uniq -c | sort -rn

# Skills not in output → disable all of them

# Check connected MCPs
# /mcp    # see how many you have
# /mcp disable <server>   # disable unused in current session
```

Edit `~/.claude/settings.json` to remove rarely-used MCPs from auto-load. Enable on-demand.

Typical result: 11 Skills → 4, 12 MCPs → 3. Saves ~15,000 tokens per request.

### Trap 6: Extended Thinking Global Switch

Extended Thinking burns 3000+ thinking tokens on trivial tasks ("rename this variable"). Only valuable for architecture decisions, complex debugging.

**Fix:**
- **Default OFF.** Enable per-message when needed (`Alt+T` in Claude Code).
- **Heuristic:** If the agent's first answer is unsatisfactory, retry with Extended Thinking ON. 80% of tasks don't need it.

### Trap 7: Letting Wrong Answers Finish

Agent writes 400 lines. You see it's wrong at line 50. Letting it finish wastes output tokens (priced higher than input). ~$15/month wasted this way.

**Fix:**
- **`Cmd+.` (Mac) / `Ctrl+.` (Windows) — immediately stop generation.** Agent keeps what's written, you redirect from there.
- **Train reflex:** Hit stop within 5 seconds of recognizing wrong direction. It won't "get better."
- Claude Code bonus: double-tap `Esc` to open checkpoint rollback—revert to any prior state and try a different approach.

## Pre-baked Audit Script

Run this in your project root:

```bash
#!/bin/bash
echo "=== 1. CLAUDE.md size ==="
wc -w ~/.claude/CLAUDE.md 2>/dev/null
wc -w .claude/CLAUDE.md 2>/dev/null
echo "Target: combined < 1200 words"

echo "=== 2. UserPromptSubmit injection ==="
cat ~/.claude/settings.json 2>/dev/null | jq '.hooks.UserPromptSubmit'
echo "Target: 1-2, fewer is better"

echo "=== 3. SessionStart Hook ==="
cat ~/.claude/settings.json 2>/dev/null | jq '.hooks.SessionStart'
echo "Target: only essential ones"

echo "=== 4. Installed Skills ==="
ls ~/.claude/skills/ 2>/dev/null
echo "Target: 3-5 matching daily work"

echo "=== 5. Connected MCPs ==="
cat ~/.claude/settings.json 2>/dev/null | jq '.mcpServers // {} | keys'
echo "Target: 3 always-on, rest on-demand"
```

Run weekly until every line hits target.

## What DOESN'T Work (Common Myths)

| Advice | Actual Impact | Why |
|---|---|---|
| "Use Haiku for simple tasks" | ~3% savings | Context bloat dominates; cheap model on bloated context costs more than expensive model on lean context |
| "Always /clear between tasks" | Negative effect | Loses needed context, forces re-explanation. Better: one long session per project with lean CLAUDE.md + audited hooks |
| "Disable ALL Skills" | Net loss | You end up rewriting 200-token instructions in every prompt. Keep 3-4 truly-used Skills |
| "Avoid peak hours" | ~7% impact | Only affects quota throttling, doesn't fix overhead. The 7 levers above matter far more |

## Agent-Specific Notes

### OpenCode
- Uses `.opencode/skills/` directory (similar SKILL.md loading pattern)
- MCP configuration in `.opencode/settings.json`
- No direct `/compact` equivalent — summarize manually and start new session

### Gemini CLI
- No CLAUDE.md equivalent (uses system instructions differently)
- Session history re-read issue still applies — keep sessions under 20 turns
- No plugin hooks, but extensions may inject context — audit extensions

### Codex
- **System instructions**: Keep system prompt files lean (<1200 words). Same bloat principle as CLAUDE.md — every turn reloads the full context.
- **Session history**: Exponential re-read cost applies equally. Hard cap at ~20 messages, then summarize + restart.
- **No /compact equivalent** — manually summarize progress and open new session.
- **Extended Thinking equivalent**: Use reasoning/o1 models only when needed (architecture, complex debug). Don't default to them for simple edits — they burn massive thinking tokens on trivial tasks.
- **Stop generation**: Codex supports interrupt (Ctrl+C). Use it the moment you spot wrong direction — don't wait for it to finish.
- **Sandbox/tool overhead**: Each connected tool/sandbox adds schema overhead. Audit and disable unused tools.

## The Bottom Line

70% of "Claude got dumber" is overhead. 30% is the model itself.

Fix all 7 traps → productive token ratio goes from ~30% to ~65%. Real-world feel: **2-3x more capacity from the same subscription.**
