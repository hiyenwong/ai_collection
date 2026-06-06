---
name: tsp-quantum-preprocessing
description: "Preprocessing methodology for combinatorial optimization (TSP and beyond) that reduces problem size by restricting candidate arcs to lowest-cost neighbors. Applicable to both classical solvers and quantum optimization frameworks (QAOA, quantum annealing)."
---

# TSP Quantum Preprocessing

## Description

Preprocessing strategy for combinatorial optimization problems that significantly reduces model size by restricting candidate edges/arcs to the k lowest-cost neighbors per vertex. Reduces decision variables from O(n²) to O(kn) while preserving solution quality. Evaluated with both classical solvers and quantum optimization techniques, showing improvements in computational time and optimality gaps.

## Activation Keywords
- TSP preprocessing
- quantum TSP
- candidate arc reduction
- combinatorial optimization preprocessing
- quantum preprocessing
- 旅行商问题预处理
- 量子组合优化

## Core Concepts

### k-Nearest Neighbor Arc Filtering

For a TSP with n cities:
- Original formulation: n(n-1) binary variables (all possible arcs)
- After preprocessing: n×k variables (only k nearest neighbors per city)
- Typical k: 5-15 (problem-dependent)

### Subtour Elimination Preservation

The preprocessing maintains subtour elimination constraints (MTZ or DFJ) on the reduced graph. The key insight: optimal tours rarely use edges that are not among the k-nearest neighbors.

### Quantum Optimization Benefits

1. **Reduced qubit count**: Fewer binary variables → fewer qubits needed
2. **Sparser coupling graph**: Fewer constraints → easier embedding
3. **Faster convergence**: Smaller search space → fewer QAOA iterations
4. **Lower chain breaks**: Less dense logical graph → better minor embedding

## Usage Patterns

### Pattern 1: Classical Preprocessing for Quantum Optimization

1. Compute pairwise distance/cost matrix for all n nodes
2. For each node, select k nearest neighbors (k = O(log n) or problem-specific)
3. Build reduced cost matrix with only selected edges
4. Formulate QUBO/Ising model on reduced graph
5. Solve with QAOA, quantum annealing, or classical solver

### Pattern 2: Adaptive k Selection

1. Start with small k (e.g., k=3)
2. Solve and check solution quality
3. If infeasible (no valid tour found): increment k
4. Repeat until feasible solution found
5. The optimal k balances solution quality vs. computational cost

### Pattern 3: Extension Beyond TSP

Applicable to any graph optimization problem:
- Vehicle Routing Problem (VRP)
- Steiner Tree Problem
- Facility Location
- Network Design

For each, define the "neighbor" relationship appropriate to the problem structure.

## Tools Used
- networkx: Graph construction, k-NN computation
- qiskit/dwave: Quantum optimization solvers
- gurobi/cplex: Classical baseline comparison
- numpy: Distance matrix computation

## Error Handling

### No Feasible Solution Found
- Symptom: Reduced graph has no valid solution
- Fix: Increase k, check if original problem is feasible
- Recovery: Fall back to full graph formulation

### Preprocessing Removes Optimal Edge
- Symptom: Optimal solution uses edges not in k-NN set
- Fix: Use adaptive k with iterative refinement
- Alternative: Add a small set of "long-range" edges strategically

### Quantum Embedding Still Fails After Preprocessing
- Symptom: Even reduced graph too dense for hardware
- Fix: Further reduce k, or use QAOA instead of quantum annealing

## Examples

### Example 1: TSP on 100-City Instance

Original: 100×99 = 9900 binary variables
Preprocessed (k=10): 100×10 = 1000 binary variables (90% reduction)

Results on TSPLIB benchmarks:
- Classical solver (Gurobi): 3x faster on preprocessed instance
- QAOA: Feasible embedding on hardware (was infeasible before)
- Optimality gap: < 2% for k≥8

## Resources

- arXiv:2603.23290 - Traveling Salesman Problem with a Preprocessing Method for Classical and Quantum Optimization
- TSPLIB benchmark instances
- QAOA literature (Farhi et al.)

## Related Skills

- quantum-optimization-qaoa
- quantum-computing-patterns
- qbalance-quantum-workflow-optimization
