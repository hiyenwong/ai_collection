---
name: ttn-quantum-state-preparation
description: >
  Log-depth quantum state preparation and circuit verification via Tree Tensor Network (TTN) compilation.
  Converts classical data into quantum states using MPS→TTN renormalization, achieving O(log N) circuit depth
  with verifiable fidelity. Use when: (1) preparing arbitrary quantum states on NISQ devices,
  (2) compiling classical data into quantum registers with bounded depth, (3) verifying quantum circuit
  fidelity via classical TTN simulation, (4) designing scalable state preparation circuits beyond 20+ qubits.
  Activation: quantum state preparation, TTN compilation, tensor network state prep, log-depth circuit,
  MPS to quantum circuit, state preparation verification, 量子态制备, 树张量网络编译
---

# TTN-Based Quantum State Preparation

Log-depth quantum circuit compilation from classical data using Tree Tensor Network (TTN) renormalization with verifiable fidelity bounds.

## Problem

Preparing an arbitrary n-qubit quantum state |ψ⟩ from classical data requires O(2ⁿ) gates in the general case — exponentially deep circuits that are infeasible on NISQ hardware. Standard methods (e.g., iterative multiplexor decomposition) produce O(2ⁿ) depth circuits regardless of the target state's structure.

## Core Principles

1. **MPS Representation**: Compress the 2ⁿ-dimensional state vector into a Matrix Product State (MPS) with bounded bond dimension χ, exploiting low entanglement structure.
2. **TTN Renormalization**: Convert the MPS to a Tree Tensor Network (TTN) with logarithmic depth O(log N), where each node is an isometric tensor mapping to a unitary gate.
3. **Log-Depth Compilation**: Extract quantum gates directly from TTN tensors, producing circuits of depth O(log N) instead of O(2ⁿ).
4. **Classical Verification**: Simulate the compiled circuit classically via TTN contraction to verify fidelity F = |⟨ψ_target|ψ_compiled⟩|² ≥ 1 - ε.
5. **Truncation Control**: Tune bond dimension χ to balance circuit complexity (∝ χ²) against fidelity loss, with explicit error bounds from truncated singular values.

## Core Algorithm

### Step 1: MPS Compression
Given target state |ψ⟩ ∈ ℂ^(2ⁿ):
```
Apply sequential SVD across n bipartitions:
|ψ⟩ → A¹ ⊗ A² ⊗ ... ⊗ Aⁿ  (bond dimension χ)
Truncate singular values σ_k < τ (threshold)
Fidelity bound: F ≥ 1 - Σ(truncated σ_k²)
```

### Step 2: MPS → TTN Conversion
```
Reshape MPS chain into binary tree:
- Leaf nodes: physical indices (qubits)
- Internal nodes: virtual indices (bond contractions)
- Depth: ⌈log₂(n)⌉
Each node becomes an isometry W: W†W = I
```

### Step 3: Gate Extraction
```
For each TTN tensor W at node i:
  1. Reshape W as matrix M (input ⊗ bond → output ⊗ bond)
  2. Apply unitary completion: U = complete(M)
  3. Decompose U into native gates (CNOT + single-qubit)
  4. Assign to qubits based on tree topology
```

### Step 4: Fidelity Verification
```
Contract TTN classically to compute |ψ_TTN⟩
F = |⟨ψ_target|ψ_TTN⟩|²
Accept if F ≥ F_min (typically 0.99)
If F < F_min: increase χ and retry
```

## Implementation Steps

### 1. State Preparation Pipeline
```python
import numpy as np
from scipy.linalg import svd

def mps_compress(state_vector, max_bond_dim=64, threshold=1e-8):
    """Compress state vector into MPS with bounded bond dimension."""
    n_qubits = int(np.log2(len(state_vector)))
    tensors = []
    remaining = state_vector.reshape([2] * n_qubits)
    
    for i in range(n_qubits - 1):
        remaining = remaining.reshape(-1, remaining.shape[-1])
        U, S, Vt = svd(remaining, full_matrices=False)
        
        # Truncate
        keep = np.where(S > threshold)[0]
        keep = keep[:max_bond_dim]
        U, S, Vt = U[:, keep], S[keep], Vt[keep, :]
        
        tensors.append(U.reshape(-1, 2, S.shape[0]))
        remaining = np.diag(S) @ Vt
    
    tensors.append(remaining.reshape(-1, 2, 1))
    return tensors

def mps_to_ttn(mps_tensors):
    """Convert MPS chain to TTN via recursive grouping."""
    def group(tensors):
        if len(tensors) == 1:
            return tensors[0]
        mid = len(tensors) // 2
        left = group(tensors[:mid])
        right = group(tensors[mid:])
        # Contract and re-factor as isometry
        merged = np.tensordot(left, right, axes=([-1], [-1]))
        # Reshape and SVD to get isometric form
        shape = merged.shape
        merged = merged.reshape(-1, shape[-1])
        U, S, Vt = svd(merged, full_matrices=False)
        return U.reshape(shape[:-1] + (S.shape[0],))
    
    return group(mps_tensors)
```

### 2. Circuit Compilation
```python
def ttn_to_circuit(ttn_root, native_gates='cnot+u3'):
    """Extract quantum gates from TTN root tensor."""
    # Each isometric tensor W maps to a unitary block
    # Decompose into native gate set using KAK or Qiskit's TwoQubitBasisDecomposer
    gates = []
    traverse_and_decompose(ttn_root, gates)
    return gates
```

### 3. Fidelity Verification
```python
def verify_fidelity(target_state, ttn_tensors):
    """Classically verify compiled circuit fidelity via TTN contraction."""
    compiled_state = contract_ttn(ttn_tensors)
    fidelity = np.abs(np.vdot(target_state, compiled_state))**2
    return fidelity
```

## Decision Table

| Scenario | Bond Dimension χ | Expected Depth | Fidelity |
|----------|-----------------|----------------|----------|
| Product states | χ = 1 | O(log n) | F = 1.0 |
| Low entanglement | χ = 4-16 | O(log n) | F ≥ 0.999 |
| Moderate entanglement | χ = 32-64 | O(n log n) | F ≥ 0.99 |
| High entanglement | χ > 128 | O(n²) | F ≥ 0.95 |
| Volume-law states | χ = O(2ⁿ) | O(2ⁿ) | F ≈ 1.0 |

## Pitfalls

1. **Volume-law entanglement**: States with volume-law entanglement scaling require exponentially large χ, negating log-depth advantage. Check entanglement entropy S ≤ log(χ) before applying.
2. **Truncation error accumulation**: Sequential SVD truncations compound errors across layers. Use global error budget: Σ ε_i ≤ ε_total.
3. **Gate decomposition overhead**: Converting arbitrary unitaries to CNOT+U3 introduces additional depth. Factor this into total depth estimate.
4. **Numerical stability**: Very small singular values (< 1e-15) can cause numerical instability in SVD. Apply threshold truncation before decomposition.
5. **Verification bottleneck**: Classical TTN contraction for fidelity verification scales as O(nχ³). For large χ, use Monte Carlo sampling or tensor network approximations.

## References

- arXiv: 2605.06579v1 (2025-05-06)
  "Practical Log-Depth Quantum State Preparation and Circuit Verification via Tree Tensor Network Compilation"
- Related: MPS compression (Schollwöck, 2011), TTN networks (Shi et al., 2006)
- Qiskit: `qiskit.quantum_info.Statevector`, `qiskit.circuit.library`
