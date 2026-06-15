---
name: pubo-mst-falqon
description: PUBO formulation for Minimum Spanning Tree using FALQON quantum optimization methodology. Reformulates MST as Polynomial Unconstrained Binary Optimization without auxiliary variables, reducing qubit requirements. Use when solving graph optimization problems (MST, OPF classifiers, network design) on quantum or quantum-inspired hardware, especially when qubit count is constrained. Applies to quantum machine learning pipelines needing efficient combinatorial optimization, graph-based classifiers, and prototype selection.
---

# PUBO-MST via FALQON

Methodology from Pexe et al. (arXiv:2605.20637, May 2026).

## Problem

Minimum Spanning Tree (MST) computation becomes prohibitive for large-scale datasets, especially in graph-based classifiers like Optimum-Path Forest (OPF) where MST-derived prototypes define decision boundaries.

## Solution

Reformulate MST as a Polynomial Unconstrained Binary Optimization (PUBO) problem and solve using FALQON (Feedback-Based Quantum Optimization) — a feedback-driven quantum algorithm that doesn't require classical outer-loop optimization.

### Key Innovation

- **No auxiliary variables** needed (unlike QUBO formulations)
- **Fewer qubits** required — direct binary encoding of edge selection
- **FALQON** replaces variational optimization with real-time feedback

## PUBO Formulation

The MST problem is encoded as minimizing:

```
H = H_connectivity + λ · H_cardinality + μ · H_cycle
```

Where:
- `H_connectivity`: ensures all nodes are connected (sum of edge weights)
- `H_cardinality`: enforces exactly n-1 edges for n nodes
- `H_cycle`: penalizes cycles in the selected subgraph

### Binary Variables

`x_e ∈ {0, 1}` for each edge e — 1 if edge is included, 0 otherwise.

Unlike QUBO, PUBO allows higher-order terms directly, eliminating the need for auxiliary variables to reduce polynomial degree.

## FALQON Algorithm

FALQON is a feedback-based quantum optimization algorithm:

```
For each layer k:
  β_k = ⟨ψ_k| [H_mix, H_prob] |ψ_k⟩  (feedback signal)
  |ψ_{k+1}⟩ = e^{-iβ_k H_mix Δt} e^{-i H_prob Δt} |ψ_k⟩
```

Key properties:
- No classical optimizer needed (unlike QAOA/VQE)
- Feedback signal β_k is measured from quantum state
- Converges toward ground state of problem Hamiltonian

## Implementation Workflow

### 1. Formulate PUBO

```python
def mst_pubo(graph):
    """Convert MST to PUBO formulation.
    
    Returns: H = connectivity + λ·cardinality + μ·cycle_penalty
    Variables: x_e for each edge
    """
    n = len(graph.nodes)
    edges = list(graph.edges)
    
    # Connectivity: sum of edge weights for selected edges
    H_connect = sum(w_e * x_e for e, w_e in graph.edge_weights())
    
    # Cardinality: exactly n-1 edges
    H_card = (sum(x_e for e in edges) - (n - 1)) ** 2
    
    # Cycle penalty: penalize any cycle in selected edges
    H_cycle = sum(cycle_penalty(cycle, x_vars) 
                  for cycle in find_all_cycles(graph))
    
    return H_connect + λ * H_card + μ * H_cycle
```

### 2. Execute FALQON

```python
def falqon(H_problem, H_mix, n_layers, dt=0.01):
    """Feedback-Based Quantum Optimization."""
    state = uniform_superposition(n_qubits)
    betas = []
    
    for k in range(n_layers):
        # Measure feedback signal
        beta_k = expectation_value(state, commutator(H_mix, H_problem))
        betas.append(beta_k)
        
        # Apply evolution
        state = evolve(state, H_problem, dt)
        state = evolve(state, H_mix, beta_k * dt)
    
    return state, betas
```

### 3. Extract Solution

```python
def extract_mst(measurement_counts, edges):
    """Extract MST from FALQON measurement results."""
    # Most frequently measured bitstring
    best_bitstring = max(measurement_counts, key=measurement_counts.get)
    selected_edges = [e for i, e in enumerate(edges) 
                      if best_bitstring[i] == '1']
    return selected_edges
```

## Results

- FALQON-optimized MST achieves accuracies **comparable to classical Prim's algorithm**
- Maintains prototype quality for OPF classification
- Occasionally reaches local minima but accuracy impact is minimal
- Reduces qubit count vs. QUBO formulations (no auxiliary variables)

## When to Use

- Graph optimization on quantum/quantum-inspired hardware
- Qubit count is a bottleneck for QUBO formulations
- Need variational-free quantum optimization
- OPF classifiers on large datasets
- Network design, clustering, or prototype selection

## Comparison

| Method | Qubits | Classical Optimizer | Accuracy |
|--------|--------|---------------------|----------|
| QUBO + QAOA | n_edges + n_aux | Yes (outer loop) | High |
| **PUBO + FALQON** | **n_edges only** | **No** | **Comparable** |
| Classical Prim | N/A | N/A | Exact |

## Pitfalls

- FALQON may converge to local minima — monitor convergence
- Cycle penalty formulation grows exponentially with graph size
- Best suited for moderate-sized graphs on current hardware
- Parameter tuning (λ, μ, Δt, n_layers) affects convergence

## Activation

quantum MST, PUBO optimization, FALQON, quantum graph algorithms, optimum-path forest, quantum combinatorial optimization, QML classifier, feedback-based quantum optimization, graph prototype selection
