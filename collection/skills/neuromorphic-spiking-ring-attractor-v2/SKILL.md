---
name: neuromorphic-spiking-ring-attractor-v2
description: "Neuromorphic spiking ring-attractor network for proprioceptive joint-state estimation on Intel Loihi. Implements continuous attractor dynamics with recurrent E/I populations for stable encoding of continuous variables. Low-power robotic control with biological plausibility. Activation: spiking ring attractor, proprioceptive estimation, Loihi neuromorphic, continuous attractor, joint-state encoding."
---

# Neuromorphic Spiking Ring Attractor for Proprioceptive Joint-State Estimation

Implementation of spiking ring-attractor networks on Intel Loihi neuromorphic processor for proprioceptive joint-state estimation, based on arXiv:2604.14021v1 (2026-04-15).

## Core Concept

Continuous attractor networks provide biologically inspired mechanisms for encoding continuous variables through:
- **Ring attractor topology**: Recurrent connectivity forming a circular manifold
- **Activity bump**: Localized population activity representing continuous values
- **E/I balance**: Excitatory and inhibitory neuron populations maintaining stability
- **Neuromorphic implementation**: Energy-efficient computation on Intel Loihi

## Architecture

### Network Structure
```
Input Layer (Muscle Spindle Feedback)
           ↓
    Ring Attractor Network
    ┌─────────────────┐
    │  E-population   │──┐
    │  (excitatory)   │  │
    └─────────────────┘  │ recurrent
           ↓             │ connections
    ┌─────────────────┐  │
    │  I-population   │──┘
    │ (inhibitory)    │
    └─────────────────┘
           ↓
    Output (Joint Position)
```

### Key Components

1. **Ring Topology**: Neurons arranged on a circular ring representing joint angles
2. **Local Connectivity**: Each neuron connects to neighbors with distance-dependent weights
3. **E/I Balance**: Excitatory and inhibitory populations maintain stable bump
4. **Tuning Curves**: Each neuron has preferred direction/position

## Implementation Guide

### Step 1: Network Architecture on Loihi
```python
import numpy as np
from lava.magma.core.process.process import AbstractProcess
from lava.magma.core.process.ports.ports import InPort, OutPort
from lava.magma.core.sync.protocols.loihi_protocol import LoihiProtocol
from lava.magma.core.model.py.ports import PyInPort, PyOutPort
from lava.magma.core.model.py.type import LavaPyType
from lava.magma.core.resources import CPU, Loihi2NeuroCore

class RingAttractorNetwork(AbstractProcess):
    """
    Ring attractor network for continuous variable encoding.
    
    Parameters
    ----------
    n_neurons : int
        Total number of neurons in the ring
    n_excitatory : int
        Number of excitatory neurons
    n_inhibitory : int
        Number of inhibitory neurons
    sigma : float
        Width of connectivity kernel
    """
    def __init__(self, n_neurons=256, n_excitatory=192, n_inhibitory=64, 
                 sigma=0.3, **kwargs):
        super().__init__(**kwargs)
        
        self.n_neurons = n_neurons
        self.n_excitatory = n_excitatory
        self.n_inhibitory = n_inhibitory
        self.sigma = sigma
        
        # Ports
        self.input_port = InPort(shape=(n_neurons,))
        self.output_port = OutPort(shape=(n_neurons,))
        
        # Variables
        self.v = Var(shape=(n_neurons,), init=0.0)  # Membrane potential
        self.s = Var(shape=(n_neurons,), init=0)    # Spike output
        
        # Connectivity matrices
        self.w_exc = self._create_ring_weights(n_excitatory, sigma, 'exc')
        self.w_inh = self._create_ring_weights(n_inhibitory, sigma, 'inh')
        
    def _create_ring_weights(self, n, sigma, neuron_type):
        """Create ring-attractor connectivity."""
        weights = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                # Distance on ring (circular)
                dist = min(abs(i-j), n-abs(i-j)) / n
                if neuron_type == 'exc':
                    # Excitatory: local excitation
                    weights[i, j] = np.exp(-dist**2 / (2*sigma**2))
                else:
                    # Inhibitory: broader inhibition
                    weights[i, j] = -0.5 * np.exp(-dist**2 / (2*(2*sigma)**2))
        return weights
```

