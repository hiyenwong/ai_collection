---
name: rubriq-grpo-quantum-circuit-synthesis
description: >
  Rubric-Guided GRPO for Constraint-Aware Quantum Circuit Synthesis. LLM-based
  quantum circuit generation optimized via Group Relative Policy Optimization
  with domain-grounded programmatic rubrics for T-gate reduction, hardware
  topology compliance, and unitary fidelity. Use when: synthesizing fault-tolerant
  quantum circuits, optimizing T-gate counts, generating hardware-compatible
  circuits, RL-based quantum compilation, LLM-guided quantum code generation,
  or constraint-aware quantum circuit design.
  arXiv: 2607.07554v1
---

# RubriQ: GRPO-Guided Quantum Circuit Synthesis

## Core Concept

Formulate fault-tolerant quantum circuit synthesis as an LLM code-generation task, optimized via Group Relative Policy Optimization (GRPO) with a domain-grounded programmatic rubric as the reward function.

## Key Findings (arXiv: 2607.07554v1)

- **3.31x T-gate compression** vs 2.05x sparse-reward RL baselines
- **2-3x faster convergence** than conventional approaches
- **<1% hardware-constraint violations** on IBM and IonQ processors
- Deployed on NERSC Perlmutter using DeepSpeed ZeRO2 across multinode A100 clusters

## Architecture

1. **LLM Generator**: Generates circuit code (OpenQASM/native format)
2. **Programmatic Rubric**: Domain-grounded reward evaluating:
   - T-gate reduction
   - Hardware topology compliance
   - Unitary fidelity
3. **GRPO Optimizer**: Group relative policy optimization with GPU-accelerated CUDA-Q simulation
4. **Feedback Loop**: Reward → policy update → next generation

## Reward Function Design

```
reward = w1 * t_gate_reduction + w2 * topology_compliance + w3 * unitary_fidelity
```

- Replace black-box neural critics with interpretable, domain-grounded rubrics
- Each rubric component is independently verifiable
- Weight tuning per hardware target

## Workflow

1. Define target circuit + hardware constraints (topology, native gates)
2. Initialize LLM policy with quantum circuit examples
3. Generate circuit candidates in groups (size = GRPO group size)
4. Evaluate each candidate against programmatic rubric
5. Compute GRPO advantage within group, update policy
6. Validate on simulator (CUDA-Q), then hardware

## Pitfalls

- Sparse-reward baselines converge slower (2-3x) and achieve lower compression
- Hardware constraint violations must be <1% for production readiness
- CUDA-Q integration requires GPU cluster for high-throughput training
- Unitary fidelity check is computationally expensive for large circuits

## Activation Keywords

- rubriq, GRPO quantum, T-gate synthesis, quantum circuit optimization, constraint-aware compilation, fault-tolerant circuit generation, LLM quantum code
