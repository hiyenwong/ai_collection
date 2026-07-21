---
name: hybrid-tensor-network-qml
description: >
  Hybrid tensor network architecture for quantum machine learning using
  post-selection as a trainable hyperparameter. Interpolates between classical
  and quantum tensor network edge cases by controlling quantum constraint
  enforcement via post-selection allocation. Use when designing hybrid
  quantum-classical ML models, tensor network quantum ML, or optimizing
  quantum resource allocation with limited post-selection budget.
  Activation: hybrid tensor network, quantum-classical interpolation,
  post-selection QML, trainable quantum constraints.
---

# Hybrid Tensor Networks for QML

## Overview

Hybrid tensor networks combine classical and quantum tensor networks in a unified
framework, using post-selection as the key property controlling the interpolation
between regimes. The amount of post-selection determines how strongly quantum
constraints are enforced on the network.

## Core Concept

### Post-Selection as Hyperparameter

The framework introduces a **new hyperparameter** controlling the transition:
- **0 post-selection** → Pure classical tensor network
- **Full post-selection** → Pure quantum tensor network
- **Partial post-selection** → Hybrid (practical regime for NISQ)

This hyperparameter complements bond dimension as a second axis for
controlling model capacity.

## Architecture

### Step 1: Classical Tensor Network Backbone

Use classical tensor network (MPS, PEPS, TTN) as the base model:
- Efficient classical inference
- Well-understood training procedures
- Proven expressiveness for many tasks

### Step 2: Quantum Edge Integration

Replace selected tensor network edges with quantum circuits:
- Each quantum edge requires post-selection to enforce quantum constraints
- Post-selection probability determines feasible quantum portion

### Step 3: Trainable Post-Selection Allocation

Instead of fixed post-selection ratio:
```
Allocate post-selection budget to quantum model in a trainable manner
→ Optimize which edges get quantum treatment
→ Maximize quantum advantage within hardware constraints
```

## Training Protocol

1. Initialize classical tensor network
2. Select subset of edges for quantum replacement
3. Define post-selection budget (hyperparameter)
4. Train with quantum inference on selected edges
5. Optimize post-selection allocation jointly with model parameters
6. Evaluate classical vs quantum vs hybrid performance

## Comparison Framework

When comparing classical vs quantum tensor networks, report:
- **Bond dimension** (traditional hyperparameter)
- **Post-selection ratio** (new hyperparameter)
- **Classical/quantum/hybrid accuracy**
- **Resource requirements** (qubits, shots, post-selection success rate)

## Key Insights

1. **Post-selection is the bottleneck**: Limited post-selection on real devices
   means pure quantum tensor networks may be impractical
2. **Hybrid is the practical regime**: Partial quantum constraints + classical
   backbone gives best tradeoff
3. **Trainable allocation**: Let the model learn where quantum matters most
4. **Complementary to bond dimension**: Two independent capacity controls

## Design Patterns

### Pattern 1: Budget-Constrained Hybrid Design

```
Fixed post-selection budget → Optimize allocation → Best hybrid architecture
```

### Pattern 2: Progressive Quantum Integration

```
Start classical → Add quantum edges gradually → Monitor performance gain
→ Stop when budget exhausted or marginal gain negligible
```

## Applications

- **Quantum ML with limited qubits**: Maximize advantage within hardware limits
- **Tensor network compression**: Use quantum edges for hard-to-classical-compress regions
- **Benchmarking**: Systematically compare classical vs quantum tensor networks

## References

- Hybrid TN paper: arxiv:2605.02385 (Jäger, Bieniasz, Plenio, Rieser, 2026)
- Tensor Networks for ML: Stoudenmire & Schwab (2016)
- Post-selection in QML: Various works on post-selected quantum computing
