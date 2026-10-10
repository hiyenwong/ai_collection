---
name: lewam-jepa-world-action
description: "Bidirectional transformer for forward, backward, inverse dynamics and policy prediction on decoder-free JEPA latent, using diffusion-steering-based model predictive control."
tags: [jepa, world-models, model-predictive-control, diffusion-steering, latent-space, vision-generative]
---

# LeWAM: JEPA World Action Model

Derived from arXiv:2610.12407 — LeWAM: JEPA World Action Model

## Paper Metadata

- **arXiv ID**: 2610.12407
- **Category**: vision-generative
- **Utility Score**: 0.87
- **Date**: October 2026
- **Link**: https://arxiv.org/abs/2610.12407

## Key Contributions

- Introduces bidirectional transformer architecture for joint world and action modeling in JEPA latent space
- Demonstrates unified framework for forward dynamics, backward dynamics, inverse dynamics, and policy prediction
- Eliminates need for decoder by operating directly on JEPA latent representations
- Proposes diffusion-steering-based model predictive control (MPC) for planning in latent space

## Core Methodology

LeWAM addresses a key limitation of Joint Embedding Predictive Architecture (JEPA): while JEPA learns rich latent representations of visual worlds, it lacks explicit action modeling. The framework extends JEPA with a bidirectional transformer that operates directly in latent space, enabling prediction of future states (forward dynamics), inference of past states (backward dynamics), recovery of actions from state transitions (inverse dynamics), and direct policy learning.

The bidirectional architecture is crucial: it allows the model to reason both forward in time (prediction) and backward in time (inference), creating a unified world model that supports multiple reasoning modes. By operating on decoder-free JEPA latents, the approach avoids the information loss and computational overhead of decoding to pixel space.

For planning, LeWAM introduces diffusion-steering-based MPC. Rather than sampling actions randomly or using gradient-based optimization, the method steers a diffusion process toward high-reward trajectories in latent space. This provides more efficient exploration of the action space and better sample efficiency compared to traditional MPC approaches.

## Relevance to Category

LeWAM represents a significant advance in vision-generative world models. By unifying forward/backward/inverse dynamics and policy learning in a single latent-space framework, it provides a more complete and efficient approach to visual world modeling. The diffusion-steering MPC is particularly relevant for robotics and autonomous systems that must plan in complex visual environments.

## Activation

lewam-jepa-world-action, 2610.12407, jepa, world models, bidirectional transformer, diffusion steering, latent planning

## References

- arXiv: https://arxiv.org/abs/2610.12407
