# Prospective Coding and Path Integration via Self-Organizing Neural Networks

---
created: 2026-06-16
arxiv_id: 2606.14649
authors: Facundo Emina, Emilio Kropff
categories: q-bio.NC, cond-mat.dis-nn, nlin.AO
published: 2026-06-12
activation: prospective coding, path integration, continuous attractor, self-organization, Hebbian plasticity, firing-rate adaptation, entorhinal cortex, neural dynamics
---

## Summary

This work reveals how continuous attractor connectivity and computational properties self-organize through Hebbian plasticity, firing-rate adaptation, and global inhibition. It demonstrates that prospective coding and path integration naturally emerge as equilibrium solutions of a single self-organizing competitive network.

## Key Findings

### Self-Organization Mechanism
- Translationally invariant inputs naturally drive the emergence of **stable, Gaussian-profiled feedforward weights**
- **Hebbian plasticity** + **firing-rate adaptation** + **global inhibition** → structured connectivity
- No pre-wired recurrent connectivity required

### Prospective Coding Emergence
- **Anticipatory dynamics arise spontaneously** in feedforward architectures
- Activity bump shifts forward without requiring recurrent excitatory collaterals
- Predictive shift can be linearly amplified across **multilayer networks**
- Consistent with anticipatory activity in **superficial layers of entorhinal cortex**

### Path Integration
- Modulating network with **time-varying baseline current encoding speed**
- System adjusts intrinsic velocity → **precise unidirectional path integrator**
- Self-sustaining moving bump of activity when recurrent interactions introduced

### Biological Interpretation
- **Continuous attractor** properties are NOT manually engineered
- Naturally co-emergent properties of **single self-organizing competitive network**
- Suggests biological mechanism for grid cell formation in entorhinal cortex

## Technical Framework

### Network Architecture
```
Components:
1. Hebbian plasticity: Δw_ij ∝ x_i · x_j
2. Firing-rate adaptation: x_i(t) → x_i(t) · decay_factor
3. Global inhibition: ∑_i x_i ≤ threshold

Emergence Process:
Input (translationally invariant) → 
Feedforward weights (Gaussian profile) → 
Activity bump → 
Predictive shift → 
Path integration (with speed modulation)
```

### Mathematical Model
- **Feedforward weight emergence**: Gaussian profiles from Hebbian learning
- **Anticipatory dynamics**: Activity bump forward shift velocity ∝ adaptation rate
- **Path integration**: Velocity encoding via baseline current modulation

## Implications

### For Computational Neuroscience
1. **Continuous attractor networks (CANNs)** can self-organize
2. Grid cell connectivity may emerge from **simple learning rules**
3. Entorhinal cortex anticipatory activity explained

### For Neural Network Design
1. **Self-organizing competitive networks** for spatial representations
2. **Feedforward architectures** can exhibit anticipatory dynamics
3. **Speed modulation** enables precise path integration

### For AI Applications
1. **Navigation systems** with self-organizing spatial memory
2. **Predictive coding** architectures without recurrent design
3. **Path integration** for autonomous agents

## Experimental Validation

### Model Predictions
- Feedforward layers show anticipatory activity shift
- Multilayer networks amplify prediction linearly
- Speed modulation enables precise integration

### Biological Correspondence
- Matches entorhinal cortex superficial layer activity
- Consistent with grid cell formation observations
- Explains hippocampal-entorhinal circuit behavior

## Implementation Guidelines

### Basic Self-Organizing CANN
```python
# Core components:
class SelfOrganizingCANN:
    def __init__(self, n_neurons, adaptation_rate, global_inhibition):
        self.weights = np.zeros((n_neurons, n_neurons))
        self.adaptation_rate = adaptation_rate
        self.global_inhibition = global_inhibition
    
    def hebbian_update(self, activity):
        # Gaussian weight emergence
        self.weights += activity * activity.T
        
    def apply_adaptation(self, activity):
        return activity * (1 - self.adaptation_rate)
    
    def apply_global_inhibition(self, activity):
        total = np.sum(activity)
        if total > self.global_inhibition:
            activity *= self.global_inhibition / total
        return activity
```

### Path Integration Extension
```python
# Add speed modulation:
def modulate_speed(baseline_current, velocity):
    return baseline_current * velocity

# Self-sustaining activity with recurrence:
def add_recurrence(self, recurrent_weights, activity):
    return activity + recurrent_weights @ activity
```

## Related Research

### Grid Cell Formation
- McNaughton et al. (2006) - Path integration in hippocampus
- Burak & Fiete (2009) - Accurate path integration in CANNs

### Predictive Coding
- Rao & Ballard (1999) - Predictive coding in visual cortex
- Friston (2010) - Free energy principle

### Self-Organization
- Kohonen (1982) - Self-organizing maps
- Miikkulainen et al. (2005) - Self-organizing maps for visual cortex

## Future Directions

1. **Experimental validation** in entorhinal cortex recordings
2. **Multilayer network** implementation for amplified prediction
3. **Hybrid architectures** combining feedforward and recurrent components
4. **Navigation applications** in autonomous agents

## Key References

- Emina & Kropff (2026) - This paper
- Burak & Fiete (2009) - CANN path integration
- McNaughton et al. (2006) - Grid cells and path integration