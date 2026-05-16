---
name: quantum-inspired-lottery-tickets
description: "Quantum-inspired classical algorithm for finding winning lottery tickets (sparse subnetworks) in neural networks via ridgelet transform sampling. Runs in O(poly(D)) time, matching quantum sampling quality classically. Use when: neural network pruning, finding sparse subnetworks, lottery ticket hypothesis, quantum-inspired ML, ridgelet transform, or efficient neural architecture search."
---

# Quantum-Inspired Lottery Tickets

## Overview

The "lottery ticket hypothesis" states that dense neural networks contain sparse subnetworks that can match full-network performance. Finding these subnetworks classically is exponential in data dimension D. A quantum algorithm achieved O(D) sampling time, but this skill implements a **fully classical** O(poly(D)) alternative using the ridgelet transform — matching quantum quality without quantum hardware.

**Key result**: O(poly(D)) runtime with empirical risk comparable to optimal sampling, vs. exp(O(D)) naive classical approach.

## Ridgelet Transform for Network Pruning

### Core Idea

A shallow neural network with hidden layer parameters {(a_i, b_i)} and output weights {c_i} can be represented via the ridgelet transform:

```
f(x) = ∫ c(a,b) · σ(a·x + b) dμ(a,b)
```

The ridgelet transform `c(a,b)` provides an **optimized probability distribution** for sampling which hidden nodes to keep.

### Algorithm

```python
def quantum_inspired_lottery_ticket(X, y, n_hidden, sparsity_ratio, hidden_layer_width=10000):
    """
    Find winning lottery ticket via quantum-inspired ridgelet sampling.
    
    X: input data (N × D)
    y: target labels
    n_hidden: number of hidden nodes to keep
    sparsity_ratio: fraction of nodes to retain
    """
    # Step 1: Train over-parameterized network
    wide_net = train_wide_network(X, y, width=hidden_layer_width)
    
    # Step 2: Compute ridgelet transform of output weights
    # c(a,b) ≈ <output_gradient, σ(a·x + b)>
    ridgelet_coeffs = compute_ridgelet_transform(wide_net, X, y)
    
    # Step 3: Build probability distribution from ridgelet magnitudes
    probabilities = np.abs(ridgelet_coeffs) ** 2
    probabilities /= probabilities.sum()
    
    # Step 4: Sample n_hidden nodes according to optimized distribution
    selected_indices = np.random.choice(
        hidden_layer_width, size=n_hidden, 
        p=probabilities, replace=False
    )
    
    # Step 5: Extract and fine-tune subnetwork
    subnetwork = extract_subnetwork(wide_net, selected_indices)
    subnetwork = fine_tune(subnetwork, X, y)
    
    return subnetwork
```

### Why This Beats Naive Sampling

| Method | Runtime | Quality |
|--------|---------|---------|
| Uniform random | O(1) per sample | Poor (high empirical risk) |
| Optimal (exhaustive) | exp(O(D)) | Best |
| Quantum | O(D) | Best |
| **This (quantum-inspired)** | **O(poly(D))** | **≈ Quantum** |

## Ridgelet Transform Computation

The key computational insight: the ridgelet transform can be approximated efficiently:

```python
def compute_ridgelet_transform(network, X, y, n_samples=10000):
    """Approximate ridgelet transform via Monte Carlo."""
    # For each candidate (a, b) direction:
    # c(a,b) = (1/N) Σᵢ [∂L/∂f(xᵢ)] · σ(a·xᵢ + b)
    
    gradients = compute_output_gradients(network, X, y)
    
    # Sample candidate directions
    a_candidates = np.random.randn(n_samples, X.shape[1])
    b_candidates = np.random.randn(n_samples)
    
    # Compute transform values
    ridgelet_coeffs = np.zeros(n_samples)
    for i in range(n_samples):
        activation = np.maximum(0, X @ a_candidates[i] + b_candidates[i])
        ridgelet_coeffs[i] = np.mean(gradients * activation)
    
    return ridgelet_coeffs
```

## Practical Guidelines

### When to Use

- **Network compression**: Reduce model size while maintaining accuracy
- **Edge deployment**: Find subnetworks that fit on-device
- **Training acceleration**: Train wide network once, extract many subnetworks
- **Architecture search**: Automated neural architecture selection

### Parameter Selection

| Parameter | Rule of Thumb |
|-----------|---------------|
| Over-parameterization | 10-100x target width |
| Ridgelet samples | 1000-10000 |
| Sparsity ratio | 1-10% for best results |
| Fine-tuning epochs | 10-50% of original training |

## Key Insights

1. **Ridgelet transform ≈ importance weights**: Larger |c(a,b)| means that direction carries more information about the target function
2. **Quantum advantage is illusory here**: The classical polynomial algorithm removes the purported quantum speedup
3. **Dequantization success**: Many "quantum ML advantages" can be matched classically with the right mathematical tools

## Applications to Finance

The lottery ticket approach transfers directly to financial modeling:

- **Factor model compression**: Find minimal set of predictive factors
- **Time series forecasting**: Sparse subnetworks for market prediction
- **Risk modeling**: Compress large risk networks for faster computation

## Related Papers

- arXiv:2605.13979 — Winning Lottery Tickets in Neural Networks via a Quantum-Inspired Classical Algorithm (Isogai et al., 2026)
