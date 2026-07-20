---
name: quantum-boltzmann-bilevel
description: "Build fully connected Quantum Boltzmann Machines using bilevel optimization to overcome QAOA's fixed target Hamiltonian limitation and classical Boltzmann machines' partial connectivity constraint. Use when designing quantum generative models, energy-based quantum models, quantum sampling algorithms, or quantum optimization circuits. Triggers: quantum Boltzmann machine, QAOA, bilevel optimization, fully connected Boltzmann, quantum generative model, energy-based quantum model, quantum sampling, quantum annealing, Hamiltonian learning"
---

# Quantum Boltzmann Machine via Bilevel Optimization

## Overview

This skill provides techniques for building fully connected Quantum Boltzmann Machines (QBMs) by extending QAOA circuits with bilevel optimization. This overcomes two fundamental limitations: QAOA's fixed target Hamiltonian constraint and classical Boltzmann machines' partial connectivity.

Based on: *Breaking QAOA's Fixed Target Hamiltonian Barrier: A Fully Connected Quantum Boltzmann Machine via Bilevel Optimization* (arxiv:2605.07473, May 2026).

## Core Problems Addressed

### Problem 1: QAOA's Fixed Target Hamiltonian

Standard QAOA uses a fixed mixer + problem Hamiltonian:

```
|ψ⟩ = e^(-iβₚH_M) e^(-iγₚH_C) ... e^(-iβ₁H_M) e^(-iγ₁H_C) |+⟩ⁿ
```

The target Hamiltonian H_C is **fixed** by the problem — QAOA cannot learn or optimize the Hamiltonian itself.

### Problem 2: Classical Boltzmann Machines Are Partially Connected

Classical BMs require tractable sampling, limiting them to:
- Restricted Boltzmann Machines (RBM): bipartite, no visible-visible or hidden-hidden connections
- Deep Belief Networks: layered, limited connectivity

Fully connected classical BMs have intractable partition functions.

## The Solution: Bilevel QAOA for QBMs

The key insight: use **bilevel optimization** where the outer loop learns the optimal target Hamiltonian and the inner loop optimizes circuit parameters:

```
Outer loop (Hamiltonian learning):
    min_H  L(H, θ*(H))

Inner loop (circuit optimization):
    θ*(H) = argmin_θ  E_θ[H] - S(ρ_θ)  (free energy minimization)
```

## Technique 1: Bilevel Optimization Framework

```python
def bilevel_qbm_optimization(data, n_qubits, p_layers, lr_outer=0.01, lr_inner=0.1):
    """
    Bilevel optimization for Quantum Boltzmann Machine.
    
    Outer loop: Learn Hamiltonian parameters J_ij, h_i
    Inner loop: Optimize QAOA circuit angles γ, β
    """
    # Initialize Hamiltonian parameters (fully connected)
    J = np.zeros((n_qubits, n_qubits))  # Coupling matrix
    h = np.zeros(n_qubits)               # Local fields
    
    for outer_step in range(n_outer_steps):
        # === INNER LOOP: Circuit optimization ===
        gamma, beta = initialize_angles(p_layers)
        
        for inner_step in range(n_inner_steps):
            # Build QAOA circuit with current Hamiltonian
            state = build_qaoa_circuit(gamma, beta, J, h)
            
            # Compute free energy gradient
            energy_grad = compute_energy_gradient(state, J, h)
            entropy_grad = compute_entropy_gradient(state)
            
            # Update angles to minimize free energy
            gamma -= lr_inner * (energy_grad - temperature * entropy_grad)
            beta -= lr_inner * compute_mixer_gradient(state)
        
        # === OUTER LOOP: Hamiltonian learning ===
        # Compute gradient of outer objective w.r.t. Hamiltonian
        # Using implicit differentiation through inner solution
        dL_dJ = compute_outer_gradient(data, state, gamma, beta)
        dL_dh = compute_local_field_gradient(data, state, gamma, beta)
        
        # Update Hamiltonian parameters
        J -= lr_outer * dL_dJ
        h -= lr_outer * dL_dh
        
        # Enforce symmetry: J_ij = J_ji
        J = (J + J.T) / 2
    
    return J, h
```

## Technique 2: Fully Connected Hamiltonian Parameterization

