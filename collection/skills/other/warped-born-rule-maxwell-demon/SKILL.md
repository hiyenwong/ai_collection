---
name: warped-born-rule-maxwell-demon
description: Use when analyzing nonlinear Born rules or replica-truncation bias. Warped-rule monitoring.
category: quantum
---

# Warped Born Rule Turns Observer into Maxwell's Demon

**Paper**: "A Warped Born Rule Turns an Observer into a Maxwell's Demon" (arXiv: 2610.13936) — Olumakinde Ogunnaike (UC Berkeley).

## Core Claim

Replace the Born rule `p(m) ∝ ∥Pm|ψ⟩∥²` by a warped rule `p_b(m) ∝ ∥Pm|ψ⟩∥^{2b}` (post-measurement state unchanged). In many-body systems with conserved particle number under repeated local occupation measurements, the warping induces an **entropic bias over measurement histories** whose sign is controlled by b−1:

- **b > 1** sharpens unequal outcome probabilities → suppresses kinetic activity → gas collects into nearly frozen, phase-separated dense domains (a many-body Maxwell's demon: observation extracts entropy from a closed system).
- **b < 1** flattens probabilities → enhances motion → scours out long-wavelength fluctuations → **hyperuniform gas** (S(q→0) → 0).

This is not a hypothetical deformation: the **replica trick** with common measurement records on n copies produces exactly the b = n warped rule (PB(m)ⁿ → normalized), so fixed-integer replica calculations of monitored number-conserving systems can select qualitatively different dynamics from the Born-weighted n→1 limit.

## Mechanism

1. **Surprisal tilt**: with ϵ = b−1, globally normalized record weight `P_b^g(m) = P_B(m)·e^{−ϵI} / Z_b`, where I = −log P_B(m) is surprisal. Positive ϵ favors less-surprising histories. Z_b acts as a partition function over records; F(b) = −log Z_b with ∂F/∂b = E[I]. Record entropy obeys **dH_b/db = −b·Var_b(I)** — increasing b strictly removes entropy from the record distribution.
2. **Sequential normalization** (used in numerics): odds per event become [p_j(a)/p_j(c)]^b; leading correction `log(P_seq/P_B) = −ϵ·Σ_j[−log p_j(m_j) − H(p_j)] + O(ϵ²)` — each outcome's surprisal is compared to the expected information at that event. The ensemble-averaged cost is a sum of conditional relative entropies.
3. **Activity-biased SEP mapping** (the solvable model): chain with number-conserving unitaries on neighboring sites + single-endpoint measurement = symmetric exclusion process. Exchange probability r; α = (1−r)^b, β = r^b; matching to activity-biased SEP weight e^{−s_E·K} (K = number of exchanges) gives
   **s_E = log((1−α)/β) = (b−1)·H(r)/r + O((b−1)²)**
   — the activity field has the same sign as b−1. Packed configurations offer fewer uncertain readouts, so b>1 entropically favors dense domains with no attractive interaction.
4. **Hydrodynamics**: macroscopic action `A = ∫dτdx [(j+∂xρ)²/(2σ(ρ)) + ζσ(ρ)]` with σ(ρ) = 2ρ(1−ρ) mobility, ζ = s_E·L². Uniform profile costs O(ζ); two interfaces cost O(√ζ) → **segregation wins at large positive ζ**. For s_E < 0 the same term suppresses density inhomogeneity → hyperuniformity.
5. **Structure factor diagnostic**:
   `S_occ(q) ≃ √(χ₀|q| / (q² − 8s_E χ₀))`, χ₀ = ρ₀(1−ρ₀). Born gas (s_E=0): finite S(q→0). Hyperuniform (s_E<0): S(q→0)→0. Segregated (s_E>0): S(2π/L) ∝ L.

## Numerics (MPS, sequential normalized pure-state histories)

Open half-filled chains L = 20–48, discrete-time projective-measurement circuits: b=2 enhances small-q spectrum (clustering), b=1 flat, b=0.5 suppressed small-q (hyperuniform). History-averaged density-matrix polarization M²z = L⁻¹Σ⟨Sᵢz⟩² stays finite for b=2, relaxes to 0 for b=1 — complementary clustering evidence surviving branch-summing.

## Replica-Trick Consequence (the practical warning)

Evolving n copies of the unnormalized trajectory density matrix with a **common measurement record**, then normalizing by the common-record trace, yields the 2n-Born rule. Example: subsystem Rényi moment `Σ_m P_m^{g,n}·Tr(ϱ_A,mⁿ) / Σ_m (Tr ϱ̃_m)ⁿ` — fixed integer n>1 sits on the positive-bias side, so a density-ordering saddle may reflect **biased histories** rather than true monitored-gas dynamics with Born weighting. Bias compounds only when density memory survives between observations: suppression when **Γ·t_diff ≲ 1, i.e. Γ ≲ D/L²** — equal conditional branch weights (e.g. exactly half filling, equilibrated readouts) remove the bias entirely. Large-system limits and the n→1 limit must be controlled together (cf. charge-sharpening field theory, Barratt et al.; quantum-tree phase boundaries, Feng et al.).

## When to Use

- Evaluating claims from **fixed-replica-number** calculations of monitored number-conserving systems (charge/spin sharpening, purification transitions) — check whether conclusions survive the n→1 Born limit.
- Analyzing generalized/nonlinear Born rules, postselection, or warped-measurement ensembles in many-body settings.
- Designing monitored-circuit numerics: use S(q) small-q behavior + M²z polarization as phase diagnostics; report the normalization convention (global vs sequential) explicitly.
- Statistical-mechanics analogies: observation-cost as entropy extraction (Landauer/Bennett demon accounting), activity-biased ensembles (s_E field), fluctuating hydrodynamics with mobility σ(ρ).

## Pitfalls

- Two inequivalent normalizations (global vs sequential) give different history ensembles; the local bias source is shared but collective dynamics differ. State which one you use.
- The demon's cost is informational (relative entropy), not physical heat — no reservoir temperature is assigned.
- Exact SEP laws S(q) ~ |q|, S(2π/L) ~ L need not carry to general protocols; the qualitative signatures (vanishing vs divergent small-q weight) are the robust diagnostics.
- Bias vanishes at exactly half filling with equilibrated readouts — absence of effect there does not disprove warping.
- Aaronson's few-body pathologies (postselection power, signaling, purification/tomography failures) apply to nonlinear Born rules generally; this paper covers the many-body/collective regime.

## Key References

Aaronson (island in theory-space, quant-ph/0401062); Galley & Masanes (Born-rule alternatives classification); Bao–Choi–Altman (monitored circuit transitions); Barratt et al. (charge sharpening field theory, PRL 129, 120604); Feng et al. (quantum trees, Quantum 9, 1692); Bennett (thermodynamics of computation).
