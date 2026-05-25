---
name: learning-sequence-timing-snn
description: "Extension of the spiking Temporal Memory (sTM) model that learns sequence timing via sequential activation of element-specific neuronal populations and uses oscillatory background inputs as a clock signal for flexible control of replay speed — biologically plausible mechanisms for encoding temporal patterns in spiking neural networks (arXiv: 2605.22523)."
arxiv_id: "2605.22523"
published: "2026-05-21"
authors: "Melissa Lober, Younes Bouhadjar, Markus Diesmann, Tom Tetzlaff"
tags: [spiking-neural-network, sequence-learning, temporal-memory, replay-speed, oscillatory-clock, timing-mechanisms, computational-neuroscience]
---

# Learning Sequence Timing and Control of Replay Speed in Networks of Spiking Neurons

## Core Concept

Extends the **spiking Temporal Memory (sTM)** model to encode not only sequence **order** but also **precise element-specific timing**, and provides a biologically plausible mechanism for flexibly controlling the **speed of sequence replay** via oscillatory background inputs.

## Key Contributions

1. **Timing Encoding Mechanism**: Duration of sequence elements is represented by sequential activation of element-specific neuronal populations, enabling encoding across a wide range of timescales.

2. **Oscillatory Clock Signal**: Oscillatory background inputs serve as a clock signal, providing a robust and flexible mechanism for controlling sequence replay speed.

3. **Wakefulness vs. Sleep Replay**: Replay speed during wakefulness and sleep is correlated with characteristics of global oscillatory activity (EEG/LFP).

4. **Biologically Plausible Framework**: Provides a biologically grounded basis for learning and replaying complex temporal patterns in spiking neural networks.

## Methodology

### sTM Model Architecture
- Each sequence element represented by a small set of synchronously firing neurons
- Active neuron set encodes element identity in sequential context
- Original model: learned order but not timing

### Timing Extension
1. **Sequence element duration**: Represented by sequential activation of population-specific neurons
2. **Temporal encoding**: Element-specific timing via population dynamics
3. **Flexible replay**: Speed modulation via background oscillatory drive

### Speed Control Mechanism
- Oscillatory background inputs as clock signal
- Frequency/phase modulation controls replay speed
- Biologically plausible (EEG/LFP rhythms)

## Key Findings

| Finding | Implication |
|---------|-------------|
| Elapsed time encoded by sparse spatiotemporal activity patterns | Distributed timing representation |
| Oscillatory inputs robustly control replay speed | Clock-like mechanism for sequence timing |
| Speed varies with global oscillatory state | Links EEG rhythms to cognitive processing |
| Timescales span wide range | Flexible temporal coding |

## Relationship to Biological Data

- **Hippocampal replay**: Slow replay during sleep, fast during wakefulness
- **Cortical oscillations**: Gamma/theta rhythms as potential clock signals
- **STDP**: Timing-dependent plasticity for sequence learning
- **Working memory**: Persistent activity maintaining sequence context

## Applications

- **Sequence learning models**: Extending SNNs to temporal processing
- **Neuromorphic computing**: Biologically plausible timing circuits
- **Computational neuroscience**: Understanding neural code for temporal sequences
- **Replay mechanisms**: Modeling consolidation and planning

## Activation Keywords

- spiking-sequence-timing, sTM-model, neural-replay-speed, oscillatory-clock-signal, spiking-temporal-memory, sequence-timing-snn, replay-speed-control, element-specific-timing, eeg-correlates-replay, biological-plausible-timing, snn-sequence-learning, temporal-pattern-spiking, sparse-spatiotemporal-encoding
