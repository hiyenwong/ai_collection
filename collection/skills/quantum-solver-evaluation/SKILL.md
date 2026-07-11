---
name: quantum-solver-evaluation
description: >
  Quantum solver evaluation and quantum neural network assessment methodology.
  Covers Q-SAGE iterative quantum solver generation evaluation, equivariant RL
  for Clifford circuit synthesis, photonic QNN algorithmic advantage assessment,
  LUNA LUT-based qubit readout, and CliNR mid-circuit noise reduction.
  Use when: evaluating LLM-generated quantum code, synthesizing quantum circuits
  with RL, benchmarking QNNs vs ANNs, designing low-latency qubit readout,
  or reducing noise in Hamiltonian simulations.
  Keywords: quantum solver evaluation, Q-SAGE, equivariant RL quantum, Clifford synthesis,
  photonic QNN, LUNA qubit readout, CliNR, mid-circuit measurement, quantum noise reduction,
  量子求解器评估, 量子神经网络评估
---

# Quantum Solver Evaluation & QNN Assessment

## Overview

Patterns from 5 arXiv papers (May 2026) for evaluating, synthesizing, and deploying quantum solvers and quantum neural networks.

## Pattern 1: Iterative Quantum Solver Evaluation (Q-SAGE)

**Source**: arXiv:2605.07525

When LLMs generate quantum solvers, success ≠ execution. Correctness requires numerical accuracy.

```python
def q_sage_evaluate(llm, problem, classical_solver, tolerance=1e-6):
    """Iterative quantum solver evaluation methodology."""
    script = llm.generate_quantum_solver(problem)
    for iteration in range(max_iters):
        result = execute_script(script)
        reference = classical_solver.solve(problem)
        if matches(result, reference, tolerance):
            return {"status": "pass", "iterations": iteration + 1}
        feedback = build_feedback(result, reference)
        script = llm.refine(script, feedback)
    return {"status": "fail", "iterations": max_iters}
```

**Key insight**: As model capability increases, failures shift from execution errors to numerical inaccuracies.

## Pattern 2: Equivariant RL for Clifford Circuit Synthesis

**Source**: arXiv:2605.10910

Formulate circuit synthesis as RL: agent learns gate sequences reducing symplectic matrix to identity.

- **Size-agnostic policy**: single model works across different qubit counts (6→30 qubits)
- **Equivariant architecture**: invariant to qubit relabelings
- **Training**: random walks from identity create curriculum
- **Results**: 99.2% optimal circuits, milliseconds per instance (6-qubit)

## Pattern 3: QNN Algorithmic Advantage Assessment

**Source**: arXiv:2605.10801

Compare QNN vs ANN using effective dimension (capacity measure from generalization-error bound):

| Metric | QNN | Matched ANN |
|--------|-----|-------------|
| XOR (2 params) | 100% accuracy | Random-guessing |
| Iris subset | Converged loss 0.04 | Failed |
| Parameters needed | 2 | ≥8 (4×) |

**Assessment protocol**:
1. Compute effective dimension for both architectures
2. Benchmark on same classification tasks
3. Measure converged cross-entropy loss and accuracy
4. Test robustness under realistic noise (photon loss, phase errors)

## Pattern 4: LUNA — LUT-Based Qubit Readout

**Source**: arXiv:2512.07808

Ultra-low-latency qubit readout using LogicNets (DNNs → LUT logic):

1. **Integrator preprocessing**: dimensionality reduction, minimal hardware
2. **LogicNets classification**: DNN synthesized into FPGA LUT logic
3. **Differential evolution**: automated design point optimization

Results: 10.95× area reduction, 30% lower latency, same fidelity.

## Pattern 5: CliNR — Mid-Circuit Noise Reduction

**Source**: arXiv:2605.06792

Combine encoding + mid-circuit measurement for noise reduction without full QEC:

1. Encode in Generalized Superfast Encoding (GSE)
2. Apply symplectic-transvection Trotter synthesis
3. Use Clifford Noise Reduction (CliNR)
4. Mid-circuit stabilizer verification (Shor-style)
5. ML-guided stabilizer selection > random choice

Result: 54% lower logical error rate. Advantage disappears if stabilizer readout deferred to end.

## Decision Table

| Goal | Pattern | Hardware |
|------|---------|----------|
| Evaluate LLM quantum code | Q-SAGE iterative eval | Any simulator |
| Synthesize Clifford circuits | Equivariant RL | All-to-all connectivity |
| Benchmark QNN vs ANN | Effective dimension + cross-entropy | Photonic/Superconducting |
| Fast qubit readout | LUNA LUT architecture | FPGA + Superconducting |
| Reduce simulation noise | CliNR + mid-circuit | Trapped ion |

## Best Practices

- Always verify numerical accuracy, not just execution success (Q-SAGE)
- Use equivariant architectures for size-generalization in quantum RL
- Use effective dimension, not just accuracy, to compare QNN/ANN capacity
- Defer stabilizer readout kills CliNR advantage — mid-circuit timing is critical
- ML-guided stabilizer selection outperforms random choices

## References

- kg.db entities: imported via 2026-05-12 cron (arXiv: 2605.07525, 2605.10910, 2605.10801, 2512.07808, 2605.06792)
