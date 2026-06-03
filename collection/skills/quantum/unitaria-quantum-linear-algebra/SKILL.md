---
name: unitaria-quantum-linear-algebra
description: Unitaria library methodology for implementing quantum linear algebra algorithms via block encodings. Provides NumPy-like interface for quantum algorithms, enabling composition, verification, and resource estimation without circuit execution.
---

# Unitaria: Quantum Linear Algebra via Block Encodings

## Description

Unitaria is a Python library that brings the simplicity of classical linear algebra toolkits (NumPy, SciPy) to quantum algorithm implementation using block encodings. A block encoding embeds a matrix as a sub-block of a larger unitary operator. Unitaria eliminates the need for deep low-level circuit construction knowledge by providing a composable array-like interface.

Key features: matrix arithmetic evaluation without ancilla qubits or simulation, automatic circuit extraction, resource estimation (gate counts, qubit counts, normalization constants), and Quantum Singular Value Transformation (QSVT) support.

Based on arXiv:2605.10768 (Deiml, Hüttenhofer, Mosco, 2026).

## Activation Keywords

- unitaria
- quantum linear algebra
- block encoding
- quantum singular value transformation
- QSVT
- quantum matrix operations
- quantum numpy
- 量子线性代数
- 块编码

## Tools Used

- execute_code: Run Unitaria Python code
- terminal: Install Unitaria via pip
- web_search: Search for Unitaria documentation and examples
- write_file: Create quantum algorithm implementations

## Usage Patterns

### Pattern 1: Quantum Algorithm Prototyping
When designing quantum algorithms that involve linear algebra (HHL, QSVT) without needing circuit-level details.

### Pattern 2: Resource Estimation
When estimating qubit counts, gate counts, and normalization constants for quantum algorithms ahead of hardware availability.

### Pattern 3: Block Encoding Composition
When composing multiple block-encoded matrices through addition, multiplication, or tensor products.

## Instructions for Agents

### Step 1: Install Unitaria

```bash
pip install unitaria
```

Source: https://github.com/tequilahub/unitaria

### Step 2: Define Block Encodings

```python
from unitaria import BlockEncoding
import numpy as np

# Encode a classical matrix as a block encoding
A = np.array([[1, 0], [0, -1]])
block_A = BlockEncoding.from_matrix(A)
```

### Step 3: Compose Operations

```python
# Standard linear algebra operations on block encodings
C = block_A + block_B          # Addition
D = block_A @ block_B          # Multiplication
E = block_A.tensor_product(block_B)  # Tensor product
```

### Step 4: Apply QSVT

```python
# Quantum Singular Value Transformation
from unitaria import qsvt

# Apply polynomial transformation to singular values
result = qsvt(block_A, polynomial=[1, 0, 1])  # Example polynomial
```

### Step 5: Extract Circuits and Resources

```python
# Get the quantum circuit
circuit = result.to_circuit()

# Resource estimation
gate_count = result.gate_count()
qubit_count = result.qubit_count()
normalization = result.normalization()
```

### Step 6: Verify Correctness

```python
# Matrix arithmetic evaluation without circuit simulation
expected = block_A.evaluate() @ block_B.evaluate()
actual = (block_A @ block_B).evaluate()
assert np.allclose(expected, actual)
```

## Key Technical Insights

### Why Block Encodings Matter
- **Unified framework**: Any linear algebra operation can be expressed as block encoding
- **Composition**: Block encodings compose naturally (add, multiply, tensor)
- **QSVT foundation**: Block encodings enable the full QSVT framework
- **Hardware-independent**: Develop algorithms before error-corrected hardware exists

### Unitaria's Innovation
- **NumPy-like API**: Familiar interface reduces barrier to entry
- **No simulation needed**: Matrix arithmetic evaluation path avoids exponential simulation
- **Automatic circuit extraction**: High-level composition → low-level circuits
- **Scalable verification**: Correctness checking beyond state-vector simulation limits

## Error Handling

### Normalization Issues
- Block encodings require proper normalization (spectral norm ≤ 1)
- Unitaria tracks normalization constants automatically
- If normalization exceeds bounds, rescale the input matrix

### Resource Explosion
- Deep compositions can lead to excessive gate counts
- Use Unitaria's resource estimation to check feasibility early
- Consider approximate block encodings for large matrices

## Resources

- GitHub: https://github.com/tequilahub/unitaria
- arXiv:2605.10768 - Original Unitaria paper
- QSVT documentation for polynomial transformations

## Related Skills

- quantum-linear-algebra-block-encoding
- qml-framework-agnostic-design
- quantum-ml-patterns
