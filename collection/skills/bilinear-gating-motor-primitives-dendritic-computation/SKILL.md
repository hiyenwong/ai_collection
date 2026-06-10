---
name: bilinear-gating-motor-primitives-dendritic-computation
description: Bilinear gating methodology linking dendritic coincidence detection to rapid goal-directed adaptation. Burst fraction encoding in motor cortex provides goal-selective code, enabling zero-shot generalization.
keywords:
  - motor cortex
  - dendritic computation
  - burst fraction
  - goal-directed adaptation
  - bilinear gating
  - motor primitives
  - coincidence detection
  - reinforcement learning
  - zero-shot generalization
  - neural coding
triggers:
  - motor cortex coding
  - dendritic computation
  - burst encoding
  - goal adaptation
  - motor primitives
  - coincidence detection
  - bilinear gate
activation_keywords:
  - motor cortex
  - dendritic
  - burst
  - goal
  - motor primitive
  - adaptation
arxiv_id: 2606.10891
paper_title: Bilinear gating of motor primitives: a principle linking dendritic computation to rapid goal-directed adaptation
authors: Cristiano Capone, Luca Falorsi, Andrea Ciardiello, Luca Manneschi
submitted: 2026-06-09
venue: arXiv
categories:
  - neuroscience
  - computational neuroscience
  - motor control
  - dendritic computation
---

# Bilinear Gating of Motor Primitives: Dendritic Computation to Goal-Directed Adaptation

## Overview

This methodology establishes **bilinear gating** as a fundamental principle linking dendritic coincidence detection in layer-5 pyramidal neurons to rapid goal-directed motor adaptation. The key finding: **burst fraction** (proportion of spikes in high-frequency bursts) encodes reach direction far more selectively than overall firing rate.

## Key Discovery

**Burst Fraction Encoding**:
- Motor cortex neurons encode reach direction (goal) via **burst fraction**, NOT firing rate
- Dissociation holds across 12 recording sessions, 3 animals, 2 laboratories (p < 10^-12)
- Goal information concentrated specifically in bursts
- State information (what action) encoded in firing rate

## Cellular Mechanism: Dendritic Coincidence Detection

**Bilinear Gate Model**:
```
G(g) · Y(s) = Burst Probability

where:
  G(g) = goal-related apical input (top-down)
  Y(s) = state-related basal drive (bottom-up)
  coincidence = apical + basal → burst
```

**Layer-5 Pyramidal Neuron Architecture**:
- **Apical dendrites**: Receive goal-related signals (cognitive/top-down)
- **Basal dendrites**: Receive state-related signals (motor/sensory/bottom-up)
- **Coincidence detection**: When both inputs arrive simultaneously → high-frequency burst

## Two-Compartment Spiking Model

**Minimal Model Implementation**:
1. Compartment 1 (somatic): Integrates basal inputs → firing rate Y(s)
2. Compartment 2 (apical): Integrates apical inputs → goal signal G(g)
3. Coincidence mechanism: Burst when both active

**Key Parameters**:
- Burst threshold: Coincidence detection window (~5-10 ms)
- Burst frequency: >100 Hz for burst classification
- Burst fraction: #bursts / total_spikes

## Computational Advantage: Zero-Shot Generalization

**Reinforcement Learning Agent Integration**:
- Bilinear gate G(g)·Y(s) embedded in RL agent
- Enables **zero-shot generalization** to new goals
- Rapid online adaptation without retraining
- Segregating goal into bursts provides learning advantage

**Why Bursts?**:
- Bursts carry goal information → easy to extract
- Firing rate carries state information → action specification
- Separation enables parallel processing: what + which goal

## Experimental Evidence

**Datasets**:
- Macaque motor cortex recordings (reaching tasks)
- 12 sessions across 3 animals
- 2 independent laboratories
- Statistical significance: p < 10^-12 for all sessions

**Controls**:
- Firing rate contribution removed
- Burst fraction still selective after controls
- Confirms dissociation is genuine

## Implementation Guide

### Burst Detection Algorithm

