---
name: fits-interpretable-spiking-neurons
description: >
  FiTS (Frequency Selectivity and Temporal Shaping) spiking neuron methodology.
  Factorizes temporal computation within individual spiking neurons into
  Frequency Selectivity (FS) and Temporal Shaping (TS) modules. Use when:
  designing interpretable spiking neurons, improving SNN temporal modeling,
  building auditory processing SNNs, analyzing frequency selectivity in neural
  networks, implementing temporal shaping in spiking models, or extending LIF
  neurons with frequency-aware dynamics. Activation: FiTS, frequency selective
  spiking neuron, temporal shaping SNN, interpretable spiking neuron, auditory
  spiking neural network, frequency selectivity neural dynamics.
---

# FiTS: Interpretable Spiking Neurons via Frequency Selectivity and Temporal Shaping

Novel spiking neuron design that factorizes temporal computation into two
interpretable components within each neuron.

## Paper Reference

- **Title**: FiTS: Interpretable Spiking Neurons via Frequency Selectivity and Temporal Shaping
- **Authors**: Jongmin Choi, Joon Son Chung
- **arXiv**: 2605.13071
- **Date**: 2026-05-13
- **Categories**: cs.NE

## Core Insight

Prior SNNs improve temporal modeling through richer neuron dynamics and
network-level mechanisms (recurrence, delays), but individual neuron
specialization remains unclear. FiTS addresses this by decomposing temporal
computation within each neuron.

## FiTS Architecture

### Two-Module Factorization

Each FiTS neuron consists of:

1. **Frequency Selectivity (FS) Module**
   - Parameterizes each neuron's target frequency
   - Target frequency = maximizer of subthreshold magnitude response
   - Each neuron "tunes" to a specific frequency band

2. **Temporal Shaping (TS) Module**
   - Reshapes when frequency components contribute to membrane voltage
   - Modulates through group-delay control
   - Controls timing of frequency contributions to spike generation

### Key Innovation

Unlike LIF neurons with fixed dynamics, FiTS neurons learn:
- **What** frequency to respond to (FS)
- **When** that frequency contributes to spiking (TS)

## Performance Results

### Auditory Benchmarks
- Consistently improves over plain LIF baseline in simple feedforward SNNs
- No recurrence or network-level delays required
- Competitive with strong temporal SNN baselines

### Interpretability
- Learned target frequencies provide neuron-level summaries of frequency organization
- Group-delay shifts reveal timing structure learned by the network
- Each neuron's role can be understood through its (frequency, delay) parameters

## Implementation Pattern

```python
# Conceptual FiTS neuron structure
class FiTSNeuron:
    def __init__(self, num_freq_bands):
        # FS module: learnable target frequencies
        self.target_freqs = nn.Parameter(torch.randn(num_freq_bands))
        # Subthreshold magnitude response
        self.magnitude_response = None
        
        # TS module: learnable group delays
        self.group_delays = nn.Parameter(torch.zeros(num_freq_bands))
        
    def forward(self, input_signal):
        # FS: filter input by target frequencies
        freq_components = self.frequency_selective_filter(input_signal)
        
        # TS: apply group-delay modulation
        shaped_components = self.temporal_shape(freq_components)
        
        # Membrane integration with shaped components
        membrane_voltage = self.integrate(shaped_components)
        
        # Spike generation
        spike = self.fire(membrane_voltage)
        return spike
```

## Comparison with Other SNN Neurons

| Neuron Type | Temporal Mechanism | Interpretability | Recurrence Required |
|-------------|-------------------|------------------|---------------------|
| LIF | Fixed decay | Low | Often needed |
| ALIF | Adaptive threshold | Medium | Often needed |
| Delay-SNN | Network-level delays | Low | Required |
| **FiTS** | **Per-neuron FS+TS** | **High** | **No** |

## When to Use This Skill

- Designing interpretable spiking neurons for temporal tasks
- Building auditory processing pipelines with SNNs
- Improving SNN performance without recurrence
- Analyzing what frequencies/timings SNN neurons learn
- Extending LIF neurons with frequency-aware dynamics
- Comparing neuron-level temporal computation strategies

## Related Skills

- `spiking-neural-network-analysis` - General SNN paper analysis
- `spikingjelly-framework` - SNN implementation framework
- `surrogate-gradient-snn-training` - SNN training methodology
- `spiking-bandpass-wavelet-encoding` - Frequency-based spike encoding
- `predictive-coding-light` - Sequence prediction with STDP
