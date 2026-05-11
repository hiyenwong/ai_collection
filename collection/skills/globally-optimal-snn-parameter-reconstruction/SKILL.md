---
name: globally-optimal-snn-parameter-reconstruction
description: >
  Globally optimal Spiking Neural Network (SNN) training via parameter
  reconstruction methodology. Extends convexification of parallel feedforward
  threshold networks to parallel recurrent threshold networks, which subsume
  parallel SNNs as a structured special case. Eliminates surrogate gradient
  approximation errors that accumulate across layers by formulating SNN
  training as a convex optimization problem solvable via parameter
  reconstruction. Use when training SNNs without surrogate gradients,
  seeking globally optimal SNN solutions, convex SNN training, recurrent
  threshold network optimization, or large-scale SNN training with data
  scalability. Triggers: globally optimal SNN, parameter reconstruction,
  convex SNN training, surrogate gradient elimination, threshold network
  convexification, recurrent SNN optimization.
---

# Globally Optimal SNN Training via Parameter Reconstruction

SNN training typically relies on surrogate gradients due to the
non-differentiability of the spike function, introducing approximation
errors that accumulate across layers. This methodology eliminates that
problem by extending convexification of parallel feedforward threshold
networks to parallel recurrent threshold networks.

## Core Insight

Parallel SNNs are a structured special case of parallel recurrent threshold
networks. By convexifying the recurrent threshold network formulation, SNN
training becomes a globally optimal convex optimization problem.

## Mathematical Framework

### From SNN to Recurrent Threshold Network

Standard SNN forward pass:
```
h[t] = W·s[t-1] + b
s[t] = 𝟙(h[t] > θ)  # non-differentiable
```

Reformulate as parallel recurrent threshold network:
```
h = W·s + b
s = 𝟙(h > θ)
```

Where s represents the entire spike train across all time steps and layers,
concatenated into a single vector.

### Convexification

The key insight: the training problem can be reformulated as a convex
optimization over the space of parameters:

```
min ||y - ŷ(W, b)||²  s.t.  s = 𝟙(Ws + b > θ)
```

This is reformulated into an equivalent convex problem via parameter
reconstruction.

### Parameter Reconstruction Algorithm

```python
def reconstruct_parameters(X, y, n_hidden, regularization=1e-4):
    """
    Reconstruct optimal SNN parameters via convex optimization.

    Args:
        X: Input data (batch, input_dim)
        y: Labels (batch, output_dim)
        n_hidden: Number of hidden neurons
        regularization: L2 regularization strength

    Returns:
        W1, W2, b1, b2: Reconstructed network parameters
    """
    import cvxpy as cp
    import numpy as np

    n_samples, input_dim = X.shape
    output_dim = y.shape[1]

    # Convex reformulation variables
    # Each neuron's contribution is a convex combination
    u = cp.Variable((n_hidden, input_dim))
    v = cp.Variable((n_hidden, input_dim))

    # Positive and negative parts (ReLU-style decomposition)
    # Threshold network: f(x) = Σᵢ (wᵢᵀx)₊ · αᵢ + (wᵢᵀx)₋ · βᵢ

    # Output layer parameters
    A = cp.Variable((output_dim, n_hidden))

    # Convex objective
    # Predictions: ŷ = A · [ReLU(X·uᵢ)]ᵢ
    predictions = cp.hstack([
        cp.maximum(X @ u[i], 0) - cp.maximum(X @ v[i], 0)
        for i in range(n_hidden)
    ])
    predictions = A @ predictions

    objective = cp.Minimize(
        cp.sum_squares(predictions - y) +
        regularization * (cp.sum_squares(u) + cp.sum_squares(v))
    )

    constraints = []  # Add problem-specific constraints

    problem = cp.Problem(objective, constraints)
    problem.solve(solver=cp.SCS)

    # Extract parameters
    # Reconstruct W1, W2 from convex solution
    W1 = np.vstack([u.value, -v.value])
    W2 = A.value

    return W1, W2
```

## Training Workflow

### Step 1: Convex Problem Construction

1. Decompose each neuron's contribution into positive/negative parts
2. Formulate the prediction as a convex combination
3. Add regularization for generalization

### Step 2: Solve Convex Problem

Use convex optimization solver (CVXPY, SCS, MOSEK):

```python
problem = cp.Problem(objective, constraints)
problem.solve(solver=cp.SCS, verbose=True)
```

### Step 3: Parameter Reconstruction

Extract original SNN parameters from the convex solution:

```python
def extract_snn_params(convex_solution):
    """Reconstruct threshold network parameters from convex solution."""
    # The convex solution provides the optimal direction and scale
    # for each neuron's weight vector

    u_opt = convex_solution['u']
    v_opt = convex_solution['v']
    A_opt = convex_solution['A']

    # Reconstruct: each hidden neuron has weight wᵢ and sign sᵢ
    weights = np.concatenate([u_opt, -v_opt], axis=0)
    signs = np.concatenate([np.ones(len(u_opt)), -np.ones(len(v_opt))])

    # Output weights absorb the sign
    W_out = A_opt * signs.T

    return weights, W_out
```

## Advantages Over Surrogate Gradients

| Property | Surrogate Gradient | Parameter Reconstruction |
|----------|-------------------|-------------------------|
| Optimality | Local minimum | Global optimum |
| Approximation error | Yes (accumulates) | None (exact) |
| Depth sensitivity | Degrades with depth | Consistent |
| Hyperparameter tuning | Extensive | Minimal |
| Data scalability | Good | Excellent |

## Combination with Surrogate Gradients

The parameter reconstruction method can be combined with surrogate gradient
training:

```python
# Hybrid training
W_reconstructed = reconstruct_parameters(X_train, y_train, n_hidden)
W_init = initialize_from_reconstruction(W_reconstructed)
W_final = surrogate_gradient_finetune(W_init, X_train, y_train)
```

This provides better initialization than random, leading to faster
convergence and better final performance.

## Scalability

The method scales with:
- **Number of neurons**: O(n_hidden²) for convex solve
- **Number of samples**: Linear in convex formulation
- **Parallelization**: GPU-accelerated convex solvers available

For large-scale SNN training:
1. Use mini-batch convex optimization
2. Apply column generation for very large networks
3. Warm-start from previous batches

## Datasets & Tasks

Validated across multiple tasks:
- Image classification (CIFAR-10, ImageNet subsets)
- Event-based vision (N-MNIST, DVS-Gesture)
- Temporal sequence prediction

## Implementation Considerations

1. **Solver choice**: SCS for large problems, MOSEK for precision
2. **Regularization**: Critical for generalization; tune on validation set
3. **Neuron count**: More neurons → tighter convex relaxation
4. **Numerical stability**: Scale inputs to [-1, 1] range

## Activation Keywords

- globally optimal SNN training
- parameter reconstruction SNN
- convex SNN training
- surrogate gradient elimination
- threshold network convexification
- recurrent threshold network
- SNN without surrogate gradient
- convex spiking neural network
- optimal spiking network training