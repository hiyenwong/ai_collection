---
name: decentralized-optimization-smtpp
description: Stochastic Momentum Tracking Push-Pull for Decentralized Optimization over Directed Graphs. Handle asymmetric communication and high variance in distributed optimization.
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [decentralized-optimization, momentum-tracking, directed-graphs, stochastic-gradient, distributed-learning]
    source_paper: "Stochastic Momentum Tracking Push-Pull for Decentralized Optimization over Directed Graphs (arXiv:2604.08219)"
    citations: 0
    category: optimization and control
---

# SMTPP: Decentralized Optimization over Directed Graphs

## Overview

This skill provides the Stochastic Momentum Tracking Push-Pull (SMTPP) algorithm for decentralized optimization over directed graphs. It addresses challenges of asymmetric communication and high variance in stochastic gradients that cause oscillations and hinder convergence.

## Core Concepts

### Decentralized Optimization
- **Setting**: Multiple agents collaborate without central coordinator
- **Challenge**: Communication asymmetry in directed graphs
- **Objective**: Minimize global objective using local information

### SMTPP Algorithm
- **Momentum Tracking**: Track momentum term instead of raw stochastic gradients
- **Push-Pull**: Combine push (out-neighbors) and pull (in-neighbors) communication
- **Variance Reduction**: Mitigate stochastic gradient variance

## Implementation Pattern

```python
import numpy as np
from typing import List, Dict, Tuple, Callable
from dataclasses import dataclass

@dataclass
class Agent:
    id: int
    neighbors_out: List[int]  # Out-neighbors (push targets)
    neighbors_in: List[int]   # In-neighbors (pull sources)
    weight_out: Dict[int, float]  # Weights for out-neighbors
    weight_in: Dict[int, float]   # Weights for in-neighbors

class SMTPPOptimizer:
    """
    Stochastic Momentum Tracking Push-Pull optimizer
    for decentralized optimization over directed graphs
    """
    
    def __init__(self, agents: List[Agent], 
                 learning_rate: float = 0.01,
                 momentum: float = 0.9,
                 beta: float = 0.9):
        self.agents = agents
        self.lr = learning_rate
        self.momentum = momentum
        self.beta = beta
        
        # State variables for each agent
        self.x = {}  # Parameters
        self.v = {}  # Momentum term
        self.y = {}  # Auxiliary variable for push-pull
        self.m = {}  # Momentum tracking variable
        
    def initialize(self, init_fn: Callable[[int], np.ndarray]):
        """
        Initialize agent states
        
        Args:
            init_fn: Function that takes agent_id and returns initial parameters
        """
        for agent in self.agents:
            self.x[agent.id] = init_fn(agent.id)
            dim = self.x[agent.id].shape
            self.v[agent.id] = np.zeros(dim)
            self.y[agent.id] = np.zeros(dim)
            self.m[agent.id] = np.zeros(dim)
    
    def step(self, gradients: Dict[int, np.ndarray]):
        """
        Perform one SMTPP iteration
        
        Args:
            gradients: Dict mapping agent_id to stochastic gradient
        """
        # Step 1: Update momentum tracking variable
        for agent in self.agents:
            grad = gradients[agent.id]
            self.m[agent.id] = self.beta * self.m[agent.id] + grad
        
        # Step 2: Push step - send information to out-neighbors
        push_messages = {}
        for agent in self.agents:
            push_messages[agent.id] = {
                'x': self.x[agent.id],
                'm': self.m[agent.id],
                'y': self.y[agent.id]
            }
        
        # Step 3: Pull step - aggregate from in-neighbors
        x_new = {}
        y_new = {}
        
        for agent in self.agents:
            # Aggregate x from in-neighbors (pull)
            x_agg = np.zeros_like(self.x[agent.id])
            for neighbor in agent.neighbors_in:
                weight = agent.weight_in.get(neighbor, 1.0 / len(agent.neighbors_in))
                x_agg += weight * push_messages[neighbor]['x']
            
            # Update momentum
            self.v[agent.id] = self.momentum * self.v[agent.id] + self.m[agent.id]
            
            # Update parameters
            x_new[agent.id] = x_agg - self.lr * self.v[agent.id]
            
            # Update auxiliary variable y (push-pull)
            y_agg = np.zeros_like(self.y[agent.id])
            for neighbor in agent.neighbors_in:
                weight = agent.weight_in.get(neighbor, 1.0 / len(agent.neighbors_in))
                y_agg += weight * push_messages[neighbor]['y']
            
            y_new[agent.id] = y_agg + self.x[agent.id] - x_new[agent.id]
        
        # Update state
        self.x = x_new
        self.y = y_new
    
    def get_average_params(self) -> np.ndarray:
        """Compute average parameters across all agents"""
        params = [self.x[agent.id] for agent in self.agents]
        return np.mean(params, axis=0)
    
    def compute_consensus_error(self) -> float:
        """
        Compute consensus error (variance of parameters across agents)
        Lower is better - indicates agents agree on solution
        """
        avg = self.get_average_params()
        errors = [np.linalg.norm(self.x[agent.id] - avg) for agent in self.agents]
        return np.mean(errors)

def create_ring_graph(n_agents: int) -> List[Agent]:
    """
    Create a directed ring graph for testing
    Each agent connects to next 2 agents
    """
    agents = []
    for i in range(n_agents):
        neighbors_out = [(i + 1) % n_agents, (i + 2) % n_agents]
        neighbors_in = [(i - 1) % n_agents, (i - 2) % n_agents]
        
        weight_out = {j: 0.5 for j in neighbors_out}
        weight_in = {j: 0.5 for j in neighbors_in}
        
        agents.append(Agent(
            id=i,
            neighbors_out=neighbors_out,
            neighbors_in=neighbors_in,
            weight_out=weight_out,
            weight_in=weight_in
        ))
    
    return agents

# Usage Example
n_agents = 10
agents = create_ring_graph(n_agents)
optimizer = SMTPPOptimizer(agents, learning_rate=0.01, momentum=0.9)
optimizer.initialize(lambda i: np.random.randn(5))

# Training loop
for iteration in range(100):
    # Compute stochastic gradients (example)
    gradients = {i: np.random.randn(5) for i in range(n_agents)}
    optimizer.step(gradients)
    
    if iteration % 10 == 0:
        consensus = optimizer.compute_consensus_error()
        print(f"Iteration {iteration}: Consensus error = {consensus:.4f}")
```

## Key Insights

1. **Momentum Tracking**: Tracking momentum instead of raw gradients reduces variance
2. **Push-Pull Mechanism**: Handles asymmetric communication in directed graphs
3. **Convergence**: Provable convergence under standard assumptions
4. **Robustness**: Mitigates oscillations caused by high gradient variance

## Best Practices

- Use momentum parameter β ∈ [0.9, 0.99] for tracking
- Ensure graph is strongly connected for convergence
- Tune learning rate based on problem conditioning
- Monitor consensus error as convergence diagnostic

## References

- Fan, W., Liao, Y., Xu, Q., Guo, B., & Dian, S. (2025). Stochastic Momentum Tracking Push-Pull for Decentralized Optimization over Directed Graphs. arXiv:2604.08219.

## Trigger Words

- decentralized optimization
- smtpp
- directed graphs
- momentum tracking
- push-pull algorithm
- distributed learning
