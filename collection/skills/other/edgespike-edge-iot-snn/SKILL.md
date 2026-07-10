---
name: edgespike-edge-iot-snn
description: "EdgeSpike: SNN framework for low-power autonomous sensing on edge IoT. Covers hybrid surrogate-gradient training, hardware-aware NAS, event-driven runtime for Loihi 2/SpiNNaker 2/ARM Cortex-M, and local plasticity for on-device adaptation. Activation: edge SNN, IoT sensing, low-power neural networks, neuromorphic edge deployment."
---

# EdgeSpike: SNN Framework for Low-Power Edge IoT Sensing

> Co-designed spiking neural network framework achieving 31x energy reduction on neuromorphic hardware and 6.1x on commodity microcontrollers, with open-source release for autonomous edge sensing.

## Metadata
- **Source**: arXiv:2604.27004
- **Authors**: Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov, Taner Yilmaz
- **Published**: 2026-04-29
- **Submitted to**: IEEE Internet of Things Journal

## Core Methodology

### Four-Pillar Architecture
EdgeSpike unifies four key components:

1. **Hybrid Training Pipeline**: Combines surrogate-gradient backpropagation with direct encoding for SNN training
2. **Hardware-Aware Neural Architecture Search (NAS)**: Searches 8400+ candidates bounded by per-inference energy and memory budgets, yielding a 12-point Pareto front
3. **Event-Driven Runtime**: Targets three hardware tiers:
   - Neuromorphic: Intel Loihi 2, SpiNNaker 2
   - Commodity: ARM Cortex-M microcontrollers with custom spike-sparse SIMD kernels
4. **Local Plasticity Rule**: Lightweight on-device adaptation enabling continual learning without backpropagation

### Key Results
- **Accuracy**: 91.4% mean across 5 tasks (within 1.2pp of INT8 CNN baselines at 92.6%)
- **Energy**: 18-47x reduction on neuromorphic hardware (mean 31x), 4.6-7.9x on Cortex-M (mean 6.1x)
- **Latency**: ≤9.4ms across all 15 task-hardware configurations
- **Battery Life**: 6.3x extension (312→1978 days at 2Wh per node) in 7-month, 64-node field deployment
- **Drift Resilience**: 0.7pp degradation with on-device adaptation vs 2.1pp without

### Evaluated Tasks
1. Keyword spotting
2. Vibration-based machine fault detection
3. Surface electromyography (sEMG) gesture recognition
4. 77 GHz radar human-activity classification
5. Structural-health acoustic-emission monitoring

## Implementation Guide

### Prerequisites
- Intel Loihi 2 SDK or SpiNNaker 2 toolchain
- ARM Cortex-M development board (e.g., STM32)
- Python with PyTorch for training pipeline

### Step-by-Step
1. Define energy/memory budget constraints for target hardware
2. Run hardware-aware NAS to search architecture space (8400+ candidates)
3. Select Pareto-optimal architecture from the 12-point frontier
4. Train using hybrid surrogate-gradient + direct encoding pipeline
5. Deploy event-driven runtime on target hardware
6. Enable local plasticity for continual on-device adaptation

### Code Architecture
```
EdgeSpike/
├── training/          # Hybrid surrogate-gradient + direct encoding
├── nas/               # Hardware-aware neural architecture search
├── runtime/           # Event-driven inference engines
│   ├── loihi2/        # Intel Loihi 2 backend
│   ├── spinnaker2/    # SpiNNaker 2 backend
│   └── cortexm/       # ARM Cortex-M with spike-sparse SIMD
└── plasticity/        # Local on-device adaptation rules
```

## Applications
- Autonomous IoT sensor networks with multi-year battery life
- Industrial predictive maintenance (vibration fault detection)
- Wearable gesture recognition (sEMG-based)
- Radar-based human activity monitoring
- Structural health monitoring

## Pitfalls
- Accuracy trade-off: ~1.2pp below strong INT8 CNN baselines
- Hardware-specific optimizations may limit portability between targets
- Local plasticity provides bounded adaptation; major distribution shifts still require retraining

## Related Skills
- quantization-spiking-neural-networks-beyond-accuracy
- snn-performance-analysis
- snn-edge-intelligence-survey
