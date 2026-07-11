---
name: dendritic-in-context-learning-snn
description: DendriCL methodology for in-context learning in single-layer spiking neural networks using apical compartment dynamics that structurally implement online Widrow-Hoff LMS. Achieves ICL without attention, depth, or inference-time plasticity.
tags:
  - spiking-neural-networks
  - in-context-learning
  - dendritic-computation
  - neuromorphic
  - computational-neuroscience
---

## Overview

DendriCL (Dendritic In-Context Learning) is the first single-layer compartmental spiking neural network to achieve general-purpose in-context learning (ICL) on the Garg-2022 benchmark. The key insight: the subthreshold dynamics of a single apical dendritic compartment already implement a complete online learning algorithm (leaky Widrow-Hoff LMS), making inference-time synaptic plasticity unnecessary.

**Paper**: Shen, Wu, & Chen (2026). "Dendritic In-Context Learning in a Single-Layer Spiking Neural Network." arXiv:2607.02283 [cs.NE, cs.LG].

## Core Architecture

### Three-Compartment Pyramidal Neuron Model

Each unit has three compartments inspired by cortical layer-5 pyramidal neurons:

1. **Basal dendrite**: Feedforward projection $u_B(t) = W_B x_t$
2. **Apical dendrite**: Persistent multi-dimensional subthreshold state $u_A \in \mathbb{R}^{d_{apical}}$ (NOT reset by spikes)
3. **Soma**: LIF neuron integrating both compartments

### The Apical Recurrence (Key Innovation)

$$u_A(t+1) = \alpha u_A(t) + \gamma e_t W_A x_t$$

where $e_t = (1 - \text{flag}_t)(y_t - \hat{y}_t)$ is a gated error signal.

This is **structurally identical to leaky online Widrow-Hoff LMS**:
$$\hat{w}_{t+1} = \alpha \hat{w}_t + \gamma(y_t - \hat{w}_t^\top x_t)x_t$$

### Key Properties

- **All synaptic weights frozen at inference** — no inference-time plasticity needed
- **Single layer sufficient** — L=1 matches L=2 performance at d=20
- **Seed-stable at super-dimensional tasks** — σ ≤ 0.036 across d ∈ {25, 30, 40, 50}
- **Mechanistically verified** — linear probe recovers LMS trajectory from apical membrane at R² = 0.93

## Performance Results

### Garg-2022 ICL Benchmark (Linear Regression)

| Architecture | d=10 R² | d=20 R² | d=30 R² | d=40 R² | d=50 R² |
|---|---|---|---|---|---|
| **DendriCL (ours)** | 0.807 | 0.820 | 0.807 | 0.787 | 0.649 |
| Transformer | 0.996 | 0.989 | **bimodal collapse** | 0.009 | 0.008 |
| Spikformer | 0.977 | 0.724 | 0.636 | 0.501 | 0.301 |
| Pure LIF | 0.801 | 0.086 | 0.007 | 0.035 | — |
| Active Dendrites | 0.668 | 0.061 | — | — | — |

### Key Findings

1. **Transformer grokking at d=30**: 3 of 6 seeds fail (R² ≤ 0.012), 2 grok (R² ≈ 0.98), 1 partial (R² = 0.315) — three-mode distribution, not bimodal
2. **DendriCL smooth convergence**: All 3 seeds rise monotonically from step 0, σ ≤ 0.005 at every step
3. **Spike efficiency**: 4× fewer spikes than Pure LIF, ~10× Loihi-class energy advantage projected
4. **Energy per correct prediction**: ~6× more efficient than Spikformer

## Implementation Guide

### Parameter Specification

```python
# DendriCL Configuration
d_model = 384          # Model dimension (also apical dimension)
d_apical = 384         # Apical compartment dimension
total_params ≈ 0.75M   # Total trainable parameters

# Learned parameters (trained via BPTT, frozen at inference)
alpha     # Leak factor (approaches 1 as d grows)
gamma     # LMS step size (~0.2× theoretical optimum γ* = 1/(d+2))
W_A       # Apical weight matrix
W_B       # Basal weight matrix  
W_A,out   # Apical-to-output projection
g_A, g_B  # Compartment gains
theta     # LIF threshold
```

### Training Protocol

```python
optimizer = AdamW(lr=1e-3, weight_decay=1e-4)
scheduler = CosineAnnealingLR()
batch_size = 64
steps = 10000  # baseline, or 50000 for compute-matched
surrogate_gradient = arctan_approximation  # For LIF spikes
loss_position = "query_only"  # Loss computed only at query position (t=k+1)
```

### Forward Pass (Per Context Position t)

```python
# Input: x_t = [x_i; y_i; flag_i] where flag marks query position
u_B = W_B @ x_t                          # Basal projection
y_hat = u_A.T @ (W_A @ x_t)             # Scalar prediction
e_t = (1 - flag_t) * (y_t - y_hat)       # Gated error (off at query)
u_A = alpha * u_A + gamma * e_t * W_A @ x_t  # Apical online-LMS update
v_soma = g_B * u_B + g_A * W_A_out @ u_A     # Somatic integration
s_t = Heaviside(v_soma - theta)           # LIF spike
v_soma = v_soma - theta * s_t             # Soft reset
# Readout active ONLY at query position (t = k+1)
```

### Critical Design Constraints

1. **Width cliff**: $d_{apical} \leq 384$ trains successfully; $d_{apical} \geq 512$ diverges (LMS stability bound $\gamma < 2/(d+2)$ violated)
2. **Apical state persistence**: $u_A$ initialized to zero and NEVER reset by somatic spikes
3. **Error gating**: Error $e_t$ must be gated OFF at the query position
4. **Frozen inference weights**: All parameters frozen after BPTT training — adaptation happens purely through apical dynamics

## Biological Grounding

- Anatomically grounded in cortical layer-5 pyramidal neurons (Larkum 2013, Major et al. 2013)
- Apical dendrite receives top-down feedback, basal receives bottom-up input
- Apical calcium plateaus on 100+ ms timescales provide persistent subthreshold state
- Consistent with predictive coding framework (Rao & Ballard 1999, Bastos et al. 2012)

## Distinction from Prior Compartmental Models

| Model | Apical Role | Adaptation Mechanism |
|---|---|---|
| Urbanczik-Senn 2014 | Teacher signal | Plasticity-driven |
| Sacramento 2018 | Backprop error | Plasticity-driven |
| Iyer 2022 Active Dendrites | External context gate | Plasticity-driven |
| **DendriCL (Ours)** | **Online LMS estimator** | **Dynamics-driven, frozen weights** |

## Applications

- **Neuromorphic hardware deployment**: Loihi, SpiNNaker 2, mixed-signal SNN accelerators
- **Edge AI**: Low-power continual learning without parameter updates
- **Brain-computer interfaces**: Real-time adaptation with minimal spike count
- **Theoretical neuroscience**: Testing hypothesis that apical compartment implements online learning in vivo

## Related Skills

- `spiking-neural-network-analysis` — General SNN paper analysis patterns
- `spikingjelly-framework` — SNN implementation in PyTorch
- `surrogate-gradient-snn-training` — Training SNNs with surrogate gradients
- `brain-inspired-gating-snn` — Brain-inspired gating mechanisms
- `dynamic-neural-manifolds-snn-control` — Neural manifold-based neuromorphic control
