---
name: parametric-oscillator-neuromorphic
description: "Neuromorphic computing based on parametrically-driven oscillators and frequency combs. Implements reservoir computing using 2:1 parametric resonance. Activation: parametric oscillator, neuromorphic, reservoir computing, frequency comb, nonlinear dynamics."
---

# Parametrically-Driven Oscillator Neuromorphic Computing

> Neuromorphic computing architecture using parametrically-driven oscillators for reservoir computing and high-dimensional transformation.

## Metadata
- **Source**: arXiv:2604.21861v1
- **Authors**: Mahadev Sunil Kumar, Adarsh Ganesan
- **Published**: 2026-04-23
- **Category**: Physics, Neuromorphic Computing

## Core Methodology

### Key Innovation
A neuromorphic computing platform based on parametrically-driven oscillators that leverages nonlinear mode coupling and intrinsic dynamics to achieve both memory and high-dimensional transformation capabilities. The system operates across distinct dynamical regimes including sub-threshold, parametric amplification, and frequency comb generation.

### Technical Framework

#### 1. Physical System
- **Two-mode system** exhibiting 2:1 parametric resonance
- Parametrically driven oscillator with nonlinear mode coupling
- Frequency comb generation for parallel processing

#### 2. Operating Regimes
1. **Sub-threshold regime**: Low-amplitude oscillations for input encoding
2. **Parametric amplification regime**: Signal gain and nonlinear transformation
3. **Frequency comb regime**: High-dimensional feature expansion

#### 3. Reservoir Computing Implementation
- Input mapping: Temporal signals modulate oscillator parameters
- Reservoir dynamics: Intrinsic nonlinear mode coupling provides temporal integration
- Readout: Frequency comb components serve as high-dimensional features

### Implementation Steps

1. **System Setup**
   - Configure parametric oscillator with 2:1 resonance condition
   - Tune driving frequency and amplitude
   - Establish stable operating point

2. **Input Encoding**
   - Modulate oscillator parameters with input signal
   - Map temporal inputs to amplitude/phase variations

3. **Reservoir Computation**
   - Allow system to evolve through nonlinear dynamics
   - Capture frequency comb spectrum as reservoir states

4. **Output Readout**
   - Train linear readout weights on frequency components
   - Apply to new inputs for inference

## Code Example

