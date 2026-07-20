---
name: fits-interpretable-spiking-neurons
description: "FiTS (Frequency Selectivity and Temporal Shaping) spiking neuron methodology for interpretable SNN temporal processing. Factorizes neuron-level temporal computation into Frequency Selectivity (FS) and Temporal Shaping (TS) modules. FS parameterizes target frequency as maximizer of subthreshold magnitude response; TS reshapes when frequency components contribute to membrane voltage accumulation through group-delay modulation. Use when: designing interpretable SNNs for audio/temporal tasks, frequency-selective spiking neurons, temporal shaping in SNNs, neuron-level frequency specialization, group-delay modulation in spiking models. Activation: FiTS, frequency selectivity spiking, temporal shaping SNN, interpretable spiking neuron, frequency-specialized neuron, group-delay spiking."
---

# FiTS: Interpretable Spiking Neurons via Frequency Selectivity and Temporal Shaping

> Spiking neuron that factorizes temporal computation into Frequency Selectivity (FS) and Temporal Shaping (TS) modules, enabling interpretable neuron-level frequency and timing specialization without recurrence or network-level delays.

## Metadata
- **Source**: arXiv:2605.13071
- **Authors**: Jongmin Choi, Joon Son Chung (KAIST)
- **Published**: 2026-05-12

## Core Methodology

### Key Innovation

FiTS makes each neuron's frequency preference and response timing **explicit and learnable** through two factorized modules:

1. **Frequency Selectivity (FS)**: Parameterizes each neuron's target frequency as the maximizer of its subthreshold magnitude response, using a closed-form inverse mapping from target frequency to adaptation strength.

2. **Temporal Shaping (TS)**: Controls when frequency-specific input responses contribute to spike generation through group-delay modulation — distinct from network-level synaptic delays that control when emitted spikes reach downstream neurons.

### Technical Framework

**FS Module — Frequency-Domain Parameterization:**
- Each neuron has a learnable `target_frequency` parameter
- FS maps target frequency → adaptation strength via closed-form inverse
- Subthreshold magnitude response peaks at target frequency
- Enables frequency-domain initialization, learning, and post-training interpretation in the same coordinate system
- Motivated by intrinsic neuronal resonance (neurons respond selectively to inputs at preferred frequencies)

**TS Module — Group-Delay Modulation:**
- Modulates group delay to reshape when frequency components contribute to membrane voltage accumulation
- Operates within a single neuron (pre-spike), not at network level
- Unlike synaptic delays (when spikes arrive downstream), TS controls when input frequency components affect spike generation
- Provides learned group-delay shifts as interpretable timing summaries

### Architecture

```
Input → FS Module (frequency filtering) → TS Module (temporal reshaping) → LIF Spiking → Output
```

- Works in **simple feedforward SNNs** — no recurrence or network-level delays needed
- Compatible with surrogate gradient training
- Parameters are readable post-training: `target_frequency` and `group_delay` per neuron

## Implementation Guide

### Prerequisites
- PyTorch + SpikingJelly or custom SNN framework
- Surrogate gradient support for spike training

### Step-by-Step

1. **Initialize FS Module**: Set initial target frequencies (can be uniformly distributed or informed by input spectrum)
2. **Compute adaptation strength**: Use closed-form inverse from target frequency to FS parameter
3. **Apply TS Module**: Modulate group delay for temporal reshaping of frequency component contributions
4. **Integrate with LIF neuron**: Combine FS+TS outputs with standard LIF membrane dynamics
5. **Train with surrogate gradients**: Standard backpropagation through surrogate spike function
6. **Interpret post-training**: Read learned `target_frequency` and `group_delay` per neuron

### Code Pattern

```python
import torch
import torch.nn as nn

class FiTSNeuron(nn.Module):
    """Frequency Selectivity + Temporal Shaping spiking neuron."""
    
    def __init__(self, n_neurons, fs_init_freqs=None):
        super().__init__()
        # FS: learnable target frequencies
        if fs_init_freqs is not None:
            self.target_freq = nn.Parameter(torch.tensor(fs_init_freqs))
        else:
            self.target_freq = nn.Parameter(torch.rand(n_neurons))
        
        # TS: learnable group delays
        self.group_delay = nn.Parameter(torch.zeros(n_neurons))
        
        # LIF parameters
        self.tau = nn.Parameter(torch.ones(n_neurons) * 0.5)
        
    def fs_magnitude_response(self, freq):
        """Subthreshold magnitude response peaking at target frequency."""
        # freq: tensor of input frequencies
        # Returns magnitude response for each neuron at each frequency
        delta = freq - self.target_freq.unsqueeze(-1)
        # Bandpass-like response centered at target_freq
        return torch.exp(-delta**2 / (2 * 0.1**2))
    
    def ts_group_delay(self):
        """Apply group-delay modulation to reshape temporal contributions."""
        return self.group_delay
    
    def forward(self, x, h=None):
        # x: input spectrogram or time-frequency representation
        # Apply FS filtering + TS temporal reshaping + LIF spiking
        mag = self.fs_magnitude_response(x)
        delay = self.ts_group_delay()
        # ... surrogate gradient LIF integration
        return spikes, new_h
```

## Applications

- **Audio classification**: Speech recognition, sound event detection, music genre classification
- **Temporal sequence processing**: Event-based vision, time-series forecasting
- **Neuromorphic audio processing**: Deploy on event-based audio sensors (e.g., cochlear implants, silicon cochleas)
- **Interpretable SNN analysis**: Understanding frequency/timing organization learned by SNN networks
- **Frequency-specialized network design**: Building SNNs with known frequency response properties

## Pitfalls

- **Requires frequency-structured input**: FS module needs time-frequency input (spectrograms, wavelet coefficients) — not suitable for raw time-series without frequency decomposition
- **Feedforward-only benefit**: The main advantage is in feedforward SNNs; recurrent SNNs may already capture temporal structure through network dynamics
- **Closed-form inverse**: The FS → adaptation strength mapping requires analytical derivation; may not generalize to all neuron models
- **Group-delay vs synaptic delay**: TS operates within-neuron; don't confuse with inter-neuron synaptic delay mechanisms
- **Surrogate gradient dependency**: Training requires surrogate gradients for spike non-differentiability

## Related Skills

- frequency-matching-snn-mmwave
- spiking-bandpass-wavelet-encoding
- rhythm-snn-temporal-processing
- convolution-delay-learning-snn
- stdp-synaptic-delay-learning
- multi-timescale-conductance-snn
- snn-learning-survey