```python
def compute_burst_fraction(spike_times, burst_threshold=100, min_burst_spikes=2):
    """
    Compute burst fraction from spike train.
    
    Args:
        spike_times: Array of spike timestamps (ms)
        burst_threshold: Minimum ISI for burst (ms, default ~10ms → 100Hz)
        min_burst_spikes: Minimum spikes in burst (default 2)
    
    Returns:
        burst_fraction: Proportion of spikes in bursts
    """
    isis = np.diff(spike_times)
    in_burst = isis < burst_threshold
    
    # Identify bursts
    burst_indices = []
    current_burst = []
    
    for i, is_burst in enumerate(in_burst):
        if is_burst:
            current_burst.append(i)
        else:
            if len(current_burst) >= min_burst_spikes:
                burst_indices.extend(current_burst)
            current_burst = []
    
    # Count burst spikes vs total
    burst_spikes = len(burst_indices)
    total_spikes = len(spike_times)
    
    return burst_spikes / total_spikes if total_spikes > 0 else 0
```

### Two-Compartment Model

```python
class BilinearGatedNeuron:
    """Two-compartment spiking model for bilinear gating."""
    
    def __init__(self, tau_somatic=20, tau_apical=50, coincidence_window=10):
        self.V_somatic = 0  # Basal state integration
        self.V_apical = 0   # Apical goal integration
        self.tau_somatic = tau_somatic
        self.tau_apical = tau_apical
        self.coincidence_window = coincidence_window
    
    def update(self, basal_input, apical_input, dt=1):
        """Update both compartments."""
        # Somatic: basal state input (Y(s))
        self.V_somatic += (basal_input - self.V_somatic) * dt / self.tau_somatic
        
        # Apical: goal input (G(g))
        self.V_apical += (apical_input - self.V_apical) * dt / self.tau_apical
        
        # Bilinear gate: coincidence detection
        burst_prob = self.V_somatic * self.V_apical
        
        return burst_prob
```

### RL Agent with Bilinear Gate

```python
class BilinearGatedAgent:
    """RL agent with bilinear gating for goal adaptation."""
    
    def __init__(self, n_goals, n_states):
        self.goal_representations = np.random.randn(n_goals)
        self.state_representations = np.random.randn(n_states)
        self.bilinear_gate = BilinearGatedNeuron()
    
    def select_action(self, goal, state):
        """Select action using bilinear gate."""
        g_signal = self.goal_representations[goal]
        s_signal = self.state_representations[state]
        
        # Compute burst probability (goal-state product)
        burst_prob = self.bilinear_gate.update(s_signal, g_signal)
        
        # Burst encodes goal-specific action selection
        # Firing rate encodes state-specific motor primitive
        
        return burst_prob
```

## Applications

1. **Motor Control**: Rapid adaptation to new reaching goals
2. **BCI Design**: Goal-specific decoding from burst patterns
3. **Neuromorphic Computing**: Dendritic coincidence detection circuits
4. **RL Agents**: Zero-shot goal generalization
5. **Neural Coding Analysis**: Burst fraction vs firing rate dissociation

## Pitfalls

1. **Burst Definition**: Must use consistent ISI threshold (~10ms)
2. **Firing Rate Control**: Remove firing rate contribution before analyzing burst fraction
3. **Coincidence Window**: Must match dendritic integration timescale (5-10 ms)
4. **Session Variability**: Burst fraction varies across sessions, normalize per session
5. **Non-linear Effects**: Burst fraction saturates at high firing rates

## Key Equations

**Bilinear Gate**:
$$P_{burst} = G(g) \cdot Y(s)$$

**Burst Fraction**:
$$f_{burst} = \frac{N_{burst\_spikes}}{N_{total\_spikes}}$$

**Goal Selectivity**:
$$Selectivity = \frac{f_{burst}(goal\_1)}{f_{burst}(goal\_2)}$$

## Verification Steps

1. Compute burst fraction for each neuron across goals
2. Verify burst fraction selectivity > firing rate selectivity
3. Apply firing rate controls (match rate distributions)
4. Check burst fraction remains selective after controls
5. Test zero-shot generalization in RL agent

## Related Work

- Larkum et al. (1999): Dendritic coincidence detection in L5 pyramidal neurons
- Polsky et al. (2009): Branch-specific dendritic processing
- Doron et al. (2020): Goal encoding in motor cortex
- Modern Hopfield Networks: Associative memory connection

## References

- arXiv:2606.10891 - Bilinear gating of motor primitives (Capone et al., 2026)
- Larkum ME, et al. (1999) Nature - Dendritic Ca2+ spikes
- Polsky A, et al. (2009) Science - Dendritic branch processing

---
*Source: arXiv:2606.10891 | Created: 2026-06-11 | Category: neuroscience*