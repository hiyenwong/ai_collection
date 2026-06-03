---
name: quantum-native-testing-framework
category: quantum-computing
description: Native quantum program testing framework using OpenQASM 3 with pragma-based assertions, covering deterministic, statistical, and property-based testing patterns. Based on QUTest (arXiv:2605.19736).
version: 1.0
created: 2026-05-26
source_paper: arXiv:2605.19736
activation: quantum testing, qutest, openqasm, pragma assertions, quantum verification, quantum debugging
---

# Quantum Native Testing Framework (QUTest)

## Overview

QUTest is a native testing framework for quantum programs where both programs and tests are standard `.qasm` files. Tests follow the **Arrange / Act / Assert** pattern, with configuration, runtime requirements, and assertions encoded as pragma comments (`//%`), preserving compatibility with existing OpenQASM tools.

## Core Architecture

### 1. Pragma-Based Assertion System
- Tests encoded as `//%` pragma comments in `.qasm` files
- 12 assertion types spanning deterministic, statistical, and property-based checks
- Configuration and runtime requirements encoded inline

### 2. Test Structure (Arrange / Act / Assert)
```
//% test: state_verification
//% shots: 1000
//% backend: simulator

// Arrange: prepare circuit
qubit q[2];
H q[0];
CX q[0], q[1];

// Act: measure
measure q -> c;

// Assert: verify entanglement
//% assert: bell_state_correlation
//% threshold: 0.95
```

### 3. Assertion Types
1. **Deterministic**: Exact state verification for small circuits
2. **Statistical**: Distribution-based checks with configurable confidence intervals
3. **Property-based**: Invariant verification across multiple executions
4. **Budget-aware**: Adaptive testing that stops when confidence threshold is met

## Implementation Patterns

### Pattern 1: Native Test Files
- Store tests as `.qasm` files alongside quantum programs
- Use pragma comments for test metadata
- Run tests with QUTest CLI or integrate into CI/CD pipelines

### Pattern 2: Statistical Verification
- Use sequential hypothesis testing to reduce shot budgets
- Apply Bayesian methods for probabilistic assertions
- Set confidence thresholds (e.g., 95%) for pass/fail decisions

### Pattern 3: Cross-Backend Testing
- Test on simulators first, then validate on real hardware
- Use noise-aware assertions that account for device-specific errors
- Implement tolerance bands for hardware noise

## Workflow

1. Write quantum circuit in OpenQASM 3
2. Add test pragmas (`//%`) inline or in separate test files
3. Run QUTest with target backend (simulator or real device)
4. Review assertion results with statistical confidence scores
5. Iterate on circuit design based on test failures

## Key Advantages

- **No host language dependency**: Tests are pure `.qasm`, not Python/Qiskit
- **Tool compatibility**: Pragma comments are ignored by standard OpenQASM parsers
- **Statistical rigor**: Built-in support for probabilistic verification
- **CI/CD ready**: Can be integrated into automated testing pipelines
- **Budget optimization**: Adaptive testing reduces unnecessary shot consumption

## Related Concepts

- Bayesian sequential verification (arXiv:2605.15601)
- OpenQASM 3 specification
- Quantum program verification
- Statistical hypothesis testing
