---
name: spiking-free-energy-control
description: >
  Spiking neural network control framework based on the Free Energy Principle (FEP) and Active Inference.
  Neurons fire only when they reduce free energy of internal representation, achieving highly sparse 
  activity with robust control. Matches performance of non-spiking frameworks while offering resilience 
  against sensory noise, synaptic noise, delays, and neuron silencing. Use when designing spiking control 
  systems, neuromorphic control algorithms, active inference with SNNs, energy-efficient robotics control, 
  or studying biological plausibility of active inference. Triggered by: spiking control, free energy 
  principle SNN, active inference spiking, neuromorphic control, spike-based free energy, SFEC, 
  spiking free energy constraint, robust spiking controller, bio-plausible control, spiking active inference.
license: arXiv perpetual non-exclusive
---

# Spiking Free Energy Control (SFEC)

Based on: Urbano, Lanillos & Keemink, "Efficient and robust control with spikes that constrain free energy" (arXiv:2603.09729)

## Core Innovation

Bridges the gap between the Free Energy Principle/Active Inference (computational level) and 
biophysically plausible spiking neural circuit implementations (mechanistic level).

**Key insight**: Neurons only fire when firing reduces free energy — spikes are constrained by 
free energy minimization, not just threshold crossings.

## Framework Components

### SFEC (Spiking Free Energy Constraint) Controller

```
For each neuron:
  1. Compute prediction error: ε = observation - prediction
  2. Compute free energy gradient: ∂F/∂representation
  3. Generate spike ONLY IF: spike reduces free energy (∂F/∂t < 0)
  4. Update internal state via spike-triggered plasticity
```

### Spiking Control Network (SCN) Architecture

- **Encoder layer**: Converts continuous sensory input to spike trains
- **Representation layer**: Maintains internal generative model
- **Decoder layer**: Maps representation to motor commands
- **Free energy monitor**: Gated spike generation — spikes constrained by energy reduction

### Key Properties

1. **Sparse activity**: Neurons fire only when energetically justified
2. **External robustness**: Resilient to sensory noise, environmental perturbations, collisions
3. **Internal robustness**: Resilient to synaptic noise, transmission delays, neuron silencing
4. **Energy efficiency**: Operations on spiking substrate, deployable on neuromorphic hardware

## Mathematical Foundation

### Free Energy Principle for Control

```
F = -log p(observation | internal state) + KL[q(internal state) || p(internal state)]
```

Active Inference treats both perception and action as minimizing F:
- **Perception**: Update internal state to better predict observations
- **Action**: Change environment to match predictions

### Spiking Implementation

The spiking constraint adds a critical gating mechanism:

```
spike_allowed = sign(-dF/dt)  # spike only if free energy decreases
```

This ensures computational efficiency — most neurons remain silent most of the time.

## Implementation Pattern

```python
class SpikingFreeEnergyController:
    def __init__(self, state_dim, action_dim, dt=0.001):
        self.state_dim = state_dim
        self.action_dim = action_dim
        self.dt = dt
        self.internal_state = np.zeros(state_dim)
        self.prediction_precision = np.ones(state_dim)  # Expected precision
        
    def compute_free_energy(self, observation, action):
        """Compute variational free energy given observation and predicted outcome."""
        prediction = self.forward_model(self.internal_state, action)
        prediction_error = observation - prediction
        # F = 0.5 * precision * error^2 + complexity term
        F = 0.5 * np.sum(self.prediction_precision * prediction_error**2)
        return F
        
    def step(self, observation, desired_state):
        """One control step: perceive, act, update."""
        F_before = self.compute_free_energy(observation, self.last_action)
        
        # Perception: update internal state
        self.internal_state += self.perception_update(observation)
        
        # Action: compute action that minimizes expected free energy
        action = self.action_policy(self.internal_state, desired_state)
        
        F_after = self.compute_free_energy(observation, action)
        
        # Spike constraint: only emit if free energy decreases
        if F_after < F_before:
            self.emit_spike(action)
            self.last_action = action
        else:
            self.last_action *= 0.9  # Decay/no-op
            
        return self.last_action
```

## Use Cases

1. **Neuromorphic robotics**: Deploy SFEC on Loihi/SpiNNaker for energy-efficient control
2. **Prosthetic control**: Spiking controllers for brain-machine interfaces
3. **Biological modeling**: Test hypotheses about how brain implements active inference
4. **Continuous control tasks**: Pendulum, cart-pole, locomotion with spike-based controllers

## Comparison with Alternatives

| Method | Energy Efficiency | Biological Plausibility | Robustness | Continuous Control |
|--------|------------------|------------------------|------------|-------------------|
| Standard ANN control | Low | Low | Moderate | Yes |
| Traditional SNN | High | High | Moderate | Yes |
| **SFEC (this framework)** | **High** | **High** | **High** | **Yes** |
| Classical Active Inference | Low | Low | High | Yes |

## Related Skills
- `spiking-neural-network-analysis` - General SNN analysis
- `neuromodulated-synaptic-plasticity` - SNN learning with plasticity
- `energy-based-neurocomputation` - Energy-based neural computation
- `spikingjelly-framework` - SNN deep learning framework
