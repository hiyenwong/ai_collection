---
name: sensorless-gaze-following-hri
description: Neuroscience-inspired framework for low-cost sensorless gaze following in Human-Robot Interaction. Uses computational models of human gaze perception to estimate where humans are looking without expensive eye-tracking hardware. Trigger words: sensorless gaze, gaze following, human-robot interaction, HRI, gaze estimation, neuroscience gaze, low-cost gaze tracking.
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    source_paper: "Perception Is All You Need: A Neuroscience Framework for Low Cost Sensorless Gaze in HRI (arXiv:2604.09829)"
    citations: 0
    published: "2026-04-10"
    tags: [hri, gaze-following, sensorless, neuroscience, robotics, perception, human-robot-interaction]
---

# Sensorless Gaze Following for HRI

## Overview

This skill implements a neuroscience-inspired framework for gaze following in Human-Robot Interaction (HRI) without requiring expensive eye-tracking hardware. By modeling human gaze perception mechanisms, robots can estimate where humans are looking using only standard cameras.

## Core Principles

1. **Head pose + scene context** can predict gaze direction with surprising accuracy
2. **Human gaze perception** relies on integration of multiple visual cues
3. **Neuroscience models** of gaze processing can be computationally implemented

## Implementation

```python
import cv2
import numpy as np

class SensorlessGazeEstimator:
    def __init__(self):
        self.head_pose_model = self.load_head_pose_model()
        
    def estimate_gaze(self, frame, face_bbox):
        head_pose = self.head_pose_model.predict(frame, face_bbox)
        gaze_vector = self.compute_gaze_from_head_pose(head_pose)
        gaze_target = self.map_gaze_to_scene(gaze_vector, frame)
        return gaze_target
    
    def compute_gaze_from_head_pose(self, head_pose):
        eye_offset = self.neuroscience_gaze_model(head_pose)
        return head_pose + eye_offset
```

## Applications

- Low-cost HRI systems
- Assistive robotics
- Social robots
- Behavioral analysis

## Activation Keywords

sensorless gaze, gaze following, human-robot interaction, HRI, gaze estimation, neuroscience gaze, low-cost gaze tracking
