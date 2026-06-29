---
name: quantum-mutant-equivalence-tbe
description: "Quantum Mutant Equivalence identification via Transpilation (TBE) — lightweight approach to identify equivalent quantum mutants by transpiling original and mutated circuits under the same configuration and comparing resulting OpenQASM code."
---

# Quantum Mutant Equivalence via Transpilation (TBE)

## Description

Mutation testing evaluates test suite quality by introducing artificial faults (mutants) and checking whether tests detect (kill) them. In quantum software, the **equivalent mutant problem** is severe: roughly half of generated quantum circuit mutants survive tests, but many are semantically identical to the original program. This skill implements **Transpiler-Based Equivalence (TBE)**, a lightweight approach that identifies equivalent quantum mutants by transpiling original and mutated circuits under the same configuration and comparing their resulting OpenQASM code.

From arXiv:2606.26604 (Campos & Miranskyy, 2026): TBE identified 32.1% of surviving mutants as equivalent with 100% precision and 82% accuracy across 348,299 mutants.

## Activation Keywords

- quantum mutant equivalence
- quantum mutation testing
- TBE transpiler equivalence
- equivalent quantum mutant
- quantum program testing
- quantum mutant detection
- OpenQASM comparison
- quantum software defect

## Core Concepts

### The Equivalent Mutant Problem

In quantum software mutation testing, mutants are created by applying mutation operators (gate replacement, gate deletion, parameter perturbation) to quantum circuits. A mutant is **equivalent** if it produces identical quantum state transformations despite syntactic differences. Equivalent mutants cannot be killed by any test and waste testing resources.

### Why Transpilation Works

Quantum circuit transpilers (Qiskit's `transpile`, etc.) apply optimization passes that:
1. Canonicalize gate sequences
2. Remove redundant operations
3. Normalize equivalent gate compositions
4. Produce a standardized output representation

If original and mutated circuits produce identical transpiled OpenQASM, they are **provably equivalent** for that transpiler configuration.

### TBE Methodology

```
Original Circuit ──→ Transpile ──→ OpenQASM_A ──→ Compare ──→ EQUIVALENT?
Mutated Circuit  ──→ Transpile ──→ OpenQASM_B ──→ Compare ──→ (Yes/No)
```

**Key insight**: Use the same transpiler configuration for both circuits to ensure fair comparison.

## Usage Patterns

### Pattern 1: Identify Equivalent Mutants in a Quantum Test Suite

When you have a set of surviving quantum mutants and need to filter out equivalent ones:

```python
from qiskit import transpile
from qiskit.circuit import QuantumCircuit

def is_equivalent_mutant(original: QuantumCircuit, mutant: QuantumCircuit,
                         optimization_level: int = 3, basis_gates: list = None) -> bool:
    """Check if a quantum mutant is equivalent to the original via TBE."""
    transpile_kwargs = {
        'optimization_level': optimization_level,
    }
    if basis_gates:
        transpile_kwargs['basis_gates'] = basis_gates

    qasm_orig = transpile(original, **transpile_kwargs).qasm()
    qasm_mutant = transpile(mutant, **transpile_kwargs).qasm()

    return qasm_orig == qasm_mutant
```

### Pattern 2: Batch Screening of Surviving Mutants

For large mutant sets (100K+), use parallel transpilation:

```python
from concurrent.futures import ThreadPoolExecutor
from functools import partial

def screen_mutants(original: QuantumCircuit, mutants: list,
                   workers: int = 8) -> dict:
    """Screen mutants for equivalence. Returns {equivalent: [...], non_equivalent: [...]}."""
    check = partial(is_equivalent_mutant, original)

    with ThreadPoolExecutor(max_workers=workers) as executor:
        results = list(executor.map(check, mutants))

    return {
        'equivalent': [m for m, eq in zip(mutants, results) if eq],
        'non_equivalent': [m for m, eq in zip(mutants, results) if not eq]
    }
```

### Pattern 3: Multi-Configuration TBE

Use multiple transpiler configurations to increase recall:

```python
def multi_config_tbe(original: QuantumCircuit, mutant: QuantumCircuit) -> bool:
    """Check equivalence across multiple transpiler configs.
    Returns True if ANY config shows equivalence."""
    configs = [
        {'optimization_level': 0},
        {'optimization_level': 1},
        {'optimization_level': 2},
        {'optimization_level': 3},
        {'optimization_level': 3, 'basis_gates': ['u1', 'u2', 'u3', 'cx']},
    ]
    for cfg in configs:
        if is_equivalent_mutant(original, mutant, **cfg):
            return True
    return False
```

## Instructions for Agents

### Step 1: Gather Mutant Set
- Obtain the set of surviving mutants from the quantum mutation testing pipeline
- Each mutant should be a Qiskit `QuantumCircuit` or equivalent representation
- Note the mutation operator applied (gate type, position, etc.)

### Step 2: Configure Transpiler
- Use the same transpiler configuration for original and mutant
- Start with `optimization_level=3` (most aggressive normalization)
- Optionally specify `basis_gates` to match target hardware

### Step 3: Execute TBE Check
- Transpile both circuits
- Compare the resulting OpenQASM strings
- If identical → mutant is equivalent (can be discarded)
- If different → mutant is potentially killable (keep for further testing)

### Step 4: Report Results
- Report the fraction of surviving mutants identified as equivalent
- TBE typically identifies ~32% of surviving mutants as equivalent
- Remaining non-equivalent mutants represent genuine test gaps

## Error Handling

### Transpiler Configuration Mismatch
**Problem**: Different configs produce different canonicalizations.
**Fix**: Always use identical configuration for both circuits.

### Large Circuit Timeout
**Problem**: Transpilation of large circuits (>50 qubits) can be slow.
**Fix**: Use `optimization_level=1` for initial screening, level=3 for borderline cases.

### False Negatives
**Problem**: TBE may not detect all equivalent mutants (recall ~32%).
**Fix**: Combine TBE with other equivalence detection methods (simulation-based comparison, symbolic equivalence checking) for comprehensive screening.

## References

- arXiv:2606.26604 — "Quantum Mutant Equivalence via Transpilation" (Campos & Miranskyy, 2026)
- Qiskit Transpiler documentation: https://docs.quantum.ibm.com/api/qiskit/transpiler
- Mutation testing for quantum programs: Bugs4Q dataset
