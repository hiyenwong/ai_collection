---
name: complex-valued-neuromorphic-ucn
description: "Unified Complex-valued Neuron (UCN) methodology — integrates continuous activation (magnitude) and phase-driven event generation (spike emission) through asymmetric complex-valued state space. Combines ANN accuracy with SNN energy efficiency for neuromorphic edge-AI. Training via BP+BPTT with Event-Driven Adaptive Phase Learning (EAPL) rule for efficiency."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [neuromorphic, spiking-neural-network, complex-valued, edge-AI, event-driven, phase-coding]
    related_skills: [spiking-neural-networks, neuromorphic-computing, hybrid-ann-snn]
  paper:
    arxiv: "2606.29099"
    title: "Unified Complex-valued Neural Network: A Magnitude-Phase Computational Model for Event-Driven Neuromorphic Learning"
    authors: ["Reza Ahmadvand", "Sarah Safura Sharif", "Yaser Mike Banad"]
    published: "2026-06-27"
    categories: ["cs.NE", "cs.AI"]
---

# Unified Complex-valued Neural Network (UCN)

## Overview

The Unified Complex-valued Neuron (UCN) model bridges Artificial Neural Networks (ANNs) and Spiking Neural Networks (SNNs) by encoding information in both **magnitude** (continuous signal strength) and **phase** (temporal evolution and spike emission) of complex-valued activations.

## Core Architecture

### Complex-Valued Neuron State

```
z = r · e^(iφ)

where:
  r (magnitude) = signal strength / activation value
  φ (phase) = temporal evolution / intrinsic timing
```

- **Magnitude pathway**: Encodes continuous-valued information (like ANN activations)
- **Phase pathway**: Governs temporal evolution and valued spike emission (like SNN timing)
- **Asymmetric coupling**: Phase depends on magnitude but magnitude evolves independently

### Key Innovations

1. **Unified computation**: Single neuron model handles both value encoding and timing dynamics
2. **Event-driven output**: Spikes are emitted based on phase evolution, not threshold crossing
3. **Sparse computation**: Event-driven nature preserves energy efficiency of SNNs
4. **Interpretable**: Magnitude and phase have clear computational roles

## Training Framework

### Phase 1: Full Backpropagation (BP + BPTT)

```python
# Magnitude pathway: standard backpropagation
∂L/∂r = standard ANN gradient computation

# Phase pathway: backpropagation through time
∂L/∂φ = BPTT accounting for temporal dependencies

# Joint optimization
θ* = argmin L(magnitude_path, phase_path)
```

### Phase 2: Event-Driven Adaptive Phase Learning (EAPL)

For reduced computational complexity:
- Replace full BPTT with local, event-driven phase updates
- Phase adapts only at spike emission events
- More efficient for online/neuromorphic deployment

```python
# EAPL update rule (simplified)
if spike_emitted(t):
    Δφ = -η · ∂L/∂φ · event_trigger(t)
    φ += Δφ
```

## Applications

### 1. Object Tracking
- Spatiotemporal learning with accurate position estimation
- Phase encodes temporal evolution of object trajectories
- Magnitude encodes confidence/uncertainty

### 2. Dynamical System Learning (Lorenz Attractor)
- Stable learning of chaotic dynamics
- Phase captures oscillatory/chaotic temporal structure
- Magnitude captures amplitude envelope

### 3. Neuromorphic Edge-AI
- Event-driven computation reduces energy consumption
- Deployable on neuromorphic hardware (Loihi, TrueNorth, etc.)
- Sparse activation pattern suitable for low-power devices

## Comparison with Existing Approaches

| Feature | ANN | SNN | UCN (this work) |
|---------|-----|-----|-----------------|
| Value encoding | ✓ (continuous) | ✗ (binary spikes) | ✓ (magnitude) |
| Temporal coding | ✗ | ✓ (spike timing) | ✓ (phase) |
| Energy efficiency | ✗ | ✓ | ✓ (event-driven) |
| Backpropagation | ✓ | Approximate | ✓ (BP+BPTT) |
| Interpretability | Low | Medium | High (magnitude/phase) |

## Implementation Notes

### Complex Arithmetic
- Use complex-valued tensors (PyTorch: `torch.complex64`)
- Magnitude-phase decomposition: `r = |z|`, `φ = arg(z)`
- Asymmetric coupling requires careful gradient flow

### Phase Unwrapping
- Phase is periodic: φ ∈ (-π, π]
- Use `torch.atan2` for numerical stability
- Phase gradients may need unwrapping for long sequences

### Spike Emission
- Valued spikes: magnitude of spike = |z| at emission time
- Phase-based threshold: emit when φ crosses threshold
- Alternative: phase velocity threshold (dφ/dt)

## Pitfalls

1. **Complex gradient flow** — standard optimizers may not handle complex parameters well; use complex-aware optimizers
2. **Phase wrapping** — discontinuities at ±π can cause gradient issues; use smooth phase representations
3. **EAPL approximation** — event-driven learning is less accurate than full BPTT; benchmark both
4. **Hardware deployment** — complex arithmetic may not map efficiently to all neuromorphic chips
5. **Training stability** — coupled magnitude-phase dynamics can be unstable; use gradient clipping

## Verification

- Compare against pure ANN baseline on static tasks (magnitude should match)
- Compare against SNN on temporal tasks (phase should capture timing)
- Test on chaotic systems (Lorenz) for stability
- Measure spike rate and energy on neuromorphic simulator

## Trigger Words

- complex-valued neuron
- magnitude-phase coding
- unified neural network
- event-driven phase learning
- neuromorphic edge-AI
- valued spike emission
- UCNN

## Related Skills

- spiking-neural-networks — core SNN methodology
- neuromorphic-computing — hardware deployment patterns
- hybrid-ann-snn — other ANN-SNN bridging approaches
