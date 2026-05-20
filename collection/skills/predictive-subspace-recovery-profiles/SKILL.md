---
name: predictive-subspace-recovery-profiles
description: "Target-space recovery profiles methodology for evaluating model-brain alignment beyond prediction accuracy. Identifies which reproducible brain response dimensions are recovered by encoding models. Activation: model-brain alignment evaluation, predictive subspace, recovery profiles, neural encoding diagnostics, brain prediction dimensions."
---

# Predictive Subspace Recovery Profiles for Model-Brain Alignment

Methodology from arXiv:2605.20127 (Nakamura et al., 2026) — a unified framework for evaluating both model-brain and brain-brain alignment by identifying the response dimensions recovered by prediction, not just measuring scalar accuracy.

## Problem Statement

Model-brain comparisons typically summarize alignment by a single score: how accurately model representations predict brain responses (encoding analysis). This score is useful for comparing models, but **does not indicate which dimensions of the target brain's response space are recovered**. A prediction can match target responses well on average while recovering only some directions in this space, or while recovering directions that differ from those recovered by another prediction with similar accuracy.

## Core Methodology

### Key Concepts

1. **Target Response Space**: For a fixed ROI, the voxel/vertex response space where each image gives one response vector (pattern across voxels/vertices).

2. **Reproducible Target Reference**: Brain response dimensions reproducibly recovered from repeated measurements of the same images. Defined independently of any source (model or brain). Uses split-half partitions of repeated trials.

3. **Source-Induced Predictive Subspace**: The subspace spanned by predicted responses from a source (another subject's brain or a model's representations). Represented by a projector $P_s = Q_s Q_s^\top$ from a ridge-regularized low-rank linear fit.

4. **Recovery Profile**: Quantifies how strongly each reproducible target-reference dimension is recovered by the prediction, organized by the reference's eigenvalue-ranked dimensions.

5. **Top-k Reference Coverage**: Summary metric — the reference-weighted fraction of leading target-reference dimensions recovered from a source.

### Step-by-Step Framework

**Step 1: Define reproducible target reference**
```python
# From repeated fMRI measurements
# Split trials into two halves, predict half-A from half-B
# The predictable subspace defines reproducible dimensions
# Repeat across multiple split-half partitions and average
```

**Step 2: Fit source-to-target prediction**
```python
# Ridge-regularized low-rank linear fit:
# Y_target ≈ X_source @ W
# W = argmin ||Y - XW||^2 + lambda||W||^2
# Retain the predictive subspace Q_s from the fit
```

**Step 3: Compute recovery profile**
```python
# For each target-reference dimension (ranked by reproducibility weight):
#   Compute projection of predicted responses onto that dimension
#   Quantify recovery strength = correlation or projection magnitude
# Result: vector of recovery strengths per reference dimension
```

**Step 4: Compare against brain-to-brain reference**
```python
# Use other subjects' brains as sources to predict target brain
# This defines the "human ceiling" for recovery profiles
# A model should recover dimensions at least as well as human brains do
```

### Mathematical Framework

- **Source matrix**: $X_s \in \mathbb{R}^{n \times p_s}$ (n images, p_s source dimensions)
- **Target matrix**: $Y \in \mathbb{R}^{n \times q}$ (n images, q voxels/vertices)
- **Predictive subspace projector**: $P_s = Q_s Q_s^\top$ where $Q_s \in \mathbb{R}^{q \times k_s}$
- **Reproducible reference**: eigenvalue-decomposed from split-half prediction covariance

## Key Findings (NSD Dataset)

1. **Low-dimensional reproducible references**: Early-to-intermediate visual cortex responses contain a small set of reproducible dimensions. First 3 dimensions account for ~88.6% of normalized reference weight; median entropy effective rank is 5.12.

2. **Brain-to-brain structured recovery**: Brain sources recover leading dimensions well (0.959 at k=1) but declining for lower-weight dimensions (0.868 at k=10). This provides a human reference profile, not just a scalar upper bound.

3. **Accuracy masks mismatches**: Pretrained and randomly initialized models can achieve similar prediction accuracy while showing distinct recovery profiles across response dimensions. Scalar accuracy alone is insufficient.

