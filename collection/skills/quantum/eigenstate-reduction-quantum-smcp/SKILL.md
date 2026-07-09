---
name: eigenstate-reduction-quantum-smcp
description: >
  Tractable Infinite-Horizon Stochastic Model Predictive Control for Quantum Filtering via Eigenstate Reduction.
  Uses almost-sure eigenstate reduction of quantum trajectories to collapse infinite-horizon stochastic objective
  to closed-form fidelity term. Eliminates per-horizon Monte Carlo sampling while retaining stochastic dynamics.
  Use when designing quantum SMPC controllers, quantum filtering-based control, mean-square stability analysis,
  or tractable stochastic optimal control for quantum systems.
metadata:
  arxiv_id: "2511.05916"
  published: "2025-11-08"
  authors: "Yunyan Lee, Ian R. Petersen, Daoyi Dong"
  tags: [quantum-control, MPC, stochastic-control, quantum-filtering, eigenstate-reduction, optimal-control, systems-engineering]
---

# Eigenstate-Reduction Quantum SMPC

## Overview

Stochastic Model Predictive Control (SMPC) for quantum systems traditionally requires per-horizon Monte Carlo
scenario sampling, which is computationally prohibitive. This methodology uses the **almost-sure eigenstate reduction**
of quantum trajectories under continuous measurement to collapse the infinite-horizon stochastic objective to a
**closed-form fidelity term** computable from the one-step averaged state.

## Core Mathematical Insight

### Eigenstate Reduction Theorem

Under continuous-time measurement, quantum trajectories almost surely converge to eigenstates of the measurement
operator. This means the infinite-horizon expected cost:

```
J = E[∑ γ^k · cost(ρ_k, u_k)]
```

collapses to:

```
J = F(ρ̄_1)  (closed-form fidelity from one-step averaged state)
```

where ρ̄_1 is the one-step averaged (expected) state after applying the control.

### Computational Reduction

| Approach | Complexity | Scalability |
|----------|-----------|-------------|
| Sampling-based SMPC | O(N_scenarios × N_horizon) | Poor for long horizons |
| Eigenstate-reduction SMPC | O(1) terminal evaluation | Linear in system dimension |

## Algorithm

### Step 1: Quantum Filter Propagation
```
ρ̄_{k+1} = 𝔼[ρ_{k+1} | ρ_k, u_k]  (deterministic)
```
Propagate the averaged density matrix deterministically — no sampling needed.

### Step 2: Terminal Fidelity Evaluation
```
F_term = Tr(ρ_target · ρ̄_N)
```
Evaluate fidelity against target state at the prediction horizon endpoint.

### Step 3: Optimization
```
min_u  -F_term(ρ̄_N(u))
s.t.   physical constraints on u (amplitude, bandwidth, etc.)
```
Solve the deterministic optimization problem.

### Step 4: Receding Horizon Implementation
Apply first control step, re-measure, re-optimize.

## Stability Guarantees

- **Equivalence**: The reduced objective is equivalent to the full stochastic objective in the infinite-horizon limit
- **Mean-square stability**: Closed-loop system is mean-square stable under the receding horizon policy
- Validated on multi-level systems and Ising-type coupled systems

## Application Workflow

1. **Define system**: Hamiltonian H₀, control Hamiltonians H_c, measurement operators M
2. **Set target**: Desired quantum state or gate operation
3. **Configure filter**: Quantum stochastic differential equation for averaged state propagation
4. **Terminal cost**: Fidelity with respect to target state
5. **Solve**: Standard optimization (gradient-based or derivative-free)
6. **Validate**: Compare with sampling-based SMPC for correctness

## Key Advantages

1. **No Monte Carlo sampling**: Eliminates the dominant computational bottleneck
2. **Closed-form terminal**: Fidelity computable analytically from one-step averaged state
3. **Mean-square stability**: Theoretical guarantees preserved
4. **Scalability**: Linear scaling vs exponential for sampling-based approaches
5. **Generality**: Applicable to finite-dimensional quantum systems under continuous measurement

## Pitfalls

- **Eigenstate reduction assumption**: Requires continuous measurement to drive trajectories to eigenstates. Intermittent or weak measurement may not satisfy the convergence condition.
- **Finite-dimensional systems**: Theory established for finite-dimensional Hilbert spaces. Extension to infinite dimensions requires additional analysis.
- **Measurement backaction**: The approach assumes the measurement operator structure is known and correctly modeled.
- **Horizon truncation**: While theoretically infinite-horizon, practical implementation uses finite N — verify convergence.

## Related Skills

- `vf-qctrl-llm-quantum-control` — LLM-driven quantum control (alternative approach)
- `quantum-control-pulse-software` — Pulse-level control software framework
- `model-predictive-quantum-control` — General MPC for quantum systems
- `discounted-mpc-control` — Discounted MPC stability analysis (classical analogue)

Activation: stochastic model predictive control, quantum SMPC, quantum filtering, eigenstate reduction, quantum trajectory, continuous measurement, mean-square stability, quantum optimal control, receding horizon quantum control
