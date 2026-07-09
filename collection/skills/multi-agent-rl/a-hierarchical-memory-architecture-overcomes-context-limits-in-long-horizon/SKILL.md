---
name: a-hierarchical-memory-architecture-overcomes-context-limits-in-long-horizon
description: 'Large language models (LLMs) demonstrate remarkable reasoning capabilities, yet their stateless architecture fundamentally limits deployment in long-horizon research workflows requiring multi-session. Based on arXiv:2607.07666.'
---

# A hierarchical memory architecture overcomes context limits in long-horizon multi-agent computational modeling

**arXiv**: 2607.07666 | **Authors**: Shivendra G. Tewari, Holly Kimko | **Utility**: 0.9

## Overview

Large language models (LLMs) demonstrate remarkable reasoning capabilities, yet their stateless architecture fundamentally limits deployment in long-horizon research workflows requiring multi-session continuity and quantitative rigor. Here we present Ensemble QSP, a multi-agent framework featuring a three-layer hierarchical memory architecture that keeps injected context bounded and constant in project duration (mid-term project state: median 301 tokens, max 4,050, across 104 runs) by capping each state category and evicting completed work, enabling continuous autonomous operation without context degradation. The system orchestrates five specialist worker agents under domain-expert principal investigators, enforcing physical constraints through physics-based checklists and structured-domain knowledge. Comprehensive benchmarking demonstrates robust autonomous pharmacokinetic-pharmacodynamic model selection without human intervention, consistent result quality across both lower-cost and frontier LLMs, improved PK parameter recovery relative to single-agent baselines, and stable model selection across linguistically diverse prompts of the same task. Feature-level ablation across physiologically based pharmacokinetic (PBPK) models spanning a broad complexity range shows that PI-agent oversight improves debugging efficiency while preserving final accuracy across conditions. The architecture is structurally domain-agnostic, adding a new scientific domain requires only a new PI agent configuration.

## Key Contributions

1. Large language models (LLMs) demonstrate remarkable reasoning capabilities, yet their stateless architecture fundamentally limits deployment in long-horizon research workflows requiring multi-session continuity and quantitative rigor.
2. Here we present Ensemble QSP, a multi-agent framework featuring a three-layer hierarchical memory architecture that keeps injected context bounded and constant in project duration (mid-term project state: median 301 tokens, max 4,050, across 104 runs) by capping each state category and evicting completed work, enabling continuous autonomous operation without context degradation.
3. The system orchestrates five specialist worker agents under domain-expert principal investigators, enforcing physical constraints through physics-based checklists and structured-domain knowledge.
4. Comprehensive benchmarking demonstrates robust autonomous pharmacokinetic-pharmacodynamic model selection without human intervention, consistent result quality across both lower-cost and frontier LLMs, improved PK parameter recovery relative to single-agent baselines, and stable model selection across linguistically diverse prompts of the same task.

## Implementation Notes

- **Keywords**: multi-agent, llm, agent-memory, reasoning, ensemble
- **Categories**: q-bio.QM, cs.MA
- **Published**: 2026-07-08

## Activation Criteria

Use this skill when working on tasks involving: multi-agent, llm, agent-memory, reasoning, ensemble.
