---
name: statistical-physics-quantum-decoding
description: "Statistical physics approach to quantum error correction decoding — reformulating maximum likelihood decoding (MLD) as partition function computation in classical spin models. Enables exact MLD via tensor networks and approximate MLD via belief propagation with convergence guarantees. Applicable to CSS codes, surface codes, quantum LDPC codes."
category: quantum-error-correction
---

# Statistical Physics Quantum Decoding Methodology

Reformulating quantum error correction maximum likelihood decoding (MLD) as partition function computation in classical statistical mechanical models, revealing deep connections between quantum decoding and statistical phase transitions.

## Core Concept (arXiv:2605.17230v1)

Maximum Likelihood Decoding is provably optimal for QEC but computationally intractable for general codes. This methodology bridges the gap:

1. **MLD ↔ Partition Function**: For CSS codes, MLD maps to computing partition functions of classical spin models with quenched disorder
2. **Statistical Phase Transitions**: Decoding threshold corresponds to thermodynamic phase transition in the spin model
3. **Exact Algorithms**: Tensor network contraction provides exact MLD
4. **Approximate Algorithms**: Belief propagation with guaranteed convergence for tree-like factor graphs

## Mathematical Framework

### CSS Code Structure
```
CSS code defined by:
- X-stabilizers: H_X · z = 0 (mod 2)  
- Z-stabilizers: H_Z · z = 0 (mod 2)
- Orthogonality: H_X · H_Z^T = 0

Error model: Pauli errors E = X^a Z^b with probabilities p_x, p_z
Syndrome: s_X = H_X · a, s_Z = H_Z · b
```

### MLD as Partition Function
```
MLD objective: Find most likely logical class given syndrome s

P(L|s) ∝ Σ_{E ∈ class L} P(E|s)
       = Σ_{E: H·E = s, E ∈ L} P(E)

This is equivalent to a partition function:
Z_L = Σ_{σ: constraints} exp(-β·H(σ))

where:
- σ = spin configuration representing error pattern
- H(σ) = energy = -log P(error pattern)
- β = inverse temperature (related to noise strength)
- constraints = syndrome satisfaction
```

### Spin Model Mapping
```
For CSS codes under independent noise:

Each qubit → spin variable s_i ∈ {+1, -1}
Error on qubit i → s_i = -1 (flip)

Hamiltonian:
H(s) = -Σ_i h_i · s_i - Σ_{stabilizers} J_α · Π_{i∈α} s_i

where:
- h_i = log((1-p_i)/p_i) from local error rates
- J_α = coupling from stabilizer constraints
- Quenched disorder = random syndrome values

Partition function:
Z = Σ_s exp(-H(s))
```

## Algorithmic Patterns

### Exact MLD via Tensor Networks
```python
import numpy as np

def tensor_network_mld(stabilizer_matrix, syndrome, noise_probs):
    """Exact MLD via tensor network contraction.
    
    Maps QEC decoding to tensor network contraction:
    - Each qubit → local tensor
    - Each stabilizer → constraint tensor
    - Contraction order optimized for minimal bond dimension
    """
    # Build tensor network from code structure
    # Optimize contraction order (greedy or dynamic programming)
    # Contract to get partition function for each logical class
    # Return most likely logical class
    pass
```

### Approximate MLD via Belief Propagation
```python
def belief_propagation_decoding(parity_check, syndrome, noise_probs, max_iter=100):
    """Belief propagation for approximate MLD.
    
    Guaranteed convergence for tree-like factor graphs.
    For graphs with cycles (surface codes, qLDPC):
    - Converges to good approximation below threshold
    - May fail above threshold (phase transition)
    """
    # Initialize messages from noise probabilities
    messages = np.log((1 - noise_probs) / noise_probs)
    
    for iteration in range(max_iter):
        # Check-to-variable messages
        # Variable-to-check messages  
        # Update beliefs
        # Check syndrome satisfaction
        
        if syndrome_satisfied:
            break
    
    return most_likely_error_pattern
```

## Key Insights

### 1. Decoding Threshold = Phase Transition
```
Below threshold: Ordered phase → successful decoding
At threshold: Critical point → phase transition
Above threshold: Disordered phase → decoding failure

This connects QEC threshold theorems to statistical mechanics.
```

### 2. Code Geometry Matters
```
Surface codes: 2D lattice → short-range interactions
qLDPC codes: Sparse graph → locally tree-like
Color codes: Triangular lattice → higher-order interactions

Geometry determines:
- Computational complexity of MLD
- BP convergence properties
- Optimal contraction order for TN
```

### 3. Syndrome as Quenched Disorder
```
Random syndrome = random magnetic field in spin model
Different syndrome instances = different disorder realizations
Need to average over syndrome distribution for typical behavior
```

## Practical Guidelines

### When to Use Tensor Network MLD
- Small to medium code sizes (n < 1000 qubits)
- Need exact optimal decoding
- Code has low treewidth (e.g., 1D, tree-like)
- Computing decoding thresholds

### When to Use Belief Propagation
- Large codes (n > 1000 qubits)
- Sparse codes (qLDPC, surface codes)
- Real-time decoding needed
- Below threshold regime

### Tuning Parameters
- **Temperature**: Set β = log((1-p)/p) for physical noise rate p
- **BP iterations**: 50-200 for most codes
- **TN bond dimension**: χ = 16-64 for surface codes

## Pitfalls

1. **BP on loopy graphs**: Convergence not guaranteed for codes with many short cycles
2. **TN contraction order**: Wrong order → exponential blowup in bond dimension
3. **Degenerate errors**: Multiple error patterns give same syndrome → need to sum not maximize
4. **Correlated noise**: Standard mapping assumes independent errors

## Verification

1. Test against known optimal decoders for small codes
2. Verify logical error rate scaling with code distance
3. Compare with MWPM (minimum weight perfect matching) for surface codes
4. Check BP convergence behavior across noise rates

## Activation Keywords

- Maximum likelihood decoding, MLD
- Quantum error correction decoding
- Statistical physics QEC
- Tensor network decoding
- Belief propagation quantum codes
- CSS code decoding
- Phase transition threshold

## References

- Cao, H., Yan, G. & Du, Y. (2026). "Maximum Likelihood Decoding of Quantum Error Correction Codes." arXiv:2605.17230v1.