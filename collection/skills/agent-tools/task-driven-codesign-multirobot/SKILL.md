---
name: task-driven-codesign-multirobot
description: Task-Driven Co-Design (TDCD) methodology for heterogeneous multi-robot systems. Bi-level combinatorial optimization combining MILP and MCTS for robot design, fleet composition, and planning. Use for multi-agent robotics, automated logistics, co-design problems, and hybrid optimization.
---

# Task-Driven Co-Design of Heterogeneous Multi-Robot Systems

This skill provides methodology for Task-Driven Co-Design (TDCD) of heterogeneous multi-robot systems, based on the paper "Task-Driven Co-Design of Heterogeneous Multi-Robot Systems" (arXiv:2604.21894).

## Overview

TDCD formulates multi-robot system design as a **bi-level combinatorial optimization problem**:
- **Outer-loop**: Selects fleet composition (discrete decisions)
- **Inner-loop**: Searches robot designs and computes coordinated multi-agent plans (continuous + discrete decisions)

## Methodology

The framework synergistically couples **Mixed-Integer Linear Programming (MILP)** and **Monte Carlo Tree Search (MCTS)**:

### MILP Component
- Handles continuous robot design variables
- Optimizes trajectory planning
- Manages operational constraints

### MCTS Component
- Explores discrete decision space of fleet composition
- Handles combinatorial explosion of robot type/quantity combinations
- Provides anytime algorithm with convergence guarantees

## Key Contributions

1. **10× speedup** compared to pure MILP baseline
2. **30% higher success rate** compared to pure MCTS
3. Validated on warehouse logistics with ground + aerial robots

## Problem Formulation

### Variables
- **Fleet composition**: Number and types of robots
- **Robot designs**: Physical parameters (size, battery, sensors)
- **Multi-agent plans**: Coordinated trajectories and task assignments

### Constraints
- Task requirements (pick-and-place operations)
- Physical feasibility (collision avoidance, battery life)
- Resource limitations (budget, space)

## Implementation Guide

### Step 1: Define Task Requirements
```python
task_requirements = {
    "operations": [...],  # List of pick-and-place tasks
    "environment": {...}, # Warehouse layout, obstacles
    "constraints": {...} # Time windows, resource limits
}
```

### Step 2: Initialize MCTS
```python
from mcts import MCTSNode, UCB1

# Root node: empty fleet
root = MCTSNode(fleet_composition={})

# UCB1 for exploration/exploitation
ucb_score = Q + C * sqrt(log(N_parent) / N)
```

### Step 3: MILP Sub-problem
```python
from pulp import LpProblem, LpVariable, lpSum

# For each candidate fleet composition from MCTS
milp = LpProblem(f"RobotDesign_{fleet_id}", LpMinimize)

# Variables: robot parameters, trajectories
robot_params = LpVariable.dicts("params", [...], lowBound=0)
trajectories = LpVariable.dicts("traj", [...], cat='Binary')

# Objective: minimize total cost / maximize throughput
milp += lpSum([costs[r] * robot_params[r] for r in robots])

# Solve MILP for this fleet composition
solution = milp.solve()
```

### Step 4: Backpropagation
```python
def backpropagate(node, reward):
    while node:
        node.visits += 1
        node.value += reward
        node = node.parent
```

## Workflow

```
1. Input: Task requirements, robot specifications
2. Initialize MCTS with empty fleet
3. While computational budget remains:
   a. Select: UCB1 to choose promising fleet composition
   b. Expand: Add new robot types/quantities
   c. Simulate: Solve MILP for trajectory and design
   d. Backpropagate: Update MCTS statistics
4. Return: Best (fleet, design, plan) triple
```

## Advantages

| Aspect | Pure MILP | Pure MCTS | TDCD (MILP+MCTS) |
|--------|-----------|-----------|------------------|
| Continuous optimization | ✓ | ✗ | ✓ (MILP) |
| Combinatorial handling | ✗ (slow) | ✓ | ✓ (MCTS) |
| Scalability | Limited | Moderate | High |
| Solution quality | Optimal (if solves) | Approximate | High-quality |
| Speed | Slow | Moderate | Fast (10×) |

## Applications

- **Warehouse logistics**: Ground + aerial robots for inventory management
- **Search and rescue**: Heterogeneous teams (drones + ground vehicles)
- **Manufacturing**: Collaborative robots with different capabilities
- **Agriculture**: Multi-modal farming robots

## Trigger Keywords

- "multi-robot co-design"
- "fleet composition optimization"
- "task-driven design"
- "heterogeneous robot systems"
- "MILP MCTS hybrid optimization"
- "warehouse automation design"
- "robot fleet planning"

## References

- Stralz, M., Alharbi, M., Huang, Y., et al. (2026). "Task-Driven Co-Design of Heterogeneous Multi-Robot Systems." arXiv:2604.21894.
- Silver, D., et al. (2016). "Mastering the game of Go with deep neural networks and tree search." Nature.
- Bertsimas, D., & Tsitsiklis, J. (1997). "Introduction to Linear Optimization."

## Tools Used

- **Python**: `pulp` (MILP), `numpy`, `anytree` (MCTS)
- **ROS**: For robot simulation
- **Gazebo**: Physics simulation for validation

## Example Use Case

```
User: "I need to design a warehouse automation system with 1000 pick-and-place 
operations per hour. Should I use ground robots, drones, or a mix?"

Agent: Using TDCD framework, I can:
1. Formulate as bi-level optimization
2. Explore fleet compositions with MCTS
3. Optimize designs and trajectories with MILP
4. Compare pure ground, pure aerial, and mixed solutions

Result: Mixed fleet of 15 ground robots + 8 drones provides optimal 
throughput at minimum cost.
```
