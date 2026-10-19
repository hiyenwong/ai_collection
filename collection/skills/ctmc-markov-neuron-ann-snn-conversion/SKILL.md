---
name: ctmc-markov-neuron-ann-snn-conversion
description: Use for ANN-SNN conversion via CTMC Markov neurons.
category: ai_collection
---

# Activation-Flexible ANN-to-SNN Conversion with Finite-State CTMC Markov Neurons

Methodology from arXiv:2609.30102 (Jia & Xiao, NYU Shanghai, Sep 2026).
A finite-state continuous-time Markov chain (CTMC) neuron framework whose **stationary spike flux approximates every continuous nonnegative monotone activation function** on a compact interval — breaking the ReLU-only restriction of standard ANN-to-SNN conversion. Use when converting ANNs with sigmoid/softplus/clipped activations to spiking networks, or analyzing spike-budget vs activation-shape tradeoffs.

## Core Idea

Standard conversion fixes a correspondence: IF dynamics ↔ ReLU positive-linear branch; leak adds rheobase/curvature. Instead, make the neuron's **stationary firing-rate curve an effective activation** and FIT it to any target via Markov transition rates.

## Three-State CTMC Neuron (B, G, R)

States: **B**ase, **G**ate, **R**efractory. Transitions: B→G at rate a(H), G→B at rate b, G→R (emits spike) at rate c(H), R→B at rate d, where H is the input (preactivation) and a, c are affine input-dependent.

Generator matrix:

```
Q_θ(H) = [ −a        a        0   ]
          [  b   −(b + c)      c   ]
          [  d        0       −d   ]
```

Solving the stationary distribution πQ = 0 gives the **stationary spike flux**:

```
ν_θ(H) = π_G·c(H) = d·a(H)·c(H) / ( d·[a(H) + b + c(H)] + a(H)·c(H) )
```

This rational form flexibly shapes the input→rate curve: transition structure shapes the curve; refractory transitions control saturation.

## Theorem 1 (Uniform Approximation)

For any continuous nondecreasing φ: [I_min, I_max] → [0, ∞) and any ε > 0, there exists a finite-state CTMC with affine input-dependent transition rates whose stationary spike flux F satisfies `sup |F(I) − φ(I)| < ε` over the compact interval. (Proof via appendix; constructive via state augmentation.)

In practice, two- and three-state CTMCs suffice for common activations on empirical operating ranges:
- sigmoid (3-state): MSE 1.1×10⁻³
- ReLU (low-state): MSE 2.4×10⁻³
- ClipReLU10: MSE 2.7×10⁻³
- softplus: MSE 1.1×10⁻²

Fitting: least squares on domain D sampled from ANN preactivations, `min_θ (1/M)Σ[ν_θ(H_m) − φ(H_m)]²`, subject to nonnegative rates. Claims are for compact empirical ranges, NOT global unbounded representation.

## Conversion Pipeline

1. **Fit CTMC rates** to each layer's target activation on its empirical preactivation domain.
2. **Layerwise rate scaling**: choose scale α_ℓ, target rate `r_ℓ = α_ℓ·a_ℓ`; rescale incoming weights `W^{ℓ,*} = W^ℓ/α_{ℓ−1}` to preserve the affine map in expectation.
3. **Filtered spike input**: `H_j^ℓ(t) = b_j^ℓ + Σ_i W^{ℓ,*}_ji (k_τ * dN_i^{ℓ−1})(t)` with normalized exponential kernel `k_τ(t) = τ⁻¹e^{−t/τ}·1{t≥0}` — kernel integrates to 1, so stationary presynaptic rate yields the desired mean input.
4. **Finite-window decoding**: over window T, decode rate `r̂ = N(T)/T`, activation `â = r̂/α_ℓ`.

## Accuracy Decomposition (Mean-Field Diagnostic)

Replace sampled spike counts by deterministic ν_θ(H) → mean-field accuracy A_MF. Then:

```
A_ANN − A_SNN = (A_ANN − A_MF) + (A_MF − A_SNN)
                  └─ fitting bias ──┘  └─ finite-window sampling gap ┘
```

On VGG-11/MNIST the dominant residual is **finite-T sampling variance**, not stationary-rate fit. On CIFAR-10, layerwise distribution mismatch (terminal layers, upper quantiles) dominates — a target for calibration.

## Key Experimental Findings

**MNIST MLP (784-256-128-10), all within 1% gap:**
- ReLU: 13.0k SynOps, 0.81% gap (cheapest)
- sigmoid: 14.4k SynOps, 0.96% (dense compressed spike distribution)
- softplus: 18.1k SynOps, 0.91%
- ClipReLU4: 9.1k SynOps — **30% event reduction** vs ReLU

**ClipReLU_K ablation (shared ReLU weights, clip-on-forward):** min SynOps for <1% gap: K=1 never converges (80% of active L1 units exceed cap), K=4 optimal (9.1k), monotone: moderate clipping removes the high-rate TAIL; aggressive clipping intersects the distribution BODY → fails. **Mechanism: tail truncation helps conditionally, bounded activations have no universal advantage.**

**VGG-11/MNIST**: ClipReLU6 → 1.93×10⁹ SynOps (−27%), 9.51 spikes/neuron vs ReLU 2.64×10⁹ / 12.97 at matched <0.5% gap.

**VGG-11/CIFAR-10: trend REVERSES** — ClipReLU_q95 needs 2.66×10⁹ SynOps (+29%) vs ReLU 2.06×10⁹. Clipping removes useful upper-tail information here; terminal-layer upper-quantile underestimation is the failure mode.

**Sigmoid cost analysis**: sigmoid's nonzero output for negative preactivations inflates spike counts; a 2-unit right shift helps only at high budget (budget-dependent, not universal).

## Cost Metric: SynOps

`SynOps(x) = Σ_ℓ Σ_i N_i^ℓ(T;x)·fanout_{ℓ+1}` — raw spike transmissions per sample. Caveats: excludes RNG, transition scheduling, memory access, communication. NOT a measured energy proxy.

## Practical Guidance

- Converting non-ReLU ANNs: fit 2-3 state CTMC per layer activation; expect sub-1% gaps on shallow nets, larger on deep nets with distribution shift.
- Spike budget optimization: try moderate clipping (K≈4-6) — validate on YOUR dataset; CIFAR-like data may reverse the benefit.
- Diagnose failures with the mean-field decomposition + layerwise preactivation quantiles (q50/q90/q99) — mismatch concentrates in terminal layers, upper quantiles.
- Event-driven hardware compatible (finite-state memory), but SynOps ≠ energy.

## References
- Cai et al. (2021); Wu et al. (2023) — earlier Markov neuron models
- Bu et al. (2022) ICLR — optimal ANN-SNN conversion baselines
- Sandler et al. (2018) — ReLU6 / bounded activations in efficient nets

Source: arXiv:2609.30102 — Jia & Xiao, "Activation-Flexible ANN-to-SNN Conversion with Finite-State Markov Neurons"