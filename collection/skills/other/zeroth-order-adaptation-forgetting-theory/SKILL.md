---
name: zeroth-order-adaptation-forgetting-theory
description: "Randomized shaping theory explaining why zeroth-order (ZO) adaptation forgets less than first-order methods in continual learning. Activation triggers: zeroth-order adaptation, ZO continual learning, randomized shaping, gradient-free adaptation, catastrophic forgetting, low-query adaptation"
---

# Why Zeroth-Order Adaptation May Forget Less: A Randomized Shaping Theory

> A theoretical framework explaining why zeroth-order (ZO) adaptation retains previously learned capabilities better than first-order (FO) descent in continual learning settings, through the lens of randomized shaping rather than noisy gradient estimation.

## Metadata
- **Source**: arXiv:2605.10658
- **Authors**: Yao Shu, Jian Mu, Zhongxiang Dai
- **Published**: 2026-05-11

## Core Problem

**Catastrophic Forgetting in Continual Learning**: When neural networks adapt to new tasks, they often degrade performance on previously learned tasks. First-order methods (gradient-based) are particularly susceptible because gradients can push parameters in directions that overwrite old knowledge.

**Surprising Observation**: Zeroth-order (ZO) methods, which estimate gradients through function evaluations rather than backpropagation, consistently show better retention of previously learned capabilities despite being viewed traditionally as "noisy" first-order estimators.

## Key Theoretical Insight

### The Randomized Shaping Perspective

**Traditional View**: ZO methods are noisy approximations of FO gradients, and their worse performance is attributed to this noise.

**New Perspective (This Paper)**: ZO methods should be understood through **randomized shaping** — the random perturbations inherent in ZO methods act as a form of implicit regularization that shapes the optimization trajectory in ways beneficial for continual learning.

### Why ZO Forgets Less

1. **Bounded Update Magnitude**: ZO perturbations naturally limit how far parameters can move, preventing large destructive updates to previously learned representations.

2. **Exploration over Exploitation**: The random direction sampling in ZO methods explores the loss landscape more broadly, finding solutions that are less likely to interfere with old task optima.

3. **Implicit Gradient Smoothing**: The averaging over random directions smooths the effective gradient, reducing sensitivity to sharp, task-specific features that cause forgetting.

4. **Low-Query Advantage**: With limited function evaluations, ZO methods naturally take smaller, more conservative steps — a feature, not a bug, for continual learning.

## Mathematical Framework

### ZO Gradient Estimation
The standard ZO gradient estimator uses random perturbations:
```
∇_ZO f(θ) ≈ (f(θ + εu) - f(θ)) / ε · u
```
where u is a random direction vector and ε is the perturbation magnitude.

### Key Theoretical Results

1. **Randomized Shaping Bound**: The expected update direction under ZO can be decomposed into the true gradient plus a shaping term that depends on the Hessian and perturbation distribution.

2. **Forgetting-Retention Tradeoff**: The paper establishes a theoretical bound showing that the expected forgetting is proportional to the update variance — ZO's higher variance in gradient estimation actually corresponds to lower expected interference with old tasks.

3. **Query Complexity vs. Retention**: Fewer ZO queries lead to better retention, revealing a fundamental tradeoff between adaptation speed and memory preservation.

## Practical Implications

### When to Use ZO for Continual Learning
- **Memory-constrained settings** where storing old task data is impossible
- **Online continual learning** where tasks arrive sequentially
- **Large models** where full backpropagation is expensive
- **Few-shot adaptation** where only limited new data is available

### Design Principles
1. **Perturbation magnitude tuning**: Larger ε → more exploration but slower adaptation
2. **Query budget allocation**: Balance between adaptation quality and forgetting prevention
3. **Hybrid approaches**: Combine ZO for stability with occasional FO for precision

## Applications
- Continual learning for LLMs without replay buffers
- Online adaptation of deployed models
- Parameter-efficient fine-tuning with memory constraints
- Multi-task learning with sequential task arrival

## Pitfalls
- **Slower convergence**: ZO methods require more iterations to reach optima
- **Query efficiency**: Naive ZO uses O(d) queries; advanced methods needed for high dimensions
- **Perturbation sensitivity**: Performance depends on ε choice and random direction distribution
- **Not universal**: Some settings (large batch, stationary tasks) still favor FO methods

## Related Skills
- continual-learning-methods
- catastrophic-forgetting-mitigation
- parameter-efficient-fine-tuning
