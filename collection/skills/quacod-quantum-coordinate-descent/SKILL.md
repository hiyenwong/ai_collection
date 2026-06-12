---
name: quacod-quantum-coordinate-descent
description: "Quantum Optimization via Coordinate Descent (QUACOD) methodology. Decomposes large-scale combinatorial optimization problems into quantum-solvable subproblems using coordinate descent, enabling NISQ-era hardware to handle problems 5-35x larger than direct quantum approaches. Use when: (1) optimization problems exceed available qubits, (2) scaling quantum optimization to practical problem sizes, (3) drone scheduling/logistics optimization, (4) iterative quantum-classical hybrid optimization workflows."
---

# QUACOD: Quantum Optimization via Coordinate Descent

Decomposes large-scale combinatorial optimization problems into quantum-solvable subproblems using coordinate descent, enabling NISQ-era quantum hardware to handle problems significantly larger than direct quantum approaches.

## Core Idea

Instead of encoding the entire problem onto a quantum circuit (limited by qubit count), QUACOD:
1. Formulates the full problem as a QUBO/Ising model
2. Identifies variable subsets (coordinates) within qubit budget
3. Solves each subproblem using quantum optimization (QAOA/VQE)
4. Iterates coordinate descent until convergence
5. Uses hardware-efficient circuits for practical execution

## Workflow

### Step 1: Problem Formulation

Express the optimization problem as QUBO:

$$\min_x x^T Q x + c^T x, \quad x \in \{0, 1\}^n$$

Where $n$ is the total number of binary variables (can be >> available qubits).

### Step 2: Coordinate Partitioning

Partition variables into blocks $B_1, B_2, \ldots, B_k$ where each $|B_i| \leq q$ (available qubits).

Strategy: Group correlated variables together, or use random/sequential partitioning.

### Step 3: Quantum Subproblem Solving

For each block $B_i$, fix all other variables and solve:

$$\min_{x_{B_i}} x_{B_i}^T Q_{B_i} x_{B_i} + (Q_{B_i, \text{rest}} x_{\text{rest}} + c_{B_i})^T x_{B_i}$$

Using quantum optimization:
- QAOA with hardware-efficient ansatz
- VQE with problem-specific ansatz
- Quantum annealing (if available)

### Step 4: Iteration & Convergence

Cycle through all blocks, updating the solution after each quantum solve.
Stop when solution converges or max iterations reached.

## Implementation Pattern

```python
import numpy as np
from qiskit.algorithms import QAOA
from qiskit.primitives import Sampler

def quacod(Q, c, qubit_budget, max_iter=10, block_size=None):
    """QUACOD: Quantum Optimization via Coordinate Descent.
    
    Args:
        Q: QUBO matrix (n x n)
        c: Linear coefficients (n,)
        qubit_budget: Maximum qubits per subproblem
        max_iter: Maximum coordinate descent iterations
        block_size: Size of coordinate blocks (default: qubit_budget)
    
    Returns:
        x: Optimal binary solution
        history: Solution trajectory
    """
    n = len(c)
    x = np.random.randint(0, 2, n)
    history = [x.copy()]
    
    if block_size is None:
        block_size = qubit_budget
    
    for iteration in range(max_iter):
        # Partition variables into blocks
        blocks = [list(range(i, min(i + block_size, n))) 
                  for i in range(0, n, block_size)]
        
        converged = True
        for block in blocks:
            rest = [j for j in range(n) if j not in block]
            
            # Build subproblem QUBO for this block
            Q_block = Q[np.ix_(block, block)]
            # Effective linear term from fixed variables
            c_block = c[block] + 2 * Q[np.ix_(block, rest)] @ x[rest]
            
            # Solve subproblem with quantum optimizer
            x_new_block = quantum_solve_subproblem(Q_block, c_block)
            
            if not np.array_equal(x[block], x_new_block):
                x[block] = x_new_block
                converged = False
        
        history.append(x.copy())
        if converged:
            break
    
    return x, history


def quantum_solve_subproblem(Q, c):
    """Solve a QUBO subproblem using quantum optimization."""
    # Implement with QAOA, VQE, or quantum annealing
    # For small subproblems (within qubit budget)
    pass
```

## Key Advantages

| Metric | Direct Quantum | QUACOD |
|--------|---------------|--------|
| Max variables | ~100 (qubit limit) | 500+ (5x more drones) |
| Max routes | ~50 | 1,750+ (35x more) |
| Circuit depth | Deep (full problem) | Shallow (subproblems) |
| NISQ feasible | Limited | Practical |

## Use Cases

1. **Drone Scheduling**: Route optimization with limited qubits
2. **Portfolio Optimization**: Large-scale financial problems
3. **Logistics**: Vehicle routing, job shop scheduling
4. **Graph Problems**: Max-Cut, vertex coloring on large graphs
5. **Any QUBO problem** exceeding available quantum resources

## Activation Keywords

- quacod
- quantum coordinate descent
- quantum optimization scaling
- large-scale qubo
- iterative quantum optimization
- drone scheduling quantum
- 坐标下降量子优化
- 大规模量子优化

## References

- Paper: arXiv:2605.14001
- Authors: Nguyen et al.
- Key finding: Hardware-efficient circuits effective for coordinate descent subproblems
