---
name: srf-similarity-representation-factorization
version: "1.0"
description: "Similarity-Based Representation Factorization (SRF) — a computational method for recovering low-dimensional, non-negative, interpretable embeddings from similarity matrices derived from brains, behavior, and AI models. Reveals shared and unique representational dimensions across systems."
triggers:
  - "SRF representation factorization"
  - "similarity-based representation"
  - "core dimensions brain AI"
  - "representational geometry factorization"
  - "brain behavior AI alignment"
  - "non-negative embedding brain"
  - "representational similarity analysis interpretable"
  - "cross-system representation alignment"
tags:
  - neuroscience
  - representational-similarity
  - brain-AI-alignment
  - interpretability
  - dimensionality-reduction
  - NMF
  - fMRI
  - vision
arxiv: "2605.26921"
source: "Revealing the core dimensions underlying representations in brains, behavior and AI (2026)"
---

# SRF: Similarity-Based Representation Factorization

## Overview

**SRF (Similarity-Based Representation Factorization)** is a general framework for discovering the low-dimensional, interpretable, non-negative "core dimensions" that underlie similarity structures in:
- Neural population activity (fMRI, EEG, single-unit recordings)
- Human behavioral judgments
- AI model activations (vision, language)

Unlike standard RSA or PCA, SRF operates directly on **similarity matrices** and produces non-negative dimensions that are semantically interpretable (additive parts-based decomposition).

## Core Methodology

### Input: Similarity Matrix
Given N stimuli, compute a pairwise similarity matrix S ∈ ℝ^{N×N} where S_{ij} = similarity(stimulus_i, stimulus_j).

Sources:
- Neural: 1 - (Euclidean distance / max) in activation space
- Behavioral: triplet judgments, rating scales
- AI: cosine similarity in layer activations

### Factorization Model
SRF decomposes S into a product of non-negative embeddings:

```
S ≈ W · W^T    where W ∈ ℝ^{N×K}, W ≥ 0
```

- K = number of latent dimensions (selected by cross-validation)
- W_{i,k} = degree to which stimulus i loads on dimension k
- Dimensions are additive, non-overlapping (unlike PCA)

### Optimization Objective
```
minimize  ||S - W·W^T||²_F + λ·||W||₁   subject to W ≥ 0
```

Solved via projected gradient descent or HALS-NMF variant.

### Algorithm
```python
def srf(S, K, n_iter=1000, lr=0.01, lambda_l1=0.001):
    """
    Similarity-Based Representation Factorization
    S: (N, N) symmetric non-negative similarity matrix
    K: number of latent dimensions
    Returns W: (N, K) non-negative embeddings
    """
    N = S.shape[0]
    # Initialize W with small non-negative values
    W = np.abs(np.random.randn(N, K)) * 0.1
    
    for _ in range(n_iter):
        # Compute reconstruction
        S_hat = W @ W.T
        
        # Gradient of Frobenius loss
        grad = -2 * (S - S_hat) @ W
        
        # L1 sparsity gradient
        grad += lambda_l1 * np.sign(W)
        
        # Gradient step
        W -= lr * grad
        
        # Project to non-negative orthant
        W = np.maximum(W, 0)
    
    return W
```

## Interpretability of Dimensions

Each SRF dimension k corresponds to a "proto-concept":
- Identify top-loading stimuli: `top_k = np.argsort(W[:, k])[-10:]`
- Label dimension by semantic consensus of top stimuli
- Example dimensions found in vision: roundness, animacy, color, texture

### Dimension Alignment Across Systems
```python
def align_representations(W1, W2, method='hungarian'):
    """
    Align SRF dimensions between two systems (brain vs. AI)
    W1, W2: (N, K) embeddings from different systems
    """
    from scipy.optimize import linear_sum_assignment
    from scipy.spatial.distance import cdist
    
    # Cost matrix: distance between dimensions
    cost = cdist(W1.T, W2.T, metric='correlation')
    row_ind, col_ind = linear_sum_assignment(cost)
    
    aligned_W2 = W2[:, col_ind]
    alignment_score = 1 - cost[row_ind, col_ind].mean()
    
    return aligned_W2, alignment_score, col_ind
```

## Cross-System Comparison

### Brain vs. AI Shared Dimensions
1. Run SRF on brain similarity matrix → W_brain (N×K)
2. Run SRF on AI similarity matrix → W_AI (N×K)
3. Align dimensions via Hungarian algorithm
4. Compute correlation per dimension: r_k = corr(W_brain[:, k], W_AI[:, k])
5. Shared dimensions: r_k > 0.5; unique dimensions: r_k < 0.2

### Multi-System Joint SRF
```python
def joint_srf(similarity_matrices, K_shared, K_unique, n_iter=2000):
    """
    Decompose multiple similarity matrices jointly.
    Returns shared dimensions W_shared and system-specific W_unique_i
    """
    # Concatenate similarity matrices block-diagonally for unique dims
    # Jointly optimize shared component across all systems
    pass  # See paper for full formulation
```

## Applications

### 1. Identifying Brain Region Specialization
- Compare SRF dimensions across V1, V4, IT, PFC
- Unique IT dimensions: object identity
- Shared V1+V4 dimensions: low-level features

### 2. Model Evaluation
- Which AI model dimensions align with human brain dimensions?
- Quantify alignment score per layer, per dimension
- Find "missing" dimensions in AI vs. brain

### 3. Behavioral Geometry
- Recover dimensions underlying human similarity judgments
- Compare with neural geometry: do people judge by the same axes the brain uses?

## Key Findings from Paper

1. **Low-K sufficiency**: 10-20 dimensions capture >80% of similarity variance for natural image sets
2. **Shared brain-AI core**: ~6-8 dimensions shared between human visual cortex and top CNN layers
3. **Behavioral uniqueness**: Human judgments emphasize semantic/functional dimensions not prominent in early visual areas
4. **Interpretability advantage**: SRF dimensions are more semantically coherent than PCA components

## When to Use

- Comparing representations across brains, models, and behavior
- Discovering what "features" a neural population is encoding
- Evaluating if an AI model captures human-like representational structure
- Building interpretable encoding models

## Pitfalls

- **K selection**: Use held-out stimuli for cross-validation; BIC/AIC also applicable
- **Negative similarities**: SRF requires non-negative S; use S = (S_raw - min) / (max - min)
- **Permutation non-uniqueness**: Dimensions are unordered; always use alignment before comparing
- **Rotation ambiguity**: W·W^T = (W·R)(W·R)^T for any rotation R; enforce uniqueness via sparsity
- **Stimulus set bias**: Dimensions depend on the stimulus distribution; match sets across systems

## Related Methods

- NMF (Lee & Seung 1999) — operates on data matrix, not similarity
- RSA (Kriegeskorte 2008) — compares but does not factorize similarity structures  
- UMAP/t-SNE — non-linear embedding, not interpretable dimensions
- Sparse Coding — related for neural coding, but not for similarity matrices
