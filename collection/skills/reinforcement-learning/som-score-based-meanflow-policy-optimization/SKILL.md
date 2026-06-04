---
name: som-score-based-meanflow-policy-optimization
description: SOM (Score-Based One-step MeanFlow Policy Optimization) — actor-critic algorithm combining MeanFlow with online RL using score estimation and probability flow ODE.
---

# SOM: Score-Based MeanFlow Policy Optimization

## Overview

Actor-critic algorithm that combines MeanFlow policy representation with online RL. Constructs target velocity field directly from Q-function via score estimation + probability flow ODE, enabling single-step policy generation without target distribution samples.

## Core Methodology

### Problem
- Diffusion/flow-matching policies require multi-step denoising → computational overhead at inference
- MeanFlow offers one-step generation but needs target distribution samples
- Target distribution unavailable in online RL

### Solution: SOM Framework
1. **Q-function Score Estimation**: Derive score from Q-function gradient
2. **Probability Flow ODE**: Connect score to velocity field
3. **Target Velocity Construction**: Build target velocity from Q-score + probability flow
4. **One-step Policy Update**: MeanFlow policy update in single network evaluation

### Key Insight
Target velocity field = score(Q-function) integrated via probability flow ODE. This concentrates probability mass on high-value modes without needing samples from target distribution.

## Implementation Steps

1. Train Q-function critic as usual
2. Estimate score: ∇log π(a|s) from Q-gradient
3. Solve probability flow ODE to get velocity field
4. Compute target velocity for MeanFlow
5. Update MeanFlow policy with one-step network evaluation

## Applications

- Online RL locomotion tasks
- Continuous control with single-step inference
- Robotics with low latency requirements
- Settings where target distribution unavailable

## Pitfalls

- **Don't**: Use multi-step diffusion when single-step MeanFlow suffices
- **Check**: Velocity field correctly aligns with high-value modes
- **Monitor**: Training stability when combining score + flow ODE

## Related Skills

- [[precise-sde-consistent-rl-flow-matching]] — SDE-consistent sampling for flow-matching RL
- [[model-based-diffusion-policy-optimization]] — MBDPO world model + diffusion

## Activation Keywords

SOM, MeanFlow, score-based policy optimization, one-step policy generation, probability flow ODE, flow-matching RL, single-step generation, online RL diffusion

## Source

arXiv:2605.23365 — Score-Based One-step MeanFlow Policy Optimization