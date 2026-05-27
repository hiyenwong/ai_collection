---
name: srf-similarity-representation-factorization
description: Similarity-Based Representation Factorization (SRF) - computational method for recovering interpretable low-dimensional embeddings from similarity matrices across neural, behavioral, and AI data.
version: 1.0.0
category: brain-ai-alignment
activation_keywords:
  - representation factorization
  - similarity matrix
  - interpretable embeddings
  - brain-AI alignment
  - neural representation
  - behavioral dimensions
  - non-negative factorization
author: arXiv:2605.26921
paper_title: Revealing the core dimensions underlying representations in brains, behavior and AI
paper_authors: Florian P. Mahner, Ka Chun Lam, Francisco Pereira, Martin N. Hebart
paper_date: 2026-05-27
arxiv_id: 2605.26921
---

# Similarity-Based Representation Factorization (SRF)

## Overview

General computational method for recovering low-dimensional, non-negative, interpretable embeddings from similarity matrices derived from neural, behavioral, and AI data. Enables extraction of core dimensions underlying representations across diverse domains.

**Core Innovation**: First unified method for interpretable dimension recovery from similarity matrices, working with sparse/incomplete data and providing higher statistical power than traditional similarity comparisons.

## When to Use

Use this skill when:
- Analyzing neural representations from brain imaging data
- Comparing behavioral representations across tasks
- Studying AI model representations and alignment
- Recovering interpretable dimensions from similarity data
- Working with sparsely sampled or incomplete datasets
- Improving hypothesis testing power over similarity matrix comparison

Trigger words: representation factorization, SRF, similarity matrix, interpretable embedding, brain-AI alignment, dimension recovery.

## Core Methodology

### Key Advantages

1. **Interpretability**: Non-negative embeddings with clear semantic meaning
2. **Robustness**: Works with sparse, incomplete similarity matrices
3. **Power**: Higher statistical power than comparing full similarity matrices
4. **Generalization**: Validated across neural, behavioral, AI datasets

### Mathematical Framework

Given similarity matrix $S \in \mathbb{R}^{n \times n}$ (positive):

$$S \approx W W^T$$

where $W \in \mathbb{R}^{n \times k}_{\geq 0}$ is the non-negative embedding matrix with $k$ interpretable dimensions.

Optimization objective:
$$\min_{W \geq 0} \|S - W W^T\|_F^2 + \lambda \|W\|_1$$

### SRF Algorithm

**Input**: Similarity matrix $S$, desired dimensionality $k$

**Output**: Non-negative embeddings $W$ for each stimulus

**Steps**:
1. Initialize $W$ with positive values
2. Apply multiplicative update rules (non-negative matrix factorization)
3. Constrain column norms for interpretability
4. Iterate until convergence

## Implementation

### Step 1: Similarity Matrix Construction

```python
import numpy as np

def construct_similarity_matrix(representations):
    """
    Build similarity matrix from representations.
    
    Parameters:
    - representations: array (n_stimuli, n_features)
    
    Returns:
    - S: similarity matrix (n_stimuli, n_stimuli)
    """
    # Normalize representations
    reps_norm = representations / np.linalg.norm(representations, axis=1, keepdims=True)
    
    # Compute pairwise similarity (cosine)
    S = reps_norm @ reps_norm.T
    
    # Ensure positive values
    S = (S + 1) / 2  # shift to [0, 1] range
    
    return S
```

### Step 2: SRF Factorization

```python
def srf_factorize(S, k, max_iter=100, tol=1e-6):
    """
    Perform SRF factorization on similarity matrix.
    
    Parameters:
    - S: similarity matrix (n, n), positive
    - k: number of dimensions to recover
    - max_iter: maximum iterations
    - tol: convergence tolerance
    
    Returns:
    - W: non-negative embeddings (n, k)
    """
    n = S.shape[0]
    
    # Initialize W with random positive values
    W = np.abs(np.random.randn(n, k)) + 0.1
    
    for iteration in range(max_iter):
        W_old = W.copy()
        
        # Multiplicative update (NMF-style)
        # W <- W * (S @ W) / (W @ W.T @ W + epsilon)
        
        numerator = S @ W
        denominator = W @ W.T @ W + 1e-10
        
        W = W * numerator / denominator
        
        # Normalize columns for interpretability
        W = W / (W.sum(axis=0) + 1e-10)
        
        # Check convergence
        if np.linalg.norm(W - W_old) < tol:
            print(f"Converged at iteration {iteration}")
            break
    
    return W
```

