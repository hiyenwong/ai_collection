---
name: reciprocity-mechanical-network-learning-floor
description: Symmetry sets untrainable error floors in physical nets.
category: ai_collection
trigger_words: reciprocity, Maxwell-Betti, mechanical network learning, physical learning, error floor, trainable metamaterial, spring network, compliance matrix, non-reciprocal coupling, odd coupling, wedge selection, sensor-actuator layout, directed response, robotic metamaterial
---

# Reciprocity Can Halve What a Mechanical Network Can Learn

Methodology from "Reciprocity can halve what a mechanical network can learn" (arXiv:2609.04169v4, cond-mat.soft, 25 Sep 2026; Thai-Son Vu, Hoang-Giang Nguyen, Quoc-Bao Nguyen, Sengaloun Keoalounxay, Bao-Viet Tran — Hanoi University of Civil Engineering et al.).

## When to Use
- Designing or analyzing trainable physical networks (spring/elastic, resistor, flow networks) where input and output terminals OVERLAP — predicting achievable vs impossible targets BEFORE training
- Computing error floors for in-material/physical learning hardware (directed aging, contrastive local rules, in-situ backprop, robotic metamaterials)
- Deciding sensor-actuator layout (full vs partial overlap) and whether non-reciprocal (odd-coupling/gyrator-like) elements are needed
- Theoretical analysis of learnability limits under symmetry constraints (applies to any symmetric response operator perturbed symmetrically — 2D/3D elasticity, resistor networks, flow networks, complex-symmetric operators)

## Core Law (Theorem 1: Capacity under Maxwell-Betti)
A passive, reciprocal, linear network (symmetric invertible K_f) driven by forces/currents at S (m_S terminals) and read at T (m_T terminals), with p = |S ∩ T| SHARED degrees of freedom, has its reachable response blocks inside a linear subspace of codimension **p(p−1)/2** — regardless of size, topology, or parameter count:
```
rank ∂R/∂k ≤ min( n_b ,  m_T·m_S − p(p−1)/2 )
```
- Full overlap (T=S, p=m): reachable dimension ≤ m(m+1)/2, so a fraction (m−1)/(2m) → **1/2 of the target space is unreachable** — hence "halve"
- The containment is GLOBAL and derivative-free: R(k) ∈ S_P for every admissible k (not just tangent space)
- Adding bonds CANNOT repair the symmetry branch (unlike the n_b bond-count branch)
- Holds with only symmetry + invertibility; positive definiteness not needed for Theorems 1-2

## Error Floor (Theorem 2 — compute BEFORE training)
For target response block R*, every training run satisfies:
```
‖R(k) − R*‖_F  ≥  ‖½(B − Bᵀ)‖_F
```
where B = R* restricted to the shared degrees of freedom. **The floor is the antisymmetric part of the target's shared block** — a number from the target alone.

Theorem 3 (with passivity, K_f ≻ 0): floor = √[ ¼‖B−Bᵀ‖²_F + Σᵢ min(λᵢ, 0)² ] where λᵢ are eigenvalues of the symmetric part B_s — passivity adds a PSD-cone term (shared block must be symmetric positive-definite).

## Verified: Learning Rules Stop ON the Floor
- Levenberg–Marquardt on log-stiffnesses, exact Jacobian, random independent starts: reaches within 0.1% of floor in **142/144** runs (forbidden targets with reachable symmetric part)
- **Contrastive coupled learning** (bond-local update: Δk_b ∝ Σⱼ[(e^free_b)² − (e^nudged_b)²], no Jacobian/no global loss gradient): median error/floor = 1.000001, **22/24** within 0.1% — a material could plausibly implement it, and it still cannot beat the floor
- Controls: allowed (SP ∩ reachable) perturbations → error → 0; odd couplings ON → error → 0 (floor disappears)

## Escape Route: Odd (Non-Reciprocal) Couplings (Theorem 16)
Odd couplings a_b on bonds add antisymmetric stiffness contributions. Each bond contributes a **wedge** z_b|_P ∧ w_b|_P (2-form in Λ²R^p) where w_b = Cq_b, z_b = Cs_b are passive response fields:
```
Π_AP im ∂R/∂(k,a) = span{ z_b ∧ w_b : b } ⊆ Λ²R^p
```
- Odd branch recovers ALL lost directions ⟺ the n_b wedges span Λ²R^p
- **Minimum count: p(p−1)/2 odd bonds** must contribute (wedges are single 2-form elements); at fixed k, three odd bonds can beat the count (at 40-node, m=p=5: 3 bonds realize 10⁻² relative antisymmetric block in 9/9 pairs, but not every triple works)
- **Selection BEFORE building**: vectorize each wedge's strictly-upper entries → wedge matrix W → **pivoted QR** selects p(p−1)/2 best-conditioned bonds (σ_min reports conditioning; rank-greedy is insufficient — near-parallel wedges fool it). Pivoted QR hits the optimal σ_min in median ratio 0.93 vs brute force
- 2D cancellation: bond direction/length drop out (SO(2) acts trivially on Λ²R²) — only which node pair a bond joins matters, conjugated by the compliance C; in 3D the transverse direction sweeps a 2-form family

