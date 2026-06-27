---
name: quantum-group-codes-non-clifford
description: "Quantum group codes methodology for non-Clifford logic with enhanced decoding, addressability and parallelizability"
category: quantum-error-correction
arxiv_id: "2606.27211"
trigger_words: ["quantum group codes", "non-Clifford gates", "transversal gates", "magic state distillation", "quasi group codes", "AG codes", "multi-control-Z gates", "quantum CSS codes"]
date_created: "2026-06-29"
---

# Quantum Group Codes for Non-Clifford Logic

## Overview

A framework based on **classical quasi group codes** to define quantum CSS codes that support **transversal multi-control-Z gates** which are both **addressable** and **parallelizable**, enabling efficient implementation of non-Clifford gate circuits at the logical level. Uses a lifting procedure from classical algebraic geometry (AG) codes to achieve **quasi-quadratic time decoding** — an almost linear speedup over previous cubic-time decoders.

**arXiv**: 2606.27211 (June 2026)
**Authors**: Jean Gasnier, Virgile Guémard

## Core Methodology

### 1. Quantum Group Code Construction

```
Classical quasi group code over F_q
         ↓ (lifting procedure from class field theory)
Quantum group code over F_{q²}
         ↓
CSS code with transversal C^m Z gates
```

### 2. Key Properties

| Property | Quantum Group Codes | Previous Quantum AG Codes |
|----------|-------------------|------------------------|
| Transversal gates | C^m Z (addressable + parallelizable) | Limited gate support |
| Decoding complexity | O(n² log n) quasi-quadratic | O(n³) cubic |
| Decoding radius | Linear in code distance | Sublinear |
| Gate parallelizability | Full parallel C^{m-1}Z | Limited |

### 3. Lifting Procedure

The lifting maps a good quantum AG code over F_q to a quantum group code over F_{q²}:

1. **Input**: Quantum AG code with transversal C^m Z gate over F_q
2. **Lift**: Apply class field theory lifting to underlying classical AG code
3. **Output**: Quantum group code over F_{q²} supporting:
   - Transversal C^m Z gate
   - Addressable and parallelizable C^{m-1}Z gates
   - Quasi-quadratic time decoder

### 4. Decoding Algorithm

```python
def decode_quantum_group_code(syndrome, code_params):
    """
    Quasi-quadratic time decoder for quantum group codes
    
    syndrome: measured error syndrome
    code_params: (n, k, d, q) code parameters
    
    Returns: estimated error pattern
    Complexity: O(n² log n) vs O(n³) for AG codes
    """
    # Step 1: Syndrome decomposition using group structure
    syndrome_groups = decompose_by_group_structure(syndrome)
    
    # Step 2: Quasi-quadratic decoding per group
    # Leverages algebraic geometry code structure
    errors = []
    for group in syndrome_groups:
        error = decode_group_efficiently(group, code_params)
        errors.append(error)
    
    # Step 3: Combine and verify
    return combine_and_verify(errors)
```

## Implementation Steps

### Step 1: Construct Base AG Code

- Start with a good classical AG code over F_q
- Ensure it supports the desired transversal gate level
- Parameters: rate R, distance d, alphabet size q

### Step 2: Apply Lifting

```python
def lift_to_quantum_group_code(base_ag_code):
    """Lift classical AG code to quantum group code"""
    # Apply class field theory lifting
    lifted_code = class_field_lift(base_ag_code)
    
    # Construct CSS code from lifted classical codes
    css_code = construct_css(lifted_code)
    
    # Verify transversal gate support
    assert supports_transversal_gate(css_code, 'C^m Z')
    
    return css_code
```

### Step 3: Implement Transversal Gates

- **C^m Z gates**: Apply transversally (physical gate on each qubit)
- **Addressability**: Individual logical qubits can be targeted
- **Parallelizability**: Multiple gates can be executed simultaneously

### Step 4: Decode with Quasi-Quadratic Complexity

- Use the group structure for efficient syndrome decoding
- Achieve O(n² log n) vs O(n³) for traditional AG code decoders
- Linear decoding radius ensures good error correction capability

## Impact on Magic State Distillation

The quasi-quadratic decoder directly reduces the **time complexity** of magic state distillation protocols:

$$T_{\text{new}} \approx \frac{T_{\text{old}}}{n} \quad \text{(almost linear speedup)}$$

This is significant because magic state distillation is the primary bottleneck for fault-tolerant non-Clifford gate implementation.

## Key Insights

1. **Group structure is key**: The algebraic group structure of the code enables both parallelizable gates and efficient decoding

2. **Class field theory connection**: Deep mathematical connection between algebraic geometry codes and quantum error correction

3. **Decoding speedup**: Quasi-quadratic vs cubic is a practically significant improvement for large codes

4. **Gate addressability**: Being able to target individual logical qubits while maintaining parallelism is crucial for practical quantum computing

## Applications

- **Fault-tolerant quantum computing**: Efficient non-Clifford gate implementation
- **Magic state distillation**: Faster distillation protocols
- **Quantum circuit compilation**: Parallelizable gate execution
- **Large-scale QEC**: Scalable decoding for large code distances

## Activation

Use this skill when:
- Designing quantum error correcting codes for non-Clifford gates
- Optimizing magic state distillation protocols
- Studying transversal gate implementations
- Analyzing quantum code decoding complexity
- Working with algebraic geometry codes in quantum context
- Building fault-tolerant quantum circuits

## References

- Gasnier, J., Guémard, V. "Quantum group codes for non-Clifford logic: enhanced decoding, addressability and parallelizability" arXiv:2606.27211 (2026)
