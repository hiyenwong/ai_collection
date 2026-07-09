# Quantum Circuit Cutting Techniques

## Overview

Circuit cutting divides large quantum circuits into smaller subcircuits that can be executed on limited-qubit hardware, then reconstructs results via classical post-processing.

## Motivation

NISQ hardware constraints:
- Limited qubits (typically 5-50)
- Gate connectivity limitations
- Noise and decoherence

Large quantum circuits (> hardware qubits) require cutting to execute.

## Basic Concept

```
Original Circuit (12 qubits) on 8-qubit hardware:

Cut at qubit 4:
┌─────────────┐    ┌─────────────┐
│ Subcircuit1 │ ←→ │ Subcircuit2 │
│  (qubits 0-7)│    │ (qubits 4-11)│
└─────────────┘    └─────────────┘

Execute subcircuits separately, reconstruct via post-processing.
```

## Cutting Methods

### 1. Wire Cutting

Cut a single qubit wire:

```python
def wire_cut(circuit, cut_position):
    """
    Cut circuit at specified qubit wire position.
    
    Returns:
        - Subcircuit A (before cut)
        - Subcircuit B (after cut)
        - Reconstruction coefficients
    """
    subcirc_a = extract_subcircuit(circuit, 0, cut_position)
    subcirc_b = extract_subcircuit(circuit, cut_position, end)
    
    # Reconstruction requires 4 basis states
    basis_states = ['0', '1', '+', '-']
    
    return subcirc_a, subcirc_b, basis_states
```

**Overhead**: O(4^k) where k = number of cuts

### 2. Gate Cutting

Cut at a specific gate:

```python
def gate_cut(circuit, gate_position):
    """
    Cut circuit at specific gate (e.g., CNOT).
    
    Suitable for sparse circuits with specific cut points.
    """
    # Decompose gate into local operations
    # Execute separately
    # Reconstruct via tensor product
```

**Overhead**: O(16^k) for two-qubit gates (CNOT)

### 3. Automatic Cutting

Automatically find optimal cut positions:

```python
def auto_cut(circuit, max_qubits):
    """
    Automatically cut circuit to fit max_qubits constraint.
    
    Strategy:
        1. Analyze circuit topology
        2. Find minimal-cut positions
        3. Minimize reconstruction overhead
    """
    # Use graph partitioning algorithms
    cut_positions = find_minimal_cuts(circuit, max_qubits)
    
    return apply_cuts(circuit, cut_positions)
```

## Reconstruction

### Step 1: Execute Subcircuits

```python
# Execute each subcircuit with different basis states
results_a = []
for basis in ['0', '1', '+', '-']:
    # Initialize cut qubit in basis state
    result = execute(subcirc_a, initial_state=basis)
    results_a.append(result)

results_b = []
for basis in ['0', '1', '+', '-']:
    # Measure cut qubit in basis
    result = execute(subcirc_b, measure_basis=basis)
    results_b.append(result)
```

### Step 2: Reconstruct Original Results

```python
def reconstruct(results_a, results_b, coefficients):
    """
    Reconstruct original circuit results via weighted sum.
    
    Formula:
        P_final = Σ_i,j coeff[i,j] × P_a[i] ⊗ P_b[j]
    """
    final_result = 0
    
    for i in range(4):
        for j in range(4):
            final_result += coefficients[i,j] * results_a[i] * results_b[j]
    
    return final_result
```

## Overhead Analysis

### Wire Cutting

| Number of Cuts | Overhead Factor |
|----------------|-----------------|
| 1 cut | 4× execution |
| 2 cuts | 16× execution |
| 3 cuts | 64× execution |
| k cuts | 4^k × execution |

### Gate Cutting (Two-Qubit)

| Number of Cuts | Overhead Factor |
|----------------|-----------------|
| 1 cut | 16× execution |
| 2 cuts | 256× execution |
| k cuts | 16^k × execution |

**Key Insight**: Minimize cuts to reduce exponential overhead.

## Optimization Strategies

### 1. Minimal Cut Finding

Use graph partitioning:

```python
import networkx as nx

def find_minimal_cuts(circuit, max_qubits):
    """
    Find cut positions that minimize overhead.
    
    Treat circuit as graph:
        - Nodes = qubits
        - Edges = gates
        
    Find partition with:
        - Each partition ≤ max_qubits
        - Minimal edge cuts
    """
    graph = circuit_to_graph(circuit)
    
    # Use Kernighan-Lin or METIS algorithm
    partitions = nx.algorithms.community.kernighan_lin_bisection(graph)
    
    return extract_cut_positions(partitions)
```

### 2. Sparse Circuit Design

Design circuits to minimize cutting:

```python
def sparse_cnot_pattern(qubits, depth):
    """
    Design sparse CNOT pattern to reduce cut needs.
    
    Strategy:
        - Connect only nearest neighbors
        - Avoid long-range entanglement
        - Use local operations when possible
    """
    cnot_pairs = []
    
    for layer in range(depth):
        # Only connect adjacent qubits
        for i in range(qubits - 1):
            cnot_pairs.append((i, i+1))
    
    return cnot_pairs
```

### 3. Hybrid Classical-Quantum Split

Move part of computation to classical:

```python
def hybrid_split(circuit, classical_threshold):
    """
    Split circuit into quantum and classical parts.
    
    Quantum: High-entanglement operations
    Classical: Post-processing, low-entanglement ops
    """
    quantum_part = extract_quantum_operations(circuit)
    classical_part = extract_classical_operations(circuit)
    
    return quantum_part, classical_part
```

## Practical Considerations

### Hardware Constraints

| Hardware | Qubits | Recommended Max Circuit |
|----------|--------|-------------------------|
| IBM Quantum | 5-127 | Match qubit count or use 1-2 cuts |
| Google Sycamore | 53 | ≤ 53 qubits, minimal cuts |
| Rigetti | 8-40 | Sparse patterns, 1-2 cuts |
| IonQ | 11-32 | All-to-all connectivity, easier cutting |

### Noise Impact

Circuit cutting amplifies noise:
- Multiple executions → noise accumulation
- Reconstruction errors from noisy subcircuit results
- Need error mitigation for each subcircuit

### Classical Post-processing

Reconstruction requires:
- Storage for all subcircuit results
- Classical computation for weighted sums
- May bottleneck overall runtime

## Implementation Libraries

```python
# Qiskit Circuit Cutting
from qiskit.circuit.library import CircuitCutting

# Pennylane Circuit Cutting
import pennylane as qml
qml.cut_circuit(...)

# Cirq Circuit Cutting
import cirq
cirq.CircuitCut(...)
```

## QNAS Integration

QNAS estimates cutting overhead in objective 3:

```python
def estimate_cutting_overhead(architecture, target_qubits):
    """
    Estimate number of subcircuits needed.
    
    Formula:
        overhead = 4^k if wire_cut
        overhead = 16^k if gate_cut
        
    where k = ceil((circuit_qubits - target_qubits) / cut_per_wire)
    """
    circuit_qubits = architecture['qubits']
    
    if circuit_qubits <= target_qubits:
        return 1  # No cutting needed
    
    # Estimate number of cuts needed
    k = estimate_minimal_cuts(circuit_qubits, target_qubits)
    
    # Use wire cutting overhead (lower)
    overhead = 4 ** k
    
    return overhead
```

---

*Reference: Peng, B., et al. "Simulating Large Quantum Circuits on Small Quantum Computers" (2020)*