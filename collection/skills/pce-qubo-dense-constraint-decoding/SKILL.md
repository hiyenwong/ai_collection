---
name: pce-qubo-dense-constraint-decoding
description: "Pauli Correlation Encoding (PCE) methodology for solving dense-constraint QUBO problems on quantum hardware. Use when: (1) encoding large QUBO problems onto few qubits using Pauli correlators, (2) decoding variational quantum circuit outputs for constrained optimization, (3) mRNA/protein structure prediction on quantum computers, (4) portfolio optimization, scheduling, or resource allocation as QUBOs, (5) IBM Heron / superconducting QPU deployment with SWAP-free compilation. Activation: PCE, Pauli Correlation Encoding, QUBO decoding, dense constraint QUBO, variational quantum optimization, problem-aware decoder, PAGD, quantum mRNA, quantum drug design."
---

# PCE for Dense-Constraint QUBO Decoding

Pauli Correlation Encoding (PCE) compresses m binary variables onto n=O(m^(1/k)) qubits by mapping to commuting Pauli correlators. This skill provides the end-to-end methodology for solving dense-constraint QUBOs on near-term quantum hardware.

## Core Concepts

### PCE Encoding
- Maps m binary QUBO variables onto n physical qubits via two-body Pauli correlations
- Each variable x_k encoded as expectation of P_qiqj ∈ {XiXj, YiYj, ZiZj} on a qubit pair
- Capacity: 3 * C(n,2) variables on n qubits
- Minimum qubits: 3*C(n*,2) ≥ m

### Problem-Aware Guided Decoder (PAGD)
Scores candidate variable commitments by:
1. **Marginal QUBO energy reduction** — how much does setting this variable reduce energy?
2. **Trained expectation-value prior** — what does the quantum circuit predict?
3. **Constraint-aware feasibility pruning** — reject infeasible assignments immediately

PAGD achieves 75-100% near-optimal recovery (P(gap<1%)) for m≤152 at K=100 restarts, vs 0-30% for sign-rounding baselines.

## Workflow

### Step 1: Formulate QUBO
Define the QUBO matrix Q and constraints. For mRNA secondary structure:
- Variables: quartet (stacked pair) x(i,j,i+1,j-1)
- Constraints: each base pairs at most once, no crossing pairs
- Energy: empirical thermodynamic data + penalty for constraint violation

### Step 2: Choose Ansatz Topology
Four options ranked by performance for dense QUBOs:
1. **Informed-k** (best) — problem-adapted pair budget captures relevant entangling structure
2. **NN** (nearest-neighbor) — good baseline, fewer parameters
3. **Informed-2k** — more pairs, may overload optimizer
4. **All** (fully-connected) — weakest for m≥120, COBYLA struggles on parameter count

### Step 3: Train with QUBO-Space Sigmoid Loss
Use the QUBO-space sigmoid loss (not Ising-space):
- Directly optimizes the same QUBO objective evaluated by the decoder
- Preserves QUBO penalty structure during training
- Layerwise parameterization: single Ry angle + single MS angle per layer

### Step 4: Decode with PAGD
```
PAGD(score) = marginal_energy_reduction × trained_EV_prior × feasibility_pruning
```
- Use K restarts (K=100-200 recommended)
- Best-of-K gap reported
- Trained prior gives advantage even at K=1 (no restarts needed)

### Step 5: Deploy on QPU
- Circuits transpile SWAP-free on IBM Heron processors
- 480 native two-qubit gates at depth 256 for 23-qubit instances
- QPU results match or beat simulator means

## Hardware Scale Results

| Instance | Variables | Qubits | Best Gap (QPU) |
|----------|-----------|--------|-----------------|
| 102 nt | 694 | 23 | 0.0% (exact CPLEX optimum at K=200) |
| 105 nt | 745 | 23 | Few-percent gap |

## Key Insights

1. **Trained prior advantage**: Largest at intermediate difficulty, diminishes on easy/hard instances
2. **Informed-k topology**: Best for m∈{120,152,195,240}, fully-connected All is weakest
3. **QUBO-space loss**: Principled default aligned with decoder, comparable to Ising-space
4. **Noise resilience**: PCE-trained priors survive transit to noisy superconducting hardware

## Applicable Domains
- mRNA/protein secondary structure prediction
- Portfolio optimization (250+ assets via iterative graph partitioning)
- Budget-constrained Min-Cut, TSP
- Scheduling, graph coloring, resource allocation
- Any dense-constraint QUBO (edge density 0.7-0.85)

## References
- arXiv:2605.20163 — PCE for mRNA secondary structure (Friedhoff et al., 2026)
- arXiv:2511.21305 — Large-scale portfolio optimization with PCE
- arXiv:2603.22399 — Quantum Wasserstein GAN for drug design (related quantum bio pipeline)
