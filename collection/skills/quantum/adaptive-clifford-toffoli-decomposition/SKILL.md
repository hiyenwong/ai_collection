---
name: adaptive-clifford-toffoli-decomposition
description: "Adaptive Clifford+T decomposition methodology for large multi-controlled Toffoli gates with minimal ancilla qubits. Use when: optimizing quantum gate decomposition, reducing T-count/T-depth in fault-tolerant circuits, multi-controlled gate synthesis, quantum arithmetic circuit optimization, relative-phase Toffoli decomposition, dynamic circuit compilation."
category: quantum
---

# Adaptive Clifford+Toffoli Decomposition

Adaptive decomposition of large multi-controlled Toffoli gates using one clean ancilla qubit. Based on arXiv:2605.18169.

## Core Concept

Multi-controlled Toffoli gates are expensive in fault-tolerant quantum computing due to T-gate costs. This method adaptively decomposes n-controlled Toffoli gates using only one clean ancilla, optimizing T-count and T-depth.

## Key Techniques

### 1. Decomposition Strategy

- **Single clean ancilla**: Reusable workspace for multi-controlled operations
- **Relative-phase Toffoli gates**: Reduced T-cost by relaxing global phase
- **Dynamic circuit techniques**: Mid-circuit measurement and feed-forward

### 2. Resource Optimization

```
Standard decomposition: T-count = O(n), T-depth = O(log n)
With ancilla + relative-phase: T-count = O(n), T-depth = O(log n)
  but with significantly smaller constants
```

### 3. Adaptive Selection

- Choose decomposition based on:
  - Available ancilla qubits
  - Target T-count budget
  - Circuit depth constraints
  - Hardware connectivity

## Implementation Pattern

```python
# Adaptive Toffoli decomposition
def decompose_toffoli(n_controls, available_ancilla=1, 
                       optimize_for='t-count'):
    """Decompose n-controlled Toffoli gate.
    
    Args:
        n_controls: Number of control qubits
        available_ancilla: Available clean ancilla qubits
        optimize_for: 't-count', 't-depth', or 'balanced'
    
    Returns:
        Circuit with decomposed gates
    """
    if n_controls <= 2:
        return standard_toffoli(n_controls)
    
    if available_ancilla >= 1:
        return ancilla_based_decomposition(
            n_controls, available_ancilla, optimize_for)
    else:
        return no_ancilla_decomposition(n_controls, optimize_for)

def ancilla_based_decomposition(n, ancilla, mode):
    # Use relative-phase Toffoli for reduced cost
    # Cascade decomposition with ancilla reuse
    # Dynamic circuit: measure intermediate results
    pass
```

## When to Use

- Fault-tolerant quantum circuit compilation
- Quantum arithmetic operations (adders, multipliers)
- Quantum oracle construction
- Resource-constrained quantum hardware

## Pitfalls

- Relative-phase gates change global phase — not suitable for all algorithms
- Ancilla qubit must be clean (initialized to |0⟩)
- Dynamic circuits require hardware support for mid-circuit measurement

## Activation
Clifford T decomposition, Toffoli gate optimization, quantum gate synthesis, T-count reduction, multi-controlled gate decomposition, quantum arithmetic circuits
