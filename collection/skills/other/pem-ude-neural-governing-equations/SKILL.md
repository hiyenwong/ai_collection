---
name: pem-ude-neural-governing-equations
description: "PEM-UDE methodology for discovering governing equations from chaotic neural systems. Combines prediction-error method with universal differential equations to extract interpretable mathematical expressions from chaotic dynamical systems, applied to neural population dynamics. Activation: pem-ude, governing equations neural, chaotic system discovery, universal differential equations neural, symbolic regression neural, neural population dynamics discovery."
---

# PEM-UDE: Scientific Machine Learning for Neural Governing Equations

> Combines the prediction-error method with universal differential equations to extract interpretable mathematical expressions from chaotic dynamical systems, enabling discovery of governing equations for neural populations from noisy, limited observations.

## Metadata
- **Source**: arXiv:2507.03631
- **Title**: Scientific Machine Learning of Chaotic Systems Discovers Governing Equations for Neural Populations
- **Authors**: Anthony G. Chesebro, David Hofmann, Vaibhav Dixit, Earl K. Miller, Richard H. Granger, Alan Edelman, Christopher V. Rackauckas, Lilianne R. Mujica-Parodi, Helmut H. Strey
- **Published**: 2025-07-04 (v3: 2025-12-17)
- **Venue**: 46 pages, 9 figures

## Core Methodology

### Key Innovation

PEM-UDE addresses the fundamental challenge of discovering governing equations for complex chaotic systems (like neural populations) where:
1. Observations are limited and noisy
2. Traditional symbolic regression (e.g., STLSQ/SINDy) fails on chaotic data
3. Direct fitting distorts optimal parameters due to chaotic sensitivity

**Solution**: Smooth the optimization landscape by removing chaotic properties during fitting WITHOUT distorting the optimal parameters, then extract interpretable mathematical expressions.

### Technical Framework

#### Step 1: Universal Differential Equations (UDE) Setup

UDE combines known physics/biological constraints with neural network components to discover unknown dynamics:

```
dx/dt = f_known(x, θ_known) + f_neural(x, θ_neural)
```

Where `f_neural` is a neural network that captures the unknown parts of the dynamics.

#### Step 2: Prediction-Error Method (PEM) Integration

Instead of fitting directly to chaotic trajectories (which is sensitive to initial conditions), PEM uses:

1. **Smoothing**: Apply filtering to remove chaotic sensitivity during optimization
2. **Parameter estimation**: Fit model parameters using prediction error minimization
3. **Recovery**: The correct functional form is recovered even when observations are corrupted by noise 5x the signal magnitude

#### Step 3: Biological Constraint Enforcement

For neural populations, the method enforces:
- **Network sparsity**: A constraint necessary for cortical information processing
- **Microscale parameter preservation**: Maintains biologically meaningful neuronal parameters
- **Multi-scale generalization**: Bridges single-neuron dynamics to macroscale brain activity

### Key Findings

1. **Connection density → oscillation frequency**: Emergent relationship between neural circuit connection density and oscillation frequency
2. **Connection density → synchrony**: Connection density predicts circuit synchrony
3. **Validation**: Confirmed using intracranial electrode recordings from:
   - Medial entorhinal cortex
   - Prefrontal cortex
   - Orbitofrontal cortex

## Implementation Guide

### Prerequisites
- PyTorch or JAX for neural network components
- Universal Differential Equations library (e.g., Diffrax, NeuralODE)
- Scientific computing stack (NumPy, SciPy)

### Step-by-Step

