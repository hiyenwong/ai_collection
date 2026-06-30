# Quantum Software Testing and Mutant Equivalence

**Topic**: Computer Science + Quantum Software Engineering (Testing)
**arXiv**: 2606.26604v1
**Title**: "Quantum Mutant Equivalence via Transpilation"

## Overview

Methodology for identifying equivalent mutants in quantum software testing using transpilation-based circuit comparison. Addresses the core challenge in quantum mutation testing where syntactically different quantum circuits may be semantically identical.

## Core Methodology

### 1. Quantum Mutant Generation

Generate mutants by applying transformation operators:
- **Gate substitution**: Replace gate G with G' (e.g., H → X)
- **Gate deletion**: Remove a gate
- **Gate insertion**: Add extra gate
- **Parameter mutation**: Change rotation angle
- **Qubit swap**: Exchange qubit assignments

### 2. Transpilation-Based Equivalence Detection

Key insight: Two quantum circuits are equivalent if they compile to the same circuit (up to known equivalences):

```
Original Circuit → Transpile → Normalized Circuit A
Mutant Circuit   → Transpile → Normalized Circuit B
Compare A and B using circuit equivalence checker
```

### 3. Equivalence Detection Pipeline

```python
def check_mutant_equivalence(original_circuit, mutant_circuit):
    # Step 1: Transpile both to same basis gates
    basis_gates = ['u3', 'cx']
    orig_norm = transpile(original_circuit, basis_gates=basis_gates, optimization_level=3)
    mut_norm  = transpile(mutant_circuit, basis_gates=basis_gates, optimization_level=3)
    
    # Step 2: Compare normalized circuits
    # Exact comparison
    if circuits_equal(orig_norm, mut_norm):
        return EQUIVALENT
    
    # Step 3: Unitary comparison (expensive but definitive)
    U_orig = Operator(orig_norm).data
    U_mut  = Operator(mut_norm).data
    if np.allclose(U_orig, U_mut, atol=1e-10):
        return EQUIVALENT
    
    return NOT_EQUIVALENT
```

### 4. Equivalence Categories

| Category | Description | Detection Method |
|----------|-------------|------------------|
| **Exact equivalent** | Same unitary transformation | Circuit comparison |
| **Global phase equivalent** | Same up to global phase | Unitary comparison with phase |
| **Redundant gate** | Gates that cancel out | Transpilation optimization |
| **Commuted gate** | Order doesn't matter due to commutation | Dependency analysis |
| **Decomposition equivalent** | Different gate decompositions | Unitary comparison |

### 5. Test Suite Quality Metrics

- **Mutation Score**: Killed mutants / (Total mutants - Equivalent mutants)
- **Equivalent Rate**: Equivalent mutants / Total mutants (should decrease with better detection)
- **Detection Coverage**: Fraction of non-trivial mutants detected

## Practical Guidelines

### When Transpilation-Based Detection Works Best
1. **Small circuits** (< 20 qubits) where full unitary comparison is feasible
2. **Clifford circuits** where equivalence can be decided efficiently
3. **Gate-level testing** where mutants are simple gate modifications

### Limitations and Workarounds
1. **Large circuits**: Use sampling-based comparison (run both circuits on random inputs)
2. **Noisy hardware**: Use statistical comparison with sufficient shots
3. **Dynamic circuits**: Analyze control flow equivalence separately

## Skill Application

**Use when**: Building or evaluating test suites for quantum software, implementing mutation testing for quantum programs, or assessing quantum code quality.

**Activation**: quantum testing, mutation testing, quantum mutant equivalence, quantum circuit comparison, quantum test suite quality, quantum software quality

## Key References

- arXiv:2606.26604v1 - "Quantum Mutant Equivalence via Transpilation"
