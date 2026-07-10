---
name: dynamical-isometry-plasticity
description: Continual learning framework preserving plasticity via dynamical isometry - Neural Tangent Kernel analysis showing layer-wise Jacobian singular values near 1 prevents plasticity loss, with isometry-promoting regularization and dormant ReLU reactivation mechanisms.
tags: [continual-learning, plasticity, dynamical-isometry, neural-tangent-kernel, optimization, deep-learning]
version: 1.0
arxiv: 2606.09762v1
date: 2026-06-08
---

# Preserving Plasticity in Continual Learning via Dynamical Isometry

## Overview

Theoretical framework relating plasticity to empirical Neural Tangent Kernel (NTK), identifying dynamical isometry (layer-wise Jacobian singular values near 1) as key mechanism for preserving plasticity in continual learning under non-stationarity.

**arXiv**: [2606.09762v1](https://arxiv.org/abs/2606.09762v1)  
**Published**: 2026-06-08  
**Keywords**: Continual Learning, Plasticity, Dynamical Isometry, Neural Tangent Kernel, Optimization, Non-stationarity

---

## Core Problem: Plasticity Loss

### Phenomenon

Continual training under non-stationarity leads to:

```
Task 1 → High performance ✓
Task 2 → Moderate performance ✓
Task 3 → Low performance ✓
Task N → Nearly zero learning ✗

Plasticity progressively declines → network becomes "rigid"
```

### Symptoms

- **Dormant Units**: ReLU activations stuck at 0
- **Gradient Vanishing**: Layer-wise gradients shrink
- **Feature Collapse**: Representations become fixed
- **NTK Degradation**: Kernel spectrum collapses

---

## Neural Tangent Kernel (NTK) Perspective

### NTK Definition

For network `f_θ(x)`:

```
K_θ(x, x') = ⟨∇_θ f_θ(x), ∇_θ f_θ(x')⟩
```

**Interpretation**: Measures similarity of function changes w.r.t. parameter changes.

### NTK Evolution in Continual Learning

**Observation**: NTK spectrum changes during training:

```
Initial:  Broad spectrum, many eigenvalues
After Task 1: Spectrum begins narrowing
After Task N: Spectrum collapsed → low plasticity
```

**Key Insight**: Plasticity ∝ NTK eigenvalue diversity

---

## Dynamical Isometry

### Definition

**Dynamical Isometry**: Layer-wise Jacobian singular values remain near 1 throughout training.

```
J_l ≈ I (identity) for each layer l

⟨‖J_l‖_F⟩ ≈ d_l (dimension of layer l)
```

### Connection to Plasticity

**Mechanism**:
1. **Signal Propagation**: Gradients propagate without vanishing/exploding
2. **Uniform Learning**: All parameters contribute equally
3. **No Dormancy**: ReLU units remain active

**Mathematical Link**:

```
Plasticity ∝ NTK quality ∝ Dynamical Isometry

NTK = sum over layers of (J_l)^T J_l

If J_l singular values ≈ 1 → NTK has healthy spectrum
```

---

## Isometric Architectures

### Almost-Everywhere Isometric Networks

**Property**: Networks that are:
- Almost everywhere isometric (AEI)
- Universal Lipschitz function approximators
- Maintain dynamical isometry during training

**Examples**:

| Architecture | Isometry Property | Expressiveness |
|--------------|-------------------|----------------|
| ReLU MLP | ❌ (singular values diverge) | ✓ |
| Orthogonal MLP | ✓ (forced orthogonality) | Limited |
| **AEI Networks** | ✓ (by construction) | ✓ (universal) |

### AEI Construction

```python
class AEILayer(nn.Module):
    """
    Almost-everywhere isometric layer.
    
    Key: Parameterize weight with orthogonal structure
    but allow expressiveness through nonlinearity.
    """
    def __init__(self, in_dim, out_dim):
        # Orthogonal initialization
        self.weight = nn.Parameter(torch.randn(out_dim, in_dim))
        self._ensure_orthogonal()
        
    def forward(self, x):
        # Apply weight with normalization
        W = self.weight / torch.norm(self.weight, dim=1, keepdim=True)
        return F.relu(W @ x)
    
    def _ensure_orthogonal(self):
        # Project to orthogonal manifold periodically
        U, _, V = torch.svd(self.weight.data)
        self.weight.data = U @ V.T
```

**Result**: Near-dynamical isometry compatible with nonlinear representations.

---

## Isometry-Promoting Regularization

### For General Architectures

**Regularizer**: Encourage singular values toward 1

```python
def isometry_regularizer(model, x_batch):
    """
    Penalize deviation from dynamical isometry.
    
    Args:
        model: Neural network
        x_batch: Input samples
    
    Returns:
        Loss: Isometry deviation penalty
    """
    total_penalty = 0
    
    for layer in model.layers:
        # Compute Jacobian
        J = compute_jacobian(layer, x_batch)
        
        # Singular values
        singular_vals = torch.svd(J).S
        
        # Penalty: deviation from 1
        penalty = torch.mean((singular_vals - 1)**2)
        
        total_penalty += penalty
    
    return total_penalty
```

### Training Procedure

```python
# Standard continual learning
for task in task_sequence:
    for batch in task_data:
        # Standard loss
        loss_task = task_loss(model, batch)
        
        # Isometry penalty
        loss_iso = isometry_regularizer(model, batch)
        
        # Combined
        loss = loss_task + λ * loss_iso
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
```

---

## Dormant ReLU Reactivation

### Novel Mechanism Discovery

**Observation**: Isometry regularization reactivates dormant ReLU units.

**Mechanism**:

```
Dormant ReLU: output = max(0, Wx + b) ≈ 0 always

Isometry regularization → adjusts W

→ Wx + b becomes positive for some inputs

→ Unit reactivates → plasticity restored
```

### Mathematical Explanation

**Key**: Isometry penalty changes weight singular values → modifies activation statistics.

```python
# Dormancy detection
def detect_dormant_units(layer, x_batch):
    """
    Find units with zero activation rate.
    """
    activations = layer.forward(x_batch)
    zero_rate = (activations == 0).float().mean(dim=0)
    
    dormant_mask = zero_rate > threshold  # e.g., 0.95
    return dormant_mask

# Dormancy cure
 dormant_units = detect_dormant_units(layer, x_batch)

if dormant_units.any():
    # Apply isometry regularization
    # → weights adjust → units reactivate
```

---

## Experimental Results

### Plasticity Metrics

| Metric | Standard Training | + Isometry Regularizer |
|--------|-------------------|------------------------|
| Dormant Unit Rate | ↑↑ (up to 80%) | ↓ (≤ 10%) |
| NTK Spectrum Width | ↓↓ (collapsed) | ✓ (maintained) |
| Gradient Norm | ↓ (vanishes) | ✓ (stable) |
| Performance on Task N | ✗ (near zero) | ✓ (near optimal) |

### Benchmark Results

**Continual Learning Benchmarks**:
- **Split MNIST**: +15% final task accuracy
- **Permuted MNIST**: +20% retention
- **Sequential CIFAR-100**: +12% plasticity

**Key Finding**: Isometry regularization outperforms replay/meta-learning methods for preserving plasticity.

---

## Comparison with Existing Methods

| Method | Addresses Plasticity | Mechanism | Computational Cost |
|--------|---------------------|-----------|-------------------|
| Replay | ✓ | Store past data | Memory heavy |
| EWC/Meta-learning | Moderate | Constraint optimization | Moderate |
| Architecture redesign | Moderate | New structure | Design overhead |
| **Isometry regularization** | ✓ (strong) | Jacobian control | Low |

---

## Practical Implementation

### Step-by-Step Guide

**1. Monitor Plasticity**

```python
def monitor_plasticity(model, validation_data):
    # Compute NTK spectrum
    K = compute_ntk(model, validation_data)
    spectrum = torch.linalg.eigvalsh(K)
    
    # Plasticity index
    plasticity = spectrum.std() / spectrum.mean()
    
    return plasticity

# Check periodically
if plasticity < threshold:
    increase_isometry_penalty()
```

**2. Apply Regularization**

```python
# During training
λ_iso = 0.01  # Start small

# Adjust λ based on plasticity monitoring
if plasticity declining:
    λ_iso *= 2  # Increase penalty
```

**3. Verify Reactivation**

```python
# Track dormant units
dormant_history = []

for epoch in range(epochs):
    dormant_rate = count_dormant_units(model)
    dormant_history.append(dormant_rate)
    
    # Should decrease with isometry regularization
```

---

## Key Insights

1. **NTK Link**: Plasticity directly relates to NTK spectrum quality
2. **Isometry Key**: Dynamical isometry prevents NTK collapse → preserves plasticity
3. **AEI Networks**: Architecture-level solution (near-isometry + expressiveness)
4. **Regularizer**: Lightweight alternative for general architectures
5. **Reactivation**: Novel mechanism curing dormant ReLU units

---

## Applications

### 1. Long-Term Deployed Models

Agents learning over months/years without plasticity loss.

### 2. Lifelong Learning Robots

Robotics systems adapting to new environments continuously.

### 3. Medical AI

Diagnostic models updating as new diseases/variants emerge.

### 4. Streaming Data Systems

Models processing non-stationary data streams (finance, climate).

---

## Limitations & Future Work

### Current Limitations

- Computational cost of Jacobian computation (large models)
- AEI networks less studied than standard architectures
- Hyperparameter sensitivity (λ_iso tuning)

### Future Directions

- Efficient Jacobian approximation
- Architectural search for AEI properties
- Combination with other continual learning methods
- Application to large-scale pretrained models

---

## Activation

Use when:
- Training models on sequential tasks
- Observing plasticity decline in continual learning
- Designing lifelong learning systems
- Analyzing NTK evolution during training
- Debugging dormant unit problems

**Trigger words**: plasticity, continual learning, dynamical isometry, Neural Tangent Kernel, NTK, dormant units, non-stationarity, lifelong learning, gradient vanishing, feature collapse

---

## References

- Original paper: arXiv:2606.09762v1
- NTK theory: Jacot et al., 2018 (Neural Tangent Kernel)
- Isometry: Saxe et al., 2014 (Exact solutions to nonlinear dynamics)
- Continual learning: Parisi et al., 2019 (Continual learning survey)