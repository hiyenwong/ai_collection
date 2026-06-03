---
name: quantum-error-cancellation
description: >
  Analyze and design quantum error mitigation and cancellation strategies for NISQ-era
  quantum computing. Covers probabilistic error cancellation (PEC), zero-noise extrapolation
  (ZNE), quantum error detection codes (QEDC), and hybrid QED+PEC schemes. Includes
  Zeno-enhanced error cancellation, sparse Pauli-Lindblad noise modeling, and sampling
  overhead optimization. Use when: designing error mitigation protocols for quantum circuits,
  analyzing PEC/ZNE trade-offs, implementing quantum error detection with post-selection,
  optimizing sampling overhead for NISQ circuits, or evaluating discrete-Zeno error suppression.
  Trigger keywords: quantum error mitigation, probabilistic error cancellation, PEC,
  zero-noise extrapolation, ZNE, quantum error detection, QEDC, Zeno effect, noise model,
  Pauli-Lindblad, sampling overhead, NISQ error mitigation, 量子误差消除.
---

# Quantum Error Cancellation

## Overview

Quantum error mitigation techniques for NISQ devices that reduce noise effects
without full fault tolerance. Focus on PEC, ZNE, QEDC, and their combinations.

## Error Mitigation Taxonomy

### Probabilistic Error Cancellation (PEC)

Core principle: Express noise channel as quasi-probability distribution over
invertible operations, then sample and reweight.

```
Noise channel: Λ(ρ) = Σ q_i O_i(ρ)
Inverse: Λ^{-1}(ρ) = Σ α_i O_i(ρ), where α_i can be negative
Sampling overhead: γ = Σ|α_i| (γ-noise)
```

Key limitation: Overhead scales as γ^C where C is circuit volume.

### Zero-Noise Extrapolation (ZNE)

1. **Amplify** noise by factor λ (unitary folding, gate repetition)
2. **Measure** observable at each noise level
3. **Extrapolate** to λ → 0 (Richardson, exponential fitting)

Trade-off: Requires multiple circuit executions at different noise levels.

### Quantum Error Detection (QED)

- Stabilizer measurements detect (but don't correct) errors
- Post-selection discards runs with detected errors
- Leaves undetectable logical residue

## Hybrid QED+PEC Scheme (Zeno-Enhanced)

Key insight from Yuan et al. (arXiv:2605.12149):

1. **QED first**: Post-selection maps physical noise → weaker logical channel
2. **PEC second**: Apply PEC only to residual logical noise
3. **Result**: 3-4 orders of magnitude lower sampling overhead vs. bare PEC

### Algorithm

```
For each logical block:
  1. Prepare state |+L⟩
  2. Apply circuit with interleaved stabilizer measurements
  3. Post-select: keep only runs with +1 syndrome
  4. On accepted trajectories, apply degree-K PEC:
     - Retain fault branches up to order K
     - Preprocessing: O(m^K) instead of 2^m
     - Per-block error: O(W^{K+1})
```

### Discrete-Zeno Trade-off

Cheap error detection reshapes the effective channel PEC must invert,
rather than simply adding overhead. Optimal balance depends on:
- Physical error rate p
- Stabilizer measurement fidelity
- Circuit depth/width

## Noise Modeling

### Sparse Pauli-Lindblad Model

For local noise, express channel as:

```
Λ(ρ) = exp(Σ r_k P_k ·) ρ
```

where P_k are Pauli strings and r_k are rates.

After QED post-selection, the accepted channel has correlated noise
structure that requires perturbative inverse construction.

### Implementation Pattern

```python
import numpy as np

def sparse_pauli_lindblad_inverse(rates, max_order=1):
    """Construct inverse channel perturbatively up to max_order."""
    n_terms = len(rates)
    inverse_coeffs = {}
    
    # Degree-1: just negate rates
    for k, r in enumerate(rates):
        inverse_coeffs[k] = -r
    
    # Higher orders: perturbative corrections
    for order in range(2, max_order + 1):
        for combo in itertools.combinations(range(n_terms), order):
            coeff = (-1)**order * np.prod([rates[k] for k in combo])
            inverse_coeffs[combo] = coeff
    
    return inverse_coeffs
```

## Performance Analysis

### GHZ State Preparation Benchmark

| Scheme | Max Qubits | Fidelity | Sampling Overhead |
|--------|-----------|----------|-------------------|
| Bare PEC | ~50 | 0.95 | 10^4-10^5 |
| QED only | ~200 | ~0.90 | N/A (post-selection) |
| QED+PEC (K=1) | ~200 | 0.956 | 10^1-10^2 |

### Overhead Comparison

```
bare_PEC_overhead     = γ^C
qed_only_overhead     = 1 / P(accept)
qed_pec_overhead      = γ_residual^K / P(accept)
```

where γ_residual << γ_bare due to QED noise shaping.

## Error Handling

### Syndrome Noise

- **Readout-only flips**: Increase post-selection cost, preserve advantage
- **Noisy stabilizer extraction**: Can eliminate QED+PEC advantage entirely
- **GHZ-assisted global extraction**: Particularly vulnerable to syndrome noise

### Post-selection Collapse

When post-selection probability drops below threshold:
1. Reduce circuit depth
2. Switch to bare PEC
3. Consider active error correction instead

## Best Practices

1. **Characterize noise first**: Use Pauli-Lindblad tomography to get rates
2. **Start with K=1**: First-order QED+PEC provides most benefit
3. **Monitor syndrome quality**: Noisy measurements kill the advantage
4. **Scale carefully**: Advantage holds to n~200 physical qubits
5. **Avoid global stabilizers**: Local measurements are more robust

## Related Skills

- quantum-error-correction-methods: Full QEC patterns
- ml-quantum-error-correction: ML-based QEC decoding
- quantum-systems-engineering: Quantum system design
