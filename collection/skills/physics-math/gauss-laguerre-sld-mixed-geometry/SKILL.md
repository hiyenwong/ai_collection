---
name: gauss-laguerre-sld-mixed-geometry
description: Use when computing mixed-state QFIM/QGT or SLD with quantum algorithms, or benchmarking quantum metrology resource estimates.
trigger: mixed-state QFI, quantum Fisher information matrix, quantum geometric tensor, symmetric logarithmic derivative, SLD Lyapunov equation, Gauss-Laguerre quadrature, Bures metric, Uhlmann curvature, multiparameter incompatibility, SLD block encoding, QSVT exponential filter, QPE-free amplitude estimation, bounded-response promise, bounded-gap promise, Tikhonov regularization, fidelity susceptibility, Cramér-Rao bound, entanglement witness
author: engineering-lion5
category: ai_collection
version: 1.0
license: MIT
related_skills: finite-shot-quantum-metrology, multiparameter-hamiltonian-estimation, geometric-obstruction-quantum-metrology, qfi-stabilizer-framework, classical-shadow-estimation, optimal-shadow-estimation
---

# Gauss–Laguerre SLD: Efficient Quantum Algorithms for Mixed-State Quantum Geometry

**Source**: arXiv 2610.24686 (Wang, Zhao, Yuan, Cai — Peking U / HKU QICI / IHEP CAS, Oct 2026). First explicit unified block encoding of the full mixed-state quantum geometric tensor and QFIM, built from an exponentially convergent Gauss–Laguerre quadrature of the Lyapunov integral that defines the symmetric logarithmic derivative.

## Problem It Solves

1. Mixed-state geometry — QFIM F_jk = 2Tr[ρ{L_j,L_k}], QGT T_jk = Tr[ρL_jL_k] with F = 4Re(T) — governs multiparameter metrology (SLD Cramér–Rao bound, Holevo bound, Uhlmann-curvature incompatibility) and many-body characterization. But the SLD is defined only IMPLICITLY by the Lyapunov equation {ρ, L_j} = ∂_jρ (convention L_j = 𝓛_j/2), an ill-conditioned inversion when the smallest nonzero eigenvalue p⁺_min is small. Pure states have closed forms; mixed states do not.
2. Prior coherent-access algorithms were narrow: Zhang–Yuan (pure ground-state fidelity susceptibility), Zhang (mixed states under unitary encoding only, Q_ρ = Õ(α_A²/(εΔ_ρ⁶))). General smooth parameterizations and full-matrix coherent access were open.
3. QPE-based amplitude estimation needs an O(log 1/ε)-qubit phase register, which would erase any double-logarithmic ancilla advantage of an SLD construction.

## Component 1 — Structure-Aware Integral Reduction (the key insight)

- Vectorize the Lyapunov equation: 𝓛_ρ|L_j⟩ = |∂_jρ⟩ with 𝓛_ρ = ρ⊗I + I⊗ρ^T. The kernel condition P_K(∂_jρ)P_K = 0 — implied by LOCAL RANK PRESERVATION of ρ(x) — makes the support-restricted inverse well defined.
- Laplace/Lyapunov integral: L_j = ∫₀^∞ e^{−tρ}(∂_jρ)e^{−tρ} dt. PSD structure ⇒ nonzero spectrum of 𝓛_ρ lies in [Δ, 2] under the bounded-gap promise.
- After rescaling x = Δt, the per-eigenmode integrand is e^{−x}e^{−μx} — EXACTLY the Gauss–Laguerre weight. The K-point rule (roots of Laguerre polynomial L_K, exact for polynomials of degree ≤ 2K−1) therefore converges exponentially: ‖L_j − L̂_j‖ ≤ (2/Δ)(1 − Δ/2)^{2K}‖∂_jρ‖_F, i.e. K_ε = Θ((1/Δ)·log(‖∂_jρ‖_F/(εΔ))) — LOGARITHMIC in 1/ε at fixed conditioning. This is not a generic linear-system solve; the PSD + support/kernel structure is what buys it.

## Component 2 — LCU Compensation Grows Only Linearly (the crucial resource fact)

