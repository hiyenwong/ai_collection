---
name: neuron-photonic-spiking-laser
description: "Neuron Surface Emitting Laser (NeuronSEL) - Neuromorphic photonics hardware for optical spiking neural networks. Single-stack multi-junction VCSEL with Negative Differential Resistance (NDR) enabling multiple neuronal features: refractory periods, excitatory/inhibitory inputs, spike bursting. Activation: photonic neuron, NeuronSEL, neuromorphic photonics, optical spiking, VCSEL neuron."
---

# NeuronSEL: Photonic Spiking Neuron Hardware

## Description
The Neuron Surface-Emitting Laser (NeuronSEL) is a compact, multi-junction Vertical-Cavity Surface Emitting Laser (VCSEL) that delivers optical and electrical neural-like spiking emission under solitary operation. It exhibits nonlinear Negative Differential Resistance (NDR), enabling multiple neuronal features essential for neuromorphic photonic systems.

## Core Innovation

### Single-Stack Photonic Neuron
Unlike previous approaches requiring complex external components:
- **All-in-one device**: Laser + modulation + detection in single VCSEL
- **Solitary operation**: No external optical feedback needed
- **Compact form factor**: Standard semiconductor fabrication
- **Scalable**: Array-compatible VCSEL technology

### Negative Differential Resistance (NDR)
```
I-V Characteristic:
    ↑ Current
    │    ╭────╮
    │   ╱      ╲____  ← NDR region (negative slope)
    │  ╱              
    │ ╱
    └────────────────→ Voltage
    
The NDR region creates:
- Bistability (two stable states)
- Excitability (spike generation)
- Self-sustained oscillations
```

### Neuronal Features Demonstrated

| Feature | Implementation | Application |
|---------|---------------|-------------|
| Refractory period | Carrier recovery time | Realistic spike timing |
| Excitatory input | Optical injection | Synaptic integration |
| Inhibitory input | Electrical modulation | Inhibition mechanisms |
| Spike bursting | Multiple NDR transitions | Burst coding |
| Threshold adaptation | Temperature effects | Gain modulation |

## Device Physics

### Multi-Junction VCSEL Structure
```
NeuronSEL Cross-Section:

    ┌─────────────────────┐
    │    Top Mirror (DBR) │
    ├─────────────────────┤
    │   Active Region 1   │ ← Gain medium
    ├─────────────────────┤
    │   Tunnel Junction   │ ← NDR source
    ├─────────────────────┤
    │   Active Region 2   │ ← Additional gain
    ├─────────────────────┤
    │  Bottom Mirror (DBR)│
    └─────────────────────┘
    
Key: Multiple active regions + tunnel junction = NDR
```

### Operating Modes

#### Mode 1: Excitable (Single Spikes)
```python
# Single spike generation
bias_current = I_baseline  # Below threshold
perturbation = delta_I     # Input pulse

if I_total > I_threshold:
    emit_optical_spike()
    enter_refractory_period(tau_ref)
```

#### Mode 2: Oscillatory (Periodic Spiking)
```python
# Self-sustained oscillations
bias_current = I_osc       # In NDR region

while True:
    emit_optical_spike()
    wait(tau_recovery)     # Carrier recovery
    # No external trigger needed
```

#### Mode 3: Bursting (Multiple Spikes)
```python
# Burst generation
bias_current = I_burst     # Higher in NDR region

spike_count = 0
while in_burst:
    emit_optical_spike()
    spike_count += 1
    if spike_count >= burst_size:
        longer_recovery()
        break
```

## Characteristics

### Electrical Characteristics
| Parameter | Value | Notes |
|-----------|-------|-------|
| Threshold current | 1.5 mA | Room temperature |
| Operating voltage | 2-3 V | Multi-junction |
| NDR region | 2.5-3.0 V | Negative slope |
| Maximum modulation | 10 GHz | Bandwidth limit |

### Optical Characteristics
| Parameter | Value | Notes |
|-----------|-------|-------|
| Wavelength | 850 nm | GaAs-based |
| Output power | 1-5 mW | Per device |
| Spectral width | <0.1 nm | Single-mode |
| Beam divergence | 15° | Circular |

### Temporal Characteristics
| Parameter | Value | Notes |
|-----------|-------|-------|
| Spike duration | 100 ps | Optical pulse |
| Refractory period | 1-10 ns | Tunable |
| Jitter | <1 ps | Timing precision |
| Energy per spike | 1-10 fJ | Ultra-low power |

