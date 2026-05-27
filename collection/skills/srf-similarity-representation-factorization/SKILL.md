---
name: srf-similarity-representation-factorization
description: Similarity-Based Representation Factorization (SRF) methodology for recovering low-dimensional, non-negative, interpretable embeddings from similarity matrices
version: 1.0.0
author: Hermes Agent
created: 2026-05-28
arxiv_id: 2605.26921
tags: [representation-learning, dimensionality-reduction, similarity-matrix, interpretability, neuroscience, brain-representation, ai-alignment]
activation_keywords: [srf, similarity-based representation, representation factorization, interpretable embeddings, brain representation, neural representation, similarity matrix, representation dimensions]
---

# Similarity-Based Representation Factorization (SRF)

## Overview

SRF (Similarity-Based Representation Factorization) is a general computational method for recovering low-dimensional, non-negative, interpretable embeddings from similarity matrices derived from measured data. It addresses the fundamental challenge of understanding the dimensions that shape representations across neuroscience, psychology, and artificial intelligence.

## Key Innovation

**From Similarity Matrices to Interpretable Dimensions**
- Recovers low-dimensional embeddings directly from similarity data
- Non-negative factorization for interpretability
- Works with sparsely sampled, incomplete data
- General-purpose method across diverse data types

## Core Problem Addressed

Current representation analysis methods:
- Study representations through similarities between stimuli
- Provide limited access to underlying dimensions
- Often lack interpretability
- Cannot handle sparse/incomplete data well

SRF solution:
- Direct dimension recovery from similarity matrices
- Interpretable non-negative embeddings
- Robust to sparse sampling
- Higher power for hypothesis testing

## Technical Framework

### Mathematical Foundation

**SRF Factorization:**
```
Given similarity matrix S ∈ ℝⁿˣⁿ
Find: S ≈ F · Fᵀ
Where: F ∈ ℝⁿˣᵏ (k dimensions)
Constraint: F ≥ 0 (non-negative)
```

**Key Properties:**
- Low-dimensional representation (k << n)
- Non-negative factors for interpretability
- Interprets each dimension as a distinct representation feature
- Preserves similarity structure in factorized form

### Algorithm Steps

1. **Similarity Matrix Construction**
   - Compute pairwise similarities from neural/behavioral/AI data
   - Handle sparse/incomplete sampling
   - Normalize similarity structure

2. **Dimension Selection**
   - Determine optimal number of dimensions k
   - Use cross-validation or information criteria
   - Balance interpretability vs accuracy

3. **Non-Negative Factorization**
   - Apply NMF-like optimization
   - Constrain factors to be non-negative
   - Ensure each dimension interpretable

4. **Interpretability Analysis**
   - Map dimensions to meaningful features
   - Validate against task-specific models
   - Predict independent behavioral properties

5. **Hypothesis Testing**
   - Compare dimensions across conditions
   - Higher statistical power than similarity comparison
   - Confirmatory analysis with recovered dimensions

### Validation Across Domains

**Neural Data:**
- Matches dimensions from task-specific models
- Predicts independent behavioral properties
- Works with sparse neural recordings

**Behavioral Data:**
- Recovers interpretable psychological dimensions
- Improves exploratory analysis
- Supports confirmatory hypothesis testing

**AI Representations:**
- Reveals dimensions in neural network embeddings
- Enables cross-model representation comparison
- Provides interpretability for deep learning

## Applications

### Neuroscience
- Brain representation analysis
- Neural coding dimension recovery
- Cross-region representation comparison

### Psychology
- Behavioral representation study
- Cognitive dimension identification
- Task performance dimension analysis

### AI Alignment
- Understanding neural network representations
- Model representation comparison
- Interpretability analysis

### Representation Comparison
- Brain vs AI alignment studies
- Behavioral vs neural representation mapping
- Cross-domain representation analysis

## Implementation Considerations

### Data Requirements
- Similarity matrix from any data type
- Handles sparse/incomplete data
- No need for complete stimulus coverage

### Dimension Selection Strategies
- Cross-validation for optimal k
- Information criteria (AIC, BIC)
- Interpretability-driven selection

### Interpretability Enhancement
- Non-negative constraint ensures positive dimensions
- Each factor corresponds to meaningful feature
- Direct mapping to cognitive/neural properties

