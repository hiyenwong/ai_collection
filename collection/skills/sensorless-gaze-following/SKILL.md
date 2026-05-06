---
name: sensorless-gaze-following
description: Neuroscience framework for sensorless gaze-following in Human-Robot Interaction (HRI). Uses brain-inspired prediction mechanisms to estimate gaze targets without eye-tracking hardware.
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [neuroscience, gaze-following, hri, brain-inspired, robotics, social-cognition]
    source_paper: "Perception Is All You Need? Neuroscience Framework for Sensorless Gaze-Following in HRI (arXiv:2601.06429)"
---

# Sensorless Gaze-Following in Human-Robot Interaction

## Overview

This framework leverages neuroscience insights about human gaze-following behavior to enable robots to estimate human gaze targets **without requiring eye-tracking hardware**. By understanding how the human brain predicts gaze direction from head pose, body orientation, and contextual cues, robots can achieve natural social interaction through sensorless gaze estimation.

## Key Insights

1. **Brain-Inspired Prediction**: Human gaze-following relies on predictive mechanisms in the superior temporal sulcus (STS) and intraparietal sulcus (IPS), which can be computationally modeled
2. **Multi-Modal Integration**: Gaze estimation integrates head pose, body orientation, scene context, and social priors — not just eye direction
3. **Context-Aware Attention**: The brain uses scene semantics and task context to disambiguate gaze targets in cluttered environments
4. **Social Cognition**: Joint attention emerges from shared spatial representations and intention modeling

## Core Framework

```
┌──────────────────────────────────────────────────┐
│           Sensorless Gaze Estimator              │
├──────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌──────────────────────┐      │
│  │  Head Pose  │  │  Body Orientation    │      │
│  │  Encoder    │  │  Encoder             │      │
│  └──────┬──────┘  └──────────┬───────────┘      │
│         │                   │                   │
│  ┌──────▼───────────────────▼──────────────┐    │
│  │       STS-Inspired Fusion Layer         │    │
│  │  (multi-modal attention integration)    │    │
│  └──────────────────┬──────────────────────┘    │
│                     │                           │
│  ┌──────────────────▼──────────────────────┐    │
│  │       IPS-Inspired Spatial Mapping      │    │
│  │  (gaze vector → scene target)           │    │
│  └──────────────────┬──────────────────────┘    │
│                     │                           │
│  ┌──────────────────▼──────────────────────┐    │
│  │     Context & Social Prior Modulator    │    │
│  └──────────────────┬──────────────────────┘    │
│                     │                           │
│  ┌──────────────────▼──────────────────────┐    │
│  │         Gaze Target Prediction          │    │
│  └─────────────────────────────────────────┘    │
└──────────────────────────────────────────────────┘
```

## Implementation Pattern

