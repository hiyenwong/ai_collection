---
name: coherent-feedback-h-infinity-quantum-control
description: Simplified coherent feedback H∞ control design for linear quantum systems using Lyapunov equations instead of coupled algebraic Riccati equations — computationally efficient robust control for quantum optical systems.
category: quantum
version: "1.0"
created: "2026-07-09"
trigger_words: ["coherent feedback", "H-infinity quantum", "quantum linear system control", "Lyapunov quantum control", "quantum robust control", "quantum optical control"]
source_paper: "arXiv:2604.06574"
---

# Coherent Feedback H∞ Control of Quantum Linear Systems

## Overview

This methodology provides a **simplified design approach for coherent feedback H∞ control** of linear quantum systems. Instead of solving two coupled algebraic Riccati equations (standard approach), a physically realizable quantum controller is obtained by solving **at most four Lyapunov equations**, providing significant computational efficiency.

## Core Methodology

### General Case
1. Formulate the linear quantum system in state-space form
2. Solve **at most four Lyapunov equations** to obtain the controller
3. Verify physical realizability conditions
4. Guarantee closed-loop stability + prescribed disturbance attenuation level

### Passive Case (Simplified)
1. Solve **two uncoupled pairs of Lyapunov equations**
2. This provides a **necessary and sufficient condition** for passive coherent H∞ control
3. Significantly simpler than the standard Riccati-based approach

## Mathematical Framework

For a linear quantum system:
```
dx = A x dt + B1 dw + B2 du
dy = C1 x dt + D12 dw
du = Ck xk dt + Dk dy  (controller)
```

The H∞ controller design problem: find Ck, Dk such that the closed-loop system is physically realizable and achieves γ-disturbance attenuation.

**Traditional**: Solve 2 coupled algebraic Riccati equations (ARE)
**This method**: Solve ≤4 Lyapunov equations

## Advantages

- **Computational efficiency**: Lyapunov equations are simpler than coupled AREs
- **Numerical stability**: Lyapunov solvers are more robust than ARE solvers
- **Scalability**: Better suited for larger quantum systems
- **Same guarantees**: Closed-loop stability + prescribed H∞ performance

## Demonstrated Applications

1. **Empty optical cavity** — standard quantum optical benchmark
2. **Degenerate parametric amplifier** — nonlinear quantum optical device (linearized)

## When to Use

- Linear quantum systems (or linearized around operating point)
- Quantum optical systems (cavities, amplifiers, optomechanical systems)
- When computational efficiency is important
- When robust disturbance attenuation is required

## Pitfalls

- Only applies to **linear** quantum systems
- Physical realizability constraints must still be verified
- For highly nonlinear systems, linearization may be insufficient
- The four Lyapunov equations must all have solutions (feasibility check needed)
- Does not handle measurement-based feedback (this is coherent/coherent-only)

## Verification

1. Verify all Lyapunov equations have positive-definite solutions
2. Check physical realizability conditions on the resulting controller
3. Simulate closed-loop response to verify H∞ performance bound
4. Validate on standard benchmarks (optical cavity, parametric amplifier)