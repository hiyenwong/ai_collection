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

## Full Abstract

Processing sequential inputs is a fundamental brain function, underlying tasks such as sensory perception, language, and motor control. A challenge in sequence processing is to represent not only the order of events, but also their precise timing. While existing computational models can learn sequential structure, many lack biologically plausible mechanisms to encode element-specific timing and to flexibly control the speed of sequence replay. The spiking Temporal Memory (sTM) model, a biologically inspired network model, provides a framework for key aspects of sequence processing. In the sTM model, each sequence element is represented by a small set of neurons firing synchronously, where the set of active neurons encodes the element's identity in its sequential context. In its original version, however, the sTM model learns the order but not the timing of sequence elements. Further, it remains an open question in neuroscience how the speed of sequence replay can be flexibly modulated. We propose a mechanism where the duration of sequence elements is represented by a sequential activation of element specific neuronal populations, enabling the model to encode sequences across a wide range of timescales. This provides a biologically plausible basis for learning and replaying complex temporal patterns. Additionally, we show that oscillatory background inputs can serve as a clock signal and provide a robust and flexible mechanism for controlling the speed of sequence replay. Our findings suggest that elapsed time is encoded by unique and sparse spatiotemporal patterns of neural activity, and that the speed of sequence replay during wakefulness and sleep is correlated to the characteristics of global oscillatory activity observed in EEG or LFP recordings.

## Core Innovations

### 1. Element-Specific Duration Encoding
Each sequence element's duration is encoded by sequential activation of element-specific neuronal populations:
- Each element recruits a dedicated chain of neurons
- Chain length determines duration of that element
- Spike timing within chain encodes passage of time
- Enables encoding across wide range of timescales (ms to seconds)

### 2. Oscillatory Clock for Replay Speed Control
Background oscillatory inputs serve as a clock signal:
- Oscillation frequency modulates replay speed
- θ rhythm (~4-8 Hz): Slow replay during wakefulness
- γ rhythm (~30-80 Hz): Fast replay during sleep
- Links to known EEG/LFP oscillatory patterns

### 3. Sequence Replay During Different Brain States

| Brain State | Oscillation | Replay Speed | Function |
|------------|-------------|--------------|----------|
| Wakefulness | θ (4-8 Hz) | Slow | Deliberate recall |
| SWS Sleep | δ/θ | Slow | Memory consolidation |
| REM Sleep | γ (30-80 Hz) | Fast | Novel associations |
| Sharp-wave ripples | 150-200 Hz | Extremely fast | Hippocampal replay |

## sTM Architecture

**Neuron Model**: LIF neurons with membrane time constant τ_m, refractory period, adaptive threshold.

**Synfire Chains for Timing**: Neurons in element-specific populations organized as synfire chains — each neuron projects to next with fixed delay, chain position encodes elapsed time.

**Oscillatory Gating**: Background oscillations modulate neuronal excitability — peaks promote spiking, troughs suppress transitions. Frequency determines chain advance speed.

**Sparse Spatiotemporal Encoding**: Elapsed time encoded by unique sparse spatiotemporal patterns — each time point has distinct neural signature.

## Key Parameters

| Parameter | Value Range | Description |
|-----------|-------------|-------------|
| τ_m | 10-30 ms | Membrane time constant |
| Synfire delay | 1-10 ms | Propagation delay |
| Oscillation freq | 4-80 Hz | Background clock |
| Population size | 10-100 neurons | Per element group |

## Biological Plausibility

1. **Synfire chains**: Observed in cortex and hippocampus
2. **Oscillatory control**: θ-γ coupling in hippocampus during memory
3. **Speed control**: Hippocampal replay speed varies with brain state
4. **Sparse coding**: Consistent with cortical sparse representation
5. **STDP learning**: Biological plasticity rule

## Applications
1. Memory consolidation models — sleep-dependent replay
2. Neuromorphic sequence learning — event-based processing
3. Timing-dependent computation — temporal organization tasks
4. BCI sequence decoding — timing inference from neural activity

## Pitfalls
- Oscillation coherence: requires globally coherent oscillations
- Parameter sensitivity: timing precision depends on delay distribution
- Scale limitations: long sequences require many neurons per element
- Training complexity: learning order + timing needs extra constraints

## Activation Keywords
- spiking temporal memory, sTM model, sequence timing SNN
- replay speed control, oscillatory clock neural, synfire chain timing
- sparse spatiotemporal encoding, SNN sequence learning
- theta gamma replay, hippocampal replay speed
- arXiv:2605.22523
