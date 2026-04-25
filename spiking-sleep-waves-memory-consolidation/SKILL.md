---
name: spiking-sleep-waves-memory-consolidation
description: "Spiking neural network modeling of sleep-related brain waves (spindles, slow oscillations, theta-gamma coupling) for understanding memory consolidation mechanisms. Applies to brain simulation, sleep disorder modeling, neuromorphic memory systems, cognitive AI. 触发词: sleep brain waves, spindles, slow oscillations, theta-gamma coupling, spiking sleep model, memory consolidation SNN, thalamocortical, hippocampal"
---

# Spiking Sleep Waves and Memory Consolidation

## Source Papers
- **Primary:** Chen, X. et al. (2026). "Spiking Neural Network Modeling of Sleep Brain Waves." *Brain Research*, arXiv:2604.05157v1
- **Supporting:** Wei, Y. et al. (2026). "Spatiotemporal Dynamics of Spindle and Slow Oscillation Interactions in a Large-Scale Thalamocortical Model." arXiv:2604.06970v1

## Overview

Sleep brain waves — spindles, slow oscillations, theta-gamma coupling — are not mere epiphenomena but **computational mechanisms** for memory consolidation. Spiking neural network models reveal how these oscillations emerge from neural circuit dynamics and coordinate information transfer between hippocampus and cortex during sleep. This skill provides the SNN modeling framework for simulating and analyzing sleep-related neural dynamics.

## Core Concepts

### 1. Sleep-Related Brain Waves

| Wave Type | Frequency | Sleep Stage | Origin | Function |
|-----------|-----------|-------------|--------|----------|
| Slow Oscillation (SO) | 0.5-1 Hz | NREM (SWS) | Neocortex | Global coordination, memory prioritization |
| Sleep Spindle | 10-16 Hz | NREM Stage 2 | Thalamus | Memory transfer window, synaptic plasticity |
| Delta Wave | 1-4 Hz | NREM (SWS) | Thalamocortical | Deep sleep maintenance |
| Theta | 4-8 Hz | REM, NREM | Hippocampus | Memory encoding/retrieval coordination |
| Gamma | 30-100 Hz | REM, Wake | Cortex | Feature binding, local processing |

### 2. SO-Spindle-SWR Triple Coupling

The most critical discovery in sleep memory research is the precise temporal coupling:

```python
# Model of SO-spindle-SWR coupling for memory consolidation
class SleepCouplingModel:
    """Computational model of triple coupling during sleep."""
    
    def __init__(self):
        self.so_phase = 0  # Slow oscillation phase (0 to 2π)
        self.spindle_times = []  # Times of spindle events
        self.swr_times = []  # Times of sharp wave ripples
        
    def generate_coupled_activity(self, duration_s=10, dt=0.001):
        """Generate realistically coupled sleep oscillations."""
        t = 0
        so_phase = 0
        so_frequency = 0.8  # Hz
        
        events = []
        
        while t < duration_s:
            so_phase += 2 * so_frequency * dt * 3.14159
            
            # SO up-state triggers spindle probability
            so_amplitude = np.sin(so_phase)
            
            if so_amplitude > 0.5:  # During up-state
                # Spindle probability increases during SO up-state
                if np.random.random() < 0.02:  # Spindle initiation
                    spindle = self._generate_spindle(t)
                    events.append(('spindle', t, spindle))
                    
                    # SWR probability increases during spindle
                    if np.random.random() < 0.15:
                        swr = self._generate_swr(t)
                        events.append(('swr', t, swr))
            
            t += dt
            
        return events
    
    def _generate_spindle(self, start_time, duration=0.5, freq=12):
        """Generate a spindle event (sigma band burst)."""
        t = np.arange(0, duration, 0.001)
        # Waxing and waning envelope
        envelope = np.sin(np.pi * t / duration)
        signal = envelope * np.sin(2 * np.pi * freq * t)
        return signal
    
    def _generate_swr(self, start_time, duration=0.1, freq=180):
        """Generate a sharp wave ripple event."""
        t = np.arange(0, duration, 0.001)
        signal = np.sin(2 * np.pi * freq * t)
        return signal
```

### 3. Thalamocortical Model of Spindles

