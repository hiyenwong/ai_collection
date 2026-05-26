---
name: maximum-entropy-neural-connectivity
title: "Maximum Entropy Neural Connectivity for Context-Dependent Computation"
description: >
  Maximum entropy framework for deriving minimally-biased neural network connectivity
  that satisfies functional constraints for context-dependent computations. Reveals
  low-rank structures required for working memory, context integration, and task switching
  while keeping other connectivity aspects random.
tags:
  - neuroscience
  - neural-connectivity
  - maximum-entropy
  - context-dependent
  - low-rank-networks
  - working-memory
  - computational-neuroscience
  - brain-network
activation_keywords:
  - maximum entropy
  - neural connectivity
  - context-dependent computation
  - low-rank structure
  - functional connectivity
  - working memory network
  - cortical connectivity
source:
  arxiv: "2605.25607"
  authors: ["Ludwig Hruza", "Srdjan Ostojic"]
  published: "2026-05-25"
  category: "q-bio.NC"
---

# Maximum Entropy Neural Connectivity for Context-Dependent Computation

## Overview

A fundamental challenge in neuroscience is understanding which aspects of neural connectivity are functionally necessary vs. arbitrary artifacts of learning. This skill presents the **maximum entropy network** framework — a principled method to derive the least-biased connectivity consistent with required computational constraints.

**Core idea**: Rather than training networks via gradient descent (which introduces initialization biases), maximize network entropy subject to functional constraints. The result: connectivity with minimal structure, yet capable of the target computation.

## Methodology

### 1. Maximum Entropy Formulation

Given observed or desired functional statistics $\langle f_k \rangle$ (e.g., low-rank components, covariance structure):

$$P^*(W) = \frac{1}{Z} \exp\left(\sum_k \lambda_k f_k(W)\right)$$

where $\lambda_k$ are Lagrange multipliers found by matching constraints:
- Maximize Shannon entropy $H[P] = -\int P(W) \log P(W) dW$
- Subject to: $\mathbb{E}[f_k(W)] = \langle f_k \rangle$

### 2. Low-Rank Structure Identification

For context-dependent computations, decompose connectivity:
$$W = W_{\text{low-rank}} + W_{\text{random}}$$

- $W_{\text{low-rank}}$: Rank-$r$ component ($r \ll N$), functionally necessary
- $W_{\text{random}}$: Random Gaussian component, can be drawn independently

**Key finding**: Context-dependent tasks require specific low-rank structure; everything else can remain random.

### 3. Task-Specific Constraints

| Task | Required Structure | Rank |
|------|-------------------|------|
| Working Memory | Persistent activity modes | 1-2 |
| Context Integration | Input-output gating vectors | 2-3 |
| Flexible Task Switching | Modular subspaces | 3-5 |

### 4. Empirical Alignment

Maximum entropy networks align with cortical observations:
- Low-dimensional structure in prefrontal connectivity
- Mixed selectivity without over-specification
- Robustness to synaptic noise

## Implementation

