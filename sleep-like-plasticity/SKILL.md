---
name: sleep-like-plasticity
description: "Biologically inspired sleep-like plasticity for spiking neural networks with thalamo-cortical architecture. Alternates wake-like learning and sleep-like consolidation phases. Enables memory consolidation, energetic downshift, and improved classification. Activation: sleep-like plasticity, sleep consolidation, thalamocortical spiking, wake-sleep cycle, memory consolidation SNN, energy-efficient learning, dendritic integration"
---

# Sleep-like Plasticity in Thalamo-Cortical Spiking Networks

## Overview

Sleep supports memory consolidation and recovery of optimal energetic regime by reorganizing synaptic connectivity. This skill implements a biologically inspired spiking multi-layer network that alternates between wake-like and deep-sleep-like states, with state-dependent dendritic integration and synaptic plasticity in a thalamo-cortical framework.

## Source Paper

- **arXiv:** 2601.17523
- **Title:** Sleep-like consolidation of memory and energy efficiency in a spiking thalamo-cortical model
- **Published:** January 2026
- **Categories:** q-bio.NC, cs.NE

## Core Concepts

### Wake-Sleep Alternation
- **Wake phase:** Network learns from few perceived examples using sensory input
- **Sleep phase:** Spontaneous replay driven by slow oscillations consolidates memories
- **Key insight:** Full inter-layer plasticity (intra + inter) yields higher post-sleep accuracy than restricted plasticity

### State-Dependent Dendritic Integration
- Different dendritic integration rules during wake vs sleep
- Wake: feedforward-dominated processing of sensory stimuli
- Sleep: recurrent-dominated spontaneous replay with slow oscillations

### Energetic Downshift
- Sleep phase promotes synaptic homeostasis
- Reduces overall energy consumption while preserving/consolidating memories
- Full plasticity leads to sharper class-specific associations post-sleep

### Memory Consolidation Mechanism
1. **Encoding:** During wake, sparse examples create initial memory traces
2. **Replay:** During sleep, spontaneous slow oscillations reactivate patterns
3. **Consolidation:** Inter-layer plasticity strengthens relevant connections
4. **Downscaling:** Global synaptic downshift preserves signal-to-noise ratio

## Implementation

