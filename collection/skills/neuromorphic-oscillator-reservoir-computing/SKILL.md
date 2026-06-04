---
name: neuromorphic-oscillator-reservoir-computing
description: "Reservoir computing using parametrically-driven oscillators and frequency combs for neuromorphic computation. Three-regime system (sub-threshold, parametric resonance, frequency-comb) with 2:1 resonance. Optimal performance at parametric resonance boundary. Applications: chaotic time-series prediction (Mackey-Glass, Rössler, Lorenz), edge AI, analog neural networks."
category: ai_collection
tags: [neuromorphic-computing, reservoir-computing, parametric-oscillator, frequency-comb, chaotic-prediction, analog-computing]
paper:
  arxiv_id: "2604.21861"
  title: "Neuromorphic Computing Based on Parametrically-Driven Oscillators and Frequency Combs"
  authors: ["Mahadev Sunil Kumar", "Adarsh Ganesan"]
  date: "2026-04-23"
---

# Neuromorphic Computing Based on Parametrically-Driven Oscillators and Frequency Combs

## Overview

Two-mode parametrically-driven oscillator system for reservoir computing with 2:1 parametric resonance. Operates across three dynamical regimes — sub-threshold (linear), parametric resonance (nonlinear coherent), and frequency-comb (high spectral dimensionality).

**Key Finding:** Optimal computational performance at parametric resonance boundary, balancing nonlinear transformation and temporal coherence.

## Three Operating Regimes

### 1. Sub-Threshold (Linear)
- Pump below threshold amplitude
- Linear response, no parametric gain
- Limited computational capability
- Stable but weakly expressive

### 2. Parametric Resonance (Optimal)
- **Optimal operating point for reservoir computing**
- Nonlinear interactions activated
- Temporal coherence preserved
- Balance of expressivity and stability
- **Best prediction performance**

### 3. Frequency-Comb (Chaotic)
- High drive amplitudes
- Increased spectral dimensionality
- Phase coherence loss in chaotic comb regime
- Inconsistent performance
- **Not recommended for computation**

## System Architecture

```
Pump Mode (ω_p) → 2:1 Resonance → Signal Mode (ω_s ≈ ω_p/2)
       ↓                                        ↓
  Drive Amplitude                          Response
  F(t) = F₀ + ε·u(t)                    Temporal/Spectral
                                        Features
```

### Key Parameters
- **ω_p**: Pump frequency
- **ω_s**: Signal frequency ≈ ω_p/2
- **δ**: Detuning = ω_s - ω_p/2
- **γ₁, γ₂**: Damping coefficients
- **F₀**: Base drive amplitude
- **ε**: Input scaling
- **u(t)**: Input signal

## Equations of Motion

```
ẍ₁ + 2γ₁ẋ₁ + ω₁²x₁ = F(t)·cos(ω_p·t) + α·x₂²  (Pump mode)
ẍ₂ + 2γ₂ẋ₂ + ω₂²x₂ = β·x₁·x₂                   (Signal mode)
```

Where:
- x₁, x₂: displacements of pump and signal modes
- α, β: nonlinear coupling coefficients
- F(t) = F₀ + ε·u(t): amplitude-modulated drive

## Implementation Guide

### Step 1: System Setup

```python
class ParametricOscillator:
    def __init__(self, omega_p, omega_s, gamma1, gamma2, alpha, beta):
        self.omega_p = omega_p      # Pump frequency
        self.omega_s = omega_s      # Signal frequency
        self.gamma1 = gamma1        # Pump damping
        self.gamma2 = gamma2        # Signal damping
        self.alpha = alpha        # Coupling coefficient
        self.beta = beta          # Coupling coefficient
        
        # Detuning
        self.delta = omega_s - omega_p/2
        
    def equations(self, t, state, F0, epsilon, u_t):
        """Define coupled ODEs."""
        x1, v1, x2, v2 = state
        
        # Drive amplitude (input-encoded)
        F_t = F0 + epsilon * u_t
        
        # Pump mode equation
        dx1 = v1
        dv1 = (-2*self.gamma1*v1 - self.omega_p**2*x1 
               + F_t * np.cos(self.omega_p*t) + self.alpha*x2**2)
        
        # Signal mode equation
        dx2 = v2
        dv2 = (-2*self.gamma2*v2 - self.omega_s**2*x2 
               + self.beta*x1*x2)
        
        return [dx1, dv1, dx2, dv2]
```

### Step 2: Input Encoding

```python
def encode_input(input_series, F0, epsilon):
    """
    Encode input time series into drive amplitude modulation.
    
    Args:
        input_series: Input time series u(t)
        F0: Base drive amplitude
        epsilon: Modulation depth (controls regime)
    
    Returns:
        modulated_drive: F(t) = F0 + ε·u(t)
    """
    # Normalize input to appropriate range
    u_scaled = (input_series - np.mean(input_series)) / np.std(input_series)
    
    # Modulate drive amplitude
    modulated_drive = F0 + epsilon * u_scaled
    
    return modulated_drive
```

