---
name: more-self-adaptive-reasoning
description: "MORE: Mode-optimized reasoning with self-adaptive effort for self-evolving agents. Use when training agents that adaptively select reasoning form and computational effort per task."
version: 1.0.0
author: Hermes Agent
date: 2026-10-27
source: arXiv:2610.33684
tags: [self-evolving-agents, adaptive-reasoning, computational-effort, verifiable-feedback, mode-optimization]
category: multi-agent-rl
---

# MORE: Mode-Optimized Reasoning with Self-Adaptive Effort for Self-Evolving Agents

## Core Contribution

MORE introduces a self-evolving training framework that adaptively selects both reasoning form (which reasoning mode to use) and computational effort (how much compute to spend) for each task. Unlike uniform deliberation, MORE optimizes both dimensions per-task.

## Key Insights

- **Problem**: Self-evolving training applies costly deliberation uniformly across tasks
- **Solution**: Adaptively select reasoning form AND computational effort per task
- **Benefit**: Avoids over-spending on easy tasks while ensuring sufficient effort on hard ones

## Technical Approach

1. **Mode Selection**: Choose appropriate reasoning mode (e.g., fast heuristic vs. deep deliberation) per task
2. **Effort Adaptation**: Dynamically adjust computational budget based on task difficulty
3. **Self-Evolving Training**: Framework improves through verifiable feedback
4. **Joint Optimization**: Optimize both mode and effort together, not independently

## Benefits

- **Efficiency**: Reduces unnecessary computation on easy tasks
- **Performance**: Ensures sufficient effort on difficult tasks
- **Adaptability**: System evolves to better allocate resources over time
- **Verifiable Feedback**: Uses concrete outcomes to guide adaptation

## Applications

- Self-improving agent systems
- Resource-efficient reasoning
- Adaptive computation allocation
- Training agents with variable difficulty tasks

## Activation Triggers

Use this skill when:
- Training self-evolving agents with verifiable feedback
- Need adaptive computational effort allocation
- Want to optimize reasoning mode selection per task
- Building agents that handle tasks of varying difficulty

## Related Concepts

- Self-evolving agents
- Adaptive computation
- Reasoning optimization
- Verifiable reward
- Resource allocation

## References

- arXiv:2610.33684
- Categories: cs.AI
