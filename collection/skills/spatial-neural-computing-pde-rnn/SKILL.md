---
name: spatial-neural-computing-pde-rnn
description: SpatialRNN methodology — PDE-medium (wave equation) recurrence giving infinite-order RNN equivalence and robust marginal stability. Use when designing long-memory recurrent models, fixing vanishing/exploding gradients, or wave-based physical computing.
category: ai_collection
created: 2026-10-09
source_paper: "Learning infinite context windows in recurrent architectures via spatial neural computing (arXiv:2610.10690)"
authors: "Salvador-Pomarol, Montanari, Miller, Motter, Cortés"
---

# Spatial Neural Computing — PDE-Medium Recurrent Architectures (SpatialRNN)

## Core Idea

Replace neuron-to-neuron recurrent communication with a **spatially evolving medium** governed by a discretized second-order PDE (wave equation). The medium's spatiotemporal patterns serve as implicit, high-capacity memory, yielding an RNN with **unbounded receptive field, O(1) memory, and fixed parameter count** that provably avoids vanishing/exploding gradients under input-dependent nonlinear perturbations. Inspired by cortical traveling waves (Benigno, Davis, Ermentrout & Kleinfeld, Singer).

## The Architecture

Standard RNN instant communication `h_t = Φ(W_h h_{t-1} + W_x x_t)` is replaced by coupling neurons to a shared medium ψ that obeys a second-order linear PDE:

```
ρ(x)² ∂²ψ/∂t² + γ(x) ∂ψ/∂t = L(ψ) + β(h(t))     (continuous, wave eq: L = c²Δ)
```

Discretized (Störmer–Verlet for the wave equation) into a second-order LDE plus the neural update:

```
ψ_t = W ψ_{t-1} + W̃ ψ_{t-2} + B h_{t-1}          (medium dynamics; wave: W = 2I + c²Δt²W_Δ, W̃ = -I)
h_t = Φ(W_x x_t + W_ψ ψ_t + b_h)                 (neurons read from medium)
y_t = softmax(W_yh h_t + W_yψ1 ψ_t + W_yψ2 ψ_{t-1} + b_y)
```

Only 4 fixed-size matrices {W, W̃, B, W_ψ} — regardless of sequence length.

## Theoretical Results

### 1. Equivalence to a structured ∞-order RNN (Theorem 2.3)

The medium state is exactly a convolution over the ENTIRE hidden-state history:

```
ψ_t = Σ_{k=1}^{t-1} W_k h_{t-k},   where  W₁ = B,  W₂ = W B,  W_k = W W_{k-1} + W̃ W_{k-2}
```

- **vs ∞-order RNN**: needs O(tn²) params + O(tn) memory. SpatialRNN: O(1) memory (just ψ_t, ψ_{t-1}) + 4 matrices.
- **vs finite-order HORNN (order d)**: every lag beyond d must transit through intermediate states → exponential decay regardless of d.

### 2. Why finite-order RNNs/HORNNs can NEVER be robustly stable (Proposition 3.2)

