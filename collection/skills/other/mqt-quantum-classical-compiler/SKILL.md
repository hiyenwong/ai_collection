---
name: mqt-quantum-classical-compiler
description: "MQT Compiler Collection - Future-proof quantum-classical compilation framework built on MLIR. Supports complex optimizations and HPC integration. Activation: quantum compiler, MQT, quantum-classical compilation, MLIR quantum, quantum circuit optimization."
---

# MQT Quantum-Classical Compiler Collection

A blueprint for future-proof quantum-classical compilation framework built on Multi-Level Intermediate Representation (MLIR), supporting full compilation pipeline from high-level algorithms to hardware-specific instructions.

## Overview

As quantum computing hardware capabilities rise, algorithms become increasingly complex, requiring sophisticated compilation frameworks that translate high-level algorithms into executable code.

### Classical-First vs Quantum-First

| Approach | Strengths | Best For |
|----------|-----------|----------|
| Quantum-First | Direct quantum optimization | Pure quantum circuits |
| Classical-First | Handles control flow, HPC integration | Hybrid algorithms, error correction |

MQT Compiler embraces **classical-first** approach using MLIR.

## Core Architecture

### MLIR-Based Design
Built on LLVM's Multi-Level Intermediate Representation:

```
High-Level Algorithm
        ↓
   [Quantum Dialect]
        ↓
   [Circuit Dialect]  
        ↓
   [Hardware Dialect]
        ↓
Hardware Instructions
```

### Key Components

1. **Frontend**: High-level language parsing (QASM, Q#, Python)
2. **IR Optimizer**: Complex optimizations beyond gate cancellation
3. **Backend**: Hardware-specific code generation
4. **HPC Integration**: Classical control flow and HPC environment support

## Activation Keywords

- MQT compiler
- quantum-classical compilation
- MLIR quantum
- quantum compiler framework
- quantum circuit optimization
- quantum compilation pipeline

## Tools Used

- exec: Run compiler commands
- write: Generate IR code
- read: Load quantum programs

## Implementation

### Step 1: Input Parsing
Parse high-level quantum programs:

```python
# QASM input
from mqt import Compiler

compiler = Compiler()
program = compiler.parse_qasm("""
OPENQASM 2.0;
include "qelib1.inc";
qreg q[2];
h q[0];
cx q[0], q[1];
""")
```

### Step 2: MLIR Generation
Convert to MLIR quantum dialect:

```mlir
// Example MLIR quantum IR
func @quantum_circuit(%qubits: !quantum.qubits<2>) -> !quantum.qubits<2> {
  %q0 = quantum.extract %qubits[0]
  %q0_h = quantum.H %q0
  %q1 = quantum.extract %qubits[1]
  %q0_out, %q1_out = quantum.CNOT %q0_h, %q1
  %result = quantum.insert %qubits[0], %q0_out
  %result = quantum.insert %result[1], %q1_out
  return %result
}
```

### Step 3: Optimization Passes
Apply MLIR optimization passes:

```python
# Optimization pipeline
pass_manager = compiler.create_pass_manager()
pass_manager.add_pass("quantum-gate-fusion")
pass_manager.add_pass("quantum-cancellation")
pass_manager.add_pass("classical-control-flow-analysis")
pass_manager.run(program)
```

### Step 4: Hardware Lowering
Lower to hardware-specific instructions:

```python
# Target-specific backend
target = compiler.get_target("ibm_sherbrooke")
executable = compiler.compile(program, target=target)
```

## Advanced Features

### Classical Control Flow Support
Handle structured control flow (conditionals, loops):

```python
# Hybrid quantum-classical program
program = """
def variational_circuit(params):
    for i in range(iterations):
        apply_circuit(params)
        expectation = measure()
        params = optimizer.step(params, expectation)
    return params
"""
compiled = compiler.compile_with_control_flow(program)
```

### Error Correction Integration
Native support for error correction codes:

```python
# Surface code compilation
from mqt import ErrorCorrection

surface_code = ErrorCorrection.SurfaceCode(distance=3)
compiled_ft = compiler.compile_fault_tolerant(circuit, surface_code)
```

### HPC Integration
Seamless integration with high-performance computing:

```python
# MPI-distributed quantum simulation
from mpi4py import MPI

compiler.enable_mpi_distribution(comm=MPI.COMM_WORLD)
compiled = compiler.compile_for_distributed(circuit, num_qubits=30)
```

## Usage Patterns

### Pattern 1: Basic Compilation
```python
from mqt import Compiler

# Compile QASM to IBM backend
compiler = Compiler()
program = compiler.load("circuit.qasm")
optimized = compiler.optimize(program, level=3)
executable = compiler.compile(optimized, target="ibm_sherbrooke")
```

### Pattern 2: Custom Optimization Passes
```python
# Define custom pass
class GateFusionPass(compiler.OptimizationPass):
    def run(self, circuit):
        # Custom fusion logic
        return fused_circuit

compiler.register_pass(GateFusionPass)
compiler.add_pass_to_pipeline("gate-fusion")
```

### Pattern 3: Quantum-Classical Hybrid
```python
# VQE with classical optimization
vqe_program = compiler.parse_python("""
from scipy.optimize import minimize

def vqe_energy(params):
    circuit = build_ansatz(params)
    return execute(circuit).expectation_value()

result = minimize(vqe_energy, x0=initial_params)
""")
compiled = compiler.compile_hybrid(vqe_program)
```

## Configuration

### Optimization Levels

| Level | Passes | Use Case |
|-------|--------|----------|
| 0 | None | Debugging |
| 1 | Basic gate cancellation | Quick compilation |
| 2 | + Gate fusion, scheduling | Balanced |
| 3 | + Advanced pattern matching | Best performance |

### Supported Targets

| Backend | Status | Features |
|---------|--------|----------|
| IBM Quantum | ✓ Complete | Full gate set, dynamic circuits |
| Rigetti | ✓ Complete | Native gates, parametric |
| IonQ | ✓ Complete | Native gates, high fidelity |
| Simulation | ✓ Complete | State vector, tensor network |

## References

- arXiv:2604.08674 - "The MQT Compiler Collection: A Blueprint for a Future-Proof Quantum-Classical Compilation Framework"
- MLIR Documentation - https://mlir.llvm.org/
- Munich Quantum Toolkit - https://github.com/munich-quantum-toolkit/core

## Related Skills

- quantum-circuit-optimization
- quantum-error-correction
- high-performance-computing
- mlir-programming

## Notes

- Open source: https://github.com/munich-quantum-toolkit/core
- Extensible pass system
- Native quantum error correction support
- Designed for future algorithm complexity
- HPC-ready architecture
