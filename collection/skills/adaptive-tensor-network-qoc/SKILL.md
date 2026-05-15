---
name: adaptive-tensor-network-qoc
description: >
  Adaptive Tensor Network Sampling for Quantum Optimal Control methodology.
  Uses Matrix Product State (MPS) / Tensor Train (TT) sampling as a gradient-free
  heuristic for discrete quantum optimal control problems. The MPS defines a score
  function over the space of discrete control parameters, inducing a sampling
  distribution that is iteratively refined through selection of top-performing
  sequences and local tensor updates. Use when: (1) designing gradient-free quantum
  optimal control algorithms, (2) optimizing quantum gate synthesis or state transfer,
  (3) implementing tensor network-based sampling for control problems, (4) exploring
  non-convex optimization landscapes in quantum control, (5) comparing gradient-free
  vs gradient-based QOC methods. Activation: tensor network quantum control, MPS sampling,
  quantum optimal control gradient-free, tensor train QOC, adaptive MPS control,
  张量网络量子优化控制, 矩阵乘积态采样.
---

# Adaptive Tensor Network Sampling for Quantum Optimal Control

Based on arXiv:2604.24467 — *Adaptive Tensor Network Sampling for Quantum Optimal Control*
(Zeybek, Mukherjee, Schmelcher, 2026).

## Core Methodology

Replace high-dimensional gradient-free search in quantum optimal control with
MPS/TT-structured sampling that captures correlations between control steps while
remaining computationally tractable.

### Key Insight
The MPS bond dimension `D` controls expressivity: `D=1` factorizes to independent
per-site distributions; increasing `D` captures inter-step correlations. For `N`
control steps with `d` discrete values each, the MPS represents the distribution
in `O(N * d * D²)` parameters vs `O(d^N)` for a full distribution.

## Workflow

### Step 1: Discretize the Control Problem
- Decompose total evolution time `T` into `N` discrete steps
- Choose discrete control values `{u_1, ..., u_d}` (e.g., pulse amplitudes, frequencies)
- Define objective function `f(sequence) → ℝ` (higher = better)

### Step 2: Initialize MPS Sampler
```python
from scripts.mps_qoc_sampler import MPSSampler, run_qoc_optimization

sampler = MPSSampler(n_sites=N, local_dim=d, bond_dim=D)
```
Bond dimension guidelines:
- `D=1`: Independent per-site (factorized) — baseline, fast but limited
- `D=2-4`: Weak correlations — single-qubit tasks
- `D=8-16`: Moderate correlations — multi-qubit gates
- `D=32+`: Strong correlations — many-body control

### Step 3: Sampling Loop
Each iteration:
1. **Sample** `M` candidate sequences from current MPS
2. **Evaluate** objective for each sequence
3. **Select** top `α*M` sequences (typically α=0.2)
4. **Update** MPS tensors via gradient step toward selected sequences

```python
best_seq, best_score = run_qoc_optimization(
    objective_fn=my_objective,
    n_sites=10,      # control steps
    local_dim=4,     # discrete control values
    bond_dim=8,      # MPS bond dimension
    n_iterations=50,
    n_samples=100,
    learning_rate=0.05
)
```

### Step 4: Objective Function Design
The objective function maps a control sequence to a scalar score. Common patterns:

**State transfer**: Maximize fidelity `|⟨target|ψ(T)⟩|²`
```python
def state_transfer_objective(seq):
    psi = evolve_state(initial_state, seq)  # propagate through control sequence
    return abs(np.vdot(target_state, psi)) ** 2
```

**Gate synthesis**: Maximize gate fidelity `|Tr(U_target† U_actual)|² / d²`
```python
def gate_synthesis_objective(seq):
    U_actual = propagate_unitary(seq)
    return np.abs(np.trace(U_target.conj().T @ U_actual)) ** 2 / dim ** 2
```

**Open system**: Use process fidelity or population transfer with decoherence
```python
def open_system_objective(seq):
    rho_final = propagate_density_matrix(initial_rho, seq, noise_model)
    return np.real(np.trace(target_rho @ rho_final))
```

## When to Use

| Scenario | Recommended Approach |
|----------|---------------------|
| Single-qubit gate, smooth landscape | Gradient-based (GRAPE, CRAB) |
| Discrete controls, many local minima | MPS/TT sampling (this method) |
| Multi-parameter, non-convex | MPS/TT sampling with D≥8 |
| Open system, non-Markovian noise | MPS/TT + uniTEMPO simulation |
| Large N (>50 steps) | Increase D or use hierarchical MPS |

## Advantages over Baselines

- **vs Random search**: MPS captures correlations between control steps
- **vs Genetic algorithms**: Structured distribution, more sample-efficient
- **vs Reinforcement learning**: No training overhead, direct optimization
- **vs Gradient-based**: No gradient computation needed, escapes local minima

## Parameters

| Parameter | Default | Effect |
|-----------|---------|--------|
| `n_sites` | 10 | Control discretization; higher = finer control, larger search space |
| `local_dim` | 4 | Discrete control resolution; higher = more precise, slower convergence |
| `bond_dim` | 8 | Expressivity; higher captures more correlations but more parameters |
| `n_samples` | 100 | Batch size; higher = better statistics, more evaluations per iteration |
| `learning_rate` | 0.05 | Update speed; too high → unstable, too low → slow convergence |
| `top_fraction` | 0.2 | Selection pressure; lower = more exploitative, higher = more explorative |

## Example Applications

1. **Single-qubit state transfer**: N=8-16, d=4, D=4
2. **Bell-pair preparation**: N=16-32, d=4, D=8
3. **Qutrit gate synthesis**: N=16, d=6, D=8
4. **Open-system population transfer**: N=20, d=4, D=16

## Implementation Notes

- The MPS sampling is done sequentially: at each site, contract left environment,
  compute local probabilities by summing over right indices, sample, update environment
- Tensor update uses simplified empirical distribution from top sequences;
  for production, use SVD-based updates for better convergence
- Normalize tensors after each update to maintain numerical stability
- For large problems, parallelize objective evaluation across samples

## Limitations

- Discrete control only (not continuous); for continuous, increase `local_dim`
  or use post-processing interpolation
- No guarantees on global optimality (heuristic method)
- Bond dimension grows exponentially with entanglement; for highly correlated
  problems, may need large `D`
- Not suited for real-time control; designed for offline protocol design

## References

- arXiv:2604.24467 — *Adaptive Tensor Network Sampling for Quantum Optimal Control*
- Related: DMRG, TEBD, variational MPS optimization methods
