---
name: vo2-mott-spiking-neuron-hardware
description: "VO2 Mott oscillator-based spiking neuron hardware for neuromorphic computing. Monolithic CMOS-BEOL integration of energy-efficient spiking neurons using vanadium dioxide phase-transition materials. Activation: vo2, mott, spiking neuron, neuromorphic hardware, phase-transition, BEOL integration."
---

# VO2 Mott Spiking Neuron Hardware

> Monolithic back-end-of-line (BEOL) integration of VO2-based spiking neurons on CMOS-compatible platforms for energy-efficient neuromorphic computing.

## Metadata
- **Source**: arXiv:2604.21487v1
- **Authors**: Fabio Bersano, Cyrille Masserey, Vanessa Conti, Andrea Iaconeta, et al.
- **Published**: 2026-04-23
- **Institution**: EPFL, Switzerland

## Core Methodology

### Key Innovation
First demonstration of monolithic BEOL integration of one-transistor-one-VO2-memristor (1T-1MR) spiking neurons on CMOS-compatible platforms, achieving sub-20 pJ energy consumption per spike with scalable manufacturing.

### Technical Framework

#### Device Architecture
- **Configuration**: 1T-1MR (one-transistor-one-memristor) compact architecture
- **Substrate**: Dielectrically isolated silicon-on-insulator (SOI) p-type junctionless field-effect transistors (JLFETs)
- **VO2 Fabrication**: Pulsed-laser deposition below 430°C
- **Device Dimensions**: 60 nm-thick VO2 with 6 μm² active area

#### Performance Characteristics
| Parameter | Value |
|-----------|-------|
| Oscillation Frequency | 40 - 410 kHz |
| Energy per Spike | 18 pJ |
| Memristor Power | 8 μW |
| Potential Scaled Power | <3 μW |
| Operating Temperature | Room temperature |

#### Key Phenomena
1. **Gate-Tunable Oscillations**: Frequency control via gate voltage
2. **Non-Monotonic Frequency Dependence**: Oscillation frequency depends non-monotonically on current and temperature
3. **Bias-Dependent Stochastic Firing**: Rich dynamical behavior for probabilistic computing
4. **Voltage-Controlled Oscillator**: Demonstrated functionality with active tunable resistive coupling

## Implementation Guide

### Prerequisites
- Cleanroom fabrication facilities
- Pulsed-laser deposition system
- SOI wafer with junctionless FETs
- Characterization equipment (oscilloscope, probe station)

### Fabrication Steps
1. **Substrate Preparation**: SOI p-type JLFET fabrication
2. **VO2 Deposition**: Pulsed-laser deposition at <430°C
3. **Device Patterning**: Nanosheet device definition
4. **BEOL Integration**: Back-end-of-line metal routing
5. **Characterization**: Electrical and thermal testing

### Circuit Configuration
```
RL Circuit Integration:
- Two-terminal VO2 device
- Series inductor L
- DC bias voltage
- Temperature control
```

## Applications
- **Neuromorphic Edge Computing**: Ultra-low power AI at the edge
- **Probabilistic Computing**: Stochastic firing for Bayesian inference
- **Oscillatory Neural Networks**: Coupled oscillator computing
- **Brain-Inspired Sensors**: Event-driven sensory processing

## Pitfalls
- **Thermal Management**: VO2 transition near room temperature requires precise thermal control
- **Process Compatibility**: BEOL temperature budget constraints (<430°C)
- **Variability**: Stochastic firing may require calibration for deterministic applications
- **Scaling Challenges**: Active area reduction while maintaining performance

## Related Skills
- `inhibitory-neuristor-mit`: Complementary inhibitory neuron implementation
- `neuromorphic-parametric-oscillators-v2`: Alternative oscillatory neuromorphic approach
- `neuromorphic-photonic-neuronsel`: Photonic spiking neurons
- `cmosx-mtj-neuron-nonlinear-classification`: CMOS+X neuron approaches

## References
- Bersano, F. et al. "Monolithically Integrated VO2 Mott Oscillators for Energy-Efficient Spiking Neurons." arXiv:2604.21487 (2026).
