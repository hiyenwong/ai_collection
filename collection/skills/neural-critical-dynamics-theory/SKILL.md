---
name: neural-critical-dynamics-theory
version: v1.0.0
last_updated: 2026-04-19
description: Theory of critical dynamics and information processing in neural networks. Neural systems at critical points exhibit optimal information processing, maximal dynamic range, and power-law distributed avalanches. Provides methods for identifying, analyzing, and exploiting critical regimes in both biological and artificial neural networks. Applicable to critical brain hypothesis, neural avalanche analysis, optimal computation regimes. Trigger: neural criticality, critical dynamics, neural avalanches, power law neural activity, edge of chaos neural networks
---

# Critical Dynamics and Information Processing in Neural Networks

## Description

A comprehensive theoretical framework for understanding how neural networks operating at critical points achieve optimal information processing capabilities. Critical dynamics are characterized by power-law distributed neural avalanches, maximal dynamic range, long-range correlations, and optimal computational capacity.

Based on: "Critical Dynamics and Information Processing in Neural Networks" (arXiv:2506.20978, June 2025)

## Critical Point Theory

### What is Criticality?

A neural network is at a critical point when it sits at the phase transition between ordered and chaotic regimes:

- **Ordered regime**: Activity quickly dies out, limited computational capacity
- **Chaotic regime**: Activity explodes, unstable and unpredictable
- **Critical regime**: Activity persists with rich dynamics, optimal for computation

### Identifying Critical Dynamics

```python
class CriticalityAnalyzer:
    """Analyze whether a neural system operates at criticality."""
    
    def __init__(self):
        pass
    
    def neural_avalanche_analysis(self, spike_train):
        """
        Detect neural avalanches and test for power-law distribution.
        
        An avalanche is a cascade of activity between periods of silence.
        """
        avalanches = self._detect_avalanches(spike_train)
        
        # Avalanche size distribution
        sizes = [len(avalanche) for avalanche in avalanches]
        
        # Fit power law: P(s) ~ s^(-tau)
        tau, log_likelihood, KS_stat = self._fit_power_law(sizes)
        
        return {
            "power_law_exponent": tau,
            "goodness_of_fit": KS_stat,
            "is_critical": KS_stat < 0.1  # Critical if power law fits well
        }
    
    def branching_parameter(self, activity):
        """
        Compute the branching parameter sigma.
        
        sigma = 1: critical
        sigma < 1: subcritical (ordered)
        sigma > 1: supercritical (chaotic)
        """
        # Ratio of activity in consecutive time bins
        sigma = np.mean(activity[1:]) / np.mean(activity[:-1])
        return sigma
    
    def susceptibility(self, network, perturbation_size=0.01):
        """
        Measure network response to small perturbations.
        At criticality, susceptibility diverges.
        """
        response = self._measure_response(network, perturbation_size)
        return response / perturbation_size
```

## Information Processing at Criticality

### Key Advantages

1. **Maximal dynamic range**: Response to stimuli spans the widest range
2. **Optimal information transmission**: Mutual information is maximized
3. **Long-range correlations**: Activity patterns span multiple scales
4. **Computational richness**: Largest repertoire of distinct activity patterns
5. **Balanced stability-flexibility**: Stable enough to store, flexible enough to compute

### Measuring Computational Capacity

```python
def computational_capacity(network, input_data):
    """
    Quantify the computational capacity of a network.
    Higher at criticality.
    """
    # Count distinct activity patterns in response to different inputs
    patterns = set()
    for inp in input_data:
        activity = network.run(inp)
        patterns.add(hash_activity(activity))
    
    return len(patterns) / len(input_data)  # Pattern diversity ratio

def memory_capacity(network, max_delay=100):
    """
    Measure how far back the network can remember inputs.
    """
    capacities = []
    for delay in range(1, max_delay):
        # Test if network state at time t contains info about input at t-delay
        cap = mutual_information(network.states, network.inputs[:, :-delay])
        capacities.append(cap)
    return np.sum(capacities)
```

## Tuning Networks to Criticality

### Self-Organized Criticality

```python
class SelfOrganizingCriticalNetwork:
    """
    Network that self-organizes to critical point without parameter tuning.
    """
    
    def __init__(self, n_neurons):
        self.weights = torch.randn(n_neurons, n_neurons) * 0.1
        self.threshold = 1.0
    
    def homeostatic_plasticity(self, activity, target_rate=0.1):
        """
        Adjust thresholds to maintain target firing rate.
        Drives network toward criticality.
        """
        error = activity.mean() - target_rate
        self.threshold += learning_rate * error
    
    def synaptic_scaling(self, activity, target_activity=1.0):
        """
        Scale synaptic weights to maintain target activity level.
        """
        scale = target_activity / (activity.std() + 1e-8)
        self.weights *= scale
```

### Branching Process Parameter Control

```python
def tune_to_criticality(network, target_sigma=1.0, steps=1000):
    """
    Adjust network parameters to achieve critical dynamics (sigma=1).
    """
    for step in range(steps):
        # Run network
        activity = network.run(input_data)
        
        # Measure branching parameter
        sigma = analyzer.branching_parameter(activity)
        
        # Adjust gain to move toward criticality
        if sigma > target_sigma:
            network.gain *= 0.99  # Reduce gain
        else:
            network.gain *= 1.01  # Increase gain
```

## Applications

- **Brain-inspired AI**: Design networks with biological critical dynamics
- **Neuromorphic computing**: Exploit critical regimes for efficient computation
- **Neuroscience**: Test critical brain hypothesis
- **Reservoir computing**: Optimize reservoirs at criticality
