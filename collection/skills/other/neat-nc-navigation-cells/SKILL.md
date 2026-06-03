---
name: neat-nc-navigation-cells
description: NEAT-guided navigation cells for robot path planning. Evolves neural network controllers for navigation using NeuroEvolution of Augmenting Topologies. Combines evolutionary computation with robotics navigation. Activation: NEAT navigation, neuroevolution path planning, evolved navigation cells, robot navigation neural evolution.
version: 1.0.0
metadata:
  hermes:
    source_paper: "NEAT-NC: NEAT guided Navigation Cells for Robot Path Planning (arXiv:2604.15076)"
    tags: [neuroevolution, robot-navigation, neat, path-planning, evolutionary-computation]
---

# NEAT-NC: NEAT-guided Navigation Cells for Robot Path Planning

## Overview
Navigation cell architecture evolved using NeuroEvolution of Augmenting Topologies (NEAT) for autonomous robot path planning. The approach evolves both the structure and weights of neural networks specialized for navigation tasks.

## Source Paper
- **Title:** NEAT-NC: NEAT guided Navigation Cells for Robot Path Planning
- **arXiv:** 2604.15076v1
- **Authors:** Hibatallah Meliani, Khadija Slimani, Samira Khoulji
- **Published:** 2026-04-16

## Core Concepts

### NEAT Algorithm
NEAT evolves neural networks by:
1. **Complexification:** Starting simple, adding neurons/connections
2. **Speciation:** Protecting innovation through species separation
3. **Historical markings:** Tracking gene lineage for crossover

### Navigation Cell Design
The evolved navigation cell processes:
- **Sensory input:** Distance sensors, compass, goal direction
- **Internal state:** Memory of visited locations
- **Motor output:** Velocity commands, turning angle

### Implementation

```python
import numpy as np

class NavigationCell:
    def __init__(self, n_inputs=8, n_outputs=2, hidden_nodes=None):
        self.n_inputs = n_inputs
        self.n_outputs = n_outputs
        self.hidden_nodes = hidden_nodes or []
        self.weights = self._init_weights()
        self.state = np.zeros(len(self.hidden_nodes))

    def _init_weights(self):
        W = {}
        W['input_hidden'] = np.random.randn(len(self.hidden_nodes), self.n_inputs) * 0.5
        W['hidden_hidden'] = np.random.randn(len(self.hidden_nodes), len(self.hidden_nodes)) * 0.1
        W['hidden_output'] = np.random.randn(self.n_outputs, len(self.hidden_nodes)) * 0.5
        return W

    def step(self, sensor_input):
        h = np.tanh(
            self.weights['input_hidden'] @ sensor_input +
            self.weights['hidden_hidden'] @ self.state
        )
        self.state = h
        output = np.tanh(self.weights['hidden_output'] @ h)
        return output

    def navigate(self, sensors, goal_dir, obstacles):
        input_vec = np.concatenate([sensors, [goal_dir]])
        motor = self.step(input_vec)
        velocity = (motor[0] + 1) / 2
        turn_angle = motor[1] * np.pi
        return velocity, turn_angle
```

## Applications
- Autonomous robot navigation
- Path planning in unknown environments
- Evolving specialized navigation controllers
- Bio-inspired robotics

## Related
- [[density-driven-multi-agent-control]]
- [[developmental-minimal-neural-circuits]]
