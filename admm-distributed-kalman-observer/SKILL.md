---
name: admm-distributed-kalman-observer
description: "ADMM-Based Distributed Kalman-like Observer methodology for multi-agent systems state estimation. Implements information-form Kalman filtering with exponential forgetting factor and partition-based ADMM correction. Provides sparsity-preserving prediction, distributed QP solving, and UGES stability guarantee via two-time-scale analysis. Use for: cooperative localization, distributed state estimation in multi-agent systems, sensor networks, robot swarm localization, distributed power network state estimation."
---

# ADMM-Based Distributed Kalman-like Observer

Distributed state estimation framework for multi-agent systems with local and relative measurements, using information-form Kalman filtering with ADMM-based distributed correction.

## Source Paper

**Title:** ADMM-Based Distributed Kalman-like Observer with Applications to Cooperative Localization  
**Authors:** Nicola De Carli, Nicola Bastianello, Dimos V. Dimarogonas  
**arXiv:** 2604.21608v1 [eess.SY]  
**Date:** April 23, 2026  
**Institution:** KTH Royal Institute of Technology, Stockholm, Sweden

## Core Problem

Distributed state estimation for multi-agent systems where:
- Global state dimension scales with network size N
- Agents have local measurements (depending only on own state)
- Agents have relative measurements (involving neighboring agents)
- Centralized approaches become intractable as N grows

## Mathematical Framework

### System Model

```
x_{i,k+1} = A_{i,k} x_{i,k} + B_{i,k} u_{i,k},    i ∈ V = {1,...,N}
```

**Graphs:**
- Sensing graph G_s = (V, E_s): directed, edge (i,j) means relative measurement
- Communication graph G_c = (V, E_c): undirected, bidirectional information exchange

**Measurements:**
- Local: y^ℓ_{i,k} = H^ℓ_{i,k} x_{i,k}
- Relative: y^r_{ij,k} = H^r_{ij,i,k} x_{i,k} + H^r_{ij,j,k} x_{j,k}

### Information-Form Representation

```
S_{k|k-1} := P_{k|k-1}^{-1}          (information matrix)
z_{k|k-1} := S_{k|k-1} x̂_{k|k-1}    (information vector)
```

### Key Innovation 1: Sparsity-Preserving Prediction

**Standard prediction** (destroys sparsity):
```
S_{k+1|k} = (A_k S_{k|k}^{-1} A_k^⊤ + Q_k)^{-1}  → becomes dense
```

**Proposed prediction** (preserves sparsity):
```
S_{k+1|k} = γ A_k^{-⊤} S_{k|k} A_k^{-1},    0 < γ < 1
```

Since A_k is block-diagonal, the sparsity pattern of S_{k|k} is preserved.

### Key Innovation 2: Distributed ADMM Correction

Correction formulated as sparse SPD linear system:
```
S_{k|k} ξ_k = b_k,    where ξ_k = (1/ε)(x̂_{k|k} - x̂_{k|k-1})
```

Solved via partition-based ADMM with local communication only.

## Implementation

