---
name: failure-guided-quantum-fuzzing
description: >
  Methodology for testing and debugging hybrid quantum-classical (HQC) programs
  using failure-guided fuzzing. Models hybrid inputs as pairs of classical
  optimizer hyperparameters and quantum circuit parameters. Use when testing
  quantum algorithms (VQE, QAOA, QML), debugging quantum circuit convergence
  failures, or systematically exploring quantum parameter spaces. Covers
  two-phase fuzzing strategy, concolic seed discovery, and local fuzzing.
  Activation: quantum fuzzing, HQC testing, quantum circuit testing, hybrid
  quantum debugging, VQE testing, QAOA testing, quantum program verification.
---

# Failure-Guided Quantum Fuzzing

## Description

Systematic testing methodology for hybrid quantum-classical (HQC) programs
that uses failure signals to guide parameter space exploration. Based on
arXiv:2605.14219 (Zhang, 2026).

## Core Insight

Hybrid quantum-classical programs have two intertwined failure modes:
- **Non-convergence**: Classical optimizer fails to find good parameters
- **Circuit sensitivity**: Small parameter changes cause large output shifts

Failure-guided fuzzing exploits these by using failure signals (non-convergence,
poor solutions) to direct further exploration, rather than random testing.

## Two-Phase Strategy

### Phase 1: Seed Discovery
Search for non-convergent or failing configurations across the joint
(classical hyperparameters, quantum circuit parameters) space.

```
For each candidate seed:
  1. Initialize VQE/QAOA with random circuit parameters
  2. Run optimization with specific hyperparameters
  3. Check: did it converge to a good solution?
  4. If NOT converged → mark as failure seed
```

Concolic execution (concrete + symbolic) can improve seed discovery for VQE
but is less stable for QAOA due to its combinatorial landscape.

### Phase 2: Local Fuzzing
For each failure seed, perturb circuit parameters locally to explore
nearby failure regions.

```
For each failure seed (θ₀, hyperparams):
  For N iterations:
    θ' = θ₀ + δ  where δ ~ small perturbation
    Run optimization with θ'
    If still failing → expand search radius
    If converging → record boundary (success/failure frontier)
```

## Key Findings

1. **Local fuzzing is the main driver** of improvement over random testing
2. **Concolic seed discovery** helps VQE but is unstable for QAOA
3. **Failure patterns are localized** — nearby parameters tend to fail similarly
4. **Two-phase beats random** by 3-5x in failure detection rate

## Implementation Pattern (Qiskit)

```python
from qiskit import QuantumCircuit
from qiskit.algorithms import VQE, QAOA
from qiskit.circuit.library import TwoLocal
from qiskit.primitives import StatevectorSampler
import numpy as np

def fuzz_vqe(num_seeds=50, local_radius=0.1):
    """Two-phase failure-guided fuzzing for VQE."""
    failures = []

    # Phase 1: Seed discovery
    for _ in range(num_seeds):
        params = np.random.rand(circuit.num_parameters) * 2 * np.pi
        result = run_vqe(params)
        if not converged(result):
            failures.append(params)

    # Phase 2: Local fuzzing around failures
    for seed in failures:
        for _ in range(20):
            perturbed = seed + np.random.normal(0, local_radius, len(seed))
            result = run_vqe(perturbed)
            if not converged(result):
                local_radius *= 1.5  # expand search
            else:
                record_boundary(seed, perturbed)

def run_vqe(params):
    ansatz = TwoLocal(num_qubits, 'ry', 'cz')
    vqe = VQE(StatevectorSampler(), ansatz, SLSQP())
    return vqe.compute_minimum_eigenvalue(operator)
```

## Parameter Perturbation Strategies

| Strategy | Use Case | Distribution |
|----------|----------|-------------|
| Gaussian | Smooth landscapes | N(θ, σ²I) |
| Uniform | Bounded parameters | U(θ-r, θ+r) |
| Coordinate | Single-param sensitivity | Perturb one axis |
| Adaptive | Unknown landscape | σ *= 1.5 on failure |

## Convergence Criteria

```python
def converged(result, threshold=1e-4, max_iters=100):
    return (result.optimal_value < threshold and
            result.num_evals < max_iters)
```

## When to Use

- Testing VQE/QAOA implementations before production
- Debugging quantum circuit parameter initialization
- Evaluating optimizer robustness across parameter space
- Finding edge cases in hybrid quantum-classical loops
- Benchmarking quantum algorithm reliability

## Related Patterns

- **Concolic execution**: Combine concrete and symbolic analysis for seed discovery
- **Adaptive radius**: Dynamically adjust perturbation magnitude based on results
- **Boundary mapping**: Record success/failure frontiers for documentation

## Pitfalls

- QAOA's combinatorial landscape makes concolic analysis unstable
- Too-large perturbation radius skips over narrow failure regions
- Too-small radius gets stuck in local failure basins
- Statevector simulators don't capture noise-induced failures

## References

- arXiv:2605.14219 — "Failure-Guided Fuzzing for Hybrid Quantum-Classical Programs" (Zhang, 2026)
- Implemented on VQE and QAOA MaxCut using Qiskit
