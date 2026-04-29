---
name: angle-based-rigidity-multi-robot
description: "Angle-based localization and rigidity maintenance control for multi-robot networks under sensing constraints. Establishes equivalence between angle rigidity and bearing rigidity with distributed control law. Activation: multi-robot formation, rigidity control, angle-based localization, bearing rigidity."
---

# Angle-based Localization and Rigidity Maintenance Control

## Overview

A novel approach to multi-robot formation control using angle measurements instead of bearing measurements. Establishes the first equivalence between angle rigidity and bearing rigidity under directed sensing graphs and body-frame measurements.

## Core Methodology

### 1. Problem Background

**Multi-Robot Formation Control Challenge**:
- Robots must maintain geometric formation while moving
- Limited sensing capabilities (direction only, no distance)
- Body-frame measurements (not global coordinates)
- Directed sensing graphs (not all-to-all communication)

**Traditional Approach**: Bearing-based rigidity
- **Limitation**: Requires precise bearing measurements in global frame
- **Practical Issue**: Expensive sensors, calibration overhead

### 2. Key Innovation: Angle Rigidity

**Angle vs Bearing**:
- **Bearing**: Direction vector from one robot to another
- **Angle**: Relative angle between two neighbors (simpler measurement)

**Equivalence Theorem**:
```
Angle rigidity ⟺ Bearing rigidity
(for directed graphs with body-frame measurements)
```

**Significance**: Enables simpler sensor requirements while maintaining rigidity guarantees

### 3. Rigidity Theory

**Graph Rigidity**: A framework is rigid if it cannot be continuously deformed while preserving edge constraints.

**Types of Rigidity**:

| Type | Constraint | Measurement |
|------|-----------|-------------|
| Distance Rigidity | Fixed edge lengths | Distance sensors |
| Bearing Rigidity | Fixed bearings | Direction sensors |
| Angle Rigidity | Fixed angles | Angle sensors (simpler) |

### 4. Angle Rigidity Framework

**Definition**: A multi-robot framework is angle rigid if the shape is uniquely determined by angle constraints between robots.

**Mathematical Formulation**:

```python
import numpy as np

class AngleRigidityFramework:
    """
    Angle rigidity framework for multi-robot networks
    """
    
    def __init__(self, positions, angle_constraints):
        """
        Args:
            positions: Nx2 array of robot positions
            angle_constraints: List of (i, j, k, angle) tuples
                - angle at robot j between neighbors i and k
        """
        self.positions = positions
        self.n_robots = len(positions)
        self.angle_constraints = angle_constraints
    
    def rigidity_matrix(self):
        """
        Compute angle rigidity matrix
        
        The rigidity matrix encodes how position changes affect angle constraints.
        Rank deficiency indicates flexible motions.
        """
        n_constraints = len(self.angle_constraints)
        n_variables = 2 * self.n_robots  # 2D positions
        
        R = np.zeros((n_constraints, n_variables))
        
        for idx, (i, j, k, target_angle) in enumerate(self.angle_constraints):
            # Partial derivatives of angle constraint
            # w.r.t. positions of robots i, j, k
            row = self._angle_constraint_gradient(i, j, k)
            R[idx, :] = row
        
        return R
    
    def is_rigid(self):
        """Check if framework is angle rigid"""
        R = self.rigidity_matrix()
        rank = np.linalg.matrix_rank(R)
        
        # In 2D: rigid if rank = 2n - 3
        # (allows translation and rotation, prevents deformation)
        return rank == 2 * self.n_robots - 3
```

### 5. Distributed Control Law

**Objective**: Maintain rigidity while robots move

**Control Strategy**:
```
For each robot i:
  1. Measure angles to neighbors
  2. Compute deviation from desired angles
  3. Apply corrective velocity
```

**Mathematical Form**:
```python
def distributed_rigidity_control(robot_id, positions, desired_angles):
    """
    Distributed control law for angle rigidity maintenance
    
    Args:
        robot_id: ID of current robot
        positions: Current positions of all robots
        desired_angles: Dict of {(i,j,k): angle} constraints
    
    Returns:
        control_input: 2D velocity for robot_id
    """
    control_input = np.zeros(2)
    
    # Find all angle constraints involving this robot
    for (i, j, k), target_angle in desired_angles.items():
        if j == robot_id:  # Robot is the vertex of the angle
            # Current angle
            current_angle = compute_angle(positions[i], 
                                          positions[j], 
                                          positions[k])
            
            # Angle error
            error = target_angle - current_angle
            
            # Gradient of angle w.r.t. position of robot j
            gradient = angle_gradient(positions[i], 
                                     positions[j], 
                                     positions[k])
            
            # Proportional control
            control_input += -k_p * error * gradient
    
    return control_input
```

