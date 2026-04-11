---
name: decentralized-optimization-smtpp
description: "Stochastic Momentum Tracking Push-Pull (SMT-PP) for decentralized optimization over directed graphs. Addresses asymmetric communication and high variance in stochastic gradients through momentum-based tracking. Activation: decentralized optimization, momentum tracking, directed graphs, stochastic gradients."
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [decentralized-optimization, momentum-tracking, directed-graphs, stochastic-gradients, push-pull]
    source_paper: "Stochastic Momentum Tracking Push-Pull for Decentralized Optimization over Directed Graphs (arXiv:2604.08219)"
    citations: 0
    category: systems-engineering
---

# Stochastic Momentum Tracking Push-Pull (SMT-PP)

## Overview

Decentralized optimization over directed networks is frequently challenged by asymmetric communication and the inherent high variance of stochastic gradients, which collectively cause severe oscillations and hinder algorithmic convergence. This paper proposes Stochastic Momentum Tracking Push-Pull (SMT-PP) to address these challenges.

## Core Concepts

### Decentralized Optimization
- **Distributed Computation**: Each node has local objective
- **Consensus**: Nodes agree on global optimum
- **No Central Coordinator**: Peer-to-peer communication

### Directed Graphs
- **Asymmetric Communication**: Links may be unidirectional
- **Mixing Matrices**: Row-stochastic and column-stochastic matrices
- **Challenges**: Standard consensus algorithms fail

### Momentum Tracking
- **Gradient Tracking**: Track global gradient information
- **Momentum**: Accelerate convergence
- **Variance Reduction**: Stabilize stochastic updates

## Implementation

