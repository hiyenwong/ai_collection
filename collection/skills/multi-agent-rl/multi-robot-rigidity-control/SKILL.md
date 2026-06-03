---
name: multi-robot-rigidity-control
description: "Angle-based localization and rigidity maintenance control for multi-robot networks under sensing constraints. Establishes equivalence between angle rigidity and bearing rigidity with directed sensing graphs and body-frame bearing measurements. Use for: multi-robot formation control, angle-based localization, rigidity maintenance, bearing rigidity analysis, decentralized robot control. Activation: multi-robot rigidity, angle-based localization, bearing rigidity, formation control, rigidity maintenance."
---

# Multi-Robot Rigidity Control

Angle-based localization and rigidity maintenance control for multi-robot networks under sensing constraints in 2D and 3D space.

## Overview

This framework provides:
- First equivalence between angle rigidity and bearing rigidity for directed sensing graphs
- Distributed angle-based localization scheme
- Angle rigidity eigenvalue metric for rigidity quantification
- Decentralized gradient-based controller for mission execution with rigidity maintenance

## Core Concepts

### Rigidity Types

```
Angle Rigidity ↔ Bearing Rigidity
    ↓                    ↓
Angle measurements    Bearing measurements
between edges         from body frames
```

### Key Equivalence (Theorem)

A framework in SE(d) is **infinitesimally bearing rigid** if and only if:
1. It is **infinitesimally angle rigid**
2. Each robot obtains at least **d-1 bearing measurements** (d ∈ {2, 3})

## Mathematical Framework

### Angle Rigidity Matrix

```
R_angle = [∂cos(θ)/∂p_i] ∈ ℝ^(m×dn)

Where:
- θ: inter-edge angles
- p_i: robot positions
- m: number of angles
- n: number of robots
- d: dimension (2 or 3)
```

### Bearing Rigidity Matrix

```
R_bearing = [∂(b_ij)/∂p_i] ∈ ℝ^(mn×dn)

Where b_ij is the unit vector from robot i to j
```

### Angle Rigidity Eigenvalue

```
λ_rigidity = smallest non-zero eigenvalue of R_angle^T R_angle

Interpretation:
- λ_rigidity > 0: framework is rigid
- Larger λ: more rigid (resistant to deformation)
```

## Algorithms

### Localization Algorithm

```python
def angle_based_localization(robot, neighbors):
    """
    Distributed localization using angle measurements.
    Requires infinitesimal angle rigidity.
    """
    # Get local angle measurements
    angles = robot.measure_angles(neighbors)
    
    # Estimate relative positions
    positions = triangulate_from_angles(angles, neighbor_positions)
    
    # Update local position estimate
    robot.position_estimate = kalman_filter_update(positions)
    
    return robot.position_estimate
```

### Rigidity Maintenance Controller

```python
def rigidity_maintenance_control(robot, mission_command, λ_min):
    """
    Execute mission while maintaining minimum rigidity.
    
    Args:
        robot: Current robot state
        mission_command: Desired motion command
        λ_min: Minimum acceptable rigidity eigenvalue
    """
    # Compute current rigidity eigenvalue
    λ_current = compute_rigidity_eigenvalue(robot, neighbors)
    
    if λ_current < λ_min:
        # Rigidity is too low - prioritize maintenance
        control = gradient_ascent_rigidity(robot)
    else:
        # Sufficient rigidity - execute mission
        control = mission_command + rigidity_preservation_term(robot)
    
    return control
```

## Implementation

### Formation Control

