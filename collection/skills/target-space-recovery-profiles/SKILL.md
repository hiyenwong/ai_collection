---
name: target-space-recovery-profiles
description: Target-Space Recovery Profiles (TSRP) methodology for evaluating model-brain alignment beyond prediction accuracy. Identifies which reproducible brain response dimensions are recovered by predictive models, providing diagnostic evaluation of alignment between artificial models and human neural data. Activation: model-brain alignment, brain model alignment evaluation, prediction accuracy neuroscience, target-space recovery, neural representational analysis, fMRI model evaluation
---

# Target-Space Recovery Profiles (TSRP) Methodology

Evaluating model-brain alignment by identifying which reproducible brain response dimensions are recovered by prediction, going beyond scalar prediction accuracy metrics.

**arXiv:** [2605.20127](https://arxiv.org/abs/2605.20127)
**Authors:** Ken Nakamura, Tomoya Nakai, Ryuto Yashiro, Ayumu Yamashita, Kaoru Amano
**Date:** 2026-05-19
**Categories:** q-bio.NC, cs.AI, cs.LG

## Core Idea

Prediction accuracy alone does not indicate which dimensions of the target brain's response space are recovered by a model. TSRP introduces a unified framework for evaluating both model-brain and brain-brain alignment by:

1. **Identifying reproducible response dimensions** — Using repeated fMRI measurements to find target-brain response dimensions that can be reproducibly predicted across independent trial splits
2. **Quantifying dimension recovery** — Predicting target-brain responses from either another subject's brain or a model's internal representations, and measuring how strongly each reproducible dimension is recovered
3. **Diagnostic evaluation** — Providing a profile (not just a scalar) showing which response dimensions are captured vs. missed

## Key Findings

- Early-to-intermediate visual cortex responses contain a **low-dimensional set of reproducible dimensions**
- Brain-to-brain comparisons identify which dimensions are consistently recoverable from other subjects' brains, providing a **diagnostic human reference** rather than only a scalar benchmark
- In some cases, **pretrained and randomly initialized models achieve similar prediction accuracy while showing distinct recovery profiles** — prediction accuracy alone can mask model-brain mismatches

## Methodology Pipeline

### Step 1: Identify Reproducible Dimensions

```python
import numpy as np
from sklearn.decomposition import PCA

def find_reproducible_dimensions(fMRI_data_split_A, fMRI_data_split_B, n_components=10):
    """Find brain response dimensions that are reproducible across trial splits."""
    # PCA on split A to define candidate dimensions
    pca = PCA(n_components=n_components)
    components_A = pca.fit_transform(fMRI_data_split_A)
    
    # Project split B onto same components
    components_B = pca.transform(fMRI_data_split_B)
    
    # Compute reproducibility (correlation) for each dimension
    reproducibility = np.array([
        np.corrcoef(components_A[:, i], components_B[:, i])[0, 1]
        for i in range(n_components)
    ])
    
    # Select dimensions with reproducibility above threshold
    reproducible_mask = reproducibility > 0.3  # threshold
    return components_A[:, reproducible_mask], reproducibility[reproducible_mask]
```

### Step 2: Train Predictor

```python
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score

def train_brain_predictor(model_features, target_brain_data):
    """Train model to predict brain responses from model representations."""
    predictor = Ridge(alpha=1.0)
    scores = cross_val_score(predictor, model_features, target_brain_data, 
                             cv=5, scoring='r2')
    predictor.fit(model_features, target_brain_data)
    return predictor, scores.mean()
```

### Step 3: Quantify Dimension Recovery

```python
def compute_recovery_profile(predictor, model_features, reproducible_dims, target_data):
    """Quantify how well each reproducible dimension is recovered."""
    predicted = predictor.predict(model_features)
    
    recovery_scores = []
    for i in range(reproducible_dims.shape[1]):
        # Correlation between predicted and actual for each dimension
        dim_prediction = predicted @ np.linalg.pinv(target_data) @ reproducible_dims[:, i]
        corr = np.corrcoef(dim_prediction, reproducible_dims[:, i])[0, 1]
        recovery_scores.append(corr)
    
    return np.array(recovery_scores)
```

### Step 4: Compare Across Models

```python
def compare_model_recovery_profiles(models_features_list, target_brain, reproducible_dims):
    """Compare recovery profiles across multiple models."""
    profiles = {}
    for name, features in models_features_list.items():
        predictor, accuracy = train_brain_predictor(features, target_brain)
        profile = compute_recovery_profile(predictor, features, reproducible_dims, target_brain)
        profiles[name] = {'accuracy': accuracy, 'profile': profile}
    return profiles
```

## Application Scenarios

- **Vision model evaluation**: Assess which visual cortex response dimensions CNN/ViT models capture
- **Cross-subject alignment**: Compare brain-to-brain recovery as a human reference baseline
- **Model comparison**: Distinguish models with similar prediction accuracy but different representational coverage
- **Architecture selection**: Guide model architecture choices based on which neural dimensions matter most
- **fMRI encoding studies**: Diagnose what aspects of neural responses encoding models capture or miss

## Relationship to Existing Methods

| Method | What it measures | TSRP advantage |
|--------|-----------------|----------------|
| Prediction accuracy (R²) | Overall prediction quality | Reveals which specific dimensions drive the score |
| Representational Similarity Analysis (RSA) | Pairwise representational geometry | Works directly in response space, no need for RDM construction |
| Encoding models | Stimulus-to-brain mapping | Evaluates model-to-brain alignment directly |
| Brain-score | Aggregated benchmark | Provides diagnostic dimension-level breakdown |

## Implementation Considerations

- **Requires repeated measurements** — Need multiple fMRI runs per subject to establish reproducibility
- **Natural Scenes Dataset (NSD)** — Ideal dataset as it has 8 subjects viewing the same images
- **Dimensionality selection** — Use cross-validated reproducibility threshold rather than fixed component count
- **Human baseline** — Always compute brain-to-brain recovery as reference; model recovery should be compared against this

## Pitfalls

- **Low reproducibility ≠ bad model** — If brain responses aren't reproducible across trials, no model can predict them
- **Different accuracies, same profile** — Models may recover the same dimensions but at different strengths
- **Same accuracy, different profile** — The key insight: two models can have identical prediction accuracy but recover completely different neural dimensions
- **Dataset dependency** — Reproducible dimensions are stimulus- and task-specific; results don't generalize across experimental paradigms

## Related Skills

- `decoding-encoding-alignment-critique` - Critical analysis of brain-model alignment methods
- `naturality-violation-score` - Category-theory-based brain-DNN alignment methodology
- `brain-dnn-transformation-alignment` - Category-theoretic framework for brain-to-DNN transformation
- `feature-visualization-brain-encoder` - Feature visualization for brain encoder models
