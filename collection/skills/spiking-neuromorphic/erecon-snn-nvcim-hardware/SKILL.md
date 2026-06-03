---
name: erecon-snn-nvcim-hardware
description: "E-ReCON energy- and resource-efficient precision-configurable sparse nvCIM macro for conventional and spiking neural edge inference. Activation: nvCIM, ReRAM CIM, SNN hardware accelerator, edge-AI hardware, compute-in-memory SNN, neuromorphic hardware macro"
---

# E-ReCON: Energy-Efficient nvCIM Macro for SNN/CNN Edge Inference

> A 16 Kb energy- and resource-efficient digital compute-in-memory (DCIM) macro based on compact 3T1R ReRAM bitcell for edge-AI inference, supporting both conventional CNN and spiking neural network (SNN) workloads.

## Metadata
- **Source**: arXiv:2605.20717
- **Authors**: Ankit Kumar Tenwar, Mukul Lokhande, Santosh Kumar Vishvakarma
- **Published**: 2026-05-20
- **Categories**: cs.NE, cs.AR, cs.CV, eess.IV

## Core Methodology

### Key Innovation
E-ReCON introduces a **novel 3T1R ReRAM bitcell** (0.85 µm²) supporting AND-based in-memory multiplication for both CNN and SNN workloads. Key innovations:
- **Interleaved 10T/28T adder tree**: Reduces transistor count by 37% and power by 28% vs conventional 28T RCA design
- **Precision-configurable**: Adaptable bit precision for different inference accuracy requirements
- **Dual workload support**: Same macro handles both CNN multiply-accumulate and SNN spike-weight multiplication
- **40% pruning preserves 99.8% accuracy** while reducing MAC operations
- **2A2W configuration**: Achieves accuracy close to FP32 baseline across VGG-8/16 and ResNet-18

### Technical Architecture

**Bitcell Design (3T1R):**
- 3 transistors + 1 ReRAM device per bitcell
- AND-type in-memory multiplication for both analog (CNN) and binary (SNN) operations
- 0.85 µm² cell area in 65nm CMOS

**Adder Tree Innovation:**
- Interleaved 10T (partial product) + 28T (final accumulation) structure
- Reduces switching activity for SNN workloads (binary spike inputs = low activity)
- 37% fewer transistors, 28% lower power

**Macro Specifications:**
- 16 Kb total capacity
- 65nm CMOS @ 1.2V
- Min latency: 0.48 ns
- Throughput: 2.31-3.1 TOPS
- Energy efficiency: up to 419 TOPS/W

**SNN-Oriented Workflow:**
1. Binary spike inputs → AND with stored weights → partial products
2. Interleaved adder tree accumulates partial products
3. Configurable precision for weight representation (1-8 bits)
4. 2A2W (2-activation, 2-weight) precision matches FP32 accuracy

## Implementation Guide

### Prerequisites
- 65nm CMOS process with ReRAM integration
- Standard digital design flow (RTL → synthesis → P&R)
- SNN/CNN model quantization pipeline

### Performance Comparison

| Metric | E-ReCON | Prior ADC-based ReRAM-CIM | Improvement |
|--------|---------|--------------------------|-------------|
| Area/bitcell | 0.85 µm² | ~1.2-2.0 µm² | 30-58% |
| Latency | 0.48 ns | ~1-2 ns | 52-76% |
| Energy Efficiency | 419 TOPS/W | ~250-300 TOPS/W | 30-40% |
| Transistor Count (adder) | 10T/28T (interleaved) | 28T (RCA) | 37% reduction |

### CNN Accuracy Results
- LeNet-5 on MNIST/A-Z: 97.81%
- AlexNet on CIFAR-10: 93.23%
- CNN-8 on SVHN: 96.51%

### SNN Accuracy with 2A2W Configuration
- VGG-8 on CIFAR-10/100: Near FP32 baseline
- VGG-16 on CIFAR-10/100: Near FP32 baseline
- ResNet-18 on ImageNet-1K: Near FP32 baseline

## Applications
- **Edge AI inference**: Low-power, high-throughput inference on IoT devices
- **Neuromorphic computing**: SNN hardware acceleration for event-based sensors
- **Biomedical sensing**: Ultra-low-power inference for wearable health monitors
- **Smart sensors**: On-sensor processing for DVS cameras and other neuromorphic sensors
- **IoT endpoints**: Battery-operated devices requiring always-on inference

## Related Skills
- edgespike-edge-iot-snn
- clockless-asynchronous-neuromorphic-computing
- sram-cim-snn-accelerator
- snn-fpga-hardware-software-codesign
- spiker-ll-fpga-snn-accelerator
- quantized-snn-hardware-optimization
