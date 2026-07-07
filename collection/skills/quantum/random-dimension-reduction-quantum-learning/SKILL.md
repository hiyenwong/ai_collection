---
name: random-dimension-reduction-quantum-learning
description: "Random dimension reduction procedure for quantum states that reduces dimensions while preserving properties invariant under tensor power action of isometries. Provides black-box method to replace dimension with max rank in sample complexity for learning symmetric properties, including multi-state estimation of distances, fidelities, and relative entropies."
metadata:
  arxiv_id: "2606.23592"
  published: "2026-06-22"
  authors: "Angus Lowe, Xinyu Tan"
  tags: [quantum-learning, dimension-reduction, state-tomography, symmetric-properties, sample-complexity]
---

# Random Dimension Reduction for Quantum States

## Core Concepts

A procedure that simultaneously reduces the dimension of many quantum states while preserving properties invariant under the tensor power action of an isometry. This enables sample-optimal learning of symmetric properties with complexity depending on **max rank** rather than **dimension**.

### Key Results

- **Dimension → Rank**: Sample complexity for symmetric properties depends on max rank of input states, not Hilbert space dimension
- **Full tomography after reduction**: yields improved upper bounds for estimating distances, fidelities, and relative entropies between state pairs
- **Efficient circuit**: implementable using the Schur transform
- **Connection to random purification**: Choi-Jamiolkowski representation reveals connection to Tang-Wright-Zhandry random purification channel

## Methodology

### Step 1: Random Dimension Reduction Procedure

For a collection of states {ρ₁, ..., ρₘ} on H_d:
1. Apply a random isometry V: H_d → H_r where r = max rank
2. Output reduced states {Vρ₁V†, ..., VρₘV†} on H_r
3. Symmetric properties are preserved under this mapping

### Step 2: Sample Complexity Reduction

For learning any symmetric property f(ρ₁, ..., ρₘ):
- **Before**: O(d²/ε²) samples
- **After reduction**: O(r²/ε²) samples where r = max rank(ρᵢ)
- When r ≪ d, this is an exponential improvement

### Step 3: Circuit Implementation

Implement via Schur transform:
1. Decompose (C^d)^{⊗n} using Schur-Weyl duality
2. Project onto irrep subspaces labeled by partitions
3. Extract reduced state on smaller representation space

## Usage Patterns

### Pattern 1: Low-Rank State Tomography

When target states are approximately low-rank (common in noisy quantum devices):
- Apply dimension reduction → full tomography on reduced space
- Achieves same accuracy with fewer samples

### Pattern 2: Multi-State Property Estimation

For comparing multiple quantum states:
- Distance estimation: ||ρ - σ||₁
- Fidelity estimation: F(ρ, σ)
- Relative entropy: S(ρ||σ)
All benefit from rank-dependent rather than dimension-dependent scaling

### Pattern 3: Quantum Learning with Symmetry

Any learning task with permutational symmetry in the samples:
- State discrimination
- Property testing
- Quantum hypothesis testing

## Pitfalls

- **Only symmetric properties**: The reduction preserves only properties invariant under U^{⊗n} action
- **Rank estimation**: Requires prior knowledge or estimation of max rank
- **Schur transform cost**: O(n² log² d) gates for n copies on d-dimensional space

## Activation Keywords

- random dimension reduction quantum
- quantum state tomography sample complexity
- symmetric property estimation quantum
- Schur transform state learning
- quantum fidelity estimation rank
- quantum dimension reduction
- 量子态降维学习
