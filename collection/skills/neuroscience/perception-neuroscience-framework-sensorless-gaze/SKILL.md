---
name: perception-neuroscience-framework-sensorless-gaze
description: >
  Neuroscience framework for sensorless gaze-following in HRI. Exploits the brain's convexity prior 
  (hollow-face illusion) to create perceived mutual gaze without sensors, power, or computation. 
  Grounded in STS gaze processing, convexity prior, and predictive processing hierarchy.
  Use when: human-robot interaction, gaze-following design, low-cost robotics, perceptual illusions 
  in HRI, neuroscience-inspired design, child-robot interaction.
  Trigger: sensorless gaze, hollow-face illusion, gaze-following HRI, convexity prior, 
  low-cost robot design, perception-based interaction, 无传感器凝视, 空心脸错觉.
version: 1.0.0
author: Research Synthesis (arXiv:2604.09829)
license: MIT
metadata:
  hermes:
    tags: [HRI, gaze-following, neuroscience, convexity-illusion, low-cost-robotics, perception]
    source_paper: "Perception Is All You Need: A Neuroscience Framework for Low Cost Sensorless Gaze in HRI (arXiv:2604.09829)"
---

# Sensorless Gaze-Following via Neuroscience Framework

## Overview

A sub-dollar cardboard robot design that exploits the human brain's own gaze computation pipeline 
in reverse — making the viewer's perceptual system the robot's "actuator" with zero sensors, 
zero power, zero computation, and zero privacy concerns.

## Neuroscience Foundation

Three converging mechanisms explain why concave eye sockets with painted pupils produce 
perceived mutual gaze from any viewing angle:

### 1. Superior Temporal Sulcus (STS) Gaze Processing
- Distributed face processing network computes gaze direction
- STS is specialized for interpreting eye direction
- Brain assumes eyes are convex (protruding outward)

### 2. High-Precision Convexity Prior
- Brain strongly expects faces to be convex
- Causes the "hollow-face illusion" — concave faces perceived as convex
- When face appears convex, painted pupils appear to track viewer

### 3. Predictive Processing Hierarchy
- Top-down face knowledge overrides bottom-up depth signals
- Prior expectation of convex face > actual concave geometry
- Results in perceived mutual gaze from any angle

## Design Principle

```
Concave Eye Socket + Painted Pupil
         ↓
Viewer's Brain Applies Convexity Prior
         ↓
Brain Perceives Convex Face with Forward-Looking Eyes
         ↓
Perception: "The robot is looking at me"
         ↓
Mutual gaze achieved — no sensors, no code, no power
```

## Design Constraints (from Perceptual Science)

| Parameter | Constraint | Rationale |
|-----------|------------|-----------|
| Socket depth | Sufficient concavity | Strong hollow-face illusion |
| Pupil placement | Center of concave region | Appears to track from all angles |
| Lighting | Even illumination | Avoids depth cues that break illusion |
| Viewing distance | Typical interaction range | Within illusion effectiveness zone |

## Boundary Conditions

### Will Succeed
- Typical child-adult interaction distances
- Normal lighting conditions
- Neurotypical observers
- Standard viewing angles

### May Fail
- Very young children (developing face processing)
- Clinical populations with face processing differences
- Extreme viewing angles (geometric limits)
- Strong directional lighting (reveals concavity)

## Applications
- Scalable child-robot interaction programs
- Educational robotics at population scale
- Low-cost social robotics research
- Privacy-sensitive environments
- Resource-limited settings

## Implementation Template

```python
# Design parameters (from paper)
GAZE_DESIGN = {
    "socket_depth": "concave, ~2-3cm depth",
    "pupil_diameter": "1-2cm, centered in socket",
    "face_width": "child-appropriate scale (~15cm)",
    "material": "cardboard or 3D printed",
    "cost": "< $1 USD",
    "sensors_required": False,
    "power_required": False,
    "privacy_risk": "None"
}
```

## Activation Keywords
- sensorless gaze, hollow-face illusion, gaze-following HRI
- convexity prior, low-cost robotics, neuroscience design
- 无传感器凝视, 空心脸错觉, 凝视跟随

## References
- Mason Kadem. "Perception Is All You Need: A Neuroscience Framework for Low Cost Sensorless Gaze 
  in HRI." arXiv:2604.09829
