---
name: state-space-ntk-collapse-bifurcations
description: "Analysis of Neural Tangent Kernel (NTK) collapse near dynamical bifurcations in state-space models. Studies how the NTK spectrum degrades as recurrent networks approach critical transitions. Activation: NTK collapse, bifurcation analysis, state-space NTK, critical transitions neural networks, dynamical systems deep learning."
---

# State-Space NTK Collapse Near Bifurcations

> Analysis of Neural Tangent Kernel (NTK) behavior near dynamical bifurcations in state-space neural networks, revealing how training dynamics change as models approach critical phase transitions.

## Metadata
- **Source**: arXiv:2605.12763
- **Authors**: James Hazelden, Eric Shea-Brown
- **Published**: 2026-05-14
- **Categories**: Machine Learning (cs.LG); Dynamical Systems (math.DS); Optimization and Control (math.OC); Neurons and Cognition (q-bio.NC)

## Core Methodology

### Key Innovation
Analyzes the behavior of the Neural Tangent Kernel (NTK) as state-space recurrent neural networks approach dynamical bifurcations. The NTK provides a linearized view of neural network training dynamics, and this work reveals how the NTK spectrum degrades near critical transitions, affecting trainability and generalization.

### Technical Framework
1. **State-Space RNN Formulation**: Analyzes recurrent networks through their continuous-time state-space dynamics
2. **NTK Computation**: Computes the Neural Tangent Kernel for state-space models
3. **Bifurcation Analysis**: Studies how NTK eigenvalues change as network parameters approach bifurcation points
4. **Critical Transition Theory**: Connects dynamical systems bifurcation theory with deep learning training dynamics

### Key Findings
- NTK spectrum collapses as the network approaches bifurcation points
- Eigenvalue structure reveals which directions in parameter space become ill-conditioned
- Different bifurcation types (saddle-node, Hopf, etc.) produce distinct NTK signatures
- Training dynamics slow down near critical transitions due to NTK degradation
- Has implications for understanding critical brain dynamics and phase transitions in neural systems

## Implementation Guide

### Prerequisites
- PyTorch/JAX for neural network implementation
- Linear algebra libraries for eigenvalue computation
- Bifurcation analysis tools (e.g., PyDSTool, PyAuto)

### Step-by-Step
1. **Define State-Space Model**: Implement recurrent network as continuous-time dynamical system
2. **Compute NTK**: Calculate Neural Tangent Kernel for the state-space model
3. **Parameter Sweep**: Vary parameters to approach bifurcation points
4. **Eigenvalue Analysis**: Track NTK eigenvalue spectrum during parameter changes
5. **Bifurcation Detection**: Identify critical transition points from NTK behavior

### Code Concept
```python
# Conceptual framework
def compute_state_space_ntk(model, inputs):
    """Compute NTK for state-space recurrent model."""
    # Linearize model around current parameters
    # Compute Jacobian of outputs w.r.t. parameters
    # NTK = J @ J.T
    jacobian = torch.autograd.functional.jacobian(model, inputs)
    ntk = jacobian @ jacobian.T
    return ntk

def analyze_ntk_collapse(ntk, bifurcation_param):
    """Analyze NTK eigenvalue spectrum near bifurcation."""
    eigenvalues = torch.linalg.eigvalsh(ntk)
    condition_number = eigenvalues.max() / eigenvalues.min()
    return eigenvalues, condition_number
```

## Applications
- Understanding training dynamics of recurrent neural networks near critical points
- Predicting when RNN training will stall due to NTK collapse
- Designing initialization schemes that avoid bifurcation-adjacent regions
- Connecting deep learning theory with critical brain dynamics
- Analyzing stability of learned dynamical systems

## Pitfalls
- NTK analysis assumes linearized training dynamics, which may not hold far from initialization
- Computing full NTK is O(N²) in data size — requires approximations for large datasets
- Bifurcation detection requires careful parameter sweep design

## Related Skills
- geodynamics-geometric-state-space
- neural-dynamics-universal-translator
- neural-critical-dynamics-theory
- nonlinear-rnn-fixed-connectivity-solution
- renormalization-scaling-brain-activity