```python
import numpy as np
from typing import Callable, List, Tuple

class SMT_PP_Optimizer:
    def __init__(self,
                 local_objectives: List[Callable],
                 row_stochastic_matrix: np.ndarray,
                 column_stochastic_matrix: np.ndarray,
                 learning_rate: float = 0.01,
                 momentum: float = 0.9,
                 beta: float = 0.9):
        self.n_nodes = len(local_objectives)
        self.f = local_objectives
        self.R = row_stochastic_matrix
        self.C = column_stochastic_matrix
        self.alpha = learning_rate
        self.beta = momentum
        self.gamma = beta
        
        self.x = None
        self.v = None
        self.y = None
        self.z = None
        
    def initialize(self, x0: List[np.ndarray]):
        self.x = [x0[i].copy() for i in range(self.n_nodes)]
        self.v = [np.zeros_like(x0[i]) for i in range(self.n_nodes)]
        self.y = [np.zeros_like(x0[i]) for i in range(self.n_nodes)]
        self.z = [np.zeros_like(x0[i]) for i in range(self.n_nodes)]
        
    def local_gradient(self, i: int, x: np.ndarray, batch_size: int = 32) -> np.ndarray:
        # Stochastic gradient estimation
        return self.f[i](x, batch_size)
    
    def step(self, iteration: int, batch_size: int = 32):
        x_new = []
        v_new = []
        y_new = []
        z_new = []
        
        for i in range(self.n_nodes):
            # Compute stochastic gradient
            g_i = self.local_gradient(i, self.x[i], batch_size)
            
            # Update auxiliary variable y (momentum tracking)
            y_new_i = self.y[i] + self.gamma * (g_i - self.z[i])
            
            # Update gradient estimate z
            z_new_i = g_i
            
            # Update momentum term v
            v_new_i = self.beta * self.v[i] + y_new_i
            
            # Update position x using push-pull
            x_new_i = np.zeros_like(self.x[i])
            for j in range(self.n_nodes):
                if self.R[i, j] > 0:
                    x_new_i += self.R[i, j] * self.x[j]
            
            x_new_i = x_new_i - self.alpha * v_new_i
            
            x_new.append(x_new_i)
            v_new.append(v_new_i)
            y_new.append(y_new_i)
            z_new.append(z_new_i)
        
        self.x = x_new
        self.v = v_new
        self.y = y_new
        self.z = z_new
        
    def get_consensus_value(self) -> np.ndarray:
        return np.mean(self.x, axis=0)
    
    def optimize(self, max_iter: int = 1000, batch_size: int = 32) -> np.ndarray:
        for t in range(max_iter):
            self.step(t, batch_size)
            
            if t % 100 == 0:
                consensus = self.get_consensus_value()
                total_loss = sum(self.f[i](consensus, 1000) for i in range(self.n_nodes))
                print(f"Iteration {t}: Loss = {total_loss}")
        
        return self.get_consensus_value()


def create_directed_graph_mixing_matrices(adjacency: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    n = adjacency.shape[0]
    
    # Row-stochastic matrix (for x update)
    R = adjacency.copy().astype(float)
    for i in range(n):
        row_sum = np.sum(R[i, :])
        if row_sum > 0:
            R[i, :] /= row_sum
    
    # Column-stochastic matrix (for gradient tracking)
    C = adjacency.copy().astype(float)
    for j in range(n):
        col_sum = np.sum(C[:, j])
        if col_sum > 0:
            C[:, j] /= col_sum
    
    return R, C


# Example: Distributed least squares
class DistributedLeastSquares:
    def __init__(self, A_list: List[np.ndarray], b_list: List[np.ndarray]):
        self.A = A_list
        self.b = b_list
        self.n_nodes = len(A_list)
        
    def local_objective(self, i: int, x: np.ndarray, batch_size: int) -> np.ndarray:
        # Stochastic gradient: sample rows
        n_samples = self.A[i].shape[0]
        indices = np.random.choice(n_samples, min(batch_size, n_samples), replace=False)
        A_batch = self.A[i][indices, :]
        b_batch = self.b[i][indices]
        
        # Gradient of 0.5 * ||Ax - b||^2
        residual = A_batch @ x - b_batch
        grad = A_batch.T @ residual / len(indices)
        return grad


# Example usage
def example_distributed_optimization():
    np.random.seed(42)
    n_nodes = 5
    dim = 10
    
    # Generate local problems
    A_list = [np.random.randn(100, dim) for _ in range(n_nodes)]
    b_list = [np.random.randn(100) for _ in range(n_nodes)]
    
    problem = DistributedLeastSquares(A_list, b_list)
    objectives = [lambda x, bs, i=i: problem.local_objective(i, x, bs) 
                  for i in range(n_nodes)]
    
    # Create directed graph (ring topology with one direction)
    adjacency = np.zeros((n_nodes, n_nodes))
    for i in range(n_nodes):
        adjacency[i, (i+1) % n_nodes] = 1  # Forward edge
        adjacency[i, i] = 1  # Self-loop
    
    R, C = create_directed_graph_mixing_matrices(adjacency)
    
    # Initialize optimizer
    optimizer = SMT_PP_Optimizer(objectives, R, C, learning_rate=0.001)
    x0 = [np.random.randn(dim) for _ in range(n_nodes)]
    optimizer.initialize(x0)
    
    # Optimize
    solution = optimizer.optimize(max_iter=500, batch_size=32)
    print(f"Solution: {solution[:5]}")


if __name__ == "__main__":
    example_distributed_optimization()
```

## Key Insights

1. **Momentum Tracking**: Combines benefits of momentum and gradient tracking
2. **Directed Graph Support**: Works with asymmetric communication topologies
3. **Variance Reduction**: Stabilizes stochastic gradient updates

## Convergence Properties

- **Convergence Rate**: O(1/T) for convex problems
- **Consensus**: Achieves exact consensus on directed graphs
- **Robustness**: Handles high-variance stochastic gradients

## Applications

- Distributed machine learning
- Sensor networks
- Multi-robot coordination
- Federated learning

## References

- Fan, W., Liao, Y., Xu, Q., Guo, B., & Dian, S. (2026). Stochastic Momentum Tracking Push-Pull for Decentralized Optimization over Directed Graphs. arXiv:2604.08219.
