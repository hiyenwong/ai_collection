---
name: neuromorphic-fw mav-snn-control
description: "Neuromorphic control of flapping-wing micro aerial vehicles using SNNs on resource-constrained ESP32 microcontroller. Hierarchical SNN framework: state estimation + CPG modulation for wing actuation. 36% latency reduction, 18% power reduction vs ANN. First onboard neuromorphic autonomous flight."
tags: ["neuromorphic-control", "spiking-neural-network", "micro-aerial-vehicle", "embedded-ai", "central-pattern-generator", "edge-computing"]
category: ai_collection
---

# Neuromorphic Control of Flapping-Wing MAV on Resource-Constrained Hardware

**arXiv**: 2605.19430 (May 19, 2026)
**Authors**: Rim El Filali, Chenrui Feng, Chao Gao, Weibin Gu
**Category**: Robotics (cs.RO)

## Overview

First demonstration of **fully onboard neuromorphic control** for autonomous flight of a Flapping-Wing Micro Aerial Vehicle (FWMAV). Deploys two lightweight Spiking Neural Networks (SNNs) on a **$5 ESP32 microcontroller** for closed-loop flight control of a butterfly-inspired robot (<30g).

## Core Innovation

### Hierarchical Neuromorphic Control Framework

```
Raw Sensors -> SNN #1: State Estimation -> Estimated State
                                           |
                              SNN #2: CPG Modulation -> Wing Actuation
```

1. **State Estimation SNN**: Processes raw sensory feedback -> estimates pitch/heading angles
2. **CPG Modulation SNN**: Takes estimated state -> modulates Central Pattern Generator for wing actuation

### Key Results

| Metric | ANN Baseline | SNN Controller | Improvement |
|--------|-------------|----------------|-------------|
| Inference Latency | 1059 us | **680 us** | 36% reduction |
| Inference Power | 0.033 W | **0.027 W** | 18% reduction |
| Training | Imitation learning | Imitation learning | Same |
| Flight Performance | Stable tracking | **Stable tracking** | Equivalent |

### Platform Details

- **Robot**: Butterfly-inspired FWMAV, <30g
- **Controller**: ESP32 microcontroller (~$5 unit cost)
- **Control Tasks**: Pitch and heading angle tracking
- **Flight Type**: Untethered real-world flight

## Methodology

### SNN Architecture

**State Estimation Network**
- Input: Raw sensor data (IMU, etc.)
- Output: Estimated pitch and heading angles
- Lightweight design for ESP32 constraints

**CPG Modulation Network**
- Input: Estimated state from state estimation SNN
- Output: Modulation signals for wing actuation CPG
- Maps desired trajectory to wing kinematics

### Training: Imitation Learning

- Teacher: Conventional controller (ANN or model-based)
- Student: SNN learns to imitate teacher's control policy
- Deployment: SNN replaces teacher for inference

### Central Pattern Generator (CPG)

- Bio-inspired oscillatory pattern generator for wing actuation
- SNN modulates CPG parameters (frequency, amplitude, phase)
- Enables stable flapping patterns with SNN-level control

## Implementation Considerations

### ESP32 Deployment

- **Resource constraints**: Limited RAM, CPU, power budget
- **SNN advantages**: Event-driven computation, sparse activation
- **No specialized hardware**: Runs on widely available ESP32

### SWaP Constraints

- **Size**: Sub-30g total system weight
- **Weight**: Minimal payload capacity
- **Power**: Battery-limited operation
- SNN's 18% power reduction directly extends flight time

### Latency-Critical Control

- Flapping-wing dynamics require sub-millisecond control loops
- SNN's 36% latency reduction enables tighter control
- Critical for stability of inherently unstable FWMAV

## Applications

- **Micro aerial vehicles**: Insect-scale robots, surveillance
- **Embedded AI**: Ultra-low-power autonomous systems
- **Bio-inspired robotics**: Biomimetic flight control
- **Edge computing**: AI on constrained microcontrollers
- **Swarm robotics**: Multiple low-cost autonomous agents

## Comparison with Existing Approaches

| Approach | Hardware | Latency | Power | Onboard Control |
|----------|----------|---------|-------|-----------------|
| Conventional ANN | ESP32 | 1059 us | 0.033 W | Yes |
| SNN (this work) | ESP32 | **680 us** | **0.027 W** | Yes |
| Neuromorphic chip | Loihi/SpiNNaker | Lower | Lower | Specialized HW required |
| Offboard control | GPU server | Lowest | Highest | No (tethered) |

## Limitations

- **Single platform**: Demonstrated on one FWMAV design
- **2D control**: Pitch and heading only (no full 3D position control)
- **Indoor flight**: Real-world but constrained environment
- **Imitation learning bound**: SNN performance limited by teacher quality

## Activation Keywords

- neuromorphic fw mav
- spiking neural network control
- flapping wing robot control
- ESP32 neuromorphic
- CPG modulation SNN
- imitation learning SNN
- micro aerial vehicle neuromorphic
- embedded spiking control
- resource-constrained SNN
- butterfly robot control
- neuromorphic autonomous flight

## Citation

```bibtex
@article{elfilali2026neuromorphic,
  title={Neuromorphic Control of a Flapping-Wing Robot on Resource-Constrained Hardware},
  author={El Filali, Rim and Feng, Chenrui and Gao, Chao and Gu, Weibin},
  journal={arXiv preprint arXiv:2605.19430},
  year={2026}
}
```
