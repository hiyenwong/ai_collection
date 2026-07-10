---
name: sensorless-gaze-hri-framework
description: "Neuroscience-inspired sensorless gaze-following framework for human-robot interaction. Uses perceptual illusions and brain's convexity assumptions to create gaze-following robots without cameras or sensors. Activation: sensorless gaze, perceptual gaze, cardboard robot, convexity prior, gaze-following HRI, low-cost robot gaze, perception neuroscience HRI."
---

# Sensorless Gaze-Following Framework for HRI

> A neuroscience-inspired framework that creates perceptual gaze-following in human-robot interaction without sensors, cameras, or computation by leveraging the brain's convexity prior and face processing mechanisms.

## Metadata
- **Source**: arXiv:2604.09829v1
- **Authors**: Mason Kadem
- **Published**: 2026-04-10

## Core Methodology

### Key Innovation
Instead of using expensive sensors ($30,000+ platforms) and complex computer vision algorithms to track human gaze, this framework **inverts the gaze computation problem** by leveraging the human visual system's own perceptual mechanisms. The robot's design exploits the brain's assumptions about convexity and face processing, making the human viewer's perceptual system serve as the "sensor" and "computer."

### Theoretical Foundation

The framework is grounded in three converging lines of neuroscience evidence:

#### 1. Distributed Face Processing Network
- The **superior temporal sulcus (STS)** computes gaze direction in the human brain
- This network processes facial features to determine where someone is looking
- **Leveraged**: Robot designs that activate this network through facial features

#### 2. Convexity Prior
- The brain has a high-precision **convexity prior** that assumes faces are convex
- This causes the brain to perceive concave faces as convex (hollow-face illusion)
- **Leveraged**: Concave eye sockets that appear convex to the viewer

#### 3. Predictive Processing Hierarchy
- **Top-down knowledge** about faces overrides bottom-up depth signals
- The brain predicts expected visual input based on prior knowledge
- **Leveraged**: Painted pupils in concave sockets create mutual gaze perception

### Design Implementation

#### Sub-Dollar Cardboard Robot Design
- **Material**: Cardboard construction (cost < $1)
- **Eye Design**: Parameterized concave eye sockets with interchangeable inserts
- **Key Feature**: Painted pupil positioned to produce perceived mutual gaze from any viewing angle

#### Why It Works
1. Concave socket → brain perceives as convex (hollow-face illusion)
2. Painted pupil → activates face processing network
3. Convexity prior → creates perception of mutual gaze regardless of actual viewing angle
4. No sensors needed because human perception does the "computation"

## Implementation Guide

### Prerequisites
- Understanding of perceptual neuroscience principles
- Basic design/fabrication capabilities
- Knowledge of HRI (Human-Robot Interaction) principles

### Design Parameters

#### Critical Geometric Constraints
```
Eye Socket Specifications:
- Concavity depth: Sufficient to trigger convexity prior
- Diameter: Proportional to face size
- Pupil placement: Must account for viewing angle range

Face Parameters:
- Overall proportions: Should match expected human face ratios
- Feature spacing: Consistent with facial geometry expectations
```

#### Interchangeable Eye Inserts
- **Parameterized system**: Allow customization for different applications
- **Material options**: Cardboard, 3D printed, molded plastic
- **Color variations**: Adapt to cultural/contextual requirements

### Boundary Conditions

The framework has defined conditions for success and failure:

#### Success Predicted
- **Developmental**: Typical adult visual perception
- **Geometric**: Viewing angles within normal face-to-face interaction range
- **Environmental**: Normal lighting conditions

#### Failure Predicted
- **Clinical**: Individuals with impaired face processing (e.g., prosopagnosia)
- **Developmental**: Very young children (< 12-18 months, before convexity prior develops)
- **Geometric**: Extreme viewing angles outside normal social interaction
- **Contextual**: When explicit depth cues override convexity prior

## Applications

### Primary Use Cases
1. **Educational Robotics**: Low-cost classroom robots for child-robot interaction studies
2. **Therapeutic Applications**: Affordable gaze-following for autism intervention
3. **Research Platforms**: Replicable, scalable HRI gaze studies
4. **Privacy-Sensitive Environments**: Settings where cameras are prohibited
5. **Developing World**: Resource-limited contexts requiring social robotics

### Scale Implications
If leveraged, **two decades of HRI gaze findings** become deliverable at population scale by eliminating cost barriers.

## Advantages Over Sensor-Based Approaches

| Aspect | Sensor-Based | Perceptual (This Framework) |
|--------|--------------|----------------------------|
| Cost | $30,000+ | < $1 |
| Privacy | Camera-based concerns | No data collection |
| Power | Requires electricity | No power needed |
| Computation | Complex algorithms | None |
| Maintenance | Sensor calibration | Minimal |
| Scalability | Limited by cost | Unlimited |

## Limitations

1. **Fixed Gaze**: Cannot dynamically track moving viewers (but perceived mutual gaze from any angle)
2. **Boundary Conditions**: Fails with certain clinical populations and extreme geometries
3. **Limited Feedback**: No true gaze tracking data for research analysis
4. **One-Way Interaction**: No closed-loop gaze contingency

## Related Concepts

- **Hollow-Face Illusion**: The classic perceptual phenomenon where concave masks appear convex
- **Predictive Processing**: Theoretical framework for understanding perception as prediction
- **Social Robotics**: Field focused on robots that interact with humans
- **Joint Attention**: Shared focus between individuals, critical for learning and social development

## Related Skills
- `brain-inspired-capture-evidence-driven`: Brain-inspired visual decoding
- `perception-neuroscience-framework-sensorless-gaze`: Perceptual frameworks for HRI
- `neuroscience-frontiers-2026`: Neuroscience research trends
- `neuroai-beyond-bridging-neuroscience-ai`: NeuroAI intersection

## References
- Kadem, M. (2026). Perception Is All You Need: A Neuroscience Framework for Low Cost Sensorless Gaze in HRI. arXiv:2604.09829
