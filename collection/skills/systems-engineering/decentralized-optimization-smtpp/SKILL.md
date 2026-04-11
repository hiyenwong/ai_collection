---
name: decentralized-optimization-smtpp
description: "Stochastic Momentum Tracking Push-Pull (SMTPP) for decentralized optimization over directed graphs. Addresses asymmetric communication and stochastic gradient variance in distributed machine learning."
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [decentralized-optimization, distributed-machine-learning, push-pull, directed-graphs, stochastic-momentum, consensus]
    source_paper: "Stochastic Momentum Tracking Push-Pull for Decentralized Optimization over Directed Graphs (arXiv:2604.08219v1)"
    authors: "Wenqi Fan, Yiwei Liao, Qing Xu, Bin Guo, Songyi Dian"
    published: "2026-04-09"
    category: "optimization and control"
---

# Stochastic Momentum Tracking Push-Pull for Decentralized Optimization

## Overview

This skill implements the Stochastic Momentum Tracking Push-Pull (SMTPP) algorithm for decentralized optimization over directed graphs. The method addresses two key challenges in distributed machine learning: asymmetric communication patterns and high variance in stochastic gradients.

## Core Concepts

### 1. Decentralized Optimization
- **Setting**: Multiple agents cooperatively optimize a global objective
- **Challenge**: No central coordinator, limited communication
- **Approach**: Local computation + neighbor communication

### 2. Directed Graph Communication
- **Problem**: Communication may be asymmetric
- **Solution**: Push-Pull mechanism for information diffusion
- **Benefit**: Works on arbitrary directed topologies

### 3. Momentum Tracking
- **Issue**: Stochastic gradients have high variance
- **Solution**: Track momentum across the network
- **Result**: Faster convergence and stable optimization

## Mathematical Framework

### SMTPP Algorithm
```
At each agent i and iteration k:

1. Local gradient:
   g_i^k = ∇f_i(x_i^k; ξ_i^k)

2. Momentum tracking:
   y_i^(k+1) = Σ_j A_ij y_j^k + g_i^(k+1) - g_i^k

3. Push-Pull update:
   x_i^(k+1) = Σ_j B_ij x_j^k - α y_i^(k+1)

4. Momentum update:
   m_i^(k+1) = β m_i^k + (1-β) y_i^(k+1)
```

## Implementation Pattern

```python
import numpy as np
from typing import List, Callable, Tuple
import networkx as nx

class SMTPPOptimizer:
    """
    Stochastic Momentum Tracking Push-Pull Optimizer
    """
    
    def __init__(
        self,
        n_agents: int,
        learning_rate: float = 0.01,
        momentum: float = 0.9,
        graph: nx.DiGraph = None
    ):
        self.n_agents = n_agents
        self.alpha = learning_rate
        self.beta = momentum
        self.graph = graph or self._create_default_graph(n_agents)
        self.A, self.B = self._build_mixing_matrices()
        
    def _build_mixing_matrices(self) -> Tuple[np.ndarray, np.ndarray]:
        """Build row-stochastic A and column-stochastic B matrices"""
        n = self.n_agents
        A = np.zeros((n, n))
        B = np.zeros((n, n))
        
        for i in range(n):
            out_neighbors = list(self.graph.successors(i))
            if len(out_neighbors) == 0:
                out_neighbors = [i]
            
            for j in out_neighbors:
                A[i, j] = 1.0 / len(out_neighbors)
            
            in_neighbors = list(self.graph.predecessors(i))
            if len(in_neighbors) == 0:
                in_neighbors = [i]
            
            for j in in_neighbors:
                B[j, i] = 1.0 / len(in_neighbors)
        
        return A, B
    
    def step(self, local_gradients: List[np.ndarray]) -> List[np.ndarray]:
        """Execute one SMTPP iteration"""
        new_agents = []
        
        for i in range(self.n_agents):
            agent = self.agents[i]
            g_new = local_gradients[i]
            
            # Momentum tracking
            y_new = sum(self.A[i, j] * self.agents[j].y for j in range(self.n_agents))
            y_new += g_new - agent.grad_old
            
            # Push-Pull update
            x_new = sum(self.B[i, j] * self.agents[j].x for j in range(self.n_agents))
            x_new -= self.alpha * y_new
            
            # Momentum update
            m_new = self.beta * agent.m + (1 - self.beta) * y_new
            
            new_agents.append(AgentState(x=x_new, y=y_new, m=m_new, grad_old=g_new))
        
        self.agents = new_agents
        return [agent.x for agent in self.agents]
```

## Key Insights

1. **Asymmetric Communication**: Push-Pull mechanism handles directed graphs

2. **Variance Reduction**: Momentum tracking reduces stochastic gradient variance

3. **Consensus**: Agents converge to consensus despite using only local information

4. **Scalability**: Communication only with neighbors makes it scalable

## Applications

- Federated learning with heterogeneous clients
- Sensor network optimization
- Multi-robot coordination
- Distributed training in data centers

## References

- Original Paper: Stochastic Momentum Tracking Push-Pull for Decentralized Optimization over Directed Graphs
- arXiv: https://arxiv.org/abs/2604.08219v1
- Authors: Wenqi Fan, Yiwei Liao, Qing Xu, Bin Guo, Songyi Dian
- Published: 2026-04-09
