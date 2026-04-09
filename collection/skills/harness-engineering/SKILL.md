# Harness Engineering: Agent-First Development

## Overview

**Source:** OpenAI Blog - "Harness Engineering: Leveraging Codex in an Agent-First World"
**Date:** March 2026
**Significance:** Critical paradigm shift in software engineering
**Key Result:** 1M lines of code in 5 months, 1/10th the time, 3 engineers → 7 engineers, 3.5 PRs/engineer/day

## Activation Keywords

- harness engineering
- agent-first development
- codex engineering
- zero manual code
- agent-generated codebase
- codex workflow

---

## The Experiment

### Constraint
**0 lines of manually-written code**

> "Humans steer. Agents execute."

### Results (5 months)

| Metric | Value |
|--------|-------|
| Lines of code | ~1,000,000 |
| Pull requests | ~1,500 |
| Engineers | 3 → 7 |
| Throughput | 3.5 PRs/engineer/day |
| Time savings | 1/10th of manual coding |
| Users | Hundreds internal, external alpha |

### What Codex Generated
- ✅ Application logic
- ✅ Tests
- ✅ CI configuration
- ✅ Documentation
- ✅ Observability
- ✅ Internal tooling
- ✅ Even the initial AGENTS.md

---

## Core Philosophy

### Human Role Shift

| Before | After |
|--------|-------|
| Write code | Design environments |
| Debug manually | Specify intent |
| Review everything | Build feedback loops |
| Hands-on coding | Enable agents |

### The Key Question

> "What capability is missing, and how do we make it both legible and enforceable for the agent?"

When something fails, the fix is almost **never "try harder"**.

---

## Key Learnings

### 1. Context Management: Map, Not Encyclopedia

**Failed approach:** One big AGENTS.md

Problems:
- Context is scarce → crowds out task/code/docs
- Too much guidance = no guidance
- It rots instantly
- Hard to verify

**Successful approach:**

```
AGENTS.md (~100 lines) → Table of Contents
    ↓
docs/ → System of Record
    ├── Design documentation (indexed, verified)
    ├── Architecture documentation (layering map)
    ├── Quality document (domain grades)
    ├── Plans (first-class artifacts)
    └── Technical debt (versioned)
```

**Progressive disclosure:**
- Small, stable entry point
- Pointers to deeper truth
- Agents learn where to look

### 2. Enforce Constraints, Not Implementations

**Architecture layers (per domain):**
```
Types → Config → Repo → Service → Runtime → UI
         ↑
    Providers (cross-cutting: auth, telemetry, flags)
```

**Enforcement:**
- Custom linters (Codex-generated)
- Structural tests
- "Taste invariants" (logging, naming, file sizes)
- Error messages include remediation instructions

> "In a human-first workflow, these rules might feel pedantic. With agents, they become multipliers: once encoded, they apply everywhere at once."

### 3. Repository as Single Source of Truth

**What agents CAN'T see:**
- Google Docs
- Slack threads
- People's heads
- External context

**What agents CAN see:**
- Code
- Markdown
- Schemas
- Executable plans

> "From the agent's point of view, anything it can't access in-context while running effectively doesn't exist."

**Action:** Push ALL context into the repository.

### 4. UI and Observability Legibility

**Challenge:** Human QA became bottleneck

**Solutions:**

| Capability | Implementation |
|------------|----------------|
| UI testing | Chrome DevTools Protocol, DOM snapshots, screenshots |
| Per-change instances | App bootable per git worktree |
| Logs | LogQL queries |
| Metrics | PromQL queries |
| Traces | Ephemeral observability stack |

**Result:** Prompts like "ensure startup < 800ms" or "no span > 2s in critical journeys" become tractable.

### 5. Agent-to-Agent Review

**Ralph Wiggum Loop:**
1. Codex opens PR
2. Codex reviews own changes locally
3. Request agent reviews (local + cloud)
4. Respond to feedback
5. Iterate until all reviewers satisfied
6. Human review optional (not required)

> "We've pushed almost all review effort towards being handled agent-to-agent."

### 6. Merge Velocity Over Perfection

**Conventional wisdom:** Block on flakes, perfect tests

**Agent-first reality:**
- PRs are short-lived
- Test flakes → follow-up runs, not blocking
- Corrections are cheap, waiting is expensive
- Single Codex runs: 6+ hours (often while humans sleep)

> "In a system where agent throughput far exceeds human attention, corrections are cheap, and waiting is expensive."

---

## Practical Implementation

### Repository Structure

