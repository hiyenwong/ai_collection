---
name: mamba-spike-forecaster-bci
description: >
  Mamba forecaster methodology for implicit behavioral decoding from next-step spike forecasts
  at Neuropixels population scale. A single Mamba state-space model, trained only on next-step
  spike counts, delivers both neural population forecasting and behavioral state readout in one
  forward pass. Use when: building closed-loop BCI systems, neural population forecasting,
  implicit behavioral decoding from neural activity, Mamba/SSM for neuroscience,
  Neuropixels-scale analysis, spike train prediction.
  arXiv: 2605.12999 (2026-05-13)
---

# Mamba Spike Forecaster for BCI

## Core Concept

A single Mamba state-space model trained on next-step spike counts simultaneously provides:
1. **Neural population forecasting** — predicting future joint firing patterns
2. **Implicit behavioral decoding** — extracting behavioral state without separate decoder

## Architecture

```
Spike counts (t-1) → Mamba SSM → Spike forecast (t)
                                      ↓
                              Per-neuron linear probe
                                      ↓
                              Behavioral readout
```

### Key Design Choices
- Single forward pass produces both forecast and behavior readout
- Per-neuron linear probes on hidden states decode behavioral variables
- Scales to Neuropixels-scale recordings (thousands of neurons)

## Implementation Pattern

```python
import torch
import torch.nn as nn
from mamba_ssm import Mamba

class SpikeForecaster(nn.Module):
    def __init__(self, n_neurons, d_model=64, n_layers=4):
        super().__init__()
        self.input_proj = nn.Linear(n_neurons, d_model)
        self.mamba_layers = nn.ModuleList([
            Mamba(d_model=d_model, d_state=16, d_conv=4, expand=2)
            for _ in range(n_layers)
        ])
        self.spike_head = nn.Linear(d_model, n_neurons)
        
    def forward(self, spike_counts):
        x = self.input_proj(spike_counts)
        for layer in self.mamba_layers:
            x = layer(x)
        forecast = self.spike_head(x)
        return forecast
```

## Behavioral Decoding

Attach lightweight per-neuron probes to the Mamba hidden states:

```python
class BehaviorProbe(nn.Module):
    def __init__(self, d_model, n_behavioral_dims):
        super().__init__()
        self.probe = nn.Linear(d_model, n_behavioral_dims)
    
    def forward(self, hidden_states):
        return self.probe(hidden_states)
```

## SpikeProphecy Benchmark (2605.12992)

Evaluate using SpikeProphecy protocol — not just aggregate Pearson r:
- Decompose prediction quality by neuron type
- Measure temporal structure preservation
- Test generalization across sessions/animals

## When to Use

- **Closed-loop BCI**: Need both forecasting and decoding from single model
- **Neural population analysis**: Understanding joint dynamics at scale
- **Real-time applications**: Mamba's O(n) scaling enables low-latency inference
- **Multi-modal neural recordings**: Adaptable to calcium imaging, EEG

## Advantages over RNN/Transformer

| Property | RNN | Transformer | Mamba |
|----------|-----|-------------|-------|
| Scaling | O(n) | O(n²) | O(n) |
| Memory | Hidden state | KV cache | Hidden state |
| Long-range | Limited | Excellent | Excellent |
| Real-time | Yes | Limited | Yes |

## Related Skills

- `spikeprophecy-benchmark` (2605.12992)
- `neural-population-dynamics`
- `neural-digital-twins-bci`

## Activation Keywords

- mamba spike forecaster, neural population forecasting
- implicit behavioral decoding
- closed-loop BCI prediction
- Mamba SSM neuroscience
- Neuropixels scale analysis
- spike train prediction
- next-step spike forecast
