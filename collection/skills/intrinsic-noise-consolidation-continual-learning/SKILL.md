---
name: intrinsic-noise-consolidation-continual-learning
description: Doob-barrier-conditioned diffusion methodology for turning analog neuromorphic hardware noise into a continual-learning resource — per-synapse consolidation via Doob h-transform creates noise-amplified restoring force that yields inverted-U noise-retention relationship. Validated on BrainScaleS-2 neuromorphic silicon with hardware-in-the-loop training.
category: neuroscience
---

# Intrinsic-Noise Consolidation for Continual Learning

## Overview

This skill implements the **Doob-barrier-conditioned diffusion** methodology from arXiv:2607.06924v1, which reframes analog neuromorphic hardware noise from an accuracy tax into a consolidation dividend. The core insight: conditioning synaptic weight diffusion on never crossing a memory-critical barrier creates a noise-amplified restoring force that non-monotonically improves sequential-task retention.

**Key paper**: *Intrinsic-Noise Consolidation: A Doob-Barrier-Conditioned Diffusion Turns Analog Device Noise into a Continual-Learning Resource* (Howe — 2026-07-08)

## Core Methodology

### Doob h-Transform for Synaptic Consolidation

After learning a task, a synaptic weight w should stay near consolidated value μ. Model as diffusion:

**Unconditioned (OU process)**: `dw = -s(w-μ)dt + σdW`
- Stationary spread σ²/2s grows with noise → more noise is strictly worse

**Barrier-conditioned (Doob h-transform)**: Condition diffusion on never crossing barrier at μ±b
- Conditioned process gains extra drift: **σ²∂_w log h(w)**
- Where h(w) is the survival probability (never hitting barrier)
- This drift: (i) points into safe region, (ii) diverges at barrier, (iii) **scales with σ²**

### The Inverted-U Prediction

The σ² steering term (stronger at moderate noise) competes with raw σ diffusion (overwhelming at high noise):

```
Retention ▲
          │     ● optimal σ*
          │    / \
          │   /   \
          │  /     \
          │ /       \
          │/         \
          └──────────────► Noise (σ)
```

This predicts a **non-monotonic inverted-U relationship** between noise and retention — a falsifiable prediction that anchored-drift methods (OU, EWC, MESU) cannot produce.

### Key Intellectual Claim Split

The method has three components; intellectual honesty requires separating them:

1. **Surrendered (known)**: The anchored drift `-s(w-μ)` — identical to small-noise limit of OU Adaptation, variance-scaled anchor of MESU, Fisher penalty of EWC
2. **Novel (a)**: Doob barrier-conditioning as a synaptic rule — every h-transform use found was generative modeling/Schrödinger bridges, none synaptic
3. **Novel (b)**: Falsifiable hardware curve prediction — increasing intrinsic noise non-monotonically improves retention

### Consolidation Rule

```
dw = [-s(w-μ) + σ²∂_w log h(w)]dt + σdW
     ↑                    ↑
     anchored drift      Doob barrier-conditioning
     (known)             (novel, noise-amplified)
```

## Experimental Validation

### E0 — Pre-registered Falsifier
- Single-head Split-MNIST, 8 seeds
- Barrier-conditioned rule lifts retention by **10.9 percentage points** at σ* = 0.02
- Paired Wilcoxon p = 0.004 vs. zero noise and vs. high noise
- Matched OU, EWC, MESU anchors are monotone-decreasing in noise

### E2 — BrainScaleS-2 Noise Model
- The inverted-U survives device-faithful BSS-2 noise model:
  - Colored noise
  - Multiplicative noise
  - Fixed-pattern noise
  - 6-bit quantization

### E5 — On-Silicon Noise Measurement
- Real BrainScaleS-2 silicon (chip hxcube7fpga3chip61_1)
- Additive, trial-to-trial-independent noise
- Coefficient of variation up to 12.0%
- `num_sends` knob averages as ≈ 1/√N — the benign noise class the mechanism needs

### E7 — On-Silicon Hardware-in-the-Loop
- Real BrainScaleS-2 silicon with chip in training loop
- Intrinsic noise steered by barrier-conditioning retains prior task **15.6 points better** than matched unconditioned control
- Single seed, one operating point; retention measured, energy modelled

## Implementation Patterns

### Barrier-Conditioned Synaptic Update

```python
# Core consolidation rule
# σ²∂_w log h(w) = noise-amplified restoring force
# h(w) = survival probability (never crossing μ±b)

def doob_barrier_drift(w, mu, barrier, sigma):
    """Compute σ²∂_w log h(w) — the Doob barrier-conditioning drift."""
    # h(w) depends on distance to barrier
    # Diverges as w → μ±b
    # Scales with σ²
    pass

def consolidated_update(w, mu, sigma, barrier, s):
    """Full barrier-conditioned synaptic update."""
    anchored = -s * (w - mu)          # Known anchored drift
    doob = doob_barrier_drift(w, mu, barrier, sigma)  # Novel Doob term
    noise = sigma * random_normal()   # Intrinsic noise
    return anchored + doob + noise
```

### Finding the Optimal Noise Level

```python
# The inverted-U means there's an optimal σ* for retention
# Search over noise levels to find the peak
for sigma in noise_range:
    retention = train_with_noise(sigma)
    if retention > best_retention:
        best_sigma = sigma
        best_retention = retention
```

### BrainScaleS-2 Integration

```python
# On BrainScaleS-2 hardware:
# 1. Measure intrinsic noise: additive, CV up to 12%
# 2. Use num_sends to adjust noise amplitude ≈ 1/√N
# 3. Apply barrier-conditioning to steer noise toward consolidation
# 4. Validate inverted-U retention curve on silicon
```

## Key Insights

1. **Noise as resource, not tax**: On analog neuromorphic hardware, intrinsic noise can be steered to consolidate memories rather than degrade them
2. **Hardware advantage**: Von-Neumann accelerators must spend energy to generate noise that neuromorphic hardware has for free
3. **Falsifiable prediction**: The inverted-U noise-retention curve is a load-bearing prediction — if it doesn't appear, the mechanism doesn't work
4. **Device-specific tuning**: The optimal σ* depends on the device's noise profile and the barrier width

## Pitfalls

- **Barrier width must be task-appropriate**: Too narrow → weights can't learn new tasks; too wide → no consolidation benefit
- **Noise must be additive and trial-independent**: Multiplicative or correlated noise may not produce the inverted-U
- **The anchored drift is NOT novel**: Don't claim novelty for `-s(w-μ)` — it's known from OU/MESU/EWC
- **Single-seed hardware results**: The on-silicon demo (E7) is single-seed — needs replication
- **Energy modelling, not measurement**: The hardware energy savings are modelled, not directly measured

## Activation Keywords

Doob h-transform, barrier-conditioned diffusion, intrinsic noise consolidation, continual learning, catastrophic forgetting, BrainScaleS-2, neuromorphic hardware, analog noise, synaptic consolidation, inverted-U noise retention, Ornstein-Uhlenbeck, MESU, EWC, rehearsal-free learning
