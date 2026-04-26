---
name: inhibitory-neuristor-mit
description: "Inhibitory neuristor based on metal-to-insulator transition (MIT) materials for neuromorphic computing. Self-oscillation dynamics with current suppression mimicking neuronal inhibition. Activation: inhibitory neuristor, MIT, metal-to-insulator, neuromorphic inhibition, self-oscillation."
---

# Inhibitory Neuristor (MIT-Based)

> Novel inhibitory artificial neuron using metal-to-insulator transition (MIT) materials that suppress current flow, complementing excitatory IMT-based neuristors for biologically plausible neuromorphic systems.

## Metadata
- **Source**: arXiv:2604.19951v1
- **Authors**: Victor Palin, Akash Agnihotri, Nareg Ghazikhanian, Matthew Frame, et al.
- **Published**: 2026-04-21

## Core Methodology

### Key Innovation
First demonstration of inhibitory neuristor using metal-to-insulator transition (MIT) materials, where electrical triggering suppresses current flow (opposite to excitatory IMT devices), enabling biologically realistic inhibitory behaviors in neuromorphic hardware.

### Biological Inspiration
Biological neurons exhibit both excitatory (increased firing) and inhibitory (decreased firing) behaviors. While IMT materials mimic excitation through abrupt current increase, MIT materials enable inhibition through current suppression.

### Technical Framework

#### Device Physics
- **Material**: Prototypical MIT material (specific composition not detailed)
- **Switching**: Volatile low-to-high resistance switching
- **Circuit**: Simple RL (resistor-inductor) configuration
- **Dynamics**: Self-sustained current oscillations via MIT triggering

#### Performance Characteristics
| Parameter | Value |
|-----------|-------|
| Oscillation Frequency | 0.1 - 1 MHz |
| Cycle-to-Cycle Variation | Minimal |
| Control Parameters | DC voltage, temperature, inductance |

#### Control Mechanisms
1. **DC Voltage**: Modulates oscillation amplitude and frequency
2. **Temperature**: Affects MIT transition threshold
3. **Inductance**: Determines oscillation frequency in RL circuit

## Implementation Guide

### Circuit Design
```
Inhibitory Neuristor Circuit:
    
    [DC Voltage Source] ---- [Inductor L] ---- [MIT Device] ---- [Ground]
                                    |
                              [Output Node]
```

### Operating Principles
1. **Rest State**: Device in low-resistance state, steady current flow
2. **MIT Triggering**: Current exceeds threshold → MIT occurs
3. **Current Suppression**: Abrupt resistance increase → current drop
4. **Recovery**: RL dynamics restore current → cycle repeats

### Fabrication Considerations
- Two-terminal device structure
- Compatible with standard microfabrication
- Temperature-stable operation
- Low-voltage switching

## Applications
- **Balanced Neural Networks**: E/I balance in SNNs
- **Pattern Completion**: Inhibition for winner-take-all dynamics
- **Oscillatory Networks**: Coupled excitatory/inhibitory populations
- **Neural Coding**: Complementary spike generation mechanisms

## Pitfalls
- **Material Selection**: MIT materials less common than IMT materials
- **Thermal Stability**: Requires careful temperature management
- **Parameter Sensitivity**: Inductance value critical for stable oscillation
- **Coupling Complexity**: E-I coupling requires careful circuit design

## Related Skills
- `vo2-mott-spiking-neuron-hardware`: Excitatory VO2-based spiking neurons
- `neuromorphic-spiking-ring-attractor-v2`: Continuous attractor networks
- `snn-working-memory-heterogeneous-delays-v3`: Working memory with inhibition

## References
- Palin, V. et al. "Inhibitory neuristor based on metal-to-insulator transition." arXiv:2604.19951 (2026).
