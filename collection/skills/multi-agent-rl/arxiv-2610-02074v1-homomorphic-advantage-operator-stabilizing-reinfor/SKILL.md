---
name: arxiv-2610-02074v1-homomorphic-advantage-operator-stabilizing-reinfor
description: "arXiv paper: Homomorphic Advantage Operator: Stabilizing Reinforcement Learning Under Fully Homomorphic Encryption Constraints"
tags: [arxiv, cs.AI, research]
created: 2026-10-04
utility: 1.0
---

# Homomorphic Advantage Operator: Stabilizing Reinforcement Learning Under Fully Homomorphic Encryption Constraints

**arXiv ID:** 2610.02074v1
**Authors:** Abid Mohamed Nadhir, Ahmad Al Hanbali, Beggas Mounir
**Published:** 2026-10-01
**Category:** cs.AI
**Utility Score:** 1.0
**URL:** https://arxiv.org/abs/2610.02074v1

## Abstract

Privacy-preserving machine learning presents significant deployment challenges on the cloud for intelligent systems with confidential data. Fully Homomorphic Encryption (FHE) offers a compelling solution for secure computation, preserving data confidentiality of cloud computations. However, applying FHE to reinforcement learning (RL) requires replacing non-linear operations with polynomial approximations, which diverge catastrophically due to a unique recursive error phenomenon known as the Bellman drift. This article introduces the Homomorphic Advantage Operator (HAO), a stabilization framework designed to prevent polynomial approximation divergence in FHE-based deep RL. HAO adapts the zero-mean centering projection from advantage-based value estimation directly to temporal-difference (TD) targets. This linear projection annihilates the uniform state-value baseline that drives the Bellman drift, maintaining per-state action rankings while requiring zero additional non-linear multiplicative depth and avoiding expensive ciphertext bootstrapping. The proposed HAO framework was evaluated using a three-tier experimental methodology, including a tabular Markov Decision Process (MDP), an encrypted CartPole environment using real CKKS cryptographic operations, and a 20-node logistics routing benchmark with dense continuous features. The results demonstrate that the proposed HAO strictly bounds network pre-activations within the safe polynomial approximation domain. The proposed HAO RL agents achieved 0% boundary breaches across all random seeds used, whereas regularization alone (L2 weight decay and gradient clipping) breached the bound on 3 of 5 seeds and the unstabilized baseline did so in 83.8% of episodes. Finally, HAO agents improve optimal policy accuracy by 18.0 percentage points in tabular domains and remain stable when DP-SGD-style Gaussian noise is added to the clipped gradients.

## Key Contributions

- Novel research in cs.AI
- Published on arXiv: 2026-10-01

## Related Work

See arXiv for citations and references.