4. **Predictive subspace sufficiency**: Readouts restricted to the selected predictive subspace preserve nearly the same accuracy as full-representation readouts, outperforming source-side PCA controls.

## Applications

- **Model selection diagnostics**: Choose models not just by accuracy but by which brain dimensions they recover
- **Architecture comparison**: Compare CNNs, ViTs, and other architectures by their recovery profiles
- **Random initialization controls**: Distinguish learned structure from architectural priors
- **Cross-subject generalization**: Understand which brain dimensions transfer across individuals
- **ROI-specific analysis**: Different visual areas (V1, V2, V3, hV4) have different recovery characteristics

## Experimental Setting (from paper)

- **Dataset**: NSD-core-shared (8 subjects, 515 shared natural images, repeated trials)
- **ROIs**: V1v, V1d, V2v, V2d, V3v, V3d, hV4 (both hemispheres)
- **Model sources**: ResNet-18/50, VGG-16, ViT-B/16 (pretrained + random controls)
- **Brain sources**: Other subjects' responses in corresponding ROI
- **Evaluation**: 5-fold cross-validation, held-out prediction accuracy + recovery profiles

## Comparison with Existing Approaches

| Approach | Measures | Limitation |
|----------|----------|------------|
| Encoding (RSA/linear) | Prediction accuracy | Scalar only, no dimensional diagnosis |
| CKA/Centered Kernel Alignment | Representational similarity | No reference to reproducibility |
| Recovery Profiles (this work) | Dimensional recovery + accuracy | Requires repeated measurements |

## Implementation Guide

```python
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split

def compute_reproducible_reference(Y_repeated_a, Y_repeated_b):
    """From split-half repeated measurements."""
    # Fit: predict half-B from half-A
    ridge = Ridge(alpha=1.0)
    ridge.fit(Y_repeated_a, Y_repeated_b)
    Y_pred = ridge.predict(Y_repeated_a)
    # Covariance of predictions defines reproducible subspace
    cov = Y_pred.T @ Y_pred / len(Y_pred)
    eigvals, eigvecs = np.linalg.eigh(cov)
    # Sort by eigenvalue descending
    idx = np.argsort(eigvals)[::-1]
    return eigvals[idx], eigvecs[:, idx]

def compute_recovery_profile(X_source, Y_target, ref_eigvecs, ref_eigvals):
    """Compute which reference dimensions are recovered."""
    # Fit source -> target
    ridge = Ridge(alpha=1.0)
    ridge.fit(X_source, Y_target)
    Y_pred = ridge.predict(X_source)
    
    # Project predictions onto reference dimensions
    projections = Y_pred @ ref_eigvecs
    recovery = []
    for i in range(len(ref_eigvals)):
        # Recovery strength for dimension i
        strength = np.var(projections[:, i]) * ref_eigvals[i]
        recovery.append(strength)
    return np.array(recovery)
```

## Pitfalls

- **Requires repeated measurements**: Cannot compute reproducible reference without repeated trials of the same stimuli
- **Hold-out requirement**: Recovery profiles must be held-out from source fitting and model selection
- **ROI-dependent**: Different brain regions have different dimensional structures; compare within fixed ROI
- **Not whole-model brain-likeness**: High recovery in one ROI does not imply global brain-likeness
- **Preprocessing sensitive**: Different voxel selections, weightings, or preprocessing define different target spaces

## Related Work

- Extends encoding analysis (Naselaris et al.) beyond scalar accuracy
- Complements representational similarity analysis (Kriegeskorte et al.)
- Brain-to-brain prediction as human reference (Haxby et al.)
- Natural Scenes Dataset (Allen et al., Nature Neuroscience 2022)

## Citation

```bibtex
@article{nakamura2026predictive,
  title={Beyond Prediction Accuracy: Target-Space Recovery Profiles for Evaluating Model-Brain Alignment},
  author={Nakamura, Ken and Nakai, Tomoya and Yashiro, Ryuto and Yamashita, Ayumu and Amano, Kaoru},
  journal={arXiv preprint arXiv:2605.20127},
  year={2026}
}
```
