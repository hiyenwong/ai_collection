---
name: iceberg-error-detection
description: "Fault-tolerant error detection using the Iceberg [[2m, 2m-2, 2]] quantum error-detecting code. Implements beyond-break-even error detection for multi-qubit gates on trapped-ion quantum computers. Keywords: quantum error detection, Iceberg code, fault-tolerant, trapped-ion, multi-qubit gates, Toffoli, Bell state, error correction."
---

# Iceberg Error Detection Code

Fault-tolerant implementation of the Iceberg [[2m, 2m-2, 2]] quantum error-detecting code achieving beyond-break-even error detection.

## Core Concepts

### Iceberg Code Properties
- **Parameters**: [[2m, 2m-2, 2]]
- **Code Distance**: 2 (detects single errors)
- **Fault Tolerance**: Fully fault-tolerant implementation
- **Performance**: Beyond-break-even error detection

### Key Innovation
- **Beyond-break-even**: Encoded circuit has higher fidelity than unencoded
- **Error Detection**: Filter out runs with errors
- **Applicability**: Small-scale circuits with substantial error-free runs

## Technical Specifications

### Hardware Platform
- **System**: Leading trapped-ion quantum computer
- **Gates Supported**: Toffoli, Bell state preparation

### Performance
- **Fidelity Gain**: Increased compared to unencoded circuit
- **Error Detection**: Effective filtering of erroneous runs
- **Implementation**: Both fault-tolerant and lean non-fault-tolerant variants

## Implementation

### Fault-Tolerant Implementation
Applied to Toffoli circuit with full fault tolerance

### Lean Implementation
Applied to Bell state preparation with reduced overhead

### Circuit Compilation
- Hardware-aware compilation essential
- Code-specific optimization required

## Workflow

### Step 1: Circuit Encoding
Encode logical circuit with Iceberg code

### Step 2: Execution
Run encoded circuit on hardware

### Step 3: Error Detection
Detect errors in output

### Step 4: Postselection
Keep only error-free runs

### Step 5: Result Extraction
Decode logical result from valid runs

## Applications

### Multi-Qubit Gates
- Toffoli gate implementation
- Controlled operations
- Logical gate synthesis

### State Preparation
- Bell state preparation
- Entangled state generation
- Logical state initialization

## Key Insights

### Error Detection Strategy
For small-scale circuits with many error-free runs:
- Error detection can be more effective than correction
- Simple filtering achieves fidelity gains
- Overhead vs benefit trade-off favorable

### Compilation Importance
- Code compilation must consider hardware constraints
- Joint optimization of code and hardware

## References

- **Paper**: arXiv:2604.13219 - "Fault-Tolerant Error Detection Above Break-Even for Multi-Qubit Gates"
- **Category**: Quantum Error Correction

## Related Skills

- quantum-error-correction
- trapped-ion-quantum-computing
- quantum-circuit-compilation
