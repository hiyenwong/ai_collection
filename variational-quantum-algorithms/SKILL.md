---
name: variational-quantum-algorithms
description: "Variational Quantum Algorithms methodology covering CVQE (Cascaded Variational Quantum Eigensolver), certified QNN training via QIBP, and resource-efficient quantum optimization. Use when designing variational quantum circuits, optimizing NISQ-era algorithms, implementing certified quantum machine learning, or applying quantum algorithms to combinatorial optimization problems. Covers VQE variants, quantum interval bound propagation, compact binary encoding for quantum optimization, and divide-and-conquer quantum execution strategies."
---

# Variational Quantum Algorithms

## Overview

Methodology for designing and implementing variational quantum algorithms across three key areas:
1. **Cascaded VQE (CVQE)** - Non-iterative quantum-classical eigensolver
2. **Certified QNN Training (QIBP)** - Adversarial robustness for quantum ML
3. **Resource-Efficient Quantum Optimization** - Compact encoding for NISQ combinatorial problems

## 1. Cascaded Variational Quantum Eigensolver (CVQE)

CVQE circumvents iterative quantum-classical communication required by conventional VQE.

### Key Method: Trapezoidal-State Guiding State Selection

1. **Prepare guiding state** using trapezoidal-state parameterization
2. **Analyze state probability distributions** at each CVQE stage
3. **Optimize guiding-state parameters** for given resource constraints
4. **Execute CVQE** without iterative quantum-classical feedback loop

### When to Use
- Many-electron ground-state energy calculation
- NISQ devices with limited coherence time
- Situations where classical-quantum communication overhead is prohibitive

### Guiding State Selection Process
```
Input: Hamiltonian H, resource constraints
1. Choose trapezoidal-state ansatz for guiding state |ψ_g(θ)>
2. Analyze probability distribution P_i = |<i|ψ_g>|^2 at each stage
3. Select θ that maximizes overlap with target ground state
   while minimizing circuit depth within resource limits
4. Execute CVQE cascade: apply unitary operations sequentially
5. Extract ground-state energy from final measurement statistics
```

### Pitfalls
- Not all guiding states yield accurate solutions
- Resource efficiency depends heavily on guiding state quality
- Probability distribution analysis is essential for parameter selection

## 2. Quantum Interval Bound Propagation (QIBP)

Certified training method for quantum neural networks that guarantees robustness under adversarial perturbations.

### Core Idea
Track lower and upper bounds of quantum state amplitudes throughout the QNN circuit, using these bounds during training to ensure certified robustness.

### Two Implementations

| Approach | Trade-off |
|----------|-----------|
| **Interval Arithmetic** | Tighter bounds, higher computational cost |
| **Affine Arithmetic** | Faster computation, looser bounds |

### QIBP Training Routine
```
For each training step:
1. Forward pass: propagate interval bounds through each quantum gate
   - For single-qubit gates: apply gate to interval bounds
   - For entangling gates: compute joint interval propagation
2. Compute certified loss: L_certified = L_standard + λ · bound_width
3. Backward pass: update parameters to minimize certified loss
4. Verify: for input x + δ (||δ|| ≤ ε), model predicts correct class
```

### When to Use
- Quantum classification tasks requiring robustness guarantees
- Adversarial scenarios where input perturbations are expected
- Hybrid quantum-classical ML pipelines

### Key Parameters
- `ε`: Adversarial perturbation budget (robustness radius)
- `λ`: Weight for bound-width regularization term
- Arithmetic type: interval (tighter) vs affine (faster)

## 3. Resource-Efficient Variational Quantum Optimization

Addresses qubit overhead in quantum combinatorial optimization (e.g., TSP, Max-Cut).

### Compact Binary-Encoding

Reduces qubit requirement from O(n²) one-hot to O(n log n) binary encoding.

```
One-hot encoding:    n cities → n² qubits
Binary encoding:     n cities → n·⌈log₂(n)⌉ + O(n) qubits
```

### Divide-and-Conquer Execution

```
1. Partition problem into subsystems of manageable size
2. Solve each subsystem independently on available hardware
3. Classically combine subsystem solutions
4. Iterate with refined partitioning if needed
```

### Permutation-Preserving Ansatz

Design ansatz that respects problem symmetries:
- For TSP: ensure ansatz preserves valid permutations
- Reduces search space, improves success probability

### When to Use
- Combinatorial optimization on resource-constrained NISQ hardware
- Problems with O(n²) qubit overhead in standard formulations
- Real hardware experiments with limited qubit counts

## Workflow: Choosing the Right Approach

```
Problem Type → Algorithm
├── Ground-state energy / Chemistry
│   └── CVQE with trapezoidal guiding states
├── Quantum ML / Classification
│   └── QIBP (interval for tight bounds, affine for speed)
├── Combinatorial Optimization (small-scale)
│   └── Compact binary encoding + divide-and-conquer
└── General variational optimization
    └── Standard VQE with problem-inspired ansatz
```

## Implementation Notes

### CVQE Implementation
- Use Qiskit or Pennylane for circuit construction
- Trapezoidal states: parameterize as superposition with specific amplitude distribution
- Monitor probability distributions at each cascade stage

### QIBP Implementation
- Pennylane recommended for differentiable quantum circuits
- Interval arithmetic: track [lower, upper] for each amplitude
- Certified accuracy = fraction of inputs where prediction is guaranteed correct

### Resource-Efficient Optimization
- Binary encoding: map city indices to binary strings
- Ansatz design: use controlled rotations that preserve permutation validity
- Hardware: tested on SpinQ Gemini Pro (2-qubit) and Triangulum II (3-qubit) NMR devices

## References

- arXiv:2605.00807 — CVQE with trapezoidal guiding states (Lai et al., 2026)
- arXiv:2605.00747 — QIBP certified training (Andrews et al., 2026)
- arXiv:2605.00739 — Resource-efficient VQE for TSP (Lin et al., 2026)
- **Paper survey details**: See [references/paper-survey-may2026.md](references/paper-survey-may2026.md) for full abstracts and methodology details