- Bounded-gap finite sum: L̂_j = (1/Δ) Σ_{k=1..K} w_k e^{x_k} · e^{−x_kρ/Δ}(∂_jρ)e^{−x_kρ/Δ}.
- Individual compensation factors e^{x_k} are exponentially large in the node — but the AGGREGATE β_K = Σ_k w_k e^{x_k} satisfies β_K ≥ 2K and β_K/(4K) → 1: Gauss–Laguerre weight decay cancels the exponential blow-up. LCU normalization is only Θ(K/Δ), so exponential quadrature convergence survives coherent assembly. Quadrature-index register: ⌈log₂K⌉ = O(log log 1/ε) qubits.
- Numerical note from paper: evaluate c_k = w_k e^{x_k} via the exponentially scaled Laguerre recurrence — directly forming w_k e^{x_k} underflows at large K.

## Component 3 — Block Encodings of the SLD

- Purification oracle O_ρ|0⟩_S|0⟩_A = Σ_n √p_n |φ_n⟩|π_n⟩ gives a (1, a+s, 0) block encoding of ρ via the SWAP trick U_ρ = (O_ρ†⊗I)SWAP_{S,S′}(O_ρ⊗I).
- Exponential filters e^{−t_kρ}: QSVT with an even polynomial approximating e^{−t|x|} on |x| ∈ [Δ,1] AND ≈1 at x = 0 (needed because ∂_jρ may connect support ↔ kernel), degree d = O((1/Δ)log(1/ε_p)) INDEPENDENT of t_k. All K nodes share one U_ρ query backbone — the two SELECT operations cost O(d) queries total, not O(Kd); nodes differ only through multiplexed QSVT phases.
- Per node: V_{j,k} = U_k^{(A₂S)} U_{∂_jρ}^{(A_∂S)} U_k^{(A₁S)} block-encodes A_{j,k} = e^{−t_kρ}(∂_jρ)e^{−t_kρ}; LCU assembly (coefficient prep P with √(c_k/β_K) amplitudes, SELECT_L · U_∂ · SELECT_R) gives an (α_L, a_L, ε_j)-block encoding of L_j with α_L = α_jβ_K/Δ, a_L = 2a+2s+m_j+2+⌈log₂K⌉, and per-call cost Q_ρ = O((1/Δ)[log(α_j/(ε_jΔ)) + log log(‖∂_jρ‖_F/(ε_jΔ))]), Q_∂ = O(1). **Ancilla overhead grows double-logarithmically in 1/ε** at fixed conditioning.

## Component 4 — Two Conditioning Promises (two physical regimes)

- **Bounded-gap** (Δ ≥ 1/poly(s)): controls worst-case inversion amplification; a numerical lower bound on min⁺ eigenvalue can be CERTIFIED from O_ρ (eigenstate filtering + thresholding, Appendix E).
- **Bounded-response** (M = max_j ‖ρ⁺∂_jρ‖_F² ≤ poly(s)): alignment of the derivative with ill-conditioned spectral directions; handles exponentially small gaps (e.g. truncated commuting Gibbs ensembles, low-rank unitary encodings, product encodings with fixed pure environment). NOT certifiable from the oracles — an a priori model parameter, like a condition-number bound in HLL. Bounded-gap ⇒ bounded-response (strictly stronger).
- Tikhonov regularization (ρ + θ/2): spectral denominators become p_m+p_n+θ; regularized integral L_j^(θ) = (1/θ)∫e^{−x}e^{−xρ/θ}(∂_jρ)e^{−xρ/θ}dx discretizes with Gauss–Laguerre WITHOUT e^{x_k} compensation (Σw_k = 1 ⇒ LCU norm 1/θ); converges unconditionally (damps kernel sector too). Regularization BIAS: **|F^(θ)_jj − F_jj| ≤ 8Mθ** — θ sets both numerical conditioning and admissible statistical bias.

## Component 5 — QPE-Free Amplitude Estimation for Diagonal QFI

