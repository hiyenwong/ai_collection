---
name: learning-sequence-timing-replay-speed-snn
description: "Learning sequence timing and control of replay speed in networks of spiking neurons. Extends the spiking Temporal Memory (sTM) model to encode element-specific duration and flexibly control replay speed via oscillatory background inputs. Applicable to computational neuroscience, SNN timing learning, neural sequence processing. Activation: spike timing, sTM model, sequence replay, oscillatory speed control, spiking temporal memory, neural sequence processing."
user-invocable: true
---

# Learning Sequence Timing and Replay Speed Control in SNNs

**Source Paper:** arXiv:2605.22523 - Learning sequence timing and control of replay speed in networks of spiking neurons

**Authors:** Melissa Lober, Younes Bouhadjar, Markus Diesmann, Tom Tetzlaff

**Published:** 2026-05-21

## Core Methodology

### 1. Spiking Temporal Memory (sTM) Model Extension

The sTM model represents each sequence element by a small set of synchronously firing neurons, where the active set encodes the element's identity in its sequential context.

**Key Innovation:** Extends sTM from order-only to order-and-timing encoding:

- **Duration encoding via sequential activation:** Element duration is represented by sequential activation of element-specific neuronal populations
- **Timescale flexibility:** Enables encoding across a wide range of timescales
- **Biologically plausible mechanism** for learning and replaying complex temporal patterns

### 2. Oscillatory Clock Signal for Speed Control

**Core Finding:** Oscillatory background inputs serve as a clock signal providing robust and flexible speed control of sequence replay.

**Mechanism:**
- Global oscillatory activity (as observed in EEG/LFP) modulates replay speed
- Speed during wakefulness vs. sleep correlates with oscillatory characteristics
- Provides a neurophysiologically grounded mechanism for flexible timing

### 3. Sparse Spatiotemporal Encoding of Time

**Key Insight:** Elapsed time is encoded by unique and sparse spatiotemporal patterns of neural activity.

## Key Contributions

1. **Timing learning:** Biologically plausible mechanism for learning element-specific durations in spiking networks
2. **Speed control:** Oscillatory background activity as a natural clock signal for replay speed modulation
3. **Implementation:** Extends sTM without requiring additional biologically implausible mechanisms

## Implementation Notes

### Spiking Temporal Memory Architecture

- Each sequence element -> dedicated neuronal population with synchronous firing
- Duration -> sequential recruitment of within-element subpopulations
- Speed control -> oscillatory drive amplitude/frequency modulates activation dynamics

### Key Parameters

- Element-specific timing: controlled by synaptic delays and recurrent connectivity within each population
- Oscillatory clock: frequency and amplitude determine replay speed
- Sparse coding: minimal overlap between representations of different elements

## Related Skills

- [[spike-timing-neuronal-assemblies]] - STDP-based neuronal assembly formation
- [[working-memory-heterogeneous-delays]] - SNN working memory with delays
- [[cognisnn-brain-inspired-snn]] - Cognition-aware SNN architectures