```python
import numpy as np
from scipy import sparse

class ADMMDistributedKalmanObserver:
    """
    Distributed Kalman-like observer using ADMM for correction.
    
    Based on: De Carli et al., "ADMM-Based Distributed Kalman-like 
    Observer with Applications to Cooperative Localization", 2026.
    """
    
    def __init__(self, num_agents, state_dim, gamma=0.9, epsilon=0.5, rho=1.0):
        self.N = num_agents
        self.d = state_dim
        self.gamma = gamma      # forgetting factor
        self.epsilon = epsilon  # correction gain
        self.rho = rho          # ADMM penalty
        
        # Initialize per-agent data
        self.S = {}  # information matrices
        self.z = {}  # information vectors
        self.x_hat = {}  # state estimates
        
    def initialize_agent(self, agent_id, x0, P0):
        """Initialize an agent with initial state and covariance"""
        S0 = np.linalg.inv(P0)
        self.S[agent_id] = {
            'self': S0,
            'neighbors': {}
        }
        self.z[agent_id] = S0 @ x0
        self.x_hat[agent_id] = x0
        
    def predict(self, agent_id, A, B, u, neighbors):
        """
        Sparsity-preserving prediction step.
        
        Args:
            agent_id: Agent identifier
            A: State transition matrix
            B: Input matrix
            u: Control input
            neighbors: List of neighbor agent IDs
        """
        A_inv = np.linalg.inv(A)
        
        # Update own information matrix
        S_self_old = self.S[agent_id]['self']
        self.S[agent_id]['self'] = self.gamma * A_inv.T @ S_self_old @ A_inv
        
        # Update neighbor coupling matrices
        for neighbor_id in neighbors:
            if neighbor_id in self.S[agent_id]['neighbors']:
                S_coupling = self.S[agent_id]['neighbors'][neighbor_id]
                # Note: A_neighbor would be retrieved from neighbor
                A_n = self._get_neighbor_dynamics(neighbor_id)
                self.S[agent_id]['neighbors'][neighbor_id] = (
                    self.gamma * A_inv.T @ S_coupling @ np.linalg.inv(A_n)
                )
        
        # State prediction
        self.x_hat[agent_id] = A @ self.x_hat[agent_id] + B @ u
        self.z[agent_id] = self.S[agent_id]['self'] @ self.x_hat[agent_id]
        
    def admm_correction(self, agent_id, y_local, H_local, R_local, 
                        neighbors, max_iter=10):
        """
        Distributed correction via ADMM.
        
        Args:
            agent_id: Agent identifier
            y_local: Local measurement
            H_local: Measurement matrix
            R_local: Measurement noise covariance
            neighbors: List of neighbor IDs for communication
            max_iter: Maximum ADMM iterations
            
        Returns:
            Updated state estimate
        """
        # Compute local innovation term
        innovation = y_local - H_local @ self.x_hat[agent_id]
        R_inv = np.linalg.inv(R_local)
        b = H_local.T @ R_inv @ innovation
        
        S_kk = self.S[agent_id]['self']
        
        # Initialize ADMM variables
        xi = np.zeros(self.d)
        lambda_dual = np.zeros(self.d)
        
        # ADMM iterations
        for iteration in range(max_iter):
            # Local primal update
            xi_new = np.linalg.solve(
                S_kk + self.rho * np.eye(self.d),
                b + self.rho * (xi - lambda_dual)
            )
            
            # Exchange with neighbors and average
            neighbor_xis = self._exchange_with_neighbors(agent_id, xi_new, neighbors)
            xi_avg = np.mean([xi_new] + neighbor_xis, axis=0)
            
            # Dual update
            lambda_dual = lambda_dual + xi_new - xi_avg
            
            xi = xi_new
        
        # Apply correction
        self.x_hat[agent_id] = self.x_hat[agent_id] + self.epsilon * xi
        self.z[agent_id] = self.S[agent_id]['self'] @ self.x_hat[agent_id]
        
        return self.x_hat[agent_id]
    
    def _get_neighbor_dynamics(self, neighbor_id):
        """Retrieve neighbor's dynamics matrix (placeholder)"""
        # In practice, this would come from network communication
        pass
    
    def _exchange_with_neighbors(self, agent_id, xi, neighbors):
        """Exchange variables with neighbors (placeholder)"""
        # In practice, this involves network communication
        return [np.zeros(self.d) for _ in neighbors]
```

## Two-Time-Scale Stability Analysis

### System Decomposition

The interconnected observer separates into:

1. **Slow subsystem** (estimation error dynamics):
   ```
   e_{k+1} = (I - ε S_{k|k}^{-1} Y_k) A_k e_k + noise
   ```
   - Uniformly exponentially stable under observability

2. **Fast subsystem** (ADMM dynamics):
   ```
   ξ^{(t+1)} = ξ^{(t)} - α ∇f(ξ^{(t)})
   ```
   - Exponentially stable for strongly convex QP

### Stability Theorem

Under standard assumptions (uniform boundedness, complete uniform observability, uniform invertibility), the overall distributed observer achieves **Uniform Global Exponential Stability (UGES)**.

## Comparison with Alternatives

| Method | Communication | Computation | Stability | Key Limitation |
|--------|--------------|-------------|-----------|----------------|
| Centralized KF | All-to-all | O(N³) | Optimal | Not scalable |
| Covariance Intersection | Local | O(d³) | Guaranteed | Conservative, underuses info |
| Consensus-based | Iterative | O(d³) | Limited | Requires consensus on global state |
| **ADMM Observer** | One-hop | O(d³) | UGES | Requires bounded ADMM iterations |

## Parameters

| Parameter | Symbol | Range | Effect |
|-----------|--------|-------|--------|
| Forgetting factor | γ | (0, 1) | Adaptation rate vs. stability |
| Correction gain | ε | (0, 1] | Observer correction magnitude |
| ADMM penalty | ρ | (0.1, 10) | Convergence speed |
| ADMM iterations | max_iter | 10-100 | Accuracy vs. computation |

## Applications

1. **Cooperative Localization**: Multi-robot teams with relative measurements
2. **Distributed Power Networks**: Smart grid state estimation
3. **Sensor Networks**: Environmental monitoring with local sensing
4. **UAV Swarms**: GPS-denied formation flying
5. **Autonomous Platoons**: Vehicle string stability

## References

De Carli, N., Bastianello, N., & Dimarogonas, D. V. (2026). ADMM-Based Distributed Kalman-like Observer with Applications to Cooperative Localization. arXiv:2604.21608v1 [eess.SY].
