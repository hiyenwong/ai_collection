---
name: cord-conflict-aware-rl-distillation
description: "CORD: Conflict-Aware Optimization for Joint RL and Distillation in Agents. Addresses gradient conflicts when combining RL and distillation objectives."
paper_id: 2610.29965
utility_score: 0.78
categories: [cs.LG]
date: 2026-10-21
tags: [reinforcement-learning, distillation, multi-objective-optimization, gradient-conflict, agent-training]
---

# CORD: Conflict-Aware Optimization for Joint RL and Distillation in Agents

## Key Contribution
Addresses the gradient conflict when combining reinforcement learning (RL) and distillation objectives in agent training. RL and distillation often pull parameters in different directions, causing suboptimal convergence. CORD detects and resolves these conflicts.

## Core Method
- **Problem**: When training agents with both RL (reward maximization) and distillation (matching teacher behavior), gradients can conflict — RL gradient points one direction, distillation gradient points another
- **Consequence**: Naive combination (weighted sum) leads to oscillation, slow convergence, or convergence to suboptimal point
- **Solution (CORD)**:
  - **Conflict detection**: Monitor cosine similarity between RL and distillation gradients
  - **Conflict resolution**: When conflict detected (negative cosine similarity), project gradients to remove conflicting components
  - **Techniques**: 
    - PCGrad-style projection: remove component of one gradient that conflicts with the other
    - Dynamic weighting: adjust RL vs. distillation weight based on conflict severity
    - Selective updates: only update parameters where gradients agree
- **Integration**: Drop-in module for any RL + distillation pipeline

## Why It Matters
- First work to explicitly address RL-distillation gradient conflicts in agent training
- Practical for anyone combining RL fine-tuning with distillation (very common in LLM alignment)
- Improves convergence speed and final performance
- Applicable to multi-objective optimization beyond RL+distillation

## Application Scenarios
- RLHF with distillation from stronger models
- Combining offline RL (behavior cloning) with online RL
- Multi-task agent training where objectives conflict
- Any scenario combining imitation learning with reward-based learning

## Implementation Notes
- Conflict detection: compute cosine similarity between gradient vectors (cheap with autograd)
- Resolution: PCGrad projection adds minimal overhead (one additional backward pass)
- Threshold: conflict detected when cosine similarity < 0 (can tune threshold)
- Works with any RL algorithm (PPO, SAC, DQN) + any distillation method (KD, behavior cloning)
- Recommended: start with PCGrad projection, add dynamic weighting if needed
