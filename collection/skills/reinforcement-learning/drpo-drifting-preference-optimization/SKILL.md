---
name: drpo-drifting-preference-optimization
description: Drifting Preference Optimization (DrPO) - Online preference-finetuning for one-step generative models using non-parametric dipole preference fields and reference drift estimation.
---

# DrPO: Drifting Preference Optimization for One-Step Generative Models

## Core Methodology

DrPO enables preference finetuning for **deterministic one-step generators** (like SD-Turbo, SDXL-Turbo) without requiring:
- Policy likelihoods
- Denoising trajectories
- Differentiable reward gradients
- Test-time optimization

### Key Innovation: Non-parametric Feature-Space Update

For each prompt:
1. Sample candidates from current generator
2. Rank them with target reward (black-box/non-differentiable allowed)
3. Synthesize update direction from high- and low-scoring samples

### Update Mechanism

**Dipole Preference Field**: Direction derived from difference between high-scoring and low-scoring sample features

**Reference Drift**: Stability anchor from frozen base generator, estimated to prevent catastrophic drift

**Feature-Space Regression**: Detached targets ensure stable optimization without reward backpropagation

## Implementation Details

### Algorithm Steps

1. **Candidate Sampling**: Generate N samples per prompt
2. **Reward Ranking**: Use target reward for ranking only (not gradients)
3. **Feature Extraction**: Extract latent features from samples
4. **Dipole Construction**: High-score - low-score feature difference
5. **Drift Estimation**: Reference generator provides anchor
6. **Regression Target**: Detached feature-space target

### Design Advantages

- **Black-box rewards**: Works with non-differentiable reward models
- **No reward backprop**: Removes expensive reward-model gradients
- **Single inference call**: Maintains one-step generation speed
- **Online learning**: Adapts continuously during deployment

## Results

- Improved alignment over reward-gradient-free one-step preference baselines
- Reduced HPSv3 training computation by removing reward-model backpropagation
- Effective on SD-Turbo and SDXL-Turbo with HPSv3 and GenEval benchmarks

## Applications

Use when:
- Preference alignment for one-step generative models
- Non-differentiable or black-box reward models
- Reducing training computation for preference finetuning
- Online adaptation during model deployment

## Trigger Keywords

- preference optimization
- one-step generator
- black-box reward
- dipole preference field
- reference drift
- non-parametric update
- feature-space regression

## Related Skills

- [[daca-grpo-denoising-credit-assignment]]
- [[conditional-equivalence-dpo-rlhf]]
- [[delta-discriminative-token-credit-assignment]]
- [[oppo-token-credit-assignment]]