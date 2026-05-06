---
name: spiking-reservoir-robustness
description: "Robust spiking reservoir computing framework bridging theory and practice. Introduces robustness interval for tuning reservoirs at edge-of-chaos under experimental uncertainty. Use when working with: (1) Spiking neural networks, (2) Reservoir computing, (3) Neuromorphic computing, (4) Temporal pattern processing. Activation: spiking reservoirs, robustness interval, edge-of-chaos, LIF reservoirs, temporal processing."
---

# Spiking Reservoir Robustness

Robust spiking reservoir computing framework bridging theory and practice. Introduces robustness interval for tuning reservoirs at edge-of-chaos under experimental uncertainty.

## Core Concept

Spiking reservoir computing provides energy-efficient temporal processing, but reliably tuning reservoirs to operate at the edge-of-chaos is challenging due to experimental uncertainty. This framework introduces the **robustness interval**—an operational measure of the hyperparameter range where a reservoir maintains performance above task-dependent thresholds.

## Theoretical Background

### Edge of Chaos

Neural computation is most effective near the boundary between ordered and chaotic dynamics:

- **Ordered regime**: Activity dies out or becomes periodic
- **Chaotic regime**: Activity becomes unpredictable and unstable
- **Edge of chaos**: Balanced dynamics enabling rich computation

### Robustness Interval

The hyperparameter range where performance stays above threshold:

```
Robustness Interval = [λ_min, λ_max]
where: Performance(λ) > Threshold for all λ in [λ_min, λ_max]
```

## Implementation

### Leaky Integrate-and-Fire (LIF) Neuron

```python
import numpy as np
from typing import Tuple, List

class LIFNeuron:
    """Leaky Integrate-and-Fire neuron model."""
    
    def __init__(
        self,
        tau_mem: float = 20.0,      # Membrane time constant (ms)
        tau_syn: float = 5.0,       # Synaptic time constant (ms)
        v_thresh: float = 1.0,      # Threshold voltage
        v_reset: float = 0.0,       # Reset voltage
        dt: float = 1.0             # Time step (ms)
    ):
        self.tau_mem = tau_mem
        self.tau_syn = tau_syn
        self.v_thresh = v_thresh
        self.v_reset = v_reset
        self.dt = dt
        
        # State variables
        self.v = v_reset  # Membrane potential
        self.I = 0.0      # Synaptic current
        self.spike = False
    
    def update(self, I_syn: float) -> bool:
        """Update neuron state for one time step."""
        # Update synaptic current
        self.I += self.dt / self.tau_syn * (-self.I + I_syn)
        
        # Update membrane potential
        self.v += self.dt / self.tau_mem * (-self.v + self.I)
        
        # Check for spike
        self.spike = self.v >= self.v_thresh
        
        if self.spike:
            self.v = self.v_reset
        
        return self.spike
    
    def reset(self):
        """Reset neuron to initial state."""
        self.v = self.v_reset
        self.I = 0.0
        self.spike = False
```

### Spiking Reservoir

