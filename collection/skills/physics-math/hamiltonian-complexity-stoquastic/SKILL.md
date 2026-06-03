---
name: hamiltonian-complexity-stoquastic
description: "Hamiltonian complexity analysis methodology for stoquastic sparse Hamiltonians. Covers StoqMA complexity class, quantum complexity classification, and sparse Hamiltonian analysis. Activation: stoquastic Hamiltonian, Hamiltonian complexity, StoqMA, quantum complexity class"
---

# Hamiltonian Complexity: Stoquastic Sparse Hamiltonians

## Paper Reference
- **Title**: The Complexity of Stoquastic Sparse Hamiltonians
- **arXiv**: 2605.02845
- **Authors**: Alex B. Grilo, Marios Rozos
- **Date**: 2026-05-04

## Core Problem
Stoquastic Hamiltonians (those with non-positive off-diagonal elements in the computational basis) occupy a unique complexity class StoqMA between MA and QCMA. Understanding their complexity is crucial for quantum simulation and adiabatic quantum computing.

## Key Concepts

### 1. Stoquastic Hamiltonians
- **Definition**: H is stoquastic if ⟨i|H|j⟩ ≤ 0 for all i ≠ j in computational basis
- **Property**: Ground state can be chosen with all non-negative amplitudes (no sign problem)
- **Significance**: Amenable to quantum Monte Carlo simulation (no negative weight problem)

### 2. StoqMA Complexity Class
- **Definition**: Promise problems verifiable by a quantum verifier with stoquastic Hamiltonians
- **Position**: NP ⊆ MA ⊆ StoqMA ⊆ QCMA ⊆ QMA
- **Role**: Central to Cubitt-Montanaro classification of Hamiltonian complexity

### 3. Sparse Hamiltonian Simulation
- **Sparse**: Each row has at most poly(n) non-zero entries
- **Simulation cost**: Depends on sparsity, norm, and evolution time
- **Query complexity**: Optimal algorithms scale as O(τ polylog(τ/ε))

## Analysis Framework

### Step 1: Classify Hamiltonian
```python
def classify_hamiltonian(H):
    """Determine if Hamiltonian is stoquastic, sparse, and its complexity class."""
    is_stoquastic = all(H[i,j] <= 0 for i != j)
    sparsity = max(sum(1 for j in range(n) if H[i,j] != 0) for i in range(n))
    is_sparse = sparsity <= poly(log(n))
    return is_stoquastic, is_sparse, sparsity
```

### Step 2: Determine Complexity
```
Stoquastic + Sparse → StoqMA-complete (typically)
Non-stoquastic + Sparse → QMA-complete
Stoquastic + Dense → Depends on structure
```

### Step 3: Select Simulation Method
| Hamiltonian Type | Method | Complexity |
|-----------------|--------|------------|
| Stoquastic, sparse | Quantum Monte Carlo | Polynomial (no sign problem) |
| Non-stoquastic, sparse | Trotter-Suzuki / LCU | O(τ polylog(τ/ε)) |
| Stoquastic, dense | Variational methods | Depends on ansatz |
| Any, k-local | Phase estimation | O(1/ε) |

## Best Practices
1. **Check stoquasticity first**: Determines whether sign problem exists
2. **Exploit sparsity**: Sparse Hamiltonians have efficient simulation algorithms
3. **Classification theorem**: Use Cubitt-Montanaro framework for complete classification
4. **Gap analysis**: Spectral gap determines adiabatic runtime

## Related Skills
- quantum-systems-engineering
- quantum-ml-patterns
- quantum-computing-patterns
- distributed-quantum-computing
