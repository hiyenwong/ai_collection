---
name: learning-sequence-timing-spiking-neurons
version: v1.0.0
last_updated: 2026-05-22
description: "Learning sequence timing and control of replay speed in networks of spiking neurons. Extends the spiking Temporal Memory (sTM) model to encode element-specific timing via sequential activation of neuronal populations and uses oscillatory background inputs as a clock signal for flexible replay speed control. Applicable to: sequence learning in SNNs, temporal coding, biological replay mechanisms, timing representation in spiking networks. Trigger: spiking temporal memory, sequence timing SNN, replay speed control, oscillatory clock signal, STDP sequence learning, sTM model"
---

# Learning Sequence Timing and Control of Replay Speed in Networks of Spiking Neurons

## Description

A biologically plausible mechanism for learning precise sequence timing in spiking neural networks, extending the spiking Temporal Memory (sTM) model. The duration of sequence elements is represented by sequential activation of element-specific neuronal populations, enabling encoding across wide timescales. Oscillatory background inputs serve as a clock signal for flexible replay speed control.

Based on: "Learning sequence timing and control of replay speed in networks of spiking neurons" (arXiv:2605.22523, May 2026)

## Problem

- Sequence processing in the brain requires representing not just order but precise timing of events
- Existing computational models (including the original sTM model) learn sequence order but not element-specific timing
- Mechanism for flexible control of replay speed (e.g., fast replay during sleep vs. slow replay during wakefulness) remains unknown
- Need biologically plausible mechanisms for both timing encoding and speed modulation

## Core Results from Paper

### Learning Sequence Timing via Delay Lines
- Time intervals between sequence elements are discretized into elementary intervals shorter than dendritic plateau potential duration (~100ms)
- Longer intervals constructed from concatenations of these elementary intervals
- Implemented as delay lines of sequentially activated neuronal assemblies within same minicolumn
- Sparse, context-specific spatiotemporal "bar code" patterns encoding time elapsed since sequence onset
- Demonstrated with musical melody sequences (Oh, Pretty Woman) with dilation factors 1x, 2x, 3x

### Replay Speed Control: Constant vs. Oscillatory Input
- **Constant background input**: Limited flexibility — slow replay requires fine-tuning; speed sensitive to input current magnitude
- **Oscillatory background input**: Robust, flexible speed control
  - 1:1 clock regime: replay speed = oscillation frequency (green band in parameter space)
  - Integer fraction modes: f/2, f/3, f/4 at lower amplitudes (blue bands)
  - Fast compressed replay at <5 Hz (like slow-wave sleep hippocampal replay)
  - Phase-invariant for frequencies >20 Hz
  - Accessible range: ~10 Hz to ~70 Hz

### Phase Invariance
- For frequencies >20 Hz, replay speed is largely invariant to oscillation phase at onset
- Initial inter-assembly intervals show small variability that quickly disappears
- At low frequencies, strong phase dependence can prevent or alter replay

## Approach

### Timing Encoding via Sequential Population Activation

The duration of each sequence element is encoded by sequential activation of element-specific neuronal populations, creating unique sparse spatiotemporal patterns of neural activity:

```text
Element A → [Population A1 → A2 → ... → An] → Element B → [Population B1 → B2 → ... → Bn]
```

### Oscillatory Clock for Speed Control

Oscillatory background inputs (representing global brain oscillations like theta rhythms) serve as a clock signal:

- Different oscillation frequencies modulate replay speed
- Higher frequencies lead to faster replay
- Lower frequencies lead to slower replay
- Provides robust mechanism independent of learned weights

### Biologically Plausible Learning

- Uses STDP-like mechanisms for sequence structure learning
- Timing information is implicit in the spatiotemporal firing patterns
- No external timer or explicit delay lines needed

## Key Findings

1. Elapsed time is encoded by unique sparse spatiotemporal patterns of neural activity
2. Replay speed during wakefulness vs. sleep correlates with global oscillatory activity observed in EEG or LFP recordings
3. The mechanism works across a wide range of timescales
4. Oscillatory clock provides robust speed control independent of learned content

## Implications

- Provides a unified framework for understanding timing in neural computation
- Connects sequence replay speed modulation to brain rhythms (theta oscillations)
- Offers testable predictions about replay speed during different brain states
- Relevant for both biological neuroscience and neuromorphic computing

## Activation

- spiking sequence timing, sTM model temporal memory, oscillatory replay speed control
- STDP temporal sequence learning, spatiotemporal neural patterns encoding
