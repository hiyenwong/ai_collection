---
name: spikfax-second-order-snn
description: Second-order KFAC optimizer for SNN training (SpiKFAX).
category: ai_collection
---

# SpiKFAX: Kronecker-Factored Second-Order Optimization for Spiking Neural Networks

**Source**: Alouani & Doan (Queen's University Belfast, CSIT), arXiv:2609.29379 (Sep 2026)
**Trigger words**: SNN training, second-order optimization, KFAC, Fisher information, surrogate gradient, sharp loss landscape, preconditioned update, neuromorphic

## Problem: Why SNNs Defeat First-Order Optimizers

Spiking activations create a **sharp loss landscape** that first-order methods (SGD/Adam/AdamW) handle poorly:

1. **Sparsity** — most neurons are silent most timesteps → gradients are sparse and high-variance
2. **Discreteness** — spike generation is a Heaviside step, non-differentiable; surrogate gradients (SuperSpike, arctan, sigmoid) only partially smooth this
3. **Time-recurrence** — membrane dynamics couple all timesteps; curvature has temporal structure that static-network preconditioners (KFC/KFAC) ignore

Prior SNN-specific optimizers (AdaBreg sparsity, SAM flatness, feedback-control local learning) never used curvature via Kronecker-factored Fisher — that is the gap SpiKFAX fills.

## Core Derivation Chain

### SNN model (LIF with subtractive soft reset)

```
u_t = β·u_{t-1} + W·x_t − V_thr·s_{t-1}
s_t = Θ(u_t − V_thr)        # Θ = Heaviside, non-differentiable
```
Backward pass replaces ∂s_t/∂u_t with surrogate σ′(u_t − V_thr).

### Lemma 1 — Recurrent Jacobian (surrogate form)

```
∂u_t/∂u_{t-1} ≈ β − V_thr·σ′(u_{t-1} − V_thr)
```
Note: this is NOT just β — the reset coupling subtracts a term proportional to the surrogate slope.

### Lemma 2 — BPTT error propagation

With terminal condition δ_{τ+1} = 0:

```
δ_t = (∂L/∂s_t)·σ′(u_t − V_thr)        # direct path (this timestep's spike)
    + δ_{t+1}·(β − V_thr·σ′(u_t − V_thr))  # recurrent path (future membrane)
```

Weight gradient accumulates over time: `∇W L = Σ_t δ_t·x_t^T`.

### Three Approximation Assumptions (stated separately — keep them explicit)

1. **Layer-wise block diagonality** — cross-layer Fisher terms discarded (standard KFAC)
2. **Independent activations & derivatives** — `E[(x_t x_s^T) ⊗ (δ_t δ_s^T)] ≈ E[x_t x_s^T] ⊗ E[δ_t δ_s^T]`
3. **Temporal homogeneity of input second moment** — `E[x_t x_s^T] ≈ A := E[r·r^T]` for ALL t,s, where `r = (1/τ)Σ_t x_t` is the **spike-rate vector**. The curvature sees the spike train only through its time-averaged firing rate, not per-timestep correlations.

### Lemma 3 — Kronecker-factored Fisher for a shared weight

```
F_W ≈ A ⊗ G
A = E[r·r^T]                          # input rate second moment (m×m)
G = E[(Σ_t δ_t)(Σ_t δ_t)^T]           # accumulated error second moment (n×n)

Preconditioned update:
∆W = −γ · G^{-1} · (∇W L) · A^{-1}
```

**Key SNN adaptation**: unlike static KFAC where factors come from single forward/backward passes, here G uses the **time-accumulated** error Σ_t δ_t and A uses the **time-averaged** rate r. This is the essence of making KFAC temporal.

For conv layers: x_t is patch-extracted input; expectations also average over spatial locations (spatially-uncorrelated-derivatives approximation of KFC on top).

## Complexity (Theorem 1)

Per layer (input dim m, output dim n, batch B, τ timesteps, inverse refresh every T_inv steps):

```
O(Bτ(m+n) + B(m²+n²) + T_inv⁻¹·(m³+n³) + N(m+n))
```

- Kronecker factor inversion: `m³+n³ ≤ 2(mn)^1.5/min(m,n)` → per-layer cost **O(N^1.5)** for balanced layers instead of O(N³) full Fisher inversion
- Wall-clock: only **1.2–1.4× slower per iteration** than Adam/AdamW/SGD; exact Fisher is intractable even for MLP

## Algorithm Sketch (implementable)

```python
# Running statistics (EMA with decay λ, e.g. λ=0.95, dampening ε):
A_run += r_batch @ r_batch.T      # r_batch = mean spike rate over τ per sample
G_run += dsum @ dsum.T            # dsum = Σ_t δ_t accumulated over τ
# every T_inv steps (e.g. 10):
A_inv = invert(A_run + εI)        # m×m
G_inv = invert(G_run + εI)        # n×n
# update:
grad = Σ_t δ_t @ x_t.T            # standard BPTT gradient
W -= lr * (G_inv @ grad @ A_inv)
```

## Experimental Results (SNNTorch, RTX A5000, 5 seeds)

| Dataset | Best Arch+Opt | Accuracy | vs AdamW |
|---------|--------------|----------|----------|
| N-MNIST | S-VGG11 + SpiKFAX | **99.92%** | +0.70 |
| CIFAR10-DVS | S-VGG11 + SpiKFAX | **56.15%** | +12.9 (vs 43.15) |
| DVS128 Gesture | S-VGG11 + SpiKFAX | **76.13%** | +6.43 (vs 69.7) |

- **Consistency**: SpiKFAX wins on ALL of {S-MLP, S-LeNet5, S-VGG11, S-VGG16, S-ResNet18} × {MNIST, F-MNIST, CIFAR10, CIFAR100, N-MNIST, CIFAR10-DVS, DVS128}
- **Stability**: loss drops steeply from ~75th step; reaches peak accuracy by epoch 15 (vs plateau at lower values for Adam/AdamW)
- **LR robustness**: stable high accuracy across LR sweep where baselines degrade

## Positioning vs Related SNN Optimizers

| Method | Mechanism | Curvature? |
|--------|-----------|-----------|
| AdaBreg / Linearized Bregman | weight sparsity via Bregman iterations | ✗ |
| Sharpness-aware surrogate training | flat minima via perturbation | ✗ (indirect) |
| Feedback-control optimizer | local online learning, no BPTT | ✗ |
| **SpiKFAX** | **direct Kronecker-factored Fisher preconditioning** | ✓ |

## When to Use

- Training deep SNNs (VGG-scale or deeper) where Adam-family plateaus early or diverges
- Neuromorphic event-camera benchmarks (CIFAR10-DVS, DVS128) — gains are largest here (+6–13%)
- Any SNN with time-shared weights and surrogate-gradient BPTT
- **Skip it**: shallow SNNs on easy datasets (N-MNIST saturates anyway), or if per-step 1.2–1.4× overhead is unacceptable on tiny budgets

## Limitations to Watch

- Assumption 3 (temporal homogeneity) discards per-timestep correlation structure — likely suboptimal for strongly time-structured tasks (temporal sequence learning, audio streams)
- Derived for fully-connected shared weights; conv adaptation stacks KFC spatial assumptions on top
- Fisher vs empirical Fisher distinction matters: sampling ŷ~p_θ(·|x) (true Fisher) vs observed label y (empirical) — paper uses the true-Fisher definition; implementations must be careful which one they estimate
