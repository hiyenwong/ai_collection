---
name: relaxation-informed-surrogate-training
description: "Relaxation-Informed Training (RIT) for neural network surrogate models enabling exact MILP embedding with reduced binary variables. Activation triggers: surrogate optimization, MILP embedding, neural network relaxation, ReLU pruning, optimization surrogate"
---

# Relaxation-Informed Training of Neural Network Surrogate Models

> Training framework for ReLU neural networks that enables exact embedding in Mixed-Integer Linear Programs (MILPs) while minimizing computational complexity through structural optimization.

## Metadata
- **Source**: arXiv:2604.22746
- **Authors**: Optimization/ML Research Group
- **Published**: 2026-04-27
- **Categories**: cs.LG, math.OC

## Core Methodology

### Problem Statement
ReLU neural networks trained as surrogate models for optimization problems can be embedded exactly in MILPs. However, the tractability of the resulting MILP depends critically on the number of binary variables representing ReLU activations. Standard training produces dense activation patterns, leading to intractable optimization problems.

### Relaxation-Informed Training Approach
**Key Insight**: Training with relaxed activations (linear instead of step) produces networks that are:
- Structurally sparse in activations
- Computationally efficient in MILP embedding
- Maintains approximation quality

### Structural Pruning During Training
- Replace ReLU step function with linear relaxation during training
- Promotes dead neurons and sparse activation patterns
- Results in fewer binary variables in final MILP formulation

## Implementation Guide

### Prerequisites
- PyTorch
- CVXPY or commercial MILP solver (Gurobi, CPLEX)
- Optimization problem formulation

### Step-by-Step

1. **Define Surrogate Architecture**
   ```python
   import torch
   import torch.nn as nn
   
   class RelaxedReLU(nn.Module):
       def __init__(self, epsilon=0.1):
           super().__init__()
           self.epsilon = epsilon
       
       def forward(self, x, training=True):
           if training:
               # Linear relaxation during training
               return torch.where(x > 0, x, self.epsilon * x)
           else:
               return torch.relu(x)
   ```

2. **Training with Relaxation**
   ```python
   def train_with_relaxation(model, data_loader, epochs=100):
       optimizer = torch.optim.Adam(model.parameters())
       
       for epoch in range(epochs):
           # Phase 1: Relaxed training (promotes sparsity)
           if epoch < epochs * 0.7:
               model.use_relaxed_activation = True
           else:
               model.use_relaxed_activation = False  # Fine-tune with ReLU
           
           for batch in data_loader:
               loss = compute_surrogate_loss(model, batch)
               optimizer.zero_grad()
               loss.backward()
               optimizer.step()
   ```

3. **MILP Embedding**
   ```python
   def embed_in_milp(model):
       binary_count = 0
       constraints = []
       
       for layer in model.layers:
           if isinstance(layer, nn.ReLU):
               # Only create binary var for active neurons
               active = (layer.weight.data.abs() > threshold).sum()
               binary_count += active
               constraints.append(create_big_m_constraint(layer))
       
       print(f"Total binary variables: {binary_count}")
       return constraints
   ```

4. **Optimization**
   ```python
   import cvxpy as cp
   
   # Create MILP with reduced binaries
   x = cp.Variable(n_inputs)
   y, binaries = model.to_milp(x)  # Sparse embedding
   objective = cp.Minimize(y)
   problem = cp.Problem(objective, constraints + binaries)
   problem.solve(solver=cp.GUROBI)
   ```

## Applications
- **Simulation Optimization**: Replace expensive simulators with tractable surrogates
- **Control Systems**: Model Predictive Control with learned dynamics
- **Chemical Engineering**: Process optimization via surrogate models
- **Energy Systems**: Power grid optimization with learned constraints

## Pitfalls
- Too aggressive relaxation (large epsilon) may degrade accuracy
- Requires careful scheduling between relaxed and ReLU phases
- MILP solver choice significantly impacts performance
- Not suitable for all problem types—test on problem class first

## Related Skills
- surrogate-optimization
- mixed-integer-programming
- physics-informed-neural-networks
- neural-network-pruning
