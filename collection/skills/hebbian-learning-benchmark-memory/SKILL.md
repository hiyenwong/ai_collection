---
name: hebbian-learning-benchmark-memory
description: "Benchmarking 7 local Hebbian learning rules for associative memory storage and prototype extraction. Bayesian-Hebbian rules achieve highest capacity. Activation: hebbian learning benchmark, associative memory capacity, prototype extraction, Bayesian-Hebbian learning, covariance learning."
---

# Hebbian Learning Rules Benchmark for Associative Memory

## Paper Reference

- **Title:** Benchmarking local Hebbian learning rules for memory storage and prototype extraction
- **Authors:** Anders Lansner, Andreas Knoblauch, Naresh B Ravichandran, Pawel Herman
- **arXiv:** 2605.01074v1 (May 2026)
- **Categories:** cs.NE, cs.LG
- **URL:** https://arxiv.org/abs/2605.01074v1

## Core Problem

Associative memory (content-addressable memory) is fundamental to both computer science and cognitive/brain science. A key but understudied capability is **prototype extraction**: recalling correct prototypes from distorted training instances.

## Benchmark Setup

### Architecture
- **Non-modular and modular recurrent networks** with winner-take-all (WTA) dynamics
- **Moderately sparse binary patterns** as input representations

### 7 Hebbian Learning Rules Tested

1. **Additive Hebb** (original): wᵢⱼ += xᵢxⱼ
2. **Covariance Learning**: wᵢⱼ += (xᵢ - μᵢ)(xⱼ - μⱼ)
3. **Bayesian-Hebbian** (multiple variants): Based on Bayesian inference principles

### Metrics Measured

| Metric | Description |
|--------|-------------|
| Pattern Storage Capacity | Max patterns stored and correctly recalled |
| Weight Information Capacity | Information stored per synapse |
| Prototype Extraction | Ability to recall clean prototype from noisy inputs |
| Correlation Sensitivity | Robustness to correlated data |

## Results Summary

### Ranking by Capacity

| Rank | Rule | Capacity | Robustness |
|------|------|----------|------------|
| 🥇 | **Bayesian-Hebbian** | Highest | High |
| 🥈 | Covariance Learning | Moderate | Robust |
| 🥉 | Other variants | Variable | Variable |
| 4 | Additive Hebb (original) | Worst | Poor |

### Key Findings

1. **Additive Hebb rule performs worst** across all capacity measures
2. **Covariance learning is robust** but has moderate capacity
3. **Bayesian-Hebbian rules achieve highest capacity** in almost all tested conditions
4. **Prototype extraction capability** correlates with storage capacity
5. **Correlated data sensitivity** varies significantly across rules

## Bayesian-Hebbian Learning

### Principle

Bayesian-Hebbian learning derives weight updates from Bayesian inference:
- Weights represent conditional probabilities
- Learning updates follow Bayes' rule
- Naturally handles sparse, correlated data

### Advantages
- Higher storage capacity
- Better prototype extraction
- More robust to data correlations
- Theoretically grounded in probabilistic inference

## Applications

- **Associative Memory Systems**: Content-addressable memory in neuromorphic hardware
- **Prototype Learning**: Learning canonical representations from noisy data
- **Figure-Ground Segmentation**: Perceptual organization tasks
- **Perceptual Reconstruction**: Filling in missing information
- **Cognitive Modeling**: Brain-inspired memory architectures

## Implementation Pattern

```python
# Additive Hebb (baseline)
def additive_hebb(X):
    """X: binary patterns (n_samples, n_features)"""
    return X.T @ X / X.shape[0]

# Covariance Learning
def covariance_hebb(X):
    X_centered = X - X.mean(axis=0)
    return X_centered.T @ X_centered / X.shape[0]

# Bayesian-Hebbian (simplified)
def bayesian_hebb(X, prior=0.5):
    """Bayesian-Hebbian with prior probability"""
    n, d = X.shape
    p_i = X.mean(axis=0)  # marginal probabilities
    p_ij = (X.T @ X) / n  # joint probabilities
    # Conditional probability-based weights
    W = np.log((p_ij + eps) / (p_i[:, None] * p_j[None, :] + eps) + eps)
    return W
```

## Modular vs Non-Modular Networks

| Aspect | Modular | Non-Modular |
|--------|---------|-------------|
| Capacity | Higher (with proper modularity) | Lower |
| Interference | Reduced between modules | Higher |
| Scalability | Better | Limited |
| Biological plausibility | High (cortical columns) | Moderate |

## WTA Dynamics

Winner-take-all dynamics in recurrent networks:
- Competitive activation among neurons
- Only strongest pattern wins
- Enables content-addressable recall
- Prevents spurious attractor states

## Pitfalls

- **Pattern correlation**: High correlation between stored patterns degrades all rules
- **Capacity limits**: All rules have fundamental capacity bounds
- **Sparsity tuning**: Moderately sparse patterns work best; too dense or too sparse hurts
- **Modularity design**: Improper modular partitioning can hurt more than help
- **WTA convergence**: WTA dynamics may not converge for very similar patterns

## Relation to Existing Skills

- `mpcs-neuroplastic-continual-learning`: MPCS uses Hebbian updates as one of 11 mechanisms
- `feedback-hebbian-continual-learning`: Hebbian learning in continual learning context
- `kernel-hopfield-associative-memory`: Attractor-based associative memory
- `hippo-multi-attractor-memory`: Multi-attractor memory models

## Activation Keywords

- hebbian learning benchmark
- associative memory capacity
- prototype extraction neural network
- Bayesian-Hebbian learning
- covariance learning rule
- WTA recurrent network
- content-addressable memory
- pattern storage capacity
