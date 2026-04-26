---
name: multi-orft-diffusion-planning
description: "Multi-ORFT: Stable Online Reinforcement Fine-Tuning for multi-agent diffusion planning in cooperative driving. Combines diffusion models with online RL for closed-loop consistent multi-agent trajectory planning. 激活词: multi-agent diffusion planning, online reinforcement fine-tuning, cooperative driving, Multi-ORFT"
category: systems-engineering
date_created: 2026-04-14
source_paper: arXiv:2604.11734
---

# Multi-ORFT: Stable Online RL Fine-Tuning for Multi-Agent Diffusion Planning

## Overview

Stable Online Reinforcement Fine-Tuning (Multi-ORFT) for multi-agent cooperative driving. Addresses scene consistency and closed-loop alignment in diffusion-based planners.

## Problem Statement

**Challenge**: Existing diffusion planners exhibit weak scene consistency and poor closed-loop alignment despite modeling multimodal behaviors.

## Technical Framework

### Multi-Agent Diffusion Model

**Joint Trajectory Distribution**:
```
p(x^{1:N}_{0:T} | c) = ∏_{t=0}^{T-1} p(x_t | x_{t+1}, c)
```

### Stable Online Fine-Tuning

**Mechanisms**:
1. **Trust Region Constraint**: D_KL(π_θ || π_θ_old) ≤ δ
2. **Behavior Cloning Regularization**: L_total = L_RL + λ * L_BC
3. **Importance Sampling**: E[ρ(τ) * R(τ) * ∇log π(τ)]

## Algorithm

```python
class MultiORFT:
    def pretrain(self, expert_data):
        """Behavior cloning pre-training"""
        # Train diffusion model on expert demonstrations
        
    def online_finetune(self, simulator):
        """Stable online RL fine-tuning"""
        # 1. Collect trajectories
        # 2. Compute policy gradient
        # 3. Add BC regularization
        # 4. Trust region constraint
```

## Applications

- Autonomous driving
- Cooperative vehicles
- Traffic simulation
- Multi-robot coordination

## Activation Keywords

multi-agent diffusion planning, online reinforcement fine-tuning, Multi-ORFT, cooperative driving, scene consistency
