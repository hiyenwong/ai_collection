---
name: sumo-whole-body-locomanipulation
description: "End-Effector Stability-Oriented Mobile Manipulation (EMMa) for tracked rescue robots. Ensures reachability, safety, and stable end-effector manipulation during autonomous rescue operations."
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [mobile-manipulation, rescue-robotics, end-effector-stability, tracked-robots, whole-body-control, locomotion]
    source_paper: "EMMa: End-Effector Stability-Oriented Mobile Manipulation for Tracked Rescue Robots (arXiv:2604.08292v1)"
    authors: "Yifei Wang, Hao Zhang, Jidong Huang, Shuohang Fang, Haoyao Chen"
    published: "2026-04-09"
    category: "robotics"
---

# EMMa: End-Effector Stability-Oriented Mobile Manipulation

## Overview

This skill implements the EMMa (End-Effector Stability-Oriented Mobile Manipulation) framework for tracked rescue robots. The approach addresses the challenge of maintaining stable end-effector manipulation while ensuring robot motion reachability and safety during autonomous rescue missions.

## Core Concepts

### 1. Whole-Body Loco-Manipulation
- **Integration**: Combining locomotion and manipulation into unified control
- **Challenge**: Balancing mobility with manipulation stability
- **Solution**: Coordinated whole-body control framework

### 2. End-Effector Stability
- **Metric**: Position/orientation accuracy under disturbances
- **Factors**: Base motion, terrain unevenness, payload variations
- **Control**: Active stabilization through arm configuration

### 3. Tracked Robot Considerations
- **Mobility**: Traversing rough terrain
- **Constraints**: Non-holonomic motion, track-ground interaction
- **Stability**: Center of mass management on slopes

## Implementation Pattern

```python
import numpy as np
from typing import Tuple, Optional
from dataclasses import dataclass

@dataclass
class RobotState:
    """Tracked robot state"""
    base_pose: np.ndarray      # [x, y, θ]
    joint_positions: np.ndarray
    joint_velocities: np.ndarray
    
@dataclass
class EndEffectorTarget:
    """End-effector target"""
    position: np.ndarray
    orientation: np.ndarray
    stability_requirement: float

class EMMaController:
    """
    End-Effector Stability-Oriented Mobile Manipulation Controller
    """
    
    def __init__(
        self,
        robot_model,
        stability_weight: float = 1.0,
        manipulation_weight: float = 1.0,
        locomotion_weight: float = 0.5
    ):
        self.robot = robot_model
        self.w_stability = stability_weight
        self.w_manip = manipulation_weight
        self.w_locomotion = locomotion_weight
    
    def compute_control(
        self,
        state: RobotState,
        target: EndEffectorTarget,
        terrain_info: Optional[dict] = None
    ) -> Tuple[np.ndarray, np.ndarray]:
        """Compute whole-body control commands"""
        # Solve optimization for coordinated control
        base_vel, joint_torques = self._solve_wbic(state, target)
        return base_vel, joint_torques
    
    def evaluate_stability(
        self,
        state: RobotState,
        target: EndEffectorTarget
    ) -> float:
        """Evaluate end-effector stability metric"""
        p_ee = self.robot.forward_kinematics(state)
        position_error = np.linalg.norm(p_ee - target.position)
        return position_error
```

## Key Insights

1. **Stability-First Design**: Prioritizing end-effector stability enables reliable manipulation during motion

2. **Whole-Body Coordination**: Integrated control of base and arm achieves capabilities beyond separate control

3. **Terrain Adaptation**: Active stability compensation for uneven terrain

4. **Rescue-Specific**: Designed for dynamic, unstructured rescue environments

## Applications

- Search and rescue operations
- Hazardous environment exploration
- Disaster response
- Industrial inspection

## References

- Original Paper: EMMa: End-Effector Stability-Oriented Mobile Manipulation for Tracked Rescue Robots
- arXiv: https://arxiv.org/abs/2604.08292v1
- Authors: Yifei Wang, Hao Zhang, Jidong Huang, Shuohang Fang, Haoyao Chen
- Published: 2026-04-09
