# Quantum Hilbert Space Machine Learning - Session Notes (2026-05-22)

## Key Paper: arXiv:2605.17895 - Geometric Prototype Learning with MPS

### Core Architecture
- Class prototypes encoded as generative Matrix Product States (MPS)
- Data and prototypes in same Hilbert space → geometric comparison
- Decision function: P(c|x) = |⟨φ_c|ψ_x⟩|² (Born rule)

### Key Discoveries
1. **Attraction effect**: Quantum-probabilistic prototypes naturally attract toward correct data points (emerges from Hilbert space geometry)
2. **Dimensionality reduction**: Via prototype distances in Hilbert space
3. **Benchmarks**: Fashion-MNIST, ECG dataset — outperforms classical prototypes, competitive with black-box NNs

### Implementation Pattern
```
For input x:
  1. Encode x → |ψ_x⟩ (quantum state)
  2. Compute |⟨φ_c|ψ_x⟩|² for all classes c
  3. argmax_c → predicted class
```

### Why MPS?
- Efficient representation: O(nχ²) vs O(2ⁿ) for full quantum state
- Bond dimension χ controls expressivity vs efficiency tradeoff
- Can inspect prototype states directly → explainable ML

## Related: arXiv:2605.17578 - Quantum Probability in Complex Projective Geometry
- Quantum probabilities expressed purely via projective space geometry
- No Hilbert space reference needed
- Projection theorem for complex projective space
- Opens generalizations of quantum theory in other geometric settings
