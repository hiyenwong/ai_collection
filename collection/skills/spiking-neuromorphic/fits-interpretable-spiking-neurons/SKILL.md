---
name: fits-interpretable-spiking-neurons
description: >
  FiTS (Frequency Selectivity and Temporal Shaping) interpretable spiking neuron methodology.
  Factorizes temporal computation within each spiking neuron into Frequency Selectivity (FS) 
  and Temporal Shaping (TS) modules. FS parameterizes each neuron's target frequency as the 
  maximizer of its subthreshold magnitude response, while TS reshapes when frequency components 
  contribute to membrane voltage accumulation through group-delay modulation.
  Use when: designing interpretable SNN neurons, frequency-selective spiking networks, 
  auditory/temporal processing SNNs, neuron specialization, temporal shaping in SNNs,
  group-delay modulation, subthreshold frequency response analysis.
  arXiv: 2605.13071v1 (2026-05-13)
---

# FiTS: Interpretable Spiking Neurons via Frequency Selectivity and Temporal Shaping

## Core Concept

FiTS introduces a spiking neuron that factorizes temporal computation into two complementary modules:

1. **Frequency Selectivity (FS)**: Each neuron parameterizes its target frequency as the maximizer of its subthreshold magnitude response
2. **Temporal Shaping (TS)**: Reshapes when frequency components contribute to membrane voltage through group-delay modulation

## Key Innovation

Prior SNN work improved temporal modeling through richer neuron dynamics and network-level mechanisms (recurrence, delays), but did not clarify how individual neurons should specialize. FiTS addresses this by providing each neuron with interpretable frequency-temporal specialization.

## Architecture

### FS Module
- Parameterizes target frequency `f_target` per neuron
- `f_target` = argmax of subthreshold magnitude response
- Creates frequency-selective neurons analogous to auditory filter banks

### TS Module
- Group-delay modulation controls timing of frequency contributions
- Reshapes when specific frequency bands drive membrane voltage accumulation
- Enables temporal phase alignment across neurons

## Implementation Pattern

```python
import torch
import torch.nn as nn

class FiTSNeuron(nn.Module):
    def __init__(self, dt=1e-3):
        super().__init__()
        # FS: learnable target frequency
        self.log_freq = nn.Parameter(torch.zeros(1))  # log-scale frequency
        # TS: learnable group-delay parameters
        self.delay_params = nn.Parameter(torch.zeros(1))
        
    def subthreshold_response(self, x):
        # Compute magnitude response at target frequency
        freq = torch.exp(self.log_freq)
        # Apply bandpass-like filtering
        return self.apply_frequency_selectivity(x, freq)
    
    def temporal_shaping(self, v):
        # Apply group-delay modulation
        delay = torch.sigmoid(self.delay_params) * max_delay
        return self.apply_delay_modulation(v, delay)
    
    def forward(self, x):
        v = self.subthreshold_response(x)
        v = self.temporal_shaping(v)
        spike = (v > self.threshold).float()
        return spike, v
```

## Performance

On auditory benchmarks where frequency selectivity and timing are central (e.g., speech commands, audio classification), FiTS outperforms standard LIF/ALIF neurons by leveraging interpretable frequency-temporal decomposition.

## When to Use

- **Auditory processing SNNs**: Speech recognition, sound classification
- **Temporal pattern recognition**: Where frequency content and timing matter
- **Interpretable SNN design**: When you need to understand what each neuron computes
- **Frequency-bank architectures**: Building filter-bank-like SNN structures

## Related Concepts

- LIF neurons (baseline comparison)
- ALIF (Adaptive LIF) neurons
- Group delay in signal processing
- Subthreshold membrane dynamics
- Frequency-selective neural coding

## Activation Keywords

- FiTS neuron, frequency selectivity temporal shaping
- interpretable spiking neuron
- frequency-selective SNN
- temporal shaping SNN
- group-delay spiking neuron
- subthreshold frequency response
