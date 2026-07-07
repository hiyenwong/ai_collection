---
name: suco-sufficiency-guided-continuous-adaptive-reasoning
description: "SuCo - Sufficiency-guided Continuous Adaptive Reasoning for LRM efficiency. Minimal Sufficient CoT (MSC) defines shortest prefix adequate for correct answer. Two-stage training: MSC-Aligned Fine-Tuning + Sufficiency-Aware Policy Optimization. Use when: (1) LRMs generate excessive CoT, (2) need principled stopping criterion, (3) reasoning budget optimization. Activation: MSC, sufficiency, adaptive reasoning, CoT efficiency, continuous spectrum."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2606.17687v1"
  published: "2026-06-16"
  authors: "Jiahao Wang, Bingyu Liang, Chenhao Hu et al."
  tags: [reasoning, efficiency, sufficiency, CoT, policy-optimization]
---

# SuCo: Sufficiency-guided Continuous Adaptive Reasoning

Framework for autonomous reasoning control along a continuous spectrum using Minimal Sufficient CoT (MSC).

## Core Concept: Minimal Sufficient CoT (MSC)

**Definition**: Shortest prefix of a CoT trajectory adequate for producing correct answer.

**Key finding**: MSC not only reduces reasoning tokens, but also **improves accuracy** across difficulty levels.

## Two-Stage Training Framework

### Stage 1: MSC-Aligned Fine-Tuning (MFT)

1. Construct MSC data using **problem-adaptive sufficiency thresholds**
2. Thresholds naturally scale with question difficulty
3. Fine-tune model to internalize concise yet sufficient reasoning patterns

```python
def compute_msc_prefix(cot_trajectory, problem_difficulty):
    """
    Problem-adaptive threshold scales with difficulty.
    Returns shortest prefix that yields correct answer.
    """
    sufficiency_threshold = adaptive_threshold(problem_difficulty)
    for i, step in enumerate(cot_trajectory):
        if can_solve_with_prefix(cot_trajectory[:i+1]):
            return cot_trajectory[:i+1]
```

### Stage 2: Sufficiency-Aware Policy Optimization (SAPO)

1. **Dynamic complexity tracking** during RL optimization
2. **Sufficiency-aware rewards** that penalize:
   - Over-thinking (excessive reasoning after sufficient solution)
   - Under-thinking (insufficient reasoning for problem)

```python
def sufficiency_reward(reasoning_length, msc_length, correctness):
    """
    Penalizes both over- and under-thinking.
    """
    if correctness:
        # Reward efficiency
        efficiency_bonus = -abs(reasoning_length - msc_length)
    else:
        # Under-thinking penalty
        efficiency_penalty = -reasoning_length  # encourage more reasoning
    return correctness_reward + efficiency_bonus
```

## Continuous Spectrum Control

Unlike discrete reasoning modes or fixed budget tiers:
- MSC provides **principled criterion** for when reasoning is sufficient
- Control operates on **continuous spectrum** (not tiered budgets)
- Autonomous adaptation based on problem characteristics

## When to Apply

- LRMs generate excessively long CoT for simple queries
- Need principled stopping criterion beyond fixed budgets
- Reasoning efficiency optimization without accuracy sacrifice

## Pitfalls

- **Threshold calibration**: Problem-adaptive thresholds require careful tuning
- **MSC construction**: Determining exact sufficiency point can be noisy
- **Reward balance**: Over-thinking and under-thinking penalties need balancing

## Related Patterns

- See `dre-dynamic-rollout-editing` for training-time overthinking intervention
- See `early-stopping-confidence-dynamics` for confidence-based stopping

---

arXiv: [2606.17687v1](https://arxiv.org/abs/2606.17687v1)