### Step 3: Reservoir State Extraction

```python
class ReservoirStateExtractor:
    def __init__(self, sampling_params):
        self.temporal_samples = sampling_params['temporal']
        self.spectral_bins = sampling_params['spectral']
        
    def extract_temporal(self, trajectory, window_size):
        """Extract temporal features from trajectory."""
        # Sample multiple time points within window
        indices = np.linspace(0, len(trajectory)-1, self.temporal_samples)
        temporal_features = trajectory[indices.astype(int)]
        return temporal_features.flatten()
    
    def extract_spectral(self, trajectory, dt):
        """Extract spectral features via FFT."""
        fft = np.fft.fft(trajectory)
        freqs = np.fft.fftfreq(len(trajectory), dt)
        
        # Sample at predefined frequency bins
        bin_indices = np.linspace(0, len(freqs)//2, self.spectral_bins)
        spectral_features = np.abs(fft[bin_indices.astype(int)])
        
        return spectral_features
    
    def get_state(self, trajectory, dt):
        """Combine temporal and spectral features."""
        temporal = self.extract_temporal(trajectory)
        spectral = self.extract_spectral(trajectory, dt)
        return np.concatenate([temporal, spectral])
```

### Step 4: Training Readout Layer

```python
class ReservoirReadout:
    def __init__(self, regularization=1e-6):
        self.regularization = regularization
        self.W_out = None
        
    def train(self, reservoir_states, targets):
        """
        Train readout using ridge regression.
        
        Args:
            reservoir_states: Matrix of reservoir states (samples × features)
            targets: Target outputs (samples × outputs)
        """
        # Ridge regression: W = (X^T X + λI)^{-1} X^T y
        X = reservoir_states
        y = targets
        
        self.W_out = np.linalg.solve(
            X.T @ X + self.regularization * np.eye(X.shape[1]),
            X.T @ y
        )
        
    def predict(self, reservoir_state):
        """Generate prediction from reservoir state."""
        return reservoir_state @ self.W_out
```

### Step 5: Complete Training Pipeline

```python
def train_reservoir(oscillator, data, params):
    """
    Complete training pipeline.
    
    Args:
        oscillator: ParametricOscillator instance
        data: Input time series
        params: Training parameters
    
    Returns:
        readout: Trained readout layer
        performance: Validation metrics
    """
    from scipy.integrate import solve_ivp
    
    # Parameters
    F0 = params['base_drive']
    epsilon = params['modulation_depth']
    washout = params['washout_steps']
    
    # Collect reservoir states
    states = []
    targets = []
    
    for i in range(len(data) - params['prediction_horizon']):
        # Encode input
        u_t = data[i]
        
        # Simulate oscillator response
        sol = solve_ivp(
            lambda t, y: oscillator.equations(t, y, F0, epsilon, u_t),
            [0, params['sampling_time']],
            params['initial_state'],
            method='RK45'
        )
        
        # Extract reservoir state (after washout)
        if i >= washout:
            state = extract_reservoir_state(sol.y)
            states.append(state)
            targets.append(data[i + params['prediction_horizon']])
    
    # Split train/test
    split = int(0.8 * len(states))
    train_states = np.array(states[:split])
    train_targets = np.array(targets[:split])
    test_states = np.array(states[split:])
    test_targets = np.array(targets[split:])
    
    # Train readout
    readout = ReservoirReadout()
    readout.train(train_states, train_targets)
    
    # Evaluate
    predictions = readout.predict(test_states)
    nmse = np.mean((predictions - test_targets)**2) / np.var(test_targets)
    
    return readout, {'nmse': nmse, 'predictions': predictions}
```

## Benchmarking: Chaotic Systems

### Mackey-Glass
```python
def mackey_glass(tau=17, beta=0.2, gamma=0.1, n=10, dt=1.0, steps=10000):
    """Generate Mackey-Glass chaotic time series."""
    x = np.ones(steps)
    for t in range(tau, steps):
        x[t] = x[t-1] + dt * (beta * x[t-tau] / (1 + x[t-tau]**n) - gamma * x[t-1])
    return x
```

### Rössler System
```python
def rossler(a=0.2, b=0.2, c=5.7, dt=0.01, steps=10000):
    """Generate Rössler attractor."""
    xyz = np.zeros((steps, 3))
    xyz[0] = [1.0, 1.0, 1.0]
    
    for i in range(1, steps):
        x, y, z = xyz[i-1]
        xyz[i, 0] = x + dt * (-y - z)
        xyz[i, 1] = y + dt * (x + a*y)
        xyz[i, 2] = z + dt * (b + z*(x - c))
    
    return xyz
```

