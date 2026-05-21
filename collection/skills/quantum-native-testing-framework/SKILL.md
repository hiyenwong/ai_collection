---
name: quantum-native-testing-framework
description: "Native quantum program testing framework using OpenQASM 3 pragma-based assertions. Tests and programs are both standard .qasm files. Provides 12 assertion types (deterministic, statistical, quantum-state, structural), linter, environment-aware mode, and CI integration. Use when: designing quantum test suites, building OpenQASM testing infrastructure, implementing quantum CI/CD, or creating language-native quantum test frameworks. Based on QUTest (arXiv:2605.19736)."
category: quantum
---

# Quantum Native Testing Framework

## Description

Methodology for testing quantum programs **natively** in OpenQASM 3, where both programs and tests are standard `.qasm` files. Tests follow the **Arrange / Act / Assert** pattern with configuration, runtime requirements, and assertions encoded as **pragma comments** (`//%`), preserving full compatibility with existing OpenQASM tools.

**Based on**: "QUTest: A Native Testing Framework for Quantum Programs" (Jos\u00e9 Campos, arXiv:2605.19736v1, 2026-05-19)

## Activation Keywords

- quantum native testing
- openqasm testing framework
- quantum test assertions
- quantum program testing
- qasm test framework
- quantum CI testing
- pragma quantum testing
- 量子测试框架

## Problem Statement

Quantum programs are typically shared as OpenQASM 3 circuits, but tests are written in **host languages** (Python with Qiskit, etc.). This creates a disconnect:
- Tests require knowledge of the host language framework
- Tests cannot be run independently of the host environment
- No standardized assertion language for quantum programs
- CI integration requires custom tooling per framework

## Pragma-Based Test Pattern

### Test File Structure

```qasm
//% test: "Verify Bell state preparation"
//% runtime: qiskit >= 1.0
//% shots: 1024

// === Arrange ===
qubit[2] q;
bit[2] c;

// === Act ===
h q[0];
cx q[0], q[1];

// === Assert ===
//% assert: bell_state(q)
//% assert: correlation(q[0], q[1]) >= 0.95
//% assert: marginal(q[0]) ~ uniform
```

### Key Design Principles

1. **Native format**: Both program and test are `.qasm` files
2. **Pragma encoding**: Tests use `//%` comments, preserving OpenQASM compatibility
3. **Arrange/Act/Assert**: Standard test pattern adapted for quantum
4. **12 assertion types**: Covering deterministic, statistical, state, and structural checks

## 12 Assertion Types

### Deterministic Assertions
| Assertion | Description |
|-----------|-------------|
| `assert: state_is(...)` | Verify exact quantum state vector |
| `assert: output_eq(...)` | Verify exact classical output bits |

### Statistical Assertions
| Assertion | Description |
|-----------|-------------|
| `assert: probability(...)` | Verify measurement probability threshold |
| `assert: distribution_eq(...)` | Compare output distributions (chi-square, KL) |
| `assert: expectation_eq(...)` | Verify expectation value within tolerance |
| `assert: correlation(...)` | Verify qubit correlation coefficient |

### Quantum-State Assertions
| Assertion | Description |
|-----------|-------------|
| `assert: bell_state(...)` | Verify Bell state preparation |
| `assert: ghz_state(...)` | Verify GHZ state preparation |
| `assert: entangled(...)` | Verify entanglement between qubits |

### Structural Assertions
| Assertion | Description |
|-----------|-------------|
| `assert: gate_count(...)` | Verify circuit gate count bounds |
| `assert: depth_le(...)` | Verify circuit depth limit |
| `assert: no_measure_before(...)` | Structural constraint on measurement placement |

## CI/CD Integration Pattern

### CLI Commands
```bash
# Discover and run all tests in directory
qutest run ./quantum_circuits/

# Run tests against specific runtime
qutest run --runtime qiskit --version 1.2 ./tests/

# Generate XML report for CI
qutest run --report xml --output junit.xml ./tests/

# Check runtime compatibility
qutest check ./tests/

# Lint test files
qutest lint ./tests/
```

### CI Pipeline Example
```yaml
# GitHub Actions
- name: Quantum Tests
  run: |
    qutest run ./tests/ --runtime qiskit --report xml
- name: Upload Report
  uses: actions/upload-artifact@v4
  with:
    name: quantum-test-results
    paths: junit.xml
```

## Environment-Aware Testing

Run the same test across multiple runtime versions:
```bash
# Test against multiple backends
qutest run --env-aware ./tests/ --runtimes qiskit,cirq,qulacs

# Isolated environment per runtime
qutest run --isolate ./tests/
```

## Implementation Workflow

### Step 1: Define Test Pragma Language
- Use `//%` prefix for all test directives
- Support test names, runtime specs, assertion types
- Maintain backward compatibility with standard OpenQASM

### Step 2: Implement Assertion Engine
- Parse pragma comments from `.qasm` files
- Map assertions to runtime-specific verification code
- Execute assertions against circuit simulation/hardware results

### Step 3: Build CLI Tool
- Automatic test discovery (find `*.qasm` with `//%` pragmas)
- Runtime compatibility checks
- Report generation (XML/JUnit format)

### Step 4: Integrate with CI
- XML report output for standard CI tools
- Version-specific testing for regression detection
- Linter for pragma syntax validation

## Error Handling

### Runtime Compatibility
```
If test requires runtime not available:
  1. Skip test with warning (not failure)
  2. Report compatibility matrix
  3. Suggest alternative runtimes
```

### Assertion Failure
```
If assertion fails:
  1. Report expected vs actual values
  2. Include statistical significance (p-value)
  3. Show full output distribution for debugging
  4. Classify as: statistical_fluke vs real_failure
```

## Best Practices

1. **Use statistical assertions** for probabilistic circuits (not exact matching)
2. **Specify minimum shot counts** in test pragmas (`//% shots: 1024`)
3. **Test across multiple runtimes** for portability assurance
4. **Include structural assertions** to catch regression in circuit optimization
5. **Use environment-aware mode** to detect runtime-specific bugs
6. **Lint before running** to catch pragma syntax errors early

## Anti-Patterns

| Anti-Pattern | Risk | Fix |
|---|---|---|
| Exact state matching | Fails on real hardware | Use statistical assertions |
| No shot count specified | Inconsistent results | Always specify `//% shots: N` |
| Host-language tests | Framework lock-in | Use native `.qasm` tests |
| Single-runtime testing | Misses compatibility bugs | Test across 2+ runtimes |

## Related Skills

- noise-aware-quantum-testing (mutation testing under hardware noise)
- quanforge-qnn-testing (QNN mutation testing)
- quantum-program-linting (static analysis for quantum code)
- quantum-program-reliability (quantum code quality assurance)

## References

- Campos, J. "QUTest: A Native Testing Framework for Quantum Programs" (arXiv:2605.19736v1, 2026)
- KG entity: `2605.19736v1` in kg.db