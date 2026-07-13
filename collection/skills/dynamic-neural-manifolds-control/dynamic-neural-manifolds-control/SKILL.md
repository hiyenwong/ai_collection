---
name: dynamic-neural-manifolds-control
description: "Dynamic neural manifolds methodology for flexible closed-loop control on neuromorphic hardware. From arXiv:2607.07373 (von Seeler et al., Jul 2026)."
tags: ["neuromorphic", "closed-loop-control", "neural-manifolds", "neural-dynamics", "brain-inspired-control"]
---

## Overview

This skill encodes the methodology from **"Dynamic neural manifolds for flexible closed-loop control on neuromorphic hardware"** (arXiv:2607.07373, Jul 2026).

**Core idea**: Use dynamic neural manifolds — low-dimensional subspaces of neural population activity — as the computational substrate for flexible closed-loop control on neuromorphic hardware.

## Key Concepts

### Neural Manifolds

- Neural population activity evolves on low-dimensional manifolds within high-dimensional state space
- These manifolds encode control-relevant features compactly
- Manifold geometry determines controllability and flexibility

### Flexible Closed-Loop Control

- Single network can switch between control tasks by reconfiguring manifold dynamics
- No retraining needed — control flexibility emerges from network architecture
- Compatible with asynchronous, event-driven neuromorphic execution

## Implementation Patterns

### Manifold Discovery

- Analyze recurrent neural activity to identify low-dimensional subspaces
- Use dimensionality reduction (PCA, factor analysis) on population activity
- Manifold curvature and topology determine available control actions

### Control Mapping

- Map sensory inputs → manifold coordinates → motor outputs
- Feedback loops close on the manifold, not individual neurons
- Enables robust control despite neuron-level variability

## Use Cases

- Neuromorphic robot control with task switching
- Energy-efficient embedded control systems
- Brain-machine interface decoding
- Adaptive control on resource-constrained hardware

## Pitfalls

### Manifold Stability
**Critical**: Dynamic manifolds must remain stable enough for control while being flexible enough for task switching. The balance depends on the timescale separation between fast control dynamics and slow manifold adaptation.

### Hardware Compatibility
**Consideration**: Implementation on neuromorphic hardware requires mapping continuous manifold dynamics to spiking representations. Quantization and timing precision affect manifold geometry.

## Activation

dynamic neural manifold, neuromorphic control, closed-loop spiking control, neural population dynamics, brain-inspired control, arxiv 2607.07373
