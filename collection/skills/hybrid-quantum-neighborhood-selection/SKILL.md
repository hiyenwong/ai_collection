---
name: hybrid-quantum-neighborhood-selection
description: "Hybrid Quantum Neighborhood Selection (HQNS) — resource-efficient framework for large-scale combinatorial optimization. Decomposes dense QUBO into bounded-width quantum subproblems via stochastic frontier selection. Preserves 99.99% solution quality while reducing wall-clock time 94.91%, CPU 64.68%, memory 88.61%. QPU execution bounded at 6-7s regardless of global problem scale."
---

# Hybrid Quantum Neighborhood Selection (HQNS)

## Core Problem

Large dense QUBO formulations cause:
- **Huge memory footprints** (O(N²) storage for N variables)
- **High CPU utilization** during classical optimization
- **Long execution times** scaling with problem size
- **QPU limitations** — near-term processors can't handle large QUBOs directly

## HQNS Solution

Decompose large dense QUBO into **bounded-width quantum subproblems** via **stochastic frontier selection**:

```
Global QUBO (N variables)
    │
    ▼
┌─────────────────────┐
│ Stochastic Frontier  │  ← Select bounded subset (F variables, F << N)
│ Selection            │
└─────────┬───────────┘
          ▼
┌─────────────────────┐
│ QPU Subproblem       │  ← Solve F-variable QUBO on quantum processor
│ (bounded width F)    │  ← Execution time: constant O(1) in N
└─────────┬───────────┘
          ▼
┌─────────────────────┐
│ Update & Iterate     │  ← Incorporate solution, select new frontier
└─────────────────────┘
```

## Implementation Pattern

```python
def hqns_optimize(qubo_matrix, n_iterations=100, frontier_size=20, 
                   quantum_solver=None, classical_solver=None):
    """Hybrid Quantum Neighborhood Selection optimization.
    
    Args:
        qubo_matrix: N×N QUBO matrix (dense)
        n_iterations: Number of HQNS iterations
        frontier_size: Fixed size of quantum subproblem (F)
        quantum_solver: QPU solver function
        classical_solver: Classical fallback/initialization
    
    Returns:
        best_solution: Best binary assignment found
        best_energy: Corresponding QUBO energy
    """
    N = qubo_matrix.shape[0]
    current_solution = np.random.randint(0, 2, N)  # or classical init
    best_solution = current_solution.copy()
    best_energy = compute_energy(qubo_matrix, current_solution)
    
    for iteration in range(n_iterations):
        # 1. Stochastic Frontier Selection
        # Select F variables based on contribution to objective
        frontier = select_frontier(
            qubo_matrix, current_solution, frontier_size,
            method='stochastic_contribution'
        )
        
        # 2. Extract subproblem
        sub_qubo = qubo_matrix[np.ix_(frontier, frontier)]
        
        # 3. Fix boundary conditions from current solution
        fixed_vars = [i for i in range(N) if i not in frontier]
        boundary_terms = compute_boundary_terms(
            qubo_matrix, current_solution, frontier, fixed_vars
        )
        
        # 4. Solve subproblem on QPU
        sub_solution = quantum_solver(sub_qubo + boundary_terms)
        
        # 5. Update global solution
        for i, idx in enumerate(frontier):
            current_solution[idx] = sub_solution[i]
        
        # 6. Track best
        energy = compute_energy(qubo_matrix, current_solution)
        if energy < best_energy:
            best_energy = energy
            best_solution = current_solution.copy()
    
    return best_solution, best_energy

def select_frontier(qubo, current_sol, size, method='stochastic_contribution'):
    """Select frontier variables stochastically based on contribution."""
    # Compute per-variable contribution to objective
    contributions = np.abs(qubo @ current_sol)
    
    # Stochastic selection weighted by contribution
    probs = contributions / contributions.sum()
    frontier = np.random.choice(
        len(current_sol), size=size, replace=False, p=probs
    )
    return frontier

def compute_boundary_terms(qubo, current_sol, frontier, fixed_vars):
    """Compute linear boundary terms from fixed variables."""
    boundary = np.zeros(len(frontier))
    for i, fv in enumerate(frontier):
        for j in fixed_vars:
            boundary[i] += 2 * qubo[fv, j] * current_sol[j]
    return np.diag(boundary)
```

## Key Innovation: Decoupled QPU Scaling

| Metric | Classical Baseline | HQNS |
|--------|-------------------|------|
| Wall-clock time | 100% | **5.09%** (94.91% reduction) |
| Peak CPU | 100% | **35.32%** (64.68% reduction) |
| Peak Memory | 100% | **11.39%** (88.61% reduction) |
| QPU time | N/A | **6-7s** (constant, independent of N) |
| Solution quality | 100% | **99.9908%** of baseline |

The QPU execution time is **decoupled from the global QUBO dimension** when frontier size is fixed.

## When to Use

- Large-scale combinatorial optimization (N > 100)
- Dense QUBO formulations where full quantum solution isn't feasible
- Resource-constrained environments (memory, CPU, QPU time limits)
- Problems where near-optimal solutions are acceptable
- Hybrid quantum-classical pipelines on NISQ hardware

## Activation
hqns, hybrid quantum neighborhood, stochastic frontier, qubo decomposition, quantum optimization, resource-efficient quantum, large-scale combinatorial