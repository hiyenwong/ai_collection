---
name: eeg-hopfield-emotion-energy
description: >
  Energy landscapes for quantifying brain network stability during emotional processing.
  Uses Hopfield network energy framework to analyze EEG dynamics, mapping emotional
  states to attractor basins in brain network energy landscapes. Provides a physics-based
  framework for understanding emotional stability and transitions.
  Activation: energy landscape, Hopfield network emotion, brain network stability,
  emotional processing EEG, attractor dynamics, affective neuroscience,
  能量景观, 情绪脑网络, 吸引子动力学
version: 1.0.0
metadata:
  hermes:
    source_paper: "Energy Landscapes of Emotion: Quantifying Brain Network Stability during Emotional Processing"
    arxiv_id: "2603.27644"
    tags: [eeg, emotion, energy-landscape, hopfield, attractor, stability]
---

# Energy Landscapes of Emotion

## Overview

Maps emotional states to attractor basins in brain network energy landscapes using Hopfield network framework. Provides quantitative measures of emotional stability, transition barriers, and metastability from EEG data.

## Core Framework

### Energy Function
```
E(x) = -½ Σᵢⱼ Wᵢⱼ xᵢ xⱼ + Σᵢ θᵢ xᵢ
```
Where:
- Wᵢⱼ = functional connectivity between brain regions
- xᵢ = activity of region i
- θᵢ = bias terms (regional excitability)

### Emotional States as Attractors
- Each emotional state corresponds to a local energy minimum
- Depth of basin → emotional stability
- Barrier height → difficulty of emotional transition
- Basin width → emotional flexibility

## Analysis Pipeline

```python
class EmotionEnergyLandscape:
    def __init__(self, connectivity_matrix):
        self.W = connectivity_matrix  # from EEG functional connectivity
        self.energy_history = []
    
    def compute_energy(self, brain_state):
        """Compute Hopfield energy for a brain state."""
        return -0.5 * brain_state @ self.W @ brain_state.T
    
    def find_attractors(self, states):
        """Identify emotional attractor basins."""
        energies = [self.compute_energy(s) for s in states]
        # Cluster states by energy level
        attractors = cluster_by_energy(energies, states)
        return attractors
    
    def transition_barriers(self, attractor_a, attractor_b):
        """Compute energy barrier between emotional states."""
        path = minimum_energy_path(attractor_a, attractor_b)
        return max(path.energies) - attractor_a.energy
```

## Key Metrics

1. **Landscape Depth**: Overall energy range → emotional range capacity
2. **Basin Stability**: Depth of each attractor → emotional persistence
3. **Transition Rates**: Barrier heights → emotional switching frequency
4. **Metastability**: Number and arrangement of basins → emotional complexity

## Applications

- Depression: abnormally deep negative attractors
- Anxiety: shallow basins with low barriers
- Bipolar: multiple competing deep basins
- Emotional regulation therapy planning

## Related Skills

- eeg-hopfield-emotion-energy, neural-dynamics-decision-making, kuramoto-brain-network

## Activation Keywords

- "eeg-hopfield-emotion-energy"
- "eeg hopfield emotion energy"
- "use eeg hopfield emotion energy"
- "eeg hopfield emotion energy help"
- "eeg hopfield emotion energy tool"

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

### Basic Eeg Hopfield Emotion Energy usage
```
User: "Help me with eeg hopfield emotion energy"
→ Understand requirements → Execute actions → Provide results
```

### Advanced usage
```
User: "I need detailed eeg hopfield emotion energy assistance"
→ Clarify scope → Provide comprehensive solution → Follow up
```
