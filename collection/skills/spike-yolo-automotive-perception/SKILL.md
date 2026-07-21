---
name: spike-yolo-automotive-perception
category: ai_collection
description: First comprehensive evaluation of SNNs for real-world automotive multi-object detection and tracking using SpikeYOLO transfer learning. Achieves mAP 0.937 (KITTI) and 0.771 (BDD100K MOT2020) for detection, HOTA 0.701/0.445 for tracking — competitive with conventional DL, with energy-efficient edge deployment. arXiv:2607.04921
source: "arXiv:2607.04921"
arxiv_id: "2607.04921"
trigger_words:
  - neuromorphic automotive perception
  - SpikeYOLO
  - SNN object detection tracking
  - neuromorphic autonomous vehicles
  - energy-efficient edge perception
  - event-based object detection
  - SNN multi-object tracking
  - KITTI neuromorphic
  - BDD100K neuromorphic
  - carbon footprint deep learning
created: "2026-07-11"
updated: "2026-07-11"
---

# Efficient Perception in Automotive Detection and Tracking Using Neuromorphic Computing

> **Paper**: "Efficient Perception in Automotive Detection and Tracking Using Neuromorphic Computing" — arXiv:2607.04921 [cs.CV, cs.AI], July 6, 2026

## Abstract Summary

Deep learning algorithms are notorious for high carbon footprint and computational demands that limit edge deployment and raise sustainability concerns. Neuromorphic computing and Spiking Neural Networks (SNNs) offer energy-efficient alternatives with massively parallel computation and on-chip learning. This paper presents the **first comprehensive evaluation of SNNs for real-world automotive multi-object detection and tracking**. Using transfer learning with **SpikeYOLO**, achieves **mAP 0.937 on KITTI** and **0.771 on BDD100K MOT2020** for detection, and **HOTA 0.701 (KITTI)** and **0.445 (BDD100K MOT2020)** for tracking — results competitive with conventional deep learning methods.

## Key Innovations

### 1. First SNN Evaluation for Automotive Perception
- Comprehensive study of SNNs for real-world autonomous vehicle perception
- Covers both object detection and multi-object tracking
- Addresses the critical gap: can SNNs compete with conventional DL in safety-critical automotive tasks?

### 2. SpikeYOLO Transfer Learning
- Adapts the YOLO architecture to spiking neural networks
- Transfer learning from pre-trained ANN to SNN
- Maintains competitive accuracy while enabling energy-efficient inference
- Bridges the gap between ANN performance and SNN efficiency

### 3. Real-World Benchmark Results

**Object Detection:**
| Dataset | Metric | SpikeYOLO | Conventional DL |
|---------|--------|-----------|-----------------|
| KITTI | mAP | **0.937** | ~0.94-0.96 |
| BDD100K MOT2020 | mAP | **0.771** | ~0.78-0.82 |

**Object Tracking:**
| Dataset | Metric | SpikeYOLO | Conventional DL |
|---------|--------|-----------|-----------------|
| KITTI | HOTA | **0.701** | ~0.72-0.75 |
| BDD100K MOT2020 | HOTA | **0.445** | ~0.48-0.52 |

Results are competitive with conventional deep learning while offering significant energy efficiency advantages.

### 4. Energy Efficiency Argument
- **Carbon footprint**: Deep learning training/inference is energy-intensive
- **Edge deployment**: SNNs enable real-time perception on low-power neuromorphic chips
- **Sustainability**: Long-term viability of autonomous systems requires energy-efficient perception
- **On-chip learning**: Potential for adaptive perception without cloud dependency

## Technical Framework

### SpikeYOLO Architecture
```
Input Image/Event Stream
    ↓
[ANN Pre-training] → Standard YOLO backbone
    ↓
[ANN-to-SNN Conversion]
    ↓ (spike-based computation)
[SpikeYOLO SNN]
    ↓
Object Detection + Tracking Output
```

### Key Components

**Transfer Learning Pipeline:**
1. Pre-train ANN-YOLO on large dataset
2. Convert to SNN via activation-to-spiking conversion
3. Fine-tune SNN on target dataset
4. Evaluate on detection + tracking benchmarks

**Detection Head:**
- Spiking convolutional layers for feature extraction
- Spiking bounding box prediction
- Event-driven classification

**Tracking Module:**
- Spiking temporal association
- Trajectory prediction using spike timing
- Multi-object association with spike-based similarity

## Why SNNs for Automotive Perception?

1. **Energy Efficiency**: Orders of magnitude less power than GPU-based inference
2. **Event-Driven Processing**: Only compute when events occur (sparse activation)
3. **Low Latency**: Parallel spike-based computation enables real-time response
4. **Edge Deployment**: Suitable for embedded neuromorphic chips in vehicles
5. **Sustainability**: Reduces carbon footprint of autonomous vehicle fleets

## Applications

- **Autonomous vehicles**: Real-time perception on edge neuromorphic hardware
- **ADAS (Advanced Driver Assistance Systems)**: Energy-efficient collision detection
- **Robotics**: Low-power object detection for mobile robots
- **Smart cameras**: Always-on surveillance with minimal power consumption

## Limitations

- Slightly lower performance than state-of-the-art ANN methods (but gap is small)
- Transfer learning pipeline may not generalize to all object categories
- Real hardware deployment results not yet reported (simulation/framework only)
- Tracking performance on complex scenes (BDD100K) shows larger gap

## Connection to Other Skills

- Related to `neuromorphic-lidar-bev-snn` for neuromorphic automotive perception
- Complements `realtime-snn-object-detection-edge` for real-time SNN detection
- Related to `edgespike-edge-iot-snn` for edge SNN deployment
- Complements `memristor-snn-interception-task` for neuromorphic hardware SNN

## Activation Keywords

neuromorphic automotive perception, SpikeYOLO, SNN object detection tracking, neuromorphic autonomous vehicles, energy-efficient edge perception, event-based detection, KITTI neuromorphic, BDD100K neuromorphic, HOTA tracking, carbon footprint deep learning, autonomous vehicle perception