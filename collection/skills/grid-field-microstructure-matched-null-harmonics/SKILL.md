---
name: grid-field-microstructure-matched-null-harmonics
description: Matched-null harmonic analysis shows single grid fields lack local sixfold symmetry.
category: ai_collection
---

# Grid-Cell Firing Fields Lack Local Sixfold Symmetry — Matched-Null Harmonic Microstructure Analysis

**Source**: arXiv:2609.31145, Anian Kerscher (LMU Munich / Bernstein Center Munich), q-bio.NC, 25 Sep 2026

## Core Finding (negative result with strong methodological value)

Global hexagonal lattice symmetry of grid-cell firing and the **local angular structure of individual firing fields are dissociated**. After correcting global elliptic lattice deformation, single grid fields show *no reliable local sixfold angular modulation* beyond what matched circular fields produce (Exp vs Circ: p=0.279, N=137 cells), while the analysis *is* sensitive to imposed sixfold structure (Exp vs Sixfold-prior: p=5×10⁻⁵, and monotonic separation with β). Individual fields behave as approximately radially symmetric bumps — validating the standard modeling assumption of radially symmetric tuning profiles on hexagonal lattices, and constraining continuous-attractor (Burak–Fiete) models: a globally periodic CAN shows the same global/local dissociation, dominated by low-order (P2) angular structure, not selective local sixfold enhancement.

## The Methodological Pattern: Per-Cell Matched-Null Harmonic Analysis

The reusable core is a **null-referenced inference pipeline** for detecting weak angular structure in noisy neural data — each experimental cell is compared against simulations that preserve *every nuisance parameter* of that cell:

1. **Rate-map construction**: `r(x,y) = (G_σs ∗ S)/(G_σo ∗ O)` — Gaussian-smoothed spike map / occupancy map, with σs=5cm > σo=4cm (spikes sparser than occupancy), boundary-support normalization, and occupancy clipping at the 1st percentile to stabilize sparse regions.
2. **Grid-scale + destretching**: λ from spatial ACF first-ring peaks (6 peaks, mean distance). Fit ellipse to the 6 peaks (direct least-squares conic fit); affine-transform the ellipse to a circle → "destretched" coordinates. This removes global elliptic deformation that would otherwise inject spurious *low-order* (P2) angular harmonics.
3. **Robust field-center detection**: Self-Organized Grid Clustering (SOGC) — mean-shift-like mode-seeking on spike density with (i) kernel-weighted attraction + (ii) weak isotropic repulsion at field scale (no lattice prior imposed) — then **anchor-free lattice-constrained filtering**: fit hexagonal lattice (spacing fixed to λ, optimize orientation+phase), keep only candidate centers near lattice sites (centers stay at empirical locations; lattice fit only *rejects* inconsistent candidates).
4. **Annular angular profiles**: extract firing rate in overlapping circular rings around the field center, radius normalized by grid scale (ρrel = ρ/λ), analysis window 0.1λ–0.4λ (inner field, avoiding center sampling instability and neighbor-field rise at >0.5λ).
5. **Harmonic regression per annulus**: normalize profile by circular mean, fit `r̃(θ) = a_k cos(kθ) + b_k sin(kθ) + c` for k=2..11 (k=1 excluded — too sensitive to center displacement; k≥12 below smoothing scale). Harmonic power `P_k = a_k² + b_k²`. **Primary statistic: sixfold power fraction** `f6 = P6 / Σ_{k=2..11} P_k` — a compositional metric isolating sixfold *specificity* against broadband angular power.
6. **Matched null simulations (the key step)**: per-cell parameters extracted (spike count, occupancy map, destretched λ, affine transform, field location, fitted field width σ̂) → simulate spikes under two local priors:
   - **Circular prior (β=0)**: isotropic Gaussian fields `exp(−ρ²/2σ²)` on a hexagonal lattice (spacing λ, orientation 16°).
   - **Sixfold prior (β>0)**: Gaussian × sixfold von-Mises modulation `[1 + β(ã(θ)−1)]₊` (rectified, unit mean; implemented as 3 von-Mises at κ=2.1 separated by 120°).
   Simulations pass through the *identical* preprocessing pipeline → null distributions per cell per radius.
7. **Null-referenced inference**: per-cell Z-scores of f6(ρrel) against each reference; window summary = AUC(Z) over 0.1–0.4 λrel; population test = two-sided sign-flip permutation (20,000 perms).
8. **Sensitivity battery** (preregistered logic): harmonic leave-one-out (recompute f6 omitting each P_j from denominator — guards the compositional metric), complementary R6² metric, radial-window sweep, smoothing-bandwidth sweep, noise-level sweep, burst-vs-tonic spike split, phase coherence `V(ρ) = Σw_i e^{iφ_i}/Σw_i` with power weights w_i=P6.

## Key Numbers

- 137/166 cells (single module, Gardner et al. 2022 data, ~140 min open-field 150×150 cm); median rate 3.40 Hz.
- Exp vs Circ AUC(Z): mean −0.0138, p=0.279 (no sixfold elevation). Exp vs Sixfold-prior: −0.0798, p=5×10⁻⁵ (analysis detects imposed structure). 109/137 cells negative vs sixfold reference.
- Leave-one-out: Exp–Circ stays non-significant (0.142≤p≤0.695) for *every* omitted harmonic; Exp–Six stays at permutation floor throughout. Omitting P2 shifts Exp–Circ closest to zero (P2 dominates denominator).
- Burak–Fete CAN (128×128 periodic sheet): no selective local sixfold enhancement despite global periodicity; local spectrum dominated by low-order structure; persists under scale/width matching.
- Burst events: no sixfold enhancement in burst-vs-tonic comparisons.

## Reusable Patterns

1. **Matched-null circular reference**: to test "does X have property P", build simulations that copy all nuisance statistics of each unit (sampling, geometry, amplitude, location) and vary only P. Compare per-unit Z, not raw measurements. This is the correct defense against finite-sampling and preprocessing-induced spurious harmonics.
2. **Compositional metric + leave-one-out guard**: when using a fraction f = P_target/ΣP_k, always run the omission sensitivity — fractions can move by denominator changes alone.
3. **Global/local dissociation testing**: correct global deformation (affine destretch to circle) *before* asking local questions; otherwise global anisotropy masquerades as local structure.
4. **Lattice-constrained filtering without bias**: fit lattice only to *reject* candidates, never to reposition accepted ones — empirical centers stay empirical.
5. **Rectified von-Mises angular modulation** `g_rad(ρ)[1+β(ã(θ)−1)]₊` as a parametric dial for injecting k-fold angular structure into radially symmetric fields (β = strength knob, κ = concentration).
6. **Sign-flip permutation at population level** with AUC(Z) per-unit window summaries — nonparametric, handles non-Gaussian Z distributions.
7. **Honest negative-result reporting**: state explicitly what *is* shown (no sixfold above sensitivity threshold) and what *cannot* be excluded (weaker-than-β_min modulation; subset-of-cells effects; non-sixfold anisotropy). The paper's conclusion is scoped, not overclaimed.

## Implications for Grid-Cell Theory

- Supports treating individual grid fields as radially symmetric compact bumps (Sanzeni/Wei-style models).
- CAN models pass the constraint: global hexagonality does not force local sixfold expression.
- Local anisotropies exist (broadband, low-order dominated) but are not lattice-inherited — their origin remains open.

## Related Skills

- `grid-cell-normative-theory-review` — normative theories of grid representations
- `grid-cells-reduce-spatial-aliasing-hippocampal-place` — coding-theory perspective
- `topological-grid-cell-decoding-codes` — decoding-side counterpart
