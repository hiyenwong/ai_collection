---
name: d2evo-dual-difficulty-self-evolution
description: "D²Evo methodology — Dual Difficulty-Aware Self-Evolution for data-efficient reinforcement learning in LLM reasoning. Addresses Effective Data Scarcity and Dynamic Difficulty Shifts by automatically selecting medium-difficulty samples via dual difficulty scoring (performance-based + entropy-based). Use when: data-efficient RL post-training for LLMs, curriculum-free self-evolution, difficulty-aware sample selection, GRPO data optimization, RL training data management. Activation: D2Evo, dual difficulty self-evolution, data-efficient RL LLM, difficulty-aware RL training, curriculum-free RL, medium-difficulty sample selection."
---

# D²Evo: Dual Difficulty-Aware Self-Evolution for Data-Efficient RL

## Overview

D²Evo addresses two fundamental challenges in RL post-training for LLM reasoning:
1. **Effective Data Scarcity** — medium-difficulty training samples (those the model can solve with effort) are rare
2. **Dynamic Difficulty Shifts** — as training progresses, previously hard/easy samples shift difficulty, making static curricula obsolete

## Core Methodology

### Dual Difficulty Scoring

Each sample is scored on two orthogonal dimensions:

**1. Performance Difficulty (PD):**
- Based on model's pass rate on the sample
- `PD(s) = 1 - pass_rate(s)` — high when model struggles
- Estimated from multiple rollout attempts

**2. Entropy Difficulty (ED):**
- Based on response diversity across attempts
- High entropy = model is uncertain/exploring → good learning signal
- `ED(s) = H(response_distribution)` — measures uncertainty

### Sample Selection Strategy

A sample is selected for RL training when:
- PD is moderate (not trivially easy, not impossibly hard)
- ED is high (model shows learning potential)

This creates a **dynamic learning zone** that adapts as the model improves, without manual curriculum design.

### Self-Evolution Loop

```
1. Generate N responses per sample via rollout
2. Compute PD and ED for each sample
3. Filter to "learning zone" samples (moderate PD + high ED)
4. Train on selected subset via RL (GRPO/PPO)
5. Repeat — learning zone shifts as model improves
```

## Key Insights

- **Static data budgets waste compute** on samples that are too easy (already mastered) or too hard (beyond current capability)
- **Dual scoring outperforms single-dimension scoring** — performance alone misses uncertain samples; entropy alone includes random guessing
- **Automatic curriculum emergence** — no manual difficulty scheduling needed

## Implementation

### Difficulty Estimation
```python
def compute_dual_difficulty(samples, model, n_rollouts=4):
    results = {}
    for s in samples:
        responses = [model.generate(s) for _ in range(n_rollouts)]
        # Performance difficulty: 1 - accuracy
        pd = 1 - mean([is_correct(r) for r in responses])
        # Entropy difficulty: response diversity
        ed = compute_entropy(responses)
        results[s] = {'pd': pd, 'ed': ed}
    return results

def select_learning_zone(results, pd_range=(0.2, 0.8), ed_threshold=0.5):
    return [s for s, r in results.items()
            if pd_range[0] <= r['pd'] <= pd_range[1]
            and r['ed'] >= ed_threshold]
```

### Practical Guidelines

- Use 4-8 rollouts per sample for reliable difficulty estimation
- PD range `[0.2, 0.8]` captures the "Goldilocks zone"
- Re-evaluate difficulty every 100-500 training steps
- Works with GRPO, PPO, and other on-policy RL methods

## Applications

- RL post-training for mathematical reasoning
- Code generation RL with verifiable rewards
- Any domain where sample difficulty is heterogeneous
- Reducing RL training compute by 30-50% via data selection

## Related

- [[learning-zone-energy-data-selection]] — complementary data selection approach
- [[sdar-self-distilled-agentic-rl]] — self-distilled agentic RL
- [[scalelogic-rl-reasoning]] — RL reasoning scaling methodology
- [[tool-integrated-reasoning-recipe]] — SFT+RL pipeline

## Paper

- arXiv: D²Evo: Dual Difficulty-Aware Self-Evolution for Data-Efficient Reinforcement Learning
- Submitted: May 2026