### Statistical Power
- Higher power for hypothesis testing than similarity comparison
- Direct dimension-level analysis
- Reduced multiple comparison burden

## Methodology Steps

1. **Collect Similarity Data**
   - Neural similarity: from brain activity patterns
   - Behavioral similarity: from task performance/judgments
   - AI similarity: from model embeddings

2. **Construct Similarity Matrix**
   - Pairwise similarity computation
   - Handle missing data appropriately
   - Normalize across data types

3. **Apply SRF Factorization**
   ```python
   from sklearn.decomposition import NMF
   
   # SRF factorization
   model = NMF(n_components=k, init='nndsvda', random_state=42)
   F = model.fit_transform(S)  # Factor matrix
   reconstruction = F @ F.T     # Approximate S
   ```

4. **Analyze Recovered Dimensions**
   - Map factors to meaningful features
   - Validate against known representations
   - Predict independent behavioral measures

5. **Confirmatory Hypothesis Testing**
   - Test specific dimension hypotheses
   - Compare across conditions/models
   - Statistical inference on factor values

## Pitfalls and Considerations

- **Dimension Selection**: Choosing k balances interpretability vs accuracy
- **Sparse Data**: Robust to sparse sampling, but very sparse may require regularization
- **Interpretability**: Non-negative constraint helps, but requires domain knowledge to interpret
- **Statistical Assumptions**: Requires appropriate hypothesis testing framework
- **Cross-Validation**: Use proper validation strategy for dimension selection

## Code Examples

### SRF Factorization
```python
import numpy as np
from sklearn.decomposition import NMF

def srf_factorization(similarity_matrix, k=None, cross_validate=True):
    """
    Apply Similarity-Based Representation Factorization
    
    Args:
        similarity_matrix: Pairwise similarity matrix S ∈ ℝⁿˣⁿ
        k: Number of dimensions (auto-detect if None)
        cross_validate: Use cross-validation for k selection
    
    Returns:
        F: Factor matrix with k interpretable dimensions
    """
    if k is None and cross_validate:
        # Cross-validate to find optimal k
        k = select_dimensions_cv(similarity_matrix)
    
    # Non-negative factorization
    model = NMF(n_components=k, init='nndsvda', max_iter=200)
    F = model.fit_transform(similarity_matrix)
    
    # Reconstruction error
    reconstruction = F @ F.T
    error = np.linalg.norm(similarity_matrix - reconstruction)
    
    return F, k, error

def select_dimensions_cv(S, k_range=range(2, 20)):
    """Cross-validation for dimension selection"""
    best_k = 2
    best_score = float('inf')
    
    for k in k_range:
        # Split similarity matrix for CV
        score = cross_validate_nmf(S, k)
        if score < best_score:
            best_k = k
            best_score = score
    
    return best_k
```

### Dimension Interpretation
```python
def interpret_dimensions(F, stimuli_labels, feature_names=None):
    """
    Interpret recovered dimensions
    
    Args:
        F: Factor matrix (n stimuli × k dimensions)
        stimuli_labels: Labels for each stimulus
        feature_names: Optional names for dimensions
    
    Returns:
        dimension_interpretations: Mapping of dimensions to features
    """
    interpretations = {}
    
    for dim_idx in range(F.shape[1]):
        # Find stimuli with high values on this dimension
        high_loading = F[:, dim_idx] > np.percentile(F[:, dim_idx], 90)
        characteristic_stimuli = stimuli_labels[high_loading]
        
        # Interpret dimension based on characteristic stimuli
        interpretation = infer_feature(characteristic_stimuli)
        interpretations[dim_idx] = {
            'feature': interpretation,
            'characteristic_stimuli': characteristic_stimuli,
            'loadings': F[:, dim_idx]
        }
    
    return interpretations
```

## References

- arXiv:2605.26921 - Revealing the core dimensions underlying representations in brains, behavior and AI
- NMF literature for factorization algorithms
- Representation similarity analysis (RSA) for background

## Related Skills

- [[brain-dnn-alignment]] - Brain-DNN representation alignment
- [[representation-similarity-analysis]] - RSA methodology
- [[neural-representation-analysis]] - Neural representation analysis methods
- [[interpretability-methods]] - General interpretability techniques