Gradient dynamics of any HORNN: `G_m = D_m Σ_k W_k G_{m-k}` where D_m = diag(Φ'(...)) is input-dependent. Frozen-time spectrum via z-transform: roots of `det(I - D Ŵ(λ)) = 0`, `Ŵ(λ) = Σ W_k λ^{-k}`. The diagonal nonlinearity factor D multiplies the whole recurrence operator, so **any** input variation perturbs eigenvalues off the unit circle. Holds for orthogonal, nonnormal (coRNN), diagonal, and LSTM/GRU-style parameterizations alike — they delay but cannot prevent decay. This is a structural impossibility, not a tuning issue.

### 3. Robust marginal stability of SpatialRNN (Theorem 3.3) — THE key theorem

SpatialRNN gradient dynamics is second-order: `Ψ_m = (W + B D_m W_ψ) Ψ_{m-1} + W̃ Ψ_{m-2}`. The nonlinearity D enters as a **structural perturbation inside a companion matrix**, not as a per-step multiplicative scaling. Constructive conditions for eigenvalues locked to circles of prescribed radius α_i, invariant to any admissible D:

Structure W, W̃ as block upper-triangular with block sizes n_i (i = 1..k):
```
W = [[W₁ ⋆ ⋆],[0 W₂ ⋆],[0 0 Wₖ]],   W̃ = [[-α₁²I ⋆ ⋆],[0 -α₂²I ⋆],[0 0 -αₖ²I]]
```
1. W_i symmetric; B = blkdiag{B₁..B_k}; W_ψ = Σ blkdiag{W_ψ,1..,W_ψ,k} for diagonal Σ
2. Norm bound: ‖W_i‖² + Φ̄‖B_i‖²‖W_ψ,i‖² < 2α_i², where Φ̄ = max(|Φ'_min|, |Φ'_max|)

Then every block contributes exactly 2n_i simple eigenvalues with **|λ| = α_i for ALL D ∈ D** (complex-conjugate underdamped pairs; condition 2 keeps discriminant negative).

- **α_i = 1** → marginal stability: nonvanishing gradients over arbitrarily long horizons (memory retention)
- **α_i < 1** → controlled exponential forgetting at a prescribed rate
- The wave equation satisfies all conditions with k=1, α₁=1 automatically.

Empirically trained SpatialRNN Jacobians change only ~6% over 783 psMNIST steps; gradient norms stay flat over long horizons.

### 4. O(1) BPTT memory via symplectic structure

With α_i = 1 the medium dynamics are non-dissipative and preserve a symplectic form → medium states can be **exactly reconstructed backward** from final states (machine precision), so BPTT needs O(1) cache instead of O(T). Dissipative blocks (α<1) amplify round-off backward and need checkpointing.

## Experimental Results (single-layer, no regularizers)

| Benchmark | SpatialRNN | Best baseline |
|---|---|---|
| Copy task T up to 1024 | ~99% at ALL lengths (6.8k params, k=4 blocks n={32,8,8,8}, α₁=1) | HORNN d=15 degrades with T (17.7k params) |
| psMNIST (T=784) | 96.3 ± 0.1% (152 units, 36k params) | coRNN 95.0 (134k), GRU 94.1 (200k), LSTM 92.9 (270k) |
| npCIFAR10 (T=1000) | 57.8% (51k params), **accuracy invariant to noise padding T** | LEM 60.5 (116k), coRNN 59.0 (46k) |

Trained models spontaneously learn a **mix of α≈1 and α<1 blocks** — simultaneous retention and forgetting.

## When to Use / Design Lessons

- **Diagnose gradient pathologies structurally**: ask HOW the nonlinearity enters the gradient recurrence (per-step multiplicative factor → doomed; structural perturbation in companion form → tractable), not just the spectrum of W.
- **Long-horizon streaming with fixed-size state** (sensor monitoring, long-horizon control, spatiotemporal signal prediction) — the sweet spot; locality/geometry of medium gives inductive bias.
- **Selective forgetting**: prescribe per-block α_i rather than gating (LSTM/GRU add parameters and break parallelism; α_i is 1 scalar per block and can be fixed a priori or learned).
- **Lifting to 2nd order generalizes**: any first-order recurrence (e.g., SSMs) can have its recurrence lifted to second order to gain robust eigenvalue placement; SSM scans and SpatialRNN medium dynamics coincide only under restrictive conditions.
- **Physical computing**: wave-based substrates (solitons, wave physics, Hughes et al. analog RNN, Marcucci rogue-wave computing) realize the medium directly; symplectic structure makes backprop memory O(1).

## Limitations

- Frozen-time guarantee is necessary but NOT sufficient for full LTV marginal stability (switched products of unit-modulus matrices can still grow/decay slowly — observed drift is sub-exponential, ~6% over 783 steps).
- Information capacity bounded by medium dimension × numerical precision — unbounded receptive field ≠ lossless infinite history.
- Sequential nonlinear recurrence: no associative-scan parallelization (unlike linear SSMs); each step costs a few extra matvecs vs plain RNN.
- npCIFAR10 ceiling: memory robustness ≠ feature-extraction power.

## Key References

- Code: anonymous.4open.science/r/SpatialRNN-code-748C
- Keller & Welling 2023 (Neural Wave Machines — oscillatory units, not shared medium); Rusch & Mishra (coRNN); Gonzalez et al. 2026 (predictability → parallelization of nonlinear SSMs)
- Montanari et al. 2026 (energy-based dynamical models for neurocomputation) — companion energy-based framework
