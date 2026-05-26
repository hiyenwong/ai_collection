---
name: qutest-quantum-testing
category: quantum
version: "1.0"
description: QUTest native testing framework for quantum programs - testing quantum circuits using pure .qasm files with pragma-based assertions, following Arrange/Act/Assert pattern
tags: [quantum-testing, openqasm, ci-cd, test-automation, quantum-programming, quality-assurance]
created: "2026-05-26"
source: "arxiv.org/abs/2605.19736"
activation: "qutest, quantum-native-testing, openqasm-testing, quantum-ci, qasm-test-framework"
---

# QUTest: Native Testing Framework for Quantum Programs

> Based on: José Campos. "QUTest: A Native Testing Framework for Quantum Programs" (arXiv:2605.19736, May 2026)

## Overview

QUTest enables quantum program testing using pure .qasm files, eliminating the need for host-language test frameworks. Tests follow the Arrange/Act/Assert pattern with pragma-based configuration.

## Problem Statement

Quantum programs are typically shared as OpenQASM 3 circuits, but tests are written in host languages (Python/Qiskit), creating:
- Language mismatch between program and tests
- Dependency on specific SDK versions
- Complex test setup for simple quantum assertions

## QUTest Architecture

### Pragma Language
Tests are encoded as pragma comments (`//%`) in standard .qasm files:
- `//% config:` - Runtime configuration
- `//% require:` - Runtime requirements (backend, version)
- `//% assert:` - Test assertions

### Arrange/Act/Assert Pattern
```
// Arrange: Prepare quantum state
// Act: Execute quantum circuit
// Assert: Verify expected outcomes
```

### 12 Assertion Types
- **Deterministic**: Exact state verification
- **Statistical**: Probability distribution checks
- **Quantum-state**: State vector and density matrix validation
- **Structural**: Circuit structure verification (gate count, depth, connectivity)

## Key Features

1. **Pure QASM Testing**: Both programs and tests are .qasm files
2. **Pragma-based Config**: `//%` comments for test metadata
3. **Environment-aware Mode**: Run same test across runtime versions
4. **CLI Tool**: Automatic test discovery, compatibility checks, XML reports
5. **CI Integration**: XML reports for continuous integration pipelines
6. **Linter**: Static analysis of quantum test files

## Implementation Steps

1. Write quantum program as standard .qasm file
2. Add test cases as .qasm files with pragma annotations
3. Run QUTest CLI: `qutest run <directory>`
4. Review XML reports for CI integration
5. Use environment-aware mode for cross-version validation

## When to Use

- Testing OpenQASM 3 quantum circuits
- Quantum CI/CD pipeline setup
- Cross-platform quantum program validation
- Statistical verification of quantum programs

## Pitfalls

- Limited to OpenQASM 3 compatible backends
- Statistical assertions require sufficient shot counts
- Complex assertions may need custom pragma extensions
- Not suitable for pulse-level testing

## Related Skills

- `quantum-program-linting` - Quantum program static analysis
- `quantum-program-analysis` - LLM-powered quantum QA
- `quantum-native-testing-framework` - Native quantum testing