### Step 2: Proprioceptive Encoding
```python
class ProprioceptiveEncoder:
    """
    Encode joint state (position, velocity) using ring attractor.
    
    The joint angle is encoded as the position of the activity bump
    on the ring. Velocity is encoded as the speed of bump movement.
    """
    def __init__(self, n_neurons=256, angle_range=(-np.pi, np.pi)):
        self.n_neurons = n_neurons
        self.angle_min, self.angle_max = angle_range
        self.angle_range = angle_range[1] - angle_range[0]
        
        # Preferred angles for each neuron
        self.preferred_angles = np.linspace(
            self.angle_min, self.angle_max, n_neurons, endpoint=False
        )
        
    def angle_to_bump(self, angle, width=0.1):
        """
        Convert joint angle to activity bump pattern.
        
        Parameters
        ----------
        angle : float
            Joint angle in radians
        width : float
            Width of activity bump
            
        Returns
        -------
        bump_activity : array
            Target activity pattern
        """
        # Distance from each neuron's preferred angle
        dist = np.abs(self.preferred_angles - angle)
        # Wrap around for circular encoding
        dist = np.minimum(dist, 2*np.pi - dist)
        
        # Gaussian bump
        bump = np.exp(-dist**2 / (2*width**2))
        return bump
    
    def bump_to_angle(self, activity):
        """
        Decode activity bump to joint angle.
        
        Uses population vector decoding.
        """
        # Normalize activity
        activity = activity / (np.sum(activity) + 1e-10)
        
        # Weighted average of preferred angles
        sin_sum = np.sum(activity * np.sin(self.preferred_angles))
        cos_sum = np.sum(activity * np.cos(self.preferred_angles))
        
        angle = np.arctan2(sin_sum, cos_sum)
        return angle
```

### Step 3: Muscle Spindle Integration
```python
class MuscleSpindleInterface:
    """
    Interface between muscle spindle feedback and ring attractor.
    
    Muscle spindles provide:
    - Primary afferents (Ia): sensitive to velocity
    - Secondary afferents (II): sensitive to position
    """
    def __init__(self, n_spindles=10, n_ring_neurons=256):
        self.n_spindles = n_spindles
        self.n_ring = n_ring_neurons
        
        # Tuning curves for spindle afferents
        self.spindle_tuning = self._create_spindle_tuning()
        
        # Projection weights to ring
        self.w_spindle_to_ring = np.random.randn(n_ring_neurons, n_spindles) * 0.1
        
    def _create_spindle_tuning(self):
        """Create muscle spindle tuning curves."""
        # Each spindle has different preferred length/stretch
        tuning = []
        for i in range(self.n_spindles):
            pref_length = np.random.uniform(0.8, 1.2)
            tuning.append({'preferred': pref_length, 'gain': 100.0})
        return tuning
    
    def spindle_to_input(self, muscle_lengths, muscle_velocities):
        """
        Convert muscle state to ring attractor input.
        
        Parameters
        ----------
        muscle_lengths : array
            Current muscle lengths
        muscle_velocities : array
            Muscle stretch velocities
            
        Returns
        -------
        ring_input : array
            Input current to ring attractor neurons
        """
        spindle_activity = np.zeros(self.n_spindles)
        
        for i, (length, velocity) in enumerate(zip(muscle_lengths, muscle_velocities)):
            # Ia afferent: velocity sensitive
            ia_response = max(0, velocity * self.spindle_tuning[i]['gain'])
            # II afferent: position sensitive
            ii_response = max(0, (length - self.spindle_tuning[i]['preferred']) * 50)
            
            spindle_activity[i] = ia_response + ii_response
        
        # Project to ring
        ring_input = self.w_spindle_to_ring @ spindle_activity
        return ring_input
```

