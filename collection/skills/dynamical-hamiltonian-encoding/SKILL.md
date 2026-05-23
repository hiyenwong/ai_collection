---
name: dynamical-hamiltonian-encoding
description: "Dynamical Hamiltonian Encoding (DHE) methodology for quantum machine learning and quantum finance data encoding. Addresses the Inverse Born Rule Fallacy — the limitation of standard amplitude encoding (psi = sqrt(P)) that renders quantum states 'phase-deaf' by restricting to the positive real orthant. DHE uses data to generate non-commutative Hamiltonian evolution (based on QIFT) rather than static phase-locked vectors. Use when: designing quantum data encoding for ML/finance, implementing amplitude encoding alternatives, avoiding phase-deaf representations, or building genuinely quantum-classifiable feature maps."
---

# Dynamical Hamiltonian Encoding

## Core Problem: The Inverse Born Rule Fallacy

Standard amplitude encoding in QML/Quantum Finance uses psi = sqrt(P), mapping classical probability P to quantum amplitudes. This approach has critical limitations:

1. **Restricts to positive real orthant** S+ — an abelianized subspace
2. **Makes representation 'phase-deaf'** — cannot access non-commutative structure
3. **Fails to enable genuine quantum advantage** in classification tasks
4. **Basis changes (Hadamard) on these states** cannot replicate active phase-kickback

The mapping P -> sqrt(P) -> |psi> is not invertible to recover the full non-commutative structure needed for quantum advantage.

## DHE Solution

Instead of encoding data as a static quantum state vector, use data to **generate non-commutative Hamiltonian evolution**:

```
H(data) = sum_i data_i * H_i
|psi> = exp(-i * H(data) * t) |psi_0>
```

Where H_i are non-commuting generators (Pauli strings, interaction terms).

## Implementation Pattern

### Step 1: Choose Non-Commuting Generators
```python
# Example: Pauli string generators
H_generators = [
    ('X0 Y1', weight_0),   # Non-commuting pair
    ('Z0 X2', weight_1),   # Additional generator
    ('Y1 Z3', weight_2),   # Creates entanglement
]
```

### Step 2: Build Hamiltonian from Data
```python
def build_hamiltonian(data_vector, generators):
    """Encode data as coefficients of non-commuting Hamiltonian terms."""
    H = sum(d * gen for d, gen in zip(data_vector, generators))
    return H
```

### Step 3: Evolve State via Hamiltonian
```python
# Instead of |psi> = sqrt(P)|i>, use dynamical evolution
def dynamical_encode(data, initial_state, generators, t=1.0):
    H = build_hamiltonian(data, generators)
    evolved_state = expm(-1j * H * t) @ initial_state
    return evolved_state
```

### Step 4: Verify Non-Commutative Structure
```python
# Check that encoded states access full Hilbert space
def verify_encoding(states):
    """Verify states span non-abelian subspace."""
    commutators = []
    for s1, s2 in zip(states, states[1:]):
        comm = s1 @ s2 - s2 @ s1
        commutators.append(norm(comm))
    return any(c > threshold for c in commutators)
```

## Comparison: Amplitude Encoding vs DHE

| Property | Amplitude Encoding | DHE |
|----------|-------------------|-----|
| State space | S+ (positive orthant) | Full Hilbert space |
| Commutativity | Abelian | Non-commutative |
| Phase information | Lost | Preserved |
| Quantum advantage | Limited | Genuine potential |
| Circuit depth | O(log N) | O(poly(N)) |

## When to Use

- Quantum ML classification tasks where amplitude encoding underperforms
- Quantum finance feature engineering requiring rich state representations
- Any scenario where the data manifold needs non-commutative structure
- When basis-state encoding fails to capture feature interactions

## Pitfalls

### QIFT Implementation Complexity
QIFT (Quantum Imaginary Time Evolution) based encoding requires Trotterization or variational approximation. Use library implementations where available.

### Generator Selection
The choice of non-commuting generators determines expressivity. Insufficient generators -> back to abelianized case. Too many -> circuit depth explosion.

### Data Scaling
Data values must be scaled to appropriate Hamiltonian coefficients to avoid numerical overflow or underflow in evolution.

## Related Skills
- quantum-ml-data-loading: General quantum data loading optimization
- spiking-quantum-encoding: SPATE encoding for quantum ML
- quantum-finance-stack: Financial computation framework

## References
- arXiv: 2602.21350 - "The Inverse Born Rule Fallacy" (Zajac et al., 2026)
- QIFT (Quantum Imaginary Time Evolution) methodology
