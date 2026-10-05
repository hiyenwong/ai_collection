---
name: gain-vs-off-manifold-decomposition
description: Decomposes neural population state changes into on-manifold movement, multiplicative gain modulation, and genuine off-manifold novelty via a tangent/normal bundle geometry with a radial gain axis, plus a 7-gate identifiability cascade (chart existence, intrinsic dimension, tangent frame, anchor bias, gain-axis existence, curvature booking, ratio conditioning). Use when analyzing neural state transitions, memory segmentation decorrelation, neuromodulator-driven gain vs. novelty attribution, neural manifold geometry, or when Euclidean/cosine distance metrics are insufficient to characterize how a new neural state relates to the existing representational repertoire. Activation: neural manifold, gain modulation, off-manifold displacement, state transition identifiability, memory segmentation, neural geometry decomposition.
license: MIT
metadata:
  arxiv_id: "2609.21272"
  published: "2026-09-18"
  authors: "Sam McKenzie"
  tags: [neural-manifold, gain-modulation, differential-geometry, identifiability, population-dynamics, memory-segmentation]
---

# Gain vs. Off-Manifold Displacement Decomposition

Source: arXiv:2609.21272 (2026-09-18) — Sam McKenzie, Univ. of New Mexico Health Sciences.

## Problem

Memory segmentation is attributed to rapid neuronal decorrelation (phasic neuromodulator
release, e.g. norepinephrine). But standard metrics — Euclidean distance, cosine angle —
detect **that** a transition occurred without revealing **what kind** of change it is:
- movement within the pre-existing state repertoire (on-manifold),
- mere amplification of a prior state (gain),
- or creation of a genuinely novel representation (off-manifold).

This matters because the same neuromodulators that drive state transitions also increase
neuronal excitability — an observed decorrelation could be pure gain, not novelty.

## Core Construction

Given a reference manifold M sampled as point set Z_A ⊂ R^F and test point z_B, with
projectors at reference point p:

- Tangent/normal split: `R^F = T_p M ⊕ N_p M`, with `P_T(p) = proj onto T_p M`,
  `P_N(p) = I − P_T(p)`.
- **Radial gain axis** (the key innovation): multiplicative gain does not change *what* is
  coded, only intensity, and the origin is a meaningful zero. Define
  `ρ̂_p = p/‖p‖`, `a(p) = ‖P_N(p) ρ̂_p‖ ∈ [0,1]`,
  gain direction within normal space `n̂_g(p) = P_N(p) ρ̂_p / a(p)` (defined iff a(p) > 0).
- Normal space is further partitioned: `N_p M = span(P_N(p) ρ̂_p) ⊕ N_res(p)`.
- Displacement `r_p = z_B − p` decomposes into three **mutually orthogonal** components:

```
r_p = P_T(p) r_p                # on-manifold pattern
    + (n̂_g(p)ᵀ r_p) n̂_g(p)     # gain
    + P_res(p) r_p,             # off-manifold residual
```

Report energy fractions `T`, `G`, `O` with `G + T + O ≡ 1` (exact identity).

**Why define the gain axis via `P_N(p) ρ̂_p` and not `ρ̂` alone**: part of the radial
energy is tangential movement along the manifold; projecting first avoids conflating
gain with on-manifold drift. Orthogonality makes projection order irrelevant.

**Anchor choice**: from static geometry you cannot know which point was gain-modulated;
the natural choice is the nearest on-manifold point. Anchor misspecification is a primary
bias source (Gates 3, 5).

## Identifiability Cascade (7 Gates)

Each gate is conditional on those above it. "Directly evaluable" = checkable from data at hand.

| Gate | Question | Diagnostic | Evals? | Failure mode |
|------|----------|-----------|--------|--------------|
| 0 | Does a local chart exist? | sheet separation vs. neighborhood extent/noise | No | mixed sheets mimic gain/novelty artifacts |
| 1 | Is intrinsic dim d right? | stability of tangent space as d varies | No | over-estimating d absorbs normal directions, corrupts O, can destroy gain axis |
| 2 | Is the tangent estimate good? | ‖V̂_d − V_d‖, gain-axis direction error | No | frame rotation mixes T/G/O (small at d = d_true under isotropic noise) |
| 3 | Where is the anchor? | anchor bias ≈ (ℓ²/2)·H⃗ (mean curvature); anchor jitter ∝ ℓ/√k | Partial (ℓ,k measurable; H⃗ not) | curvature-induced anchor bias = dominant systematic error |
| 4 | Does the gain axis exist? | a = ‖P_N ρ̂‖ | **Yes** | a=0 undefined; a≪1 ill-conditioned; shrinking a converts G into O |
| 5 | Where is anchor displacement booked? | c = n̂_gᵀ H⃗/‖H⃗‖ | No | \|c\|=1 routes anchor displacement to G; c=0 routes it to spurious O |
| 6 | Is G/O ratio conditioned? | C₆ = k‖r‖²/ℓ² per probe | **Yes** | denominator ~ anchor jitter → O unstable/uninformative |

## Key Laws (from simulations on idealized manifolds)

- Off-manifold estimate bias is: **signed by the direction of gain**, **linear in anchor
  displacement at first order**, computable up to the second fundamental form.
- Gate 3: anchor bias grows with neighborhood size ℓ (curvature), anchor jitter shrinks
  with sample count k — a **deliberate** trade-off, not a default-small-k decision.
- Noise along the gain axis is governed by σ_w/ℓ — larger neighborhoods *reduce* it, the
  opposite of Gates 2/3 where larger neighborhoods increase anchor bias and frame rotation.
- Dimension check trick: sweep d; a sharp drop in alignment a between d and d+1 indicates
  normal directions being absorbed into the tangent estimate. On origin-centered manifolds
  `a² ≈ 1 − capture`, so the drop reads the absorbed share directly.

## Practical Diagnostics (§6.1)

The decomposition is trustworthy when: locally valid chart, intrinsic dimension supported
by the data, tangent estimate stable across neighborhood scales, test state within a
plausible projection region, radial axis sufficiently aligned with hypothesized gain
direction. Ratio summaries (G/O) need an explicit conditioning check (Gate 6) because
small denominators make relative attribution unstable even when the vector decomposition
is fine.

Interpretation posture: this framework does not assign a change to gain vs. novelty; it
specifies **when those assignments are identifiable, how they become biased, and which
diagnostics reveal the failure regime**.

## Usage Protocol

1. Build reference manifold sample Z_A from baseline/pre-existing states.
2. Estimate intrinsic dimension d; validate with the alignment-drop sweep (Gate 1).
3. Fit local tangent frame at candidate anchors; compute projectors P_T, P_N.
4. Compute a(p) at the anchor — if a ≈ 0, gain/novelty separation is not available.
5. Decompose displacement into T/G/O fractions; check C₆ conditioning before reporting ratios.
6. Report the gate status alongside the numbers (which gates passed/failed/unknown).

## Limitations

- Anchor ambiguity is irreducible from static geometry — decomposition is anchor-relative.
- Mean curvature vector H⃗ (Gates 3, 5) is not estimated by the framework; must be argued
  from manifold geometry.
- Only a small set of sensory geometries/tasks tested; under-estimated d not simulated
  (leaves tangential directions booked as O).
- Single test state per probe; temporal dynamics out of scope.

## Related

- Complements cosine/Euclidean decorrelation analyses of memory segmentation (it adds
  *mechanism*, not just detection).
- Natural pairing with attractor-repertoire analyses and representational-drift studies
  where "repurposing old vs. creating new representations" is the question.
