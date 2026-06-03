---
name: quantum-end-to-end-learning
description: >
  Quantum End-to-End Learning (QEL) methodology for contextual combinatorial
  optimization using QAOA-based quantum surrogate policies. Covers context
  re-uploading phase-separator design, stationarity-guaranteed end-to-end
  training, and avoiding NP-hard solver calls. Based on Lee & Kwon (arXiv:2605.20222).
  Use when: quantum optimization, contextual combinatorial optimization, QAOA
  training, quantum surrogate policy, end-to-end quantum learning, variational
  quantum algorithms for decision-making, quantum machine learning for
  optimization problems.
---

# Quantum End-to-End Learning (QEL) for Contextual Combinatorial Optimization

Based on Lee & Kwon, "Quantum End-to-End Learning for Contextual Combinatorial Optimization" (arXiv:2605.20222).

## Core Idea

QEL is the first quantum computing-based end-to-end learning framework for
contextual combinatorial optimization (CCO). It leverages QAOA and integrates
context re-uploading with a phase-separator that jointly captures relations
among contexts, uncertain coefficients, and optimal solutions.

## Architecture

```
Context Input → Context Re-uploading Phase-Separator → Quantum Surrogate Policy → Task Loss → Backprop
```

### Key Components

1. **Context Re-uploading Phase-Separator**: Encodes contextual information
   directly into the quantum circuit via repeated data re-uploading layers,
   analogous to state preparation in QAOA.

2. **Quantum Surrogate Policy**: A QAOA-based variational circuit that outputs
   probability distributions over combinatorial solutions, trained end-to-end
   on task loss.

3. **Stationarity Guarantee**: The contextual encoder integrates seamlessly
   within the quantum policy, ensuring gradient-based training has stationarity
   guarantees despite discreteness and nonconvexity.

## Training Workflow

1. Encode context features via re-uploading layers into quantum state
2. Apply QAOA-style alternating phase separator (problem Hamiltonian) and
   mixer (driver Hamiltonian)
3. Measure output qubits to sample solutions
4. Compute task loss directly (no NP-hard solver calls)
5. Backpropagate through quantum circuit to update parameters
6. Iterate until convergence

## Advantages Over Classical Methods

- **Fewer parameters**: Substantially fewer trainable parameters than classical
  benchmarks
- **No NP-hard solver calls**: Direct task-loss training avoids expensive
  optimization subroutine calls
- **Physical structure exploitation**: Optimization-aware structure grounded
  in quantum physical principles that classical methods cannot leverage
- **Competitive performance**: Empirically matches classical baselines on
  standard CCO benchmarks

## Parameter Structure

- Context encoder depth: scales with context dimensionality
- QAOA layers (p): depth vs. solution quality trade-off
- Re-uploading frequency: how often context is re-injected per layer

## Applications

- Resource allocation under uncertainty
- Routing with time-varying demands
- Portfolio optimization with market context
- Supply chain optimization with contextual features

## Activation

Keywords: quantum end-to-end learning, QEL, contextual combinatorial
optimization, QAOA training, quantum surrogate policy, context re-uploading,
variational quantum optimization, quantum decision-making
