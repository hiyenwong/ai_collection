---
name: gelneuro-neuromorphic-tactile-system
description: Fully integrated sensing-computing neuromorphic visuo-tactile system for texture recognition on edge hardware
tags: [neuromorphic, tactile-sensing, spiking-neural-network, edge-computing, robotics, texture-recognition, low-power]
source: arXiv:2607.05241v1
created: 2026-07-08
---

# GelNeuro: Neuromorphic Tactile System for Texture Recognition

## Core Innovation

First fully integrated sensing-computing visuo-tactile system that directly pairs GelSight Mini optical tactile sensor with Speck2f neuromorphic SoC, achieving 96.3% accuracy with only 19.6 mW power consumption.

## System Architecture

### 1. Sensing Front-End: GelSight Mini
- Optical tactile sensor with elastomer gel
- Captures contact-induced marker motions
- High-resolution tactile imaging
- Converts physical contact to visual data

### 2. Neuromorphic Processing: Speck2f SoC
- Dynamic Vision Sensor (DVS) captures marker motions as events
- On-chip spiking convolutional neural network (SCNN) classifier
- Integrated event routing and processing
- 8-bit quantized deployment

### 3. Hardware-Aware Optimization
- **Weight clamping strategy** mitigates 8-bit deployment accuracy loss
- Maintains performance under quantization constraints
- Optimized for neuromorphic hardware characteristics

## Performance Metrics

### Accuracy
- **15-class natural texture recognition**: 96.3%
- **Inference window**: 80 ms
- **Hardware-in-the-loop testing**: Physical chip validation

### Power Efficiency
- **Board-level active power**: 19.6 mW
- **Comparison**: 3 orders of magnitude lower than CPU/GPU baselines
- **Energy efficiency**: Ultra-low power for edge deployment

### Generalization
- Robust across unseen contact depths
- Maintains performance under varying pressure conditions
- Adapts to different tactile interaction scenarios

## Technical Pipeline

1. **Tactile Contact**: GelSight Mini captures surface texture
2. **Event Generation**: DVS converts marker motions to spike events
3. **On-Chip Routing**: Events routed through neuromorphic network
4. **SCNN Classification**: Spiking convolutional network processes events
5. **Texture Prediction**: Output texture class within 80 ms

## Key Innovations

### Direct Sensor-to-Chip Integration
- Eliminates host computer dependency
- No preprocessing or relaying required
- End-to-end edge processing

### Hardware-Aware Training
- Accounts for 8-bit quantization during training
- Weight clamping prevents accuracy degradation
- Optimized for neuromorphic hardware constraints

### Ultra-Low Power Operation
- 19.6 mW board-level power
- Suitable for battery-operated robots
- Enables always-on tactile sensing

## Applications

- **Robotic manipulation**: Texture-based object recognition
- **Prosthetics**: Tactile feedback for artificial limbs
- **Quality inspection**: Surface texture analysis
- **Human-robot interaction**: Safe contact detection

## Comparison with Baselines

| Metric | GelNeuro | CPU Baseline | GPU Baseline |
|--------|----------|--------------|--------------|
| Accuracy | 96.3% | ~95% | ~96% |
| Power | 19.6 mW | ~20 W | ~50 W |
| Latency | 80 ms | ~100 ms | ~80 ms |
| Form factor | Edge SoC | Desktop | Desktop |

## Implementation Details

### Hardware
- **Sensor**: GelSight Mini optical tactile sensor
- **Processor**: Speck2f neuromorphic SoC
- **Event camera**: Dynamic Vision Sensor (DVS)
- **Deployment**: 8-bit quantized SCNN

### Software
- Event-driven processing pipeline
- Hardware-aware weight quantization
- Real-time inference engine

## Challenges Addressed

1. **Host dependency**: Previous systems required external preprocessing
2. **Power consumption**: Conventional systems consume 1000x more power
3. **Latency**: End-to-end processing reduces system latency
4. **Deployment complexity**: Integrated system simplifies deployment

## Activation Triggers

neuromorphic-tactile, tactile-sensing, texture-recognition, edge-neuromorphic, spiking-convolutional, low-power-robotics, GelSight, Speck2f, visuo-tactile, hardware-aware-quantization

## Related Concepts

- Spiking Neural Networks (SNNs)
- Neuromorphic computing
- Tactile sensing
- Edge AI
- Robotics perception
- Hardware-software co-design
