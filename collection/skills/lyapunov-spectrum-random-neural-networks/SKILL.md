---
name: lyapunov-spectrum-random-neural-networks
description: "Use when computing full Lyapunov spectra, attractor dimensions, or entropy rates of random RNNs via minimum-norm response and cavity method. Solves Sompolinsky 1988 open problem."
category: ai_collection
trigger: Lyapunov spectrum, random neural network, Sompolinsky model, attractor dimension, Kaplan-Yorke, entropy rate, extensive chaos, cavity method, dichotomy projector, minimum-norm solution, tangent dynamics, chaotic RNN
source: arXiv:2610.12426 (David G. Clark, Flatiron Institute, v1 8 Oct 2026)
---

# Lyapunov Spectrum of Random Neural Networks

## Core Contribution

Solves the ~40-year open problem posed by Sompolinsky et al. (1988): the **full Lyapunov spectrum** (not just λ_max) of the chaotic random rate network, computed analytically in the limit N→∞ via a three-part derivation: (1) an exact finite-N identity turning the spectrum's cumulative distribution into a response function, (2) a Hermitization-style forward-backward regularization, (3) a joint cavity calculation over network + tangent dynamics. Establishes that chaos is **extensive** (D_KY/N and h_KS/N are O(1)).

## Model

Euler-discretized Sompolinsky network, time step 0 < δ ≤ 1:

```
x_i(n+1) = (1-δ) x_i(n) + δ Σ_j J_ij φ(x_j(n)),   J_ij ~ N(0, g²/N),  φ = tanh
Jacobian:  M(n) = (1-δ)I_N + δ J D(n),   D(n) = diag(φ'(x_i(n)))  (gains)
```

Chaos onset at g=1; chaotic phase g>1 models spontaneous cortical activity.

## Why the Full Spectrum Matters

- **Kaplan–Yorke dimension**: D_KY = j + (λ₁+...+λⱼ)/|λ_{j+1}| — coordinate-invariant attractor dimension (largest k-dim volume growth rate sign change)
- **Entropy rate** (Pesin): h_KS = Σ_{λᵢ>0} λᵢ — rate at which dynamics reveal initial-condition information
- **Extensivity**: D_KY/N, h_KS/N → O(1) constants as N→∞ (confirmed; D_KY stays < ~N/10 in continuous time — extensive but low-dimensional relative to phase space)
- Both are diffeomorphism-invariant, unlike the participation-ratio dimension (which depends on variable choice)

## The Three-Part Derivation

### Part 1 (exact, finite N): Cumulative distribution as response function

Shift every exponent down by s: multiply Jacobians by e^{-δs} → shifted dynamics
`v(n+1) = M_s(n) v(n)`, `M_s = α_s I + β_s J D` with α_s = (1-δ)e^{-δs}, β_s = δe^{-δs}.
Directions with λᵢ < s decay forward. Count them:

- Consider tangent trajectories on n ∈ ℤ (no initial condition), driven by a source: `KV = I^v` where K is block-bidiagonal (IN; -M_s blocks)
- Solutions form an N-dim affine family; select the **minimum-norm** solution ‖V‖² = Σ_n ‖v(n)‖²
- Oseledets splitting R^N = E^s(n) ⊕ E^u(n) ⇒ the constructed solution decays both directions; at source time k+1 the tangent vector equals **P(k+1)w = projector onto E^s** along E^u
- Therefore **F(s) = (1/N) tr R_vv(k+1,k)**: the cumulative distribution of Lyapunov exponents is the one-step response of the minimum-norm solution of the shifted tangent dynamics. This is the dichotomy projector relation underlying Sacker–Sell spectrum computation.

### Part 2: Regularized forward–backward system (Hermitization)

Minimum-norm solution = η→0⁺ limit of regularized least-squares min ‖KV − I^v‖² + η²‖V‖². Introduce rescaled residual U = (I^v − KV)/η; the stationarity condition becomes the 2×2 block system on the 2N-dim state (forward field v, backward field u):

```
B [U; V] = [I^v; I^u],   B = [[ηI, -Kᵀ], [K, ηI]]
```

B = ηI + antisymmetric ⇒ positive definite ⇒ unique solution for η>0. Same structure as **Hermitization** for non-Hermitian random-matrix spectra. At η=0 the blocks decouple and solution freedom returns; η couples forward/backward at every time and selects the regularized solution.

### Part 3: Cavity method → single-site theory

Add neuron 0 to an N-reservoir. Perturbations of reservoir states/responses are O(N^{-1/2}); couplings J₀ᵢ, Jᵢ₀ independent of reservoir variables. Reservoir feedback reduces to:

- **Neuronal cavity field** ξ₀(n) = Σ J₀ᵢ φ(xᵢ(n)): zero-mean Gaussian, self-consistent covariance
  `⟨ξ₀(n)ξ₀(n')⟩ = g² ⟨φ(x₀(n))φ(x₀(n'))⟩` — the standard DMFT (one-way structure: network drives tangent dynamics, not vice versa)
- **Reaction kernels** Γ_vv, Γ_vu, Γ_uv, Γ_uu (n,n') = double sums of couplings × reservoir responses; at large N only two survive: A(n,n') and P(n,n')

Single-site problem: gain trajectory d₀(n) = φ'(x₀(n)) sampled from DMFT drives forward/backward fields through kernels A, P:

```
[ ηI + A,            L        ] [U₀]   [I₀ᵛ]
[ -Lᵀ,    ηI + γ_s D₀ P D₀   ] [V₀] = [I₀ᵘ]
```

(L bidiagonal shift matrix, D₀ = diag(d₀(n)), γ_s = β_s²). Self-consistency:

```
A(n,n') = γ_s ⟨d₀(n) R₀₀ᵛᵘ(n,n') d₀(n')⟩
P(n,n') = ⟨R₀₀ᵘᵛ(n,n')⟩
F(s) = lim_{η→0⁺} ⟨R₀₀ᵛᵛ(k+1,k)⟩        ← the spectrum readout
```

**Main assumption**: exchange of limits N→∞ before η→0⁺ (routine in RMT Hermitization). Solve numerically by iterating Eq. (66) on a periodic window, sampling gain trajectories from Eq. (57), lowering η in steps.

## Consistency Checks (theory recovers known results)

| Limit | Result |
|---|---|
| Trivial fixed point (g<1), any δ | Circular law: F(s) = fraction of disk \|μ\|<g inside \|μ−c_δ\|<r_s; δ→0 → semicircle density (Engelken); δ=1 → F(s)=e^{2s}/g² (Curato–Politi) |
| λ_max, δ→0 | Sompolinsky Schrödinger-operator result λ₁ = −1+√(1−E₀), E₀ ground-state energy with potential √(1−g)C^d(τ) |
| λ_max, δ=1 | Molgedey et al.: λ₁ = log g √(C^d(0)) |
| Finite δ | λ₁ = s* where 0 enters spectrum of operator T_s — nonlinear eigenvalue problem |

## Outputs

- **Lyapunov spectra** λᵢ vs rank fraction i/N (validated vs QR-method simulations at N=4096, g=3 and g=5, δ ∈ {0.05, 0.1, 0.25, 0.5}: close agreement)
- **D_KY/N = 1 − F(s_KY)** where s_KY solves ∫₀^{s_KY} s F'(s)ds = 0
- **h_KS/N = ∫₀^∞ s F'(s) ds**
- Monotone increase with g; D_KY saturates at strong coupling and can decrease (max near g=10 at δ=0.5); participation ratios grow slower at strong coupling

## Key Conceptual Advances

1. **Minimum-norm selection replaces initial conditions** — counting decaying directions via response functions avoids simulating the QR cocycle; connects Lyapunov spectra to cavity/DMFT machinery
2. **Joint cavity over network + tangent dynamics** — gains d(n) from DMFT are the only time-dependence entering the tangent problem
3. **Deninger's theorem connection** (AI-derivation route): p_N(s) = N^{-1}Σ max(λᵢ−s,0) equals a Fuglede–Kadison log-determinant of propagation operator K; differentiating gives the regularized inverse
4. Extensivity of chaos established analytically for all-to-all coupled systems (nontrivial — Ruelle's argument was for spatially extended weakly-coupled subsystems)

## Extensions (paper's roadmap)

- Multiple populations (separate E/I), low-rank coupling components, correlated reciprocal couplings J_ij↔J_ji
- Spiking networks (products of inter-spike Jacobians)
- Looped-transformer reasoning dynamics Lyapunov spectra; weight dynamics during learning

## Code

https://github.com/davidclark1/rnn-lyapunov

## AI Methodology Note

First-known case study of frontier AI deriving a long-open physics result: GPT-6 Astra produced the initial derivation (100-min autonomous session, via Deninger's theorem + matrix Dyson equation + Gaussian conditioning); author + Claude Opus 5.5 reworked it into the transparent minimum-norm/cavity presentation. The paper documents the full prompt and derivation trajectory in its "AI methodology" section.

## Related Skills

- [[cavity-method-rnn-analysis]] — two-site cavity for covariance matrices (linear equivalence)
- [[second-order-synaptic-motifs-nonlinear-dynamics]] — DMFT for structured couplings, Lyapunov geometry
- [[predictable-mean-field-chaos-rnn]] — mean-field chaos predictability
- [[bipartite-oscillator-synchronization-modes]] — E-I oscillator synchronization
