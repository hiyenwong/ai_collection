---
name: fc-spectral-flattening-fmri-pretraining
description: Use when recalibrating FC spectra for fMRI prediction.
category: ai_collection
---

# FC Spectral Flattening: Eigenvalue Recalibration for Connectome Prediction & fMRI Encoder Pretraining

**Source**: Marraffini, Shevchenko, Barbano, Wassermann — "Flattening the Connectome Spectrum: A Spectral Filter for FC Induces a Pretraining Target for fMRI Encoders" (arXiv:2609.37642, Sep 2026, Inria Saclay / Sigma Nova)

**Trigger words**: functional connectivity, FC, eigenvalue, spectral filter, kernel ridge regression, KRR, fMRI, phenotype prediction, brain foundation model, BFM, pretraining target, distillation, fingerprinting, connectome, SPD matrix

## The One-Line Insight

Kernel ridge regression (KRR) on raw functional connectivity (FC) still beats every published brain foundation model (BFM) at phenotype prediction. The reason is that the KRR kernel implicitly **weights eigenvector overlaps by eigenvalues**, and raw FC eigenvalues are miscalibrated: the kernel over-weights the few top modes and starves the mid-spectrum modes that carry inter-individual differences. Raising every eigenvalue to a power α≈0.35 ("flattening the spectrum") recalibrates the kernel and matches/exceeds the KRR baseline on 5 datasets, 11 parcellations, 6 targets — then serves as the **distillation teacher** for pretraining a small fMRI encoder that matches the best BFMs with 10× fewer parameters.

## The Transform

Per subject, with Pearson FC matrix Σ = V D Vᵀ (symmetric PSD), the transform is:

```
Σ^α = V · D^α · Vᵀ,   D^α = diag(λ₁^α, ..., λ_P^α)
```

- Computed **per subject**: no group mean, no parameter estimated from other subjects.
- One eigendecomposition per subject — drop-in replacement for FC in ANY existing pipeline.
- α* = 0.35 selected once via nested-CV grid search on HCP-YA / Schaefer-400 (cognitive composite).
- Second, hyperparameter-free selection: maximize centered **kernel-target alignment** A(α) = ⟨K̄_α, Ȳ⟩_F / (‖K̄_α‖_F ‖Ȳ‖_F) with Ȳ = H y yᵀ H. Gives α_A = 0.387; α* = 0.35 sits at 99.55% of its maximum. Smooth with closed-form derivative (Brent optimization).

### Why eigenvalues matter in the kernel

For correlation-kernel KRR, subject similarity is the Frobenius inner product of their FC matrices:

```
⟨Σ_a^α, Σ_b^α⟩_F = Σ_{i,j} λ_i^α μ_j^α (v_iᵀ u_j)²
```

The kernel is a weighted sum of squared eigenvector overlaps, weight = λ_i^α μ_j^α. Raw FC has participation ratio ≈ 10 modes, so the kernel is dominated by a handful of top modes; raw FC gains nothing beyond its top-20 eigenvectors. Flattening redistributes kernel weight toward the mid-spectrum where individuals differ.

## Three Equivalent Interpretations (Appendix D)

1. **Geodesic** (log-Euclidean AND affine-invariant metrics agree): Σ^α = exp(α log Σ) is the geodesic from the identity to the raw connectome; α is arclength.
2. **Heat kernel**: with L̃ = −log(Σ/λ₁) PSD, Σ^α ∝ e^{−αL̃} — a proper heat semigroup interpolating identity (t=0) → raw connectome (t=1) → rank-one projector v₁v₁ᵀ (t→∞). The per-subject scale factor λ₁^{−t} cancels under the correlation kernel.
3. **Spectral filter**: recalibration of the connectome spectrum.

## Evidence and Controls (Appendix F — the ablation discipline)

