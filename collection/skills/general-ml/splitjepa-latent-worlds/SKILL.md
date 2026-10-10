---
name: splitjepa-latent-worlds
description: Use when learning invariant and variant latent world representations without pixel reconstruction. Factorizes state into shared and varying components.
tags: [world-models, latent-representation, invariance, JEPA, factorization, self-supervised-learning]
---

# SplitJEPA: Invariant/Variant Latent Worlds

## Paper Metadata

- **arXiv ID**: 2610.12349
- **Authors**: arXiv authors
- **Categories**: cs.LG, cs.CV
- **Utility Score**: 0.86
- **Date**: 2026-10
- **Link**: https://arxiv.org/abs/2610.12349

## Key Contributions

- Learns invariant and variant latent worlds without reconstruction — avoids the inductive bias of pixel-level decoding
- Organizes state into shared (invariant) and varying (variant) factors for dynamical world understanding
- Extends JEPA (Joint Embedding Predictive Architecture) with explicit factorization of latent dynamics
- Enables compositional world models where invariant structure transfers across varying contexts

## Core Methodology

SplitJEPA builds on the Joint Embedding Predictive Architecture (JEPA) paradigm, which predicts latent representations rather than pixel-level reconstructions. The key extension is factorizing the latent state into two components: an invariant part that captures structure shared across different observations/contexts, and a variant part that captures what changes.

The method trains two parallel predictive pathways — one for invariant factors (e.g., object identity, physical laws) and one for variant factors (e.g., viewpoint, lighting, configuration). By separating these in latent space, the model learns disentangled dynamics that generalize better: invariant predictions transfer across contexts, while variant predictions adapt to specific conditions.

Crucially, this is done without reconstruction loss. The model never decodes back to pixels, avoiding the well-known problems of reconstruction-based methods (blur, mode collapse, inductive bias toward low-frequency content). Instead, prediction happens entirely in latent space, with the factorization providing the structural inductive bias.

## Relevance to general-ml

Advances world model learning for RL and planning: factorized latent dynamics enable better generalization and compositional reasoning about how the world changes.

## Activation

world-models, latent-representation, invariance, JEPA, factorization, self-supervised-learning
