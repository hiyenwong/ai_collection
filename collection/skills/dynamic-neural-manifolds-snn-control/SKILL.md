---
name: dynamic-neural-manifolds-snn-control
description: >
  Dynamic neural manifolds methodology for flexible closed-loop control
  on neuromorphic hardware. Implements low-dimensional manifold geometry
  control via spiking ring networks with sensory-modulated circuit
  mechanisms (heterogeneous inhibition, gain, transient currents) on
  SpiNNaker 2 chip. Enables explainable neuromorphic architectures for
  real-time adaptive control.
---

# Dynamic Neural Manifolds for Flexible Closed-Loop Control on Neuromorphic Hardware

## Source

**Paper**: Dynamic neural manifolds for flexible closed-loop control on neuromorphic hardware
**arXiv**: 2607.07373v1
**Authors**: Oskar von Seeler, Christian Tetzlaff, Andrew B. Lehr
**Published**: 2026-07-08
**Categories**: cs.NE (Neural and Evolutionary Computing)

## Core Concepts

### Neural Manifold Framework

The collective activity of N neurons is represented as a trajectory in an N-dimensional state space. Brain activity is constrained to **low-dimensional manifolds** that capture latent task variables. Geometric features of manifolds map to behavioral execution:

- **Subspace rotations** occur when switching between behaviors
- **Trajectory speed** adapts with changes in movement timing
- **Manifold geometry** directly determines behavioral output

### Oscillatory Sequences on Ring Networks

A canonical pattern across spinal cord and brain: oscillatory sequences of neural activity on timescales of seconds or longer. These are modeled as a **bump of activity moving along a ring of neurons** — a canonical object in computational neuroscience.

Circuit mechanisms acting on the ring dynamically control sequential activity, which maps onto predictable changes in manifold geometry.

### Circuit Mechanisms for Manifold Control

Three key circuit parameters that control manifold geometry:

1. **Heterogeneous Inhibition**: Modulates the shape and stability of the activity bump
2. **Gain Control**: Adjusts the speed of neural trajectories along the manifold
3. **Transient Currents**: Enables rapid switching between behavioral states

### Sensory-Feedback Closed-Loop Architecture

The key innovation: sensory inputs modulate the circuit mechanisms **in real-time**, enabling:

- **Rapid subspace rotations** to switch between behaviors (e.g., steering vs. jumping)
- **Fine-grained trajectory control** within behavioral modes
- **Dynamic reconfiguration** of manifold geometry based on environmental cues

### Implementation on SpiNNaker 2

First implementation of dynamic neural manifold control on neuromorphic hardware (SpiNNaker 2 chip):

- Real-time, closed-loop control with low latency
- Energy-efficient spiking computation
- Explainable internal state (manifold geometry is mathematically interpretable)

### Validation: Robotic Maze Navigation

Validated via robotic simulation where an agent navigates a maze:
- Agent uses local environmental cues as sensory feedback
- Sensory inputs modulate inhibition, gain, and transient currents
- Agent dynamically reconfigures manifold geometry to navigate obstacles and turns

## Implementation Guide

### Ring Network Architecture

```python
# Canonical ring of N neurons with bump activity
# Each neuron i has: membrane potential V_i, firing rate r_i
# Connectivity: local excitation + global inhibition
# The bump position θ(t) defines the manifold state

class DynamicManifoldRing:
    """Ring network implementing dynamic neural manifolds."""
    
    def __init__(self, N=100):
        self.N = N
        # Recurrent weights: local excitation profile
        self.W_recurrent = self._gaussian_connectivity(sigma=5)
        # Heterogeneous inhibition profile
        self.inhibition_profile = np.ones(N)
        # Gain control per neuron
        self.gain_profile = np.ones(N)
        # Transient current injection
        self.transient_current = np.zeros(N)
    
    def step(self, sensory_input):
        """Update ring dynamics with sensory-modulated circuit mechanisms."""
        # Sensory input modulates circuit parameters
        self._update_inhibition(sensory_input)
        self._update_gain(sensory_input)
        self._update_transient(sensory_input)
        
        # Spiking dynamics with modulated parameters
        net_input = self.W_recurrent @ self.firing_rates
        net_input *= self.gain_profile
        net_input -= self.inhibition_profile * self.mean_rate
        net_input += self.transient_current
        
        self.membrane_potentials = self._leaky_integrate(
            self.membrane_potentials, net_input
        )
        self.spikes = self.membrane_potentials > self.threshold
        self.membrane_potentials[self.spikes] = self.reset_potential
```

