---
name: quantum-optimization-qaoa
description: "Guide for understanding and applying the Quantum Approximate Optimization Algorithm (QAOA) for combinatorial optimization problems. Covers QAOA principles, circuit construction, parameter optimization, and classical-quantum hybrid workflows. Use when working with quantum optimization, variational quantum algorithms, combinatorial optimization on quantum hardware, or analyzing QAOA performance on specific problem instances."
---

# Quantum Optimization with QAOA

## Core Concept

QAOA is a variational quantum algorithm for combinatorial optimization. It alternates between applying a problem Hamiltonian (cost function) and a mixing Hamiltonian, with parameters optimized classically.

## When to Use

- Combinatorial optimization problems (MaxCut, portfolio optimization, scheduling)
- When quantum advantage may be achievable with NISQ-era hardware
- As a baseline for comparing quantum vs classical optimization approaches
- When variational quantum algorithm patterns are needed

## Algorithm Structure

### 1. Problem Encoding

Map the optimization problem to a binary formulation. Two common approaches:

**QUBO (Quadratic Unconstrained Binary Optimization)**: Standard form, well-supported by quantum hardware and classical solvers.

**HUBO (Higher-Order Unconstrained Binary Optimization)**: Captures complex constraints impossible in QUBO (e.g., correlated scheduling rules, multi-resource couplings) using k-local terms (k>2). HUBO uses fewer binary variables than QUBO through compact encoding, reducing qubit demand — but introduces higher-order interaction terms that increase circuit depth. On NISQ hardware, HUBO is typically reduced to QUBO via auxiliary variables (accepting qubit overhead); in fault-tolerant regimes, HUBO maps directly to quantum circuits with multi-controlled gates. See `hubo-quantum-optimization` skill for full methodology.

### 2. QAOA Circuit

For depth p, the circuit applies alternating layers:
```
|ψ(γ,β)⟩ = Π_{k=1}^{p} e^{-iβ_k H_M} e^{-iγ_k H_C} |+⟩^{⊗n}
```
- H_M = Σ X_i (mixing Hamiltonian)
- H_C encodes the problem

### 3. Classical Optimization Loop

1. Initialize parameters (γ, β)
2. Run quantum circuit, measure expectation ⟨H_C⟩
3. Use classical optimizer (COBYLA, SPSA, gradient-based) to update parameters
4. Repeat until convergence

## Key Patterns

### Pattern 1: MaxCut QAOA

```python
# Problem: MaxCut on graph G
# H_C = 1/2 Σ_{(i,j)∈E} (I - Z_i Z_j)
# For each edge (i,j), apply ZZ rotation
```

### Pattern 2: Parameter Initialization

- Start with γ_k = small values, β_k = π/4 (annealing-inspired)
- Use layer-by-layer initialization (FOOF pattern)
- Warm-start from lower depth solutions

### Pattern 3: Noise-Aware Optimization

- SPSA optimizer is robust to hardware noise
- Increase shots for gradient estimation
- Use error mitigation (readout correction, zero-noise extrapolation)

## Performance Considerations

- **Depth p**: Higher depth → better approximation but more noise
- **Problem structure**: Local vs global connectivity affects performance
- **Classical optimizer**: Gradient-free (SPSA, Nelder-Mead) preferred for noisy hardware
- **Barren plateaus**: Shallow circuits (p ≤ 3) typically avoid this issue

### NISQ Scaling Boundary (empirical, IBM hardware 2026)

On IBM 127-qubit devices at QAOA depth p=1:
- >97% solution quality up to 15 qubits
- ~85% at 20 qubits
- <65% at 25 qubits (circuit noise dominates)
- Near-zero signal at 30 qubits

### Constraint-Preserving Mixers

Standard QAOA uses Pauli-X mixer (H_M = Σ X_i). For constrained problems, two approaches compete:

| Constraint structure | Recommended mixer | Rationale |
|---------------------|-------------------|-----------|
| Multiple disjoint local blocks (e.g. one-hot per group) | XY-mixer | Trotter errors stay localized; preserves feasible subspace |
| Single global equality spanning all variables | Pauli-X mixer | XY-mixer Trotter errors propagate across entire system |

See [references/constraint-mixers.md](references/constraint-mixers.md) for detailed patterns.

### QAOA Efficacy Mechanism for Random k-SAT (arXiv:2605.20288)

Recent work reveals that QAOA's efficacy for random k-SAT problems can be explained by a **novel adiabatic manifold** within a universal-mixer k-local search framework:
- Optimal QAOA parameters lie on a **smooth manifold** that can be characterized by a **sublinear number of parameters**
- This enables **efficient parameter optimization** — no need to search the full parameter space
- The adiabatic manifold connects to the underlying physics of the problem Hamiltonian's spectral structure

**Implication for practitioners**: Instead of variational optimization over all 2p parameters, constrain parameters to the adiabatic manifold and optimize only the sublinear subset. This dramatically reduces classical optimization overhead while maintaining solution quality.

### Counterdiabatic QAOA (CCD-QAOA)

CCD-QAOA adds counterdiabatic driving terms to the QAOA ansatz to suppress non-adiabatic transitions, achieving better approximation ratios at fixed depth:

```
|γ,β,α⟩ = Π e^{-iα_k H_CD} e^{-iβ_k H_M} e^{-iγ_k H_C} |+⟩^{⊗n}
```

- **H_CD**: Approximate adiabatic gauge potential from nested commutators [H_C, H_M], [H_C,[H_C,H_M]], etc.
- **XY-mixer + CD**: Natural combination for cardinality constraints (preserves Hamming weight)
- **Superior to penalty methods**: No energy landscape distortion
- **Trotterization tradeoff**: More steps = better constraint preservation but deeper circuits (see [references/counterdiabatic-qaoa.md](references/counterdiabatic-qaoa.md))
- **Key papers**: arXiv:2605.06858 (CCD-QAOA for portfolio), arXiv:2605.02465 (XY-mixers under Trotterization)

### Compressed AQC-QAOA Initialization

Instead of uniform superposition |+⟩^{⊗n}, initialize with compressed Approximate Quantum Compilation (AQC) prefix of digitized adiabatic evolution. Reduces two-qubit gate depth while maintaining or improving feasible solution discovery — especially effective for routing problems (VRP, TSP). Effectiveness depends on compatibility between compressed prefix and variational ansatz.

### SAFE ma-QAOA: Surrogate-Assisted Training with Parameter Distillation

For **multi-angle QAOA** (ma-QAOA) where each gate has independent parameters, the SAFE framework reduces QPU workload by 94.5%:

1. **Surrogate pre-training**: Use Low-Weight Pauli Propagation (LWPP) classically — zero QPU calls
2. **Parameter distillation**: Remove near-zero angles after surrogate convergence (≈64% fewer params)
3. **Exact fine-tuning**: Optimize remaining active parameters on quantum hardware

See [references/safe-ma-qaoa.md](references/safe-ma-qaoa.md) for full methodology and benchmarks.

## References

- Farhi et al. (2014): Original QAOA paper
- arXiv:2511.12379: Quantum Optimization Algorithms survey
- arXiv:2511.18377: QAOA tutorial with first-principles introduction
