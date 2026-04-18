---
name: perception-neuroscience-framework-sensorless-gaze
description: Neuroscience framework for sensorless gaze-following in Human-Robot Interaction (HRI). Grounds robot attention in biological visual mechanisms (retinotopic maps, dorsal/ventral streams, gaze cells, head-direction cells) without requiring gaze sensors. Triggers: sensorless gaze, robot gaze-following, HRI attention, visual attention robotics, neuroscience HRI, gaze prediction, biological vision robotics, retinotopic robotics.
---

# Sensorless Gaze-Following in HRI: A Neuroscience Framework

## Overview

A neuroscience-grounded framework enabling robots to infer and follow human gaze without dedicated gaze-tracking sensors. The system leverages biological visual processing principles — retinotopic mapping, dorsal/ventral stream processing, and neural gaze cell models — to predict where humans are looking based on head pose and environmental context.

**Source Paper**: "Perception All You Need? Neuroscience Framework for Sensorless Gaze-Following in HRI" (arXiv:2604.10699, 2026-04-12)

## Biological Grounding

### Visual Processing Pathways

| Pathway | Function | Robot Equivalent |
|---------|----------|-----------------|
| Dorsal stream ("where") | Spatial attention, motion | Head pose → spatial map |
| Ventral stream ("what") | Object recognition | Object detection pipeline |
| Retinotopic mapping | Visual field organization | Attention heatmap generation |
| Gaze cells (STS) | Gaze direction encoding | Head pose → gaze vector |
| Head-direction cells | Orientation encoding | Robot orientation tracking |

### Core Mechanism

1. **Input**: RGB camera → head pose estimation
2. **Retinotopic projection**: Map head direction to visual field coordinates
3. **Ventral stream integration**: Combine with detected objects in scene
4. **Attention heatmap**: Generate probability distribution over possible gaze targets
5. **Robot response**: Orient robot attention toward predicted target

## Key Contributions

1. **Sensorless approach**: No eye tracker or gaze camera needed
2. **Neuroscience-grounded**: Direct mapping from biological mechanisms
3. **Computational model**: Formal retinotopic projection functions
4. **HRI application**: Natural joint attention in human-robot interaction
5. **Testable predictions**: Framework generates falsifiable hypotheses

## Implementation Pattern

```python
import numpy as np

class SensorlessGazeFollower:
    """Neuroscience-grounded sensorless gaze-following for HRI."""
    
    def __init__(self, fov=(60, 40), resolution=(32, 32)):
        self.retinotopic_map = self._build_retinotopic_map(fov, resolution)
        self.gaze_vector = None
        self.attention_heatmap = None
    
    def _build_retinotopic_map(self, fov, resolution):
        """Build retinotopic coordinate mapping."""
        # Cortical magnification: foveal over-representation
        x = np.linspace(-fov[0]/2, fov[0]/2, resolution[0])
        y = np.linspace(-fov[1]/2, fov[1]/2, resolution[1])
        return np.meshgrid(x, y)
    
    def estimate_gaze(self, head_pose, scene_objects):
        """Predict gaze target from head pose and scene."""
        # Dorsal stream: spatial projection
        gaze_direction = self._project_head_to_gaze(head_pose)
        
        # Ventral stream: object-based attention
        object_salience = self._compute_object_salience(scene_objects, gaze_direction)
        
        # Retinotopic integration
        self.attention_heatmap = self._integrate_retinotopic(
            gaze_direction, object_salience
        )
        
        return self.attention_heatmap
    
    def _project_head_to_gaze(self, head_pose):
        """Map head pose to gaze direction (STS gaze cell model)."""
        # Gaze = head_pose + eye_offset (learned prior)
        return head_pose
    
    def _compute_object_salience(self, objects, gaze_dir):
        """Ventral stream: object relevance to gaze direction."""
        # Objects within gaze cone get higher salience
        pass
    
    def _integrate_retinotopic(self, gaze_dir, salience):
        """Combine dorsal and ventral streams in retinotopic space."""
        # Weighted combination
        pass
```

## Activation Keywords

- sensorless gaze, gaze-following, HRI attention, visual attention
- retinotopic mapping, dorsal ventral stream, neuroscience robotics
- joint attention, human-robot interaction, gaze prediction
- 无传感器注视跟随, 机器人注意力, 神经科学HRI

## Applications

- Natural human-robot interaction
- Assistive robotics for social engagement
- Autism therapy robots
- Attention-aware service robots

## References

- Paper: arXiv:2604.10699 (2026-04-12)
- Related: gaze cell models in superior temporal sulcus (STS)
- Related: head-direction cell literature