### Step 3: Dimension Interpretation

```python
def interpret_dimensions(W, stimuli_labels, top_k=10):
    """
    Interpret recovered dimensions by top stimuli.
    
    Parameters:
    - W: embeddings (n_stimuli, k)
    - stimuli_labels: list of stimulus names
    - top_k: number of top stimuli per dimension
    
    Returns:
    - interpretations: dict mapping dimension to top stimuli
    """
    interpretations = {}
    
    for dim in range(W.shape[1]):
        # Find stimuli with highest weights on this dimension
        top_indices = np.argsort(W[:, dim])[-top_k:][::-1]
        top_stimuli = [stimuli_labels[i] for i in top_indices]
        top_weights = W[top_indices, dim]
        
        interpretations[f'Dimension {dim+1}'] = {
            'top_stimuli': top_stimuli,
            'weights': top_weights
        }
    
    return interpretations
```

### Step 4: Statistical Testing

```python
def test_dimension_relevance(W1, W2, null_distribution=None):
    """
    Test whether recovered dimensions are meaningful.
    
    Higher power than testing full similarity matrix.
    """
    # Compute dimension-wise statistics
    dim_correlation = np.corrcoef(W1.T, W2.T)[:W1.shape[1], W1.shape[1]:]
    
    # Compare to null distribution
    if null_distribution:
        p_values = (null_distribution > dim_correlation).mean()
    
    return dim_correlation, p_values
```

## Validated Applications

### Neural Data

- **fMRI**: Recover task-relevant dimensions from brain activity patterns
- **Neural recordings**: Extract interpretable features from population responses
- **EEG**: Identify core temporal patterns in similarity structure

### Behavioral Data

- **Psychology**: Recover latent dimensions from similarity judgments
- **Decision making**: Extract choice-relevant features
- **Perception**: Identify perceptual dimensions

### AI Data

- **DNN representations**: Recover interpretable dimensions from layer activations
- **Model comparison**: Compare dimensions across architectures
- **Brain-AI alignment**: Test whether AI dimensions match neural dimensions

## Key Findings

1. **Interpretability**: Recovered dimensions match task-specific model predictions
2. **Prediction**: Dimensions predict independent behavioral properties
3. **Exploration**: Improve exploratory analysis of representational structure
4. **Power**: Higher statistical power for hypothesis testing

## Practical Workflow

```python
# Full SRF pipeline
def srf_pipeline(data, labels, k=5):
    """Complete SRF analysis pipeline."""
    
    # 1. Compute similarity matrix
    S = construct_similarity_matrix(data)
    
    # 2. Factorize with SRF
    W = srf_factorize(S, k)
    
    # 3. Interpret dimensions
    interpretations = interpret_dimensions(W, labels)
    
    # 4. Visualize
    for dim, info in interpretations.items():
        print(f"\n{dim}:")
        for stim, weight in zip(info['top_stimuli'], info['weights']):
            print(f"  {stim}: {weight:.3f}")
    
    return W, interpretations
```

## Pitfalls & Solutions

| Pitfall | Solution |
|---------|----------|
| Negative similarities | Shift/clip to positive range |
| Too many dimensions | Use cross-validation to select k |
| Sparse data | SRF robust to incomplete matrices |
| Non-convergence | Increase iterations, adjust initialization |
| Uninterpretable dimensions | Check dimension normalization |

## Comparison to Alternatives

| Method | Interpretability | Sparse Data | Statistical Power |
|--------|-----------------|-------------|-------------------|
| SRF | ✓ Non-negative | ✓ Robust | ✓ High |
| RSA | ✗ No factors | ✗ Needs complete | ✗ Lower |
| PCA | ✗ Negative values | ✗ Needs complete | Medium |
| NMF | ✓ Non-negative | Medium | Medium |

## Related Skills

- [[rsa-representational-similarity-analysis]] - RSA methodology
- [[brain-ai-alignment]] - Brain-AI comparison
- [[neural-representation]] - Neural representation analysis
- [[interpretability-methods]] - Model interpretability

## References

1. Original paper: arXiv:2605.26921 (Mahner et al., 2026)
2. NMF foundations: Lee & Seung, Nature
3. RSA methodology: Kriegeskorte et al., Frontiers

## Summary

SRF provides first unified method for interpretable dimension recovery from similarity matrices across neural, behavioral, and AI data. Key advantages: non-negative interpretable embeddings, robust to sparse/incomplete data, higher statistical power than similarity matrix comparison. Validated across diverse datasets with dimensions matching task models and predicting independent behaviors.