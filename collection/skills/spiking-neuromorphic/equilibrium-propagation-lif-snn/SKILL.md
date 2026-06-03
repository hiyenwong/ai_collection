---
name: equilibrium-propagation-lif-snn
description: "Equilibrium Propagation (EP) with Predictive Learning in Leaky Integrate-and-Fire Spiking Neural Networks. Biologically plausible alternative to backpropagation for training SNNs using energy-based two-phase learning. Use when training SNNs without backpropagation through time, implementing biologically realistic learning rules, or applying equilibrium-based optimization to spiking neuron networks."
activation_keywords:
  - equilibrium propagation SNN
  - EP leaky integrate-and-fire
  - predictive learning SNN
  - biologically plausible SNN training
  - energy-based spiking learning
  - EP without BPTT
  - equilibrium propagation LIF
  - spiking neural network backprop-free
tags:
  - spiking-neural-network
  - equilibrium-propagation
  - biologically-plausible-learning
  - leaky-integrate-and-fire
  - predictive-learning
  - energy-based-models
  - backprop-free-training
---

# Equilibrium Propagation in LIF Spiking Neural Networks

## Description

Equilibrium Propagation (EP) is a biologically plausible alternative to backpropagation that trains neural networks by comparing free equilibrium states with nudged (target-perturbed) equilibrium states. When extended to Leaky Integrate-and-Fire (LIF) spiking neural networks, EP provides a backpropagation-free training method that respects biological constraints while achieving competitive performance.

Based on crossref:2026.05.19.726261 "Equilibrium Propagation with Predictive Learning in Leaky Integrate-and-Fire Spiking Neural Networks."

## Core Concepts

### Equilibrium Propagation Principle

EP computes gradients by comparing two equilibrium states:
1. **Free phase**: Network relaxes to equilibrium with input only
2. **Nudged phase**: Network relaxes with input + target perturbation

The gradient estimate:
```
∂E/∂θ ≈ (F_nudged - F_free) / β
```
Where β is the nudging strength and F is the equilibrium energy.

### EP for LIF Neurons

For LIF spiking neurons, EP is adapted by:
1. **Spike-based equilibrium**: Equilibrium defined as steady-state firing rates rather than voltage convergence
2. **Predictive learning**: Network learns to predict future spikes based on current state
3. **Local plasticity rules**: Weight updates computed from pre/post spike correlations in each phase
4. **Membrane potential dynamics**: LIF differential equations govern neuron dynamics during both phases

### Two-Phase Learning for SNNs

```
Free Phase (duration T_free):
  1. Present input x as spike trains
  2. Let network relax to steady-state firing rates
  3. Record firing rates r_free and spike timings

Nudged Phase (duration T_nudged):
  1. Present input x + target perturbation β·(y_target - y_output)
  2. Let network relax to perturbed steady-state
  3. Record firing rates r_nudged and spike timings

Weight Update:
  Δw_ij ∝ (r_nudged_i - r_free_i) · r_pre_j
```

## Mathematical Framework

### LIF Neuron Dynamics

```
τ_m · dv/dt = -v + R·I_syn(t)
if v >= v_th: spike, v ← v_reset
```

### EP Gradient Estimation

For weight w_ij connecting neuron j to neuron i:

```
∂E/∂w_ij ≈ (1/β) · [⟨r_i·r_j⟩_nudged - ⟨r_i·r_j⟩_free]
```

Where ⟨·⟩ denotes time-averaged firing rate correlation.

### Predictive Learning Extension

The predictive learning variant adds:
- **Temporal prediction error**: Compare predicted next-state spikes with actual spikes
- **Predictive nudging**: Perturbation applied to prediction error rather than output error
- This enables learning temporal dependencies without BPTT

## Usage Patterns

### Pattern 1: Classification with EP-SNN
Train a spiking neural network for classification:
1. Encode input as Poisson spike trains
2. Build feedforward or recurrent LIF network
3. Run free phase: present input, record steady-state rates
4. Run nudged phase: add target-dependent perturbation, record rates
5. Update weights using EP gradient estimate
6. Repeat for multiple epochs

### Pattern 2: Temporal Sequence Learning
Train on temporal sequences using predictive EP:
1. Encode sequence as time-varying spike trains
2. Use recurrent LIF connections for memory
3. Free phase: let network predict next timestep
4. Nudged phase: correct prediction errors
5. Weight updates capture temporal dependencies

### Pattern 3: Neuromorphic Hardware Deployment
Deploy EP-trained SNN on neuromorphic hardware:
1. Train using EP simulation on conventional hardware
2. Convert trained weights to neuromorphic format
3. Deploy on Loihi/SpiNNaker with LIF neuron models
4. No backpropagation needed during inference or online fine-tuning

## Key Parameters

| Parameter | Description | Typical Value |
|---|---|---|
| β (nudging strength) | Perturbation magnitude | 0.01-0.1 |
| T_free | Free phase duration | 50-200 timesteps |
| T_nudged | Nudged phase duration | 50-200 timesteps |
| τ_membrane | LIF membrane time constant | 10-30ms |
| v_threshold | Spike threshold | 1.0 (normalized) |
| v_reset | Reset potential after spike | 0.0 |

## Advantages Over BPTT

1. **Biological plausibility**: No error backpropagation through time
2. **Local learning rules**: Each synapse only needs local pre/post activity
3. **Energy efficiency**: Can be implemented with event-driven neuromorphic hardware
4. **Temporal learning**: Predictive EP handles sequences without storing full trajectories

## Error Handling

### Network Doesn't Converge to Equilibrium
- Increase free/nudged phase duration
- Reduce learning rate
- Check LIF parameters (τ_m, threshold) are stable

### EP Gradient Too Noisy
- Average over multiple trials per phase
- Increase β slightly (but not too large to break linear approximation)
- Use exponential moving average of gradients

### Poor Classification Performance
- Ensure input encoding preserves relevant features
- Try deeper network architecture
- Compare with surrogate gradient baseline to isolate EP-specific issues

## Related Skills

- **energy-based-neurocomputation**: General energy-based learning frameworks
- **snn-learning-survey**: Comprehensive SNN learning rules survey
- **decolle-snn-learning**: Deep continuous local learning for SNNs
- **selective-alignment-kd-snn**: Knowledge distillation for SNNs
- **spiking-free-energy-control**: Spiking control via free energy principle