```python
import numpy as np
from scipy.optimize import minimize

def maximum_entropy_connectivity(N, rank, target_statistics, n_samples=1000):
    """
    Derive maximum entropy connectivity matrix.
    
    Args:
        N: Number of neurons
        rank: Required low-rank component rank
        target_statistics: Dict of {stat_name: target_value}
        n_samples: Monte Carlo samples for optimization
    
    Returns:
        W: Connectivity matrix (N x N)
        W_lr: Low-rank component
        W_rand: Random component
    """
    # Initialize Lagrange multipliers
    lambdas = np.zeros(rank * 2)  # For U, V in low-rank W = U @ V.T
    
    def neg_entropy_minus_constraints(lambdas):
        """Objective: negative entropy + constraint penalty"""
        # Sample from current distribution
        U = np.random.randn(n_samples, N, rank)
        V = np.random.randn(n_samples, N, rank)
        
        # Low-rank component
        W_lr_samples = np.einsum('snr,smr->snm', U, V) / np.sqrt(rank)
        
        # Compute statistics
        loss = 0
        for k, (stat_name, target) in enumerate(target_statistics.items()):
            computed = compute_statistic(W_lr_samples, stat_name)
            loss += lambdas[k] * (computed - target)**2
        
        return loss
    
    # Optimize Lagrange multipliers
    result = minimize(neg_entropy_minus_constraints, lambdas, method='L-BFGS-B')
    
    # Sample final connectivity
    U_opt = np.random.randn(N, rank) * result.x[:rank]
    V_opt = np.random.randn(N, rank) * result.x[rank:]
    W_lr = U_opt @ V_opt.T / np.sqrt(rank)
    W_rand = np.random.randn(N, N) / np.sqrt(N)
    
    W = W_lr + W_rand
    return W, W_lr, W_rand


def compute_statistic(W_samples, stat_name):
    """Compute connectivity statistics."""
    if stat_name == 'spectral_radius':
        eigenvalues = np.linalg.eigvals(W_samples.mean(0))
        return np.max(np.abs(eigenvalues))
    elif stat_name == 'participation_ratio':
        # Effective dimensionality
        cov = np.cov(W_samples.reshape(W_samples.shape[0], -1).T)
        evals = np.linalg.eigvalsh(cov)
        return (np.sum(evals)**2) / np.sum(evals**2)
    return 0.0
```

### Working Memory Network Example

```python
# Context-dependent working memory with maximum entropy connectivity
def working_memory_constraints():
    """Define constraints for working memory computation."""
    return {
        'spectral_radius': 0.9,           # Near-critical dynamics
        'low_rank_variance': 0.8,          # High variance in low-rank modes
        'excitatory_fraction': 0.8,        # Dale's law approximation
    }

# Build network
N = 200
rank = 2
constraints = working_memory_constraints()
W, W_lr, W_rand = maximum_entropy_connectivity(N, rank, constraints)

# Verify: low-rank structure captures functional modes
U, s, Vt = np.linalg.svd(W_lr)
print(f"Top singular values: {s[:5]}")  # Should show 2 dominant values
print(f"Random component variance: {np.var(W_rand):.4f}")
```

## Key Results and Insights

### 1. Minimal Structure Principle
Only the task-critical low-rank modes need to be specified. The remaining ~95% of connectivity can be random without affecting performance.

### 2. Universality Across Tasks
Maximum entropy analysis reveals that diverse cognitive tasks share a common motif: **selective amplification** via low-rank connectivity, superimposed on random background.

### 3. Biological Plausibility
- Consistent with observed low-dimensional structure in cortical recordings
- Explains why different animals performing the same task show different detailed connectivity but similar function
- Predicts which synapses are "functionally critical" vs. redundant

### 4. Implications for Neuroscience
- Provides principled method to identify functionally necessary connectivity
- Bridges connectomics and neural dynamics
- Guides perturbation experiments: disrupting low-rank modes should impair computation

## Applications

1. **Connectomics Analysis**: Identify low-rank signal in empirical connectivity matrices
2. **Network Design**: Generate minimally-structured networks for cognitive tasks  
3. **Lesion Predictions**: Predict which connectivity perturbations disrupt function
4. **Comparison Across Species**: Compare functional structure while ignoring irrelevant variability

## Relation to Existing Work

- Extends low-rank RNN literature (Mastrogiuseppe & Ostojic, 2018; Schuessler et al., 2020)
- Complements gradient-descent trained networks by removing initialization bias
- Related to random matrix theory approaches to neural dynamics
- Connects to information-theoretic frameworks for neural coding

## Pitfalls

- Maximum entropy requires knowing which statistics to constrain — domain expertise needed
- Computational cost scales with network size for Monte Carlo estimation
- Low-rank approximation may miss higher-order interaction effects
- Biological networks may have additional constraints not captured by functional tasks alone

## Citation

```bibtex
@article{hruza2026maximum,
  title={Balancing structure and randomness: maximum entropy networks for context-dependent computations},
  author={Hruza, Ludwig and Ostojic, Srdjan},
  journal={arXiv preprint arXiv:2605.25607},
  year={2026}
}
```