The learned Hamiltonian allows arbitrary connectivity:

```python
def build_fully_connected_hamiltonian(J, h, n_qubits):
    """
    Build fully connected Ising-type Hamiltonian:
    
    H = -Σ_{i<j} J_ij Z_i Z_j - Σ_i h_i Z_i
    
    Unlike classical BMs, all pairs (i,j) can have non-zero couplings.
    """
    H = np.zeros((2**n_qubits, 2**n_qubits), dtype=complex)
    
    for i in range(n_qubits):
        # Local field term
        for state in range(2**n_qubits):
            spin_i = 1 if (state >> i) & 1 else -1
            H[state, state] -= h[i] * spin_i
        
        # Coupling terms (fully connected!)
        for j in range(i+1, n_qubits):
            for state in range(2**n_qubits):
                spin_i = 1 if (state >> i) & 1 else -1
                spin_j = 1 if (state >> j) & 1 else -1
                H[state, state] -= J[i, j] * spin_i * spin_j
    
    return H
```

**Key advantage:** Classical RBMs cannot model these interactions directly because the partition function becomes intractable. The quantum circuit provides efficient sampling.

## Technique 3: Quantum-Classical Nested Optimization

The nested loop structure:

```
┌─────────────────────────────────────────────┐
│ Outer Loop: Learn H (Hamiltonian)           │
│                                             │
│   ┌───────────────────────────────────┐     │
│   │ Inner Loop: Optimize θ (angles)   │     │
│   │                                   │     │
│   │  min_θ  F(θ; H) = ⟨H⟩_θ - TS(θ)  │     │
│   │  where F = free energy            │     │
│   │                                   │     │
│   └───────────────────────────────────┘     │
│                                             │
│   Update H: min_H D_KL(p_data || p_model)  │
│                                             │
└─────────────────────────────────────────────┘
```

**Implementation considerations:**
- Inner loop converges when free energy change < ε
- Outer loop uses implicit differentiation or finite differences
- Number of QAOA layers p controls expressivity (typically p=2-8)
- Temperature T controls exploration vs. exploitation

## Technique 4: Energy-Based Quantum Generative Modeling

Once trained, the QBM generates samples:

```python
def qbm_sample(J, h, gamma, beta, n_samples):
    """
    Generate samples from the trained QBM by running the optimized
    QAOA circuit and measuring in the computational basis.
    """
    samples = []
    for _ in range(n_samples):
        # Run optimized circuit
        state = build_qaoa_circuit(gamma, beta, J, h)
        # Measure to get bitstring
        sample = measure_computational_basis(state)
        samples.append(sample)
    return np.array(samples)
```

The distribution p(x) ∝ exp(-E(x)/T) where E(x) is determined by the learned Hamiltonian — the QBM naturally captures complex, multi-modal distributions.

## Activation Scenarios

Use this skill when:
- Building quantum generative models that surpass classical RBMs
- Need fully connected energy-based models (classical BMs are limited)
- Extending QAOA beyond fixed problem Hamiltonians
- Designing quantum sampling algorithms for complex distributions
- Working on combinatorial optimization via quantum annealing
- Implementing quantum approximate thermal states
- Comparing quantum vs. classical generative models

## Comparison: QBM vs. Classical Alternatives

| Capability | RBM | Deep BM | QBM (this skill) |
|-----------|-----|---------|------------------|
| Fully connected | ❌ | ❌ | ✅ |
| Learnable Hamiltonian | N/A | N/A | ✅ |
| Efficient sampling | ✅ (Gibbs) | Partial | ✅ (quantum) |
| Expressivity | Limited | Medium | High |
| Quantum advantage | N/A | N/A | Potential |

## Anti-Patterns to Avoid

1. **Too few QAOA layers** — p=1 is essentially classical; use p≥3 for quantum advantage
2. **Ignoring temperature** — Temperature is a critical hyperparameter; don't set T=0
3. **Overfitting Hamiltonian** — Regularize J matrix (e.g., sparsity penalty) to prevent overfitting
4. **No convergence check** — Inner loop must converge before outer step; don't use fixed iteration counts
5. **Classical simulation limits** — Full state vector simulation is O(2ⁿ); use tensor network or sampling-based methods for n>20
