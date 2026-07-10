---
name: iterative-ising-qec-decoder
description: Iterative Low-Order Decoding (ILOD) methodology for quantum error correction — mapping QEC decoding onto ground-state optimization of classical Ising Hamiltonians with Bayesian prior-based cross-term approximation. Use when: implementing QEC decoders, optimizing quantum circuit error correction, reducing Ising model interaction order, or applying statistical mechanics approaches to quantum error correction. Activates on keywords: iterative Ising decoder, ILOD, quantum error correction decoding, Ising model QEC, Bayesian prior decoding, toric code decoder, color code decoder.
---

# Iterative Ising Quantum Error Correction Decoder

## ILOD Methodology (arXiv:2606.12301)

The **Iterative Low-Order Decoding (ILOD)** algorithm maps quantum error correction (QEC) decoding onto classical Ising Hamiltonian ground-state optimization, with a key innovation: alternating X/Z sub-Hamiltonian optimization with Bayesian prior-based cross-term approximation.

## Core Problem

Under phenomenological depolarizing noise, the exact joint Ising formulation of QEC decoding contains **high-order interaction terms**:
- **Toric code**: up to 8-body interactions
- **6.6.6 color code**: up to 10-body interactions

These high-order terms cause:
1. Solver convergence degradation
2. Inflated runtime
3. Excessive auxiliary spin overhead for 2-body hardware embedding

## ILOD Algorithm

```
Given: syndrome measurement s, code distance d
Initialize: X-config = identity, Z-config = identity

Repeat until convergence (or max iterations):
  1. Optimize X-sub-Hamiltonian:
     - Use Bayesian priors from current Z-config
     - Reweight X couplings based on inferred Z errors
     - Solve for optimal X error configuration

  2. Optimize Z-sub-Hamiltonian:
     - Use Bayesian priors from updated X-config
     - Reweight Z couplings based on inferred X errors
     - Solve for optimal Z error configuration

  3. Check convergence:
     - If both configs stable → return correction
     - If max iterations reached → return best found
```

## Key Results

| Code | ILOD Threshold | Joint Threshold | Speedup |
|------|---------------|-----------------|---------|
| Toric | 4.73% | 4.83% | O(√n) empirical |
| 6.6.6 Color | ≈ joint (small d) | Converges at large d | 2.5x fewer spins |

ILOD halves the maximum body count of interaction terms, reducing 2-body embedding spin count by **2.5x**.

## Implementation Patterns

### Ising Hamiltonian Construction
```python
# X-sub-Hamiltonian with Bayesian priors from Z errors
H_X = -sum(J_X_ij * x_i * x_j) - sum(h_X_i * x_i)
# J_X_ij reweighted by P(X_error | Z_inferred)

# Z-sub-Hamiltonian with Bayesian priors from X errors  
H_Z = -sum(J_Z_ij * z_i * z_j) - sum(h_Z_i * z_i)
# J_Z_ij reweighted by P(Z_error | X_inferred)
```

### Bayesian Prior Reweighting
```python
def reweight_couplings(couplings, inferred_errors, noise_model):
    """Reweight Ising couplings using Bayesian priors from other type's inference."""
    for i, j in couplings:
        prior = compute_joint_probability(
            inferred_errors[i], inferred_errors[j], noise_model
        )
        couplings[i, j] *= prior
    return couplings
```

### Cross-Domain Application
This methodology bridges:
- **Quantum error correction** → syndrome decoding
- **Statistical mechanics** → Ising model ground state
- **Bayesian inference** → cross-correlation approximation
- **Combinatorial optimization** → hardware-embeddable 2-body Ising

## When to Use

- QEC decoder implementation for surface/toric/color codes
- Reducing Ising model complexity for quantum annealing hardware
- Statistical mechanics approaches to quantum information processing
- Bayesian approximation methods in quantum decoding
- Hardware-aware QEC with limited interaction orders

## Pitfalls

- **Threshold trade-off**: ILOD sacrifices ~0.1% threshold for significant speedup
- **Convergence**: Joint formulation may fail to converge at large distances; ILOD handles this gracefully
- **Iteration count**: More iterations needed for higher error rates near threshold
- **Noise model dependency**: Bayesian priors depend on accurate noise characterization

## References

- arXiv:2606.12301 — "An iterative Ising decoder for quantum error correction codes" (Liu et al., June 2026)
- Related: Coset Ensemble Decoder (arXiv:2606.11291), Sparse Mamba Decoder for QEC
