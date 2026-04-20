---
name: neuromorphic-photonic-neuronsel
description: "Neuron Surface Emitting Laser (NeuronSEL) — 基于多结VCSEL的神经形态光子脉冲神经元。利用负微分电阻(NDR)实现类神经元的脉冲发放、不应期和整合-发放动力学。适用于光子计算、光通信、神经形态硬件、光学传感。Activation: neuromorphic photonics, VCSEL spiking neuron, negative differential resistance, optical neural network, photonic computing, integrate-and-fire laser"
version: 1.0.0
metadata:
  hermes:
    tags: [neuromorphic, photonics, VCSEL, spiking, NDR, optical-computing]
    source_paper: "Neuron Surface Emitting Laser (NeuronSEL): Spiking Regimes and Negative Differential Resistance in Solitary Multi-junction VCSELs (arXiv:2604.12893)"
    authors: "Maria Duque-Gijon, Josh Robertson, Dafydd Owen-Newns, Jack Baker, Craig P. Allford, Xavier Porte, Sam Shutts, Peter M. Smowton, Antonio Hurtado"
    published: "2026-04-14"
---

# NeuronSEL: Neuromorphic Photonic Spiking Neuron

## Overview

NeuronSEL is a **compact, multi-junction Vertical-Cavity Surface-Emitting Laser (VCSEL)** that demonstrates optical and electrical neural-like spiking behavior under solitary operation. It exhibits Negative Differential Resistance (NDR) similar to memristive devices, enabling multiple neuronal features including refractoriness and threshold/integrate-and-fire dynamics.

**Source Paper**: arXiv:2604.12893 (2026-04-14)

## Core Concepts

### 1. Negative Differential Resistance (NDR)
The NeuronSEL exhibits NDR behavior:
- Current increases → voltage drops beyond threshold
- Creates natural threshold switching mechanism
- Similar to memristive devices but in a photonic platform
- Enables excitable dynamics essential for spiking

### 2. Integrate-and-Fire Dynamics
The laser naturally implements neuronal integration:
- **Integration**: Input signals accumulate in the cavity
- **Threshold**: When carrier density exceeds critical level
- **Fire**: Rapid optical pulse emission
- **Refractory**: Recovery period before next spike

### 3. Optical Spiking Neuron
Key neuronal behaviors demonstrated:
- **Coincidence detection**: Fires only when multiple inputs arrive simultaneously
- **XOR operation**: Logical computation via spiking dynamics
- **Refractory period**: Natural dead time after each spike
- **Threshold adaptation**: Sensitivity adjustment based on input history

### 4. Scalability
- **Array architecture**: Multiple NeuronSELs can be interconnected
- **Classification tasks**: Network of NeuronSELs performs pattern recognition
- **VCSEL advantages**: Low cost, compact, efficient, vertical emission
- **Integration**: Straightforward integration into large arrayed structures

## Implementation

### NeuronSEL Behavior Model

```python
import numpy as np

class NeuronSELModel:
    """Computational model of NeuronSEL spiking behavior."""
    
    def __init__(self, 
                 threshold=1.0,        # Firing threshold
                 refractory_period=5.0,  # ms
                 decay_rate=0.1,        # Integration decay
                 ndr_slope=-0.5,        # NDR characteristic
                 spike_amplitude=1.0):   # Output spike amplitude
        self.threshold = threshold
        self.refractory_period = refractory_period
        self.decay_rate = decay_rate
        self.ndr_slope = ndr_slope
        self.spike_amplitude = spike_amplitude
        
        # State variables
        self.membrane_potential = 0.0
        self.last_spike_time = -np.inf
        self.spike_train = []
        
    def integrate(self, input_current, dt=0.1):
        """Integrate input with NDR and decay."""
        # Check refractory period
        t = len(self.spike_train) * dt
        if t < self.last_spike_time + self.refractory_period:
            self.membrane_potential *= (1 - self.decay_rate * dt)
            return 0.0
        
        # NDR-modulated integration
        # High input → NDR kicks in → threshold effectively lower
        effective_input = input_current
        if input_current > self.threshold * 0.8:
            effective_input *= (1 + abs(self.ndr_slope) * 
                              (input_current - self.threshold * 0.8))
        
        # Leak integration
        self.membrane_potential += (effective_input - 
                                    self.decay_rate * self.membrane_potential) * dt
        
        # Threshold check
        if self.membrane_potential >= self.threshold:
            self.membrane_potential = 0.0  # Reset
            self.last_spike_time = t
            self.spike_train.append(t)
            return self.spike_amplitude
        
        return 0.0
    
    def coincidence_detection(self, input_a, input_b, dt=0.1):
        """Demonstrate coincidence detection behavior."""
        # NeuronSEL fires only when both inputs arrive together
        combined = input_a + input_b
        
        # With NDR, combined suprathreshold inputs trigger firing
        # Individual subthreshold inputs do not
        if combined > self.threshold and input_a > 0 and input_b > 0:
            return self.integrate(combined, dt)
        else:
            return self.integrate(combined * 0.3, dt)  # Subthreshold integration


def demonstrate_coincidence_detection():
    """Simulate NeuronSEL coincidence detection."""
    neuron = NeuronSELModel(threshold=1.0)
    
    dt = 0.1
    spikes = []
    
    for t in range(100):
        # Input A: arrives at t=20
        input_a = 0.6 if 20 <= t < 25 else 0.0
        
        # Input B: arrives at t=22 (overlapping) or t=40 (separate)
        input_b = 0.6 if 22 <= t < 27 else 0.0
        
        spike = neuron.integrate(input_a + input_b, dt)
        spikes.append(spike)
    
    return spikes


def demonstrate_xor_operation():
    """Simulate XOR logic with NeuronSEL."""
    neuron = NeuronSELModel(threshold=1.5)
    
    test_cases = [
        (0, 0, "Both off → no spike"),
        (1, 0, "A only → no spike (subthreshold)"),
        (0, 1, "B only → no spike (subthreshold)"),
        (1, 1, "Both on → spike (suprathreshold with NDR)")
    ]
    
    results = []
    for a, b, desc in test_cases:
        input_a = a * 0.8
        input_b = b * 0.8
        spike = neuron.integrate(input_a + input_b)
        results.append(f"{desc}: spike={spike > 0}")
    
    return results
```

