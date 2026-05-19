---
name: eeg-preprocessing-reliability
description: "EEG decoding reliability assessment methodology addressing preprocessing instability. Covers Walsh-Hadamard decomposition of pipeline spaces, Preprocessing Uncertainty (PU) diagnostics, and Normalized Adaptive PGI regularization. Trigger: EEG reliability, 预处理可靠性, preprocessing uncertainty, pipeline sensitivity, BCI reliability, EEG decoding robustness, 脑电解码稳定性."
---

# EEG Preprocessing Reliability

## Description

Assess and mitigate EEG decoding reliability issues caused by preprocessing pipeline choices. Deep learning models for EEG are typically trained/evaluated under a single preprocessing pipeline, but up to 42% of trial-level predictions can flip when only preprocessing changes.

## Activation Keywords
- eeg reliability
- 预处理可靠性
- preprocessing uncertainty
- pipeline sensitivity
- bci reliability
- eeg decoding robustness
- 脑电解码稳定性

## Tools Used
- read: Load EEG datasets and preprocessing configs
- exec: Run Python analysis scripts for pipeline decomposition
- write: Save reliability reports

## Core Methodology

### Step 1: Preprocessing Uncertainty (PU) Assessment

Measure per-trial instability across preprocessing pipeline variations:

```python
import numpy as np

def preprocessing_uncertainty(predictions_dict):
    """
    predictions_dict: {pipeline_name: predictions_array}
    Returns per-trial uncertainty score
    """
    all_preds = np.array(list(predictions_dict.values()))
    # Entropy-based uncertainty across pipeline variations
    agreement = np.mean(all_preds == all_preds[0], axis=0)
    pu_score = 1 - agreement  # 0 = stable, 1 = unstable
    return pu_score
```

### Step 2: Walsh-Hadamard Decomposition

Decompose 2^k pipeline space into main effects and interactions:

```python
from scipy.linalg import hadamard

def walsh_hadamard_decompose(effects, k):
    """
    Decompose 2^k binary intervention space
    effects: array of 2^k prediction differences
    k: number of preprocessing interventions
    """
    H = hadamard(2**k)
    coefficients = H @ effects / (2**k)
    return coefficients  # Near-additive if higher-order terms small
```

### Step 3: Normalized Adaptive PGI (NA-PGI)

Apply graph-structured regularization to reduce preprocessing sensitivity:

```python
def na_pgi_regularization(loss, adjacency_matrix, lambda_reg=0.1):
    """
    Graph-structured regularizer exploiting
    compositional structure of preprocessing interventions
    """
    laplacian = np.diag(adjacency_matrix.sum(1)) - adjacency_matrix
    smoothness = lambda_reg * trace(model_weights.T @ laplacian @ model_weights)
    return loss + smoothness
```

## Pipeline Interventions (7 binary factors)
1. Filtering (bandpass vs wideband)
2. Re-referencing (average vs common)
3. Artifact removal (ICA vs none)
4. Epoching window length
5. Baseline correction
6. Normalization method
7. Downsampling rate

## Key Findings
- Sensitivity is near-additive under binary intervention design
- PU captures instability complementary to model-based confidence
- Standard uncertainty methods don't quantify preprocessing instability
- NA-PGI reduces sensitivity but has clear scope conditions

## Best Practices
1. Always report preprocessing pipeline details in publications
2. Use PU as per-trial diagnostic alongside model confidence
3. Test at least 2-3 preprocessing variations before deployment
4. Walsh-Hadamard decomposition enables efficient pipeline optimization

## Error Handling
### High PU Detected
If PU > 0.3 on critical trials:
- Expand pipeline search space
- Consider ensemble across pipelines
- Flag predictions as unreliable

### Pipeline Space Too Large
For k > 10 interventions:
- Use fractional factorial design
- Apply screening methods to identify dominant factors
- Focus on main effects (usually sufficient)

## References
- arXiv:2605.07212 - "Same Brain, Different Prediction" (Hou et al., May 2026)
