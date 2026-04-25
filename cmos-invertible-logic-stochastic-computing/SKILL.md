---
name: cmos-invertible-logic-stochastic-computing
description: "CMOS invertible logic using spiking stochastic computing — dual-mode (forward/reverse) logic gates based on Boltzmann machine configurations implemented with spiking neural networks and stochastic computing on minimal CMOS hardware. Activation: invertible logic, stochastic computing, spiking CMOS, Boltzmann machine logic, factorization hardware, reversible computing."
---

# CMOS Invertible Logic via Spiking Stochastic Computing

> Implements dual-mode (forward computation and reverse inference) logic using spiking neural networks based on stochastic computing principles, demonstrated on fabricated ASIC hardware for multiplication and factorization.

## Metadata
- **Source**: arXiv:2603.27030
- **Authors**: Sean C. Smithson, Naoya Onizawa, Brett H. Meyer, Warren J. Gross, Takahiro Hanyu
- **Published**: 2026-03-27
- **Categories**: cs.AR, cs.NE

## Core Methodology

### Key Innovation
Invertible logic gates that operate in two modes — forward (input → output) and reverse (output → consistent inputs) — implemented using spiking neural networks on stochastic computing principles. This is the first demonstration that simple spiking stochastic circuits can replicate Boltzmann-machine-based invertible logic with minimal CMOS hardware.

### Technical Framework

#### 1. Invertible Stochastic Gates
- Design methodology for gates that function bidirectionally
- Forward mode: standard Boolean computation (AND, OR, XOR)
- Reverse mode: output is fixed, inputs converge to consistent values via stochastic dynamics
- Based on Boltzmann machine probability distributions

#### 2. Spiking Neural Network Implementation
- Spiking neurons generate stochastic bit streams for probabilistic computation
- Spike timing encodes probability values (rate coding over stochastic bit sequences)
- Network dynamics naturally implement the sampling process required for Boltzmann machine inference

#### 3. Circuit Extensions
- Basic invertible gates compose into larger circuits
- **Invertible adder**: forward = addition, reverse = decomposition
- **Invertible multiplier**: forward = multiplication, reverse = factorization
- Minimal CMOS area per gate

#### 4. Hardware Validation
- Synthesizable RTL for FPGA and ASIC targets
- **Fabricated ASIC** with measurement results confirming correct operation
- Both multiplication and factorization demonstrated on silicon

## Implementation Guide

### Prerequisites
- CMOS design flow (RTL synthesis, place-and-route)
- Understanding of stochastic computing fundamentals
- Spiking neuron models (integrate-and-fire variants)

### Step-by-Step

1. **Design invertible stochastic gate**
   - Define forward truth table
   - Configure Boltzmann energy function for bidirectional sampling
   - Map to spiking neuron circuit with minimal transistor count

2. **Validate gate-level operation**
   - Forward mode: verify correct Boolean output
   - Reverse mode: verify input convergence to consistent values
   - Measure convergence time and accuracy vs. bit-stream length

3. **Compose into functional circuits**
   - Cascade gates for adder/multiplier construction
   - Verify forward computation matches deterministic reference
   - Test reverse mode (e.g., factorization of products)

4. **ASIC fabrication and test**
   - Synthesize to target technology node
   - Measure power, area, and timing
   - Validate forward and reverse modes on fabricated chip

### Code Example
```python
# Conceptual stochastic invertible AND gate
import numpy as np

def stochastic_and_forward(a_bits, b_bits):
    """Forward mode: AND two stochastic bit streams."""
    return [a & b for a, b in zip(a_bits, b_bits)]

def stochastic_and_reverse(y_bits, n_samples=1000):
    """Reverse mode: given output y, sample consistent (a, b) inputs."""
    # For AND: if y=1, both a=1 and b=1; if y=0, at least one is 0
    a_samples, b_samples = [], []
    for y in y_bits:
        if y == 1:
            a_samples.append(1)
            b_samples.append(1)
        else:
            # Stochastic sampling from {(0,0), (0,1), (1,0)}
            choice = np.random.randint(3)
            a_samples.append([0, 0, 1][choice])
            b_samples.append([0, 1, 0][choice])
    return a_samples, b_samples

# Spiking neuron wrapper for stochastic bit generation
class SpikingStochasticNeuron:
    def __init__(self, probability, length=256):
        self.prob = probability
        self.length = length
    
    def generate_bitstream(self):
        return (np.random.random(self.length) < self.prob).astype(int)
    
    def estimate_probability(self, bitstream):
        return np.mean(bitstream)
```

## Applications
- **Hardware factorization engines**: Reverse-mode multiplier performs integer factorization
- **Combinatorial optimization**: Boltzmann sampling on dedicated low-power hardware
- **Reversible computing**: Ultra-low-power computing paradigm for energy-constrained systems
- **Edge AI inference**: Stochastic circuits with natural error tolerance
- **Neuromorphic co-processors**: Spiking stochastic units as co-processors for conventional digital systems

## Key Results
- Correct operation of basic invertible gates (AND, OR, XOR)
- Successful extension to invertible adder and multiplier circuits
- **Fabricated ASIC** measurement results confirming silicon-level functionality
- Both multiplication (forward) and factorization (reverse) demonstrated on hardware

## Pitfalls
- Stochastic bit-stream length directly impacts accuracy — longer streams = better precision but slower convergence
- Reverse-mode convergence depends on problem complexity — factorization of large numbers may require many sampling steps
- Noise and variability in physical CMOS implementation can affect stochastic bit-stream quality
- Temperature sensitivity of spiking neuron circuits may require calibration

## Related Skills
- spiking-neural-network-training
- neuromorphic-low-power-ai
- snn-neuromorphic-fpga
- intrinsic-neurosynaptic-spiking-memristive
