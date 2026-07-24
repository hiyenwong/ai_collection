---
name: scalable-training-continuous-time-snn-dstd
description: "Scalable Training of Continuous-Time Spiking Neural Networks with Differentiable Spike-Time Discretization (DSTD) — reduces memory and training time for deep SNNs via fixed-time discretization and synfire-chain-inspired regularization"
metadata:
  arxiv_id: "2607.14672"
  authors: "Yusuke Sakemi, Tomoya Takeuchi, Takeo Hosomi, Kazuyuki Aihara"
  published: "2026-07-16"
  categories: "cs.LG"
---

## Context

Continuous-time spiking neural networks (SNNs) offer an event-driven framework for temporal computation, bridging neuroscience and neuromorphic hardware. However, training deep continuous-time SNNs is hindered by the memory demands of exact spike-time computation, which requires evaluating and storing candidate firing times over intervals determined by presynaptic spike ordering.

## Core Methodology

We introduce a memory-efficient training framework based on differentiable spike-time discretization (DSTD) for leaky integrate-and-fire (LIF) neurons with general membrane and synaptic time constants. DSTD maps irregular presynaptic spikes onto differentiable weighted events at fixed time points, replacing the input-dependent candidate dimension with M fixed time intervals while accurately approximating continuous-time membrane-potential dynamics. This reduces candidate-related activation memory from O(N_out N_in) to O(N_out M) for time-to-first-spike (TTFS) coding, where N_in and N_out are the numbers of presynaptic and postsynaptic neurons. Additionally, we introduce synfire-chain-inspired temporal regularization that organizes layer-wise firing windows, mitigates dead-neuron failures, and enables pipeline-like processing.

## Key Contributions

- Proposes DSTD, a differentiable spike-time discretization method that drastically reduces memory footprint for training continuous-time SNNs.
- Demonstrates up to 100-fold reduction in peak memory consumption and up to 20-fold reduction in training time compared to exact spike-time computation in dense LIF layers.
- Enables training of 9-layer convolutional SNNs on CIFAR-10 and 20-layer convolutional SNNs on Fashion-MNIST on a single GPU.
- Combines DSTD with synfire-chain-inspired temporal regularization to organize layer-wise firing windows and prevent dead-neuron failures.

## Implementation Steps

1. Define the LIF neuron model with membrane and synaptic time constants.
2. Choose a fixed time grid with M intervals covering the simulation window.
3. For each presynaptic spike, compute its contribution to postsynaptic potential via differentiable kernel (e.g., exponential or alpha function) evaluated at the fixed grid points.
4. Accumulate weighted contributions across presynaptic neurons to obtain postsynaptic membrane potential at each time step.
5. Apply spike threshold to generate output spikes (e.g., using surrogate gradient for differentiability).
6. Incorporate synfire-chain-inspired temporal regularization: add a penalty term that encourages structured firing windows across layers, reducing variability and dead-neuron occurrences.
7. Train the network using gradient-based optimization (e.g., Adam) on the discretized dynamics.
8. Validate on benchmark datasets such as CIFAR-10 and Fashion-MNIST using convolutional SNN architectures.

## Pitfalls

- The choice of M (number of fixed time intervals) affects accuracy-resolution trade-off; too coarse may lose temporal precision.
- Surrogate gradient selection is crucial for stable training; inappropriate choice can lead to vanishing or exploding gradients.
- Temporal regularization strength must be tuned to balance fidelity and regularization benefits.
- The method assumes LIF dynamics; extensions to more complex neuron models may require adjusted discretization kernels.
- Hardware implementation may need custom kernels to fully exploit memory savings.

## Verification

- Compare memory consumption and training time against exact spike-time computation baselines.
- Report classification accuracy on CIFAR-10 and Fashion-MNIST for various layer depths.
- Ablation study: assess impact of DSTD alone vs. DSTD plus temporal regularization.
- Test robustness across different time constants and coding schemes (e.g., rank-order, phase).
- Ensure gradient flow and stability via loss curve inspection and gradient norm monitoring.

## Activation

continuous-time spiking neural networks, CSNN, differentiable spike-time discretization, DSTD, synfire-chain regularization, neuromorphic hardware, event-driven training, 2607.14672