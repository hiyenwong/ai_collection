---
name: flux-markov-blanket-gray-scott-fep-test
description: Use when auditing FEP blanket claims. Gray-Scott flux fails.
category: neuroscience
trigger: free energy principle test, Markov blanket conditional independence, Gray-Scott spots, active inference falsification, reaction-diffusion organisms, collider conditioning
---

# Flux-Defined Markov Blanket Test in Gray–Scott Self-Replicating Spots

**Source**: "Does a Flux-Defined Markov Blanket Screen Self-Replicating Gray–Scott Spots? A Computational Test of a Blanket Condition from the Free Energy Principle" — John E. Pearson, arXiv:2610.27235 (Oct 2026). Code: github.com/johnepearson/GS_FEP (solvers, individuation/lineage pipeline, CMI estimator, all figures).

## Core Finding

A direct falsification test of the free energy principle's central mathematical claim — that persisting, self-replicating structures possess Markov blankets rendering internal and external states conditionally independent. In Gray–Scott self-replicating spots (the most organism-like compact structures a fully specified PDE produces), the claim **fails for every boundary-defined blanket variable tested**:

- Flux blanket (Φu, Φv) removes only ~40% of the marginal linear interior–exterior dependence (partial r −0.19 vs marginal r −0.25, N=566,967).
- Nonlinearly, conditioning on flux **increases** dependence ~80% (CMI 0.137 nats vs unconditioned MI 0.075 nats; 23.5 null SDs) — flux behaves as a **collider** (joint downstream function of both sides), not a mediating state.
- Boundary concentration (a genuine single-side state) conditions the opposite way (0.076→0.061 nats, +19.6% screened) but still nowhere near screening.
- A band of the surrounding field ~1 organism radius thick (w=24 px, R≈21 px) does screen (<0.01 nats) — but placebo disks in empty field screen too (16 px): thick-band screening is generic short-range-field physics, not evidence of inference/organismhood.

## Test Protocol (reusable)

### 1. System
Gray–Scott: ∂u/∂t = Du∇²u − uv² + F(1−u); ∂v/∂t = Dv∇²v + uv² − (F+k)v. Chaotic self-replication regime: Du=2e−5, Dv=1e−5, F=0.018, k=0.055 (Pearson class ε). 1024×1024 pseudo-spectral, first-order ETD; ~20 px per organism radius. Background relaxation time τ = 1/(F+k) ≈ 13.7.

### 2. Individuation (4 steps)
(1) Otsu threshold on v, recomputed per frame (v level drifts); (2) markers = local maxima of v ≥24 px apart; (3) inverted watershed with periodic padding; (4) merge raw regions whose equivalent-radius circles overlap, iterate. Interior I = mean v in core shrunk to ≥50% of radius from boundary; Exterior E = mean v in 24-px ring just outside. Robustness: repeat key test with fixed-threshold connected components (no watershed machinery) — violation survives.

### 3. Blanket variable
Net diffusive flux across the boundary via the divergence theorem, ΦX = −DX ∮ ∇²X dA (discrete Laplacian). Φu and Φv are nearly collinear (r≈−0.98) → condition on PC1 of the standardized pair (conservative; joint 2-D conditioning lands outside single-flux range = further collider signature).

### 4. Friston's three criteria
- **(A) Timescale separation**: positional measure ρ = v_centroid·τ/R, median 0.032 over 93,722 transitions (organisms move ~3% of radius per relaxation time); boundary outline correlation 0.916 between matched frames. Holds by direct measure. Autocorr 1/e lags: I≈48, E≈62, fluxes 61/58 — blanket slower than I but NOT slower than E → strict form unresolved.
- **(B) Directed exchange asymmetry**: Φu<0 (substrate in) 99.99%, Φv>0 (product out) 99.96%. Nearly a tautology of segmentation (high-v region ⇒ depleted u ⇒ inward diffusion) — coherent labeling, no confirmation of directed dependency.
- **(C) Conditional independence I ⊥ E | B** — the load-bearing criterion. Fails (see above).

### 5. Estimator stack
- Linear: partial correlation of OLS residuals after regressing I and E on (1, Φ_PC1). Report screened fraction = 1 − r²_partial/r²_marginal.
- Nonlinear: conditional mutual information via Frenzel–Pompe kNN estimator (kNN=5), **z-score all inputs first** (estimator is scale-sensitive: flux ~1e−4 vs concentrations ~1e−1).
- Null: local permutation among nearest neighbors in B-space (Runge 2018 style); validate null calibration on synthetic data with constructed independence (mean −0.18, SD 0.97, ~4–5% false-positive rate at 1.645).
- Non-independence of same-frame instances → frame-cluster bootstrap (resample whole frames, 2000 replicates).