```python
import numpy as np
from typing import Tuple

class ThalamoCorticalSleepNetwork:
    """
    Spiking thalamo-cortical network with wake-sleep alternation.
    
    Architecture:
    - Thalamus (input layer) → Cortex (hidden layer) → Output layer
    - State-dependent dendritic integration
    - Inter-layer and intra-layer plasticity
    """
    
    def __init__(self, n_thalamus=64, n_cortex=128, n_output=10):
        # Network dimensions
        self.n_thalamus = n_thalamus
        self.n_cortex = n_cortex
        self.n_output = n_output
        
        # Weights (thalamus → cortex → output)
        self.W_tc = np.random.randn(n_thalamus, n_cortex) * 0.1
        self.W_co = np.random.randn(n_cortex, n_output) * 0.1
        
        # Recurrent connections (cortex)
        self.W_cc = np.random.randn(n_cortex, n_cortex) * 0.05
        np.fill_diagonal(self.W_cc, 0)
        
        # Inter-layer plasticity weights
        self.W_inter = np.random.randn(n_thalamus, n_cortex) * 0.01
        
        # Membrane potentials
        self.V_thalamus = np.zeros(n_thalamus)
        self.V_cortex = np.zeros(n_cortex)
        self.V_output = np.zeros(n_output)
        
        # Threshold and reset
        self.threshold = 1.0
        self.reset_potential = 0.0
        
        # State
        self.state = 'wake'  # 'wake' or 'sleep'
        self.spike_history = []
    
    def set_state(self, state: str):
        """Switch between wake and sleep states."""
        self.state = state
        if state == 'sleep':
            # Activate slow oscillations
            self._init_slow_oscillations()
    
    def _init_slow_oscillations(self):
        """Initialize slow oscillation dynamics for sleep state."""
        self.slow_oscillation_phase = 0.0
        self.slow_oscillation_freq = 0.5  # Hz
        self.up_state_threshold = 0.3
    
    def _slow_oscillation_drive(self, t: float) -> np.ndarray:
        """Generate slow oscillation input during sleep."""
        phase = self.slow_oscillation_phase
        # Up-state / down-state alternation
        oscillation = np.sin(2 * np.pi * self.slow_oscillation_freq * t + phase)
        
        # Rectified: up states are positive, down states near zero
        drive = np.maximum(oscillation, 0) * 2.0
        return np.full(self.n_cortex, drive)
    
    def dendritic_integration(self, feedforward: np.ndarray, 
                                recurrent: np.ndarray, 
                                inter_layer: np.ndarray) -> np.ndarray:
        """
        State-dependent dendritic integration.
        
        Wake: feedforward-dominated
        Sleep: recurrent + inter-layer dominated (spontaneous replay)
        """
        if self.state == 'wake':
            # Feedforward dominates during wake
            return 0.7 * feedforward + 0.2 * recurrent + 0.1 * inter_layer
        else:
            # Recurrent and inter-layer dominate during sleep
            return 0.2 * feedforward + 0.5 * recurrent + 0.3 * inter_layer
    
    def step(self, stimulus: np.ndarray = None, t: float = 0) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        One simulation step.
        
        Args:
            stimulus: External input (required for wake, optional for sleep)
            t: Current time step
        
        Returns:
            Spikes from thalamus, cortex, and output layers
        """
        # Update membrane potentials
        if self.state == 'wake' and stimulus is not None:
            self.V_thalamus += stimulus * 0.5
            feedforward = self.V_thalamus @ self.W_tc
            recurrent = self.V_cortex @ self.W_cc
            inter_layer = self.V_thalamus @ self.W_inter
        else:
            # Sleep: spontaneous activity driven by slow oscillations
            sleep_drive = self._slow_oscillation_drive(t)
            feedforward = np.zeros(self.n_cortex)
            recurrent = self.V_cortex @ self.W_cc + sleep_drive
            inter_layer = self.V_thalamus @ self.W_inter
        
        # Dendritic integration
        cortex_input = self.dendritic_integration(feedforward, recurrent, inter_layer)
        self.V_cortex += cortex_input * 0.1
        
        # Output layer
        self.V_output += self.V_cortex @ self.W_co * 0.1
        
        # Spike generation
        thalamus_spikes = (self.V_thalamus >= self.threshold).astype(float)
        cortex_spikes = (self.V_cortex >= self.threshold).astype(float)
        output_spikes = (self.V_output >= self.threshold).astype(float)
        
        # Reset spiked neurons
        self.V_thalamus *= (1 - thalamus_spikes)
        self.V_cortex *= (1 - cortex_spikes)
        self.V_output *= (1 - output_spikes)
        
        # Store spike history for replay
        if self.state == 'sleep':
            self.spike_history.append(cortex_spikes.copy())
        
        return thalamus_spikes, cortex_spikes, output_spikes
    
    def apply_plasticity(self, pre_spikes: np.ndarray, post_spikes: np.ndarray, 
                         state: str, lr: float = 0.001):
        """
        Apply synaptic plasticity with state-dependent rules.
        
        Wake: Hebbian learning (input-driven)
        Sleep: Homeostatic + consolidation (replay-driven)
        """
        if state == 'wake':
            # Hebbian-like: strengthen co-active connections
            self.W_tc += lr * np.outer(pre_spikes, post_spikes)
            self.W_co += lr * np.outer(pre_spikes, post_spikes)
        else:
            # Sleep: consolidate and downscale
            # Strengthen frequently replayed patterns
            if len(self.spike_history) > 1:
                avg_activity = np.mean(self.spike_history[-10:], axis=0)
                self.W_tc *= 0.95  # Global downscaling
                self.W_co *= 0.95
                # Strengthen connections for active patterns
                self.W_tc += lr * np.outer(pre_spikes, avg_activity) * 2.0
    
    def run_wake_sleep_cycle(self, n_wake_steps: int = 100, 
                              n_sleep_steps: int = 200,
                              stimuli: np.ndarray = None) -> dict:
        """
        Run one complete wake-sleep cycle.
        
        Returns metrics on memory performance and energy consumption.
        """
        metrics = {'wake_energy': 0, 'sleep_energy': 0, 
                   'wake_accuracy': 0, 'sleep_accuracy': 0}
        
        # Wake phase
        self.set_state('wake')
        self.spike_history = []
        for t in range(n_wake_steps):
            stim = stimuli[t % len(stimuli)] if stimuli is not None else np.random.rand(self.n_thalamus)
            th_sp, cx_sp, out_sp = self.step(stim, t)
            self.apply_plasticity(th_sp, cx_sp, 'wake')
            metrics['wake_energy'] += np.sum(cx_sp)
        
        # Sleep phase
        self.set_state('sleep')
        for t in range(n_sleep_steps):
            th_sp, cx_sp, out_sp = self.step(None, t)
            self.apply_plasticity(th_sp, cx_sp, 'sleep')
            metrics['sleep_energy'] += np.sum(cx_sp)
        
        return metrics


# Usage example
if __name__ == '__main__':
    # Create network
    net = ThalamoCorticalSleepNetwork(n_thalamus=32, n_cortex=64, n_output=10)
    
    # Generate stimuli (one-hot encoded patterns)
    n_patterns = 5
    stimuli = np.eye(n_patterns, 32)  # 5 patterns, each 32-dimensional
    
    # Run multiple wake-sleep cycles
    for cycle in range(5):
        metrics = net.run_wake_sleep_cycle(
            n_wake_steps=50,
            n_sleep_steps=100,
            stimuli=stimuli
        )
        print(f"Cycle {cycle+1}: "
              f"Wake energy={metrics['wake_energy']:.1f}, "
              f"Sleep energy={metrics['sleep_energy']:.1f}")
```

## Applications

### 1. Energy-Efficient Continual Learning
Use sleep-like consolidation to periodically reorganize learned representations without catastrophic forgetting. Run sleep cycles after accumulating new data.

### 2. Memory-Compressed SNN Training
Train SNNs with alternating wake-sleep phases. Wake phases learn from data, sleep phases consolidate and compress memories through global synaptic downscaling.

### 3. Biologically Plausible Offline Processing
Implement sleep-like replay in edge devices for offline model improvement without requiring new training data.

## Key Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| Slow oscillation freq | 0.5-1 Hz | Controls sleep replay rhythm |
| Inter-layer plasticity lr | 0.001-0.01 | Memory consolidation strength |
| Global downscaling factor | 0.95 | Synaptic homeostasis |
| Wake:Sleep ratio | 1:2 to 1:4 | Learning vs consolidation balance |

## Related Skills

- [[spiking-neural-network-training]]
- [[morphsnn-structural-plasticity]]
- [[neuron-dropin-neuroplasticity]]
- [[multi-plasticity-snn-training]]
- [[context-selective-multimodal-memory]]

## Activation Keywords
- sleep-like plasticity
- sleep consolidation SNN
- thalamocortical spiking network
- wake-sleep cycle learning
- memory consolidation spiking neural network
- energy-efficient learning SNN
- dendritic integration state-dependent
- slow oscillation replay
- synaptic homeostasis spiking
- inter-layer plasticity
