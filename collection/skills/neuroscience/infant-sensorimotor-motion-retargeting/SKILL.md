---
name: infant-sensorimotor-motion-retargeting
description: "Framework for simulating infant first-person sensorimotor experience via motion retargeting from babies to humanoids. Reconstructs 3D infant pose from video and maps onto developmental robotics platforms (iCub, pyCub, EMFANT, MIMo). Activation: infant sensorimotor, motion retargeting, developmental robotics, humanoid infant simulation, sensorimotor experience, developmental neuroscience."
---

# Infant Sensorimotor Experience via Motion Retargeting

> A framework that reconstructs infant body configurations from single-video 3D pose estimation and retargets motion onto physical and virtual humanoid platforms to simulate multimodal sensorimotor experience.

## Metadata
- **Source**: arXiv:2604.27583
- **Authors**: Francisco M. López, Hoshinori Kanazawa, Ondrej Fiala, Yakov Balashov, Valentin Marcel, Lukas Rustler, Miles Lenz, Dongmin Kim, Yasuo Kuniyoshi, Jochen Triesch, Matej Hoffmann
- **Published**: 2026-04-30
- **Subjects**: Neurons and Cognition (q-bio.NC); Robotics (cs.RO)
- **Venue**: Submitted to IEEE ICDL

## Core Methodology

### Key Innovation
Bridges developmental neuroscience and robotics by extracting infant motion from video and replaying it on multiple humanoid embodiments to generate simulated multisensory streams. This provides a computational window into the infant's first-person sensorimotor experience.

### Technical Framework

#### 1. Video-Based Infant Pose Reconstruction
- **Input**: Single video of infant movement
- **Skeletal extraction**: Estimate infant body structure from video frames
- **3D pose estimation**: Full 3D joint positions reconstructed per frame
- **Temporal tracking**: Continuous motion sequence recovery

#### 2. Motion Retargeting to Embodiments
Maps reconstructed infant motion onto multiple developmental platforms:
- **Physical iCub robot**: Real humanoid platform with physical sensors
- **pyCub**: Virtual simulation of iCub
- **EMFANT**: Developmental robot simulator
- **MIMo**: Multimodal infant-like robot model

#### 3. Multimodal Sensorimotor Stream Generation
Replaying retargeted motions produces:
- **Proprioception**: Joint angles and muscle states
- **Touch**: Contact and tactile feedback
- **Vision**: First-person visual input

#### 4. Accuracy and Validation
- **Sub-centimeter accuracy** for best-matching embodiment
- **Multimodal analysis** of infant development patterns
- **Automated behavior annotation** enhancement

## Implementation Guide

### Prerequisites
- Video recordings of infant movement
- 3D pose estimation model adapted for infant body proportions
- Access to one or more developmental robot simulators (iCub/pyCub/EMFANT/MIMo)

### Pipeline Steps

```python
# Conceptual pipeline
1. video_capture = load_infant_video(path)
2. skeleton = estimate_infant_skeleton(video_capture)
3. pose_3d = reconstruct_3d_pose(video_capture, skeleton)
4. 
5. for embodiment in [iCub, pyCub, EMFANT, MIMo]:
6.     retargeted = map_motion(pose_3d, embodiment.kinematics)
7.     sensory_stream = replay(retargeted, embodiment)
8.     # proprioception + touch + vision streams
9.     analyze_multimodal(sensory_stream)
```

### Platform Selection Criteria
- **Kinematic similarity**: Match infant body proportions to robot embodiment
- **Sensor availability**: Choose platform with required sensor modalities
- **Simulation fidelity**: Trade-off between physical accuracy and computation speed

## Applications
- **Developmental neuroscience**: Understanding infant sensorimotor learning
- **Neurodevelopmental disorder detection**: Early identification through motion analysis
- **Robotics**: Infant-inspired robot learning and development
- **Automated behavior annotation**: Enhanced labeling of infant behaviors
- **Computational developmental psychology**: Testing theories of embodied cognition

## Pitfalls
- **Infant-adapted pose estimation**: Standard human pose models don't fit infant body proportions
- **Embodiment mismatch**: Motion transfer accuracy varies across robot platforms
- **Single-video limitation**: Reconstruction quality depends on video viewpoint and quality
- **Sensor simulation fidelity**: Simulated sensors may not match real infant sensory experience

## Related Skills
- `neural-brain-framework`: Neuroscience-inspired embodied AI
- `sensorless-gaze-following-hri`: Neuroscience-inspired HRI framework
- `neurodevelopmental-4d-diffusion`: 4D diffusion for neurodevelopmental modeling
- `agentic-behavioral-modeling`: Agentic behavioral modeling framework
