---
name: spectral-bias-orthogonal-polynomial-dynamics
description: Use for NN spectral bias via orthogonal polynomial dynamics.
category: ai_collection
---

# Spectral Bias via Orthogonal Polynomial Dynamics (GFS Framework)

**Source**: Yanyang Xiao — "Why Shallow Neural Networks Learn Sinusoidal Components First: An Orthogonal Polynomial Dynamics Framework" (arXiv: 2610.21964, SIAT CAS, 15 Oct 2026; theory co-developed 2018-2019 with the F-principle authors of Xu et al. 1901.06523). Code: github.com/bewantbe/ANN_GFS.

**Trigger words**: spectral bias, F-principle, frequency principle, Chebyshev/Legendre coefficients, orthogonal polynomial, Bernstein ellipse, dynamics matrix, graded matrix, flat loss landscape, effective dimension, aliasing-free frequency, NTK alternative, learning dynamics of frequency modes

## Core Idea

Explain spectral bias (networks learn low-frequency components first) **without finite-domain Fourier aliasing** and for **any sensible activation** by expanding the network output in an orthogonal-polynomial General Fourier Series (GFS) and reading gradient-descent dynamics off a single symmetric matrix **H**. The index k of orthonormal polynomial p_k is the aliasing-free "frequency" (p_k has exactly k zeros in [−1,1]).

## Framework (5 steps)

1. **Induced geometry**: population loss L(θ) = ½∫(Υθ(x)−y(x))²ρ(x)dx induces inner product ⟨f,g⟩ρ = ∫fgρ and orthonormal polynomial basis {p_k} (Chebyshev for ρ=(1−x²)^(−1/2), Legendre for ρ=1; both share asymptotics, Wang–Xiang).
2. **GFS expansion**: Υθ(x) = Σ_k c_k(θ)p_k(x), c_k = ⟨Υθ, p_k⟩ρ.
3. **Governing ODE**: under GD (small step), residual coefficients r_k = c_k − ŷ_k obey **dr/dt = −αH r** with dynamics matrix
   **H = [∂c_k/∂θ][∂c_k/∂θ]ᵀ** (stack k rows × parameter columns). H is symmetric PSD, time-dependent but structurally stable.
4. **Row decay (the mechanism)**: ∂c_k/∂θ decays with k at a rate set by the activation's complex-domain smoothness:
   - **Analytic σ** (nearest singularity ±iB; sigmoid B=π, tanh B=π/2): |∂c_k/∂θ| ≲ 2M·Θ(w_l)^(−k), **Θ(w) = B/w + √(1+(B/w)²)** (Bernstein ellipse parameter of σ(w·x); smaller input weights ⇒ faster decay ⇒ stronger low-frequency bias).
   - **σ ∈ C^(ν−1)** with bounded variation V of σ^(ν) (ReLU: ν=1): |∂c_k/∂θ| ≲ 2V/(π(k−ν̃)^(ν̃+1)) with ν̃ = ν−1 for θ=w,b (derivative loses one smoothness order) and ν̃ = ν for θ=a. ReLU: function ~k⁻², ∂/∂w (has a jump) ~k⁻¹.
5. **Graded matrix**: H = D·B·D with diagonal D_kk = Θ(w)^(−k) (exponential case) or (k+1)^(−(ν̃+1)) (algebraic case), B of bounded spectral norm. Min-max + Schur–Horn give **λ_k(H) ≤ D_kk²·λ_max(B)** and **λ_k ≤ Σ_{j≥k} H_sorted(j)(j)** — eigenvalues inherit the grading.

## Consequences

- **Spectral bias**: e^{−αΛt} contraction acts per-mode; low-k modes (large λ) converge exponentially faster. Verified: in a 64-unit sigmoid net fitting 0.8sin(2πx)+0.4sin(12πx), the k=25 Chebyshev mode stayed frozen at its initial error (0% learned after 25k GD steps) while k=1 converged 99.2% and k=6 within 2.5k steps.
- **Flat landscape / effective dimension**: at the global optimum the loss Hessian equals H_L = [∂c_k/∂θ]ᵀ[∂c_k/∂θ], which shares its nonzero spectrum with H_c = [∂c_k/∂θ][∂c_k/∂θ]ᵀ — hence the vast near-zero eigenvalue tail ⇒ extremely flat loss, numerically rank-deficient ELM/feature Gram matrices.
- **Why sinusoidal**: p_k = cos(k·arccos x) — the preferred low-k GFS modes ARE low-frequency sinusoids in the stretched coordinate; natural signals (images, sounds, EEG) have low-frequency-dominated principal components, which "coincides" with what NNs learn first — a candidate explanation for why NNs handle natural signals well.
- **Architecture/activation lever**: spectral bias strength is governed by max|w_l| (slowest-decaying rows) and σ's singularity distance B; high-frequency tasks need architectures that break the graded structure.

## Numerical Verification (2026-10-19, all reproduced exactly)

- Θ_w = B/w+√(1+(B/w)²) measured from fitted Chebyshev decay: w=6→1.6524, w=4→2.0570, w=3→2.4954, w=2→3.4332; tanh→3.4332 (rel err ≤1e-4). Sanity 1/(2−x)→3.7321 = 2+√3.
- ReLU(wx+b) kink envelope exponent −2.03; x·1[x>−0.3] (jump) −0.98.
- H_kk slope −1.91 vs predicted −2·log Θ_min = −2.06 (max|w|=2.57, Θ_min=2.80); eigenvalues monotone decreasing, decay steeper than the diagonal bound; Schur–Horn tail-sum inequality λ_k ≤ Σ_{j≥k} H_sorted: 0/60 violations; GGᵀ vs GᵀG spectra identical.

## Implementation Notes (pitfalls verified)

- Compute Chebyshev coefficients by Gauss–Chebyshev quadrature: a_k ≈ (2/M)Σ_j f(x_j)T_k(x_j), x_j = cos((j+½)π/M); evaluate T_k by recurrence T_{k+1}=2xT_k−T_{k−1}. Do NOT use cos(k·arccos x) — phase error near ±1 blows the noise floor to ~1e-10.
- Odd functions (σ(w x)−½, tanh) have exactly-zero even coefficients — fit decay rates only on above-floor points, never over a contiguous k-range.
- Kinked functions have oscillating coefficients (~sin(kθ_t+φ)/k^p): fit the local-maxima envelope, not raw points.
- Double precision floors measured decay at |a_k|≈1e-13; for fast-decaying cases (small inputs) use larger w (slower decay) to keep a clean fit window.
- GFS H analysis applies per-block: rows of ∂c_k/∂θ for θ=a_l, b_l, w_l each carry the same Θ(w_l) but different algebraic orders (ν̃=ν vs ν−1).

## When to Use

- Diagnosing why a net fails on high-frequency/sharp features and predicting which frequency modes will train first
- Choosing activation/input-weight initialization to control spectral bias (Θ(w) formula gives the exact dial)
- Estimating flat directions / effective dimension of the loss near global minima without Hessian spectra
- Replacing finite-domain Fourier analysis (aliasing-prone) for frequency bookkeeping on bounded domains
- Theoretical analysis of arbitrary networks: H is defined for any differentiable fθ; truncation is justified by the fast decay of c_k
