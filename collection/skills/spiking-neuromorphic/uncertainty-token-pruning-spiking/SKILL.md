---
name: uncertainty-token-pruning-spiking
description: >
  Training-free token pruning for spiking transformers using temporal uncertainty patterns.
  Models token-wise class evidence with Dirichlet distribution and summarizes each token's
  temporal uncertainty via mean and fluctuation across spiking steps. Tokens with low
  uncertainty contribution are pruned during inference. Use when optimizing spiking
  transformer inference efficiency, reducing token redundancy in SNN vision models, or
  implementing plug-and-play token reduction for neuromorphic models.
  Activation: token pruning spiking transformer, uncertainty token reduction, spiking
  transformer efficiency, Dirichlet token importance, Uncert, temporal uncertainty pruning
---

# Uncertainty-Aware Token Pruning in Spiking Transformers

## Core Idea

Spiking transformers process tokens across multiple spiking steps, introducing redundancy.
Unlike ANNs where token importance is evaluated at a single forward pass, spiking transformers
build representations progressively over time. Token importance should be evaluated via
**temporal uncertainty patterns**, not just instantaneous responses.

## Key Observation

Tokens exhibit heterogeneous uncertainty trajectories over spiking steps. Tokens whose
uncertainty is low and stable across time contribute more to the final decision; tokens
with high or erratic uncertainty are less informative.

## Uncert Framework

1. **Dirichlet evidence modeling**: Model token-wise class evidence with Dirichlet(α)
   distribution per spiking step
2. **Temporal uncertainty statistics**: For each token, compute:
   - Mean uncertainty across spiking steps (E[U_t])
   - Fluctuation/variance of uncertainty across steps (Var[U_t])
3. **Uncertainty-aware importance score**: Combine mean + fluctuation into a single score
   - Lower score → more informative → keep
   - Higher score → redundant → prune
4. **Training-free**: No fine-tuning required; plug-and-play at inference time

## Why Uncertainty > Activation Magnitude

- Activation magnitude only captures instantaneous response strength
- Uncertainty captures the **quality** of evidence evolution over time
- Better distinguishes informative tokens from those with spurious high firing rates

## Results

- Favorable accuracy-efficiency tradeoffs on static and neuromorphic benchmarks
- Most consistent gains under token pruning (vs token merging)
- Empirical connection between temporal uncertainty patterns and token contribution

## When to Use

- Spiking transformer inference optimization (vision, neuromorphic tasks)
- Plug-and-play token reduction without retraining
- Energy-efficient neuromorphic vision deployment
