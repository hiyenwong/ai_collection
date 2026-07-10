---
name: rl-closed-loop-eeg-tms
description: Reinforcement learning-based closed-loop EEG-TMS system for personalized brain stimulation. Uses RL to identify individual-specific brain state markers for optimized neurostimulation.
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [neuroscience, eeg, tms, reinforcement-learning, closed-loop, brain-stimulation, personalized-medicine]
    source_paper: "A first realization of reinforcement learning-based closed-loop EEG-TMS (arXiv:2602.06907v1)"
---

# RL-Based Closed-Loop EEG-TMS

## Overview

This paper presents the **first realization of closed-loop EEG-TMS in humans** using reinforcement learning. Traditional TMS uses a one-size-fits-all approach, while brain state-dependent EEG-TMS still requires user-defined target phases. This system uses RL to **user-independently identify** the individual mu-rhythm phase associated with high vs. low corticospinal excitability, enabling personalized brain stimulation without manual parameter tuning.

## Key Insights

1. **RL-Driven Phase Identification**: Reinforcement learning discovers the optimal stimulation phase for each individual without requiring a priori target phase specification
2. **Individualized Neuroplasticity**: Repetitive stimulation of RL-identified phases produces long-term increases/decreases in functional connectivity
3. **Closed-Loop Real-Time**: System operates in real-time, continuously adapting stimulation parameters based on ongoing EEG feedback
4. **Connectivity Modulation**: Successfully modulated resting-state EEG coherence in the stimulated sensorimotor network

## Core Architecture

```
┌─────────────────────────────────────────────────┐
│         RL-Based Closed-Loop EEG-TMS            │
├─────────────────────────────────────────────────┤
│                                                 │
│  ┌───────────────────────────────────────────┐  │
│  │          Real-Time EEG Acquisition         │  │
│  │     (mu-rhythm phase extraction)           │  │
│  └──────────────────┬────────────────────────┘  │
│                     │                           │
│  ┌──────────────────▼────────────────────────┐  │
│  │        RL Agent (State → Phase)            │  │
│  │  State: current mu-rhythm phase + history   │  │
│  │  Action: select TMS stimulation phase       │  │
│  │  Reward: corticospinal excitability (MEP)   │  │
│  └──────────────────┬────────────────────────┘  │
│                     │                           │
│  ┌──────────────────▼────────────────────────┐  │
│  │        Phase-Locked TMS Stimulation        │  │
│  │  (deliver pulse at RL-selected phase)      │  │
│  └──────────────────┬────────────────────────┘  │
│                     │                           │
│  ┌──────────────────▼────────────────────────┐  │
│  │       Response Measurement (MEP/EEG)       │  │
│  │  Motor Evoked Potential + EEG coherence     │  │
│  └──────────────────┬────────────────────────┘  │
│                     │                           │
│  ┌──────────────────▼────────────────────────┐  │
│  │         RL Reward Computation              │  │
│  │  (feedback to agent for learning)           │  │
│  └────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────┘
```

## Implementation Pattern

