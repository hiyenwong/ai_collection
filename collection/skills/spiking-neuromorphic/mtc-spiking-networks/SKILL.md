---
name: mtc-spiking-networks
description: "Multi-Timescale Conductance Spiking Networks (MTC-SN): A sparse, gradient-trainable SNN framework with rich firing dynamics for enhanced temporal processing. Uses fast/slow/ultra-slow conductances to shape I-V curves, enabling direct BPTT without surrogate gradients. Activation: multi-timescale conductance, MTC-SN, conductance-based SNN, gradient-trainable spiking, temporal regression SNN, neuromorphic regression."
category: neuroscience
---

# MTC-SN: Multi-Timescale Conductance Spiking Networks

**arXiv**: 2605.11835v1 (2026-05-12)
**Authors**: Alex Fulleda-Garcia, Saray Soldado-Magraner, Josep Maria Margarit-Taulé
**Affiliation**: IMB-CNM CSIC (Spain), UCLA (USA)
**Keywords**: Spiking Neural Networks, Conductance-Based Neuron Models, Multi-Timescale Dynamics, Temporal Regression, Neuromorphic Computing

## Overview

MTC-SN (Multi-Timescale Conductance Spiking Networks) is a gradient-trainable spiking neural network framework that addresses the fundamental trade-off between biological plausibility, trainability, and computational efficiency in SNNs. The key innovation is using **multi-timescale conductances** (fast, slow, ultra-slow) to shape the current-voltage (I-V) curve, enabling rich firing dynamics while maintaining differentiability for direct backpropagation through time.

### Core Innovation

Unlike traditional SNNs that rely on surrogate gradients (approximate gradients for non-differentiable spike functions), MTC-SN derives a **discrete-time formulation of differentiable conductance-based dynamics**, enabling **exact BPTT** without surrogate-gradient approximations.

## Technical Details

### Problem Addressed

Current SNN limitations:
- **Simple neuron models** (LIF) trade dynamical richness for trainability
- **Surrogate gradients** are approximations that may not capture true gradient information
- **Regression tasks** suffer from approximation error, noise, and spike discretization
- **Limited control** over spiking diversity and sparsity

### MTC-SN Architecture

1. **Multi-Timescale Conductances**:
   - **Fast conductance**: Rapid response to input changes
   - **Slow conductance**: Medium-term adaptation
   - **Ultra-slow conductance**: Long-term dynamics and memory
   - These shape the I-V curve to produce diverse firing regimes

2. **Rich Firing Regimes**:
   - **Tonic firing**: Sustained response to constant input
   - **Phasic firing**: Transient response to input onset
   - **Bursting**: High-frequency spike clusters
   - All within a single, unified model

3. **Differentiable Dynamics**:
   - Discrete-time formulation enables exact gradients
   - Direct BPTT without surrogate approximations
   - Systematic control over excitability through conductance tuning

4. **Hardware Compatibility**:
   - Can be implemented efficiently in analog circuits
   - Suitable for neuromorphic hardware deployment

### Comparison with Baselines

| Feature | LIF | AdLIF | MTC-SN |
|---------|-----|-------|--------|
| Dynamical Richness | Low | Medium | High |
| Gradient Type | Surrogate | Surrogate | Exact |
| Firing Regimes | Single | Limited | Multiple |
| Sparsity Control | Limited | Moderate | High |
| Hardware Mapping | Simple | Moderate | Efficient |

## Evaluation

### Task: Mackey-Glass Time-Series Regression
- Evaluated at the **predictability limit** (challenging benchmark)
- **Outperforms** both LIF and AdLIF networks
- **Substantially sparser activity** from both communication and computational perspectives

### Key Results
- Better accuracy on temporal regression tasks
- Higher spike sparsity (more energy-efficient)
- Richer temporal processing capabilities
- Direct trainability without surrogate approximations

## Implementation Guide

### Neuron Dynamics

The MTC-SN neuron model extends the standard conductance-based formulation:

```
C dV/dt = -g_fast(V - E_fast) - g_slow(V - E_slow) - g_ultraslow(V - E_ultraslow) + I_ext
```

Where each conductance has its own timescale:
- τ_fast << τ_slow << τ_ultraslow

### Discrete-Time Formulation

For gradient-based training, the continuous dynamics are discretized:
```
V[t+1] = V[t] + Δt/C * (sum of conductance currents + external input)
```

This enables exact gradient computation through the entire temporal trajectory.

### Training Workflow

1. **Initialize** conductance parameters and time constants
2. **Forward pass**: Simulate spiking dynamics over time
3. **Compute loss**: Compare output to target (e.g., MSE for regression)
4. **Backward pass**: Exact BPTT through discretized dynamics
5. **Update**: Gradient-based optimization of conductance parameters

## Practical Applications

### 1. Temporal Regression
- Time-series prediction
- System identification
- Signal processing

### 2. Neuromorphic Computing
- Energy-efficient edge inference
- Analog circuit implementation
- Low-power temporal processing

### 3. Biological Modeling
- Capturing diverse neuronal firing patterns
- Studying multi-timescale neural dynamics
- Bridging biological and artificial neural networks

## Key Concepts

### Conductance-Based Neurons
More biologically realistic than current-based models, where synaptic inputs modulate membrane conductance rather than injecting current directly.

### Multi-Timescale Dynamics
Different biological processes operate at different timescales (ion channel kinetics, synaptic plasticity, adaptation). MTC-SN explicitly models this hierarchy.

### Surrogate Gradient vs Exact Gradient
- **Surrogate**: Approximate gradient for non-differentiable spike functions (common in SNNs)
- **Exact**: True gradient through differentiable dynamics (MTC-SN approach)

### Mackey-Glass Equation
A delay differential equation known for chaotic dynamics, used as a benchmark for temporal prediction capabilities.

## Research Implications

1. **Exact Gradients for SNNs**: Eliminates the need for surrogate gradient approximations, providing more accurate learning signals.

2. **Multi-Timescale as Inductive Bias**: Incorporating biological timescale hierarchy improves temporal processing without increasing model complexity.

3. **Energy Efficiency**: Higher sparsity combined with better performance suggests MTC-SN is well-suited for neuromorphic hardware.

4. **Unified Framework**: Single model captures multiple firing regimes, reducing the need for task-specific neuron designs.

## Related Concepts
- Leaky Integrate-and-Fire (LIF) neurons
- Adaptive LIF (AdLIF)
- Conductance-based neural models
- Backpropagation through time (BPTT)
- Neuromorphic hardware
- Temporal sequence learning
- Spike-based regression

## Activation Triggers
- multi-timescale SNN
- conductance-based spiking
- gradient-trainable SNN
- exact gradient spiking
- temporal regression SNN
- MTC-SN
- neuromorphic regression
- multi-timescale dynamics
- conductance neuron model
- BPTT spiking network
- Mackey-Glass SNN
- spiking regression

## References
- Fulleda-Garcia, A., Soldado-Magraner, S., Margarit-Taulé, J.M. (2026). "Multi-Timescale Conductance Spiking Networks: A Sparse, Gradient-Trainable Framework with Enhanced Temporal Processing." arXiv:2605.11835v1