## Price of Non-Reciprocity (Prop 18, Cor 19)
Any network realizing target B has non-reciprocity η(K) ≥ η(B) (ratio of odd to even parts, congruence-normalized) — the target itself bounds from below how non-reciprocal the hardware must be. Least-norm odd coupling: ‖a*‖₂ ≤ √2·‖B_a‖_F / σ_min(W) — maximizing σ_min of selected wedges = column-subset selection (strong rank-revealing QR approximates the optimum).

## Imposed-Displacement Drive (Theorem 10-11 — weaker law for the common hardware mode)
Most physical-learning hardware prescribes displacements, not forces. Reciprocity survives as:
- Exact balance: forward transmission / driving-point compliance at input = reverse transmission / its driving-point compliance (4 measurable scalars, testable on a black box)
- Rank cap on off-diagonal entries: ≤ min(n_b, ½(p−1)(p+2)) — at least (p−1)(p−2)/2 below the p(p−1) free entries
- Spectral inequality (Thm 11): **no symmetric positive-definite chain can meet both targets** of the published Du et al. robotic metamaterial (imposed-angle task) — their DOF count misses this entirely

## Layout Law (Prop 21)
- Fixed number of accessed DOF (each drivable AND readable), bond count not binding: **full overlap is optimal**, approaching factor 2
- Fixed sensor+actuator budget: full overlap is NOT best — split the terminals

## Task-List Form (Sec 3.4, Cor 8 — for labs, not idealized blocks)
Reciprocity charges a list of single drive–read tasks **only for pairs instrumented in BOTH directions**. A shared terminal alone costs nothing; a reversed pair is what pays. All 19 published physical-learning layouts tabulated: p = 0, deficit = 0 — no published force/current-driven in-place layout pays the price; a force-driven layout asking one pair to respond differently in two directions will.

## Decision Procedure (apply this pipeline)
```
1. Identify shared terminals P = S ∩ T, count p
2. Extract target's shared block B; floor₁ = ½‖B−Bᵀ‖_F (antisymmetric part)
3. If passive: add passivity term from negative eigenvalues of sym(B)
4. floor > tolerance? → need p(p−1)/2 odd couplings:
   a. Solve passive network: C = K_f⁻¹, compute w_b = Cq_b, z_b = Cs_b per bond
   b. Build wedge matrix W (vec of strictly-upper 2-form entries per bond)
   c. Pivoted QR on W → select bonds; check σ_min conditioning
   d. Budget: η(K) ≥ η(B) — check hardware can deliver required non-reciprocity
5. Imposed-displacement drive? Use Thm 10 balance test (4 terminal scalars) instead of block codimension
6. Task list only charges reversed pairs — audit which pairs you actually instrument bidirectionally
```

## Concrete Scale
16-node network, 3-task list + ONE reversed task → floor = 9.9% of target norm; one odd bond chosen in advance (rank test) removes it. Exact realization: Newton from a=0 at fixed k reaches prescribed antisymmetric block (10⁻⁴→10⁻¹ relative) in 336/336 configurations, ‖a‖/‖k₀‖ ≈ 2ε median.

## Scope & Limits
- Linear response regime (tangent response about finitely deformed states included via Sec 3.3)
- Floor is a LOWER bound; tight only when target's symmetric part is reachable (Sec 6 measures the gap; on arbitrary targets the passivity term accounts for most of it)
- Joint (k,a) solve outside a=0 neighborhood: symmetric part of K can lose positive definiteness at large odd coupling (115/336 at ε=10⁻¹) — Remark 11 governs the safe neighborhood
- Wedge-spanning is MEASURED (251/251 spanning configs), not proved generically; rationalization argument plausible but unverified

## Related Skills
- `mechanical-field-networks` — MFN learning (this skill explains WHY some MFN targets are unreachable)
- `kirchhoff-inspired-neural-networks` — KINN state-variable physical networks
- `thermodynamic-networks-computation` — autonomous physical learning systems
- `physics-guided-neural-network` — adjacent physical-learning theory