### Sensory-Modulated Control Loop

```python
def sensory_modulated_control(agent_state, manifold_network, sensory_data):
    """
    Closed-loop control where sensory feedback modulates manifold geometry.
    
    agent_state: current position, velocity, etc.
    manifold_network: DynamicManifoldRing instance
    sensory_data: local environmental cues (obstacles, targets)
    """
    # Extract sensory features
    obstacle_direction = detect_obstacles(sensory_data)
    target_direction = detect_target(sensory_data)
    
    # Map sensory features to circuit modulation
    # Obstacles → increase inhibition in affected region → rotate manifold
    if obstacle_direction is not None:
        manifold_network.apply_inhibition(
            direction=obstacle_direction,
            strength=0.3
        )
        # This causes a subspace rotation → steering behavior
    
    # Target → increase gain toward target direction → accelerate
    if target_direction is not None:
        manifold_network.apply_gain(
            direction=target_direction,
            factor=1.5
        )
    
    # Extract motor command from manifold state
    # The bump position on the ring encodes the desired movement
    bump_position = manifold_network.get_bump_position()
    motor_command = manifold_network.decode_motor_output(bump_position)
    
    return motor_command
```

### Subspace Rotation Mechanism

```python
def compute_subspace_rotation(manifold_before, manifold_after):
    """
    Quantify the subspace rotation between two manifold states.
    
    This measures how much the neural activity subspace has rotated,
    which corresponds to behavioral switching.
    """
    # PCA on both states to get principal subspaces
    U1, _, _ = np.linalg.svd(manifold_before, full_matrices=False)
    U2, _, _ = np.linalg.svd(manifold_after, full_matrices=False)
    
    # Principal angles between subspaces
    cos_angles = np.linalg.svd(U1.T @ U2).S
    angles = np.arccos(np.clip(cos_angles, -1, 1))
    
    return angles  # Large angles = significant behavioral switch
```

## Key Design Principles

1. **Explainability**: Manifold geometry is mathematically interpretable — you can see *why* the agent chose a behavior by examining the manifold state
2. **Low-Dimensional Control**: Despite N neurons, behavior is controlled by a few parameters (inhibition profile, gain, transients)
3. **Biological Plausibility**: Based on observed neural sequences across species (rat spinal cord, Drosophila larvae, turtle spinal cord, mouse MEC)
4. **Energy Efficiency**: Spiking computation on neuromorphic hardware for low-power autonomous systems
5. **Real-Time Operation**: Closed-loop control with minimal latency on SpiNNaker 2

## Application Domains

- **Neuromorphic robotics**: Real-time adaptive control for autonomous agents
- **Prosthetics and BCI**: Explainable neural decoding for motor control
- **Computational neuroscience**: Testbed for studying how biological circuits translate spatiotemporal dynamics into goal-directed behavior
- **Autonomous navigation**: Energy-efficient path planning and obstacle avoidance

## Relationships to Other Skills

- Related to `spiking-neural-network-analysis` for SNN implementation details
- Complements `neuromorphic-fw mav-snn-control` for neuromorphic control patterns
- Builds on `brain-network-controllability` for network control theory foundations
- Connects to `kuramoto-brain-network` for oscillatory network dynamics

## Pitfalls

- **Manifold dimensionality**: The low-dimensional manifold assumption may not hold for all tasks; validate with PCA/variance explained analysis
- **Sensory mapping**: The mapping from sensory features to circuit parameters (inhibition/gain/transient) is task-specific and requires careful tuning
- **Hardware constraints**: SpiNNaker 2 has specific constraints on connectivity and precision; verify compatibility before deployment
- **Training vs. inference**: The circuit parameters are trained offline (via simulation); the closed-loop modulation happens at inference time