```python
class MultiRobotRigidityController:
    def __init__(self, n_robots, dimension, desired_rigidity):
        self.n = n_robots
        self.d = dimension
        self.λ_desired = desired_rigidity
        self.robots = [Robot(dimension) for _ in range(n_robots)]
    
    def check_rigidity(self):
        """Check if current formation is rigid."""
        R = self.construct_rigidity_matrix()
        λ = smallest_nonzero_eigenvalue(R.T @ R)
        return λ > self.λ_desired
    
    def compute_control(self, robot_id, mission_velocity):
        """Compute decentralized control for robot."""
        robot = self.robots[robot_id]
        neighbors = robot.get_neighbors()
        
        # Mission control
        u_mission = mission_velocity
        
        # Rigidity maintenance
        λ = compute_local_rigidity(robot, neighbors)
        if λ < self.λ_desired:
            u_rigidity = self.rigidity_gradient(robot, neighbors)
            # Blend mission and rigidity
            α = (self.λ_desired - λ) / self.λ_desired
            u = (1 - α) * u_mission + α * u_rigidity
        else:
            u = u_mission
        
        return u
    
    def rigidity_gradient(self, robot, neighbors):
        """Gradient of rigidity eigenvalue."""
        # Numerical gradient computation
        ε = 1e-6
        grad = np.zeros(self.d)
        for i in range(self.d):
            robot_pos_plus = robot.position.copy()
            robot_pos_plus[i] += ε
            λ_plus = compute_rigidity_with_position(robot_pos_plus, neighbors)
            
            robot_pos_minus = robot.position.copy()
            robot_pos_minus[i] -= ε
            λ_minus = compute_rigidity_with_position(robot_pos_minus, neighbors)
            
            grad[i] = (λ_plus - λ_minus) / (2 * ε)
        
        return grad
```

### Rigidity Graph Construction

```python
def construct_rigidity_graph(positions, sensing_range):
    """
    Construct sensing graph ensuring rigidity.
    
    Args:
        positions: n×d matrix of robot positions
        sensing_range: Maximum sensing distance
    
    Returns:
        adjacency: n×n adjacency matrix
    """
    n, d = positions.shape
    adjacency = np.zeros((n, n))
    
    for i in range(n):
        for j in range(i+1, n):
            distance = np.linalg.norm(positions[i] - positions[j])
            if distance <= sensing_range:
                adjacency[i, j] = 1
                adjacency[j, i] = 1
    
    return adjacency
```

## Use Cases

### 1. Formation Flying

```
Application: Drone swarms maintaining geometric formation
Requirements: 
- Minimum bearing measurements per drone
- Angle rigidity for shape maintenance
- Bearing rigidity for absolute positioning
```

### 2. Underwater Vehicle Networks

```
Application: AUV networks for ocean mapping
Challenges:
- Limited sensing range
- Body-frame measurements only
- Switching topologies
```

### 3. Ground Robot Teams

```
Application: Search and rescue robot formations
Benefits:
- Robust localization without GPS
- Formation maintenance during mission
- Scalable to large teams
```

## Parameters

| Parameter | Description | 2D | 3D |
|-----------|-------------|----|-----|
| Min bearings | Minimum per robot | 1 | 2 |
| Rigidity λ | Quality metric | >0 | >0 |
| Sensing range | Max distance | Depends | Depends |
| Switching freq | Topology changes | Limited | Limited |

## Activation Keywords

- multi-robot rigidity
- angle-based localization
- bearing rigidity
- formation control
- rigidity maintenance
- SE(2)/SE(3) control
- directed sensing graphs

## Related Skills

- `distributed-bilevel-mas-optimization`: Multi-agent optimization
- `density-driven-optimal-control`: Density-based control
- `multi-agent-density-control`: Multi-agent density control

## References

- Paper: arXiv:2604.11754 (April 2026)
- Authors: Presenza, Colombo, Giribet, Mas
- Categories: Multi-robot systems, Formation control, Rigidity theory

## Example Usage

```
"Design angle-based formation control for robot swarm"
"Maintain rigidity in multi-robot network with switching topology"
"Implement bearing-based localization for drone team"
"Compute rigidity eigenvalue for robot formation"
```

## Notes

- Works in both 2D (SE(2)) and 3D (SE(3)) configurations
- Requires at least d-1 bearing measurements per robot
- Switching topologies supported under mild conditions
- Angle and bearing rigidity are equivalent under given conditions
- Decentralized implementation scales to large networks