```
repo/
├── AGENTS.md          # ~100 lines, table of contents
├── docs/
│   ├── design/        # Catalogued, indexed, verified
│   ├── architecture/  # Domain/layer map
│   ├── quality/       # Domain grades
│   ├── plans/         # Execution plans (versioned)
│   └── debt/          # Known technical debt
├── src/
│   └── [domain]/
│       ├── types/
│       ├── config/
│       ├── repo/
│       ├── service/
│       ├── runtime/
│       └── ui/
└── .linters/          # Custom (Codex-generated)
```

### AGENTS.md Template (~100 lines)

```markdown
# Agent Guide

## Quick Start
- How to run tests
- How to open PRs
- How to get help

## Architecture
- Link to docs/architecture/
- Layer rules summary

## Key Domains
- Link to each domain's docs/

## Conventions
- Naming patterns
- Logging format
- Test requirements

## Where to Learn More
- Design docs: docs/design/
- Quality status: docs/quality/
- Active plans: docs/plans/
```

### Custom Linters

```python
# Example: Enforce structured logging
def check_logging(node):
    if is_console_log(node):
        return Error(
            "Use structured logging via logger.info()",
            "See docs/conventions/logging.md"
        )
```

**Key:** Error messages include remediation instructions for agent context.

### Doc-Gardening Agent

Recurring agent that:
1. Scans for stale documentation
2. Compares docs to actual code behavior
3. Opens fix-up pull requests
4. Maintains doc/code consistency

---

## Key Metrics to Track

| Metric | Target | Why |
|--------|--------|-----|
| PRs/engineer/day | 3-5 | Throughput indicator |
| Agent review % | >90% | Reduce human bottleneck |
| Doc coverage | >95% | Agent context availability |
| Lint pass rate | >99% | Constraint enforcement |
| PR lifetime | <4 hours | Velocity indicator |

---

## Anti-Patterns to Avoid

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| Giant AGENTS.md | Context pollution | ~100 lines, use pointers |
| Human-written code | Breaks the model | Only prompt-driven changes |
| External documentation | Invisible to agents | Push to repo |
| Blocking merge gates | Slows throughput | Fast merges, fast fixes |
| Human-only reviews | Bottleneck | Agent-to-agent review |

---

## Applicability to OpenClaw

### Current Alignment

| Aspect | OpenClaw | Harness Engineering |
|--------|----------|---------------------|
| AGENTS.md | ✅ Exists | Should be ~100 lines |
| MEMORY.md | ✅ Repo-local | Good pattern |
| docs/ | ⚠️ Partial | Should be structured |
| Agent review | ❌ Not yet | Implement agent-to-agent |
| Custom linters | ❌ None | Add for conventions |
| Doc-gardening | ❌ None | Add recurring agent |

### Improvements to Make

1. **AGENTS.md → ~100 lines** (currently long)
2. **Structure docs/ directory** (design, architecture, quality, plans)
3. **Add custom linters** for agent conventions
4. **Implement agent-to-agent review** for PRs
5. **Add doc-gardening agent** for stale docs
6. **Push Slack discussions to repo** (decisions → markdown)

---

## Quotes to Remember

> "Humans steer. Agents execute."

> "The primary job of our engineering team became enabling the agents to do useful work."

> "Give Codex a map, not a 1,000-page instruction manual."

> "In a system where agent throughput far exceeds human attention, corrections are cheap, and waiting is expensive."

> "Enforce boundaries centrally, allow autonomy locally."

> "Once encoded, they apply everywhere at once."

---

## Description
Framework from arXiv papers. See paper reference for details.
## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents

1. **Understand the Request**: Analyze what the user needs related to this skill's domain.
2. **Search for Information**: Use web_search to find relevant papers or documentation.
3. **Apply the Framework**: Follow the methodology described in the skill's key concepts.
4. **Provide Results**: Summarize findings and actionable recommendations.
5. **Verify Accuracy**: Cross-check key facts before presenting to user.

## Examples

### Example 1: Basic Usage

**User:** How can I apply harness-engineering?

**Agent:** I'll help you understand and apply harness-engineering...

### Example 2: Advanced Application

**User:** What are the key considerations for harness-engineering?

**Agent:** Let me search for the latest research and best practices...

## References

- Blog: https://openai.com/index/harness-engineering/
- AGENTS.md spec: https://agents.md/
- Architecture docs: https://matklad.github.io/2021/02/06/ARCHITECTURE.md.html
- Parse don't validate: https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/
- Execution plans: https://cookbook.openai.com/articles/codex_exec_plans

---

**Created:** 2026-03-28
**Source:** OpenAI Blog - "Harness Engineering" (March 2026)
**Significance:** 🌟🌟🌟🌟🌟 (Critical paradigm shift)