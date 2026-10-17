---
name: olqs-regret-lower-bound-quantum-tomography
description: OLQS regret lower bound and online quantum tomography.
---

# OLQS Regret Lower Bound & Online Quantum State Tomography

## What This Is

arXiv:2610.21273 (Li & Tseng, NTU, Oct 2026). Quantum generalization of online portfolio selection — Online Learning of Quantum States (OLQS) with logarithmic loss. Establishes that no OLQS algorithm achieves regret O(d^γ log T) for γ<2, proving Exponential Weights and Q-VB-FTRL have optimal polynomial dimension dependence. Yields a sample-optimal (up to polylog) quantum state tomography algorithm and matrix-mean confidence sequences.

## The OLQS Game

- Physicist plays ρ_t ∈ D_d (density matrices); Nature plays PSD A_t with eigenvalues in [0,1]
- Loss: f_t(ρ) = −log tr(A_t ρ); Regret = Σ f_t(ρ_t) − min_ρ Σ f_t(ρ)
- Classical case: diagonal A_t, ρ_t in common basis ⇒ exactly Cover's online portfolio selection (minimax Θ(d log T))
- OLQS regret upper bounds: Exponential Weights O(d² log T), Q-VB-FTRL O(d² log(d+T)), both via vectorization to dim Θ(d²)

## Key Theorems

1. **Regret lower bound (Thm 1.1)**: For T ≫ d² log d, no algorithm achieves O(d^γ log T) for any γ<2. Proof: online-to-batch tomography reduction; a γ<2 algorithm would give estimation error Õ(d^{(1+γ)/2}√(log n/n)), violating Haah et al./Lowe-Nayak Ω(d³/ε²) sample lower bound.
2. **Shrinkage lemma**: ρ̃ = (1−1/n)ρ + I_d/(nd) gives f_t(ρ̃)−f_t(ρ) ≤ log(n/(n−1)) ≤ 1/(n−1). Makes log-loss bounded (≤ log(nd)) and 1-exp-concave on shrunk set D̃_d, enabling Mehta's exp-concave online-to-batch.
3. **Tomography algorithm (Thm 3.3)**: Set A_t = M_{η_t}/tr(M_{η_t}) from POVM outcomes, run EW or Q-VB-FTRL from ρ_1 = I_d/d, output average of shrunk iterates ⇒ ‖ρ̂_n−ρ♮‖₁ = Õ(√(d³ log n/n)) w.p. ≥ 2/3 (4-design POVM, λ_M ≥ 1/(3√d)).
4. **Blum-Kalai extension (Thm 4.5)**: For η-exp-concave losses on convex X with affine-hull dimension p, EW with uniform prior has regret ≤ (1/η) log C(T+p, p). Sharper than (d²−1)(1+log(T+1)) — verified: d=8,T=200 gives 141.9 vs 397.1.
5. **Matrix confidence sequences (Cor 4.6)**: Supermartingale W_t(µ) = Π tr(ξ_t(µ)ρ_t(µ)) with matrix division ξ_t(µ) = µ^{−†/2}ξ_tµ^{−†/2}; Ville's inequality gives C_t = {µ: Regret_t(µ) > log α − L*_t(µ)}. Explicit version uses Regret̄ = log C(t+p, p), p = d²−1 (complex) or d²/2+d/2−1 (real) — no OLQS algorithm implementation needed, membership checked by convex optimization.

## Proof Techniques Worth Reusing

- **Regret→sample-complexity reduction**: combine (a) excess risk controls trace-norm error via POVM norm constant + Pinsker (‖ρ̂−ρ♮‖₁ ≤ (1/λ_M)√(2·ER)), (b) online-to-batch for exp-concave losses, (c) known sample-complexity lower bounds — to transfer hardness across formulations.
- **Shrinkage to maximally mixed state** ρ̃ = (1−1/n)ρ + I/(nd): tames unbounded log-loss near the boundary of D_d at cost O(1/n) — reusable whenever log-likelihoods on density-simplex-like sets blow up at the boundary.
- **Euler/Beta identity** ∫₀¹(1−t^{1/T})^p dt = T·B(T,p+1) = 1/C(T+p,p): volume-of-shrunk-set argument for exp-concave EW regret with exact constants (verified to rel 1e-40; log C(T+p,p) beats p(1+log(T+1)) by ~3x).
- **Realification Φ(M) = [[Re M, Im M],[−Im M, Re M]] / complexification Ψ**: regret-preserving bijection D_{2d}^R ↔ D_d (Goemans-Williamson SDP trick) — lower bound for complex case transfers to real symmetric case.
- **Supermartingale + Ville anytime-valid confidence**: wrap any no-regret log-loss learner into a matrix-mean confidence sequence; membership test = convex program, no learner implementation.

## Numerical Verification (this session, before committing)

- Euler integral: T·B(T,p+1) = 1/C(T+p,p) at dps=80, rel < 1e-40 for (T,p) up to (5000, 255) ✓
- Shrinkage inequality on 2000 random PSD pairs (d=4): max violation 0.00e+00 ✓
- log C(T+p,p) < (d²−1)(1+log(T+1)) in all tested regimes ✓
- Error chain: regret d^γ log n ⇒ trace error O(√(d^{1+γ} log n/n)); γ=2 ⇒ n ~ d³/ε² matches Haah et al. lower bound ✓

## When To Use

- Deriving regret lower bounds for online learning problems connected to statistical estimation (tomography, density estimation)
- Constructing anytime-valid confidence sequences for matrix parameters (covariance, Gram, density matrices) without tuning parameters
- Analyzing exp-concave log-loss algorithms on spectrahedra or density-simplex-like sets
- Quantum state tomography with single-copy non-adaptive POVMs at optimal sample complexity Õ(d³/ε²)

## Limitations

- Lower bound excludes only O(d^γ log T), γ<2 — exact minimax regret (Θ(d² log T)?) remains open
- Confidence-sequence optimality unproven; no shrinkage-rate theory for set sizes
- OLQS game assumes A_t PSD bounded; classical portfolio structure (diagonal) is the only known Θ(d log T) subcase
