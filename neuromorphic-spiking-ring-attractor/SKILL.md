---
name: neuromorphic-spiking-ring-attractor
description: "Neuromorphic Spiking Ring Attractor for proprioceptive joint-state estimation. Implements neural clusters with local recurrent excitation and global inhibition to encode joint angles on neuromorphic processors like DYNAP-SE2. Activation: spiking ring attractor, proprioceptive encoding, neuromorphic joint estimation, SRA network."
category: neuroscience
tags: [neuromorphic, spiking-ring-attractor, proprioception, DYNAP-SE2, robotics]
paper_reference: "2604.14021v1"
paper_title: "Neuromorphic Spiking Ring Attractor for Proprioceptive Joint-State Estimation"
authors: ["Federica Ferrari", "Flavia Davidhi", "Bernard Maacaron", "Alberto Motta", "Luuk van Keeken", "Elisa Donati", "Giacomo Indiveri", "Chiara De Luca", "Chiara Bartolozzi"]
published: "2026-04-15"
---

# Neuromorphic Spiking Ring Attractor (SRA)

A neuromorphic implementation of Spiking Ring Attractor for encoding and continuously tracking joint states from proprioceptive inputs with low latency and power consumption.

## Overview

The Spiking Ring Attractor (SRA) architecture encodes continuous variables (like joint angles) using localized activity bumps on a circular neural topology:

- **Neural Clusters**: N clusters arranged on a circular axis
- **Local Excitation**: Recurrent connections within clusters
- **Global Inhibition**: Cross-cluster inhibition creating competition
- **Activity Bump**: Localized firing representing current value
- **Neuromorphic Hardware**: Implemented on DYNAP-SE2 processor

## Core Architecture

### 1. Ring Topology

```
        Cluster 0
       /         \
  Cluster N-1     Cluster 1
      |             |
  Cluster N-2     Cluster 2
       \         /
        ...
```

### 2. Connectivity Pattern

- **Local Recurrent Excitation**: Each cluster excites itself (positive feedback)
- **Nearest-Neighbor Coupling**: Adjacent clusters have weak excitation
- **Global Inhibition**: All clusters inhibit all others (competition)
- **Input Projections**: Proprioceptive inputs drive appropriate clusters

### 3. Activity Bump Dynamics

The peak position of the activity bump encodes the joint angle:

```
Joint Angle:    0°        90°       180°      270°
                |         |         |         |
Firing Rate:   ███       ███       ███       ███
               ▓▓▓      █████      ▓▓▓       ▓▓▓
               ░░░     ███████     ░░░       ░░░
               ░░░    █████████    ░░░       ░░░
               ░░░   ███████████   ░░░       ░░░
                     Activity Bump
```

## Mathematical Model

### Neuron Dynamics

Leaky Integrate-and-Fire (LIF) neurons with continuous attractor dynamics:

$$\tau_m \frac{dv_i}{dt} = -v_i + \sum_j W_{ij}^{rec} s_j(t) + I_i^{input}(t)$$

Where:
- $\tau_m$: Membrane time constant
- $v_i$: Membrane potential of neuron i
- $W_{ij}^{rec}$: Recurrent connection weights
- $s_j(t)$: Spike train of neuron j
- $I_i^{input}$: Proprioceptive input current

### Weight Structure

```python
# Weight matrix construction
W[i, j] = {
    w_exc if i == j (self-excitation)
    w_neighbor if |i-j| == 1 (nearest neighbor)
    -w_inh otherwise (global inhibition)
}
```

### Bump Position Encoding

$$\theta(t) = \frac{2\pi}{N} \sum_i i \cdot r_i(t)$$

Where:
- $\theta(t)$: Encoded joint angle
- $r_i(t)$: Firing rate of cluster i (normalized)
- N: Number of clusters

## Implementation on DYNAP-SE2

### Hardware Configuration

```python
from pynn import setup, Population, Projection

# Setup DYNAP-SE2
setup(timestep=1.0, min_delay=1.0)

# Create neural clusters
num_clusters = 64
neurons_per_cluster = 4

clusters = []
for i in range(num_clusters):
    pop = Population(neurons_per_cluster, 
                     neuron_type=DYNAPSE_IF,
                     params={'tau_m': 20.0, 'v_thresh': -50.0})
    clusters.append(pop)

# Setup recurrent connectivity
setup_ring_attractor_weights(clusters, 
                             w_exc=0.5, 
                             w_inh=-0.3, 
                             w_neighbor=0.2)

# Input encoding
proprioceptor_input = create_proprioceptor_projection(clusters, gain=2.0)
```

### Proprioceptive Input Encoding

Convert joint encoder readings to neural drive:

```python
def encode_joint_angle(angle, num_clusters):
    """Encode joint angle (0-2π) to cluster activations."""
    cluster_indices = np.arange(num_clusters)
    preferred_angles = 2 * np.pi * cluster_indices / num_clusters
    
    # Gaussian tuning curves
    tuning_width = 2 * np.pi / num_clusters * 2.5
    activations = np.exp(-0.5 * ((angle - preferred_angles) / tuning_width) ** 2)
    
    return activations
```

