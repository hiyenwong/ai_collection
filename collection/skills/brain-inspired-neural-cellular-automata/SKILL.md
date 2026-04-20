---
name: brain-inspired-neural-cellular-automata
description: Brain-inspired Neural Cellular Automata (BraiNCA) for morphogenesis and motor control. Uses biological neighborhood structures beyond regular grids.
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [neural-cellular-automata, morphogenesis, motor-control, brain-inspired, self-organization, developmental]
    source_paper: "BraiNCA: brain-inspired neural cellular automata and applications to morphogenesis and motor control (arXiv:2604.01932v1)"
---

# BraiNCA: Brain-Inspired Neural Cellular Automata

## Overview
BraiNCA extends Neural Cellular Automata beyond regular Moore neighborhoods to incorporate brain-inspired connectivity patterns. By using biologically-motivated neighborhood structures and update rules, BraiNCA achieves complex morphogenesis and motor control behaviors with self-organizing dynamics.

## Core Concepts

### Beyond Grid Neighborhoods
- Traditional NCAs use fixed Moore (8-neighbor) neighborhoods
- BraiNCA uses irregular, brain-inspired connectivity graphs
- Neighborhood structure adapts to task requirements

### Self-Organization
- Local rules produce global patterns (emergent behavior)
- Morphogenesis: growing complex structures from simple rules
- Motor control: coordinated movement through local interactions

### Biological Inspiration
- Cortical column organization
- Recurrent local processing with long-range connections
- Developmental plasticity during growth phase

## Implementation Pattern
```python
class BraiNCA(nn.Module):
    def __init__(self, n_cells, state_dim, neighborhood_graph):
        super().__init__()
        self.n_cells = n_cells
        self.state_dim = state_dim
        self.adj = neighborhood_graph
        self.update_rule = nn.Sequential(
            nn.Linear(state_dim * 2, 64), nn.ReLU(),
            nn.Linear(64, state_dim)
        )
    
    def step(self, states):
        new_states = []
        for i in range(self.n_cells):
            neighbors = self.get_neighbors(i, states)
            cell_state = states[i]
            neighbor_mean = neighbors.mean(dim=0)
            combined = torch.cat([cell_state, neighbor_mean])
            new_state = self.update_rule(combined)
            new_states.append(new_state)
        return torch.stack(new_states)
    
    def get_neighbors(self, cell_idx, states):
        neighbor_indices = torch.where(self.adj[cell_idx])[0]
        return states[neighbor_indices]
```

## Applications
- Developmental robotics
- Self-organizing materials and structures
- Biological morphogenesis simulation
- Distributed motor control systems

## Activation Keywords
- neural cellular automata, BraiNCA, morphogenesis NCA, self-organizing systems, brain-inspired cellular automata, 神经细胞自动机, 形态发生

## References
- BraiNCA: brain-inspired neural cellular automata and applications to morphogenesis and motor control
- Authors: Léo Pio-Lopez, Benedikt Hartl, Michael Levin
- Published: 2026-04-02
- arXiv: https://arxiv.org/abs/2604.01932v1

## Tools Used

- `Read` - Read existing files and documentation
- `Write` - Create new files and documentation
- `Bash` - Execute commands when needed

## Instructions for Agents

1. Identify user's intent and specific requirements
2. Gather necessary context from files or user input
3. Execute appropriate actions using available tools
4. Provide clear results and suggest next steps

## Examples

### Basic Brain Inspired Neural Cellular Automata usage
```
User: "Help me with brain inspired neural cellular automata"
→ Understand requirements → Execute actions → Provide results
```

### Advanced usage
```
User: "I need detailed brain inspired neural cellular automata assistance"
→ Clarify scope → Provide comprehensive solution → Follow up
```
