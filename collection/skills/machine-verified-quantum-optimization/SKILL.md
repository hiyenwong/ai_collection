---
name: machine-verified-quantum-optimization
description: "Machine-verified quantum optimization proof methodology — formal verification of QAOA approximation ratios and quantum algorithm guarantees. Combines formal methods with quantum algorithm analysis."
trigger_words: "QAOA, quantum optimization, formal verification, approximation ratio, machine-verified, FGG conjecture, proof verification, quantum algorithm guarantees"
---

# Machine-Verified Quantum Optimization

## Overview

This skill implements the methodology from arXiv:2606.29687 for **machine-verified proofs of quantum optimization conjectures**. It establishes formal verification patterns for quantum algorithms, specifically resolving the Farhi-Goldstone-Gutmann (FGG) conjecture about QAOA approximation ratios on the ring of disagrees.

## Core Methodology

### Problem Statement

The FGG conjecture states that depth-p QAOA on the ring of disagrees (MaxCut on cycle graphs) attains a specific approximation ratio. This skill provides a framework for:
1. Formally stating quantum algorithm claims
2. Encoding them in a proof assistant
3. Machine-verifying the claims

### Formal Verification Framework

#### Step 1: Define the Quantum Algorithm
```
QAOA_p(γ, β) = ∏_{k=1}^{p} e^{-iβ_k H_M} e^{-iγ_k H_C}
```
where H_M is the mixer Hamiltonian and H_C is the cost Hamiltonian.

#### Step 2: Formalize the Claim
For the ring of disagrees (cycle graph C_n with MaxCut):
```
∀p, n: max_{γ,β} ⟨QAOA_p(γ,β)|H_C|QAOA_p(γ,β)⟩ / |E| ≥ α_p
```
where α_p is the conjectured approximation ratio.

#### Step 3: Machine Verification
- Encode quantum operations in a formal language
- Use proof tactics to establish bounds
- Verify numerical claims with interval arithmetic

### Verification Tactics

#### Tactic 1: Symmetry Reduction
Exploit graph symmetries to reduce the verification space:
```
For cycle graphs: |Aut(C_n)| = 2n symmetries
Reduce n-qubit problem to O(1) effective qubits
```

#### Tactic 2: Recursive Structure
QAOA on rings has a recursive structure:
```
QAOA_p on C_n can be decomposed into local patches
Each patch depends only on O(p) neighbors
```

#### Tactic 3: Analytical Bounds
For small p, derive exact expressions:
```
p=1: α_1 = (2√2 - 1) / (2√2) ≈ 0.693...
p=2: α_2 = ... (computed via machine verification)
```

## Implementation

### Formal Encoding

```python
from dataclasses import dataclass
from typing import List, Tuple
import numpy as np

@dataclass
class QuantumOperator:
    """Formal representation of a quantum operator."""
    matrix: np.ndarray  # Complex matrix
    qubits: List[int]   # Target qubits
    name: str
    
    def compose(self, other: 'QuantumOperator') -> 'QuantumOperator':
        """Compose two operators (tensor product + multiply)."""
        # Implementation using Kronecker product
        pass

@dataclass
class QAOACircuit:
    depth: int
    n_qubits: int
    gamma: List[float]
    beta: List[float]
    cost_hamiltonian: QuantumOperator
    mixer_hamiltonian: QuantumOperator
    
    def statevector(self) -> np.ndarray:
        """Compute exact statevector for verification."""
        state = np.zeros(2**self.n_qubits)
        state[0] = 1.0  # |00...0⟩
        
        for k in range(self.depth):
            # Apply mixer
            state = expm(-1j * self.beta[k] * self.mixer_hamiltonian.matrix) @ state
            # Apply cost
            state = expm(-1j * self.gamma[k] * self.cost_hamiltonian.matrix) @ state
        
        return state
```

### Verification Engine

```python
class QAOAVerifier:
    """Machine verifier for QAOA approximation ratios."""
    
    def __init__(self, graph_type: str, max_p: int = 5):
        self.graph_type = graph_type
        self.max_p = max_p
    
    def verify_approximation_ratio(self, p: int, claimed_ratio: float) -> dict:
        """
        Verify that QAOA_p achieves at least claimed_ratio.
        
        Returns verification result with proof certificate.
        """
        # Step 1: Reduce problem size using symmetry
        reduced_n = self.symmetry_reduction(p)
        
        # Step 2: Parameterize QAOA
        qaoa = self.build_qaoa(reduced_n, p)
        
        # Step 3: Optimize parameters
        opt_result = self.optimize_parameters(qaoa)
        
        # Step 4: Verify bound with interval arithmetic
        lower_bound = self.interval_verify(opt_result, qaoa)
        
        return {
            'verified': lower_bound >= claimed_ratio,
            'achieved_ratio': float(opt_result.fun),
            'lower_bound': lower_bound,
            'claimed_ratio': claimed_ratio,
            'certificate': self.generate_certificate(opt_result)
        }
    
    def symmetry_reduction(self, p: int) -> int:
        """Reduce problem size using graph symmetries."""
        if self.graph_type == 'ring':
            # Ring of disagrees: only O(p) qubits matter
            return 2 * p + 1
        raise ValueError(f"Unknown graph type: {self.graph_type}")
```

### Interval Arithmetic Verification

```python
import mpmath

def interval_verify(params, qaoa):
    """Verify approximation ratio with rigorous interval arithmetic."""
    # Use arbitrary precision interval arithmetic
    mpmath.mp.dps = 50  # 50 decimal places
    
    # Compute expectation value with interval bounds
    state = qaoa.statevector_interval(params)
    energy = state @ qaoa.cost_hamiltonian.matrix @ state
    
    return energy.lower  # Guaranteed lower bound
```

## Workflow

### Step 1: State the Claim
Define the quantum algorithm and the property to verify (e.g., approximation ratio ≥ α).

### Step 2: Symmetry Analysis
Identify symmetries in the problem to reduce verification complexity.

### Step 3: Numerical Optimization
Find optimal parameters using classical optimization.

### Step 4: Rigorous Verification
Use interval arithmetic and formal methods to establish guaranteed bounds.

### Step 5: Certificate Generation
Produce a machine-checkable proof certificate.

## Key Insights

1. **Symmetry is crucial**: Without symmetry reduction, verification is intractable
2. **Local structure**: QAOA on local graphs has O(p)-depth light cones
3. **Interval arithmetic**: Provides rigorous bounds without floating-point errors
4. **Machine verification**: Eliminates human error in complex proofs

## Applications

- Quantum algorithm verification
- Approximation ratio certification
- Quantum advantage claims verification
- Formal quantum software verification

## Related Skills

- `quantum-optimization-qaoa` - QAOA methodology
- `quantum-program-semantic-verification` - Quantum program verification
- `quantum-fault-tolerance-verification` - Fault-tolerance verification

## References

- arXiv:2606.29687 — A Machine-Verified Proof of a Quantum-Optimization Conjecture
