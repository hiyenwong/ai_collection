---
name: neural-operator-enabled-topology-informed-evolutionary-strategy-for-pde
description: 'The inverse design of physical systems governed by partial differential equations is computationally demanding due to the high dimensionality and non-convexity of design spaces. Generative models for. Based on arXiv:2607.07682.'
---

# Neural Operator-enabled Topology-informed Evolutionary Strategy for PDE-Constrained Optimization

**arXiv**: 2607.07682 | **Authors**: Xiangming Huang, Guannan Zhang, Lu Lu, Raphaël Pestourie | **Utility**: 0.85

## Overview

The inverse design of physical systems governed by partial differential equations is computationally demanding due to the high dimensionality and non-convexity of design spaces. Generative models for inverse design often lack robustness and transferability, whereas evolutionary strategies are robust but struggle in high-dimensional spaces. This paper introduces a Neural Operator-enabled Topology-informed Evolutionary Strategy (NOTES) that integrates dimensionality reduction, representation learning, and evolutionary optimization for efficient and transferable inverse design. NOTES couples a DeepONet-based neural operator with the Covariance Matrix Adaptation Evolution Strategy (CMA-ES) to perform global optimization in a compact latent space that encodes topology-aware priors while discovering high-performance designs for unseen operating conditions. Applied to nanophotonic beam-deflector inverse design governed by Maxwell's equations, NOTES reduces the design dimensionality from 256 to 25 and consistently achieves over 95 percent efficiency, outperforming CMA-ES, topology optimization, and other baselines. Applied to structural optimization, NOTES discovers designs that achieve compliance down to 246. By decoupling topology learning of a DeepONet from the governing physics in a PDE solver, NOTES provides a flexible and transferable framework for the inverse design of physical systems.

## Key Contributions

1. The inverse design of physical systems governed by partial differential equations is computationally demanding due to the high dimensionality and non-convexity of design spaces.
2. Generative models for inverse design often lack robustness and transferability, whereas evolutionary strategies are robust but struggle in high-dimensional spaces.
3. This paper introduces a Neural Operator-enabled Topology-informed Evolutionary Strategy (NOTES) that integrates dimensionality reduction, representation learning, and evolutionary optimization for efficient and transferable inverse design.
4. NOTES couples a DeepONet-based neural operator with the Covariance Matrix Adaptation Evolution Strategy (CMA-ES) to perform global optimization in a compact latent space that encodes topology-aware priors while discovering high-performance designs for unseen operating conditions.

## Implementation Notes

- **Keywords**: pde-optimization
- **Categories**: cs.LG
- **Published**: 2026-07-08

## Activation Criteria

Use this skill when working on tasks involving: pde-optimization.