- **Same eigenvectors, two weightings**: top-20 eigenvectors score 0.544 with raw weights, 0.610 with λ^0.35. Gain comes from eigenvalue weighting alone.
- **Kernel form does not matter; per-subject basis does**: Pearson/cosine/centered/dot-product kernels agree to 0.0006; RBF kernels on SPD geodesic distances are at-or-below linear. A subject's own top-20 eigenvectors keep 0.610; a shared PCA basis needs ~200 components to match (900 → 0.589). Informative directions differ across subjects — per-subject re-weighting beats any shared/learned projection.
- **Other filters fail**: 100 random monotone/non-monotone filters, none exceed 0.621; learned filters (30-param binned, MLP) fit inner CV and generalize worse (0.586/0.579 vs 0.624). Simple power law wins.
- **Not an identity effect**: one-hot subject ID predicts at 0.000; random per-subject embedding 0.054. FC^α* raises split-half reliability 0.597 → 0.830; observed 0.624 is 95% of the disattenuated ceiling 0.655.
- Beats tangent-space, log-Euclidean, partial-correlation parameterizations.

**Headline numbers** (HCP-YA composite, Pearson r): Schaefer-400: 0.543 → 0.627; AOMIC-ID1000 movie: 0.348 → 0.432. Fingerprinting 0.762 → 0.895. All significant (Nadeau-Bengio corrected t-test).

## Distillation into a Timeseries Encoder (Section 3.4)

- **Student**: fMRI-BERT — BERT-style bidirectional Transformer over parcellated timeseries; each timepoint of the P-region sequence is one token; sinusoidal positions → variable-length recordings at inference; [CLS] output is the embedding.
- **Teacher**: z_i = vec(FC_i^α*) (off-diagonal edges of the flattened connectome from the WHOLE recording), centered, unit-norm.
- **Objective**: kernel-target alignment between student Gram K_s = EEᵀ and teacher Gram K_t = ZZᵀ. No positive pairs, no augmentations needed — the distance teacher itself defines the target.
- **Key asymmetry**: teacher always sees the full recording; student sees only a short window → student learns to infer whole-recording connectivity from a partial view. This is exactly what wins on short scans.
- Trained on ~4,000 hours of fMRI from 162 open datasets (multi-site, multi-country).
- **Results**: on par with the best of 6 published BFMs on the composite with ~10× fewer parameters; beats raw-FC KRR on short scans and in smaller cohorts; strongest in fingerprinting. Neither transform nor encoder needs a GPU.

## Implementation Sketch

```python
import numpy as np

def flatten_fc(sigma: np.ndarray, alpha: float = 0.35) -> np.ndarray:
    """Per-subject spectral recalibration of a Pearson FC matrix."""
    lam, V = np.linalg.eigh(sigma)                    # symmetric eigendecomposition
    return (V * np.power(np.maximum(lam, 0.0), alpha)) @ V.T

def kernel_target_alignment(K: np.ndarray, y: np.ndarray) -> float:
    """Alignment between centered kernel and label kernel (model-selection for alpha)."""
    H = np.eye(len(y)) - np.ones((len(y), len(y))) / len(y)
    Yb = H @ (np.outer(y, y)) @ H
    Kb = H @ K @ H
    return np.sum(Kb * Yb) / (np.linalg.norm(Kb) * np.linalg.norm(Yb))
```

## When to Use

1. **Any FC-based phenotype/diagnosis/behavior regression** — replace FC with FC^0.35 before KRR/ridge/SVM (one extra eigendecomposition per subject).
2. **Pretraining fMRI encoders** — use flattened-connectome Gram alignment as the distillation objective instead of contrastive objectives.
3. **Fingerprinting / subject identification** — largest gains.
4. **Clinical cohorts with short scans and small samples** — where the advantage over raw FC is biggest.
5. **Strengthening FC–behavior correlations** in any study relating FC to cognition, diagnosis, or identity.

## Pitfalls / Limitations

- α* was selected once on HCP-YA/Schaefer-400 (optimistic for that cell); matched-or-improved everywhere tested, but the per-cohort optimum could differ — use kernel-target alignment to re-estimate without labels-needing nested CV.
- α→0 limit scores below the peak — don't over-flatten; the optimum is interior.
- Fixed hand-set eigenvalue profiles recover only ~half the gain — the subject's own compressed magnitudes matter.
- Teacher–student gap: full-scan encoder reads at par with raw FC, still below its FC^α* teacher (bigger batches hypothesized to close the gap).
- Pretraining corpus is public multi-site data, not a national biobank — a feature for under-represented populations.

## Related

- Contrast with tangent-space/log-Euclidean FC parameterizations (this transform dominates both).
- Related skills: `spectralot-functional-alignment` (geometry-aware fMRI alignment), `brain-foundation-model-batch-effects`, `functional-connectome-fingerprint`.
