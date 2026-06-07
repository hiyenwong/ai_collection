---
name: quantum-program-linting
description: >
  LLM-powered static analysis and linting for quantum programs. Use when:
  (1) analyzing quantum circuits for correctness and optimization opportunities,
  (2) detecting anti-patterns in quantum code (Qiskit, Cirq, Pennylane),
  (3) improving quantum program quality through automated review,
  (4) validating quantum algorithms before execution on hardware.
  Covers LLM-based linting rules, quantum circuit analysis, and best practices
  for quantum software engineering.
category: devops
---

# Quantum Program Linting

## Description
LLM-powered linting methodology for quantum programs that goes beyond traditional
static analysis. Quantum programs have unique characteristics (entanglement,
superposition, measurement) that make conventional linting inadequate.

## Activation Keywords
- quantum program linting
- quantum code analysis
- quantum static analysis
- quantum code review
- linting quantum circuits
- 量子程序分析
- quantum software quality

## Problem Statement

Traditional static analysis for quantum programs is inadequate because:
1. **Quantum-specific semantics**: Entanglement, measurement collapse, no-cloning
2. **Hardware constraints**: Qubit connectivity, gate fidelity, circuit depth limits
3. **Algorithmic correctness**: Phase estimation, amplitude amplification patterns
4. **Optimization opportunities**: Gate decomposition, circuit compression, qubit reuse

## LLM-Based Linting Approach

### Step 1: Parse Quantum Program
- Extract circuit structure from Qiskit/Cirq/Pennylane code
- Identify quantum operations: gates, measurements, resets
- Map qubit usage and entanglement patterns

### Step 2: Apply Linting Rules (LLM-Powered)

#### Correctness Rules
| Rule | Description | Severity |
|------|-------------|----------|
| UNMEASURED_QUBIT | Qubit used but never measured | Warning |
| UNUSED_QUBIT | Qubit allocated but never used | Info |
| MID_CIRCUIT_MEASURE | Measurement followed by quantum ops | Warning |
| NO_CLONING_VIOLATION | Attempted qubit cloning | Error |

#### Optimization Rules
| Rule | Description | Severity |
|------|-------------|----------|
| REDUNDANT_GATE | Self-inverse gate applied twice consecutively | Warning |
| DEEP_CIRCUIT | Circuit depth exceeds hardware limits | Warning |
| INEFFICIENT_ENCODING | Suboptimal state preparation | Info |
| MISSING_COMPILATION | No transpilation for target backend | Warning |

#### Best Practice Rules
| Rule | Description | Severity |
|------|-------------|----------|
| NO_ERROR_MITIGATION | Missing error mitigation for NISQ | Info |
| BARRIER_MISUSE | Overuse or misuse of barriers | Info |
| MISSING_DOCSTRING | No documentation for quantum algorithm | Warning |

### Step 3: Generate Report
- List violations with severity and suggested fixes
- Provide circuit metrics: depth, width, gate count, entanglement depth
- Compare against hardware constraints if target backend specified

## Integration Patterns

### Pre-commit Hook
```bash
# Add to .pre-commit-config.yaml
- repo: local
  hooks:
    - id: quantum-lint
      name: quantum-lint
      entry: python scripts/quantum_lint.py
      types: [python]
      files: '.*quantum.*\.py$'
```

### CI/CD Pipeline
- Run quantum lint on all PRs with quantum code changes
- Fail on errors, warn on optimization suggestions
- Track circuit complexity trends over time

### IDE Integration
- Real-time linting as quantum code is written
- Quick-fix suggestions for common issues
- Circuit visualization with highlighted problem areas

## Key Research

### Paper: "Beyond Rules: LLM-Powered Linting for Quantum Programs" (2026-05-05)
- Traditional static analysis techniques are increasingly inadequate for quantum programs
- LLMs can understand quantum semantics and provide context-aware suggestions
- Combines rule-based checks with LLM reasoning for comprehensive analysis

## Common Quantum Anti-Patterns

### 1. Excessive Circuit Depth
```python
# Bad: Unoptimized circuit
for i in range(n_qubits):
    for j in range(n_qubits):
        qc.cz(i, j)  # O(n²) depth

# Good: Optimized with parallelism
for i in range(0, n_qubits, 2):
    qc.cz(i, i+1)  # O(n) depth with parallel gates
```

### 2. Missing Error Mitigation
```python
# Bad: No error mitigation for NISQ device
result = backend.run(circuit).result()

# Good: Add error mitigation
from qiskit.primitives import Estimator
estimator = Estimator(options={"resilience_level": 1})
result = estimator.run(circuit).result()
```

### 3. Qubit Allocation Without Connectivity
```python
# Bad: Assumes all-to-all connectivity
qc.cx(0, 7)  # May require many SWAP gates on real hardware

# Good: Transpile for target backend
from qiskit.transpiler import transpile
qc_transpiled = transpile(qc, backend=real_device)
```

## Metrics to Track

| Metric | Description | Good Threshold |
|--------|-------------|----------------|
| Circuit Depth | Number of sequential gate layers | < 100 for NISQ |
| Circuit Width | Number of qubits used | < device qubit count |
| Two-Qubit Gate Count | Gates prone to errors | Minimize |
| Entanglement Depth | Max entanglement chain length | Track for complexity |

## Related Skills
- quantum-system-engineering
- quantum-program-analysis
- beyond-rules-quantum-linting