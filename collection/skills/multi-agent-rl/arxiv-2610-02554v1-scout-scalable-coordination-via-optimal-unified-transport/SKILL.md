---
name: arxiv-2610-02554v1-scout-scalable-coordination-via-optimal-unified-transport
description: "SCOUT: First offline MARL framework combining flow-matching behavioral prior with decomposed value function for test-time action refinement (NeurIPS 2026)"
tags: [arxiv, multi-agent-rl, offline-rl, flow-matching, value-decomposition, neurips-2026]
arxiv_id: "2610.02554v1"
utility: 0.95
date_added: "2026-10-05"
---

# SCOUT: Scalable Coordination via Optimal Unified Transport

**arXiv:** 2610.02554v1 | **Utility:** 0.95 | **Date:** 2026-10-05 | **Venue:** NeurIPS 2026

## Abstract

Offline MARL faces a persistent trade-off between expressive generative policies (which can represent multi-modal coordination) and value-optimized policies (which exploit Q-functions but collapse multi-modal distributions). SCOUT is the first offline MARL framework to combine a generative foundation model with a learned value function through test-time action refinement via Stein variational gradient descent.

## Key Contributions

- **Policy-free value maximization**: Separates behavioral modeling from value improvement, replacing training-time regularization with test-time refinement budget
- **Decomposed value gradient transport**: Under IGM principle, enables fully decentralized test-time refinement with bounded approximation gap
- **Single-term KL bound**: Proves KL bound on joint soft-value gap that vanishes as transport converges, with irreducible residual proportional to IGM violation
- **Empirical SOTA**: Best average performance across discrete and continuous offline MARL benchmarks; improvements in ALL offline-to-online configurations

## Methods

Two decoupled components trained offline:
1. **Flow-matching behavioral prior**: Captures multi-modal coordination from demonstration data
2. **Decomposed value function**: Learned separately, provides value gradients

At test-time: behavioral samples are transported toward high-value regions via Stein variational gradient descent (SVGD). Number of transport steps controls adaptive test-time scaling.

## Relevance

Fundamentally changes the offline MARL paradigm by decoupling exploration (behavioral prior) from exploitation (value refinement). The test-time scaling knob is practically valuable — no retraining needed to adjust coordination quality. The IGM-theoretic guarantees provide principled foundations for decentralized refinement.
