---
name: unitaria-quantum-linear-algebra
description: "Python library methodology for quantum linear algebra via block encodings. Provides NumPy/SciPy-like interface for quantum algorithms without low-level circuit construction. Based on arXiv:2605.10768."
---

# Unitaria: Quantum Linear Algebra via Block Encodings

Python library methodology that brings NumPy/SciPy simplicity to quantum algorithms based on block encodings (arXiv:2605.10768).

## Core Problem

Block encodings embed matrices as sub-blocks of larger unitary operators. Implementation traditionally requires deep knowledge of low-level circuit construction, creating a high barrier for quantum algorithm development.

## Methodology

### 1. Block Encoding Abstraction
- Matrix embedded as sub-block of larger unitary operator
- Composable, array-like interface
- Standard operations: addition, multiplication, tensor products
- Quantum Singular Value Transformation (QSVT) support

### 2. Matrix-Arithmetic Evaluation Path
- Operations computed directly on encoded vectors and matrices
- No dependence on ancilla qubits or circuit simulation
- Enables correctness verification beyond state vector simulation limits
- Classical simulation scales beyond traditional limits

### 3. Automatic Circuit Extraction
- Define block encodings through standard array operations
- Combine encodings using standard math operations
- Extract resulting quantum circuits automatically
- Resource estimation without executing any circuit

### 4. Resource Estimation
- Gate counts
- Qubit counts
- Normalization constants
- All computed without circuit execution

### 5. Development Workflow
```python
# Unitaria-style workflow (pseudocode)
import unitaria as ua

# Define block encodings
A = ua.BlockEncoding(matrix_A)
B = ua.BlockEncoding(matrix_B)

# Standard operations
C = A + B  # Addition
D = A @ B  # Multiplication
E = ua.tensor_product(A, B)  # Tensor product
F = ua.qsvt(D, polynomial)  # QSVT

# Extract circuit
circuit = E.extract_circuit()

# Resource estimation
resources = E.estimate_resources()
print(resources.gate_count)
print(resources.qubit_count)
```

## Key Advantages
- Eliminates need for low-level circuit knowledge
- Enables algorithm development before fault-tolerant hardware exists
- Supports verification and analysis at scale
- Open source (GitHub: tequilahub/unitaria)

## Applications
- Quantum linear systems algorithms
- Quantum machine learning pipelines
- Hamiltonian simulation
- Quantum signal processing
- Any algorithm requiring block encodings

## Limitations
- Requires understanding of block encoding theory
- Resource estimates are theoretical (not hardware-specific)
- Circuit extraction may produce suboptimal circuits
- Designed for future fault-tolerant hardware

## Activation
- unitaria
- quantum linear algebra
- block encoding
- quantum singular value transformation
- QSVT
- quantum matrix operations

## References
- arXiv:2605.10768 - Unitaria: Quantum Linear Algebra via Block Encodings
- GitHub: https://github.com/tequilahub/unitaria
- QSVT and block encoding theory