- SLD block encoding prepares |ψ_j⟩ = (L_j⊗I_A)|ρ⟩_SA with ⟨ψ_j|ψ_k⟩ = T_jk and N_j = ‖ψ_j‖ = √F_jj / 2 → F_jj = 4N_j². Diagonal QFI estimation = success-amplitude estimation of W_j = (U_{L_j}⊗I)(I⊗O_ρ) with γ_j = Ñ_j/α_{L_j}.
- **QPE-free additive amplitude estimation (Lemma 1)**: binary-search strategy with classically controlled queries; Q_amp = O((1/ε_amp)(log 1/ϑ + log log 1/ε_amp)) calls to U, U†, ONE extra ancilla qubit — no phase register, preserving the double-log ancilla scaling.
- **Theorem 3 (bounded-gap QFI)**: Q_ρ = Õ(α_j‖∂_jρ‖_F/(ε·Δ^{7/2})), Q_∂ = Õ(α_j‖∂_jρ‖_F/(ε·Δ^{5/2})); total qubits 3a+3s+3+m_j+O(log 1/Δ + log log 1/ε). Near-Heisenberg 1/ε scaling. The Frobenius response norm RETAINS effective-rank sensitivity: ‖∂_jρ‖_F ≤ √(min{2r,N})·α_j for low-rank responses — structure-specific bounds enter the resource estimate instead of a √N worst case.
- Small-response shortcut: F_jj ≤ 2‖∂_jρ‖_F²/Δ, so output 0 when this is below ε (uses analytic norm bounds, no estimation needed).
- **Theorem 5 (bounded-response QFI)**: budget split θ = Θ(ε/M), ε_j = Θ(ε/√M), ε_amp = Θ(ε²/(α_jM^{3/2})) → Q_ρ = Õ(α_jM^{7/2}/ε⁴), Q_∂ = Õ(α_jM^{3/2}/ε²). Polynomial ε-scaling replaces the gap dependence.
- Unitary-encoding specialization (∂_xρ = −i[A,ρ] via a two-term commutator construction, ‖∂_xρ‖_F ≤ 2‖A‖): Q_ρ = Õ(α_A²/(εΔ_ρ^{7/2})) — smaller inverse-gap powers than Zhang's Δ_ρ⁶ at the same input normalization, retaining near-Heisenberg scaling.

## Component 6 — Unified Full QGT/QFIM Block Encoding (conceptual centerpiece)

- **Theorem 4**: with w = ⌈log₂m⌉ index registers X, R, uniform superposition gate D, multiplexed SLD ops 𝒰_R (controlled by R) and 𝒰_L (controlled by X), U_T = (O_ρ†⊗I)(D†⊗I)·SWAP_{X,R}·𝒰_L·𝒰_R·(D⊗I)·(O_ρ⊗I) is an (mα², a_tot, ε_tot)-block encoding of T_ij = Tr(ρL_iL_j), with a_tot = w + 2a_L + a + s and ε_tot = (Σ_ij [α(ε_i+ε_j)+ε_iε_j]²)^{1/2} (= m(2αε+ε²) for uniform errors).
- Swapping the two controlled block encodings (𝒰_R·𝒰_L instead of 𝒰_L·𝒰_R) yields the transposed QGT T^⊤. **Corollary 1**: F = 4Re(T) = 2(T + T^⊤) via a Hadamard-controlled LCU of U_T and U_T^⊤ — one extra qubit, (4mα², a_tot+1, 4ε_tot)-block encoding of the QFIM.
- Downstream quantum linear algebra on the geometry as ONE coherently accessible matrix — without classical reconstruction of entries: matrix inversion for the inverse QFIM of the multiparameter SLD Cramér–Rao bound; eigenvalue processing to identify high-information parameter directions; singular-value thresholding of the antisymmetric imaginary part (Uhlmann curvature) to certify multiparameter INCOMPATIBILITY (subject to the spectral promises of the respective QSVT routines; the SLD CRB need not be attainable — Holevo bound governs the ultimate limit).

## Resource Comparison Tables (from the paper)

