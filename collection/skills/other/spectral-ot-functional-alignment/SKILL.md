---
name: spectral-ot-functional-alignment
description: SpectralOT — a geometry-aware, spectral optimal-transport functional alignment method for fMRI that embeds cortical surface geometry (Laplace-Beltrami eigenmodes) into the alignment cost to regularize cross-subject alignment while preserving anatomical structure. Use when building population-level brain decoders, doing cross-subject fMRI alignment, or need a fast geometry-preserving alternative to Hyperalignment / Riemannian alignment. Trigger words: functional alignment, cross-subject decoding, fMRI alignment, Laplace-Beltrami, cortical geometry, optimal transport, Hyperalignment, surface-based alignment, population decoder.
---

# SpectralOT — Geometry-Aware Functional Alignment for fMRI

## What it is
SpectralOT (arXiv:2607.10931, Barbarant et al., 2026-07-12) is a new **functional alignment**
method for fMRI that aligns functional data across individuals before training
population-level decoders. The core innovation: it **embeds cortical surface geometry into
Laplace–Beltrami eigenmodes** and uses them to regularize an optimal-transport (OT) alignment,
striking the balance between (a) aligning functional features and (b) preserving anatomical
structure, while staying computationally efficient (spectral/spectral-OT rather than full
pairwise OT on vertices).

### Problem it solves
Inter-individual variability in brain response patterns limits decoders that generalize across
subjects. Functional alignment maps each subject's data into a shared space. Existing methods
trade off alignment quality vs. anatomical preservation vs. speed:
- **Hyperalignment (Haxby 2011):** fast, PCA-based, but ignores cortical geometry.
- **Riemannian / surface-based alignment:** preserves geometry but is slow / optimization-heavy.
- **Optimal transport on vertices:** geometrically natural but expensive at brain scale.

SpectralOT addresses all three: spectral (Laplace–Beltrami) regularization + OT formulation +
efficient solver.

## Core methodology (reusable recipe)
1. **Build cortical geometry basis.** Compute the Laplace–Beltrami (LB) eigenmodes of each
   subject's cortical surface mesh (e.g. from FreeSurfer / fsLR surface). These eigenmodes are
   the "spectral" coordinates that encode anatomy independent of functional data.
2. **Functional data projection.** Represent each subject's fMRI time series / feature maps in a
   shared functional basis (e.g. task contrasts or ROI responses).
3. **Regularized optimal transport.** Solve an OT problem that transports one subject's functional
   embedding toward another's, with a **geometry penalty** term measured in LB-eigenmode space
   (penalize warps that violate cortical adjacency/structure). This is the "SpectralOT" cost:
   `cost = functional_OT_distance + λ · geometry_deviation(LB_modes)`.
4. **Shared decoder training.** After aligning all subjects into the common space, train a single
   population-level decoder (e.g. ridge / logistic) on the pooled aligned data.
5. **Leave-one-subject-out evaluation.** Align held-out subject to the rest; decode; report
   cross-subject generalization vs. baseline (no alignment / Hyperalignment).

## When to use
- Multi-subject fMRI studies needing a **population decoder** (decoding thoughts/stimuli across people).
- Scenarios where anatomical preservation matters (surface-based ROIs, cortical topography).
- Compute-constrained pipelines (need speed but want geometry awareness).
- Benchmarking new alignment methods against a strong, simple, geometry-regularized baseline.

## When NOT to use
- Single-subject analyses (alignment is only meaningful across subjects).
- Non-surface data (volume-only fMRI without a mesh) — you'd need to adapt the LB basis.
- If a heavyweight learned alignment (deep hyperalignment, VPN) is already beating spectral
  methods on your task and compute is not a concern.

## Implementation notes / pitfalls
- **Mesh consistency is mandatory.** All subjects must be in the same surface template
  (fsLR32k / fsaverage) so LB eigenmodes are comparable. Mis-registered meshes silently corrupt
  the geometry term.
- **λ tuning.** The geometry-weight λ controls the alignment↔anatomy trade-off. Sweep λ and
  validate on a held-out decoding metric, not on alignment loss alone.
- **LB eigenmode count.** Use enough low-frequency modes to capture coarse anatomy but not so many
  that you overfit to noise; 100–300 modes is a typical starting range.
- **OT solver.** Use an entropic-regularized Sinkhorn OT for speed; the geometry penalty can be
  folded into the cost matrix before Sinkhorn.
- **Functional basis choice** strongly affects results — task-contrast vectors are the standard
  for Natural Scenes / Haxby-style datasets; for resting-state use parcellated FC vectors.

## Relationship to existing ai_collection skills
- Distinct from `brain-alignment-*` (those are DNN↔brain representational alignment, RSA-style).
  SpectralOT is **subject↔subject functional alignment** for decoding, not model↔brain.
- Complements `atlas-free-brain-network-transformer` (single-subject spatial) — SpectralOT is the
  cross-subject bridge.
- Overlaps thematically with `flexibrain-resolution-agnostic-fmri-encoding` (encoding side) — pair
  them: align with SpectralOT, then train encoding models.

## Verification
- Reproduce the paper's cross-subject decoding gain on a public dataset (Haxby, Natural Scenes
  Dataset, or fMRI Nimstim).
- Ablate the geometry term (λ=0) → should degrade to near-Hyperalignment behavior; confirms the
  LB regularization is doing work.
- Check that aligned maps preserve known retinotopic / functional gradients (sanity anatomical check).

## Source
Barbarant P-L, Meyniel F, Thirion B. "Fast Whole-Brain, Geometry-Aware Functional Alignment for
Cross-Subject Decoding." arXiv:2607.10931 (2026-07-12), q-bio.NC.