```python
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import minimize

class PEMUDE:
    """
    Prediction-Error Method with Universal Differential Equations
    for discovering governing equations from chaotic neural data
    """
    
    def __init__(self, known_dynamics, neural_net, dt=0.001):
        """
        Args:
            known_dynamics: Known parts of the ODE (function)
            neural_net: Neural network for unknown dynamics
            dt: Time step
        """
        self.known_dynamics = known_dynamics
        self.neural_net = neural_net
        self.dt = dt
        
    def smooth_trajectory(self, data, window_size=5):
        """
        Smooth chaotic trajectory to remove sensitivity during optimization
        
        Uses moving average or Savitzky-Golay filtering
        """
        from scipy.signal import savgol_filter
        return savgol_filter(data, window_length=window_size, polyorder=2, axis=0)
    
    def prediction_error(self, params, data, t_span):
        """
        Compute prediction error for parameter estimation
        
        Minimizes: Σ ||x_measured(t) - x_predicted(t; θ)||²
        """
        # Unpack parameters
        theta_known = params[:len(self.known_dynamics.params)]
        theta_neural = params[len(self.known_dynamics.params):]
        
        # Set parameters
        self.known_dynamics.set_params(theta_known)
        self.neural_net.set_params(theta_neural)
        
        # Integrate UDE
        def ode_rhs(t, x):
            f_known = self.known_dynamics(x)
            f_neural = self.neural_net(x)
            return f_known + f_neural
        
        sol = solve_ivp(ode_rhs, t_span, data[0], 
                       method='RK45', t_eval=t_span, rtol=1e-6)
        
        # Compute prediction error
        error = np.sum((sol.y.T - data) ** 2)
        return error
    
    def enforce_sparsity(self, params, sparsity_threshold=0.1):
        """
        Enforce network sparsity constraint
        
        Zero out connections below threshold
        """
        # Apply L1 regularization or hard thresholding
        mask = np.abs(params) > sparsity_threshold
        return params * mask
    
    def discover_equations(self, neural_data, t_span, 
                          max_iterations=1000, sparsity=0.1):
        """
        Main discovery pipeline
        
        Args:
            neural_data: Observed neural population activity [time, neurons]
            t_span: Time vector
            max_iterations: Optimization iterations
            sparsity: Sparsity threshold
            
        Returns:
            discovered_equations: Interpretable mathematical expressions
            parameters: Fitted parameters
        """
        # Step 1: Smooth data
        smoothed_data = self.smooth_trajectory(neural_data)
        
        # Step 2: Initialize parameters
        initial_params = self.initialize_parameters()
        
        # Step 3: Optimize using PEM
        result = minimize(
            self.prediction_error,
            initial_params,
            args=(smoothed_data, t_span),
            method='L-BFGS-B',
            options={'maxiter': max_iterations}
        )
        
        # Step 4: Enforce sparsity
        sparse_params = self.enforce_sparsity(result.x, sparsity)
        
        # Step 5: Extract symbolic expressions
        equations = self.extract_symbolic(sparse_params)
        
        return equations, sparse_params
    
    def extract_symbolic(self, params):
        """
        Convert neural network weights to symbolic expressions
        
        Uses techniques like:
        - Taylor expansion of activation functions
        - Symbolic regression on learned weights
        - Threshold-based pruning to simple forms
        """
        # Simplified implementation
        expressions = []
        
        for i in range(len(params)):
            if abs(params[i]) > 1e-3:  # Non-zero contribution
                # Convert to symbolic form
                expr = self.weight_to_symbolic(i, params[i])
                expressions.append(expr)
                
        return expressions
```

### Validation Pipeline

```python
def validate_discovered_equations(equations, validation_data):
    """
    Validate discovered equations against held-out data
    
    Checks:
    1. Prediction accuracy on validation set
    2. Biological plausibility of parameters
    3. Consistency with known neural dynamics
    """
    # Simulate with discovered equations
    predicted = simulate(equations, validation_data[0])
    
    # Compute metrics
    rmse = np.sqrt(np.mean((predicted - validation_data) ** 2))
    
    # Check biological constraints
    is_sparse = check_sparsity(equations)
    has_correct_signs = check_parameter_signs(equations)
    
    return {
        'rmse': rmse,
        'is_sparse': is_sparse,
        'biologically_plausible': has_correct_signs
    }
```

## Applications
- **Neural population dynamics**: Discover governing equations from neural recordings
- **Multi-scale brain modeling**: Bridge single-neuron to macroscale dynamics
- **Cortical circuit analysis**: Extract connection density-oscillation relationships
- **Clinical neuroscience**: Identify dynamical biomarkers from noisy neural data
- **Chaotic system identification**: General method for any chaotic dynamical system

## Pitfalls
- **Noise sensitivity**: Requires smoothing step; direct fitting to chaotic data fails
- **Symbolic extraction**: Converting neural weights to interpretable equations is non-trivial
- **Computational cost**: UDE optimization can be expensive for large networks
- **Initial conditions**: Poor initialization may lead to local optima
- **Overfitting**: Sparsity constraint is essential to avoid overfitting to noise

## Related Skills
- spiking-neural-network-differential-equation
- neural-operator-stability-discovery
- generative-brain-dynamics-models
- complex-system-robustness-collapse