### 6. Stability Analysis

**Theorem**: The distributed control law asymptotically stabilizes the desired formation if:
1. The desired framework is angle rigid
2. The sensing graph is connected
3. Control gains are sufficiently small

**Proof Sketch**:
- Use Lyapunov function based on angle errors
- Show rigidity matrix guarantees local stability
- Global stability via invariant set analysis

## Implementation Steps

### Step 1: Define Formation

```python
# Define 4-robot square formation
positions = np.array([
    [0, 0],    # Robot 0
    [1, 0],    # Robot 1
    [1, 1],    # Robot 2
    [0, 1]     # Robot 3
])

# Angle constraints (at vertex, between neighbors)
angle_constraints = [
    (3, 0, 1, np.pi/2),  # Angle at robot 0 between 3 and 1
    (0, 1, 2, np.pi/2),  # Angle at robot 1 between 0 and 2
    (1, 2, 3, np.pi/2),  # Angle at robot 2 between 1 and 3
    (2, 3, 0, np.pi/2),  # Angle at robot 3 between 2 and 0
]

framework = AngleRigidityFramework(positions, angle_constraints)
print(f"Is rigid: {framework.is_rigid()}")
```

### Step 2: Simulation

```python
def simulate_formation_control(n_robots, duration, dt):
    """
    Simulate multi-robot formation with angle rigidity control
    """
    # Initialize positions (slightly perturbed)
    positions = initialize_formation(n_robots) + noise
    
    # Define desired angles
    desired_angles = compute_desired_angles(n_robots)
    
    trajectory = [positions.copy()]
    
    for t in range(int(duration / dt)):
        # Each robot computes its control locally
        velocities = np.zeros((n_robots, 2))
        
        for i in range(n_robots):
            velocities[i] = distributed_rigidity_control(
                i, positions, desired_angles
            )
        
        # Update positions
        positions += velocities * dt
        trajectory.append(positions.copy())
    
    return np.array(trajectory)
```

### Step 3: Deploy to Robots

```python
class RobotController:
    """
    On-robot implementation of angle rigidity control
    """
    
    def __init__(self, robot_id, desired_angles):
        self.robot_id = robot_id
        self.desired_angles = desired_angles
        self.k_p = 0.5  # Proportional gain
    
    def update(self):
        """Main control loop"""
        # Measure angles to neighbors (local sensing)
        measured_angles = self.measure_neighbor_angles()
        
        # Compute control
        velocity = np.zeros(2)
        for (i, j, k), target in self.desired_angles.items():
            if j == self.robot_id:
                error = target - measured_angles.get((i, k), 0)
                velocity += self.compute_gradient(i, k) * error
        
        # Apply velocity
        self.set_velocity(velocity * self.k_p)
```

## Activation Keywords

- multi-robot formation control
- angle rigidity
- bearing rigidity
- distributed robot control
- formation maintenance
- rigidity theory
- angle-based localization

## Applications

1. **Warehouse Robots**: Formation navigation in constrained spaces
2. **Drone Swarms**: Coordinated flight with minimal sensing
3. **Underwater Vehicles**: Formation control with limited visibility
4. **Search and Rescue**: Robot team coordination

## Advantages

- **Simpler Sensors**: Angle sensors vs bearing sensors
- **Distributed**: No central coordination needed
- **Scalable**: Handles varying team sizes
- **Robust**: Maintains formation under perturbations

## Reference

- **Paper**: Angle-based Localization and Rigidity Maintenance Control for Multi-Robot Networks
- **Authors**: J. Francisco Presenza, Leonardo J. Colombo, Juan I. Giribet et al.
- **arXiv**: 2604.11754 (2026-04-13)
- **Category**: eess.SY (Systems and Control)

## Related Skills

- distributed-systems
- control-systems
- multi-agent-systems
- robotics

## Notes

- Works with directed sensing graphs
- Body-frame measurements (no global coordinates needed)
- First equivalence proof between angle and bearing rigidity
