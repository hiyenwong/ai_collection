---
name: the-importance-of-tensor-handling-and
description: "The importance of tensor handling and implementati..."
tags: [cs.LG, physics.comp-ph]
source: arxiv
arxiv_id: 2610.22157v1
utility: 0.9
published: 2026-10-15
---

# The importance of tensor handling and implementation of physics-informed DeepONets

**Authors:** Nahum Banks, Gustavo A. M. de Almeida, Sergio Maldonado
**Published:** 2026-10-15
**arXiv:** [2610.22157v1](https://arxiv.org/abs/2610.22157v1)
**Categories:** cs.LG, physics.comp-ph
**Utility Score:** 0.9

## Abstract

Physics-informed neural networks (PINNs) reduce or eliminate the need for large labelled datasets by enforcing governing equations during training. Physics-informed Deep Operator Networks (PI-DeepONets) extend this approach to learning solution operators, enabling rapid prediction across families of problems. Despite these advantages, we show that their application to higher-dimensional problems remains limited by the computational cost of training. To address this issue, we propose a modified PI-DeepONet architecture that reduces this cost by removing redundancy in how the Branch network processes input functions across collocation points. The proposed formulation is mathematically equivalent to the original architecture but reduces input tensor sizes and the number of Branch network evaluations. We analyse the computational complexity of both architectures and derive theoretical scaling laws for training time with respect to the number of collocation points and input functions. The proposed architecture is evaluated on 1D, 2D, and 3D linear advection problems. In all cases, it achieves comparable predictive accuracy to the original PI-DeepONet while consistently reducing training time. In 2D experiments, a maximum speed-up of $3.75\times$ is observed, with empirical training-time scaling agreeing with the predicted linear dependence on collocation points and input functions. Furthermore, training a 3D model on an NVIDIA A100 GPU is only feasible using the proposed architect

## Key Contributions

- Novel research in cs.LG, physics.comp-ph
- Published 2026-10-15

## Activation

importance, tensor, handling, implementation, physicsinformed, deeponets
