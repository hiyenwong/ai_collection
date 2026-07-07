---
name: muon-ogd-spectral-orthogonal-gradient-projection
description: "Muon-OGD: Spectral-norm-aware orthogonal gradient projection for LLM continual learning. Integrates Muon optimizer's spectral-norm geometry with OGD's non-interference constraints. Activation triggers: Muon-OGD, spectral norm continual learning, orthogonal gradient projection LLM, Muon optimizer CL, Frobenius vs spectral norm CL"
---

# Muon-OGD: Muon-based Spectral Orthogonal Gradient Projection for LLM Continual Learning

> A spectral-norm-aware continual learning framework that integrates Muon-style operator-norm geometry with orthogonal projection constraints, providing a practical and effective alternative to Frobenius-norm projection for sequential LLM adaptation.

## Metadata
- **Source**: arXiv:2605.08949
- **Authors**: Binghang Lu, Zheyuan Deng, Bing Hu, Runyu Zhang, Changhong Mou, Yunhan Zhao, Guang Lin, Yuan Tian, Xiaomin Li
- **Published**: 2026-05-09
- **Institutions**: Purdue, Brown, MIT, UC Irvine, Harvard, Utah State

## Core Problem

**Catastrophic Forgetting in LLM Continual Learning**: When fine-tuning LLMs on sequential tasks, performance on previously learned tasks degrades rapidly.

**Projection-Based CL Limitation**: Existing methods (OGD, O-LoRA, Sculpting Subspaces) restrict updates to subspaces orthogonal to past-task directions, but they operate under **Frobenius-norm geometry** (Euclidean parameter geometry). The Muon optimizer's empirical success suggests that **spectral-norm geometry** may be more appropriate for matrix-valued LLM parameters.

## Key Innovation

**Muon-OGD** bridges two paradigms:
1. **Projection-based CL** (Frobenius norm): minimize gradient update while avoiding protected directions
2. **Muon optimizer** (Spectral norm): steepest descent under spectral-norm geometry

The result: a **spectral-norm-constrained optimization** problem with linear non-interference constraints.

## Mathematical Framework

### Traditional OGD (Frobenius Norm Geometry)
```
min_Δ ⟨G, Δ⟩ + λ||Δ||²_F
s.t. ⟨Δ, C_i⟩ = 0  for all protected directions C_i
```

### Muon Update (Spectral Norm Geometry)
```
min_Δ ⟨G, Δ⟩
s.t. ||Δ||₂ ≤ η

Solution: Δ = -η · msgn(G)  (matrix sign function)
```

### Muon-OGD (Combined)
```
min_Δ ⟨G, Δ⟩
s.t. ⟨Δ, C_i⟩ = 0  AND  ||Δ||₂ ≤ η
```

### Efficient Solution via Dual Iterations
1. **Form corrected matrix**: H^(m) = G + Σ λ_i C_i
2. **Muon-like update**: Δ = -msgn(H)
3. **Dual variable update**: λ_i^(m) = λ_i^(m-1) - η_λ ⟨C_i, msgn(H^(m))⟩
4. **Parameter update**: θ ← θ + ηΔ

This uses **Newton-Schulz matrix-sign approximations** for efficient computation.

## Why Spectral Norm Matters

1. **Matrix-valued parameters**: LLM weight matrices are naturally 2D objects; Frobenius norm treats them as flattened vectors, losing structural information.
2. **Spectral norm captures largest singular direction**: More relevant for understanding how updates affect model behavior.
3. **Muon's empirical success**: The Muon optimizer, which applies orthogonalized matrix updates with spectral-norm interpretation, has shown strong results in LLM training.
4. **Better stability-plasticity tradeoff**: Spectral-norm constraints may provide more natural regularization for matrix updates.

## Implementation Guide

### Prerequisites
- LLM with matrix-valued parameters
- Protected subspace extraction from past tasks
- Matrix sign function implementation (Newton-Schulz iteration)

### Step-by-Step
1. **Extract protected subspace**: Compute directions associated with past tasks (e.g., gradient covariance, NTK eigenvectors)
2. **Compute gradient/momentum**: Standard forward-backward pass
3. **Dual iteration**: Iteratively solve for Lagrange multipliers
4. **Matrix sign update**: Apply Newton-Schulz iteration for msgn(H)
5. **Parameter update**: Apply constrained spectral-norm update

### Code Sketch
```python
def newton_schulz_sign(A, iters=5):
    """Compute matrix sign function via Newton-Schulz iteration."""
    X = A / torch.norm(A)  # Normalize
    for _ in range(iters):
        X = 0.5 * (3 * X - X @ X.T @ X)
    return X

def muon_ogd_update(G, protected_dirs, eta=0.01, dual_lr=0.1, dual_iters=10):
    """Muon-OGD update with spectral norm constraint."""
    lambdas = torch.zeros(len(protected_dirs))
    
    for _ in range(dual_iters):
        H = G + sum(l * C for l, C in zip(lambdas, protected_dirs))
        msgn_H = newton_schulz_sign(H)
        
        # Dual ascent
        for i, C in enumerate(protected_dirs):
            lambdas[i] -= dual_lr * torch.sum(C * msgn_H)
    
    # Final update
    H = G + sum(l * C for l, C in zip(lambdas, protected_dirs))
    delta = -eta * newton_schulz_sign(H)
    return delta
```

## Evaluation Results

- **Benchmarks**: TRACE (standard CL benchmark), Coding-Math-Medical domain curricula
- **Architectures**: Both encoder-decoder and decoder-only
- **Results**: Consistently improves over sequential fine-tuning and competitive OGD baselines
- **Scalability**: Computationally scalable for LLM-scale models

## Applications
- Continual fine-tuning of LLMs across domains
- Sequential task adaptation without replay buffers
- Multi-domain LLM deployment with incremental learning
- Any matrix-valued parameter continual learning scenario

## Pitfalls
- **Protected subspace quality**: OGD methods depend on accurate extraction of protected directions
- **Matrix sign convergence**: Newton-Schulz iteration may need careful normalization
- **Dual iteration cost**: Additional inner loop overhead compared to standard OGD
- **Memory overhead**: Storing protected directions grows with number of past tasks
- **Spectral norm estimation**: May require SVD or approximations for very large matrices

## Related Skills
- plasticity-prediction-deep-continual-learning
- zeroth-order-adaptation-forgetting-theory
- rft-visual-continual-learning
- continual-learning-methods