### 6. DPI licensing of coarse-graining
Two-sided data processing inequality: MI(X;Y|Z) ≥ MI(F(X);G(Y)|Z). A positive CMI on low-dim summaries I,E is a **lower bound** on richer descriptions — a positive finding cannot be a coarsening artifact. (Caveat: masks must not depend on the values; conditioning on B itself gets no protection.)

## Collider Diagnosis Pattern (generalizable)

When the proposed blanket variable is a **joint downstream function of both sides** (flux depends on concentrations inside AND outside via Fick's law), conditioning on it can INFLATE dependence instead of screening it. Diagnostic: condition instead on a genuine single-side state (here boundary concentration). **Opposite-direction effects confirm collider structure** — flux raised MI +80%, boundary concentration lowered it ~20%. Rule: never accept a blanket variable that is computed from both sides of its own boundary.

## Robustness / Alternative-Explanation Checklist
All were tested and none explains the violation away:
- Local crowding: partial r essentially unchanged
- Whole-domain confound: frame fixed effects ≤3%
- Between-organism mixture: lineage fixed-effects r=−0.262, covariance entirely within-lineage
- Life-cycle stage: coupling builds with age (youngest third r=−0.116; older thirds ~3.5× stronger) — not inherited
- Size/shape: marginal −0.255 → −0.252 controlling radius+eccentricity (adding them to the blanket flips sign → ill-conditioning, radius shares 70% variance with flux PC1)
- Individuation artifact: non-watershed connected-components replication; unmerged-only organisms r=−0.188
- Spatial decay: partial r negative at ALL distances out to 19–20 radii; concentrated within ~1 radius but never zero

## Free-Energy Falsifiability Rules

1. **A fit counts only if it could have failed.** A flexible generative model fit to almost any smooth, roughly Gaussian system finds a consistent parameterization — computing a well-behaved variational free energy ℱ is not evidence of inference.
2. The life-cycle signature (ℱ rising before division, falling ~3× at division) IS recovered (template-deviation energy and linear-Gaussian Friston ℱ correlate r=0.934 over 695 confirmed divisions) — but both are functions of the same measured field, ~1/3 of shared variance is organism size, and the dynamics never reference I, E, or Φ. It is flux statistics, not surprise.
3. Chemical free energy is not well-posed when the autocatalytic step is irreversible (affinity diverges as −ln kr); only the reaction-rate prefactor uv² serves as a small-kr leading-order stand-in, and its agreement with ℱ is a conservation identity (inward u flux = consumption − feed, r=0.97–0.99).
4. Do not re-partition post hoc to get the best-looking result (Raja et al. 2021 "Markov blanket trick"); fix the partition by the natural individuation, report the failure.

## Scope Limits (what the test does NOT rule out)
- I,E are low-dimensional summaries (covered by DPI lower-bound logic); no claim about arbitrary full-state partitions
- Single-instant conditioning; history-based blankets untested
- Deterministic dynamics vs Friston's assumed stochastic steady-state density
- One parameter regime of one model; exact screening is not required for variational free energy to bound surprisal — only for the belief-encoding (inferential) reading

## Key Numbers
| Quantity | Value |
|---|---|
| Marginal r(I,E) | −0.245 (ensemble), −0.255 (trajectory) |
| Partial r given flux PC1 | −0.189 / −0.198 (~40% screened) |
| CMI(I;E|flux), kNN | 0.137 nats (23.5 SDs over null) |
| Unconditioned MI(I;E) | 0.075 nats → conditioning inflates ~80% |
| CMI given boundary concentration | 0.061 nats (+19.6% screened) |
| Thick-band screening onset | w≈24 px ≈ 1 organism radius, CMI ≤0.009 nats |
| Placebo-disk screening | 16 px — screening belongs to the field, not the organism |

## Position in the Critical Literature
Sharpens Raja et al. (2021) "Markov blanket trick": the strict conditional-independence sense IS directly testable and fails here. Compatible with Aguilera et al. (2022) — sparse thin partitions are not generically blankets — and with the finite-thickness reply: blankets of finite thickness are what local coupling produces, but then they carry no inferential distinction. Distinguishes Pearl-style statistical blankets (tested) from Friston's stronger dynamical blankets.