---
name: bilinear-gating-motor-primitives-dendritic-computation
description: >
  Bilinear gating methodology linking dendritic coincidence detection to goal-directed adaptation.
  Motor cortex neurons encode goal information in burst fraction (not firing rate), implementing
  bilinear gate G(g)·Y(s) where goal and state inputs multiply via dendritic coincidence detection.
  Supports zero-shot generalization and rapid online adaptation. Accepted arXiv 2606.10891.
category: neuroscience
---

# Bilinear Gating of Motor Primitives

## Context

Motor cortex must specify both **what action** to produce and **which goal** it serves. This paper reveals a cellular mechanism for separating these factors: **burst fraction** encodes goal direction far more selectively than overall firing rate.

**Key discovery**: Layer-5 pyramidal neurons implement a **bilinear gate** G(g)·Y(s) through dendritic coincidence detection — when goal-related apical input coincides with state-related basal drive, the neuron bursts.

## Core Methodology

### 1. Burst Fraction as Goal-Selective Code

**Definition**: Burst fraction = proportion of spikes emitted in high-frequency bursts

**Validation** (12 recording sessions, 3 animals, 2 labs):
- Burst fraction encodes reach direction more selectively than firing rate (p < 10⁻¹² in every session)
- Dissociation holds after firing rate controls removed
- Goal information concentrated specifically in bursts

### 2. Bilinear Gate Mechanism

**Mathematical formulation**:
```
P(burst) = G(goal) × Y(state)

where:
- G(g) = goal-related apical input
- Y(s) = state-related basal drive
- Burst probability = multiplicative product
```

**Cellular mechanism**:
- Apical dendrites receive goal signals (top-down)
- Basal dendrites receive state signals (bottom-up)
- Coincidence detection triggers bursting
- Burst fraction = goal encoding quality

### 3. Two-Compartment Spiking Model

**Implementation**:
```python
class BilinearGateNeuron:
    def __init__(self):
        self.apical_input = 0.0  # goal signal
        self.basal_input = 0.0   # state signal
        self.threshold = 1.0     # coincidence threshold
        
    def compute_burst_probability(self):
        # Bilinear gate: product of goal and state
        return self.apical_input * self.basal_input
    
    def should_burst(self):
        # Coincidence detection
        coincidence = self.apical_input * self.basal_input
        return coincidence > self.threshold
```

### 4. Reinforcement Learning Integration

**Zero-shot generalization**:
- Embed bilinear gate in RL agent
- Goal information segregated into burst channel
- Rapid adaptation to new goals without retraining
- Motor primitives multiply with goal vectors

## Implementation Steps

### Step 1: Extract Burst Fraction from Spike Trains

```python
import numpy as np

def compute_burst_fraction(spike_times, burst_threshold_hz=50):
    """Calculate burst fraction from spike train.
    
    Args:
        spike_times: array of spike timestamps (seconds)
        burst_threshold_hz: minimum frequency to classify as burst
        
    Returns:
        burst_fraction: proportion of spikes in bursts
    """    
    if len(spike_times) < 2:
        return 0.0
    
    # Compute inter-spike intervals
    isi = np.diff(spike_times)
    
    # Identify bursts (ISI < threshold)
    burst_isi_threshold = 1.0 / burst_threshold_hz  # 20ms for 50Hz
    burst_spikes = isi < burst_isi_threshold
    
    # Count spikes in bursts (both spike pairs)
    n_burst_spikes = np.sum(burst_spikes) + 1  # +1 for burst initiation spike
    
    burst_fraction = n_burst_spikes / len(spike_times)
    return burst_fraction
```

### Step 2: Build Dendritic Coincidence Detector

