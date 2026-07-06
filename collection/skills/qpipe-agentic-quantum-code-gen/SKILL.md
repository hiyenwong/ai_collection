---
name: qpipe-agentic-quantum-code-gen
description: "LLM-based multi-agent architecture for autonomous quantum application generation from natural language requirements. Use when building agentic systems for quantum software engineering, automated quantum code generation, NL-to-quantum workflows, or quantum test optimization pipelines. Activation: qpipe, agentic quantum code generation, LLM quantum application, natural language quantum workflow, quantum test optimization agent, multi-agent quantum compilation, autonomous quantum code review."
metadata:
  arxiv_id: "2607.00939"
  published: "2026-07-01"
  tags: [quantum, software-engineering, llm, multi-agent, code-generation]
---

# QPipe Agentic Quantum Code Generation

## Description

LLM-based multi-agent architecture that autonomously turns natural language requirements into traceable quantum-application workflows through specialized agents.

## Core Architecture

### Agent Decomposition
- **Requirement Parsing Agent**: Extracts quantum-specific requirements from NL
- **Formulation Agent**: Translates requirements into quantum circuit specifications
- **Code Generation Agent**: Generates executable quantum code (Qiskit/Cirq/etc.)
- **Review Agent**: Validates quantum code correctness and optimization
- **Execution Agent**: Runs quantum circuits on simulators/hardware
- **Verification Agent**: Validates results against expected outcomes

### Performance Metrics
- 100% code compilation rate across 20 benchmarks
- 96.7% application execution success rate
- Average generation: 260 seconds, 1.89M tokens per requirement
- Generated solutions outperform offline genetic algorithm baseline

### Key Ablation Findings
Success depends on retaining:
1. Code-generation skills
2. Task knowledge
3. Review feedback
4. Multi-agent decomposition

## When to Use
- Building agentic systems for quantum software engineering
- Automated quantum code generation from specifications
- Quantum test optimization pipelines
- NL-to-quantum workflow automation

## Pitfalls
- Token costs are significant (~1.89M per requirement)
- Multi-agent coordination overhead is non-trivial
- Requires strong quantum domain knowledge in LLM prompts
- Review feedback loop is critical — skipping it degrades quality
