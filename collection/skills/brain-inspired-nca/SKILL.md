---
name: brain-inspired-nca
version: v1.0.0
last_updated: 2026-04-06
description: Brain-inspired Neural Cellular Automata for morphogenesis and motor control. Extends traditional NCA with brain-like topologies and long-range connections beyond Moore neighborhood. Use for: (1) Morphogenesis simulation and pattern formation, (2) Motor control systems, (3) Bio-inspired self-organizing systems, (4) Complex topology cellular automata research. Triggered by: BraiNCA, neural cellular automata, brain-inspired CA, morphogenesis NCA, bio-inspired self-organization.
---

# Brain-Inspired Neural Cellular Automata (BraiNCA)

## Overview

BraiNCA extends traditional Neural Cellular Automata by incorporating brain-like topologies with long-range connections and complex network structures, moving beyond simple Moore neighborhoods. This enables morphogenesis simulation, motor control, and self-organizing systems that better mimic biological neural development processes.

## Core Concepts

### Traditional NCA vs BraiNCA

**Traditional NCA Limitations:**
- Regular grid topology
- Moore neighborhood (8 adjacent cells)
- No long-range connections
- Simple local interactions

**BraiNCA Extensions:**
- Brain-inspired complex topologies
- Long-range connections beyond neighborhood
- Multi-scale network structure
- Richer interaction dynamics

### Key Applications

1. **Morphogenesis** - Pattern formation and shape development
2. **Motor Control** - Movement coordination and execution
3. **Self-Organization** - Emergent behavior from local rules
4. **Developmental Biology** - Simulating biological growth processes

## Implementation Workflow

### Step 1: Define Topology

Create brain-inspired network topology:

```python
import numpy as np
import networkx as nx

# Create brain-like topology
G = nx.Graph()

# Add nodes (cells/units)
n_cells = 1000
G.add_nodes_from(range(n_cells))

# Add local connections (Moore-like neighborhood)
for i in range(n_cells):
    local_neighbors = get_local_neighbors(i, radius=1)
    G.add_edges_from([(i, j) for j in local_neighbors])

# Add long-range connections (brain-inspired)
# These mimic white matter tracts in the brain
long_range_prob = 0.01  # Low probability, high impact
for i in range(n_cells):
    if np.random.random() < long_range_prob:
        distant = np.random.randint(0, n_cells)
        G.add_edge(i, distant)
```

### Step 2: Configure Cellular Automata Rules

Define update rules with neural dynamics:

```python
def brain_nca_update(state, G, weights):
    """Update state based on neighbor inputs."""
    new_state = np.zeros_like(state)
    
    for node in G.nodes():
        neighbors = list(G.neighbors(node))
        neighbor_states = state[neighbors]
        
        # Weighted combination of neighbor states
        local_weight = 0.8
        long_range_weight = 0.2
        
        # Compute weighted input
        input_sum = compute_weighted_input(
            neighbor_states, neighbors, node, G,
            local_weight, long_range_weight
        )
        
        # Apply neural-like activation
        new_state[node] = sigmoid(input_sum)
    
    return new_state
```

### Step 3: Implement Morphogenesis

For pattern formation tasks:

```python
def morphogenesis_simulation(n_steps=100):
    """Simulate morphogenesis with BraiNCA."""
    state = initialize_pattern()
    topology = create_brain_topology()
    weights = initialize_weights()
    
    for t in range(n_steps):
        state = brain_nca_update(state, topology, weights)
        
        # Visualize progress
        if t % 10 == 0:
            visualize_pattern(state, topology)
    
    return state
```

### Step 4: Motor Control Application

For motor coordination:

```python
def motor_control_simulation(target_pattern):
    """Use BraiNCA for motor control."""
    # Initialize motor state
    motor_state = initialize_motor_units()
    
    # Create control topology
    control_topology = create_motor_control_topology()
    
    # Train to reach target
    for epoch in range(training_epochs):
        current = run_brain_nca(motor_state, control_topology)
        error = compute_motor_error(current, target_pattern)
        update_weights(error)
    
    return trained_weights
```

## Reference Papers

- **BraiNCA arXiv**: 2604.01932
- **Authors**: Léo Pio-Lopez, Benedikt Hartl, Michael Levin
- **Key Innovation**: Brain-inspired topology for NCA

## Related Skills

- `spikingjelly-framework` - Spiking neural network implementation
- `bio-neuron-snn-learning` - Biological neuron models
- `neural-dynamics-decision-making` - Neural dynamics analysis

## Tools Used

- `exec`: Run Python scripts for NCA simulation
- `write`: Create simulation scripts and results
- `read`: Load topology configurations and parameters

## Examples

### Example 1: Morphogenesis Simulation

**User**: "Create a BraiNCA simulation for pattern formation"

**Agent**: 
1. Define brain-inspired topology with long-range connections
2. Configure cellular automata update rules
3. Initialize pattern state
4. Run simulation for 100 steps
5. Visualize morphogenesis progress

### Example 2: Motor Control System

**User**: "Design a motor control system using BraiNCA"

**Agent**:
1. Create motor unit topology
2. Define target movement pattern
3. Configure neural update dynamics
4. Train weights to achieve target
5. Test trained system performance

---

**Note**: This skill is research-oriented and based on the BraiNCA paper (arXiv:2604.01932). It provides conceptual framework and implementation guidance for brain-inspired cellular automata systems.
