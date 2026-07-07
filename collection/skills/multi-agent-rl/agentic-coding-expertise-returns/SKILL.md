---
name: agentic-coding-expertise-returns
trigger_words:
  - agentic coding
  - Claude Code
  - coding agent
  - domain expertise
  - labor market AI
  - AI coding productivity

description: Analysis of ~400,000 Claude Code sessions showing domain expertise (not coding skill) determines success with coding agents. People make planning decisions; agents make execution decisions. Task value rose 25% over 7 months.

activation_pattern: When analyzing AI coding tools, labor market impacts of AI, or how domain expertise interacts with AI assistants

scope: Research synthesis and practical insights for AI-assisted development workflows

author: Anthropic Research
date: 2026-06-16
source: https://www.anthropic.com/research/claude-code-expertise
---

# Agentic Coding and Persistent Returns to Expertise

## Overview

Privacy-preserving analysis of ~400,000 Claude Code sessions from ~235,000 users (Oct 2025 - Apr 2026) revealing how domain expertise amplifies AI coding effectiveness.

## Key Findings

### Division of Labor
- **People**: Planning decisions (what to build)
- **Agent**: Execution decisions (how to build)
- Greater domain expertise → more work Claude does per instruction

### Success Rates
- Every major occupation succeeds at nearly same rate as software engineers on coding tasks
- Domain experts succeed more often than intermediates, but gap is **modest**
- Proficiency is enough to use tool almost as effectively as deep mastery

### Work Modes (9 Categories)
1. **Building** - Creating something new
2. **Fixing** - Debugging broken code
3. **Testing** - Writing/running tests
4. **Orchestrating** - Managing other agents/pipelines
5. **Operating** - Deploying, configuring, monitoring
6. **Understanding** - Analyzing existing systems
7. **Planning** - Designing architecture
8. **Analyzing data** - Data analysis tasks
9. **Writing docs** - Non-code documentation

### 7-Month Trends (Oct 2025 → Apr 2026)
- Debugging share fell by **nearly half**
- Shift toward end-to-end agentic use (deploying, running, analyzing)
- Typical task value rose **~25%** across all work types

## Labor Market Implications

1. **Success = domain understanding, not coding training**
2. Agents reward firm understanding of problems being solved
3. Coding agents **not substituting** for domain expertise
4. More understanding → more quality work the agent can do

## Practical Applications

### For Developers
- Focus on domain knowledge over syntax mastery
- Use agent for execution; reserve planning for yourself
- Higher domain expertise → leverage agent more effectively

### For Organizations
- Coding proficiency barriers may diminish
- Domain expertise becomes primary productivity driver
- Training focus should shift to problem understanding

### For Tool Designers
- Design for human planning + agent execution split
- Support domain experts with varying coding backgrounds
- Reduce debugging burden through better agent capabilities

## Methodology

- **Dataset**: ~400,000 sessions, ~235,000 users
- **Timeframe**: October 2025 - April 2026
- **Privacy**: Privacy-preserving analysis techniques
- **Platforms**: CLI, Claude.ai, desktop app
- **Success metric**: Verifiable evidence (tests pass, code committed)

## Related Work

- Prior measures of autonomy in Claude Code sessions
- How Claude Code is changing work at Anthropic
- GitHub coding agent activity doubled since late 2025
- Average usage: 20 hours/week per user

## Limitations

- Limited to Claude Code users (may not generalize)
- Early-stage tool, patterns may evolve
- Self-reported occupation categories
- Cannot fully isolate model improvement effects