---
name: an-optimal-control-approach-for-neural-network-architecture-adaptation-with-a
description: 'This work presents a novel approach for adapting neural network architecture along the depth based on a posteriori error estimation. By formulating neural network training as a continuous-time optimal. Based on arXiv:2607.07637.'
---

# An optimal control approach for neural network architecture adaptation with a posteriori error estimation

**arXiv**: 2607.07637 | **Authors**: C G Krishnanunni, Thomas Scott, Tan Bui-Thanh | **Utility**: 0.85

## Overview

This work presents a novel approach for adapting neural network architecture along the depth based on a posteriori error estimation. By formulating neural network training as a continuous-time optimal control problem, we derive rigorous error estimates that quantify how approximation error distributes across network layers. This error decomposition enables a principled depth adaptation strategy: new layers are inserted at locations of maximum estimated error, allowing the network to efficiently capture complex, nonlinear variations in the underlying problem. Our framework introduces a novel network architecture that treats weights and biases as piecewise linear functions varying across layers, with the error estimator bounding the discrepancy between this discrete representation and the true continuous optimal control solution. The approach leverages dual weighted residual methodology from finite element analysis to derive computable upper bounds on the functional error. A key theoretical contribution is the derivation of explicit error bounds that decompose the total approximation error into interval-wise contributions, providing a rigorous basis for targeted architecture refinement. We demonstrate the effectiveness of our method on scientific datasets, including learning the observable-to-parameter map for the Navier-Stokes equation. Numerical results reveal that our approach consistently outperforms existing architecture adaptation methods in terms of generalization performance.

## Key Contributions

1. This work presents a novel approach for adapting neural network architecture along the depth based on a posteriori error estimation.
2. By formulating neural network training as a continuous-time optimal control problem, we derive rigorous error estimates that quantify how approximation error distributes across network layers.
3. This error decomposition enables a principled depth adaptation strategy: new layers are inserted at locations of maximum estimated error, allowing the network to efficiently capture complex, nonlinear variations in the underlying problem.
4. Our framework introduces a novel network architecture that treats weights and biases as piecewise linear functions varying across layers, with the error estimator bounding the discrepancy between this discrete representation and the true continuous optimal control solution.

## Implementation Notes

- **Keywords**: control-systems, neural-network
- **Categories**: cs.LG, math.NA, math.OC
- **Published**: 2026-07-08

## Activation Criteria

Use this skill when working on tasks involving: control-systems, neural-network.
