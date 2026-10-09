---
name: trace-temporal-gradient-inversion
version: v1.0.0
last_updated: 2026-09-26
description: "TRACE methodology — temporal gradient-inversion attack on embodied RL that autoregressively reconstructs private observation-action trajectories from per-step policy gradients, exploiting cross-time gradient correlation and closed-form action recovery. Use when: (1) auditing privacy leakage of distributed/federated RL gradient streams, (2) designing sequence-aware privacy defenses, (3) threat-modeling gradient sharing in embodied agents. Keywords: gradient inversion, embodied RL, privacy attack, trajectory reconstruction, federated learning security."
arxiv_id: "2609.30258"
authors: "Sudip Bhujel, Shanghao Shi, Ruiquan Huang, Ning Zhang, Yang Xiao"
tags: [gradient-inversion, privacy, embodied-rl, federated-learning, security-audit]
---

# TRACE: Temporal Gradient Inversion for Embodied RL

From arXiv:2609.30258 (2026-09-24).

## Problem

Distributed embodied RL keeps raw sensor data on-device and uploads only policy gradients — presumed private. But **temporal structure amplifies leakage**: gradients from consecutive time steps share the same scene and correlate strongly. Single-frame gradient-inversion attacks ignore this and leave most of the signal unused.

## Method: Two Structural Signals

1. **Cross-time correlation between successive embodied gradients**, formalized via a **conditional mutual-information bound** — consecutive-step gradients jointly constrain the shared underlying observation far more than each gradient alone
2. **Closed-form action recovery from policy-head gradient structure** — provably exact when standard entropy regularization is sufficiently small (solve for the action analytically instead of optimizing)

**Amortized autoregressive reconstruction**: an amortized inverter reconstructs each frame conditioned on previously reconstructed frames (18.8 dB PSNR, near-perfect action recovery, 3–4.5 ms/frame — orders of magnitude faster than optimization-based attacks). Works across recurrent, residual, and compact transformer victims, multimodal inputs, larger discrete action spaces.

## Defense Implication

Defending per-gradient (noise, clipping) is insufficient against temporal attacks: **sequence-aware privacy mechanisms are required** (temporal DP accounting, decorrelation across steps, batching-aware noise).

## Reusable Pattern

**Audit shared-state correlation in "private" update streams.** Whenever a distributed learning protocol sends sequential updates computed from overlapping world state (RL rollouts, continual learning, sensor fusion), the mutual information *between consecutive updates* is the attacker's leverage. The audit recipe: (1) formalize cross-update MI bound, (2) look for closed-form recovery of low-dimensional components (actions/labels) from gradient algebra, (3) build an amortized autoregressive inverter and measure PSNR/action-recovery. Conversely, defense must break temporal correlation, not just mask individual updates.

## Resources

- Paper: https://arxiv.org/abs/2609.30258
