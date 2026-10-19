---
name: bosonic-gaussian-classical-capacity
description: Classical capacity of single-mode bosonic Gaussian channels.
category: ai_collection
trigger: bosonic Gaussian channel capacity, Holevo additivity, optical channel classical capacity, phase-sensitive Gaussian capacity, energy-constrained Holevo information, rate-error tradeoff bosonic
arxiv_id: "2610.22308"
---

# Classical Capacity of Single-Mode Bosonic Gaussian Channels

Methodology from arXiv:2610.22308 (Adesso, Lami, Giovannetti, 15 Oct 2026). Proves that the energy-constrained classical capacity of **every** single-mode bosonic Gaussian channel equals its single-use Gaussian Holevo information at **every** input energy — neither non-Gaussian inputs nor entanglement/correlations across channel uses help. Also determines the exact rate–error tradeoff and a strong-converse dichotomy.

## Core Results

1. **Universal Gaussian optimality + additivity**: `C(Φ, N) = χ_G(Φ, N)` for every single-mode Gaussian channel Φ (attenuator, amplifier, phase conjugator, additive-noise; phase-insensitive AND phase-sensitive) at every mean photon number N. Formally: `χ(Φ⊗n, nN) = n·χ_G(Φ, N)` (Corollary 3(i)).
2. **Strong additivity across channels** (Corollary 3(ii)): `χ(Φ⊗Ψ, E) = max_{E1+E2≤E} [χ(Φ,E1) + χ(Ψ,E2)]` for products of single-mode Gaussian channels — correlated encodings give no advantage.
3. **Water-filling energy allocation** (Corollary 3(iii)): among channels receiving nonzero energy, marginal gains `∂χ_G(Φ_j, N_j)` are equalized; with per-mode costs c_j, equalize `∂χ_G/c_j`.
4. **Exact nonzero-error capacity** (Theorem 6): `C_ε(Φ, N) = C(Φ, N/(1−ε))` — allowing average error ε is exactly equivalent to raising the mean-energy argument. Note: this is NOT C(Φ,N)/(1−ε).
5. **Strong-converse dichotomy**: under mean-energy constraint only, no strong converse exists (dilution with vacuum keeps success ≥ N/N′ above capacity). Under a hard per-codeword total-photon-number cutoff ⌊nE⌋, success decays exponentially at every R > C(Φ,E) (Proposition 7), with computable exponents E_filt (energy-filter, always positive) and E_ph (photon-tail, positive for R > U(Φ,E)).
6. **Correlated-noise/memory channels** (Corollary 4): when the quadrature noise blocks Yx, Yp commute, diagonalize into normal modes and apply the single-mode result; capacity of the memory channel follows, and independent squeezed signals in the normal-mode basis are optimal (entanglement between physical uses can still appear when transforming back).

## Canonical Channel Form

Any single-mode Gaussian channel reduces (input rotation + output symplectic unitary) to:

- `X = k·diag(1, ς)`, `Y = y·diag(ξ⁻¹, ξ)` with k = |det X|, 0 < ξ ≤ 1, y ≥ |1−τ|, ς = sign τ
- Attenuators: 0 < τ < 1; amplifiers: τ > 1; conjugators: τ < 0; additive noise: τ = 1. Phase-insensitive ⇔ ξ = 1.

## Verified Computational Formulas (all numerically re-derived and cross-checked; nats)

Entropy of a Gaussian state with symplectic eigenvalue µ ≥ 1:

```
G(µ) = ((µ+1)/2)·ln((µ+1)/2) − ((µ−1)/2)·ln((µ−1)/2)
```

Mean photon number N from diagonal covariance z, w (zw ≥ 1, Heisenberg): `z + w = 4N + 2`.

Average-output entropy with input moments (z, w):

```
h(z, w) = G(√((k·z + y/ξ)·(k·w + y·ξ)))
```

Minimum seed output entropy over feasible squeezed vacua γ_u (u ∈ [1/w, z]):

```
ε(z, w) = h(û, 1/û),  û = min{z, max{1/w, 1/ξ}}
S_min = G(k + y)      [unconstrained optimum at u = 1/ξ]
```

Single-use Gaussian Holevo information (transcendental 1D optimization, eq (10)):

```
χ_G(Φ, N) = max_{z+w=4N+2, zw≥1} [h(z,w) − ε(z,w)]
```

**Threshold energy Nth** (RECOVERED — pdftotext corrupted the printed eq (11); derived from seed-feasibility + output-isotropy and verified to 1e-12 against the numeric optimum):

