---
name: neuromorphic-spacecraft-pose-event-camera
description: "End-to-end spacecraft 6-DoF pose estimation using event cameras and BrainChip Akida neuromorphic processor. MobileNet-style keypoint regression on event-frame representations with quantization-aware training (8/4-bit) converted to spiking neural networks. First demonstration of spacecraft pose estimation on Akida hardware. Activation: neuromorphic, event camera, spacecraft pose, Akida, spiking neural network, space robotics, event-based vision."
---

# Efficient Onboard Spacecraft Pose Estimation with Event Cameras and Neuromorphic Hardware

**arXiv:** [2604.04117](https://arxiv.org/abs/2604.04117)  
**Published:** 2026-04-05  
**Authors:** Arunkumar Rathinam, Jules Lecomte, Jost Reelsen, Gregor Lenz, Axel von Arnim et al.  
**Categories:** cs.RO, cs.CV, cs.LG

## Problem

Space imagery for autonomous rendezvous and proximity operations faces:
- Extreme illumination variations
- High contrast ratios
- Fast target motion causing motion blur
- Strict power/compute constraints on spacecraft

Traditional frame-based cameras saturate or blur under these conditions.

## Core Solution

### Event Cameras + Neuromorphic Processing
- **Event cameras:** Asynchronous, change-driven measurements — remain informative when frame-based imagery fails
- **Neuromorphic processors (Akida):** Exploit sparse activations for low-latency, energy-efficient inference

### Pipeline Architecture

```
Event Camera → Event Frame Representation → MobileNet Keypoint Regression 
    → Quantization (8/4-bit) → Akida SNN Conversion → 6-DoF Pose
```

### Component 1: Event Representations
Three event-frame representations benchmarked:
1. **Time surface** — encodes temporal dynamics of events
2. **Event count/frame** — accumulates events per pixel
3. **Exponential decay surface** — weighted temporal representation

### Component 2: Keypoint Regression Network
- **MobileNet-style** lightweight CNN architecture
- Keypoint regression for spacecraft landmark detection
- Designed for spacecraft geometry (solar panels, antenna, body)

### Component 3: Neuromorphic Model Conversion
- **Quantization-Aware Training (QAT):** 8-bit and 4-bit precision
- Conversion to **Akida-compatible spiking neural networks**
- Maintains accuracy while enabling neuromorphic inference

### Component 4: Akida V1/V2 Deployment
- **Akida V1:** Physical hardware benchmarking
- **Akida V2 (Cloud):** Heatmap-based model with improved pose accuracy
- Real-time, low-power inference on neuromorphic hardware

## Key Results

### SPADES Dataset Evaluation
- Real-time inference on Akida V1 hardware
- Akida V2 with heatmap model yields improved pose accuracy
- **First end-to-end demonstration** of spacecraft pose estimation on Akida hardware

### Advantages over Frame-Based Approaches
- Robust to extreme illumination changes
- No motion blur from fast target motion
- Low power consumption suitable for spacecraft
- Low latency from sparse event processing

## Reusable Methodology

### 1. Event-to-SNN Pipeline for Space Applications
```python
# Pipeline pattern
events = event_camera.capture()
event_frame = event_representation(events, method='time_surface')
keypoints = mobilenet_regressor(event_frame)
keypoints_quantized = quantize_aware(keypoints, bits=4)
snn_model = convert_to_akida(keypoints_quantized)
pose_6dof = estimate_pose(keypoints)
```

### 2. Quantization-Aware Training for Neuromorphic Conversion
- Train with fake quantization operators
- Fine-tune with target bit-width constraints
- Validate Akida SNN accuracy matches float model

### 3. Event Representation Selection
- Benchmark multiple representations for target application
- Consider temporal dynamics vs spatial resolution tradeoff
- SPADES dataset provides standardized evaluation

### 4. Heatmap-Based Pose Estimation (Akida V2)
- Replace direct regression with heatmap keypoint detection
- Better suited for spiking network inference patterns
- Improved accuracy on neuromorphic hardware

## Applications

- **Autonomous rendezvous:** Spacecraft approach and docking
- **Proximity operations:** Close-range satellite servicing
- **Space debris tracking:** Pose estimation for non-cooperative targets
- **Onboard processing:** Edge AI for space missions with strict power budgets
- **Planetary landing:** Terrain-relative navigation with event cameras

## Datasets

- **SPADES:** Spacecraft Pose Estimation Dataset with Event Cameras
  - Event camera data of spacecraft models
  - Ground truth 6-DoF pose annotations
  - Various illumination and motion conditions

## Key Innovations

1. **First end-to-end** spacecraft pose estimation on Akida neuromorphic hardware
2. Event camera + neuromorphic SNN pipeline for space applications
3. Quantization-aware training with 8/4-bit conversion to spiking networks
4. Heatmap-based Akida V2 model for improved accuracy
5. Practical route to low-latency, low-power space perception

## Limitations

- Akida V1 has limited model complexity support
- Event cameras have lower spatial resolution than frame cameras
- Training requires SPADES or similar space-specific datasets
- Hardware-dependent (Akida-specific conversion pipeline)

## Related Skills

- `neuromorphic-low-power-ai`: Neuromorphic computing for energy-efficient AI
- `snn-neuromorphic-fpga`: SNN on FPGA platforms
- `spiking-neural-network-training`: Training methodologies for SNNs
- `neuromorphic-spiking-ring-attractor-v2`: Neuromorphic spiking networks
