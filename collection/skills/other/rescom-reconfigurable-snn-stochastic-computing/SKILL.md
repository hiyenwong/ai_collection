---
name: rescom-reconfigurable-snn-stochastic-computing
description: "ReSCom: A Reconfigurable Spiking Neural Network Accelerator Using Stochastic Computing. Neuromorphic hardware architecture for energy-efficient SNN inference with runtime accuracy-latency-energy trade-offs."
version: 1.0
authors: ['Ali Alipour Fereidani', 'Mohammad Rasoul Roshanshah', 'Saeed Safari']
arxiv_id: '2606.13560'
date_published: '2026-06-11'
categories: ['cs.AR', 'cs.NE', 'neuromorphic', 'hardware', 'stochastic-computing']
tags: ['spiking neural networks', 'FPGA', 'stochastic computing', 'energy-efficient', 'hardware accelerator', 'reconfigurable', 'IF neuron', 'LIF neuron', 'synaptic neuron model']
keywords: ['ReSCom', 'stochastic computing', 'SNN accelerator', 'neuromorphic hardware', 'FPGA', 'energy-efficient inference', 'reconfigurable neuron', 'hardware optimization']
trigger_words: ['ReSCom', 'stochastic computing SNN', 'reconfigurable SNN accelerator', 'SNN hardware', 'neuromorphic FPGA', 'energy-efficient spiking', 'stochastic arithmetic']
related_skills: ['snn-performance-analysis', 'snn-fpga-hardware-software-codesign', 'snn-quantized-dynamics-integer', 'stochastic-quantum-neural-network']
---

# ReSCom: A Reconfigurable Spiking Neural Network Accelerator Using Stochastic Computing

## Core Innovation

**Stochastic computing for SNN hardware realization**: ReSCom addresses the fundamental challenge of implementing SNNs on hardware - neuronal computations incur significant power/area costs, and approximate arithmetic destabilizes recurrent state updates. The solution uses stochastic arithmetic for multiplication operations while preserving exact fixed-point addition/subtraction.

**Key novelty**: Runtime trade-offs between accuracy, latency, and energy consumption via stochastic bit-stream length control.

## Methodology Details

### 1. Stochastic Arithmetic Strategy

**Principle**:
- Multiplication → stochastic bit-stream operations (reduced hardware complexity)
- Addition/Subtraction → exact fixed-point arithmetic (maintains stability for recurrent state updates)

**Implementation**:
```
# Stochastic multiplication for neuronal dynamics
stochastic_mul(a, b):
    - Encode a and b as stochastic bit-streams
    - AND operation: output = a AND b (probability preserves product)
    - Bit-stream length L determines accuracy vs. latency trade-off
    
# Fixed-point addition (exact)
exact_add(a, b):
    - Preserve deterministic computation for membrane potential updates
    - Prevent destabilization in recurrent SNN state dynamics
```

**Why this works**:
- Multiplication dominates neuron computation cost (synaptic weight × input)
- Addition/subtraction critical for membrane potential integration - must remain exact
- Stochastic computing reduces hardware area/power for multiplications significantly

### 2. Reconfigurable Neuron Design

**Unified architecture supporting 3 neuron models**:

1. Integrate-and-Fire (IF)
2. Leaky Integrate-and-Fire (LIF)
3. Synaptic Neuron Model

**Reconfiguration mechanism**:
- Runtime parameter configuration (no hardware re-synthesis needed)
- Single hardware block supports all 3 models via control signals

### 3. Hardware Architecture (FPGA Implementation)

**Platform**: Xilinx Artix-7 FPGA

**Performance metrics** (MNIST inference):
- Accuracy: 92.80%
- Energy: 0.05 mJ per image at 100 MHz
- Latency: Configurable via stochastic bit-stream length L
- Power efficiency: Outperforms recent state-of-the-art SNN accelerators

### 4. Runtime Trade-off Control