## Integration Approaches

### 1. Photonic Integrated Circuit (PIC)
```python
# On-chip photonic neural network
class PhotonicNeuralNetwork:
    def __init__(self, n_neurons):
        self.neurons = [NeuronSEL() for _ in range(n_neurons)]
        self.waveguides = MeshNetwork(n_neurons)
        self.detectors = Photodetectors(n_neurons)
    
    def simulate(self, inputs, duration):
        for t in range(duration):
            # Neurons emit spikes
            spikes = [n.step() for n in self.neurons]
            
            # Optical routing
            optical_signals = self.waveguides.route(spikes)
            
            # Detection and feedback
            currents = self.detectors.convert(optical_signals)
            
            # Update neuron inputs
            for n, i in zip(self.neurons, currents):
                n.receive_input(i)
```

### 2. Free-Space Optical System
```python
# Free-space interconnect for larger networks
class FreeSpacePNN:
    def __init__(self, array_size):
        self.neuron_array = VCSELArray(array_size)
        self.optical_interconnect = DMD_SLM()  # Spatial light modulator
        self.detector_array = SPADArray(array_size)
    
    def propagate(self):
        # Emission
        optical_field = self.neuron_array.emit()
        
        # Weighted interconnection
        modulated = self.optical_interconnect.modulate(optical_field, weights)
        
        # Detection
        photocurrents = self.detector_array.detect(modulated)
        
        return photocurrents
```

## Synaptic Integration

### Optical Synapses
```
Weight Implementation:

Input spike ──→ [Attenuator/Amplifier] ──→ Weighted spike
                (Variable optical attenuator)
                
OR

Input spike ──→ [Ring Resonator] ──→ Wavelength-selective weight
                (Tunable coupling)
```

### Electrical Synapses
```python
# CMOS-compatible approach
class ElectricalSynapse:
    def __init__(self):
        self.weight = Memristor()  # Or SRAM cell
        self. integrator = Capacitor()
    
    def process(self, input_spike):
        charge = self.weight.read() * input_spike.charge
        self.integrator.accumulate(charge)
        return self.integrator.voltage
```

## Applications

### 1. Optical Neural Networks
- Image classification at speed of light
- Reservoir computing with photonic neurons
- Spike-based optical computing

### 2. Sensing and LIDAR
- Neuromorphic event-based cameras
- Spike-encoded depth sensing
- Adaptive sensing with plasticity

### 3. Communication Systems
- Spike-based optical communication
- Neuromorphic signal processing
- Optical pattern recognition

### 4. Brain-Computer Interfaces
- Optical neural recording
- Bidirectional neural interfaces
- Closed-loop neurostimulation

## Performance Comparison

| Platform | Speed | Energy/Op | Scalability | Integration |
|----------|-------|-----------|-------------|-------------|
| NeuronSEL | 10 GHz | ~1 fJ | High | PIC |
| CMOS neuron | 100 MHz | ~1 pJ | Very High | Standard |
| Memristor | 1 MHz | ~10 fJ | Medium | Emerging |
| Biological | 1 kHz | ~1 fJ | Very High | N/A |

## Fabrication Considerations

### Material Systems
- **GaAs/AlGaAs**: 850 nm operation, mature technology
- **InP/InGaAsP**: 1550 nm telecom wavelength
- **GaN**: Visible light, bio-compatible

### Integration Challenges
1. Thermal management (multi-junction heating)
2. Electrical isolation (independent biasing)
3. Optical coupling (efficient light extraction)
4. Yield optimization (uniform NDR characteristics)

## References

- **Paper**: Neuron Surface Emitting Laser (NeuronSEL): Spiking Regimes and Negative Differential Resistance in Solitary Multi-junction VCSELs (arXiv:2604.12893, 2026)
- **Authors**: Maria Duque-Gijon, Joshua Robertson, Dafydd Owen-Newns, et al.
- **Key innovation**: Single-device photonic neuron with NDR

## Activation Keywords
- photonic neuron
- NeuronSEL
- neuromorphic photonics
- optical spiking
- VCSEL neuron
- photonic neural network
- NDR laser

## Related Skills
- spiking-memristor-multimodal: Memristive spiking neurons
- neuromorphic-aer-encoder-design: AER encoder for neuromorphic systems
- robust-spiking-reservoir: Photonic reservoir computing
