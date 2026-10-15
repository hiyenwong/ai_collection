---
name: finite-time-lyapunov-mde-rnn
description: "Use when deriving full Lyapunov spectra of random RNNs at finite time or stationarity via matrix Dyson equations. Log-determinant + cocycle framework."
category: ai_collection
trigger: finite-time Lyapunov spectrum, matrix Dyson equation, random recurrent neural network, tangent propagator singular values, spectral free energy, Hermitization, gain history, quenched connectivity, Schrödinger edge problem, Fuglede-Kadison determinant, cocycle representation, temporal memory replay, soft spectral tail, Sompolinsky model, chaotic RNN stability
source: arXiv:2610.14922 (Haoyu Albert Wang & Wei P. Dai, Fudan University, v1 10 Oct 2026)
---

# Full Lyapunov Spectra of Random Neural Networks, Part I — Finite-Time & Asymptotic MDE Framework

## When to Use

- Compute **full Lyapunov spectra** of random RNNs (not just λ_max) at **finite observation time T** or in the **stationary asymptotic regime**.
- Predict tangent-volume growth, positive-exponent fraction p+, Kolmogorov–Sinai entropy h+ (=Pesin), Kaplan–Yorke dimension d_KY.
- Distinguish this from the contemporaneous **cavity approach** (arXiv:2610.12426, Clark; see skill `lyapunov-spectrum-random-neural-networks`) — the MDE framework here is complementary: log-determinant + Hermitization vs. response-function + cavity.

## Model (Sompolinsky–Crisanti–Sommers rate network)

```
dx_i/dt = -x_i + Σ_j W_ij tanh(x_j),   W_ij = g·ξ_ij/√N (ξ~N(0,1), W_ii=0)
Tangent dynamics:  du/dt = [-I + W D(t)] u,   D_ii(t) = sech²(x_i(t))  (local gains)
Stationary chaotic branch: (1-∂²_τ) C_x(τ) = g²·E[tanh x(0)·tanh x(τ)]  (DMFT)
Gain process d(t)=sech²(x(t)) is generally NON-Gaussian — use its full path law, never a one-time fit.
```

## Core Contribution

Two mean-field formulations that **retain complete local gain histories** and the **repeated action of quenched connectivity** (the same W acts at every time step — a one-time Jacobian distribution does NOT specify the product law):

1. **Finite-time**: exact log-determinant identity → spectral free energy → closed-contour **matrix Dyson equation (MDE)** for the smoothed spectral tail
2. **Stationary**: **cocycle representation** (Y = B·U with time-shift U) → operator MDE via Fuglede–Kadison/Deninger determinant for the asymptotic cumulative spectrum

## Key Formulas

### Spectral free energy & soft tail (exact at finite N)

```
F_{N,T}(µ) = (1/2NT)·log det[I + e^{-2µT} M_T† M_T]
ν_{N,T}(µ) = -∂_µ F_{N,T}(µ)  = (1/N)·Σ_i 1/(1+e^{2T(µ-λ_i^{(T)})})   ← logistic soft tail, smoothing width O(1/T)
det(I + q M_T† M_T) = Σ_k q^k ∧^k(M_T†M)^{1/2}   ← same determinant generates tangent-volume growth at EVERY rank k
```

Asymptotic limits (multiplicative ergodic theorem + empirical-measure limit): `F(µ)=∫(λ-µ)⁺ρ(dλ)`, `ν(µ)=-F'(µ)`, **p⁺=ν(0)** (positive-exponent fraction), **h⁺=F(0)** (KS entropy/neuron), and at the KY crossing: `F(µ*)+µ*ν(µ*)=0 → d_KY=ν(µ*)`.

### Finite-time MDE (Hermitization)

Discretize with `B_t = cI + bW D_t` (c=e^{-δ}, b=1-e^{-δ}), `M_T = B_{m-1}···B_0`. Hermitization produces site blocks of size 4m. For gain histories sampled independently across sites:

```
M_d^{-1}(z) = h_0 - zI - g²(X + A_d M_d A_d†),   X = E_d(A_d M_d A_d†)
Physical branch: Im M_d ⪰ 0 for z = iη, η>0. Tail = corner readout ν_T(µ) = 1 - lim_{η↓0} Re E_d[M_d(iη)]²_{m,0}
```

**Critical structural point**: the covariance contraction `E_d(A_d M_d A_d†)` keeps the correlations created by REUSE of the same quenched matrix. Averaging the gains before the inverse gives a DIFFERENT (wrong) equation.

### Stationary MDE (cocycle)

