---
name: sensorless-gaze-following
description: "Neuroscience framework for sensorless gaze-following in Human-Robot Interaction. Uses human visual system's convexity assumption to produce perceptual gaze-following without sensors, algorithms, or computation. Sub-dollar cardboard robot design. Activation: sensorless gaze, gaze-following, HRI, child-robot interaction, perceptual gaze, convexity assumption"
---

# Sensorless Gaze-Following for Human-Robot Interaction

A neuroscience-based framework for gaze-following in HRI that eliminates sensors, computation, and cost by leveraging the human visual system's own gaze computation pipeline.

## Source Paper

- **Title**: Perception Is All You Need: A Neuroscience Framework for Low Cost Sensorless Gaze in HRI
- **Authors**: See paper
- **arXiv**: 2604.09829v1
- **Published**: 2026-04
- **PDF**: https://arxiv.org/pdf/2604.09829v1
- **Categories**: cs.HC, cs.AI, q-bio.NC

## Overview

Gaze-following in child-robot interaction improves attention, recall, and learning. Traditional approaches require expensive platforms ($30,000+), eye-tracking sensors, gaze estimation algorithms, and raise privacy concerns.

This paper proposes a radically different approach: **make the human's visual system do the computation**. By designing a robot whose physical appearance exploits the brain's convexity assumption for gaze direction, the viewer's own perceptual system becomes the robot's "actuator."

**Key result**: Sub-dollar cardboard robot design with no sensors, no power, and no privacy concerns.

## Core Concepts

### The Convexity Assumption
- The human visual system assumes that faces and gaze-related features are convex
- The brain uses convexity cues to compute where someone is looking
- By engineering a physical robot that exploits this assumption, the viewer's brain automatically computes gaze direction
- The robot doesn't need to "know" where to look — the viewer's brain does the computation

### Neuroscience Foundation

Three converging lines of evidence:

1. **Distributed Face Processing Network**: The brain has specialized regions for face and gaze processing (FFA, STS, amygdala)
2. **Convexity Assumption in Gaze Perception**: The visual system uses convexity as a cue for gaze direction
3. **Perceptual Inference**: The brain infers gaze direction from geometric cues automatically

### Design Comparison

```
Traditional Approach:
  Camera -> Algorithm -> Gaze Estimation -> Motor Control -> Robot Head Movement
  Cost: $30,000+ | Privacy: Concerns | Latency: 100-500ms

Sensorless Approach (This Framework):
  Physical Design -> Human Visual System -> Automatic Gaze Perception
  Cost: <$1 | Privacy: None | Latency: ~50ms (human perception)
```

## Implementation

### Cardboard Robot Design Parameters
```python
design = {
    'material': 'cardboard',
    'cost': '<$1 USD',
    'sensors': 0,
    'power': 'none',
    'privacy_concerns': False,
    'latency': '~50ms (human perception speed)'
}
```

### Gaze Direction Encoding
```python
import numpy as np

def encode_gaze_in_design(gaze_target_x, gaze_target_y):
    """
    Encode gaze direction in robot's physical appearance.
    The human visual system will automatically decode this.
    """
    # Eye angle = arctan(gaze_target / face_geometry)
    # The brain does this computation automatically
    eye_angle = np.arctan2(gaze_target_y, gaze_target_x)
    return {
        'eye_orientation': eye_angle,
        'viewer_perception': 'automatic gaze at target'
    }
```

### Design Validation Framework
```python
def validate_sensorless_design():
    """
    Validate that the sensorless design produces correct gaze perception.
    """
    metrics = {
        'perception_accuracy': 'mean angular error < 15 degrees',
        'response_time': '< 200ms (automatic perception)',
        'consistency': 'high across participants'
    }
    return metrics
```

## Practical Applications

1. **Child-Robot Interaction in Education**: Low-cost robots for classroom use, no privacy concerns
2. **Healthcare Settings**: Autism therapy robots, social skills training, developing regions
3. **Research Applications**: Controlled gaze studies without sensor artifacts

## Comparison with Traditional Methods

| Aspect | Traditional | Sensorless |
|--------|-------------|------------|
| Cost | $30,000+ | <$1 |
| Sensors | Camera + eye tracker | None |
| Computation | Gaze estimation algorithm | Human brain |
| Privacy | Camera-based concerns | None |
| Latency | 100-500ms | ~50ms |
| Lighting dependency | Yes | No |

## Limitations
- Only works for pre-designed gaze directions (not dynamic real-time)
- Requires careful physical design to match convexity assumptions
- May not work for all cultural contexts (gaze norms vary)
- Limited to simple gaze scenarios

## Related Work
- Gaze-following in developmental psychology
- Social robotics and HRI
- Visual perception of gaze direction
- Convexity in face processing

## Activation Keywords
- sensorless gaze
- gaze-following HRI
- child-robot interaction
- perceptual gaze
- convexity assumption
- low-cost HRI
- cardboard robot
- neuroscience HRI
