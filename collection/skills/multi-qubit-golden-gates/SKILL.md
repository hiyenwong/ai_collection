---
name: multi-qubit-golden-gates
description: Construction of optimal topological generators for compact unitary Lie groups, extending golden and super-golden gates to multi-qubit systems. Uses Sarnak-Xue Density Hypothesis variants for definite projective unitary groups to create efficient universal gate sets. Use when designing multi-qubit quantum gate sets, compiling quantum circuits, or studying optimal quantum gate synthesis.
---

# Multi-Qubit Golden Gates

## Description

Constructs optimal universal multi-qubit gate sets using algebraic number theory and representation theory. Extends the golden gate construction to arbitrary dimensions, providing efficient topological generators for SU(2^n) with provable spectral gap properties.

## Activation Keywords

- golden gates
- multi-qubit gate synthesis
- topological generators
- Sarnak-Xue hypothesis
- quantum gate compilation
- unitary Lie group generators
- 最优量子门
- 黄金门
- golden gate construction
- universal gate set design

## Tools Used

- exec: Run spectral gap computations
- read: Access group theory references
- write: Generate gate sequences

## Core Methodology

### Gate Construction via Number Theory

1. **Identify Group**: Target SU(d) for d=2^n qubits
2. **Choose Ring**: Select appropriate number ring (Gaussian, Eisenstein)
3. **Generate Elements**: Use algebraic units to produce group elements
4. **Verify Gap**: Check spectral gap using Sarnak-Xue bounds

### Golden Gate Properties

- **Dense**: Elements generate a dense subgroup of SU(d)
- **Efficient**: Word length O(log(1/ε)) for ε-approximation
- **Constructive**: Explicit generators from number theory
- **Spectral Gap**: Uniform gap independent of dimension

### Sarnak-Xue Density Hypothesis Application

For projective unitary groups PU(d):
- Matrix coefficients decay as p^(-1/2+ε)
- Spectral gap λ₁ ≥ 1 - O(p^(-1/2))
- Approximation quality: ε ≈ exp(-c·word_length)

## Implementation Patterns

### Gate Set Construction

```python
def construct_golden_gates(n_qubits: int, precision: float):
    """Construct golden gate set for n qubits
    
    Returns generators with spectral gap properties
    """
    d = 2**n_qubits  # Hilbert space dimension
    
    # Choose number ring based on dimension
    ring = select_number_ring(d)
    
    # Generate algebraic units
    generators = algebraic_units(ring, d)
    
    # Verify spectral gap
    gap = compute_spectral_gap(generators)
    
    return generators, gap
```

### Circuit Compilation

```python
def compile_unitary(U: np.ndarray, gates: list, epsilon: float):
    """Compile unitary using golden gates
    
    Uses Solovay-Kitaev with golden gate generators
    """
    # Recursive decomposition
    if distance(U, I) < epsilon:
        return []
    
    # Find closest gate
    g, residual = find_closest_gate(U, gates)
    
    # Recursive compilation
    return [g] + compile_unitary(residual, gates, epsilon/2)
```

## Performance Metrics

| Metric | Classical Gates | Golden Gates |
|--------|----------------|--------------|
| Gate count for ε | O(log^c(1/ε)) | O(log(1/ε)) |
| Compilation time | Polynomial | Near-optimal |
| Spectral gap | Variable | Uniform |
| Construction | Numerical | Algebraic |

## Error Handling

### Insufficient Spectral Gap

If gap < threshold:
- Verify number ring selection
- Check algebraic unit properties
- Consider alternative prime ideals

### Compilation Failure

If target unitary not reachable:
- Verify unitarity of input
- Check dimension compatibility
- Increase precision tolerance

## References

- arXiv:2509.09047 - Multi-Qubit Golden Gates
- Sarnak-Xue Density Hypothesis
- Solovay-Kitaev theorem
