---
name: kl-minimality-distribution-reconstruction
description: "Uniqueness theorem: among smooth f-divergences, KL is the ONLY entropy-adapted divergence for maximum-entropy distribution reconstruction from finitely many generalized moments — moment matching and information projection coincide iff divergence is KL. Use when choosing divergence measures for moment-constrained reconstruction, exponential-family approximation, or generalizing max-ent methods; prevents silently broken best-approximation guarantees."
---

# KL Minimality for Moment-Constrained Distribution Reconstruction

**Source**: On Minimum Divergence for Distribution Reconstruction (arXiv: 2610.21872, math.ST, 2026-10-15)

## Problem

Maximum-entropy reconstruction recovers a probability distribution from
finitely many (generalized) moment constraints by minimizing divergence to a
reference measure. With **KL**, the reconstruction lies in an exponential
family and is simultaneously the **best KL-approximation** of the unknown
distribution within that family: *moment matching and information projection
coincide*. The natural generalization question: replace KL by another smooth
f-divergence — does the coincidence survive?

## Key Definitions

A family F is **entropy-adapted** (w.r.t. moment functions g₁…g_m) if the
f-projection of any distribution onto F matches its moments — i.e. the
minimizer of D_f(·‖μ_ref) over F is also the moment-matching point.

## Main Theorem

> Up to equivalence, **KL is the only C² f-divergence that is entropy-adapted**,
> whatever the choice of the generalized moments.

Consequences:

- Replace KL by any other smooth f-divergence (reverse-KL, Hellinger, χ²,
  α-divergences…): reconstructions still exist in an associated family, but
  the **best-approximation property fails** — the recovered distribution is
  no longer the information projection of the truth.
- The exponential-family geometry (moments ↔ natural parameters, Legendre
  duality, Bregman divergence structure) is *privately owned by KL* among
  smooth f-divergences.

## Reusable Pattern: "Divergence-Selection Audit"

Before swapping KL for a "more robust" f-divergence in any moment-matching or
projection pipeline (variational inference, distributionally-robust
optimization, transformer softmax-attention energy models, exponential-family
embedding):

1. Ask what structural guarantee you are inheriting: existence (usually
   survives), uniqueness (often survives), **best-approximation / projection
   property (KL-only)**, conjugate closed-form (KL-only for exponential
   families).
2. If the guarantee is projection-interpretability, keep KL on that axis and
   handle robustness with outlier weighting inside the moments (which
   preserves the exponential-family structure).
3. If you genuinely need a non-KL geometry (e.g. score-matching ↔ Fisher/
   Hellinger), re-derive the moment conditions — do not assume they carry over.

## Cross-Domain Connections

- This KL-minimality is why **free-energy / variational inference** uses
  reverse-KL with its mode-covering/mode-seeking asymmetry, while
  **maximum-entropy moment reconstruction** must use forward-KL.
- Explains a recurring pitfall in DRO (distributionally robust optimization):
  χ²- or Hellinger-balls keep existence but lose the moment-matching
  interpretation of the worst-case distribution.
- In today's sibling paper (arXiv 2610.21103), the same reverse-KL direction
  appears in the "reverse KL tensorization" used to prove one-sided McDiarmid
  inequalities for heavy tails — the direction of KL is load-bearing there too.

## Limitations

- Smoothness class C² — non-smooth f-divergences (total variation) have
  separate existence theory outside this result's scope.
- "Up to equivalence" is affine reparameterization of the divergence;
  check the paper for the exact equivalence relation.
- Numerical illustrations of the failure are in the source; the theorem is
  infinite-dimensional, so finite-sample behavior needs the usual
  empirical-process caveats.

## Related Skills

- `reverse-kl-tensorization-mcdiarmid` — (today, sibling) reverse KL tensorization for concentration
- `renyi-entropy-sample-complexity` — Rényi divergence estimation rates
- `distortion-riskmetric-wasserstein-dro` — non-KL DRO geometry
