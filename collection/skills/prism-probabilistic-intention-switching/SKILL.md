---
name: prism-probabilistic-intention-switching
description: "PRISM (Probabilistic Recurrent Intention Switching Model) for multi-intention inverse reinforcement learning - lightweight recurrent network mapping observation history to intention distribution with O(nK) E-step decomposition. Use when modeling goal switching within episodes, recovering temporally coherent intentions from unlabeled demonstrations, or applying multi-intention IRL to robotic manipulation. Keywords: multi-intention IRL, intention switching, recurrent intention distribution, goal switching, EM decomposition."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.26998"
  published: "2026-05-26"
  authors: "Wenyuan Sheng, Hao Zhu, Joschka Boedecker"
  tags: [inverse-reinforcement-learning, multi-intention, recurrent-network, intention-switching, goal-switching, EM-algorithm, robotic-manipulation]
---

# PRISM: Probabilistic Recurrent Intention Switching Model

## Core Innovation

PRISM replaces traditional multi-intention IRL mechanisms with a lightweight recurrent network that maps observation history to per-step intention distribution, achieving exact EM decomposition.

**Key advantage:** O(nK) E-step with no variational approximation - closed-form solution for each intention.

## Problem: Goal Switching in IRL

**Traditional IRL limitation:** Assumes single stationary reward per episode.

**Existing multi-intention approaches:**
- Markov chain intention transitions (memoryless)
- Manual state augmentation with fixed history window

**PRISM innovation:** Recurrent network for intention distribution - captures non-Markovian dependencies naturally.

## Mathematical Framework

### EM Objective Decomposition

**Theorem:** EM objective decomposes exactly into independent per-intention reward subproblems.

**Result:**
- Each intention: Closed-form solution
- Complexity: O(nK) E-step
- No variational approximation needed
- Provably optimal decomposition

### Architecture Components

1. **Recurrent intention network** - Maps history → intention distribution
2. **Per-intention reward functions** - K independent reward models
3. **Per-step intention assignment** - Probabilistic, not hard segmentation

## Algorithm

### E-Step (Intention Assignment)

```
For each timestep t:
    q_t(k) = RNN(h_t) → intention distribution
    where h_t = observation history up to t
```

**Key:** History-dependent, not memoryless Markov or fixed-window.

### M-Step (Reward Recovery)

```
For each intention k:
    Solve reward r_k in closed form
    Independent of other intentions
```

**Key:** Exact decomposition, no coupling between intentions.

## Applications

### Evaluated Domains

1. **Non-Markovian gridworld** - Intention switching with history dependence
2. **Mouse labyrinth** - Biological goal-switching behavior
3. **BridgeData V2 robotic manipulation** - First large-scale multi-intention IRL application

**Results:**
- Highest held-out log-likelihood
- Recover nameable, temporally coherent intentions
- No trajectory segmentation labels needed

### Robotic Manipulation Insights

**Discovery:** Discrete goal switching present in both biological and artificial agents.

**Implication:** Multi-intention structure universal, not artifact.

## Methodology

### Applying PRISM

1. **Collect demonstrations** - Unlabeled trajectories
2. **Define intention count K** - Number of latent goals
3. **Train recurrent intention network** - History → distribution
4. **EM optimization** - Iterative intention assignment + reward recovery
5. **Extract intentions** - Nameable, temporally coherent segments

### Key Design Decisions

**Recurrent network choice:**
- Lightweight (not heavy LSTM/transformer)
- History encoding sufficient
- Per-step distribution output

**Intention initialization:**
- Uniform or informed prior
- EM convergence typically fast

## Advantages vs Traditional Methods

| Method | Memory | History | Complexity |
|--------|--------|---------|------------|
| Markov chain | None | Fixed | Variational |
| State augmentation | Window | Limited | O(nK²) |
| **PRISM** | Recurrent | Full | **O(nK)** |

## Use Cases

### When to Use PRISM

1. **Goal switching within episodes** - Not just trajectory-level intentions
2. **Non-Markovian intention dependence** - History matters
3. **Unlabeled demonstrations** - No segmentation needed
4. **Large-scale robotic data** - First multi-intention IRL at scale
5. **Temporal coherence extraction** - Nameable intention recovery

### Activation Keywords

- `PRISM`, `probabilistic recurrent intention switching`, `multi-intention IRL`
- `goal switching`, `intention distribution`, `EM decomposition`
- `non-Markovian IRL`, `recurrent intention network`

## Key Insights

1. **Exact decomposition** - No variational approximation sacrifice
2. **History captures switching** - Recurrent beats fixed window
3. **Intention coherence emerges** - From EM optimization, not labeling
4. **Universal goal switching** - Present in biological and artificial agents

## References

- Sheng, Zhu, Boedecker (2026) - PRISM original paper [arXiv:2605.26998]
- Multi-intention IRL literature - Trajectory segmentation methods
- EM algorithm theory - Probabilistic latent variable models

## Pitfalls

- **Over-segmentation:** Choosing too large K fragments intentions
- **Markov assumption:** Don't use for truly non-Markovian switching
- **Fixed window:** Recurrent network needed for full history dependence
- **Variational approximation:** PRISM exact, don't substitute

## Summary

PRISM provides O(nK) multi-intention IRL through recurrent intention network and exact EM decomposition. Replaces memoryless Markov and fixed-window approaches with full history dependence. Recovers temporally coherent intentions from unlabeled demonstrations. First large-scale robotic application shows goal switching universal across biological and artificial agents.