---
name: contractual-skills-governspec
description: "Contractual Skills: A GovernSpec Design Framework for Enterprise AI Agents. Based on arXiv:2605.22634 (May 2026). Use when designing governance layers for AI agent systems, structuring skill files as inspectable task contracts, or implementing verification gates for enterprise AI agent runtimes."
---

# Contractual Skills: GovernSpec Design Framework

Core methodology from arXiv:2605.22634 (May 2026). Author: Ting Liu.

## Problem

Enterprise AI agent skills need to express more than task guidance. They must make goals, input boundaries, permissions, evidence requirements, output contracts, quality criteria, verification steps, human approval points, and handoff rules inspectable. Without this structure:
- **Black-box skills**: Instructions are opaque, making governance impossible
- **Unsafe tool calls**: Agents may attempt high-risk operations without guardrails
- **No contract enforcement**: No formal way to verify agent outputs against requirements
- **Fragile handoffs**: Agent-to-agent or agent-to-human transitions lack clear protocols

## Solution: Contractual Skills Framework

A GovernSpec-inspired design framework for organizing SKILL.md files as readable task contracts while preserving lightweight skill discovery and progressive loading.

### Core Components

#### 1. Contractual Skill Structure
Each contractual skill is organized around these governable fields:
- **Goal**: What the skill achieves (declarative intent)
- **Input boundaries**: What data/parameters the skill accepts
- **Permissions**: What tools, files, or systems the skill may access
- **Evidence requirements**: What the skill must demonstrate/prove
- **Output contracts**: Expected outputs with type/structure specifications
- **Quality criteria**: Acceptable quality thresholds
- **Verification steps**: How to verify the skill executed correctly
- **Human approval points**: Where human-in-the-loop is required
- **Handoff rules**: How to transition between skills or to human operators

#### 2. Governance Boundary
The framework clarifies the boundary between:
- **Contractual skills** (task contracts with governance metadata)
- **GovernSpec YAML contracts** (formal governance specifications)
- **Model Context Protocol surfaces** (tool/API interfaces)
- **Tool adapters** (implementation-level tool wrappers)
- **Runtime guardrails** (enforcement at execution time)
- **Tracing** (observability and audit trails)
- **Evaluation systems** (post-execution assessment)

#### 3. Multi-Layer Protection
```
Contractual Skill (design-time intent)
  → GovernSpec (formal governance policy)
    → MCP Surface (tool interface definition)
      → Tool Adapters (runtime tool wrappers)
        → Runtime Guardrails (execution-time enforcement)
          → Tracing (observability)
            → Evaluation (post-execution assessment)
```

### Key Findings

#### Text Generation Study
- **Setup**: 3 enterprise skills, 15 synthetic tasks, 4 instruction conditions, 8 generation models
- **Scale**: 960 outputs, 1680 cross-judge score records
- **Results**:
  - Contractual skills outperform no-skill and minimal-skill baselines on ALL tested models
  - Gains relative to information-rich plain expanded skills are small and mixed
  - Primary value is in **checkability and maintainability**, not raw generation quality

#### Tool-Calling Challenge
- **Setup**: 8 models, 192 simulated tool-call records
- **Results**:
  - Skills usually reduce high-risk tool attempts
  - Model differences remain significant
  - Runtime tool guardrails are still required as safety net

### Practical Recommendation

Contractual skills are best understood as a **governance layer** that makes task intent, boundaries, and acceptance criteria explicit — NOT as a standalone safety mechanism. Key takeaways:

1. **Use for governance, not safety**: Contractual skills make intent inspectable but don't replace runtime guardrails
2. **Improve maintainability**: Explicit contracts make skills easier to audit and update
3. **Enable verification**: Quality criteria and verification steps enable systematic output checking
4. **Support handoffs**: Clear handoff rules enable reliable multi-agent coordination
5. **Combine with tool guardrails**: Always pair contractual skills with runtime enforcement

## Implementation Patterns

### Pattern 1: Contractual Skill Template
```yaml
goal: "What this skill achieves"
input_boundaries:
  - "What parameters are accepted"
  - "What assumptions are made"
permissions:
  - "Tools/files/systems allowed"
evidence_requirements:
  - "What must be demonstrated"
output_contract:
  format: "Expected output format"
  structure: "Output structure specification"
quality_criteria:
  - "Acceptable quality thresholds"
verification:
  - "Steps to verify execution"
human_approval_points:
  - "Where human review needed"
handoff_rules:
  - "How to transition between skills"
```

### Pattern 2: Governance Stack Integration
```
┌─────────────────────────┐
│ Contractual Skill       │  Intent specification
├─────────────────────────┤
│ GovernSpec YAML         │  Formal policy
├─────────────────────────┤
│ MCP Surface             │  Tool interface
├─────────────────────────┤
│ Runtime Guardrails      │  Execution enforcement
├─────────────────────────┤
│ Tracing & Evaluation    │  Observability & audit
└─────────────────────────┘
```

## Related Skills
- [[spec-driven-agent-architecture]] - Workflow and architecture patterns for building robust AI agents
- [[llm-decision-centric-design]] - Decision-centric framework for LLM systems
- [[logact-agentic-reliability]] - LogAct for agentic reliability via shared logs

## Activation Keywords
- contractual skills, GovernSpec, AI agent governance
- enterprise AI agents, skill contracts, task contracts
- agent verification, safe agent execution
- AI agent guardrails, agent handoff protocols
- governed multi-agent runtime, agent admission control