```python
class SpikingReservoir:
    """Spiking neural network reservoir."""
    
    def __init__(
        self,
        n_neurons: int = 1000,
        n_inputs: int = 10,
        connection_prob: float = 0.1,
        spectral_radius: float = 1.0,
        inhibitory_ratio: float = 0.2,
        **neuron_params
    ):
        self.n_neurons = n_neurons
        self.n_inputs = n_inputs
        
        # Initialize neurons
        self.neurons = [LIFNeuron(**neuron_params) for _ in range(n_neurons)]
        
        # Initialize weights
        self.W = self._initialize_weights(
            n_neurons, connection_prob, spectral_radius, inhibitory_ratio
        )
        
        # Input weights
        self.W_in = np.random.randn(n_neurons, n_inputs) * 0.1
        
        # Track spikes
        self.spike_history = []
        
    def _initialize_weights(
        self,
        n: int,
        p: float,
        rho: float,
        inhibitory_ratio: float
    ) -> np.ndarray:
        """Initialize recurrent weights."""
        # Random sparse connectivity
        W = np.random.randn(n, n) * (np.random.rand(n, n) < p).astype(float)
        
        # Scale to desired spectral radius
        eigs = np.linalg.eigvals(W)
        max_eig = np.max(np.abs(eigs))
        W *= rho / max_eig
        
        # Make some neurons inhibitory
        n_inh = int(n * inhibitory_ratio)
        inh_indices = np.random.choice(n, n_inh, replace=False)
        W[inh_indices] = -np.abs(W[inh_indices])
        
        return W
    
    def simulate(
        self,
        input_signal: np.ndarray,
        duration: int
    ) -> Tuple[np.ndarray, List]:
        """
        Simulate reservoir dynamics.
        
        Args:
            input_signal: [duration, n_inputs] input signal
            duration: Number of time steps
        
        Returns:
            states: [duration, n_neurons] membrane potentials
            spikes: List of spike times per neuron
        """
        states = np.zeros((duration, self.n_neurons))
        spikes = [[] for _ in range(self.n_neurons)]
        
        for t in range(duration):
            # Current input
            I_ext = self.W_in @ input_signal[t]
            
            # Recurrent input
            spike_vector = np.array([n.spike for n in self.neurons]).astype(float)
            I_rec = self.W @ spike_vector
            
            # Update each neuron
            for i, neuron in enumerate(self.neurons):
                I_total = I_ext[i] + I_rec[i]
                fired = neuron.update(I_total)
                
                if fired:
                    spikes[i].append(t)
                
                states[t, i] = neuron.v
        
        return states, spikes
    
    def reset(self):
        """Reset all neurons."""
        for neuron in self.neurons:
            neuron.reset()
```

### Robustness Analysis

```python
class RobustnessAnalyzer:
    """Analyze robustness interval of spiking reservoir."""
    
    def __init__(self, reservoir: SpikingReservoir):
        self.reservoir = reservoir
    
    def evaluate_performance(
        self,
        parameter_name: str,
        parameter_value: float,
        task: 'ReservoirTask',
        n_trials: int = 5
    ) -> float:
        """
        Evaluate reservoir performance at specific parameter value.
        
        Args:
            parameter_name: Name of parameter to vary
            parameter_value: Value to test
            task: Task to evaluate on
            n_trials: Number of trials for averaging
        
        Returns:
            Average performance score
        """
        scores = []
        
        for _ in range(n_trials):
            # Set parameter
            self._set_parameter(parameter_name, parameter_value)
            
            # Evaluate on task
            score = task.evaluate(self.reservoir)
            scores.append(score)
        
        return np.mean(scores)
    
    def find_robustness_interval(
        self,
        parameter_name: str,
        param_range: Tuple[float, float],
        threshold: float,
        task: 'ReservoirTask',
        n_points: int = 50
    ) -> Tuple[float, float]:
        """
        Find robustness interval for a parameter.
        
        Args:
            parameter_name: Parameter to analyze
            param_range: (min, max) range to search
            threshold: Performance threshold
            task: Task for evaluation
            n_points: Number of parameter values to test
        
        Returns:
            (lambda_min, lambda_max) robustness interval
        """
        param_values = np.linspace(param_range[0], param_range[1], n_points)
        performances = []
        
        for val in param_values:
            perf = self.evaluate_performance(parameter_name, val, task)
            performances.append(perf)
        
        # Find interval above threshold
        above_threshold = np.array(performances) >= threshold
        
        if not np.any(above_threshold):
            return (param_range[0], param_range[0])  # No robust region
        
        # Find contiguous region
        indices = np.where(above_threshold)[0]
        lambda_min = param_values[indices[0]]
        lambda_max = param_values[indices[-1]]
        
        return (lambda_min, lambda_max)
    
    def _set_parameter(self, name: str, value: float):
        """Set reservoir parameter."""
        if name == 'spectral_radius':
            # Rescale weights
            eigs = np.linalg.eigvals(self.reservoir.W)
            current_radius = np.max(np.abs(eigs))
            self.reservoir.W *= value / current_radius
        elif name == 'tau_mem':
            for neuron in self.reservoir.neurons:
                neuron.tau_mem = value
        elif name == 'connection_prob':
            # Reinitialize with new probability
            n = self.reservoir.n_neurons
            self.reservoir.W = self.reservoir._initialize_weights(
                n, value, 1.0, 0.2
            )
```

