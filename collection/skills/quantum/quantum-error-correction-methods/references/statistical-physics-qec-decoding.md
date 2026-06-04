# Statistical Physics Approach to Quantum Error Correction Decoding

Detailed reference for reformulating MLD as partition function computation in classical spin models.
Source: arXiv:2605.17230v1 (Cao, Yan & Du, 2026).

## CSS Code to Spin Model Mapping

### Code Structure
- X-stabilizers: H_X · z = 0 (mod 2)
- Z-stabilizers: H_Z · z = 0 (mod 2)
- Orthogonality: H_X · H_Z^T = 0
- Error model: Pauli errors E = X^a Z^b with probabilities p_x, p_z
- Syndrome: s_X = H_X · a, s_Z = H_Z · b

### MLD Objective
Find most likely logical class given syndrome s:
```
P(L|s) ∝ Σ_{E ∈ class L} P(E|s) = Σ_{E: H·E = s, E ∈ L} P(E)
```

### Spin Model Construction
Each qubit → spin variable s_i ∈ {+1, -1}
Error on qubit i → s_i = -1 (flip)

Hamiltonian:
```
H(s) = -Σ_i h_i · s_i - Σ_{stabilizers} J_α · Π_{i∈α} s_i
```
where:
- h_i = log((1-p_i)/p_i) from local error rates
- J_α = coupling from stabilizer constraints
- Quenched disorder = random syndrome values

Partition function:
```
Z = Σ_s exp(-H(s))
```

### Phase Transition Interpretation
- Below threshold: Ordered phase → successful decoding
- At threshold: Critical point → phase transition on Nishimori line
- Above threshold: Disordered phase → decoding failure

## Algorithm Implementations

### Tensor Network Exact MLD
- Build tensor network from code structure
- Each qubit → local tensor, each stabilizer → constraint tensor
- Optimize contraction order for minimal bond dimension
- Contract to get partition function for each logical class
- Best for: n < 1000 qubits, low treewidth codes

### Belief Propagation Approximate MLD
- Initialize messages from noise probabilities: m = log((1-p)/p)
- Iterative message passing: check-to-variable, variable-to-check
- Check syndrome satisfaction after each iteration
- Guaranteed convergence for tree-like factor graphs
- Best for: n > 1000 qubits, sparse codes (qLDPC, surface codes)

### Code Geometry Impact
| Code Type | Geometry | TN Complexity | BP Convergence |
|-----------|----------|---------------|----------------|
| Surface code | 2D lattice | Moderate (χ^d) | Good (locally tree-like) |
| qLDPC | Sparse graph | Low | Excellent (tree-like) |
| Color code | Triangular | Higher | Moderate (short cycles) |

## Practical Tuning
- Temperature: Set β = log((1-p)/p) for physical noise rate p
- BP iterations: 50-200 for most codes
- TN bond dimension: χ = 16-64 for surface codes
- Syndrome as quenched disorder: average over syndrome distribution for typical behavior