### Lorenz System
```python
def lorenz(sigma=10, rho=28, beta=8/3, dt=0.01, steps=10000):
    """Generate Lorenz attractor."""
    xyz = np.zeros((steps, 3))
    xyz[0] = [1.0, 1.0, 1.0]
    
    for i in range(1, steps):
        x, y, z = xyz[i-1]
        xyz[i, 0] = x + dt * (sigma*(y - x))
        xyz[i, 1] = y + dt * (x*(rho - z) - y)
        xyz[i, 2] = z + dt * (x*y - beta*z)
    
    return xyz
```

## Parameter Optimization

### Finding Optimal Operating Point

```python
def optimize_parameters(oscillator, data, param_grid):
    """
    Grid search for optimal reservoir parameters.
    
    Args:
        param_grid: Dictionary with ranges for F0, epsilon, delta, etc.
    
    Returns:
        best_params: Optimal parameter set
        performance_map: NMSE across parameter space
    """
    results = []
    
    for F0 in param_grid['F0']:
        for epsilon in param_grid['epsilon']:
            for delta in param_grid['delta']:
                # Update oscillator parameters
                oscillator.omega_s = oscillator.omega_p/2 + delta
                
                # Train and evaluate
                _, metrics = train_reservoir(oscillator, data, {
                    'base_drive': F0,
                    'modulation_depth': epsilon,
                    # ... other params
                })
                
                results.append({
                    'F0': F0,
                    'epsilon': epsilon,
                    'delta': delta,
                    'nmse': metrics['nmse']
                })
    
    # Find best
    best = min(results, key=lambda x: x['nmse'])
    return best, results
```

### Bifurcation Analysis

```python
def bifurcation_analysis(oscillator, F0_range, fixed_params):
    """
    Map bifurcation structure and overlay with prediction error.
    
    Identifies alignment between low-error regions and parametric 
    resonance boundaries.
    """
    bifurcation_diagram = []
    
    for F0 in F0_range:
        # Simulate long trajectory
        states = simulate_steady_state(oscillator, F0, fixed_params)
        
        # Identify attractor
        attractor_type = classify_attractor(states)
        
        bifurcation_diagram.append({
            'F0': F0,
            'attractor': attractor_type,
            'max_amplitude': np.max(states[:, 0])
        })
    
    return bifurcation_diagram
```

## Design Principles

### Input Modulation Depth (ε)
- Controls accessible dynamical regimes
- Too low: limited to sub-threshold (linear)
- Too high: enters chaotic comb regime (incoherent)
- **Optimal**: At parametric resonance boundary

### Detuning (δ)
- Frequency mismatch from exact 2:1 resonance
- Small detuning: stronger resonance, narrower bandwidth
- Large detuning: weaker resonance, broader bandwidth
- **Trade-off**: Selectivity vs. robustness

### Damping Ratio (γ₁/γ₂)
- Controls memory duration in reservoir
- Higher damping: shorter memory, faster forgetting
- Lower damping: longer memory, slower dynamics
- **Balance**: Match task's temporal requirements

### Input Data Rate
- Must be slower than oscillator response time
- **Guideline**: Input period > 10 × oscillator period
- Prevents aliasing, allows proper encoding

## Physical Implementation

### Mechanical Oscillators
- Micro/nanomechanical resonators
- MEMS/NEMS implementations
- Quality factors Q > 10,000

### Optical Systems
- Optical parametric oscillators
- Whispering-gallery mode resonators
- High coherence, fast operation

### Superconducting Circuits
- Josephson parametric converters
- Circuit QED implementations
- Ultra-low loss, quantum-compatible

## Advantages

1. **Physical reservoir**: Computation in physical dynamics, not software
2. **Event-driven**: Only consumes power during operation
3. **Analog processing**: No ADC/DAC bottlenecks
4. **High speed**: GHz operation in optical/superconducting
5. **Scalable**: Multiple oscillators can be coupled

## Limitations

1. **Parameter sensitivity**: Requires careful tuning
2. **Operating regime**: Narrow optimal region
3. **Device variability**: Fabrication affects parameters
4. **Limited programmability**: Fixed physical parameters
5. **Readout complexity**: Requires sensitive measurement

## Applications

### Time-Series Prediction
- Financial forecasting
- Weather prediction
- Traffic flow modeling
- Renewable energy forecasting

### Signal Processing
- Channel equalization
- Noise reduction
- Pattern recognition

### Edge AI
- Low-power inference
- Real-time sensor processing
- Wearable devices

## Related Skills

- `superconducting-neuron-neuromorphic` - Similar physical implementation
- `neural-operator-stability-discovery` - Stability analysis methods
- `spiking-neural-network-analysis` - Neuromorphic computing principles

## Citation

```bibtex
@article{kumar2026neuromorphic,
  title={Neuromorphic Computing Based on Parametrically-Driven Oscillators and Frequency Combs},
  author={Kumar, Mahadev Sunil and Ganesan, Adarsh},
  journal={arXiv preprint arXiv:2604.21861},
  year={2026}
}
```
