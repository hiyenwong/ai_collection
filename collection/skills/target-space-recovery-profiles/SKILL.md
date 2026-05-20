---
name: target-space-recovery-profiles
description: >
  Target-Space Recovery Profiles (TSRP) methodology for evaluating model-brain
  alignment beyond prediction accuracy. Identifies which reproducible brain
  response dimensions are actually recovered by prediction models, providing
  diagnostic evaluation rather than scalar benchmarks. Use when: evaluating
  neural encoding models, comparing model-brain alignment methods, designing
  brain alignment evaluation frameworks, diagnosing why models with similar
  accuracy show different neural representations, brain-brain comparison studies.
  Triggered by: target-space recovery, recovery profiles, model-brain alignment
  evaluation, encoding model diagnostics, brain prediction dimensions, neural
  encoding evaluation, prediction accuracy limitations, brain-brain alignment,
  response dimension recovery, reproducible brain dimensions, TSRP.
---

# Target-Space Recovery Profiles (TSRP)

Evaluate model-brain alignment by identifying **which** reproducible brain
response dimensions are recovered, not just how accurately.

## Core Problem

Prediction accuracy alone masks model-brain mismatches. Models with identical
encoding accuracy can recover completely different dimensions of brain activity.
TSRP makes explicit *which* dimensions are aligned.

## Methodology

### Step 1: Identify Reproducible Dimensions
```
Split fMRI trials into independent halves → PCA on each → compare subspaces
```
Dimensions with high cross-split reliability are "reproducible" — they represent
stable neural signals, not noise.

### Step 2: Train Encoding Models
```
For each model (brain-to-brain, CNN, transformer):
  - Train linear mapping: model features → fMRI voxels
  - Use cross-validation across stimuli
```

### Step 3: Compute Recovery Profiles
For each reproducible dimension d:
1. Project predicted responses onto d
2. Compute correlation between predicted and actual projection
3. Recovery(d) = correlation² — how well dimension d is recovered

### Step 4: Brain-to-Brain Baseline
```
Use other subjects' fMRI as "ideal model" to establish:
  - Upper bound on recoverable dimensions
  - Diagnostic human reference (not just scalar)
```

## Key Findings (Nakamura et al., arXiv:2605.20127)

- Early-to-intermediate visual cortex has **low-dimensional reproducible subspace**
- Pretrained and random models can match in accuracy but **diverge in recovery profiles**
- Brain-to-brain comparison provides dimension-specific reference, not scalar
- Some dimensions are consistently recoverable across subjects; others are not

## Implementation Pattern
```python
# Reproducibility analysis
from sklearn.decomposition import PCA
import numpy as np

def find_reproducible_dims(fmrA, fmrB, max_dims=20):
    """Find dimensions reproducible across two trial splits."""
    pca_a = PCA(max_dims).fit(fmrA)
    pca_b = PCA(max_dims).fit(fmrB)
    # Subspace similarity via canonical correlation
    A = pca_a.transform(fmrA)[:, :k]
    B = pca_b.transform(fmrB)[:, :k]
    # Project between subspaces, measure alignment
    scores = []
    for i in range(k):
        sim = np.abs(np.corrcoef(A[:, i], B[:, i])[0, 1]**2)
        scores.append(sim)
    return scores  # reproducibility per dimension

def compute_recovery_profile(predicted, actual, repro_dims):
    """Compute recovery profile for encoding model predictions."""
    recovery = []
    for i, (_, dim_score) in enumerate(repro_dims):
        pred_proj = predicted @ repro_dims[i]
        act_proj = actual @ repro_dims[i]
        rec = np.corrcoef(pred_proj, act_proj)[0, 1]**2
        recovery.append((dim_score, rec))
    return recovery
```

## When to Use TSRP vs Standard Encoding

| Scenario | Method |
|----------|--------|
| Compare model accuracy | Standard encoding (R²) |
| Diagnose *why* models differ | TSRP recovery profiles |
| Brain-to-brain comparison | TSRP with subject baseline |
| Dimension-specific alignment | TSRP |
| Quick benchmark | Standard encoding |

## Activation
target-space recovery, recovery profiles, model-brain alignment evaluation,
encoding model diagnostics, brain prediction dimensions, neural encoding
evaluation, prediction accuracy limitations, brain-brain alignment, response
dimension recovery, reproducible brain dimensions, TSRP, Nakamura 2026.

## Paper
Nakamura, K. et al. "Beyond Prediction Accuracy: Target-Space Recovery
Profiles for Evaluating Model-Brain Alignment." arXiv:2605.20127 [q-bio.NC],
2026.
