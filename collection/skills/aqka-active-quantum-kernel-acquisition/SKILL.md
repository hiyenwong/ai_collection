---
name: aqka-active-quantum-kernel-acquisition
description: >
  Active Quantum Kernel Acquisition (AQKA) methodology for shot-budgeted quantum kernel learning.
  Optimally allocates measurement shots across kernel matrix entries using closed-form gradient-based
  acquisition theory. Use when: (1) designing quantum kernel estimation strategies under shot budget
  constraints, (2) implementing adaptive shot allocation for VQC/QKRR on NISQ hardware, (3) analyzing
  tradeoffs between Nyström-QKE, ShoFaR, and uniform allocation regimes, (4) building quantum kernel
  methods with provable regret bounds. arXiv: 2605.14672.
---

# AQKA: Active Quantum Kernel Acquisition

Optimal shot allocation for quantum kernel estimation under budget constraints. Source: arXiv:2605.14672.

## Core Method

### Closed-Form Shot Allocation

For Kernel Ridge Regression (KRR), optimal shots per entry:

```
s_ij* ∝ |g_ij| × sqrt(K_ij(1 - K_ij))
```

where `g_ij = |β_i α_j + β_j α_i|` (KRR dual variables).

For SVM, via envelope theorem:

```
s_ij* ∝ |η_i* η_j*| × sqrt(K_ij(1 - K_ij))
```

### Regime Selection

| Regime | Budget | Best Method | Why |
|--------|--------|-------------|-----|
| Budget-limited | B ≲ 16×n_pairs | **AQKA** | Gradient-aware allocation |
| Saturating | B large | **Nyström-QKE** | Low-rank reconstruction wins |
| Extreme low | B very small | **ShoFaR** | Minimal overhead |

### Sparsity-Aware Rate

Corrected Cauchy-Schwarz: `ρ ≤ 2m/N` (not `m²/N²`).
SVM ceiling: `ρ_SVM ≤ m_sv²/N²`.

## Implementation

```python
def compute_optimal_shots(K, alpha, beta, total_budget):
    """AQKA shot allocation for KRR."""
    N = K.shape[0]
    g = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            g[i,j] = abs(beta[i]*alpha[j] + beta[j]*alpha[i])
    
    variance = np.sqrt(K * (1 - K))
    score = g * variance
    total = score.sum()
    shots = (score / total) * total_budget
    return np.maximum(shots, 1).astype(int)
```

## Hardware Results

- `ibm_pittsburgh` (156-qubit Heron): +26-32 pts over uniform allocation
- `ibm_aachen` (N=20): +17.0 ± 4.8 pts, 3.5σ, 5 seeds
- Advantage scales with N (gap grows +8→+25 pts as N: 225→1000)

## Activation Keywords

- AQKA
- active quantum kernel acquisition
- shot budget allocation
- quantum kernel estimation
- adaptive shot allocation
- quantum kernel ridge regression

## Related Skills

- `qml-spiking-encoding`: SPATE encoding for QML
- `quantum-ml-data-loading`: QML data loading optimization
- `quantum-kernel-medical-embeddings`: Quantum kernel methods for medical AI

## Resources

- arXiv: [2605.14672](https://arxiv.org/abs/2605.14672)
- PDF: [Download](https://arxiv.org/pdf/2605.14672)