Sleep spindles emerge from thalamic reticular nucleus (TRN) — thalamocortical (TC) loop dynamics:

```python
# Simplified thalamocortical spindle generation
class ThalamocorticalSpindle:
    """Two-population model of thalamic spindle generation."""
    
    def __init__(self):
        # Thalamic reticular nucleus (inhibitory)
        self.trn_activity = 0
        # Thalamocortical relay cells (excitatory)
        self.tc_activity = 0
        
        # Connection weights
        self.trn_to_tc = -0.8  # GABAergic inhibition
        self.tc_to_trn = 0.6   # Glutamatergic excitation
        
        # Intrinsic currents
        self.IT_trn = 0  # T-type Ca2+ current (TRN)
        self.IT_tc = 0   # T-type Ca2+ current (TC)
        
    def step(self, dt=0.001, cortical_input=0):
        """One simulation step."""
        # T-type calcium currents generate rebound bursts
        self.IT_trn = self._t_current(self.trn_activity)
        self.IT_tc = self._t_current(self.tc_activity)
        
        # Update TRN
        trn_input = (self.tc_to_tc_to_trn * self.tc_activity + 
                    cortical_input)
        self.trn_activity = self._neuron_update(trn_input, self.IT_trn)
        
        # Update TC
        tc_input = self.trn_to_tc * self.trn_activity
        self.tc_activity = self._neuron_update(tc_input, self.IT_tc)
        
        return self.tc_activity  # Spindle output
    
    def _t_current(self, activity):
        """T-type calcium current — key for spindle generation."""
        # Low-threshold Ca2+ spike when hyperpolarized
        if activity < -0.5:
            return 1.0  # De-inactivated, ready to burst
        return 0.0
    
    def _neuron_update(self, input_current, t_current):
        """Simplified neuron update with T-current."""
        return np.tanh(input_current + t_current)
```

### 4. Hippocampal CA3-CA1 Network During Sleep

```python
# Hippocampal network generating SWRs
class HippocampalSWRNetwork:
    """CA3-CA1 network model for sharp wave ripple generation."""
    
    def __init__(self, n_ca3=100, n_ca1=100):
        self.n_ca3 = n_ca3
        self.n_ca1 = n_ca1
        
        # CA3 recurrent connections (auto-associative)
        self.W_ca3 = np.random.randn(n_ca3, n_ca3) * 0.1
        np.fill_diagonal(self.W_ca3, 0)
        
        # CA3→CA1 Schaffer collateral
        self.W_ca3_ca1 = np.random.randn(n_ca3, n_ca1) * 0.2
        
        # CA1 inhibitory interneurons
        self.n_inhib = 20
        self.W_ca1_inhib = np.random.randn(n_ca1, self.n_inhib) * 0.3
        
    def generate_swr(self, stored_pattern):
        """Generate sharp wave ripple from stored pattern replay."""
        # CA3 spontaneous activation of stored pattern
        ca3_activity = stored_pattern.copy()
        
        # Recurrent amplification in CA3
        for _ in range(5):  # Iterations during SWR
            ca3_input = self.W_ca3 @ ca3_activity
            ca3_activity = np.tanh(ca3_input)
            ca3_activity = np.clip(ca3_activity, 0, 1)
        
        # CA1 activation (the ripple)
        ca1_activity = self.W_ca3_ca1.T @ ca3_activity
        ca1_activity = np.tanh(ca1_activity)
        
        return ca3_activity, ca1_activity
```

### 5. Theta-Gamma Coupling

Theta-gamma phase-amplitude coupling is critical for memory encoding and retrieval:

```python
# Theta-gamma PAC model
def theta_gamma_coupling(theta_phase, n_gamma=5):
    """
    Model theta-gamma phase-amplitude coupling.
    
    Gamma oscillations are nested within theta cycles,
    with each gamma cycle encoding one item.
    ~7 items per theta cycle (Miller's 7±2).
    """
    gamma_signals = []
    for i in range(n_gamma):
        # Each gamma cycle at different theta phase
        gamma_phase = (i / n_gamma) * 2 * np.pi
        gamma_amplitude = np.sin(theta_phase + gamma_phase)
        gamma_amplitude = max(0, gamma_amplitude)  # Rectified
        gamma_signals.append(gamma_amplitude)
    
    return gamma_signals
```

