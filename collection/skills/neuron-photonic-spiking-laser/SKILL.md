---
name: neuron-photonic-spiking-laser
description: "Neuron Surface Emitting Laser (NeuronSEL) for neuromorphic photonics. Multi-junction VCSEL exhibiting spiking regimes and negative differential resistance for optical neural computing. Activation: neuronsel, photonic spiking, VCSEL, neuromorphic photonics, optical neuron, laser spiking."
---

# Neuron Surface Emitting Laser (NeuronSEL)

> Compact multi-junction Vertical-Cavity Surface Emitting Laser (VCSEL) that delivers optical and electrical neural-like spiking emission under solitary operation for neuromorphic photonics.

## Metadata
- **Source**: arXiv:2604.12893v1
- **Authors**: Maria Duque-Gijon, Joshua Robertson, Dafydd Owen-Newns, Jack Baker, et al.
- **Published**: 2026-04-14
- **Institution**: University of Cambridge, UK

## Core Methodology

### Key Innovation
First single-stack laser capable of generating neuro-mimetic optical signals under solitary operation, exhibiting non-linear Negative Differential Resistance (NDR) similar to memristive devices, enabling multiple neuronal features including refractoriness and threshold-/integrate-and-fire dynamics.

### Technical Framework

#### Device Architecture
- **Type**: Multi-junction Vertical-Cavity Surface Emitting Laser (VCSEL)
- **Operation**: Solitary (no external optical feedback required)
- **Key Property**: Negative Differential Resistance (NDR)
- **Output**: Optical and electrical spiking

#### Neuronal Features Demonstrated
| Feature | Description |
|---------|-------------|
| Refractoriness | Post-spike recovery period |
| Threshold Firing | Spike generation above threshold |
| Integrate-and-Fire | Accumulation-driven spiking |
| Coincidence Detection | Multiple input integration |
| XOR Operation | Logical computation |

#### Advantages of VCSEL Technology
- Low manufacturing cost
- Compact size
- High efficiency
- Vertical emission
- Straightforward array integration
- Scalable to large networks

## Implementation Guide

### Device Operation
```
Spiking Regimes:
1. Sub-threshold: Membrane potential integration
2. Threshold crossing: Spike initiation
3. Spike emission: Optical pulse generation
4. Refractory period: Recovery before next spike
5. Reset: Return to integration state
```

### Network Implementation
- **Array Architecture**: Scalable 2D VCSEL arrays
- **Connectivity**: Optical coupling between neurons
- **Weighting**: Intensity-based synaptic weights
- **Classification**: Demonstrated network-level computation

### Integration Considerations
- Electrical biasing for NDR region
- Thermal management for stable operation
- Optical coupling efficiency
- Readout electronics for spike detection

## Applications
- **Optical Neuromorphic Computing**: High-speed brain-inspired processing
- **Optical Communications**: Spike-based optical signaling
- **Optical Sensing**: Event-driven optical detection
- **AI Acceleration**: Photonic neural network inference

## Pitfalls
- **Biasing Complexity**: Requires precise NDR region operation
- **Thermal Sensitivity**: Temperature affects NDR characteristics
- **Optical Crosstalk**: Array integration requires isolation
- **Power Consumption**: Trade-off between speed and efficiency

## Related Skills
- `vo2-mott-spiking-neuron-hardware`: Electronic spiking neurons
- `inhibitory-neuristor-mit`: Complementary inhibitory neurons
- `neuromorphic-photonic-neuronsel-v2`: Extended photonic neuron architectures

## References
- Duque-Gijon, M. et al. "Neuron Surface Emitting Laser (NeuronSEL): Spiking Regimes and Negative Differential Resistance in Solitary Multi-junction VCSELs." arXiv:2604.12893 (2026).