## Tasks

### Temporal Pattern Recognition

```python
class TemporalPatternTask:
    """Recognize temporal patterns in spike trains."""
    
    def __init__(self, patterns: List[np.ndarray]):
        self.patterns = patterns
    
    def evaluate(self, reservoir: SpikingReservoir) -> float:
        """Evaluate reservoir on pattern recognition."""
        accuracies = []
        
        for pattern in self.patterns:
            # Present pattern
            reservoir.reset()
            states, _ = reservoir.simulate(pattern, len(pattern))
            
            # Readout (would train readout weights)
            # For now, use final state as feature
            features = states[-1]
            
            # Classification accuracy (simplified)
            accuracy = self._classify(features, pattern)
            accuracies.append(accuracy)
        
        return np.mean(accuracies)
    
    def _classify(self, features: np.ndarray, pattern: np.ndarray) -> float:
        """Simplified classification."""
        # Placeholder: would use trained classifier
        return np.random.random()  # Replace with actual classification
```

### MNIST with Temporal Coding

```python
class MNISTTemporalTask:
    """MNIST classification using temporal coding."""
    
    def __init__(self, images: np.ndarray, labels: np.ndarray):
        self.images = images
        self.labels = labels
    
    def encode_temporal(self, image: np.ndarray, duration: int = 100) -> np.ndarray:
        """
        Encode image as temporal spike pattern using rate coding.
        
        Args:
            image: [28, 28] grayscale image
            duration: Time duration in ms
        
        Returns:
            spike_pattern: [duration, 784] spike train
        """
        # Normalize and flatten
        rates = image.flatten() / 255.0
        
        # Generate Poisson spikes
        spike_pattern = np.random.random((duration, 784)) < rates[None, :]
        
        return spike_pattern.astype(float)
    
    def evaluate(self, reservoir: SpikingReservoir) -> float:
        """Evaluate on MNIST."""
        # Sample subset for evaluation
        n_test = min(100, len(self.images))
        indices = np.random.choice(len(self.images), n_test, replace=False)
        
        correct = 0
        for idx in indices:
            image = self.images[idx]
            label = self.labels[idx]
            
            # Encode as spikes
            spike_input = self.encode_temporal(image)
            
            # Run reservoir
            reservoir.reset()
            states, _ = reservoir.simulate(spike_input, len(spike_input))
            
            # Readout (would need trained weights)
            # Simplified: use mean firing rate
            prediction = self._predict(states)
            
            if prediction == label:
                correct += 1
        
        return correct / n_test
    
    def _predict(self, states: np.ndarray) -> int:
        """Predict label from reservoir states."""
        # Placeholder: would use trained readout
        return np.random.randint(0, 10)
```

## Best Practices

### Reservoir Design

1. **Spectral Radius**: Start with 0.9-1.1 for edge-of-chaos
2. **Connectivity**: Sparse connectivity (5-20%) works well
3. **Neuron Diversity**: Vary time constants for rich dynamics
4. **Input Scaling**: Scale inputs to match neuron sensitivity

### Robustness Tuning

1. **Parameter Sweeps**: Test wide range before fine-tuning
2. **Threshold Selection**: Set based on application requirements
3. **Multiple Parameters**: Analyze interactions between parameters
4. **Noise Robustness**: Test with input noise

### Readout Training

1. **Ridge Regression**: Use regularized linear regression
2. **Time Constants**: Consider different readout time windows
3. **Feature Selection**: Select informative neurons
4. **Cross-Validation**: Validate on held-out data

## References

- Paper: "Bridging Theory and Practice in Crafting Robust Spiking Reservoirs" (arXiv:2604.06395v1, 2026)
- Maass et al. (2002): Real-time computing without stable states
- Jaeger (2001): The "echo state" approach to analyzing and training recurrent neural networks
- Bertschinger & Natschlager (2004): Real-time computation at the edge of chaos

## Activation Keywords

- spiking reservoirs
- robustness interval
- edge-of-chaos
- LIF neurons
- reservoir computing
- temporal pattern processing
- neuromorphic computing
- spiking neural networks
