---
name: rts-neural-physics-ode-learning
description: "Hybrid neural-physics framework for learning unknown components of ODEs using Rauch-Tung-Striebel smoother and neural networks"
metadata:
  arxiv_id: "2607.15180v1"
  authors: ["Ahmet Demirkaya", "Georgios Stratis", "Tales Imbiriba", "Zachary D. Danziger", "Deniz Erdogmus"]
  published: "2026-07-16"
  categories: ["cs.LG", "eess.SY"]
  keywords: ["Rauch-Tung-Striebel smoother", "neural differential equations", "partial state observation", "hybrid modeling", "system identification"]
license: Complete terms in LICENSE.txt
---

# RTS Smoother-Guided Learning of Physics-Based Neural Differential Models

This skill implements the hybrid neural-physics framework from arXiv:2607.15180v1 for learning unknown components of ordinary differential equations (ODEs) when only partial state measurements are available.

## Overview

When modeling dynamical systems, we often know some components of the dynamics from first principles but have unknown components that need to be learned from data. This skill provides a methodology for combining known physics with neural networks to identify missing ODE components using partial state measurements.

The approach alternates between:
1. State estimation using a Rauch-Tung-Striebel (RTS) smoother (assuming known parameters)
2. Parameter estimation using backpropagation on neural networks (assuming known states)

## When to Use This Skill

Use this skill when you need to:
- Model dynamical systems with partially known dynamics
- Learn unknown ODE components from partial state measurements
- Combine mechanistic models with data-driven components
- Work with systems where only a subset of state variables are measurable
- Apply system identification to physical, biological, or physiological systems

## Core Methodology

### Two-Stage Alternating Procedure

**Stage 1: State Estimation (RTS Smoother)**
- Treat model parameters as known constants
- Use available measurements to estimate latent states via Rauch-Tung-Striebel smoother
- Produces smoothed state trajectories that minimize estimation error

**Stage 2: Parameter Estimation (Backpropagation)**
- Treat smoothed trajectories from Stage 1 as known
- Use these trajectories to train neural network parameters via backpropagation
- Minimize prediction error between model outputs and measurements

**Iteration**: Repeat stages until convergence (predetermined criterion met)

### Mathematical Formulation

For a system:
```
dx/dt = f_known(x, θ_known) + f_nn(x, θ_nn)
y = h(x) + v
```

Where:
- `f_known`: Known physics-based component
- `f_nn`: Neural network component to be learned
- `θ_known`: Known parameters
- `θ_nn`: Neural network parameters to learn
- `y`: Measured outputs (partial state observation)
- `v`: Measurement noise

## Implementation Steps

1. **Define Known Components**: Identify and implement the known portions of your ODE based on first principles
2. **Neural Network Architecture**: Design a neural network to approximate the unknown dynamics
3. **RTS Smoother Implementation**: Implement the Rauch-Tung-Striebel smoother for state estimation
4. **Alternating Optimization**:
   - Fix neural network weights, run RTS smoother to estimate states
   - Fix state trajectories, update neural network weights via backpropagation
   - Repeat until convergence criteria met
5. **Validation**: Test on held-out data and assess generalization to unseen conditions

## Key Advantages

- **Interpretability**: Preserves known physical structure while learning unknown components
- **Data Efficiency**: Leverages partial measurements effectively through smoothing
- **Generalization**: Learned neural network components can extrapolate to new conditions
- **Stability**: RTS smoother provides optimal state estimates under Gaussian assumptions

## Practical Considerations

### Network Architecture
- Choose appropriate architecture (MLP, LSTM, etc.) based on system dynamics
- Ensure sufficient capacity to capture unknown dynamics without overfitting
- Consider physics-informed constraints if applicable

### Convergence Criteria
- Monitoring validation loss on held-out data
- Checking parameter stability between iterations
- Setting maximum iterations to prevent infinite loops

### Initialization
- Proper initialization of neural network weights is crucial
- Consider pretraining on available data if possible
- Initialize physical parameters based on prior knowledge when available

## Validation Approach

1. **Synthetic Data Testing**: Validate on systems with known ground truth
2. **Cross-Validation**: Use temporal cross-validation for time series data
3. **Prediction Horizon**: Test both short-term and long-horizon predictions
4. **Robustness**: Evaluate sensitivity to noise levels and sampling rates

## Extensions and Variations

- **Multiple Unknown Components**: Extend to learn several distinct unknown functions
- **Time-Varying Parameters**: Allow learned components to vary with time or operating conditions
- **Uncertainty Quantification**: Incorporate Bayesian approaches for uncertainty estimates
- **Hybrid Architectures**: Combine multiple neural network types for different subsystems

## Common Pitfalls

1. **Over-reliance on Neural Network**: Ensure known physics component is sufficiently accurate
2. **Poor Observability**: Verify that measured states provide sufficient information for estimation
3. **Local Minima**: Use multiple random initializations to avoid poor local solutions
4. **Overfitting**: Regularize neural network and validate on unseen data
5. **Numerical Stability**: Ensure proper scaling of states and parameters

## References

- arXiv:2607.15180v1 - RTS Smoother-Guided Learning of Physics-Based Neural Differential Models
- Rauch, H.E., Tung, F., & Striebel, C.T. (1965). Maximum likelihood estimates of linear dynamic systems.
- Chen, T.Q., Rubanova, Y., Bettencourt, J., & Duvenaud, D.K. (2018). Neural Ordinary Differential Equations.

## Related Skills

- neural-ode-based-modeling: For pure neural ODE approaches
- physics-informed-neural-networks: For PINNs applied to PDEs
- system-identification-methods: For traditional system identification techniques