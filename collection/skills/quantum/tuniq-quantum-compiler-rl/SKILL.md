---
name: tuniq-quantum-compiler-rl
description: >
  RL-based autotuning compilation for quantum workloads. Use when optimizing quantum circuit
  compilation passes for fidelity and efficiency, selecting compilation passes dynamically,
  adapting to circuit structure and backend noise profiles, or improving over fixed-pass
  compilers like Qiskit. Covers dual-encoder stage-aware representation, shaped rewards for
  cross-stage credit assignment, dynamic action masking for valid compilation. Based on
  arXiv:2605.11375 (TuniQ). Activation: quantum compilation RL, tuniq, quantum compiler
  optimization, RL transpiler, quantum pass selection, fidelity optimization, autotuning
  quantum compilation, compilation pass scheduling.
tags: [quantum-compilation, reinforcement-learning, fidelity-optimization, autotuning, qiskit, transpiler]
arxiv_id: "2605.11375"
paper_title: "TuniQ: Autotuning Compilation Passes for Quantum Workloads at Scale for Effectiveness and Efficiency"
authors: "Mohammad Abrarul Hasanat, Jason Ludmir, Tirthak Patel, Rohan Basu Roy"
---

# TuniQ: RL-Based Quantum Compilation Pass Autotuning

## Problem

Quantum circuit compilation determines output fidelity and runtime. Standard compilers (e.g.,
Qiskit transpiler) use fixed pass sequences that ignore circuit-specific, backend-specific,
and noise-dependent optimal pass selection. This leads to suboptimal fidelity and wasted
compile time.

## TuniQ Architecture

### 1. Stage-Aware Dual Encoder

```
Circuit Representation
  ├── Graph encoder (circuit topology)
  └── Pass encoder (pipeline stage context)
        └── Stage-aware representation fusion
```

The dual encoder produces stage-aware representations that let the RL agent understand:
- Current circuit state (gate types, connectivity, depth)
- Pipeline stage context (which passes have been applied)

### 2. Shaped Reward Design

```
Reward = α * Fidelity + β * (-CompileTime) + γ * CrossStageBonus
```

- **Fidelity term**: Primary objective, measured via simulated execution
- **Compile time**: Secondary penalty to avoid over-optimization
- **Cross-stage bonus**: Encourages beneficial pass sequences across stages

### 3. Dynamic Action Masking

Ensures only valid compilation passes are available at each stage:
- Prevents applying gate synthesis before routing
- Blocks redundant passes
- Respects hardware topology constraints

## Pipeline Stages

1. **Gate decomposition**: Break down high-level gates into native gate set
2. **Qubit mapping**: Map logical to physical qubits
3. **Routing**: Insert SWAPs for non-local interactions
4. **Optimization**: Reduce gate count and depth
5. **Scheduling**: Arrange gates for parallel execution

## Usage

### Analyzing a quantum circuit for compilation optimization

1. Extract circuit features (gate count, topology, connectivity)
2. Identify target backend (IBMQ, IonQ, etc.) and its noise profile
3. Apply TuniQ-inspired RL policy to select compilation passes
4. Evaluate fidelity and compile time against baseline

### Reproducing TuniQ results

```python
# Key evaluation metrics
metrics = {
    "fidelity_improvement": "vs Qiskit highest optimization level",
    "compile_time_reduction": "vs fixed-pass sequence",
    "generalization": "cross-backend without retraining",
    "scaling": "utility-scale circuits"
}
```

### Integration patterns

```
Circuit → [Dual Encoder] → State → [RL Policy] → Pass Selection
  → Execute Pass → Update State → Repeat until pipeline complete
  → Final circuit → Execute on QPU → Measure fidelity
```

## Key Results from Paper

- **Fidelity improvement**: Consistently outperforms Qiskit highest optimization level
- **Compile time reduction**: Faster compilation than heuristic-heavy approaches
- **Generalization**: Works across different backends without retraining
- **Scaling**: Shows growing advantage on utility-scale circuits

## Related Skills

- `quantum-compiler-routing`: Qubit mapping and routing
- `quantum-compilation-workflow`: Multi-objective compilation
- `mqt-quantum-classical-compiler`: Quantum compilation tools
- `tuniq-quantum-compiler-rl`: This skill

## References

- arXiv: https://arxiv.org/abs/2605.11375
- PDF: https://arxiv.org/pdf/2605.11375
