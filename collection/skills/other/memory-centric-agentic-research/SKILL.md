---
name: memory-centric-agentic-research
description: "Memory-centric agentic system methodology for full scientific research lifecycle automation. Covers schema-governed research memory (SciMem), five-stage lifecycle execution (SciFlow), DAG-shaped multi-agent operators (SciDAG), and self-evolving feedback loops (SciEvolve). Use when designing autonomous research agents, building persistent AI research systems, implementing scientific workflow automation, or creating self-improving agent systems. Activation: memory-centric agent, agentic research, autonomous scientist, research lifecycle automation, SciMem, SciFlow, SciDAG, SciEvolve"
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.31468"
  published: "2026-05-29"
  authors: "Weitong Qian, Beicheng Xu, Zhongao Xie, et al."
  tags: [agentic-ai, research-automation, memory-systems, scientific-workflow]
---

# Memory-Centric Agentic Research

## Overview

Automated scientific research requires persistent memory across projects, structured lifecycle execution, and self-improvement from feedback. AutoSci (arXiv:2605.31468) provides a unified four-module architecture for the full research lifecycle: literature understanding → hypothesis formulation → experimentation → manuscript writing → rebuttal.

## Core Modules

### SciMem: Schema-Governed Research Memory

Two-tier memory separation:
- **Long-Term Knowledge Memory (LTKM)**: Reusable scientific knowledge that persists across all projects
- **Active Research Memory (ARM)**: Project-level artifacts (ideas, experiments, manuscripts, reviews)

**Key principle**: Schema governance ensures structured, queryable memory rather than unstructured text dumps. Memory entries follow consistent schemas for retrieval and reasoning.

### SciFlow: Five-Stage Lifecycle Execution

Controlled harness manages:
1. **Literature Understanding** — parse and synthesize related work
2. **Hypothesis Formulation** — generate testable hypotheses from literature gaps
3. **Experimentation** — design and execute experiments
4. **Manuscript Writing** — produce publication-quality papers
5. **Rebuttal** — respond to reviewer feedback

Each stage uses state management, context preservation, verification, and feedback orchestration.

### SciDAG: DAG-Shaped Multi-Agent Operators

For complex skills requiring coordination:
- Represent difficult operations as DAGs of sub-tasks
- Reuse stage-specific templates across research projects
- Enable parallel execution where dependencies allow

### SciEvolve: Self-Evolving System

Converts feedback signals into versioned updates:
- **User feedback** → update SciMem organization
- **Experiment results** → refine SciFlow skills
- **Review responses** → improve SciDAG templates
- **External environment** → adapt all components

## Methodology

### Designing a Persistent Research Agent

1. **Define memory schema** — What knowledge persists vs. what is project-scoped?
2. **Implement lifecycle harness** — State machine controlling research stages with verification checkpoints
3. **Build multi-agent DAGs** — Decompose complex operations (e.g., "run experiment") into coordinated sub-tasks
4. **Add evolution loop** — All feedback must produce versioned updates, not just logging

### Key Design Decisions

| Decision | AutoSci Approach | Why |
|----------|-----------------|-----|
| Memory organization | Two-tier (LTKM + ARM) | Cross-project knowledge vs. project artifacts have different lifecycles |
| Search structure | Explicit parent pointers (tree) | Implicit trace history loses structural information during backtracking |
| Skill evolution | Versioned updates from feedback | Ensures traceable improvement, prevents regression |

### Integration with Existing Agent Systems

- **Compatible with**: Any LLM-based agent framework with tool-use capability
- **Requires**: Persistent storage (database), state machine controller, feedback collection mechanism
- **Extends**: Single-turn agents → persistent multi-project research environments

## Pitfalls

- **Memory bloat**: Without schema governance, research memory becomes unstructured and useless. Enforce strict schemas for all memory entries.
- **Stage coupling**: Research stages must be independently verifiable. If one stage fails, later stages should not silently produce incorrect results.
- **Feedback overload**: Not all feedback signals are equally useful. Prioritize experiment results and reviewer feedback over environmental noise.
- **Template rigidity**: SciDAG templates should be parameterized, not hardcoded. Overly rigid templates prevent adaptation to novel research scenarios.

## Related Skills

- `agent-coordinator` — Agent orchestration patterns
- `autopoiesis-self-evolving-systems` — Self-evolving system paradigms
- `coral-open-ended-discovery` — Open-ended discovery workflows
