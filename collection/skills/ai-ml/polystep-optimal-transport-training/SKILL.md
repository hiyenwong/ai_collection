---
name: polystep-optimal-transport-training
description: "Gradient-free optimization for non-differentiable networks using optimal transport (PolyStep). Trains spiking neurons, quantized layers, discrete routing without surrogate gradients. Activation: polystep, optimal transport training, gradient-free optimizer, non-differentiable networks, spiking training without backprop."
---

# PolyStep: Training Non-Differentiable Networks via Optimal Transport

> Gradient-free optimizer that updates parameters using only forward passes via structured polytope vertices and optimal transport barycentric projection.

## Metadata
- **Source**: arXiv:2605.01928
- **Authors**: An T. Le
- **Published**: 2026-05-03
- **Category**: cs.LG, cs.NE, cs.RO, math.OC

## Core Methodology

### Key Innovation
PolyStep is a gradient-free optimizer that trains genuinely non-differentiable models (spiking neurons, quantized layers, discrete routing, blackbox simulators) where backpropagation is inapplicable and surrogate gradients introduce bias. It achieves 93.4% accuracy on hard-LIF spiking networks, outperforming all gradient-free baselines by 60+pp and closing to within 4.4pp of surrogate-gradient Adam.

### Technical Framework

1. **Polytope Vertex Evaluation**: Each optimization step evaluates the loss at structured polytope vertices in a compressed subspace
2. **Softmax-Weighted Assignment**: Computes assignments over the resulting cost matrix using softmax
3. **Barycentric Projection**: Displaces particles toward low-cost vertices via barycentric projection
4. **Optimal Transport Connection**: The update corresponds to the one-sided limit of a regularized optimal transport problem, inheriting its geometric structure without Sinkhorn iterations

### Theoretical Guarantees
- Convergence to conservative-stationary points at rate O(log T/√T) on piecewise-smooth losses
- Upgraded to Clarke-stationary on headline architectures
- Extended to piecewise-constant regime via hitting-time bound
- Rates match known zeroth-order query-complexity lower bounds

## Applications
- **Spiking Neural Networks**: Training hard-LIF neurons without surrogate gradients
- **Quantized Networks**: int8 quantization training
- **Discrete Architectures**: argmax attention, hard MoE routing, staircase activations
- **Combinatorial Optimization**: MAX-SAT (sustains 92%+ clause satisfaction at 1M variables)
- **RL Policy Search**: Matches OpenAI-ES on classical control, robust to integer/binary quantization

## Implementation Guide

### Prerequisites
- PyTorch or similar deep learning framework
- Models with non-differentiable components

### Algorithm Steps
1. Define a compressed subspace dimension d << D (parameter dimension)
2. Generate structured polytope vertices in the compressed subspace
3. Evaluate loss at each vertex (forward pass only)
4. Compute softmax-weighted assignment over cost matrix
5. Perform barycentric projection to update particles
6. Map update back to original parameter space

### Code Sketch
```python
import torch
import torch.nn.functional as F

def polystep_step(model, loss_fn, data, target, n_vertices=2*d+1, temperature=1.0):
    """Single PolyStep optimization step."""
    params = list(model.parameters())
    flat_params = torch.cat([p.view(-1) for p in params])
    D = flat_params.shape[0]
    d = min(64, D)  # compressed subspace dimension
    
    # Generate polytope vertices in compressed subspace
    vertices = generate_polytope_vertices(d, n_vertices)
    
    # Evaluate loss at each vertex
    losses = []
    for v in vertices:
        # Map vertex to parameter perturbation
        delta = project_to_paramspace(v, D)
        with torch.no_grad():
            apply_perturbation(model, delta)
            output = model(data)
            loss = loss_fn(output, target)
            losses.append(loss.item())
        restore_model(model)  # Reset to original params
    
    # Softmax-weighted assignment
    costs = torch.tensor(losses)
    weights = F.softmax(-costs / temperature, dim=0)
    
    # Barycentric projection (displace toward low-cost vertices)
    update = sum(w * v for w, v in zip(weights, vertices))
    
    # Apply update to parameters
    apply_update(model, project_to_paramspace(update, D), lr=0.01)
```

## Pitfalls
- **Vertex count**: n_vertices = 2d+1 is minimal; more vertices improve accuracy but increase forward passes
- **Compressed dimension**: d should be small (32-128) for efficiency but large enough for expressiveness
- **Temperature**: Controls exploration vs exploitation; needs tuning per problem
- **Not for smooth networks**: If surrogate gradients work well, PolyStep is unnecessary overhead
- **Query complexity**: O(n_vertices) forward passes per step — more expensive than gradient-based methods

## Related Skills
- gradient-free-continual-learning-snn
- scalable-snn-without-backprop
- surrogate-gradient-snn-training
- quantization-spiking-neural-networks-beyond-accuracy
- density-driven-optimal-control