### NeuronSEL Network Architecture

```python
class NeuronSELNetwork:
    """Network of NeuronSELs for classification."""
    
    def __init__(self, input_dim, hidden_neurons, output_neurons):
        # Input layer: weighted connections
        self.input_weights = np.random.randn(input_dim, hidden_neurons) * 0.1
        
        # Hidden layer: NeuronSEL neurons
        self.hidden_neurons = [
            NeuronSELModel(threshold=np.random.uniform(0.8, 1.2))
            for _ in range(hidden_neurons)
        ]
        
        # Output layer: readout weights
        self.output_weights = np.random.randn(hidden_neurons, output_neurons)
        
    def forward(self, input_pattern, timesteps=50, dt=0.1):
        """Forward pass through NeuronSEL network."""
        # Input to hidden layer
        hidden_inputs = input_pattern @ self.input_weights
        
        # NeuronSEL spiking in hidden layer
        hidden_spikes = np.zeros(len(self.hidden_neurons))
        
        for i, neuron in enumerate(self.hidden_neurons):
            for t in range(timesteps):
                spike = neuron.integrate(hidden_inputs[i] + 
                                        np.random.normal(0, 0.05), dt)
                hidden_spikes[i] += spike
        
        # Output layer (linear readout)
        output = hidden_spikes @ self.output_weights
        return output
```

## Applications

### 1. Neuromorphic Photonic Computing
- Ultra-fast optical neural networks
- Low-latency inference at speed of light
- Energy-efficient pattern recognition

### 2. Optical Communications
- Spike-based optical encoding
- Event-driven optical signal processing
- All-optical logic gates

### 3. Optical Sensing
- Event-driven optical sensors
- Coincidence detection for lidar/radar
- Temporal pattern recognition

### 4. Edge AI Hardware
- VCSEL arrays for compact neural inference
- Integration with existing CMOS processes
- Low manufacturing cost at scale

## VCSEL Advantages

| Property | Benefit |
|----------|---------|
| Vertical emission | Easy 2D array integration |
| Low manufacturing cost | Mass production viable |
| Compactness | High density integration |
| Energy efficiency | Low power operation |
| CMOS compatibility | Standard fabrication |

## Key Innovations

1. **First solitary VCSEL spiking neuron**: No external injection required
2. **NDR-based neuronal dynamics**: Natural threshold switching mechanism
3. **Multiple neuronal features**: Refractoriness, integrate-and-fire, coincidence detection
4. **Scalable architecture**: Array-based network for classification tasks
5. **Logical computation**: XOR and other logic operations demonstrated

## Limitations

- Requires experimental validation at scale
- Network training methodology needs development
- Inter-NeuronSEL optical coupling needs characterization
- Currently proof-of-concept, not production-ready

## References

- Duque-Gijon, M. et al. (2026). "Neuron Surface Emitting Laser (NeuronSEL): Spiking Regimes and Negative Differential Resistance in Solitary Multi-junction VCSELs." arXiv:2604.12893.

## Activation Keywords

- NeuronSEL
- neuromorphic photonics
- VCSEL spiking neuron
- negative differential resistance
- optical neural network
- photonic computing
- integrate-and-fire laser
- optical coincidence detection
- neuromorphic hardware
- 光子神经形态计算
- 脉冲VCSEL

## Related Skills

- [[spiking-neural-network-analysis]]
- [[snn-universal-approximation]]
- [[learning-neuron-dynamics-deep-snn]]

## Tools Used

- `Read` - Read existing files and documentation
- `Write` - Create new files and documentation
- `Bash` - Execute commands when needed

## Instructions for Agents

1. Identify user's intent and specific requirements
2. Gather necessary context from files or user input
3. Execute appropriate actions using available tools
4. Provide clear results and suggest next steps

## Examples

### Basic Neuromorphic Photonic Neuronsel usage
```
User: "Help me with neuromorphic photonic neuronsel"
→ Understand requirements → Execute actions → Provide results
```

### Advanced usage
```
User: "I need detailed neuromorphic photonic neuronsel assistance"
→ Clarify scope → Provide comprehensive solution → Follow up
```