Diagonal QFI to additive error ε (coherent access):
| Route | Q_ρ | Q_∂ | ε-scaling |
|---|---|---|---|
| This work, bounded gap | Õ(α_j‖∂_jρ‖_F/(εΔ^{7/2})) | Õ(α_j‖∂_jρ‖_F/(εΔ^{5/2})) | near-Heisenberg |
| This work, bounded response | Õ(α_jM^{7/2}/ε⁴) | Õ(α_jM^{3/2}/ε²) | polynomial |
| Zhang (mixed, unitary encoding) | Õ(α_A²/(εΔ_ρ⁶)) | Õ(α_A²/(εΔ_ρ³)) | near-Heisenberg |
| Zhang–Yuan (pure ground state) | Õ(α_Hα_I²/(εΔ_H³)) on U_H | Õ(α_I²/(εΔ_H²)) | near-Heisenberg |

SLD block encoding (bounded-gap, error ε_L):
| Construction | Q_ρ | α_L | LCU index width |
|---|---|---|---|
| Clayton (trapezoidal) | Õ(Δ_ρ^{−5/2}√(α_j/ε_L)) | Õ(α_jΔ_ρ^{−3}) | O(log 1/ε_L) |
| Somma (Fourier/Riemann) | Õ(Δ_ρ^{−1}) | Õ(α_jΔ_ρ^{−1}) | O(log 1/ε_L) |
| **This work (Gauss–Laguerre)** | Õ(Δ_ρ^{−1}) | Õ(α_jΔ_ρ^{−2}) | **O(log log 1/ε_L)** |

## When to Use

- Estimating QFI/QFIM/QGT of mixed probe states given purification access O_ρ + derivative block encodings U_{∂_jρ} (thermal/noisy sensing probes, truncated Gibbs ensembles, low-rank mixed states).
- Building the SLD as an algorithmic primitive for coherent multiparameter-metrology pipelines (inverse-QFIM CRB, optimal-direction eigenprocessing, Im(T)-based incompatibility certification).
- Benchmarking quantum metrology algorithm resources — the Δ^{7/2} query and double-log ancilla scalings are the current reference points; keep ‖∂_jρ‖_F visible for low-rank response families.
- Classical use: the SAME Gauss–Laguerre filtered-derivative finite sum (Eqs. 34/41) is a practical classical scheme (ED / tensor-network) for SLDs — exponentially convergent with only linear LCU-weight growth (cf. prior tensor-network Lyapunre-integration work whose cost depends on integration time and bond dimension).

## Pitfalls

- LOCAL RANK PRESERVATION is required (kernel-kernel block of ∂_jρ must vanish); at rank-changing points the SLD-QFIM ≠ Bures metric, QFIM can be discontinuous, and both promise regimes lose their guarantees (Tikhonov SLD stays defined but the bounded-response promise fails).
- M (bounded-response) is an a priori promise — no known oracle procedure certifies it; derive it analytically per model. It can FAIL for commuting Gibbs families whose relative response accumulates over exponentially many configurations.
- The regularized route covers DIAGONAL QFI only — full QGT/QFIM block encoding under bounded response is open.
- e^{x_k} compensation factors: use the exponentially scaled Laguerre recurrence; direct w_k·e^{x_k} underflows for large K.
- QSVT filter must approximate ≈1 at x = 0, not just e^{−t|x|} on [Δ,1] — the derivative can couple support to kernel.
- Frobenius-norm bounds are family-specific; converting through the operator norm costs √N (use rank-aware bounds ‖X‖_F ≤ ‖X‖√rank(X) instead).
- Õ(1/ε⁴) regularized scaling may be improvable (open); whether extra tail-decay promises (e.g. ‖(ρ⁺)²∂_jρ‖_F bounds) recover 1/ε² or near-Heisenberg is open.

## References

- arXiv 2610.24686 — Efficient Quantum Algorithm for Mixed-State Quantum Geometry (Wang, Zhao, Yuan, Cai).
- SLD/QGT conventions: Paris, Int. J. Quantum Inf. (SLD QFIM); Carollo–Uhlmann (QGT, curvature).
- Baselines: Zhang–Yuan (fidelity susceptibility), Zhang (mixed QFI, unitary encoding), Clayton et al. (trapezoidal Lyapunov), Somma et al. (normal-matrix Lyapunov).
- Tools: Gilyén–Su–Low–Wiebe (QSVT/block encodings), Lin (eigenstate filtering), QPE-free amplitude estimation per Lin–Dong (binary-search estimators), Gauss–Laguerre quadrature (Davis–Rabinowitz).