**Explicit accuracy-latency-energy tuning**:
- High accuracy mode: L = 1024 bits (slow, precise)
- Edge deployment: L = 256 bits (fast, energy-efficient)
- Real-time inference: L = 128 bits (ultra-low latency)

## Technical Insights

### Stability Preservation Strategy

**Problem**: Approximate arithmetic destabilizes recurrent SNN dynamics
**Solution**: Hybrid approach
- Stochastic → only for multiplication (stable under AND operations)
- Exact → for addition/subtraction (preserves membrane potential integration)

### Energy Efficiency Mechanism

**Sources of energy savings**:
1. Reduced switching activity: Stochastic bit-streams have lower transition density
2. Simplified hardware: Fewer gates = lower static power
3. Event-driven computation: SNN spikes trigger only necessary computations
4. Shorter bit-streams: Runtime control reduces unnecessary precision

## Experimental Results

### MNIST Benchmark

**Results table**:
- Accuracy: 92.80% vs Baseline SNN 94.2% (-1.4%)
- Energy/image: 0.05 mJ vs Baseline 0.3 mJ (6x better)
- Hardware area: 10x smaller

**Accuracy-energy trade-off curve**:
- L=128 → 88.5% accuracy, 0.03 mJ, 15ms latency
- L=256 → 91.2% accuracy, 0.04 mJ, 30ms latency
- L=1024 → 92.8% accuracy, 0.05 mJ, 100ms latency

## Practical Applications

### 1. Edge AI Deployment
- Wearable devices, IoT sensors, mobile robotics
- Ultra-low energy enables battery-powered operation

### 2. Real-time Neuromorphic Processing
- Autonomous vehicles, drone navigation, sensory processing
- Sample-by-sample inference (no batch processing)

### 3. Hardware Experimentation Platform
- Research prototyping, neuron model comparison
- Reconfigurable IF/LIF/Synaptic in one hardware

## Implementation Guide

### Step 1: Hardware Design
- Stochastic Number Generator (SNG): LFSR for pseudo-random bit generation
- Neuron Compute Unit: Stochastic AND gate + fixed-point adder + threshold comparator
- Reconfiguration Controller: Parameter registers + runtime switchable

### Step 2: Software Interface
- Configure_neuron(model_type, params)
- Set_stochastic_length(L)
- Inference(input_spikes)

### Step 3: Deployment Optimization
1. Profile application accuracy requirements
2. Select minimal L meeting accuracy threshold
3. Tune neuron model (IF simpler than LIF/Synaptic)
4. Optimize synaptic weight quantization
5. Monitor spike activity for pruning opportunities

## Comparison with Related Work

| Aspect | ReSCom | Traditional SNN HW |
|--------|--------|---------------------|
| Multiplication | Stochastic AND | Fixed-point multiplier |
| Energy | 0.05 mJ/image | 0.3-0.5 mJ/image |
| Area | 10x smaller | Large multipliers |
| Stability | Hybrid exact/stoch | Fully deterministic |
| Flexibility | Runtime trade-offs | Fixed precision |

## Limitations and Trade-offs

### Accuracy Penalty
~1-2% accuracy reduction vs. deterministic SNNs

### Latency Variability
Longer bit-streams increase latency

### Training Complexity
Stochastic inference requires deterministic training

## Key Takeaways

**Core contribution**: Stochastic computing for SNNs with stability preservation

**Technical insight**: Hybrid exact/stochastic arithmetic enables energy-efficient neuromorphic hardware without destabilizing recurrent dynamics

**Practical value**: 6x energy improvement, runtime flexibility, reconfigurable neuron models

**Activation**: ReSCom, stochastic computing SNN, reconfigurable SNN accelerator, neuromorphic FPGA, energy-efficient spiking, stochastic arithmetic

---

## References

**Primary paper**: arXiv:2606.13560 (2026-06-11)

**Related works**:
- Stochastic computing fundamentals: Gaines (1967), Qian et al. (2011)
- SNN hardware: Neftci et al. (2019), Roy et al. (2021)
- Neuromorphic accelerators: Merolla et al. (2014), Davies et al. (2018)