```python
import numpy as np
from scipy.integrate import odeint

class ParametricOscillatorReservoir:
    """
    Parametrically-driven oscillator reservoir computer.
    Based on 2:1 parametric resonance for neuromorphic computation.
    """
    
    def __init__(self, omega_0=1.0, gamma=0.1, epsilon=0.3, 
                 driving_freq_ratio=2.0, num_modes=2):
        self.omega_0 = omega_0  # Natural frequency
        self.gamma = gamma      # Damping coefficient
        self.epsilon = epsilon  # Parametric driving strength
        self.driving_omega = driving_freq_ratio * omega_0
        self.num_modes = num_modes
        self.W_out = None       # Output weights
        
    def equations_of_motion(self, state, t, input_signal):
        """
        Parametrically driven oscillator dynamics.
        
        state: [x, v, y, w] for two coupled modes
        """
        x, v, y, w = state
        
        # Mode 1: Parametrically driven
        parametric_drive = self.epsilon * np.cos(self.driving_omega * t)
        dxdt = v
        dvdt = -(self.omega_0**2 + parametric_drive) * x - self.gamma * v
        dvdt += 0.1 * input_signal(t)  # Input coupling
        
        # Mode 2: Coupled to mode 1 (2:1 resonance)
        dydt = w
        dwdt = -(2*self.omega_0)**2 * y - self.gamma * w
        dwdt += 0.05 * x**2  # Nonlinear coupling from mode 1
        
        return [dxdt, dvdt, dydt, dwdt]
    
    def compute_frequency_comb(self, states):
        """Extract frequency comb features from reservoir states."""
        # FFT-based feature extraction
        features = []
        for mode in range(self.num_modes):
            signal = states[:, 2*mode]  # Position of each mode
            fft = np.fft.fft(signal)
            features.extend(np.abs(fft[:len(fft)//4]))  # First quarter frequencies
        return np.array(features)
    
    def fit(self, X_train, y_train, T=10.0, dt=0.01):
        """
        Train reservoir readout weights.
        
        X_train: List of input time series
        y_train: Target outputs
        """
        reservoir_states = []
        
        for x_input in X_train:
            # Define input function
            t = np.arange(0, T, dt)
            input_func = lambda tau: np.interp(tau, t, x_input)
            
            # Evolve reservoir
            initial_state = [0.1, 0, 0.05, 0]
            states = odeint(self.equations_of_motion, initial_state, t, 
                          args=(input_func,))
            
            # Extract features
            features = self.compute_frequency_comb(states)
            reservoir_states.append(features)
        
        # Ridge regression for readout
        X_matrix = np.array(reservoir_states)
        self.W_out = np.linalg.solve(
            X_matrix.T @ X_matrix + 1e-6 * np.eye(X_matrix.shape[1]),
            X_matrix.T @ y_train
        )
        
        return self
    
    def predict(self, X_test, T=10.0, dt=0.01):
        """Generate predictions for test inputs."""
        predictions = []
        
        for x_input in X_test:
            t = np.arange(0, T, dt)
            input_func = lambda tau: np.interp(tau, t, x_input)
            
            initial_state = [0.1, 0, 0.05, 0]
            states = odeint(self.equations_of_motion, initial_state, t,
                          args=(input_func,))
            
            features = self.compute_frequency_comb(states)
            pred = features @ self.W_out
            predictions.append(pred)
        
        return np.array(predictions)


# Example usage: Mackey-Glass prediction
from sklearn.metrics import mean_squared_error

# Generate Mackey-Glass time series
def mackey_glass(beta=0.2, gamma=0.1, n=10, tau=17, dt=0.1, T=5000):
    t = np.arange(0, T, dt)
    x = np.ones_like(t)
    delay_steps = int(tau / dt)
    
    for i in range(delay_steps, len(t)):
        x[i] = x[i-1] + dt * (beta * x[i-delay_steps] / (1 + x[i-delay_steps]**n) - gamma * x[i-1])
    
    return x[1000:]  # Remove transient

# Prepare data
mg_series = mackey_glass()
window_size = 100

X_train = []
y_train = []
for i in range(0, len(mg_series) - window_size - 10, 10):
    X_train.append(mg_series[i:i+window_size])
    y_train.append(mg_series[i+window_size+10])  # 10-step ahead prediction

X_train = np.array(X_train[:100])  # Use first 100 samples
y_train = np.array(y_train[:100])

# Train and evaluate
reservoir = ParametricOscillatorReservoir(omega_0=1.0, gamma=0.1, epsilon=0.3)
reservoir.fit(X_train, y_train, T=10.0, dt=0.01)

print("Reservoir computing with parametric oscillator trained!")
```

## Applications

- **Temporal signal processing**: Time series prediction, filtering
- **Pattern recognition**: Spoken digit recognition, gesture classification
- **Dynamical systems**: Chaotic system prediction, attractor reconstruction
- **Edge computing**: Low-power analog neuromorphic implementations

## Advantages

1. **Energy efficiency**: Analog computation with passive components
2. **Parallel processing**: Frequency comb enables parallel feature extraction
3. **Temporal integration**: Natural memory through oscillator dynamics
4. **Scalability**: Array of parametric oscillators for large-scale systems

## Pitfalls

- Requires precise tuning of parametric resonance condition
- Sensitive to noise in analog implementations
- Limited to tasks matching the oscillator's intrinsic timescales
- Frequency comb complexity vs. readout accuracy tradeoff

## Related Skills

- `neuromorphic-reservoir-computing`: General reservoir computing
- `snn-learning-neuromorphic`: Spiking neural networks
- `memristor-preprocessing-reservoir`: Memristor-based reservoirs
- `spiking-oscillation-mapping`: Oscillatory dynamics in SNNs

## References

- Kumar, M. S., & Ganesan, A. (2026). Neuromorphic Computing Based on Parametrically-Driven Oscillators and Frequency Combs. arXiv:2604.21861v1.
