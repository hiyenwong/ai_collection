---
name: effective-rank-qnn-expressivity
description: "Methodology for measuring and maximizing Quantum Neural Network (QNN) expressivity using effective rank (kappa). Introduces a quantitative measure capturing the number of effectively independent variational parameters in parameterized quantum circuits. Use when: designing QNN architectures, analyzing barren plateaus, optimizing variational quantum circuits, measuring quantum model capacity, or studying expressivity-entanglement relationships. Triggered by: QNN expressivity, effective rank quantum, variational circuit design, barren plateau expressivity, quantum neural architecture, parameterized quantum circuit capacity."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2506.15375"
  published: "2025-06-15"
  tags: [quantum, machine-learning, expressivity, effective-rank, qnn, variational]
---

# Effective Rank for QNN Expressivity

Methodology from arXiv:2506.15375 - using **effective rank (kappa)** to quantify and maximize Quantum Neural Network expressivity.

## Core Concept

The effective rank `kappa` captures the number of effectively independent parameters among all variational parameters in a parameterized quantum circuit (PQC). Unlike raw parameter count, kappa measures the true degrees of freedom available for learning.

### Mathematical Foundation

```
kappa = exp(H(p) / log(d))
```

Where `H(p)` is the Shannon entropy of the normalized singular value distribution of the quantum Fisher information matrix, and `d` is its dimension.

- `kappa ~ 1`: circuit is effectively a single parameter (severely limited expressivity)
- `kappa ~ d`: all parameters are independent (maximal expressivity)

## Key Findings

1. **Expressivity-Entanglement Trade-off**: Higher entanglement in the ansatz does NOT always yield higher expressivity
2. **Circuit Depth Saturation**: Beyond a critical depth, adding layers does NOT increase kappa significantly
3. **Barren Plateau Correlation**: Low kappa correlates strongly with barren plateau severity
4. **Architecture Selection**: kappa serves as a pre-training diagnostic for ansatz quality

## Workflow

### Step 1: Compute Quantum Fisher Information Matrix

For a parameterized quantum circuit U(theta), estimate QFI from parameter shifts using the 4-point rule.

### Step 2: Compute Effective Rank

1. Compute SVD of QFI matrix
2. Normalize singular values: p = s / sum(s)
3. Filter near-zero values (threshold 1e-10)
4. Compute Shannon entropy: H = -sum(p * log(p))
5. Effective rank: kappa = exp(H / log(d))

### Step 3: Optimize Circuit Architecture

Use kappa as pre-training diagnostic for ansatz selection. Test different depths and topologies (linear, ring, all-to-all) and select minimal circuit achieving target kappa/d ratio >= 0.8.

## Pitfalls

- **Sampling noise**: QFI estimation from finite shots adds variance. Use shots >= 1000 for reliable kappa
- **Numerical stability**: Near-zero singular values cause log issues. Filter with threshold 1e-10
- **Dimension scaling**: kappa is normalized by log(d), making it comparable across different circuit sizes
- **Not a loss function**: kappa is a diagnostic metric, not directly differentiable for gradient-based optimization

## Activation Keywords

effective rank, QNN expressivity, quantum neural network capacity, variational circuit design, barren plateau expressivity, parameterized quantum circuit analysis, quantum Fisher information rank