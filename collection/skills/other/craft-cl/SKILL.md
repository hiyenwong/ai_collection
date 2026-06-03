---
name: craft-cl
description: "CRAFT: Forgetting-Aware Intervention-Based Adaptation for continual learning. Avoids weight updates by learning low-rank interventions on hidden representations. Routes in representation space using KL divergence to decide between adaptation and routing. Use when: LLM continual learning, intervention-based adaptation, catastrophic forgetting mitigation, representation-space routing."
---

# CRAFT: Intervention-Based Continual Learning

## Core Innovation

**Does NOT update model weights** — instead learns low-rank interventions applied to hidden representations during inference.

## Mechanism

1. **Low-Rank Intervention Learning**: Learn task-specific interventions Δh = W_down @ W_up @ h
2. **KL-Based Routing**: Compute KL divergence between current and past representations
3. **Adaptation vs. Routing**: If KL < threshold, apply intervention; else route to dedicated intervention

## Advantages

- Zero weight update → no catastrophic forgetting
- Memory efficient — interventions are low-rank
- Composable across tasks

## Paper

- Hossen et al., arXiv:2605.05732, 2026
