---
name: agentic-agile-v
description: Agentic Agile-V framework for verified AI-assisted engineering — SCOPE-V micro-cycle (Specify, Constrain, Orchestrate, Prove, Evolve, Verify) for software, firmware, and hardware development using AI coding agents.
category: systems-engineering
tags:
  - agentic-engineering
  - agile-v
  - scope-v
  - ai-agents
  - verified-engineering
  - systems-engineering
source: arXiv:2605.20456
author: Christopher Koch
---

# Agentic Agile-V: Verified Engineering with AI Agents

Based on: *Agentic Agile-V: From Vibe Coding to Verified Engineering in Software and Hardware Development* (arXiv:2605.20456)

## Overview

Agentic AI coding systems can inspect repositories, plan implementation steps, edit files, call tools, run tests, and submit pull requests. However, the central problem is no longer **prompt engineering** — it is **engineering process control**.

Agentic Agile-V provides a process framework that uses Agile-V as the lifecycle backbone and a task-level **SCOPE-V loop** to convert conversational intent into structured engineering artifacts and acceptance evidence.

## Core Contribution: The SCOPE-V Micro-Cycle

Each task is executed through a six-step micro-cycle:

| Step | Name | Description |
|------|------|-------------|
| **S** | **Specify** | Create a task brief with clear requirements, acceptance criteria, and constraints |
| **C** | **Constrain** | Define boundaries: file scope, dependencies, permissions, risk level |
| **O** | **Orchestrate** | Plan and execute agent work: tasks, tool calls, test runs |
| **P** | **Prove** | Generate evidence: test results, logs, diffs, coverage |
| **E** | **Evolve** | Iterate based on feedback, fix defects, refine implementation |
| **V** | **Verify** | Independent verification and acceptance review |

## Conversation-to-Contract Gate

After discovery/discussion with the user, the relevant intent **must** be converted into a reviewed execution brief. Do not rely solely on chat history:

1. Extract requirements from conversation
2. Write a structured task brief (template below)
3. Get the user's approval on the brief
4. Execute within the approved scope

## Minimum Input Artifacts

### For Software Tasks
- **Feature Brief**: requirements, acceptance criteria, affected files, risk level (R1/R2/R3)
- **Bug Brief**: reproduction steps, expected behavior, actual behavior, environment
- **Test Plan**: test scope, expected coverage, risk mitigation

### For Hardware/Firmware Tasks
- **Hardware Brief**: constraints, interface definitions, timing requirements, platform
- **Verification Plan**: simulation scope, formal checks, HIL requirements

## Risk-Adaptive Workflows

### Risk Levels
- **R1 (Low)**: Isolated changes, comprehensive test coverage, no external dependencies
  - Workflow: Auto-approve after CI passes
- **R2 (Medium)**: Moderate scope, some test gaps, external integrations
  - Workflow: Require human review of plan + evidence bundle
- **R3 (High)**: Core architecture, public API changes, hardware/firmware
  - Workflow: Full brief + human review + evidence bundle + rollback plan

## Evidence Bundle Requirements

For R2 and R3 tasks, assemble an evidence bundle containing:
- Task brief and requirement identifiers
- Agent plan and affected files
- Executed commands and test results
- Diff summary and known residual risks
- Trace from acceptance criteria to tests
- Reviewer decision and follow-up actions
- Rollback or recovery path for production changes

## When to Use Conversation

Conversation helps with:
- Requirement discovery and surfacing ambiguity
- Comparing architectures
- Identifying risks early

Conversation is **not sufficient** for:
- Implementation without a brief
- Changes where bugs would be expensive
- Hardware, firmware, or safety-critical work
- Multi-file changes without a plan

## When to Apply This Skill

**Activation**: agentic engineering, AI agent workflow, verified engineering, software agent process, AI code review, agent safety, engineering process control, SCOPE-V

Apply this skill when:
- Using AI coding agents (Claude Code, Codex, Copilot, etc.) for production work
- Setting up agent guidelines for a team
- Implementing review gates for AI-generated code
- Working on hardware/firmware with AI assistance
- Designing agent evaluation benchmarks

## Usage Pattern

```
1. DISCOVER → Have conversation to surface intent
2. CONTRACT → Write task brief, get user approval
3. EXECUTE → Agent implements within constraints
4. PROVE → Run tests, collect evidence
5. REVIEW → Human reviews evidence bundle
6. ACCEPT → Approve or rollback
```

## Template: Feature Brief

```markdown
## Feature Brief

**Title**: [Feature name]
**Risk Level**: R1 / R2 / R3
**Requirements**: [Bulleted list]
**Acceptance Criteria**: [Executable criteria]
**Constraints**: [Files, dependencies, permissions]
**Affected Components**: [List]
**Rollback Strategy**: [How to revert]
```

## References

- Koch, C. (2026). Agentic Agile-V: From Vibe Coding to Verified Engineering in Software and Hardware Development. arXiv:2605.20456.