```python
import numpy as np
from dataclasses import dataclass
from typing import Optional

@dataclass
class GazeEstimate:
    """Gaze target estimation result."""
    target_position: np.ndarray  # 3D coordinates of estimated gaze target
    confidence: float
    target_object: Optional[str]  # Semantic label of target object
    uncertainty_cone: float  # Angular uncertainty in degrees

class SensorlessGazeEstimator:
    """
    Neuroscience-inspired sensorless gaze-following system.
    
    Estimates human gaze targets using:
    - Head pose and body orientation (visual cues)
    - Scene context and object semantics
    - Social interaction priors
    """
    
    def __init__(self, n_objects: int = 10):
        self.n_objects = n_objects
        
        # STS-inspired: multi-modal fusion weights
        self.head_pose_weight = 0.5
        self.body_weight = 0.3
        self.context_weight = 0.2
        
        # IPS-inspired: spatial attention map
        self.attention_map = np.zeros((64, 64))
        
        # Social priors: object salience scores
        self.object_salience = np.ones(n_objects) / n_objects
    
    def estimate_gaze(
        self,
        head_pose: np.ndarray,  # [yaw, pitch, roll]
        body_orientation: np.ndarray,  # [yaw, pitch]
        scene_objects: list,  # [(position, semantic_label)]
        social_context: dict = None
    ) -> GazeEstimate:
        """Estimate gaze target from visual cues and context."""
        
        # 1. STS-inspired: compute gaze direction from head + body
        gaze_direction = self._fuse_multimodal_cues(
            head_pose, body_orientation
        )
        
        # 2. IPS-inspired: project gaze onto scene objects
        object_scores = self._spatial_attention(
            gaze_direction, scene_objects
        )
        
        # 3. Context modulation: apply social priors
        if social_context:
            object_scores = self._apply_social_priors(
                object_scores, scene_objects, social_context
            )
        
        # 4. Select target with highest combined score
        target_idx = np.argmax(object_scores)
        confidence = self._compute_confidence(object_scores)
        
        return GazeEstimate(
            target_position=scene_objects[target_idx][0],
            target_object=scene_objects[target_idx][1],
            confidence=confidence,
            uncertainty_cone=self._compute_uncertainty(object_scores)
        )
    
    def _fuse_multimodal_cues(
        self,
        head_pose: np.ndarray,
        body_orientation: np.ndarray
    ) -> np.ndarray:
        """STS-inspired multi-modal fusion of visual cues."""
        # Head pose is primary cue for gaze direction
        head_direction = np.array([
            np.cos(head_pose[0]) * np.cos(head_pose[1]),
            np.sin(head_pose[0]) * np.cos(head_pose[1]),
            np.sin(head_pose[1])
        ])
        
        # Body orientation provides contextual support
        body_direction = np.array([
            np.cos(body_orientation[0]),
            np.sin(body_orientation[0]),
            0.0
        ])
        
        # Weighted fusion (head pose dominates)
        fused = (self.head_pose_weight * head_direction +
                 self.body_weight * body_direction)
        fused /= np.linalg.norm(fused)
        
        return fused
    
    def _spatial_attention(
        self,
        gaze_direction: np.ndarray,
        scene_objects: list
    ) -> np.ndarray:
        """IPS-inspired spatial attention scoring of objects."""
        scores = np.zeros(len(scene_objects))
        for i, (position, _) in enumerate(scene_objects):
            # Compute angular alignment with gaze direction
            obj_dir = position / np.linalg.norm(position)
            alignment = np.dot(gaze_direction, obj_dir)
            scores[i] = np.clip(alignment, 0, 1)
        return scores
    
    def _apply_social_priors(
        self,
        scores: np.ndarray,
        scene_objects: list,
        context: dict
    ) -> np.ndarray:
        """Modulate scores with social interaction priors."""
        task_relevance = context.get('task_relevance', {})
        for i, (_, label) in enumerate(scene_objects):
            if label in task_relevance:
                scores[i] += task_relevance[label] * self.context_weight
        return scores / scores.sum()
    
    def _compute_confidence(self, scores: np.ndarray) -> float:
        """Compute confidence from score distribution entropy."""
        normalized = scores / scores.sum()
        entropy = -np.sum(normalized * np.log(normalized + 1e-10))
        max_entropy = np.log(len(scores))
        return 1.0 - (entropy / max_entropy) if max_entropy > 0 else 0.0
    
    def _compute_uncertainty(self, scores: np.ndarray) -> float:
        """Estimate angular uncertainty from score spread."""
        normalized = scores / scores.sum()
        spread = np.std(normalized)
        return np.clip(90 * (1 - spread * 2), 5, 45)
```

## Applications

1. **Human-Robot Collaboration**: Robots that naturally follow human gaze during joint tasks
2. **Assistive Robotics**: Understanding user intent without wearable sensors
3. **Social Robotics**: Natural eye contact and joint attention behaviors
4. **Smart Environments**: Gaze-aware interactive displays and systems
5. **Autonomous Vehicles**: Predicting pedestrian attention and intent

## Key Parameters

| Parameter | Description | Typical Range |
|-----------|-------------|---------------|
| `head_pose_weight` | Importance of head pose | 0.4 - 0.7 |
| `body_weight` | Importance of body orientation | 0.2 - 0.4 |
| `context_weight` | Importance of social context | 0.1 - 0.3 |
| `attention_resolution` | Spatial attention map size | 32x32 - 128x128 |

## Activation Keywords

- sensorless gaze following
- gaze estimation
- human-robot interaction
- joint attention
- brain-inspired robotics
- social cognition
- head pose gaze
- 无传感器注视跟踪
- 人机交互注视

## References

- **Original Paper**: Perception Is All You Need? Neuroscience Framework for Sensorless Gaze-Following in HRI. arXiv:2601.06429 (2026)
- **Related Skills**: [[neural-brain-framework]], [[context-selective-multimodal-memory]], [[ember-hybrid-snn-llm-architecture]]

## Limitations

- Accuracy degrades with occluded head/face views
- Requires accurate head pose estimation
- Social priors need domain-specific calibration
- Performance depends on scene understanding quality