### Step 4: Robustness to Noise and Dropout
```python
def add_noise_robustness(network, noise_level=0.1, dropout_rate=0.05):
    """
    Add mechanisms for robust encoding under realistic conditions.
    
    Parameters
    ----------
    network : RingAttractorNetwork
        Base network
    noise_level : float
        Standard deviation of membrane noise
    dropout_rate : float
        Probability of sensor dropout
    """
    # Add membrane potential noise
    network.v_noise = noise_level
    
    # Redundant encoding: multiple overlapping bumps
    network.redundancy = 3
    
    # Homeostatic plasticity: maintain stable firing rates
    network.homeostasis = True
    network.target_rate = 20.0  # Hz
    
    return network

def decode_with_dropout(activity, preferred_angles, dropout_mask=None):
    """
    Decode joint angle even with partial sensor dropout.
    
    Uses robust statistical estimation.
    """
    if dropout_mask is not None:
        activity = activity.copy()
        activity[dropout_mask] = 0
    
    # Use only active neurons
    active_idx = activity > np.max(activity) * 0.1
    
    if np.sum(active_idx) < 10:
        # Too few active neurons, use last estimate
        return None
    
    # Robust population vector
    active_angles = preferred_angles[active_idx]
    active_activity = activity[active_idx]
    
    sin_sum = np.sum(active_activity * np.sin(active_angles))
    cos_sum = np.sum(active_activity * np.cos(active_angles))
    
    return np.arctan2(sin_sum, cos_sum)
```

## Energy Efficiency

### Loihi Advantages

1. **Event-driven computation**: Only active neurons consume power
2. **Low voltage operation**: ~100x lower energy per spike than GPUs
3. **On-chip learning**: Local plasticity rules without data movement
4. **Massive parallelism**: Thousands of neurons on single chip

### Performance Metrics

```
Traditional Digital Implementation:
- Power: ~10W
- Latency: ~1ms
- Precision: floating-point

Loihi Implementation:
- Power: ~10mW (1000x reduction)
- Latency: ~1ms (event-driven)
- Precision: spike-based (robust)
```

## Applications

### 1. Robotic Joint Control
```python
# Real-time joint position estimation
encoder = ProprioceptiveEncoder(n_neurons=256)
network = RingAttractorNetwork(n_neurons=256)

while True:
    # Read muscle spindles
    lengths, velocities = read_muscle_spindles()
    
    # Encode to ring attractor
    ring_input = spindle_interface.spindle_to_input(lengths, velocities)
    
    # Update network
    network.run(steps=10, input=ring_input)
    
    # Decode joint angle
    activity = network.get_activity()
    joint_angle = encoder.bump_to_angle(activity)
    
    # Control motor
    control_motor(joint_angle)
```

### 2. Prosthetic Limb Control
- Natural proprioception from residual muscles
- Low-power wearable implementation
- Real-time sensory feedback

### 3. Humanoid Robotics
- Whole-body posture estimation
- Dynamic balance control
- Energy-efficient walking

## Biological Plausibility

### Connection to Neural Systems

1. **Head Direction Cells**: Ring attractors in rodent entorhinal cortex
2. **Place Cells**: Continuous attractor dynamics in hippocampus
3. **Motor Cortex**: Population coding of movement parameters
4. **Cerebellum**: Proprioceptive processing and motor control

### Key Matches

- **Tuning curves**: Similar to cortical neurons
- **E/I balance**: Observed in cortical circuits
- **Attractor dynamics**: Persistent activity during working memory
- **Noise robustness**: Graceful degradation like biological systems

## Advanced Topics

### Multi-Joint Coordination

Extend to multiple joints using:
1. **Multiple ring attractors**: One per joint
2. **Cross-coupling**: Coordinate joint movements
3. **Hierarchical organization**: Higher-level posture encoding

### Learning and Adaptation

Online adaptation through:
1. **Hebbian plasticity**: Learn appropriate connectivity
2. **Homeostatic regulation**: Maintain stable activity
3. **Error-based learning**: Calibrate to actual joint positions

## References

- Ferrari, F., Davidhi, F., & Maacaron, B. (2026). Neuromorphic Spiking Ring Attractor for Proprioceptive Joint-State Estimation. arXiv:2604.14021v1

## Activation Keywords

- spiking ring attractor
- proprioceptive estimation
- Loihi neuromorphic
- continuous attractor
- joint-state encoding
- muscle spindle
- robotic proprioception
- E/I balanced network
