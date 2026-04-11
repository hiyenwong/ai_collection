---
name: lattice-field-theory-neurons
description: Lattice Field Theory (LFT) framework for interpreting neural recordings from Brain-Computer Interfaces. Connects statistical mechanics with neuroscience via maximum entropy models.
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [neuroscience, lattice-field-theory, statistical-mechanics, maximum-entropy, brain-computer-interface, spike-rasters]
    source_paper: "Lattice Field Theory for a network of real neurons (arXiv:2604.05251)"
    authors: "Simone Franchini, Giampiero Bardella"
    published: "2026-04-06"
    venue: "LATTICE 2025"
---

# Lattice Field Theory for Neural Networks

Lattice Field Theory (LFT) framework for interpreting neural recordings from Brain-Computer Interfaces using statistical mechanics principles.

## Overview

This methodology introduces a simplified Lattice Field Theory (LFT) framework that allows experimental recordings from major Brain-Computer Interfaces (BCIs) to be interpreted in a simple and physically grounded way.

From a neuroscience perspective, the method modifies the Maximum Entropy model for neural networks to account for the time evolution of the system, interpretable as another version of the Free Energy Principle (FEP).

## Core Concepts

### Lattice Field Theory (LFT)

LFT provides a mathematical framework to:
- Model neural activity as field configurations on a lattice
- Capture spatial and temporal correlations
- Connect microscopic dynamics to macroscopic behavior

### Maximum Entropy Extension

Traditional Maximum Entropy models:
- Capture static correlations between neurons
- Model pairwise interactions
- Ignore temporal dynamics

This extension:
- Incorporates time evolution
- Models temporal dependencies
- Maintains interpretability

### Free Energy Principle Connection

The framework can be interpreted through the Free Energy Principle:
- Neural systems minimize variational free energy
- Perception as inference
- Action as minimizing expected free energy

## Mathematical Framework

### Field Configuration

```python
class LatticeNeuralField:
    """
    Lattice Field Theory model for neural networks
    """
    def __init__(self, lattice_size, time_steps):
        self.lattice = np.zeros((lattice_size, time_steps))
        self.interaction_kernel = self.build_kernel()
        
    def build_kernel(self):
        """Build spatial-temporal interaction kernel"""
        # Local interactions + temporal dependencies
        kernel = {
            'spatial': self.spatial_coupling(),
            'temporal': self.temporal_coupling()
        }
        return kernel
    
    def field_energy(self, configuration):
        """
        Compute energy of field configuration
        
        E[φ] = Σᵢⱼ Jᵢⱼ φᵢ φⱼ + Σᵢ hᵢ φᵢ + temporal_terms
        """
        spatial_energy = self.spatial_interaction(configuration)
        temporal_energy = self.temporal_dynamics(configuration)
        external_field = self.external_coupling(configuration)
        
        return spatial_energy + temporal_energy + external_field
    
    def partition_function(self, beta):
        """
        Compute partition function
        Z = Σ_{configs} exp(-β E[config])
        """
        # Monte Carlo estimation or analytical approximation
        return self.estimate_partition(beta)
    
    def free_energy(self, beta):
        """Compute Helmholtz free energy"""
        Z = self.partition_function(beta)
        return -np.log(Z) / beta
```

### Maximum Entropy with Dynamics

```python
class DynamicMaxEntropy:
    """
    Maximum entropy model with temporal dynamics
    """
    def __init__(self, n_neurons, history_length):
        self.n_neurons = n_neurons
        self.history = history_length
        
        # Constraints: firing rates and correlations
        self.target_rates = None
        self.target_correlations = None
        
    def fit(self, spike_rasters):
        """
        Fit model to spike raster data
        
        Args:
            spike_rasters: Binary matrix (neurons × time)
        """
        # Compute empirical statistics
        self.target_rates = np.mean(spike_rasters, axis=1)
        self.target_correlations = self.compute_correlations(spike_rasters)
        
        # Lagrange multipliers via gradient descent
        self.lagrange_multipliers = self.solve_for_multipliers()
        
    def probability(self, state, history):
        """
        Probability of state given history
        
        P(sₜ | sₜ₋₁, ..., sₜ₋ₕ) ∝ exp(Σᵢ λᵢ sᵢ + Σᵢⱼ λᵢⱼ sᵢ sⱼ + ...)
        """
        energy = self.compute_energy(state, history)
        return np.exp(-energy) / self.Z
```

## Applications

### Brain-Computer Interfaces

- **Chronic Multi-site BCIs**: Interpret long-term recordings
- **Spike Raster Analysis**: Model single-neuron activity
- **Population Dynamics**: Understand collective neural behavior

### Theoretical Neuroscience

- **Statistical Mechanics of Neural Systems**: Bridge physics and biology
- **Information Processing**: Quantify neural computation
- **Dynamical Systems**: Analyze attractors and stability

## Key Insights

1. **Physical Interpretation**: Neural activity as field configurations
2. **Statistical Mechanics**: Thermodynamic analogies for neural systems
3. **Time Evolution**: Dynamic extension of static maximum entropy models
4. **BCI Compatibility**: Tailored for chronic multi-site recordings

## Implementation Notes

### For Spike Raster Data

```python
def analyze_spike_rasters(rasters, bin_size=1):
    """
    Analyze spike raster data using LFT framework
    
    Args:
        rasters: List of spike rasters (neurons × time)
        bin_size: Time bin size in ms
    
    Returns:
        Field model parameters and statistics
    """
    # Initialize LFT model
    model = LatticeNeuralField(
        lattice_size=rasters[0].shape[0],
        time_steps=rasters[0].shape[1]
    )
    
    # Fit to data
    model.fit(rasters)
    
    # Extract physical quantities
    free_energy = model.free_energy(beta=1.0)
    entropy = model.entropy()
    specific_heat = model.specific_heat()
    
    return {
        'free_energy': free_energy,
        'entropy': entropy,
        'specific_heat': specific_heat,
        'parameters': model.get_parameters()
    }
```

## References

- Franchini, S., & Bardella, G. (2026). Lattice Field Theory for a network of real neurons. *LATTICE 2025*.
- Bardella et al. (2024). Entropy 26 (6), 495.

## Related

- [[maximum-entropy-models]]
- [[free-energy-principle]]
- [[statistical-mechanics-neuroscience]]
- [[brain-computer-interface]]
