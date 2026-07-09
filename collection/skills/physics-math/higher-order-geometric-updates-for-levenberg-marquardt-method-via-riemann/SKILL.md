---
name: higher-order-geometric-updates-for-levenberg-marquardt-method-via-riemann
description: 'Nonlinear least-squares optimization is central to regression, physics-informed neural networks, and other machine-learning tasks. Such problems have a natural geometric interpretation, model predicti. Based on arXiv:2607.07623.'
---

# Higher-Order Geometric Updates for Levenberg-Marquardt Method via Riemann Normal Coordinates

**arXiv**: 2607.07623 | **Authors**: Jianing Liu, Dong H. Zhang | **Utility**: 0.85

## Overview

Nonlinear least-squares optimization is central to regression, physics-informed neural networks, and other machine-learning tasks. Such problems have a natural geometric interpretation, model predictions form a manifold in data space, while the chosen parameterization can introduce parameter-effects curvature that becomes a dominant source of nonlinearity. This exposes a limitation of the Levenberg-Marquardt (LM) method, its tangent-space step is applied as a straight update in parameter coordinates. Geodesic acceleration gives a second-order correction, but its removal of parameter-effect curvature is exact only in the infinitesimal-step limit. We propose a Riemann-normal-coordinate Levenberg-Marquardt method (RNC-LM) to improve this consistency for finite optimization steps. By reformulating the geodesic equation, RNC-LM extends geodesic acceleration to arbitrary-order corrections and constructs finite-step updates with progressively higher reparameterization consistency. A line search along the resulting RNC curve controls the traveled distance while keeping the cost close to standard LM. The method eliminates the tangential component of residual acceleration order by order in a moving tangent frame, making the actual objective reduction more consistent with the linear model prediction of LM. On classical nonlinear least-squares benchmarks, RNC-LM improves convergence and robustness in curved valleys and rank-deficient problems. On a reaction-diffusion PINN failure-mode benchmark, it reduces the relative L2 error to the order of 1e-3 and recovers a physically meaningful solution. On a large-scale machine-learning potential-energy-surface fitting task, it achieves a 34-fold speedup over standard LM.

## Key Contributions

1. Nonlinear least-squares optimization is central to regression, physics-informed neural networks, and other machine-learning tasks.
2. Such problems have a natural geometric interpretation, model predictions form a manifold in data space, while the chosen parameterization can introduce parameter-effects curvature that becomes a dominant source of nonlinearity.
3. This exposes a limitation of the Levenberg-Marquardt (LM) method, its tangent-space step is applied as a straight update in parameter coordinates.
4. Geodesic acceleration gives a second-order correction, but its removal of parameter-effect curvature is exact only in the infinitesimal-step limit.

## Implementation Notes

- **Keywords**: neural-network
- **Categories**: cs.LG, math.NA, physics.chem-ph, physics.comp-ph, physics.data-an
- **Published**: 2026-07-08

## Activation Criteria

Use this skill when working on tasks involving: neural-network.
