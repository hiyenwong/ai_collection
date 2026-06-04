---
name: precise-sde-consistent-rl-flow-matching
description: Precise — SDE-consistent stochastic sampling for RL post-training of flow-matching models with clean-latent posterior mean freezing.
---

# Precise: SDE-Consistent RL Flow Matching

## Overview

Stochastic sampler design for RL post-training of flow-matching models. Decomposes sampler into exploration amount + discretization faithfulness. Uses "clean-latent posterior mean freezing" to ensure SDE-consistency at small step counts.

## Core Methodology

### Problem
- Flow-matching models use deterministic ODE; RL needs stochastic policy
- Standard reverse-time SDE introduces excess noise at small step counts
- Exploration vs. denoising stability tradeoff

### Solution: Precise Framework
1. **Sampler Decomposition**: Exploration amount + discretization faithfulness
2. **SDE Schedule Design**: Balance exploration vs. denoising stability
3. **Clean-Latent Posterior Mean Freezing**: Freeze posterior mean during sampling
4. **SDE-Consistency**: Ensure discretization matches continuous SDE at small steps

### Key Insight
At small step counts, standard samplers add excess discretization noise. Precise freezes the clean-latent posterior mean to keep the denoising trajectory SDE-consistent.

## Implementation Steps

1. Derive SDE schedule from ODE: add noise proportional to exploration needs
2. Identify clean-latent posterior mean in flow-matching architecture
3. Freeze posterior mean during sampling process
4. Tune exploration amount based on reward landscape
5. Use small step counts for RL efficiency

## Applications

- RL post-training for image generation models
- Diffusion policy alignment (PickScore, HPSv2.1)
- Flow-matching models with reward optimization
- Text-to-image generation RL

## Pitfalls

- **Don't**: Use standard reverse-time SDE directly at small steps
- **Check**: Posterior mean freezing correctly implemented
- **Monitor**: Training time vs. prior methods (should see reduction)

## Related Skills

- [[som-score-based-meanflow-policy-optimization]] — MeanFlow one-step policy
- [[daca-grpo-denoising-credit-assignment]] — Denoising-aware GRPO

## Activation Keywords

Precise, SDE-consistent sampling, flow-matching RL, stochastic sampler design, posterior mean freezing, diffusion RL post-training, clean-latent freezing, small-step sampling

## Source

arXiv:2605.23522 — Precise: SDE-Consistent Stochastic Sampling for RL Post-Training of Flow-Matching Models