```python
class DendriticCoincidenceDetector:
    """Two-compartment model for bilinear gating."""    
    def __init__(self, tau_apical=10.0, tau_basal=5.0):
        self.apical_state = 0.0
        self.basal_state = 0.0
        self.tau_apical = tau_apical  # ms
        self.tau_basal = tau_basal    # ms
        
    def update(self, goal_input, state_input, dt_ms=1.0):
        """Update dendritic states with exponential integration."""        
        # Apical integration (goal signal)
        decay_apical = np.exp(-dt_ms / self.tau_apical)
        self.apical_state = decay_apical * self.apical_state + goal_input
        
        # Basal integration (state signal)
        decay_basal = np.exp(-dt_ms / self.tau_basal)
        self.basal_state = decay_basal * self.basal_state + state_input
        
    def compute_gate_output(self):
        """Bilinear gate output."""        
        return self.apical_state * self.basal_state
```

### Step 3: Implement Goal-Conditioned RL Agent

```python
class BilinearGateRLAgent:
    """RL agent with goal-conditioned bilinear gating."""    
    def __init__(self, n_primitives=10, n_goals=5):
        self.primitives = np.random.randn(n_primitives)  # motor primitives Y(s)
        self.goal_vectors = np.random.randn(n_goals, n_primitives)  # G(g)
        
    def select_action(self, goal_idx, state_features):
        """Select action via bilinear gate."""        
        G = self.goal_vectors[goal_idx]  # goal vector
        Y = self.primitives * state_features  # state-modulated primitives
        
        # Bilinear gate: goal × primitive × state
        action = G.dot(Y)
        return action
    
    def adapt_to_new_goal(self, new_goal_features):
        """Zero-shot adaptation to new goal."""        
        # Project new goal onto existing primitive space
        new_goal_vector = np.linalg.lstsq(
            self.primitives.reshape(-1, 1),
            new_goal_features,
            rcond=None
        )[0].flatten()
        
        # Add new goal without retraining primitives
        self.goal_vectors = np.vstack([self.goal_vectors, new_goal_vector])
```

## Pitfalls

1. **Firing rate confound**: Burst fraction ≠ firing rate. Must control for overall firing rate when interpreting goal selectivity. Use ISI-based burst detection, not rate thresholds.

2. **Apical-basal timing**: Coincidence window is critical. Apical and basal inputs must arrive within ~10-20ms. Longer delays reduce gate effectiveness.

3. **Burst classification**: High-frequency threshold matters. 50Hz threshold (20ms ISI) works for motor cortex; different thresholds may be needed for other regions.

4. **Goal vector normalization**: Goal vectors G(g) should be normalized to prevent magnitude bias in gate output. Otherwise, strong goals dominate weak states.

5. **Primitive redundancy**: Motor primitives Y(s) should be orthogonal or low-rank. Redundant primitives reduce generalization capacity.

6. **Electrode placement**: Apical vs basal recording sites affect burst detection. L5 pyramidal neurons have distinct dendritic compartments.

## Verification

1. **Burst fraction vs firing rate**: Compute both metrics; verify burst fraction encodes goal more selectively (ANOVA p < 10⁻⁵)

2. **Coincidence timing**: Test different apical-basal delays; optimal window should match L5 neuron integration time (~10-20ms)

3. **Zero-shot generalization**: New goal should be executable without primitive retraining. Measure success rate on novel goals.

4. **RL performance**: Compare bilinear gate agent vs standard RL. Expect faster adaptation, higher zero-shot success.

5. **Cellular match**: Simulated burst pattern should match recorded burst fraction distribution (KS test p > 0.05)

## References

- Capone et al. (2026) arXiv:2606.10891 - Original bilinear gating discovery
- Larkum et al. (2004) - Dendritic coincidence detection in L5 pyramidal neurons
- modern Hopfield Networks - Associative memory foundation
- Motor primitive theory - Goal-conditioned action selection

## Activation

bilinear gating, motor primitives, dendritic computation, burst fraction, goal-directed adaptation, coincidence detection, apical basal, L5 pyramidal, zero-shot generalization, motor cortex, goal encoding
