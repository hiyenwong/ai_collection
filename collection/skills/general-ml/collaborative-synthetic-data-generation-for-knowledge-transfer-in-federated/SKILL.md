---
name: collaborative-synthetic-data-generation-for-knowledge-transfer-in-federated
description: 'One-shot federated learning (OSFL) addresses the communication overhead of federated learning by limiting training to a single round, but doing so without sacrificing model quality is non-trivial, par. Based on arXiv:2607.07565.'
---

# Collaborative Synthetic Data Generation for Knowledge Transfer in Federated Learning

**arXiv**: 2607.07565 | **Authors**: Maximilian Andreas Hoefler, Karsten Mueller, Wojciech Samek | **Utility**: 0.85

## Overview

One-shot federated learning (OSFL) addresses the communication overhead of federated learning by limiting training to a single round, but doing so without sacrificing model quality is non-trivial, particularly when client data distributions diverge. Recent work has addressed this challenge by aggregating client knowledge on the server through the construction of transferable synthetic datasets or distillates. However, most of these methods lack formal privacy guarantees, leaving a gap in jointly achieving low communication, robustness to heterogeneity, and rigorous privacy. We propose FedKT-CSD (Federated Knowledge Transfer via Collaborative Synthetic Data), a framework inspired by neural image compression that closes this gap by leveraging publicly pretrained autoencoders as a shared latent space. Each client encodes its private data in a single forward pass, computes class-conditional latent statistics, and transmits these to the server. The server aggregates these statistics via secure aggregation, adds calibrated differential privacy noise, and decodes a synthetic dataset for training a global model and further downstream tasks. This design provides formal $(\varepsilon,δ)$-differential privacy by construction, while keeping client-side computation and communication lightweight. Despite operating under privacy constraints, FedKT-CSD is competitive with and even outperforms non-private baselines across diverse datasets and heterogeneity settings, and scales to a large number of clients. Our code is available at: https://github.com/an7123/FedKT-CSD

## Key Contributions

1. One-shot federated learning (OSFL) addresses the communication overhead of federated learning by limiting training to a single round, but doing so without sacrificing model quality is non-trivial, particularly when client data distributions diverge.
2. Recent work has addressed this challenge by aggregating client knowledge on the server through the construction of transferable synthetic datasets or distillates.
3. However, most of these methods lack formal privacy guarantees, leaving a gap in jointly achieving low communication, robustness to heterogeneity, and rigorous privacy.
4. We propose FedKT-CSD (Federated Knowledge Transfer via Collaborative Synthetic Data), a framework inspired by neural image compression that closes this gap by leveraging publicly pretrained autoencoders as a shared latent space.

## Implementation Notes

- **Keywords**: federated-learning, ecg, privacy
- **Categories**: cs.LG, cs.AI
- **Published**: 2026-07-08

## Activation Criteria

Use this skill when working on tasks involving: federated-learning, ecg, privacy.