### 6. Sleep-Dependent Synaptic Plasticity

```python
class SleepSynapticPlasticity:
    """Synaptic changes during sleep for memory consolidation."""
    
    def __init__(self, synapses):
        self.synapses = synapses  # Dictionary of {pre, post: weight}
        
    def apply_stdp_during_spindle(self, pre_spikes, post_spikes):
        """
        Spike-timing-dependent plasticity during spindles.
        
        Spindles provide optimal timing windows for LTP/LTD.
        """
        delta_weights = {}
        
        for (pre, post), weight in self.synapses.items():
            # Find spike time differences during spindle
            for t_pre in pre_spikes:
                for t_post in post_spikes:
                    dt = t_post - t_pre
                    
                    if 0 < dt < 0.02:  # LTP window (pre before post)
                        delta = 0.01 * np.exp(-dt / 0.01)
                        delta_weights[(pre, post)] = delta_weights.get(
                            (pre, post), 0) + delta
                    elif -0.02 < dt < 0:  # LTD window (post before pre)
                        delta = -0.005 * np.exp(dt / 0.01)
                        delta_weights[(pre, post)] = delta_weights.get(
                            (pre, post), 0) + delta
        
        # Apply accumulated changes
        for key, delta in delta_weights.items():
            self.synapses[key] += delta
            self.synapses[key] = np.clip(self.synapses[key], 0, 1)
        
        return delta_weights
    
    def synaptic_downscaling(self, factor=0.8):
        """
        Global synaptic downscaling during slow-wave sleep.
        
        Implements Synaptic Homeostasis Hypothesis (SHY):
        All synapses are scaled down, but strong synapses 
        (important memories) survive proportionally.
        """
        for key in self.synapses:
            # Nonlinear downscaling — strong synapses resist
            w = self.synapses[key]
            self.synapses[key] = w * (factor + (1 - factor) * w)
```

## Implementation Workflow

```
1. Build thalamocortical model → Generate spindles
2. Build hippocampal CA3-CA1 → Generate SWRs
3. Couple SO-spindle-SWR → Realistic sleep dynamics
4. Store waking patterns → Encode memories in CA3
5. Run sleep simulation → Replay memories during SWRs
6. Measure consolidation → Track cortical weight changes
7. Analyze coupling → SO-spindle-SWR timing statistics
```

## Key Parameters

| Parameter | Biological Range | Modeling Value |
|-----------|-----------------|----------------|
| SO frequency | 0.5-1 Hz | 0.8 Hz |
| Spindle frequency | 10-16 Hz | 12 Hz |
| SWR frequency | 150-250 Hz | 180 Hz |
| Spindle duration | 0.5-2 s | 0.5-1.0 s |
| SWR duration | 50-200 ms | 100 ms |
| Theta frequency | 4-8 Hz | 6 Hz |
| Gamma frequency | 30-100 Hz | 40 Hz |

## Applications

1. **Sleep disorder modeling:** Insomnia, sleep apnea, narcolepsy
2. **Memory enhancement:** Targeted memory reactivation (TMR) during sleep
3. **Neuromorphic systems:** Offline consolidation in spiking AI
4. **Brain-computer interfaces:** Decoding memory states from sleep EEG
5. **Drug development:** Testing sleep-modulating compounds in silico

## References

- Chen, X. et al. (2026). "Spiking Neural Network Modeling of Sleep Brain Waves." *Brain Research*. arXiv:2604.05157v1
- Wei, Y. et al. (2026). "Spatiotemporal Dynamics of Spindle and Slow Oscillation Interactions." arXiv:2604.06970v1
- Destexhe, A. et al. (1999). "Thalamic Spindle Generation." *Journal of Neurophysiology*.
- Tononi, G., Cirelli, C. (2014). "Sleep and the Price of Plasticity." *Neuron*, 81(1), 12-34.

## Related Skills
- [[hippocampal-reactivation-memory-consolidation]]
- [[computational-neuroscience-models]]
- [[adaptive-spiking-neurons-asn]]
- [[neural-dynamics-criticality]]
