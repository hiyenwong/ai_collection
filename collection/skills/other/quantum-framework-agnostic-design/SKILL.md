---
name: quantum-framework-agnostic-design
description: Design framework-agnostic quantum machine learning (QML) systems that eliminate vendor lock-in. Use when building QML solutions that need to work across multiple quantum computing platforms (IBM Quantum, Amazon Braket, Azure Quantum, IonQ, Rigetti), or when designing quantum neural networks for cross-framework compatibility. Covers unified computational graphs, hardware abstraction layers, and multi-framework export strategies. Activation: framework-agnostic QML, quantum vendor lock-in, QML interoperability, cross-platform quantum ML, quantum neural network portability, framework-independent quantum computing.
---

# Quantum Framework-Agnostic Design

Design QML systems that work seamlessly across quantum computing frameworks and hardware backends.

## Core Architecture Components

From arXiv:2604.04414 - Framework-agnostic quantum neural network architecture:

### 1. Unified Computational Graph

Abstract quantum operations into vendor-independent graph:

```python
# Unified quantum operation representation
class QuantumOp:
    name: str          # Operation type (CNOT, H, RX, etc.)
    qubits: List[int]  # Target qubits
    params: Dict       # Gate parameters
    # Framework-specific implementations injected at runtime
```

**Key pattern**: Define quantum circuit once, execute everywhere.

### 2. Hardware Abstraction Layer (HAL)

Single API for multiple backends:

| Backend | Provider | Capabilities |
|---------|----------|--------------|
| IBM Quantum | qiskit | Gate-based, simulators |
| Amazon Braket | braket | Gate-based, annealing |
| Azure Quantum | azure-quantum | Multiple providers |
| IonQ | ionq | Trapped ion |
| Rigetti | pyquil | Superconducting |

HAL interface:
```python
abstract class QuantumHAL:
    def execute(circuit: QuantumCircuit) -> Results
    def get_backend_info() -> BackendInfo
    def estimate_cost(circuit) -> CostEstimate
```

### 3. Multi-framework Export Pipeline

Lossless circuit translation via ONNX metadata:

- Export from: Qiskit, Cirq, PennyLane, Braket
- ONNX format with quantum metadata extensions
- Import to: Any supported framework

### 4. Pluggable Encoding Strategies

Three core encoding methods compatible with all backends:

| Encoding | Use Case | Complexity |
|----------|----------|------------|
| Amplitude | High-dimensional data | O(n) qubits for n features |
| Angle | Low-dimensional data | O(n) qubits for n features |
| IQP | Classical ML acceleration | Polynomial features |

## Quick Start

### Design a Framework-Agnostic QNN

1. Define circuit in unified graph
2. Select encoding strategy
3. Choose target backends via HAL
4. Export to desired framework

```python
# Example: Iris classification QNN
from framework_agnostic import UnifiedQNN, HAL, Encoding

# Define circuit (framework-independent)
qnn = UnifiedQNN(
    num_qubits=4,
    encoding=Encoding.ANGLE,
    layers=3
)

# Select backends
hal = HAL(['ibm_quantum', 'amazon_braket', 'ionq'])

# Export to specific framework
qiskit_circuit = qnn.export('qiskit')
pennylane_circuit = qnn.export('pennylane')
```

## Workflow: Portability-First QML Design

### Step 1: Define Unified Architecture

Before picking a framework:
- Specify quantum operations abstractly
- Choose encoding compatible with all targets
- Design classical co-processor interface

### Step 2: Configure HAL

Select target backends based on:
- Available hardware (gate-based vs annealing)
- Cost constraints
- Performance requirements

### Step 3: Export & Deploy

Generate framework-specific code:
- Qiskit for IBM Quantum
- PennyLane for gradient-based training
- Cirq for Google ecosystem
- Braket for AWS deployment

### Step 4: Train & Execute

Run in native framework, compare results:
- Verify identical classification accuracy
- Check training time parity (target: <10% overhead)
- Validate cross-framework reproducibility

## Key Design Patterns

### Pattern 1: Vendor-Neutral Circuit Definition

Define gates without framework-specific syntax:

```python
# Instead of qiskit-specific:
# circuit.h(0); circuit.cx(0, 1)

# Use unified representation:
ops = [
    QuantumOp('H', [0]),
    QuantumOp('CNOT', [0, 1]),
    QuantumOp('RX', [0], {'theta': 0.5})
]
```

### Pattern 2: Backend-Aware Cost Estimation

Before execution, estimate cost across backends:

```python
for backend in hal.available_backends():
    cost = hal.estimate_cost(circuit, backend)
    time = hal.estimate_runtime(circuit, backend)
    # Choose optimal backend
```

### Pattern 3: Classical Co-Processor Integration

QML works with classical frameworks (TensorFlow, PyTorch, JAX):

```python
# Hybrid quantum-classical model
model = HybridModel(
    classical_nn=nn.Sequential(...),  # PyTorch
    quantum_layer=UnifiedQNN(...),    # Framework-agnostic
    framework='pytorch'               # Target classical framework
)
```

## Benchmarks (arXiv:2604.04414)

Performance parity across frameworks:

| Task | Native Framework | Framework-Agnostic | Overhead |
|------|------------------|--------------------| ---------|
| Iris classification | Qiskit ML | Unified QNN | 8% |
| Wine classification | PennyLane | Unified QNN | 6% |
| MNIST-4 | TensorFlow Quantum | Unified QNN | 5% |

**Key result**: Identical classification accuracy across frameworks.

## Best Practices

1. **Design first, framework second**: Define circuit before picking implementation
2. **Use ONNX for translation**: Standard metadata format prevents information loss
3. **Test multiple backends**: Verify results match across frameworks
4. **Monitor overhead**: Target <10% overhead from abstraction layer
5. **Choose encoding wisely**: Encoding affects all backends equally

## Common Pitfalls

- **Vendor-specific syntax**: Locks you into one framework
- **Non-portable encoding**: Some encoding methods work only in specific frameworks
- **Ignoring cost**: Different backends have vastly different pricing
- **Backend capabilities mismatch**: Gate-based circuit on annealing hardware fails

## Resources

### references/

See `references/encoding_strategies.md` for detailed encoding implementations and `references/hal_interface.md` for HAL API specification.

### scripts/

See `scripts/export_circuit.py` for circuit translation utility.

---

**Related Skills**: quantum-machine-learning, quantum-circuit-spectral-analysis, variational-quantum-algorithms