```
Nth = (ξ⁻¹ − 1)/2 + y·(ξ⁻¹ − ξ)/(4k)
```

For N ≥ Nth the optimum is closed-form (seed γ_{1/ξ}, isotropic average output):

```
χ_G(Φ, N) = G(k·(2N+1) + y·(ξ+ξ⁻¹)/2) − G(k+y)          (eq 12)
```

For 0 < N < Nth the optimum uses seed γ_{u*} with u* < 1/ξ, displacements in ONE quadrature only (squeezing competes with message-carrying displacement energy; solve eq (10) numerically). At N = 0, χ_G = 0.

**Pure-loss specialization sanity check**: with ξ = 1, k = η, y = 1−η ⇒ χ_G = g(ηN) where g(x) = (x+1)ln(x+1) − x·ln x — recovers the classic Giovannetti–Guha–Lloyd–Shapiro capacity.

Above-capacity photon-tail exponent threshold:

```
U(Φ, E) = G(2·N_out(E) + 1) − S_min,   N_out(E) = kE + (y(ξ+ξ⁻¹) + 2k − 2)/4
```
U(Φ,E) = C(Φ,E) iff E ≥ Nth; E_ph > 0 only for R > U, while E_filt > 0 for all R > C.

## Proof Architecture (reusable pattern)

The capacity proof is a two-bound sandwich on Holevo information `χ = S(average output) − Σ p_i S(signal output_i)`:

1. **Upper bound the average-output entropy**: subadditivity + Gaussian maximum-entropy at fixed moments: `S(avg out) ≤ Σ_j h_j(z_j, w_j)` (eq 19).
2. **Lower bound each signal-output entropy via Theorem 1** (sharp, moment-resolved): for ANY (possibly entangled, non-Gaussian) m-mode input,
   `S((Φ1⊗…⊗Φm)(ρ)) ≥ Σ_j ε_j(2⟨x²_j⟩, 2⟨p²_j⟩)` — tight on products of squeezed vacua. Key tools: an affine (tangent-line) lower bound on entropy from the many-pair/mixed-state entanglement inequality (Proposition 8 = Adesso's affine entanglement inequality v3), plus a symplectic-dilation construction (Lemma 9) isolating each quadrature moment. ε is a supremum of affine functions ⇒ jointly convex (eq 18).
3. **Jensen on the ensemble** (ε convex, moments affine in the state) ⇒ Theorem 2: `χ ≤ Σ_j [h_j − ε_j]`, attained by product Gaussian displacement ensembles ⇒ the ensemble problem collapses to a **concave program in the diagonal second moments**.
4. Regularization collapse: the n-use bound reproduces the single-use value ⇒ additivity; water-filling follows from concavity in N_j.
5. **Rate–error converse**: dilution (mix codewords with vacuum at weight N/N′) kills any mean-energy strong converse; under a photon-number cutoff, an energy-filter argument (project onto Fock sectors ≤ ⌊nE⌋) yields the exponential converse; a projection estimate (Proposition 12) transfers the cutoff converse to mean-energy codes, giving C_ε = C(·, N/(1−ε)).

**Reusable insight**: "moment-resolved tangent-line entropy lower bounds + Gaussian max-entropy upper bound + Jensen" is a template for proving Gaussian-optimality/additivity statements in continuous-variable settings; resolving BOTH quadrature moments (not just total energy) is essential below threshold.

## Near-optimal ensemble control (Proposition 5)

With σ* the optimal Gaussian average output and λ = ∂_N C(Φ,N):

```
D(Φ⊗n(ρ) ‖ σ*⊗n) ≤ n·C(Φ,N) + λ·(Tr[ρH_n] − nN)
```

Averaging over an ensemble: `D(σ̄_n ‖ σ*⊗n) ≤ nC − χ_n`. Consequences: the capacity-achieving average output is **unique**; Holevo deficit bounds trace distance via Pinsker (√(Δχ/2)); per-use deficit → vanishing relative entropy per use.

## References

- arXiv:2610.22308 — Adesso, Lami, Giovannetti (2026)
- Builds on: Gaussian minimium-output-entropy theorems (Giovannetti et al.), phase-sensitive low-energy optimisation (Refs 13–14), Adesso's affine entanglement inequality (v3 Theorem 2), Ji's single-use result.
- Numerically verified: G(µ)↔thermal entropy (1e-12), pure-loss reduction to g(ηN) (exact), û closed-form minimizer vs brute force (1e-13), χ_G concavity in N, Nth recovery (1e-12 at transition), eq(12)↔eq(10) equality above Nth (2e-16), U(Φ,E)=C(Φ,E) for E≥Nth (exact).
