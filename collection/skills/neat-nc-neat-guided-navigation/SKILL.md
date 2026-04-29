---
name: neat-neural-cell-navigation
description: "NEAT-guided navigation cells for robot path planning. Inspired by brain navigation cells (place cells, grid cells, head direction cells) using evolutionary algorithms. Activation: neat navigation, robot path planning, navigation cells, brain inspired robotics, evolutionary robotics."
---

# NEAT-NC: NEAT Guided Navigation Cells for Robot Path Planning

## Overview

To navigate a space, the brain makes an internal representation of the environment using different cells such as place cells, grid cells, head direction cells, border cells, and speed cells. All these cells, along with sensory inputs, enable an organism to explore the space around it. This skill provides a methodology for evolving navigation cells using NEAT (NeuroEvolution of Augmenting Topologies) for robot path planning.

## Source Paper

- **Title**: NEAT-NC: NEAT guided Navigation Cells for Robot Path Planning
- **arXiv**: 2604.15076v1
- **Published**: 2026

## Core Concepts

### Biological Navigation Cells

The brain's navigation system consists of specialized cell types:

| Cell Type | Function | Brain Region |
|-----------|----------|--------------|
| Place Cells | Fire at specific locations | Hippocampus |
| Grid Cells | Hexagonal firing pattern | Entorhinal cortex |
| Head Direction Cells | Encode heading direction | Multiple regions |
| Border Cells | Fire near boundaries | Subiculum |
| Speed Cells | Encode movement speed | Medial entorhinal cortex |

### NEAT Algorithm

NEAT (NeuroEvolution of Augmenting Topologies) evolves both:
1. **Network weights** (connection strengths)
2. **Network topology** (which connections exist)

This allows emergence of navigation-like representations without hand-designed architectures.

## Implementation

### Navigation Cell Network

```python
import numpy as np
import neat

class NavigationCellNetwork:
    """NEAT-evolved network that learns navigation cell behaviors."""
    
    def __init__(self, genome, config):
        self.network = neat.nn.FeedForwardNetwork.create(genome, config)
        
    def activate(self, sensor_inputs):
        """Process sensor inputs and produce navigation outputs."""
        outputs = self.network.activate(sensor_inputs)
        return outputs

class NEATNavigationPlanner:
    """Robot path planner using evolved navigation cells."""
    
    def __init__(self, genome, config):
        self.network = NavigationCellNetwork(genome, config)
        self.path_history = []
        
    def plan_path(self, start, goal, environment):
        """Plan path from start to goal using navigation cell network."""
        current_pos = start
        path = [current_pos]
        
        for step in range(500):
            if np.linalg.norm(np.array(current_pos) - np.array(goal)) < 0.1:
                break
            sensors = self.get_sensor_readings(current_pos, environment)
            outputs = self.network.activate(sensors)
            current_pos = self.apply_movement(current_pos, outputs)
            path.append(current_pos)
        
        return path
    
    def get_sensor_readings(self, position, environment):
        """Simulate sensor inputs for the network."""
        distances = [
            environment.distance_to_obstacle(position, angle)
            for angle in np.linspace(0, 2*np.pi, 8, endpoint=False)
        ]
        return distances + [0, 1.0]  # heading, speed
```

### Fitness Function Design

```python
def navigation_fitness(genome_id, genome, config):
    """
    Fitness function for navigation cell evolution.
    Combines: path efficiency, collision avoidance, exploration bonus.
    """
    net = neat.nn.FeedForwardNetwork.create(genome, config)
    total_score = 0
    for env in test_environments:
        path = evolve_path(net, env)
        path_length = sum(np.linalg.norm(np.array(path[i+1]) - np.array(path[i]))
                         for i in range(len(path)-1))
        collisions = count_collisions(path, env)
        reached_goal = reached_target(path, env.goal)
        score = 1000 * reached_goal - 10 * path_length - 100 * collisions
        total_score += max(score, 0)
    return total_score
```

## Practical Applications

### 1. Indoor Robot Navigation

Use evolved navigation cells for:
- Warehouse robots (avoiding obstacles, finding targets)
- Service robots (navigating dynamic environments)
- Delivery robots (mapping and path optimization)

### 2. Biological Plausibility Analysis

```python
def analyze_cell_similarity(network_activations, real_cell_data):
    """Compare evolved cell responses to biological data."""
    place_correlation = np.corrcoef(
        network_activations['place'],
        real_cell_data['place']
    )[0, 1]
    grid_hexagonality = compute_grid_hexagonality(
        network_activations['grid']
    )
    return {
        'place_correlation': place_correlation,
        'grid_hexagonality': grid_hexagonality,
    }
```

## Limitations

- Requires significant evolutionary computation time
- Performance depends on environment complexity
- May not generalize across very different environments
- Biological cell similarity is approximate, not exact

## Related Skills

- brain-network-controllability
- density-driven-multi-agent-control

## Activation Keywords

- neat navigation, robot path planning, navigation cells, brain inspired robotics, evolutionary robotics, place cells, grid cells
