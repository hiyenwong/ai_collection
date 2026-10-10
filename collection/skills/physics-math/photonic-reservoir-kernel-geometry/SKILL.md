---
name: photonic-reservoir-kernel-geometry
description: Use when deciding if quantum/photonic interference helps a learning task. Pre-experimental kernel geometry + alignment test.
category: quantum
---

# Kernel Geometry as a Pre-Experimental Test for Photonic Reservoir Computing

**Source**: arXiv:2610.11360 (Kar & Babu H, IIIT Dharwad, quant-ph/cs.CE, 2026-10-08) — task-independent resolution of whether multi-photon interference is a learning resource, reconciling 4 conflicting experiments (Joly, Di Bartolo, Rambach, Yin).

## Core Thesis

**Geometry bounds what is learnable; alignment decides what is learned.** Quantum advantage claims in reservoir computing are task-dependent and thus incomparable across platforms. The fix: characterize the *feature maps* (kernels) themselves before running any task. Both quantities (geometric difference g, kernel-target alignment A) are computable from data + circuit alone.

## The Two Kernels

Boson-sampling reservoir: input x ∈ [0,1]^d encoded as phases between two Haar-random M×M interferometers U(x) = U_res Φ(x) U_pre; N photons in, collision-free output distribution = feature vector of dim D = C(M,N).

- **K_Q (indistinguishable/quantum)**: P_Q(t|x) = |Per U(x)[s,t]|² — signed amplitudes interfere
- **K_C (distinguishable/classical)**: P_C(t|x) = Per |U(x)[s,t]|² — nonnegative permanents, no cancellation
- Both are degree-2N functions of input phases: any learning difference comes from **sign structure**, not nonlinearity order.
- Partial distinguishability via overlap matrix S_ij = ⟨φ_i|φ_j⟩, uniform S_ij = I, HOM visibility V = I².

## Geometric Separation g (the resource)

g = √λ_max(K_Q (K_C + ε1)^(−1/2) K_Q)^(1/2) — geometric difference; g > 1 certifies tasks exist where classical readout is disadvantaged (NOT that any particular task benefits).

Key properties:
- **Spectral broadening**: K_Q spreads the same trace across ~2× effective dimensions (61 vs 33 dims to 90% trace at M=12, N=3, n=100). K_C's smallest eigenvalue sits an order of magnitude above K_Q's. Mechanism: signed amplitudes cancel, decorrelating outcome fluctuations → variance spreads across directions.
- **Superlinear dial**: g−1 grows superlinearly with V (effective exponent 1.06–1.22). At N=2 exactly linear: g(V)−1 = (s/2)V + O(V²), s = λ_max of cross-statistics matrix (first-order perturbation theory, pairwise-transposition dominance).
- **Hardware retention**: R(V) = (g(V)−1)/(g(1)−1) = 80.3% at V=0.864 (Rambach-class processor), 95.8% at V=0.972. Decoherence is smooth attenuation, not a threshold.
- **Sampling accessible**: advantage stable from S=10³ to 10⁶ shots; S=3×10⁴ (Rambach's per-image budget) matches exact arithmetic (+0.244±0.112).
- **Conditioning caveat**: g·λ_min(K_C) ≈ const across n (27-fold g range) — g is attained in tail directions; compare g only at matched n. Task-level advantage is immune: g drops 5.6× between configs while advantage unchanged (+0.248 vs +0.207).
- **Does NOT grow with system size**: advantage constant across 25-fold feature-dim range at matched M, n — alignment, not Hilbert size, governs learnability.
- **Photonic-specific**: Random Fourier Features matched in D and preprocessing do NOT recover the designed-task advantage; the Q-vs-C photonic separation is what interference contributes (both photonic kernels beat RFF on adversarial tasks: 0.883/0.878 vs 0.439).

## Learnability Gate: Kernel-Target Alignment

A(K,y) = ⟨K, yyᵀ⟩_F / (‖K‖_F ‖y‖²). Adversarial task = leading generalized eigenvector of K_Q(K_C+ε1)^(−1/2)K_Q^(1/2), binarized at median (OOS variant: direction from train split only; reverse construction favors K_C — machinery carries no bias).

| Setting | ∆A = A_Q−A_C | Accuracy gap | p |
|---|---|---|---|
| Designed (Q-adv, OOS) | +0.036 | **+0.222±0.046** | <10⁻⁴ |
| Radial | +0.017 | +0.041±0.027 | 0.001 |
| Threshold | +0.011 | +0.032±0.041 | 0.041 |
| Linear combination | +0.014 | +0.024±0.036 | 0.082 |
| Checkerboard | +0.017 | −0.006±0.024 | 0.501 |
| C-adversarial | neg. | −0.048 | — |

Natural-task advantage is an order of magnitude below designed tasks; fine-grained natural ordering unresolved at these n (9/13 sign predictions in pre-registered battery; ρ=0.027). **Gating supported at extremes; graded interior is a resolution limit.**

## Convexity Theorem (interior optima impossible)

s_K(V)(y) is **convex in V for every labeling**: cross-statistics term obeys s_X ≤ √(s_Q s_C) (Cauchy-Schwarz on embeddings), so quadratic coefficient ≥ (√s_Q − √s_C)² ≥ 0. Interior optima in distinguishability are provably non-geometric — any reported interior optimum must be readout-level or noise (Joly's reported optimum would need ~800 draws at 1σ; they used 100).

## Reconciling the Experimental Record

- **Joly (fibre, N=2, MNIST)**: easiest binary task, no alignment + rank-limited features → geometry present, unexploited. Blind prediction: g=4.4±0.5 but ∆A=+0.008 → predicted effect (+0.015) < realization spread (±0.017) — reproduces their null to within 10%.
- **Di Bartolo (4-mode PIC, temporal)**: task nonlinearity spans the alignment axis; linear-recall null is the control case.
- **Rambach (N=3 quantum processor)**: geometry improves *trainability*; *generalization* gated by weak alignment of natural tasks (train-only effect explained).
- **Yin (designed tasks)**: designed alignment realizes the separation.

## Pre-Experimental Protocol (Box 1 — the reusable procedure)

Given candidate task family + system params (M, N, d):
1. **Estimate kernels** on n~100 unlabeled pilot inputs (O(n) circuit evals, S≈3×10⁴ shots suffice in hardware).
2. **Compute g** with ε ≪ λ_min(K_C); compare only at matched n.
3. **Compute alignment** A_Q, A_C per candidate labeling family — labels are cheap to enumerate, kernels computed once.
4. **Decision rule**: interference is worth hardware cost only if g is large AND A_Q > A_C on the task family. Otherwise high-visibility sources offer no expected benefit.

Protocol is classically computable up to the #P-hard permanent wall (engineering regime, N≤~4 sim-able; N≥50 out of reach).

## Reusable Rules

1. Task-dependent accuracy cannot adjudicate resource claims across platforms — compute task-independent kernel geometry first.
2. Expressivity (geometry) and generalization (alignment) are separate axes; a quantum resource can improve one without the other.
3. Uniform loss cancels in renormalized post-selected distributions; mode-dependent loss = effective interferometer — neither degrades g.
4. Convexity in the resource dial: any interior optimum claim warrants a readout-level or noise investigation.
5. Blind prospective tests (compute predictions before seeing results) are the validation standard for reconciliation frameworks.

## Related Skills

- `deep-photonic-reservoir-computing` — ultrafast photonic reservoir architecture
- `photonic-variational-trainability` — trainability of photonic VQAs
- `ml-quantum-teleportation`, `quantum-photonic-reservoir-computing` — adjacent QRC methodology
