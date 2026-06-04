---
name: sbsrl-sampling-based-safe-rl
description: SBSRL — Sampling-based safe RL with joint constraint enforcement across dynamics samples and epistemic uncertainty exploration constraints.
---

# SBSRL: Sampling-Based Safe RL

## Overview

Model-based RL for safe exploration. Enforces safety constraints jointly across finite dynamics samples (approximating worst-case optimization). Uses epistemic uncertainty as exploration constraint without explicit bonuses.

## Core Methodology

### Problem
- Safe exploration fundamental challenge in RL
- Worst-case optimization over uncertain dynamics intractable
- Need safety guarantees throughout learning (not just at convergence)

### Solution: SBSRL Framework
1. **Dynamics Ensemble**: Learn ensemble of dynamics models from data
2. **Joint Constraint Enforcement**: Draw multiple dynamics samples; enforce constraints on all jointly (not per-sample)
3. **Epistemic Uncertainty Exploration**: Use ensemble disagreement as exploration bound (no bonus needed)
4. **Theoretical Guarantees**: High-probability safety throughout learning + finite-time sample complexity

### Key Insight
Joint constraint across samples approximates worst-case without computational burden. Epistemic uncertainty naturally bounds exploration.

## Implementation Steps

1. Collect initial safe data
2. Train ensemble of dynamics models (capture uncertainty)
3. For each policy optimization:
   - Draw N dynamics samples from ensemble
   - Solve for policy that satisfies constraints on all N samples jointly
   - Use epistemic uncertainty (ensemble disagreement) to bound exploration
4. Deploy policy, collect new data, repeat

## Applications

- Robot learning with safety constraints
- Autonomous vehicle control
- Industrial process control
- Medical RL applications
- Hardware experiments

## Pitfalls

- **Don't**: Enforce constraints per-sample (overly conservative or unsafe)
- **Check**: Ensemble captures dynamics uncertainty adequately
- **Monitor**: Safety throughout learning (not just final policy)

## Related Skills

- [[lilac-safe-continual-rl]] — safe continual RL under nonstationarity
- [[efficient-tdmpc]] — efficient TDMPC

## Activation Keywords

SBSRL, sampling-based safe RL, ensemble dynamics, joint constraint, epistemic uncertainty exploration, safe exploration, model-based safe RL, dynamics uncertainty

## Source

arXiv:2605.19469 — Sampling-Based Safe Reinforcement Learning