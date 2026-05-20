---
name: target-space-recovery-profiles
description: "Target-Space Recovery Profiles (TSRP) methodology for evaluating model-brain alignment beyond prediction accuracy. Identifies which dimensions of brain response space are recovered by predictive models, providing diagnostic evaluation of alignment between AI models and neural activity. Applicable to brain-encoding studies, computational neuroscience, neural alignment research."
---

# Target-Space Recovery Profiles for Model-Brain Alignment

## Overview

Target-Space Recovery Profiles (TSRP) is a unified framework for evaluating both model-brain and brain-brain alignment by identifying the response dimensions recovered by prediction. Published as arXiv:2605.20127 (Nakamura et al., 2026).

**Core Insight**: Prediction accuracy alone does not indicate which dimensions of the target brain's response space are recovered. Two models with identical prediction accuracy can have fundamentally different alignment profiles with neural data.

## Key Contributions

### 1. Beyond Scalar Accuracy Metrics
- Traditional brain-encoding studies use scalar metrics (correlation, R²) to measure model-brain alignment
- TSRP decomposes prediction into response dimensions to reveal *what* is being predicted
- Provides diagnostic profiles rather than single-number benchmarks

### 2. Reproducible Response Dimension Identification
- Uses repeated fMRI measurements to identify target-brain response dimensions
- Identifies dimensions that can be reproducibly predicted across independent trial splits
- Establishes upper bound on predictability for each dimension

### 3. Recovery Profile Analysis
- Quantifies how strongly each reproducible response dimension is recovered
- Compares recovery profiles across different models and baselines
- Brain-to-brain comparisons provide human reference for diagnostic evaluation

## Methodology

### Step 1: Identify Reproducible Dimensions
```python
# Split fMRI data into independent trial sets
# Perform PCA/SVD on trial-averaged responses
# Identify dimensions with high cross-validation reliability
from sklearn.decomposition import PCA
from sklearn.model_selection import cross_val_score

# For each voxel or ROI, compute reliability across splits
reliability = compute_dimension_reliability(trial_split_1, trial_split_2)
```

### Step 2: Build Encoding Models
```python
# Train encoding models to predict brain responses from:
# 1. Another subject's brain responses (brain-brain baseline)
# 2. Model internal representations (model-brain alignment)
from sklearn.linear_model import Ridge

encoding_model = Ridge(alpha=1.0)
encoding_model.fit(model_features, brain_responses)
predictions = encoding_model.predict(test_features)
```

### Step 3: Compute Recovery Profiles
```python
# For each reproducible dimension, compute recovery strength
# Recovery = correlation between predicted and actual dimension scores
recovery_profiles = {}
for dim in reproducible_dimensions:
    predicted_dim = project_to_dimension(predictions, dim)
    actual_dim = project_to_dimension(actual_responses, dim)
    recovery_profiles[dim] = correlation(predicted_dim, actual_dim)
```

### Step 4: Compare Recovery Profiles
```python
# Visualize recovery profiles across models
# Identify dimensions where models diverge despite similar accuracy
import matplotlib.pyplot as plt

plt.bar(dimension_ids, recovery_profile_model1, alpha=0.7, label='Model 1')
plt.bar(dimension_ids, recovery_profile_model2, alpha=0.7, label='Model 2')
plt.axhline(y=brain_brain_baseline, color='r', linestyle='--', label='Brain-Brain')
```

## Key Findings from Natural Scenes Dataset

1. **Early-to-intermediate visual cortex** contains low-dimensional set of reproducible response dimensions
2. **Brain-to-brain comparisons** identify consistently recoverable dimensions across subjects
3. **Pretrained vs random models** can achieve similar prediction accuracy but show distinct recovery profiles
4. **Prediction accuracy masks mismatches** - models can score equally while recovering different neural computations

## Applications

- **Brain-Encoding Studies**: Evaluate which aspects of neural activity models capture
- **Model Comparison**: Diagnose differences between architectures beyond accuracy
- **Brain-Brain Alignment**: Establish human baselines for model evaluation
- **Computational Neuroscience**: Understand representational structure in neural data

## Related Concepts

- Neural encoding models
- Representational Similarity Analysis (RSA)
- Brain-computer interface evaluation
- Model-brain alignment benchmarks
- fMRI response decomposition
- Cross-subject generalization

## Implementation Considerations

- Requires repeated measurements for reliability estimation
- Works best with high-quality fMRI datasets (e.g., Natural Scenes Dataset)
- Can be applied to other neural modalities (EEG, MEG, ECoG)
- Complements existing alignment metrics rather than replacing them

## References

- arXiv:2605.20127 - "Beyond Prediction Accuracy: Target-Space Recovery Profiles for Evaluating Model-Brain Alignment"
- Natural Scenes Dataset (NSD) - large-scale fMRI dataset for vision research
- Brain-encoding model literature (Naselaris et al., 2011; Huth et al., 2016)
