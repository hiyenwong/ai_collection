---
name: lilac-safe-continual-rl
description: LILAC+ — Safe continual RL under nonstationarity with adaptive safety constraints (context-based, adaptation-speed, budget-to-state).
---

# LILAC+: Safe Continual RL under Nonstationarity

## Overview

Framework for safe continual RL in nonstationary environments. Combines three adaptive safety mechanisms: context-based constraints (proactive), adaptation-speed constraints (reactive), and budget-to-state enforcement (local).

## Core Methodology

### Problem
- Safe RL assumes fixed constraints/stable environment
- Distribution shift in nonstationary settings invalidates fixed safety mechanisms
- Need safety that adapts to environmental changes

### Solution: LILAC+ Three Mechanisms
1. **Context-Based Safety Constraints**: Infer/predict environmental context → adjust safety thresholds per context
2. **Adaptation-Speed Constraints**: Monitor environment change rate vs. agent adaptation speed → tighten when change outpaces adaptation
3. **Budget-to-State Enforcement**: Maintain cumulative safety budget → convert to state-level constraints at each decision

### Key Insight
Nonstationarity requires both proactive (anticipate changes) and reactive (respond to changes) safety mechanisms. Budget-to-state provides local enforceable constraints.

## Implementation Steps

1. Train context inference model (recognize environmental regimes)
2. Define safety thresholds per context
3. Monitor adaptation speed: track environment change rate
4. If change > adaptation speed, tighten safety thresholds
5. Maintain cumulative safety budget across episodes
6. At each decision, convert remaining budget to state-level constraint

## Applications

- Autonomous driving under nonstationary conditions
- Continual RL with safety requirements
- Robotics in changing environments
- Safe RL with distribution shift

## Pitfalls

- **Don't**: Assume fixed safety thresholds in nonstationary settings
- **Check**: Context inference correctly identifies environmental regimes
- **Monitor**: Safety violations reduced under distribution shift

## Related Skills

- [[sbsrl-sampling-based-safe-rl]] — sampling-based safe RL
- [[clipping-bottleneck-nsr]] — near-boundary stochastic rescue

## Activation Keywords

LILAC, safe continual RL, nonstationary RL, adaptive safety constraints, context-based safety, budget-to-state, distribution shift, safe RL adaptation

## Source

arXiv:2605.18842 — LILAC+: Safe Continual Reinforcement Learning under Nonstationarity via Adaptive Safety Constraints