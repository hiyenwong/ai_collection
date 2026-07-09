---
name: stability-of-flow-models-for-graph-signals
description: 'Generating signals on graphs requires permutation-equivariant models that exhibit stability with respect to relative structural perturbations. While favorable stability properties of Graph Neural Netw. Based on arXiv:2607.07510.'
---

# Stability of Flow Models for Graph Signals

**arXiv**: 2607.07510 | **Authors**: Martin Schmidt, Gonzalo Mateos | **Utility**: 0.85

## Overview

Generating signals on graphs requires permutation-equivariant models that exhibit stability with respect to relative structural perturbations. While favorable stability properties of Graph Neural Networks (GNNs) have been well documented, it is unclear how structural errors propagate through the dynamics of continuous generative flow models that are gaining traction for graph signal generation. In this paper, we analyze continuous normalized flow models parameterized by GNNs and show that permutation equivariance is preserved for both the resulting continuous-time ordinary differential equations and their discrete numerical approximations used as graph signal samplers. Our primary contribution is to derive explicit stability bounds on the generated probability distributions, which quantify how relative graph perturbations affect the final sampled signals. Motivated by these theoretical bounds, we introduce a stability-promoting regularized flow matching strategy that actively penalizes the spatial Lipschitz constant of the vector field during model training. Experiments using synthetic smooth signals on stochastic block model graphs and real-world fMRI signals on brain connectomes demonstrate that this bound-oriented approach yields generative models that are more robust to structural noise, without sacrificing output quality.

## Key Contributions

1. Generating signals on graphs requires permutation-equivariant models that exhibit stability with respect to relative structural perturbations.
2. While favorable stability properties of Graph Neural Networks (GNNs) have been well documented, it is unclear how structural errors propagate through the dynamics of continuous generative flow models that are gaining traction for graph signal generation.
3. In this paper, we analyze continuous normalized flow models parameterized by GNNs and show that permutation equivariance is preserved for both the resulting continuous-time ordinary differential equations and their discrete numerical approximations used as graph signal samplers.
4. Our primary contribution is to derive explicit stability bounds on the generated probability distributions, which quantify how relative graph perturbations affect the final sampled signals.

## Implementation Notes

- **Keywords**: neural-network, graph-neural-network, rope-embedding
- **Categories**: eess.SP, cs.AI, cs.LG
- **Published**: 2026-07-08

## Activation Criteria

Use this skill when working on tasks involving: neural-network, graph-neural-network, rope-embedding.
