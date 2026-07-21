# TEE-Regulated VQA: Key Formulas & Implementation Details

## Topological Entanglement Entropy (TEE)

### Kitaev-Preskill Construction

TEE = S(A) + S(B) + S(C) - S(AB) - S(BC) - S(AC) + S(ABC)

Where S(X) = -Tr(ρ_X log ρ_X) is the von Neumann entropy of the reduced density matrix ρ_X.

### Regime Classification

| TEE Value | Regime | Trainability |
|-----------|--------|-------------|
| TEE > 0 | Sparse structured state | ✅ Trainable |
| TEE = 0 | Critical point (edge of chaos) | ⚠️ Marginal |
| TEE < 0 | Untrainable chaos | ❌ Divergent |

### Cost Function with TEE Regularization

L_total(θ) = ⟨H⟩(θ) + λ · max(0, -TEE(θ))

- λ = regularization strength (start small ~0.01-0.1, increase if diverging)
- The max(0, -TEE) term only activates in the chaotic regime
- Guides optimization toward the "edge of chaos" boundary

### Quantum Nyquist-Shannon Bounds

The theorem establishes:
- Resource bound: minimum qubits needed to encode a function of given smoothness
- Error bound: how encoding errors propagate through VQA training
- Complexity bound: structural complexity of the quantum state vs. classical function

### Subsystem Partitioning Strategy

For a ring of n qubits:
- Divide into 3 contiguous regions A, B, C
- Each region should contain O(n/3) qubits
- Boundaries between regions capture topological information

For general geometries:
- Choose regions based on problem graph structure
- A, B, C should be spatially connected
- Avoid single-qubit regions (finite-size effects)

## Source Paper

Hashizume, T., Wang, Z., Schlawin, F., & Jaksch, D. (2026). "Quantum computation at the edge of chaos." arXiv: 2604.15441.
