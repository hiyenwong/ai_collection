---
name: learning-sequence-timing-snn
description: "Learning sequence timing and control of replay speed in networks of spiking neurons — biologically plausible SNN sequence learning mechanism using spiking Temporal Memory (sTM) with element-specific timing encoding via sequential population activation and oscillatory clock control of replay speed. arXiv: 2605.22523"
tags: [snn, spiking-neural-network, sequence-learning, timing, replay, temporal-memory, oscillatory-control, biological-plausibility]
arxiv_id: "2605.22523"
date: "2026-05-21"
---

# Learning Sequence Timing and Replay Speed in SNNs

## Paper Reference

**Title:** Learning sequence timing and control of replay speed in networks of spiking neurons
**Authors:** Melissa Lober, Younes Bouhadjar, Markus Diesmann, Tom Tetzlaff
**arXiv:** 2605.22523 (May 21, 2026)
**Category:** q-bio.NC (Neurons and Cognition)

## Abstract Summary

Processing sequential inputs is a fundamental brain function underlying sensory perception, language, and motor control. The spiking Temporal Memory (sTM) model is a biologically inspired SNN framework for sequence processing. This work extends sTM to learn not just the **order** of sequence elements but their **precise timing**, and introduces a mechanism for flexibly controlling **replay speed** via oscillatory background input.

## Core Innovations

### 1. Element-Specific Duration Encoding

Each sequence element's duration is encoded by sequential activation of **element-specific neuronal populations**:

```
Element A ─► Population A₁ → A₂ → A₃ → ... → Aₙ
             ↑                  ↑                    ↑
             t=0ms             t=100ms              t=200ms
```

- Each element recruits a dedicated chain of neurons
- The chain length determines the duration of that element
- Spike timing within the chain encodes the passage of time
- Enables encoding across wide range of timescales (ms to seconds)

### 2. Oscillatory Clock for Replay Speed Control

Background oscillatory inputs serve as a clock signal:

```
Normal replay (θ rhythm, ~8 Hz):
    Input:  [A] [B] [C] [D] [E]
    ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐
    │ │ │ │ │ │ │ │ │ │ │ │ │ │
    └─┘ └─┘ └─┘ └─┘ └─┘ └─┘ └─┘

Compressed replay (γ rhythm, ~40 Hz):
    Input:  [A][B][C][D][E]
    ┌┐┌┐┌┐┌┐┌┐┌┐┌┐┌┐
    ││││││││││││││││
    └┘└┘└┘└┘└┘└┘└┘└┘
```

- Oscillation frequency modulates replay speed
- θ rhythm (~4-8 Hz): Slow replay during wakefulness
- γ rhythm (~30-80 Hz): Fast replay, possibly during sleep
- Links to known EEG/LFP oscillatory patterns

### 3. Sequence Replay During Different Brain States

| Brain State | Oscillation | Replay Speed | Function |
|------------|-------------|--------------|----------|
| Wakefulness | θ (4-8 Hz) | Slow | Deliberate recall |
| SWS Sleep | δ/θ | Slow | Memory consolidation |
| REM Sleep | γ (30-80 Hz) | Fast | Novel associations |
| Sharp-wave ripples | 150-200 Hz | Extremely fast | Hippocampal replay |

## spiking Temporal Memory (sTM) Architecture

### Neuron Model

LIF neurons with:
- Membrane time constant τ_m
- Refractory period
- Adaptive threshold (for sequence separation)

### Synaptic Organization

```
┌─────────────────────────────────────────────────┐
│               Sequence Layers                    │
│                                                   │
│  Layer 1: Input encoding                          │
│  ┌───────────────────────────────────────────┐   │
│  │ Item A: [A₁][A₂]...[Aₙ]                   │   │
│  │ Item B: [B₁][B₂]...[Bₙ]                   │   │
│  └───────────────────────────────────────────┘   │
│         │ Synfire chain connections                │
│         ▼                                         │
│  Layer 2: Timing encoding                         │
│  ┌───────────────────────────────────────────┐   │
│  │ Duration populations                       │   │
│  │ ┌─────┐ ┌─────┐ ┌─────┐                  │   │
│  │ │ t₁  │→│ t₂  │→│ t₃  │→...              │   │
│  │ └─────┘ └─────┘ └─────┘                  │   │
│  └───────────────────────────────────────────┘   │
│         │ Oscillatory gating                      │
│         ▼                                         │
│  Layer 3: Replay control                          │
│  ┌───────────────────────────────────────────┐   │
│  │ Oscillation frequency × input gain        │   │
│  └───────────────────────────────────────────┘   │
└─────────────────────────────────────────────────┘
```

