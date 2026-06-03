---
name: snn-eeg-alzheimer-biophysical-signatures
description: "Learning Alzheimer's disease biophysical signatures via EEG and Spiking Neural Networks. Combines biophysical modeling of neurodegeneration with SNN-based biomarker extraction from EEG signals. Simulates AD pathology effects on neural circuits and learns discriminative signatures. Activation: Alzheimer, EEG biomarker, spiking neural network, neurodegeneration, AD detection, biophysical simulation."
---

# SNN-EEG Alzheimer's Disease Biophysical Signature Learning

> Combines biophysical simulation of Alzheimer's disease pathology with spiking neural network (SNN) processing of EEG signals to learn discriminative biomarker signatures for AD detection.

## Metadata
- **Source**: arXiv:2602.07010
- **Authors**: Dongyu Zhou, Yanjun Li, Guojun Dai, Haifeng Chen, Jingen Liu
- **Published**: 2026-02-11
- **Category**: q-bio.NC

## Core Methodology

### Key Innovation
A dual-stage framework that bridges **biophysical modeling** and **SNN-based learning** for Alzheimer's disease detection:
1. **Forward path**: Biophysical simulation of AD pathology (synaptic loss, neuronal death, connectivity disruption) generates realistic EEG-like signals
2. **Inverse path**: SNN learns to extract discriminative signatures from both simulated and real EEG

### Technical Framework

**Stage 1: Biophysical Simulation**
- Model cortical microcircuits with conductance-based neurons
- Introduce AD-specific pathology:
  - **Amyloid-β effects**: Reduced synaptic efficacy (AMPA/NMDA receptor density decrease)
  - **Tau pathology**: Impaired axonal transport → increased transmission delays
  - **Neurodegeneration**: Progressive neuronal loss in hippocampal and cortical circuits
- Generate synthetic EEG from population activity via forward model

**Stage 2: SNN-Based Signature Learning**
- Input: Raw or preprocessed EEG signals → spike encoding (threshold-based or delta modulation)
- SNN architecture: Recurrent spiking layers with learnable synaptic delays
- Training: Surrogate gradient method optimized for AD discrimination
- Output: Learned biophysical signatures (spike timing patterns, oscillation features)

**Stage 3: Clinical Translation**
- Transfer learning from simulation to real EEG
- Biomarker extraction: Identify which biophysical parameters (synaptic strength, delay, cell count) are most discriminative
- Cross-validation on clinical AD datasets

### Key Results
- Simulated AD EEG reproduces known clinical features (slowed oscillations, reduced complexity)
- SNN learns signatures that generalize across simulation-to-real domain gap
- Biophysical interpretability: learned features map to specific AD pathology mechanisms
- Performance competitive with deep learning baselines on AD vs. healthy control classification

## Implementation Guide

### Prerequisites
- EEG datasets (e.g., AD patients + healthy controls)
- Python: Brian2 or NEST for spiking simulation, PyTorch for training
- Basic knowledge of computational neuroscience and AD pathology

### Step-by-Step
1. **Biophysical model setup**: Configure cortical column model with AD pathology parameters
2. **Synthetic data generation**: Run simulations across AD severity spectrum
3. **Spike encoding**: Convert EEG signals to spike trains (temporal coding)
4. **SNN training**: Train recurrent SNN with surrogate gradients on AD classification
5. **Signature extraction**: Analyze trained SNN to identify biophysical feature importance
6. **Clinical validation**: Apply to real EEG and evaluate classification performance

### Code Example
```python
import numpy as np
import torch
import torch.nn as nn

class ADSNNClassifier(nn.Module):
    # Spiking Neural Network for AD biomarker learning from EEG.
    
    def __init__(self, n_channels=19, n_hidden=128, n_output=2, tau=10.0):
        super().__init__()
        self.tau = tau
        self.n_hidden = n_hidden
        
        # Spike encoding layer
        self.encode = nn.Linear(n_channels, n_hidden)
        # Recurrent spiking layer
        self.recurrent = nn.Linear(n_hidden, n_hidden)
        # Readout
        self.readout = nn.Linear(n_hidden, n_output)
        
        # Surrogate gradient
        self.spike_fn = lambda x: (x > 0).float()
    
    def forward(self, eeg_sequence):
        # eeg_sequence: (batch, time, channels)
        batch_size, seq_len, _ = eeg_sequence.shape
        membrane = torch.zeros(batch_size, self.n_hidden, device=eeg_sequence.device)
        spikes = torch.zeros_like(membrane)
        outputs = []
        
        for t in range(seq_len):
            input_current = self.encode(eeg_sequence[:, t])
            recurrent_current = self.recurrent(spikes)
            
            # LIF dynamics with AD-modeled synaptic decay
            membrane = membrane * (1 - 1/self.tau) + input_current + recurrent_current
            new_spikes = self.spike_fn(membrane - 1.0)
            membrane = membrane * (1 - new_spikes)  # Reset
            
            spikes = new_spikes
            outputs.append(self.readout(spikes))
        
        # Temporal aggregation
        return torch.stack(outputs, dim=1).mean(dim=1)

# Biophysical AD simulation parameters
AD_PARAMS = {
    'synaptic_loss': [0.0, 0.15, 0.30, 0.45],  # Progressive Aβ effect
    'delay_increase': [1.0, 1.2, 1.5, 2.0],     # Tau-related delay (ms)
    'neuron_loss': [0.0, 0.05, 0.15, 0.25],     # Neurodegeneration fraction
}

def simulate_ad_eeg(params, duration=1000, dt=0.1):
    # Simplified biophysical AD EEG simulation.
    # Returns synthetic EEG signal with specified AD pathology level.
    n_neurons = 800
    alive = np.random.random(n_neurons) > params['neuron_loss']
    syn_weight = 1.0 - params['synaptic_loss']
    delay = params['delay_increase']
    
    # LIF simulation (simplified)
    v = np.random.uniform(-0.06, -0.05, n_neurons) * alive
    n_steps = int(duration / dt)
    eeg = np.zeros(n_steps)
    
    for t in range(n_steps):
        # Synaptic input with AD-modulated weight
        I = syn_weight * np.random.normal(0, 0.01, n_neurons) * alive
        v += dt * (-v/0.02 + I)
        spikes = v > -0.05
        v[spikes] = -0.065
        # Forward model: sum of spikes → scalp EEG
        eeg[t] = spikes.sum() / alive.sum()
    
    return eeg
```

## Applications
- **AD early detection**: Identify biomarkers from routine EEG recordings
- **Biomarker discovery**: Map SNN-learned features to specific AD pathology mechanisms
- **Drug trial monitoring**: Track AD progression via biophysical signature changes
- **Simulation-informed diagnosis**: Augment limited clinical data with realistic simulated AD EEG
- **Personalized medicine**: Patient-specific biophysical parameter estimation

## Pitfalls
- Biophysical model complexity vs. simulation speed tradeoff
- Simulation-to-real domain gap requires careful transfer learning
- EEG artifacts (eye blinks, muscle) can confound SNN learning
- AD is heterogeneous — single model may not capture all subtypes
- Requires careful regularization to avoid overfitting on small clinical datasets

## Related Skills
- snn-eeg-alzheimer-biophysical-signatures
- eeg-hopfield-emotion-energy
- highfidelity-networkbased-alzheimers-progression
- brain-inspired-snn-pattern-analysis
- pa-tcnet-brain-tumor-seg
