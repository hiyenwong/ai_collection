---
name: spiking-recurrent-cells-fpga-accelerator
description: "FPGA accelerator for Spiking Recurrent Cell (SRC) neurons — a trade-off between biological plausibility and hardware cost. Removes costly unary operators (tanh, exp) via piecewise approximations, avoids floating-point arithmetic. Achieves 96.31% MNIST accuracy at 0.55-2.2mJ per digit on Artix-7 FPGA. Activation: FPGA spiking neural network, SRC neuron hardware, neuromorphic FPGA, energy-efficient SNN, VHDL SNN implementation, spiking recurrent cells."
---

# Spiking Recurrent Cells FPGA Accelerator

> Energy-efficient FPGA implementation of Spiking Recurrent Cell (SRC) neurons, providing a trade-off between biological plausibility and hardware cost with piecewise approximations replacing costly unary operators.

## Metadata
- **Source**: arXiv:2605.10679
- **Authors**: Pascal Harmeling, Florent De Geeter, Guillaume Drion
- **Published**: 2026-05-11
- **Subjects**: Neural and Evolutionary Computing (cs.NE)

## Core Methodology

### Key Innovation
Spiking Neural Networks can reduce energy vs. ANNs when spiking is sparse and neuron models are hardware-friendly. However, biologically faithful models are too costly for FPGAs, while simple models (IR/LIF) sacrifice neuronal dynamics. This paper introduces an **FPGA accelerator for SRC neurons** that provides a middle ground, using mathematical simplifications to remove costly unary operators (tanh, exp) and avoid floating-point arithmetic through scaling and piecewise-defined approximations.

### Technical Framework

1. **SRC Neuron Model**: Spiking Recurrent Cells offer richer dynamics than LIF/IR models while remaining implementable on hardware
2. **Unary Operator Removal**: Costly functions (tanh, exp) are replaced with piecewise-defined approximations using fixed-point arithmetic
3. **Weight Storage in LUT-Registers**: Weight matrices computed offline are stored directly in LUT-registers without adaptation, demonstrating SRC robustness
4. **VHDL Implementation**: Complete network implemented in VHDL on Artix-7 XC7A200T FPGA

### Implementation Details
- **Platform**: Artix-7 XC7A200T FPGA, 100 MHz clock
- **Accuracy**: 96.31% on MNIST (220-image spiking trace, 1.7424 ms per digit)
- **Energy-Accuracy Trade-off**:
  - 93.32% accuracy at 0.55 mJ per digit (55 images, 5-bit weights)
  - 92.89% accuracy at 0.45 mJ per digit (44 images, 4-bit weights)
- **Quantization**: Synaptic weights quantized down to 4 bits with minimal accuracy loss

## Implementation Guide

### Prerequisites
- FPGA development tools (Vivado for Xilinx Artix-7)
- VHDL programming knowledge
- SRC neuron model definition
- MNIST or similar dataset for validation

### Step-by-Step
1. **Define SRC Neuron Equations**: Start with the full SRC model with recurrent connections
2. **Approximate Unary Operators**: Replace tanh and exp with piecewise linear approximations
3. **Fixed-Point Conversion**: Convert all floating-point operations to fixed-point arithmetic with appropriate bit-width
4. **VHDL Architecture Design**:
   - Neuron processing units (parallel or sequential)
   - Weight memory in LUT-registers
   - Spike routing and timing logic
5. **Weight Off-line Training**: Train weights in software, then quantize and load into FPGA
6. **Synthesis & Place/Route**: Target Artix-7 or compatible FPGA
7. **Validation**: Compare FPGA output with software reference using spike traces

### Code Example
```python
# SRC neuron with piecewise approximation (Python reference)
import numpy as np

def src_piecewise_tanh(x):
    """Piecewise linear approximation of tanh for hardware implementation."""
    if x < -2.0:
        return -1.0
    elif x < -1.0:
        return -0.5 * x - 1.5
    elif x < 0.0:
        return x
    elif x < 1.0:
        return -0.5 * x + 1.5
    else:
        return 1.0

def src_neuron_step(membrane, input_current, weights, prev_spikes, dt=0.001):
    """SRC neuron update with hardware-friendly approximations."""
    # Recurrent input
    recurrent = np.dot(weights, prev_spikes)
    
    # Total input
    total = input_current + recurrent
    
    # Piecewise activation (replaces tanh)
    activation = src_piecewise_tanh(total)
    
    # Membrane update
    membrane_new = membrane + dt * activation
    
    # Spike generation
    spike = 1.0 if membrane_new > 1.0 else 0.0
    
    # Reset
    if spike:
        membrane_new = 0.0
    
    return membrane_new, spike
```

### VHDL Implementation Notes
- Use block RAM or LUT-registers for weight storage
- Implement piecewise functions as lookup tables or comparator chains
- Pipeline spike processing for throughput
- Clock domain: 100 MHz target for Artix-7

## Applications
- **Edge AI inference**: Low-power SNN deployment on FPGA for IoT devices
- **Neuromorphic prototyping**: Hardware validation of SRC neuron models
- **Energy-constrained SNNs**: Battery-powered neural processing with sub-mJ energy budget
- **Real-time signal processing**: Event-based processing with guaranteed latency

## Pitfalls
- **Offline training only**: Weights are computed offline and loaded; no on-chip learning
- **Limited precision**: 4-5 bit quantization introduces accuracy degradation vs. full precision
- **Model-specific**: SRC-specific implementation may not generalize to other neuron models
- **FPGA resource constraints**: LUT-register storage limits network size; larger networks require external memory

## Related Skills
- snn-mcu-fullfeature-edge (SNN on microcontrollers)
- circuit-level-spiking-neuron-robustness (hardware-robust spiking neurons)
- quantized-snn-hardware-optimization (SNN quantization)
- edgespike-edge-iot-snn (edge SNN deployment)
- neuromorphic-continual-nuclear-ics (neuromorphic continual learning)
- snn-fpga-hardware-software-codesign