```python
import numpy as np
from dataclasses import dataclass
from typing import Optional

@dataclass
class EEGTMSState:
    """Current brain state for RL agent."""
    mu_phase: float           # Current mu-rhythm phase (0 to 2π)
    mu_amplitude: float       # Mu-rhythm power
    phase_history: np.ndarray # Recent phase trajectory
    timestamp: float

@dataclass
class TMSAction:
    """TMS stimulation action."""
    stimulation_phase: float  # Phase at which to deliver TMS
    intensity: float          # Stimulation intensity (% of motor threshold)

class EEGTMS_RLAgent:
    """
    RL agent for closed-loop EEG-TMS stimulation.
    
    Learns to identify individual-specific mu-rhythm phases
    associated with high/low corticospinal excitability.
    """
    
    def __init__(
        self,
        n_phase_bins: int = 36,  # 10-degree resolution
        learning_rate: float = 0.1,
        exploration_rate: float = 0.3
    ):
        self.n_phase_bins = n_phase_bins
        self.lr = learning_rate
        self.epsilon = exploration_rate
        
        # Q-table: phase_bin → expected MEP response
        self.q_table = np.zeros(n_phase_bins)
        self.visit_counts = np.zeros(n_phase_bins)
        
        # Phase discretization
        self.phase_resolution = 2 * np.pi / n_phase_bins
        
        # MEP history for reward computation
        self.mep_history = []
    
    def discretize_phase(self, phase: float) -> int:
        """Convert continuous phase to discrete bin."""
        phase = phase % (2 * np.pi)
        return int(phase / self.phase_resolution) % self.n_phase_bins
    
    def select_action(self, state: EEGTMSState) -> TMSAction:
        """Select stimulation phase using epsilon-greedy policy."""
        phase_bin = self.discretize_phase(state.mu_phase)
        
        if np.random.random() < self.epsilon:
            # Explore: try random phase
            action_bin = np.random.randint(self.n_phase_bins)
        else:
            # Exploit: choose best-known phase
            action_bin = np.argmax(self.q_table)
        
        stimulation_phase = action_bin * self.phase_resolution
        return TMSAction(
            stimulation_phase=stimulation_phase,
            intensity=1.0  # 100% motor threshold
        )
    
    def update(self, state: EEGTMSState, action: TMSAction, mep_amplitude: float):
        """Update Q-values based on MEP response."""
        phase_bin = self.discretize_action(action.stimulation_phase)
        
        # Reward: normalized MEP amplitude
        if len(self.mep_history) > 0:
            baseline = np.mean(self.mep_history[-20:])
            reward = (mep_amplitude - baseline) / (baseline + 1e-10)
        else:
            reward = mep_amplitude
        
        self.mep_history.append(mep_amplitude)
        self.visit_counts[phase_bin] += 1
        
        # Q-learning update
        td_error = reward - self.q_table[phase_bin]
        self.q_table[phase_bin] += self.lr * td_error
    
    def get_optimal_phase(self) -> float:
        """Return the currently learned optimal stimulation phase."""
        optimal_bin = np.argmax(self.q_table)
        return optimal_bin * self.phase_resolution
    
    def get_phase_preference_map(self) -> np.ndarray:
        """Return full phase preference map for visualization."""
        return self.q_table.copy()
    
    def discretize_action(self, phase: float) -> int:
        """Convert action phase to bin index."""
        phase = phase % (2 * np.pi)
        return int(phase / self.phase_resolution) % self.n_phase_bins
```

## Applications

1. **Personalized TMS Therapy**: Individualized stimulation without manual phase selection
2. **Neurorehabilitation**: Stroke and motor disorder treatment optimization
3. **Brain-State Dependent Stimulation**: Phase-locked TMS for cognitive enhancement
4. **Closed-Loop BCI**: Integration with brain-computer interfaces for adaptive stimulation
5. **Neuromodulation Research**: Discovering individual-specific stimulation protocols

## Key Parameters

| Parameter | Description | Typical Range |
|-----------|-------------|---------------|
| `n_phase_bins` | Phase discretization resolution | 18-72 bins |
| `learning_rate` | RL agent learning rate | 0.01-0.2 |
| `exploration_rate` | Epsilon for exploration | 0.1-0.5 (decay) |
| `stimulation_intensity` | TMS pulse intensity | 80-120% MT |

## Activation Keywords

- closed-loop EEG-TMS
- reinforcement learning TMS
- phase-locked stimulation
- personalized neurostimulation
- mu-rhythm phase
- corticospinal excitability
- 闭环脑电经颅磁刺激
- 强化学习TMS
- 个性化神经调控

## References

- **Original Paper**: A first realization of reinforcement learning-based closed-loop EEG-TMS. arXiv:2602.06907v1 (2026)
- **Related Skills**: [[tms-eeg-biomarkers]], [[brain-stimulation-dynamics-state]], [[seizure-suppression-hub-stimulation]]

## Limitations

- Requires real-time EEG processing infrastructure
- MEP measurement needs concurrent EMG recording
- Individual learning period needed before optimal phase identification
- Safety considerations for closed-loop stimulation parameters
