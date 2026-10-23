---
name: guideevolve-self-evolving-agent
description: "GuideEvolve: Self-evolving agent framework with expert guidance and 3Ts mechanisms (Think Fast/Slow, Throwback, Termination). Use when building self-improving agent systems."
paper_id: 2610.30017
utility_score: 0.97
categories: [cs.AI]
date: 2026-10-21
tags: [self-evolving-agents, expert-guidance, autonomous-regulation, evolutionary-prompting]
---

# GuideEvolve: Self-Evolving Agent Framework with Expert Guidance and 3Ts Mechanisms

## Key Contribution
Introduces GuideEvolve, a self-evolving agent framework with dual innovations: (1) task-specific expert-evaluation-driven evolutionary prompting, and (2) three autonomous regulatory mechanisms called "3Ts": Think Fast and Slow, Throwback, and Termination by choice.

## Core Method
- **Expert Guidance**: Task-specific experts evaluate agent performance and guide evolutionary search over prompt/strategy space
- **3Ts Mechanisms**:
  - **Think Fast and Slow**: Adaptive switching between fast heuristic and deliberate reasoning modes
  - **Throwback**: Ability to revert to earlier successful strategies when current approach fails
  - **Termination by Choice**: Agent autonomously decides when to stop iterating vs. continue evolving
- **Evolutionary Pipeline**: Population of agent configurations → expert evaluation → selection → mutation → next generation

## Why It Matters
- Addresses critical limitations in self-evolving agent paradigms: unbounded evolution, lack of expert signal, no mechanism to abandon failing strategies
- 3Ts mechanisms provide cognitive realism — mirrors human metacognition (knowing when to think hard, when to fall back, when to stop)
- Expert-driven evolution is more sample-efficient than pure self-play
- Applicable to any LLM agent that needs to improve over repeated deployments

## Application Scenarios
- Long-running autonomous agents that must self-improve
- Coding agents evolving better strategies across tasks
- Customer service agents adapting to new domains
- Research agents refining their search/analysis approaches

## Implementation Notes
- Framework is model-agnostic (works with any LLM backbone)
- Expert evaluators can be rule-based, model-based, or human
- 3Ts mechanisms require minimal overhead — mostly prompt-level control flow
- Throwback needs a strategy memory/store to revert to
