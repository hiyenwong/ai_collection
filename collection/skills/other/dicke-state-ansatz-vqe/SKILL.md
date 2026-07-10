---
name: dicke-state-ansatz-vqe
description: "Feasibility-preserving mixed Dicke state ansatz for encoding equality and inequality constraints in variational quantum eigensolvers. Eliminates penalty terms by structurally encoding Hamming weight constraints into quantum circuits. Use when: (1) solving constrained combinatorial optimization with VQE/QAOA, (2) designing constraint-preserving ansatze, (3) eliminating penalty-based Lagrange multiplier tuning, (4) encoding equality/inequality constraints directly into quantum circuit structure. Activation: Dicke state, constrained VQE, penalty-free optimization, Hamming weight, ansatz design, combinatorial optimization"
metadata:
  arxiv_id: "2606.08504"
  published: "2026-06-07"
  authors: "J. V. S Scursulim"
  tags: ["dicke-state", "VQE", "combinatorial-optimization", "ansatz-design", "hamming-weight", "constraint-encoding", "penalty-free"]
---

# Dicke State Ansatz for Constrained VQE

## Core Methodology

Replaces penalty-based constraint handling in variational quantum algorithms with **structural constraint encoding** via Dicke states. The ansatz naturally lives in the feasible subspace, eliminating the need for penalty terms and Lagrange multiplier tuning.

### Key Innovations

1. **Mixed Dicke state ansatz**: Extends pure Dicke states via density matrix formalism to handle both equality and inequality constraints
2. **Penalty-free optimization**: Constraints are encoded in circuit structure, not added to the objective function
3. **Tensor product generalization**: Multiple constraint groups handled via tensor products of individual Dicke states
4. **Pure Dicke as special case**: Equality constraints recovered as special case of the mixed formulation

### How Dicke States Work

A Dicke state |D(n,k)⟩ is an equal superposition of all n-qubit computational basis states with Hamming weight k:

|D(n,k)⟩ = (1/√C(n,k)) Σ_{|x|=k} |x⟩

This naturally encodes "exactly k qubits must be 1" (equality constraint) into the quantum state.

### Mixed Dicke States for Inequality Constraints

The mixed state formalism extends to inequalities (e.g., "at most k" or "between k1 and k2") by forming appropriate density matrices over Dicke states of different weights.

## Agent Workflow

### Step 1: Identify Constraint Structure

For the optimization problem:
- Identify Hamming weight constraints (e.g., portfolio selection with exactly k assets)
- Classify as equality (exact k) or inequality (range of k values)
- Group constraints into independent sets

### Step 2: Construct Dicke State Circuit

For equality constraint (Hamming weight = k on n qubits):
1. Prepare initial Dicke state |D(n,k)⟩
2. Apply parameterized unitaries that preserve Hamming weight
3. These unitaries explore only the feasible subspace

For inequality constraint:
1. Use mixed Dicke state preparation
2. Density matrix spans the feasible weight range
3. Measurement samples from feasible distribution

### Step 3: Optimize Within Feasible Subspace

- The ansatz only generates feasible solutions — no infeasible samples
- Use classical optimizer (e.g., CMA-ES) to tune circuit parameters
- No penalty parameters to tune — the feasible space is hard-coded

### Step 4: Handle Multiple Constraints

For problems with multiple independent constraint groups:
- Construct Dicke state for each group
- Tensor product the individual Dicke states
- Apply group-preserving parameterized unitaries

## Implementation Patterns

### Pattern 1: Portfolio Optimization

For k-asset portfolio selection from n candidates:
- Prepare |D(n,k)⟩ as initial state
- Apply Hamming-weight-preserving mixers
- Measure to get valid k-asset portfolios

### Pattern 2: Multi-Group Constraints

For problems with multiple constraint types (e.g., k1 from group A, k2 from group B):
- Prepare |D(nA,k1)⟩ ⊗ |D(nB,k2)⟩
- Apply separate parameterized unitaries to each group
- Tensor product structure maintains independence

## Error Handling

### Hardware Noise
- Dicke state preparation circuits can be deep — use circuit optimization
- Consider noise-adaptive transpilation for NISQ devices
- Error mitigation techniques (zero-noise extrapolation) may be needed

### Large Hamming Weights
- State space grows as C(n,k) — optimization becomes harder for large n
- Consider symmetry reduction or problem decomposition for large instances

## Pitfalls

- **Dicke state preparation is non-trivial**: Efficient circuits for preparing |D(n,k)⟩ exist but require O(n) gates
- **Not all constraints are Hamming weight**: This method only works for constraints expressible as Hamming weight conditions on qubit subsets
- **Hardware experiments show noise sensitivity**: As noted in the paper, noise mitigation and transpilation remain challenges for practical deployment
