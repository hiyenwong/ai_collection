---
name: singularity-tensor-network-pricing
description: "Tensor network surrogate model for efficient option pricing using singularity-aware tensor decomposition. Replaces expensive Monte Carlo/PDE solvers with compressed tensor representations for large-scale portfolio revaluation. Use when: pricing complex derivatives at scale, building tensor network surrogates for financial PDEs, or accelerating portfolio revaluation with compressed mathematical representations."
---

# Singularity Tensor Network for Option Pricing (STN-GPR)

## Description

Uses tensor network decomposition to create efficient surrogate models for option pricing, targeting large-scale portfolio revaluation. Handles singularities (sharp payoff features) through adaptive tensor compression, replacing costly Monte Carlo or PDE solvers.

## Core Methodology

### Tensor Network Representation

Financial pricing problems are represented as high-dimensional tensors:
- **Dimensions**: Underlying assets × time steps × scenario parameters
- **Problem**: Full tensor exponential in dimensions (curse of dimensionality)
- **Solution**: Tensor Train (TT) or Tensor Ring decomposition for compression

### Singularity Handling

Option payoffs have discontinuities (e.g., at strike prices):
1. **Detect singularities** via gradient analysis on payoff surface
2. **Adaptive refinement**: Increase tensor bond dimension near singularities
3. **Smooth approximation**: Use mollified payoff functions during compression
4. **Error control**: Track compression error bounds

### Gaussian Process Regression (GPR) Integration

- GPR provides uncertainty quantification on tensor surrogate predictions
- Combines TT compression with probabilistic error bounds
- Enables adaptive sampling: query expensive solver where surrogate uncertainty is high

### Algorithm Pipeline

```
1. Generate training data: sparse samples from Monte Carlo/PDE solver
2. Build tensor network surrogate from samples
3. Identify singularity regions → refine tensor locally
4. Train GPR on residual errors
5. Price = TT_prediction + GPR_correction
6. Validate against held-out samples
```

## Key Advantages

1. **Speed**: 100-1000x faster than Monte Carlo for portfolio-level revaluation
2. **Dimensionality**: Handles 10+ underlying assets (impossible for grid methods)
3. **Accuracy**: Controlled error bounds via GPR uncertainty
4. **Compression**: Bond dimension r~10-50 captures most pricing information

## Usage Patterns

### Pattern 1: Portfolio Revaluation at Scale
For revaluing thousands of options daily:
1. Build TT surrogate for each option class
2. Batch-evaluate all positions via tensor contraction
3. Use GPR uncertainty to flag positions needing full repricing

### Pattern 2: Exotic Option Pricing
For path-dependent or multi-asset options:
1. Encode path integral as tensor network
2. Compress via TT-SVD with singularity adaptation
3. Evaluate at any parameter point in O(d·r³) time

### Pattern 3: Greeks Computation
For sensitivity analysis (Delta, Gamma, Vega):
1. Differentiate tensor network analytically
2. Automatic derivative propagation through TT format
3. No finite-difference noise

## Implementation Notes

- **Bond dimension**: Start with r=10, increase until error threshold met
- **Tensor format**: TT-Train for 1D chains, Tensor Ring for circular dependencies
- **GPR kernel**: Matérn 5/2 works well for pricing surfaces
- **Validation**: Always check against analytical solutions (Black-Scholes) first

## Activation Keywords
- tensor network option pricing
- STN-GPR pricing
- tensor train surrogate finance
- singularity-aware tensor pricing
- portfolio revaluation tensor network
- 张量网络期权定价
- tensor network Greeks computation
- compressed option pricing
