---
name: learning-sequence-timing-spiking-neurons
description: Learning sequence timing and control of replay speed in networks of spiking neurons — sTM model extension for encoding element-specific timing and flexible replay speed modulation via oscillatory background input. arXiv 2605.22523 (May 2026).
arxiv_id: "2605.22523"
published: 2026-05-21
category: neuroscience
tags: [spiking-neural-network, sequence-learning, replay, timing, oscillations, sTM, temporal-memory]
activation: spiking neural network, sequence timing, replay speed, sTM model, temporal memory
---

# Learning Sequence Timing and Control of Replay Speed in Networks of Spiking Neurons

**arXiv:** 2605.22523 | **Authors:** Melissa Lober, Younes Bouhadjar, Markus Diesmann, Tom Tetzlaff  
**Affiliation:** Jülich Research Centre, RWTH Aachen, Fraunhofer IIS

## Overview

Processing sequential inputs is a fundamental brain function underlying sensory perception, language, and motor control. This paper extends the **spiking Temporal Memory (sTM)** model — a biologically inspired spiking neural network — to encode not just the *order* but the *precise timing* of sequence elements, and to flexibly control the *speed* of sequence replay.

## Key Contributions

### 1. Timing Encoding via Delay Lines
- The sTM model discretizes time into elementary intervals shorter than dendritic plateau potentials (~100ms).
- Longer intervals are constructed by concatenating sequentially activated neuronal assemblies ("delay lines") within the same minicolumn.
- Produces a sparse "bar code" of neuronal activity encoding both element identity and temporal duration.
- Demonstrated on a musical melody (Roy Orbison's "Oh, Pretty Woman") with 8, 16, and 24-note sequences.

### 2. Oscillatory Background Input Controls Replay Speed
- Constant background input provides limited replay speed modulation.
- **Oscillatory background input** (simulating cortical theta/gamma rhythms) acts as a clock signal.
- Replay speed range: ~10-70 Hz, independent of encoding speed.
- Oscillation frequency, amplitude (50-200 pA), phase, and offset jointly determine replay characteristics.

### 3. Testable Predictions
- Elapsed time is encoded by unique, sparse spatiotemporal patterns of neural activity (not rate codes).
- Replay speed during wakefulness vs. sleep correlates with global oscillatory activity (EEG/LFP).
- Predicts cross-frequency coupling between replay speed and background oscillations.
- Spike threshold modulation by background inputs determines replay speed bounds.

## Network Architecture (sTM Model)

- **M=6 minicolumns**, each with nE=200 excitatory + nI=1 inhibitory neurons
- Sparse random recurrent connectivity with **dendritic action potentials (dAPs)** as prediction signals
- **Lateral inhibition** → winner-take-all (WTA) competition
- **Structural STDP** (spike-timing-dependent plasticity) + continuous weight decay
- Plateau potentials last ~100ms, setting the intrinsic timescale

## Methods

- Training: 500 presentations of melody sequences, fixed inter-element interval ΔT=40ms
- Slower tempo variants: repeating each note (1x → 2x → 3x) yielding C=8, 16, 24
- Replay mode: increased excitability (reduced spike threshold or background current)
- Background inputs: constant (Ī=50-300 pA) vs oscillatory (f=10-100 Hz, a=50-200 pA)
- Metric: stable replay with correct order, no spurious assembly activations

## Key Results

1. **Delay lines encode timing**: Repeated same-stimulus presentations within a minicolumn generate sequentially activated assemblies encoding duration.
2. **Oscillatory background > constant**: Wider dynamic range, more robust replay, encoding-speed-independent.
3. **Replay speed bounds**: Lower bound ≈ 10Hz (dAP duration ~100ms), upper bound ≈ 70Hz (synaptic/membrane time constants).
4. **Encoding-speed independence**: Replay can be faster or slower than encoding speed without relearning.
5. **Phase-sensitive**: Oscillatory input phase relative to plateau onset affects reliability.

## Implications

- Biologically plausible mechanism for representing both "what" and "when" in sequences.
- Links global brain oscillations (theta/gamma) to replay speed control — functional role for network rhythms.
- Relevant to memory consolidation (sharp-wave ripples, hippocampal replay), motor sequence learning, temporal processing in neurological disorders.
- Provides a SNN-based alternative to Transformer positional encodings for temporal structure.

## Limitations

- Static minicolumn assignment — biological cortex has more flexible assembly formation.
- Single sequence demonstrated; multi-sequence interference not addressed.
- Assumes uniform inter-element intervals during encoding.
- Not validated on naturalistic variable-timing sequences.

## Activation Keywords
`spiking neural network`, `sequence timing`, `replay speed`, `sTM model`, `temporal memory`, `oscillatory control`, `dendritic action potential`, `working memory`, `sequence learning SNN`, `hippocampal replay`

## Related Skills
- working-memory-heterogeneous-delays-v3
- attractor-models-language-reasoning
- spike-timing-neuronal-assemblies
- ssn-working-memory-heterogeneous-delays-v3