## Workflow

### Step 1: Network Design

```python
# SRA parameters
sra_config = {
    'num_clusters': 64,
    'neurons_per_cluster': 4,
    'tau_m': 20.0,  # ms
    'v_thresh': -50.0,  # mV
    'v_reset': -70.0,  # mV
    'w_exc': 0.5,
    'w_inh': -0.3,
    'w_neighbor': 0.2
}
```

### Step 2: Weight Calibration

```python
def calibrate_ring_attractor(clusters, target_bump_width):
    """Calibrate weights for stable bump."""
    # Iterative calibration
    for trial in range(100):
        w_exc, w_inh = optimize_weights(clusters, target_bump_width)
        bump = test_bump_formation(clusters)
        
        if bump.width == target_bump_width:
            break
    
    return w_exc, w_inh
```

### Step 3: iCub Robot Integration

```python
class ProprioceptiveSRA:
    def __init__(self, num_joints=7):
        self.sras = []
        for joint in range(num_joints):
            sra = SpikingRingAttractor(sra_config)
            self.sras.append(sra)
    
    def update(self, joint_angles):
        """Update SRA states from joint encoder readings."""
        for angle, sra in zip(joint_angles, self.sras):
            activations = encode_joint_angle(angle, sra.num_clusters)
            sra.set_input(activations)
            sra.run(timestep=1.0)
    
    def get_estimated_angles(self):
        """Decode joint angles from SRA activity bumps."""
        angles = []
        for sra in self.sras:
            bump_center = sra.decode_bump_position()
            angle = bump_center * 2 * np.pi / sra.num_clusters
            angles.append(angle)
        return angles
```

### Step 4: Real-Time Operation

```python
# Main loop for iCub robot
sra_system = ProprioceptiveSRA(num_joints=7)

while robot.running:
    # Read joint encoders
    joint_angles = robot.get_joint_positions()
    
    # Update SRA states
    sra_system.update(joint_angles)
    
    # Get neuromorphic estimates
    estimated_angles = sra_system.get_estimated_angles()
    
    # Use for control
    robot.control_joints(estimated_angles)
```

## Performance Metrics

### Accuracy

- **Angular Resolution**: 360° / 64 clusters ≈ 5.6°
- **Tracking Error**: < 2° RMS on iCub robot
- **Settling Time**: < 50ms for step changes

### Efficiency

- **Power Consumption**: < 1mW per joint on DYNAP-SE2
- **Latency**: < 10ms end-to-end
- **Event Rate**: ~1k events/second per joint

## Applications

### 1. Robot Proprioception
- Real-time joint angle estimation
- Sensor fusion with vision
- Closed-loop motor control

### 2. Neuromorphic Sensory Processing
- Tactile encoding
- Vestibular system modeling
- Continuous variable representation

### 3. Brain-Inspired Control
- Hippocampal place cell models
- Head direction cells
- Path integration

## Advantages

1. **Low Power**: Event-driven computation on neuromorphic hardware
2. **Low Latency**: Parallel spike-based processing
3. **Continuous Representation**: Smooth encoding of analog variables
4. **Robustness**: Distributed representation resistant to neuron loss
5. **Biological Plausibility**: Matches neural ring attractor models

## Limitations

- Limited angular resolution (depends on cluster count)
- Requires calibration for stable bump formation
- Susceptible to drift without input
- Hardware-specific implementation details

## Related Skills

- **snn-working-memory-heterogeneous-delays**: SNN working memory
- **brain-digital-twins-execution-semantics**: Brain model execution
- **adaptive-spiking-neuron-asn**: Adaptive spiking neurons

## References

- Ferrari, F., Davidhi, F., Maacaron, B., et al. (2026). Neuromorphic Spiking Ring Attractor for Proprioceptive Joint-State Estimation. arXiv:2604.14021v1.

## Tools Used

- **execute_code**: Python simulation and analysis
- **terminal**: DYNAP-SE2 deployment and testing
- **write_file**: Create configuration files

## Example: iCub Integration

```python
# Complete iCub integration example
from pynn import *

# Initialize neuromorphic hardware
setup('dynapse2')

# Create SRA for 7-DOF arm
arm_sra = ProprioceptiveSRA(
    num_joints=7,
    clusters_per_joint=64,
    hardware='dynapse2'
)

# Connect to iCub robot
robot = iCubRobot('/icub')

# Run proprioceptive estimation
for _ in range(10000):
    # Get true joint angles
    true_angles = robot.get_joint_positions()
    
    # Update SRA
    arm_sra.update(true_angles)
    
    # Read estimated angles
    estimated = arm_sra.get_estimated_angles()
    
    # Log performance
    error = np.abs(np.array(true_angles) - np.array(estimated))
    print(f"Mean error: {np.mean(error):.2f} rad")
```

---

_Last updated: 2026-04-16_
