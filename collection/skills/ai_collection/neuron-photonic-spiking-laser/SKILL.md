---
name: neuron-photonic-spiking-laser
description: NeuronSEL - Photonic spiking neurons using multi-junction VCSELs for ultra-fast neuromorphic computing with optical interconnects.
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [neuromorphic, photonics, VCSEL, spiking, hardware, optoelectronic]
    source_paper: "Neuron Surface Emitting Laser (NeuronSEL): Spiking Regimes and Negative Differential Resistance in Multi-junction VCSELs (arXiv:2604.15391)"
    citations: 0
    related_skills: [circuit-level-spiking-neuron-robustness, neuromorphic-low-power-ai]
---

# NeuronSEL: Photonic Spiking Neurons

## Overview
NeuronSEL implements spiking neurons using multi-junction Vertical-Cavity Surface-Emitting Lasers (VCSELs), achieving ultra-fast neuromorphic computation at THz speeds. The device exhibits spiking regimes and negative differential resistance (NDR), enabling photonic neuromorphic computing with optical interconnects between neurons.

## Key Concepts

### Photonic Spiking Mechanism
- VCSEL operates as an excitable system analogous to biological neurons
- Input optical pulses trigger spike outputs (laser pulses)
- Negative differential resistance enables threshold behavior
- Refractory period emerges naturally from carrier dynamics

### Multi-Junction Architecture
- Multiple VCSEL junctions stacked vertically
- Each junction acts as a computational unit
- Optical interconnects between junctions for fast communication
- Wavelength division multiplexing for parallel processing

### Implementation Pattern
```python
class NeuronSELModel:
    """Rate-equation model of NeuronSEL photonic spiking neuron."""
    def __init__(self, threshold=1.0, refractory_time=10.0):
        self.carrier_density = 0
        self.photon_density = 0
        self.threshold = threshold
        self.refractory_time = refractory_time
        self.last_spike_time = -float('inf')
        
    def step(self, input_power, dt):
        t = input_power.get('time', 0)
        
        # Check refractory period
        if t - self.last_spike_time < self.refractory_time:
            return 0  # No spike during refractory period
        
        # Rate equations (simplified)
        dN = input_power['power'] - self.carrier_density / tau_n
        self.carrier_density += dN * dt
        
        if self.carrier_density > self.threshold:
            # Spike!
            spike_power = (self.carrier_density - self.threshold) * gain
            self.carrier_density = self.threshold * 0.5  # Reset
            self.photon_density = spike_power
            self.last_spike_time = t
            return 1
        
        self.photon_density *= 0.9  # Decay
        return 0
```

## Activation Keywords
photonic neuron, VCSEL, spiking laser, neuromorphic hardware, optical computing, negative differential resistance, NeuronSEL

## Applications
- Ultra-fast neuromorphic processors
- Optical neural networks
- Low-latency edge inference
- Photonic integrated circuits for AI

## Limitations
- Requires specialized optoelectronic fabrication
- Thermal management critical for multi-junction devices
- Optical-to-electrical conversion overhead at interfaces
