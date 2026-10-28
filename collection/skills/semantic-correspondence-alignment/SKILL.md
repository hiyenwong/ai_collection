---
name: semantic-correspondence-alignment
version: 1.0
author: neuro-cron (2026-10-26 run3)
license: MIT
description: Use when aligning latent spaces across models or brains
metadata:
  hermes:
    tags: [representational-alignment, model-stitching, relative-representations, fMRI, cross-subject, zero-shot, correspondence, neural-manifolds]
    related_skills: [platonic-representations-brain, spectralot-functional-alignment, cross-species-rsa-brain-alignment, naturality-violation-score, correspondence-score-audit-alignment]
---

# Semantic Correspondence Alignment (Zero-Shot)

Source: "The Geometry of Meaning in Neural Manifolds" — PhD thesis, Sapienza (Rodolà/Locatello), arXiv:2610.30938. Fourteen methods (RelRep ICLR'23 oral, ASIF, Latent Functional Maps, ResiDual, HeadPursuit, LinEAS, …) unified by one principle.

## When to Use

- Zero-shot comparison, retrieval, stitching, or steering across independently trained models (different seeds, architectures, dimensionalities) — no joint training, no adapter training.
- Cross-subject alignment of brain recordings (fMRI/EEG) given shared stimuli; cross-population or cross-species decoding.
- Auditing whether ensemble disagreement is genuine model uncertainty vs reparameterization noise.
- Any setting where two representation spaces must be compared but absolute coordinates are incomparable (dim mismatch, rotation/scale gauge freedom).

## Core principle

Independently trained systems that extract overlapping semantic structure converge in **intrinsic** geometry (angles, neighborhoods, spectra, invariants) while diverging in **extrinsic** coordinates (absolute positions, axes, scales). A **correspondence** Γ ⊆ OX×OY — known pairs of semantically equivalent observations — breaks the coordinate symmetry and reveals the shared geometry, enabling zero-shot transformation without joint training. Empirical fact, not a theorem: state alignment assumptions explicitly and validate geometrically; never claim sufficiency conditions.

## Design rules

1. **Γ encodes the task, not just the data.** Cross-modal retrieval pairs *concepts across modalities* (cat-image↔cat-text); style transfer pairs *instances across conditions* (same scene, with/without style). Wrong Γ fails regardless of method sophistication. Ask: what should the two columns of each pair share?
2. **Match correspondence strength to method.** Strength spectrum: shared semantic anchors (same stimulus to both models / both subjects) > cross-modal pairs (image-caption, translations) > task structure (shared label space, no pairing) > distributional statistics (means/covariances/spectral decay only). Weaker Γ ⇒ stronger geometric assumptions required.
3. **Pick the revealed structure deliberately**: angular (cosine to anchors — invariant to rotation+scaling), metric (distances), spectral (eigenstructure — dimension-free), component (which unit encodes which concept), distributional (statistics over sets).
4. **Choose the operator family by what consumes the output:**
   - *Parallel* ΠΓ: transform each space independently via its own Γ side → outputs in shared **semantic coordinates**. One-to-many modular ("nexus"); but incompatible with pretrained decoders. Use for retrieval, comparison, ensembles, cross-subject analysis.
   - *Coupled* TΓ: use both sides jointly (Procrustes/translation/IRP) → outputs in **target-native coordinates**; direct decoder reuse, zero-shot stitching (encoder→T→target decoder). But pairwise — O(N²) across a model zoo.
   - *Same-space* ΣΓ (special case): intervene within one model (steering, head analysis) by pairing internal components with external references.
5. **Modular escape hatch**: chain parallel projection with pseudo-inverse (inverse relative projection) to return to target-native coordinates — stitching that keeps modularity but trails native accuracy by measurable 3–20 points; inverse stability trades off with anchor count (condition number).

## Instantiations (verified recipes)

- **Relative representations (RelRep)** — the workhorse: rel(x) = [cos(x, a_j)]_{j=1..K} against K anchors shared across spaces. Exactly invariant to rotation+scaling reparameterization. Anchors: random works; K≈latent-dim preserves dimensionality; coverage matters more than count (query far from anchors ⇒ extrapolation).
- **Cross-subject fMRI (Cosyne'24 protocol)**: per-subject *supervised* bottleneck first (MLP trained to classify stimuli), THEN RelRep with 300 shared anchor images, Γ = same stimulus recorded in both subjects. Task-informed encoding is what makes noisy, individually-variable brains alignable — raw-signal RSA is the weaker baseline. Evaluate cross-subject MRR; relative ≫ PCA-reduced ≫ absolute.
- **Ensemble uncertainty audit**: observed latent variance σ²_O = σ²_R (reparameterization noise) + σ²_M (genuine). Quantify removal with FLD-style ρ = σ²_B/(σ²_B+σ²_W) computed on J ensemble members per observation. Pure-reparam ensemble: ρ_abs≈0.1 vs ρ_rel≈1.0. Sample ensemble members near mode-connectivity-curve *midpoints* — that is where new information lives. Projection choice is architecture-dependent and not innocuous (unit-norm cosine inflates near-zero-vector uncertainty).
- **Online RL / drifting encoders**: EMA-stabilize anchor embeddings so correspondence survives coordinate drift; turns O(n_v×n_t) retrainings into O(n_v+n_t) modular components.
- **Coupled family**: orthogonal Procrustes on pairs (needs matched dims + enough pairs); latent functional maps for spectral, dimension-free maps (sensitive to eigenvector count; assumes full correspondence — not partial); Latent Space Translation learns the transport directly.
- **ΣΓ interventions**: HeadPursuit = simultaneous orthogonal matching pursuit of head outputs vs unembedding concepts (linearity assumption; uniform over tokens); LinEAS learns steering maps from distributional correspondence with ~32 unpaired samples per concept; ResiDual aligns residual-stream principal components across models (requires task-relevant PCs to exist).

## Pitfalls

- **Stitching success ≠ representational similarity** (Smith et al. 2025): task metrics constrain only task-relevant geometry; two spaces can stitch while broader semantic organization differs. Validate with structural probes (neighborhood overlap, CKA, reconstruction fidelity, spectra) — not only downstream accuracy; accuracy directly optimized can mislead.
- **Semantic overlap is the prerequisite** — models trained on unrelated objectives have no alignable geometry; alignment failing there is a feature (it exposes structure, does not invent mappings).
- RelRep projects R^d→R^K: information loss is real; generation from semantic coordinates needs auxiliary decoders or inversion.
- Platonic convergence is **local neighborhood structure**, not global geometry (Gröger et al. 2026 qualification) — do not claim global isometry from kNN overlap.
- Safety: correspondence-based translation/steering can bypass alignment (redirect models) or extract proprietary capabilities without weights — treat as dual-use.

## Verification (2026-10-26, numpy, sklearn-digits MLPs, all pass)

T1 invariance: |rel(Z,A)−rel(sZQ,sAQ)|max = 6e-13 while |Z−sZQ|max = 16. T2 pure-reparam ensemble (J=20): ρ_abs=0.098, ρ_rel=1.000. T3 two independently trained encoders (100% train acc): cross-model MRR relative=0.244 vs PCA=0.007 vs absolute=0.003; cross-dim pair (64 vs 32 latent) aligns ONLY via correspondence (MRR 0.212). Script: ~/.hermes/workspace/scripts/test_semantic_correspondence_skill_20261026.py

## Related topics

platonic-representations-brain (fMRI cross-subject isometry), fast-whole-brain-spectralot-alignment + spectralot-functional-alignment (functional alignment alternative), cross-species-rsa-brain-alignment, naturality-violation-score (category-theoretic audit of alignment claims), correspondence-score-audit-alignment (RSA score auditing), retrieval-based-brain-decoding-alignment, orthogonal-residual-quantization (multi-space fusion). Open tooling: LATENTIS (unified correspondence-operator API).
