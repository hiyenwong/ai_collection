---
name: visual-place-recognition-rate-encoded-snn-stdp
description: "Skill for understanding and implementing the discrete tensor-native STDP-based SNN visual place recognition pipeline from arXiv:2607.13584v1. Use when working with spiking neural networks for visual place recognition, loop closure in SLAM, or neuromorphic computing applications."
---

# Visual Place Recognition Using Rate-Encoded Spiking Neural Networks with Discrete STDP Learning

## Overview

This skill provides knowledge about the paper "Visual Place Recognition Using Rate-Encoded Spiking Neural Networks with Discrete STDP Learning" (arXiv:2607.13584v1). 
The paper presents a discrete, tensor-native implementation of an STDP-based Spiking Neural Network (SNN) for Visual Place Recognition (VPR) using PyTorch and snnTorch.
It investigates three key implementation decisions that affect Recall at 100% Precision (R@100P):
  1. Neuron assignment via a closed-form deterministic tensor pipeline (instead of argmax).
  2. Resetting the network state after each query.
  3. Using a velocity-compensated sliding window aggregation over multiple frames.

The skill enables users to understand these contributions and apply them in their own SNN-based VPR systems.

## Key Contributions

### 1. Deterministic Neuron Assignment
- The authors propose a closed-form, deterministic tensor pipeline for assigning neurons to clusters, replacing the standard argmax procedure.
- This method provides significantly higher R@100P, though part of the gain is due to implementation differences compared to prior continuous-time models.

### 2. State Reset After Each Query
- Resetting the SNN state after each query presentation improves R@100P regardless of the neuron assignment method.
- This addresses the issue of temporal leakage in continuous-time ODE solvers (like Brian2) that can affect state isolation between independent queries.

### 3. Velocity-Compensated Sliding Window Aggregation
- Aggregating predictions over a sliding window of k consecutive frames, compensated for velocity, achieves perfect R@100P (100.00%) at k=5 for constant-velocity traversal.
- This introduces only an additional 0.20 ms latency.

## Methodology

The implementation uses:
- PyTorch and snnTorch for a discrete, tensor-native simulation of the SNN.
- STDP for unsupervised learning.
- Evaluation on the Nordland dataset (100 places) with 15 independently-trained networks.

## When to Use This Skill

Use this skill when:
- Designing or implementing a spiking neural network for visual place recognition or loop closure in SLAM.
- Seeking to improve the retrieval precision (R@100P) of an existing SNN-VPR system.
- Investigating the impact of implementation choices (neuron assignment, state reset, temporal aggregation) on SNN performance.
- Working with neuromorphic hardware deployment where efficient on-device inference is required.

## How to Apply

To apply the insights from this paper:
1. Replace argmax neuron assignment with the proposed deterministic tensor pipeline for clustering neuron responses.
2. Ensure the network state is reset after processing each query (or frame) to avoid temporal correlations.
3. Implement a velocity-compensated sliding window that aggregates predictions over k frames (e.g., k=5) to boost precision under motion.

## References

- arXiv:2607.13584v1 [cs.NE] 15 Jul 2026
- The paper is available at: https://arxiv.org/abs/2607.13584v1

## Resources

This skill includes example resource directories (scripts/, references/, assets/) that can be used to store relevant code, documentation, and assets.
For this skill, you might want to:
- Add a script implementing the deterministic neuron assignment in `scripts/`.
- Add a copy of the paper or notes in `references/`.
- Add any relevant configuration or template files in `assets/`.