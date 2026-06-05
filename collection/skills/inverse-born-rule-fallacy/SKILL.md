---
name: inverse-born-rule-fallacy
description: "Critical analysis methodology for quantum data encoding — identifies how naive amplitude encoding (psi=sqrt(P)) abelianizes the Hilbert space and fails to achieve genuine quantum advantage in QML/finance. Advocates for Dynamical Hamiltonian Encoding (DHE) where data generates non-commutative evolution."
---

# Inverse Born Rule Fallacy — Dynamical Hamiltonian Encoding

## Description
Critical methodology for analyzing quantum data encoding schemes in QML and quantum finance. Identifies the fundamental flaw in naive amplitude encoding: mapping classical probability P to quantum state via psi=sqrt(P) restricts data to the positive real orthant S+, abelianizing the accessible Hilbert space and making the representation "phase-deaf." Advocates for Dynamical Hamiltonian Encoding (DHE) where data generates non-commutative quantum evolution rather than serving as a static phase-locked vector.

## Activation Keywords
- amplitude encoding fallacy
- inverse born rule
- dynamical hamiltonian encoding
- DHE quantum encoding
- phase-deaf representation
- quantum data encoding critique
- 振幅编码缺陷
- 动态哈密顿编码
- QML encoding limitation
- non-commutative data encoding

## Tools Used
- exec: Run quantum circuit simulations comparing encoding schemes
- read: Analyze encoding methodology papers
- write: Implement DHE encoding circuits
- search_files: Locate QML encoding comparison studies

## Core Concepts

### The Inverse Born Rule Fallacy

In QML and Quantum Finance, amplitude encoding is motivated by its logarithmic storage capacity:
- n classical data points → log₂(n) qubits
- Standard mapping: psi = sqrt(P) where P is classical probability distribution

**The Problem**: This mapping restricts the data manifold to the positive real orthant S+
- Accessible Hilbert space is effectively abelianized
- Representation becomes "phase-deaf" — cannot leverage quantum interference
- Simple square-root mapping fails to recover non-commutative structure needed for quantum advantage
- Applying basis changes (Hadamard, etc.) to these states fails to replicate active phase-kickback mechanisms

### Dynamical Hamiltonian Encoding (DHE)

Instead of encoding data as static amplitudes, DHE makes data the generator of quantum evolution:
- Data parameters enter as coefficients in Hamiltonian: H(data)
- State evolves unitarily: |psi(t)> = exp(-i*H(data)*t)|psi_0>
- Non-commutativity arises naturally from data-dependent evolution
- Phase information is actively generated, not statically assigned

## Usage Patterns

### Pattern 1: Encoding Scheme Audit
When evaluating a QML or quantum finance pipeline:
1. Check if amplitude encoding uses psi=sqrt(P) mapping
2. Verify whether the encoded states span non-commuting subspaces
3. Test if basis changes provide genuine quantum advantage or just classical rotation
4. Flag encoding as "phase-deaf" if it cannot generate interference patterns

### Pattern 2: DHE Implementation
When building quantum ML or quantum finance models:
1. Define data-dependent Hamiltonian H(data) with non-commuting terms
2. Choose initial state |psi_0> (typically |+>^n or computational basis)
3. Evolve state: |psi(data)> = exp(-i*H(data)*t)|psi_0>
4. Measure in appropriate basis for downstream task
5. Optimize evolution time t as hyperparameter

### Pattern 3: Encoding Comparison
When comparing encoding schemes:
1. Compute Hilbert space coverage for each scheme
2. Measure phase diversity (variance of relative phases)
3. Test expressivity on classification benchmarks
4. Evaluate circuit depth vs expressivity tradeoff

## Instructions for Agents

### Step 1: Identify the Encoding Method
Check if the paper/code uses:
- `psi = sqrt(data) / norm` → Amplitude encoding (phase-deaf)
- `R(data) |0>` → Angle/rotation encoding
- `exp(-i*H(data)*t)` → Dynamical Hamiltonian Encoding (preferred)

### Step 2: Analyze Expressivity
For amplitude encoding:
1. Check if data is restricted to non-negative values
2. If yes: the state lives in positive orthant → abelianized
3. Compute the commutator [H_measure, H_data] for relevant observables
4. If commutator is zero: encoding cannot provide quantum advantage

### Step 3: Propose DHE Alternative
Replace static encoding with dynamical:
```
H(data) = sum_j data[j] * P_j + sum_{j,k} data[j]*data[k] * P_jk + ...
```
where P_j are Pauli operators. Non-commuting Pauli terms ensure non-trivial phase structure.

### Step 4: Circuit Implementation
```python
from qiskit import QuantumCircuit
import numpy as np

def dhe_encoding(data, evolution_time=1.0):
    """Dynamical Hamiltonian Encoding."""
    n = len(data)
    qc = QuantumCircuit(n)
    qc.h(range(n))  # Initial superposition
    
    # Single-qubit terms
    for i, d in enumerate(data):
        qc.rz(2 * d * evolution_time, i)
    
    # Two-qubit non-commuting terms
    for i in range(n-1):
        qc.rzz(2 * data[i] * data[i+1] * evolution_time, i, i+1)
    
    return qc
```

## Error Handling

### Phase-Deaf Encoding Detected
If analysis finds psi=sqrt(P) encoding:
1. Inform user that encoding abelianizes Hilbert space
2. Explain why basis changes (Hadamard) don't fix the issue
3. Propose DHE as alternative with concrete circuit implementation
4. Provide expressivity comparison data

### DHE Circuit Depth Too High
If DHE produces deep circuits:
1. Use Trotter decomposition with bounded error
2. Exploit data sparsity for term reduction
3. Apply variational compilation for hardware-efficient implementation

## Examples

### Example: Finance Feature Encoding
```python
# Classical financial features: [volatility, return, volume]
features = [0.15, 0.02, 1.2]

# BAD: Phase-deaf amplitude encoding
bad_state = np.sqrt(np.array(features)) / np.linalg.norm(np.array(features))
# All amplitudes real and positive → no interference possible

# GOOD: DHE encoding
qc = dhe_encoding(features, evolution_time=0.5)
# Non-commuting Rz and Rzz terms generate rich phase structure
```

## Resources
- arXiv: 2602.21350 — The Inverse Born Rule Fallacy
- arXiv: dynamical-hamiltonian-encoding (DHE) methodology
- Quantum Machine Learning encoding survey papers

## Related Skills
- quantum-ml-data-loading — Alternative encoding strategies
- qml-feature-encoding — Feature map design
- quantum-neural-architecture — QNN design patterns