## Key Mechanisms

### Synfire Chains for Timing

Neurons in each element-specific population are organized as **synfire chains**:
- Each neuron projects to the next with fixed delay
- Activity propagates along the chain
- Chain position encodes elapsed time since element onset

### Oscillatory Gating

Background oscillations modulate neuronal excitability:
- Peak: Promote spiking (replay)
- Trough: Suppress spiking (transition)
- Frequency determines how quickly the chain advances

### Sparse Spatiotemporal Encoding

The model finds that elapsed time is encoded by **unique and sparse spatiotemporal patterns** of neural activity — each time point has a distinct neural signature.

## Implementation Notes

### Key Parameters

| Parameter | Value Range | Description |
|-----------|-------------|-------------|
| τ_m | 10-30 ms | Membrane time constant |
| Synfire delay | 1-10 ms | Inter-neuron propagation delay |
| Oscillation freq | 4-80 Hz | Background clock frequency |
| Population size | 10-100 neurons | Per element-specific group |

### Pseudocode

```python
class SpikingTemporalMemory:
    def __init__(self, num_elements, population_size, tau_m, delays):
        self.elements = [ElementPopulation(n=population_size) 
                        for _ in range(num_elements)]
        self.oscillator = Oscillator(frequency=8.0)  # Default θ
        self.synfire_chains = self._build_synfire_chains(delays)
    
    def forward(self, sequence_input):
        """Process sequence input through sTM."""
        for item, duration in sequence_input:
            # 1. Activate element-specific population
            active_pop = self.elements[item]
            
            # 2. Propagate through synfire chain
            #    Chain length ∝ duration
            chain_steps = int(duration / self.synfire_delay)
            for step in range(chain_steps):
                self.synfire_chains[item].step()
                
                # 3. Oscillatory gating
                oscillation_phase = self.oscillator.get_phase()
                if oscillation_phase > 0.5:  # Trough
                    self._suppress_spiking()
    
    def replay(self, speed_factor=1.0):
        """Replay learned sequence at controlled speed."""
        oscillation_freq = self.oscillator.base_freq * speed_factor
        self.oscillator.set_frequency(oscillation_freq)
        # Replay with new timing
        self._trigger_replay()
```

## Biological Plausibility

The model is grounded in known neuroscience:

1. **Synfire chains**: Observed in cortex and hippocampus
2. **Oscillatory control**: θ-γ coupling in hippocampus during memory
3. **Speed control**: Hippocampal replay speed varies with brain state
4. **Sparse coding**: Consistent with cortical sparse representation
5. **STDP learning**: Biological plasticity rule for learning connections

## Applications

1. **Memory consolidation models**: Understanding sleep-dependent replay
2. **Sequence learning in neuromorphic hardware**: Event-based sequence processing
3. **Timing-dependent computation**: Tasks requiring precise temporal organization
4. **BCI sequence decoding**: Inferring timing from neural activity

## Pitfalls & Considerations

- **Oscillation coherence**: Requires globally coherent oscillations across populations
- **Parameter sensitivity**: Timing precision depends on precise delay distribution
- **Scale limitations**: Long sequences require many neurons per element
- **Training complexity**: Learning both order and timing requires additional constraints

## Activation Keywords

- spiking temporal memory
- sTM model
- sequence timing spiking neural network
- replay speed control
- oscillatory clock neural
- synfire chain timing
- sparse spatiotemporal encoding
- SNN sequence learning
- theta gamma replay
- arXiv:2605.22523

## References

- arXiv:2605.22523 — "Learning sequence timing and control of replay speed in networks of spiking neurons" (Lober et al., 2026)
- sTM original model (Bouhadjar et al., prior work)
- Hippocampal replay during sleep (Wilson & McNaughton, 1994; Lee & Wilson, 2002)
- Theta-gamma coupling (Lisman & Jensen, 2013)
