---
name: quantum-circuit-sat-analysis
description: "Quantum circuit analysis via weighted model counting (#SAT). Based on Quokka# (arXiv:2605.16509), reducing quantum circuit simulation, verification, equivalence checking, and synthesis to #SAT solving. Use when: (1) analyzing quantum circuits via SAT solvers, (2) performing quantum circuit equivalence checking (exact or approximate), (3) synthesizing depth-optimal quantum circuits, (4) verifying quantum circuits using Hoare logic, (5) encoding quantum states/gates as Boolean formulas. Activation: quantum circuit SAT, weighted model counting quantum, Quokka#, quantum circuit verification, quantum equivalence checking, quantum circuit synthesis #SAT."
---

# Quantum Circuit SAT Analysis

Methodology for analyzing quantum circuits by reducing them to weighted model counting (#SAT). Based on Quokka# (Mei et al., Leiden University/TU Delft, arXiv:2605.16509).

## Core Idea

Represent quantum circuits as Boolean formulas with complex-valued weights. Feed the weighted CNF to a #SAT solver. The solver's output directly gives quantum amplitudes and probabilities.

This bridges classical satisfiability solving with quantum computation — state-of-the-art #SAT solvers become quantum circuit analyzers.

## Four Engines

### 1. Simulation Engine

**Input**: Circuit U, Measurement specification M
**Output**: Probability ⟨0ⁿ|U†MU|0ⁿ⟩
**Method**: Encode circuit as wCNF, solve with #SAT solver

### 2. Verification Engine

**Input**: Circuit U, Pre-condition P, Post-condition Q
**Output**: true iff {P}U{Q} (Hoare logic verification)
**Method**: Encode specification + circuit as wCNF

### 3. Equivalence Engine

**Input**: Circuits U, V, Precision ε
**Output**: true iff V is at least 1-ε similar to U
**Method**: Encode both circuits, compare via #SAT

### 4. Synthesis Engine

**Input**: Circuit U, Gate set G, Precision ε
**Output**: Depth-optimal circuit V in gate set G, at least 1-ε similar to U
**Method**: Iterative synthesis via Max#SAT

## Encoding Methods

### Computational-Basis Encoding

n-qubit state → Boolean formula over n variables + weight function:

```
|ψ⟩ = Σ α_x |x⟩  →  (F, W)
```

- Each basis state |x⟩ encoded as conjunction of literals
- Amplitude α_x encoded as weight W(x)
- Superpositions use auxiliary variables for non-unit amplitudes

Example: |+⟩ = 1/√2(|0⟩+|1⟩)
```
F_+(q, h) = h,  W(h) = 1/√2, W(¬h) = 1/√2
```

### Gate Encoding

Gate U encoded as Boolean relation F_U(q, q') such that:
```
F_U|φ⟩(q') = F_|φ⟩(q) ∧ F_U(q, q')
```

Example: Hadamard H = 1/√2[[1,1],[1,-1]]
```
F_H(q, q', h) = h ↔ (q ∧ q'),  W(h) = 1/√2
```

### Pauli-Basis Encoding

Alternative encoding using Pauli operator decomposition. Supports complex weights via extended GPMC model counter.

## Supported Gate Sets

- **Clifford+T**: Universal gate set with T gate for non-Clifford operations
- **Toffoli+H**: Toffoli + Hadamard, useful for reversible computing
- **Clifford+R**: Clifford + arbitrary rotation gates (RX, RY, RZ)

Users can add arbitrary gates by editing the encoding codegen scripts.

## Solver Integration

Quokka# actively collaborates with the #SAT community:
- **GPMC**: Extended with negative and complex weights
- **d4Max**: Max#SAT solver for synthesis, supports complex weights
- **Ganak**: State-of-the-art model counter, supports complex weights

## Extensibility Pattern

To add a new gate:

1. Express the gate's Boolean relation in SymPy syntax
2. Run codegen to produce CNF encoding
3. The gate is now available in all four engines

Example for X gate:
```python
# SymPy: Equivalent(q, ~q')  means q' ↔ ¬q
```

## Performance Trade-offs

| Encoding | Strengths | Weaknesses |
|----------|-----------|------------|
| Computational-basis | Direct state representation, efficient for |z⟩ states | Requires auxiliary variables for superpositions |
| Pauli-basis | Efficient for Clifford circuits | Less efficient for arbitrary rotations |

## Applications Beyond Quantum

The #SAT encoding pattern applies to any domain where:
- States can be encoded as Boolean formulas
- Transitions can be encoded as Boolean relations
- Weights capture amplitudes/probabilities/costs

This makes the methodology applicable to probabilistic reasoning, Markov processes, and optimization problems.

## Related Papers

- arXiv:2605.16509 — Quokka#: Quantum Computing with #SAT
- arXiv:2605.16523 — Lean-QEC: complementary formal verification approach
