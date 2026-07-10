---
name: conjugacy-based-similarity-analysis
description: Conjugacy-based Similarity Analysis (CSA) methodology for comparing dynamical systems in neuroscience and ML. Addresses limitations of Dynamical Similarity Analysis (DSA) by restricting alignments to state-space bijections rather than arbitrary orthogonal matrices.
version: 1.0.0
date: 2026-07-08
source: arXiv:2607.04493
authors: Prakhar Godara, Pang Shiang Tay, Marcelo G. Mattar
tags: [dynamical-systems, neuroscience, koopman-theory, conjugacy, similarity-analysis, neural-dynamics]
---

# Conjugacy-based Similarity Analysis (CSA)

## Overview

CSA is a methodology for comparing whether two dynamical systems implement the same computation despite differences in coordinates or measurements. It addresses fundamental limitations of Dynamical Similarity Analysis (DSA) in neuroscience and machine learning.

## Core Problem

Comparing dynamical systems is central to neuroscience and ML:
- Do two neural networks implement the same computation?
- Are two brain regions performing similar operations?
- How do we measure similarity when systems use different coordinates?

## DSA Limitations

**Dynamical Similarity Analysis (DSA)** aligns finite-dimensional Koopman approximations through orthogonal similarity transformations.

**Key Insight**: Orthogonal alignment is **neither necessary nor sufficient** for topological conjugacy:
1. Conjugate systems may require **non-orthogonal** basis-transfer matrices that DSA cannot capture
2. Non-conjugate systems may have **orthogonally equivalent** Koopman operators that DSA fails to distinguish

## CSA Methodology

### Core Principle
CSA restricts alignments to those **induced by candidate state-space bijections** rather than arbitrary orthogonal matrices.

### Mathematical Foundation
- CSA's fitted alignment is the **finite-data projection of the composition operator** associated with the candidate bijection
- This ensures the alignment respects the actual state-space mapping between systems

### Key Theoretical Result
**Theorem**: CSA's alignment matrix equals the projection of the Koopman composition operator onto the observable dictionary space.

## When to Use CSA

### Appropriate Scenarios
1. **Comparing neural recordings** from different brain regions or subjects
2. **Validating computational models** against biological data
3. **Analyzing RNN dynamics** to identify functional equivalences
4. **Studying neural manifolds** across experimental conditions

### Inappropriate Scenarios
- When systems have fundamentally different state-space dimensions
- When no reasonable bijection hypothesis exists
- For purely statistical similarity without mechanistic interpretation

## Implementation Steps

### 1. Define Candidate Bijection
```python
# Example: Linear bijection hypothesis
def candidate_bijection(x, A, b):
    """Affine transformation between state spaces"""
    return A @ x + b
```

### 2. Compute Koopman Operators
```python
def compute_koopman(data, observables):
    """
    data: (T, n_features) time series
    observables: function mapping state to observation space
    """
    # Construct Koopman matrix from data
    K = least_squares_fit(observables(data[:-1]), observables(data[1:]))
    return K
```

### 3. Fit CSA Alignment
```python
def csa_alignment(K1, K2, bijection_params):
    """
    K1, K2: Koopman operators from two systems
    bijection_params: parameters of candidate bijection
    """
    # Compute composition operator
    C = composition_operator(K1, K2, bijection_params)
    # Project onto observable space
    alignment = project_to_observables(C)
    return alignment
```

### 4. Evaluate Conjugacy Quality
```python
def conjugacy_error(K1, K2, alignment):
    """Measure how well alignment satisfies conjugacy relation"""
    # ||K1 - A^{-1} K2 A||_F
    error = norm(K1 - inv(alignment) @ K2 @ alignment)
    return error
```

## Comparison with DSA

| Aspect | DSA | CSA |
|--------|-----|-----|
| Alignment constraint | Orthogonal matrices | State-space bijections |
| Captures conjugacy | No (only orthogonal equivalence) | Yes (by construction) |
| False positives | Possible (non-conjugate systems) | Avoided |
| False negatives | Possible (conjugate but non-orthogonal) | Avoided |
| Interpretability | Limited | Direct mechanistic meaning |

## Practical Considerations

### Observable Dictionary Selection
- **Critical**: Results depend heavily on observable choice
- Use domain knowledge to select meaningful observables
- Test robustness across different observable sets

### Finite Data Effects
- CSA alignment is a **finite-data projection**
- Convergence guarantees require sufficient data
- Use cross-validation to assess stability

### Computational Cost
- More expensive than DSA due to bijection optimization
- Parallelize over candidate bijections
- Use warm starts from DSA solution

## Applications in Neuroscience

### Neural Population Analysis
Compare population dynamics across:
- Different experimental conditions
- Brain regions performing similar computations
- Species with homologous circuits

### Model Validation
Test whether computational models capture:
- Qualitative dynamics (fixed points, limit cycles)
- Quantitative trajectories
- Response to perturbations

### Learning and Plasticity
Track how neural representations evolve:
- During learning
- Across development
- After injury/recovery

## Pitfalls and Limitations

1. **Bijection hypothesis**: CSA assumes a bijection exists; if wrong, results are meaningless
2. **Observability**: Systems must be sufficiently observed; hidden states break assumptions
3. **Noise sensitivity**: Finite data + noise can obscure true conjugacies
4. **Computational scaling**: High-dimensional systems require careful optimization

## Related Methods

- **Dynamical Similarity Analysis (DSA)**: Orthogonal Koopman alignment
- **Representational Similarity Analysis (RSA)**: Compare representational geometries
- **Procrustes analysis**: Shape comparison under rigid transformations
- **Optimal transport**: Distribution-level comparisons

## References

- Godara, P., Tay, P. S., & Mattar, M. G. (2026). Beyond DSA: Conjugacy-based Comparison of Dynamical Systems. arXiv:2607.04493
- Ostrow, E., et al. (2023). Dynamical Similarity Analysis. 

## Activation Triggers

Use this skill when:
- Comparing neural dynamics across conditions/subjects
- Validating computational models against neural data
- Analyzing RNN internal representations
- Studying neural manifold structure
- Keywords: dynamical systems, Koopman, conjugacy, similarity analysis, neural comparison
