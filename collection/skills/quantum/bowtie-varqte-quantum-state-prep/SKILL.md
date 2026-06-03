---
name: bowtie-varqte-quantum-state-prep
description: >
  Bowtie VarQTE methodology for resource-efficient quantum state preparation
  using variational quantum time evolution with causal light-cone optimization.
  Covers classical-quantum hybrid simulation, McLachlan's variational principle,
  and reducing quantum resource requirements. Based on Drudis et al.
  (arXiv:2605.20331). Use when: quantum state preparation, variational quantum
  time evolution, VarQTE, causal light-cone optimization, hybrid
  classical-quantum simulation, quantum resource efficiency, imaginary time
  evolution, quantum algorithm primitives.
---

# Bowtie VarQTE: Resource-Efficient Quantum State Preparation

Based on Drudis, Baiardi, Chiurco, Tacchino, Woerner, Zoufal,
"Bowtie VarQTE: A Resource-Efficient Quantum State Preparation Primitive"
(arXiv:2605.20331).

## Core Idea

Bowtie VarQTE uses classical simulation where possible and quantum resources
where necessary, leveraging causal light-cones to minimize quantum circuit
depth in evaluating gradient and quantum geometric tensor (QGT) terms.

## Architecture

```
Initial State → Trotter Decomposition → Light-Cone Analysis
     → Classical Simulation (causal subcircuits)
     → Quantum Evaluation (non-causal terms)
     → McLachlan Parameter Updates → Prepared State
```

## Key Innovations

### 1. Causal Light-Cone Exploitation

For local Hamiltonians, the causal light-cone of an operator determines which
qubits actually influence the measurement. Terms within the light-cone can be
simulated classically, reducing quantum circuit requirements.

### 2. Hybrid Classical-Quantum Evaluation

- **Classical**: Simulate causally relevant subcircuits on classical hardware
- **Quantum**: Only evaluate terms requiring genuine quantum resources
- **Result**: Exact parameter updates via McLachlan's variational principle

### 3. McLachlan's Variational Principle

Minimizes the distance between exact time evolution and variational manifold:

```
A θ_dot = C
```

where A is the quantum geometric tensor and C encodes the Hamiltonian action.

## Comparison with AQC (Approximate Quantum Compilation)

| Aspect | AQC | Bowtie VarQTE |
|--------|-----|---------------|
| Target state | Requires classical representation | No classical representation needed |
| Fidelity | High | Comparable |
| Quantum cost | Higher | Reduced via light-cone optimization |
| Numerical stability | May degrade | Improved via exact updates |

## Algorithm Steps

1. **Initialize** variational ansatz (e.g., hardware-efficient or Trotter-based)
2. **Compute light-cones** for each gradient and QGT term
3. **Classical simulation** for terms within causal light-cone
4. **Quantum evaluation** for terms requiring quantum resources
5. **Solve** McLachlan linear system A θ_dot = C
6. **Update** parameters and iterate
7. **Combine** imaginary + real time evolution for target state preparation

## Applications

- Ground state preparation for quantum algorithms
- Sample-based quantum algorithms (e.g., Krylov diagonalization)
- 2D system state preparation with reduced quantum requirements
- Hybrid quantum-classical simulation pipelines

## Resource Analysis

- Circuit depth: reduced by O(1) per light-cone layer
- Qubit count: unchanged but effective usage improved
- Classical overhead: polynomial in light-cone size
- Quantum measurements: reduced proportional to classical simulation fraction

## Activation

Keywords: bowtie varqte, variational quantum time evolution, quantum state
preparation, causal light-cone, McLachlan variational principle, hybrid
quantum-classical simulation, quantum resource optimization, imaginary time
evolution, approximate quantum compilation