```
F_N(µ) = δ^{-1}·log Δ_τ(e^{δµ}I - Y_N) - µ     (Deninger determinant; radii of Brown measure = e^{δλ_i})
M_d(r,z) = [ -zI-Γ   ℓ_r ; ℓ_r†  -zI-g²K_d†PK_d ]^{-1}
ℓ_r = rI - cS,  K_d = -bD_d S,  S = time-shift (Sf)_t = f_{t-1},  r = e^{δµ}
P = E_d G_{++,d},  Γ = g² E_d(K_d G_{--,d} K_d†)   (convolution operators — two Fourier functions)
ν(µ) = 1 - r·lim_{η↓0} Re τ_erg E_d G_{-+,d}(r,iη)
```

### Maximal exponent recovery (consistency check)

Exterior stability of the stationary MDE → linearized equation reduces to a **1D Schrödinger problem** with effective potential `1 - g²C_d(τ)` where C_d(τ)=E[d(0)d(τ)]:

```
λ_e = -1 + √(1 - E_0),   H = -∂²_τ + 1 - g²C_d(τ),  E_0 = lowest spectral value
```

Recovers the classical two-copy DMFT result (Sompolinsky 1988; Cugliandolo et al.). At g=1.2/1.5/2.5 the MDE edges are 0.011919464 / 0.046745834 / 0.175779366 (abs. diff. from independent two-copy calc: ≤2.4×10⁻⁶).

## Validation Protocol (error decomposition worth copying)

Three-tier separation on a common threshold grid G:

```
E_A = max_µ |ν_MDE - ν̄_path|          ← tests the marked-path equation itself
E_B = max_µ |ν̄_path - ν̄_net|          ← tests replacing autonomous paths by independent DMFT paths
E_net = max_µ |ν_MDE - ν̄_net| ≤ E_A + E_B   ← combined prediction
```

- Finite-time: T=4, N=1024, all couplings g∈{1.2,1.5,3} → E_net < 0.0056. All 45 prescribed-path predictions within pointwise 95% Student intervals (largest thin-tail rel. error 23.15%).
- Stationary full spectrum: max tail discrepancy < 0.018 across couplings; g=2.5 prediction FROZEN before reference simulations (pre-registration).
- Positive sector (p⁺, h⁺, d_KY) within 3% of QR readouts via implicit differentiation (needs tight regularizer control).

## The Replay Experiment (physical takeaway)

Hold the one-time gain law fixed, speed up the path: `d_a(t) = d(at)`, a>0. Instantaneous Jacobian statistics unchanged (stationarity) and Σλ_i = -1 exactly (Liouville, since W_ii=0) — yet at g=1.3, N=4096, a=1→3 drops the **mean positive exponent count from 10.0 to 2.5**.

**Conclusion: temporal memory redistributes instability among tangent directions while instantaneous statistics and total contraction stay fixed.** Spectral stability carries information about dynamical history beyond the one-time Jacobian distribution. (Caveat: 2 of 30 stationary replay comparisons exceeded sampling intervals; this is a prescribed linear cocycle, not a new autonomous attractor.)

## Honest Limitations (authors' own)

- Accuracy is not uniform in N, T, path resolution, or near spectral edges; near-onset spectral density and critical amplitudes open.
- Autonomous-network use requires stationary cavity replacement + small-singular-value control in the zero-regulator limit — small equation residual ≠ proof.
- N=2048 point has one matrix (no sampling interval); connecting lines in time-controls imply no intervals.
- Same first author dynasty as Clark's contemporaneous cavity paper — the two frameworks agree on the maximal exponent and overlap on mean-field bulk results.

## Reusable Patterns

1. **Log-determinant generating function**: one determinant simultaneously encodes soft spectral tail + all-rank tangent-volume growth (Σ_k q^k∧^k). Use whenever you need both spectrum and volume asymptotics.
2. **Quenched-reuse covariance**: in any MDE over products sharing one disorder matrix, the contraction `E_d(A M A†)` must be evaluated INSIDE the inverse — pre-averaging gains is a different theory.
3. **Replay dial as memory probe**: rescaling a stationary process in time (fixed 1-time law) isolates the causal effect of temporal correlations on stability — applicable to any Jacobian-product system (reservoirs, trained RNNs, forced oscillators).
4. **Frozen-prediction validation**: record numerical predictions before generating reference data, report both.
5. **Schödinger-reduction for spectral edges**: exterior MDE stability → 1D Schrödinger eigenvalue with potential 1-g²C_d(τ) — a cheap way to get λ_max from a two-time correlation only.

## Related

- `lyapunov-spectrum-random-neural-networks` (arXiv:2610.12426) — contemporaneous cavity solution, same model, extensive-chaos results; the two are complementary MDE-vs-cavity closures.
- Sompolinsky, Crisanti & Sommers (1988) — original SCS chaotic-rate-network DMFT.
- Skills: `predictable-mean-field-chaos-rnn`, `krylov-mean-field-chaos-rnn`, `ei-network-chaos-synchrony-theory`.
