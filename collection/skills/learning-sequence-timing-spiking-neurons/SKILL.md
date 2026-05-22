---
name: learning-sequence-timing-spiking-neurons
description: Learning sequence timing and control of replay speed in networks of spiking neurons. Research methodology from arXiv 2605.22523 (May 2026). Extending the spiking Temporal Memory (sTM) model to encode element-specific timing and flexibly control replay speed via oscillatory background inputs. Use when working on: spiking neural network temporal processing, biologically plausible sequence learning, replay/sleep consolidation mechanisms, or neuromorphic timing circuits.
---

# Learning Sequence Timing and Control of Replay Speed in Networks of Spiking Neurons

**arXiv:** 2605.22523 | **Authors:** Melissa Lober, Younes Bouhadjar, Markus Diesmann, Tom Tetzlaff

## Overview

Processing sequential inputs is a fundamental brain function underlying sensory perception, language, and motor control. This paper extends the spiking Temporal Memory (sTM) model — a biologically inspired spiking neural network — to encode not just the *order* but the *precise timing* of sequence elements, and to flexibly control the *speed* of sequence replay.

## Key Contributions

### 1. Timing Encoding via Sequential Activation
- Each sequence element's duration is represented by sequential activation of element-specific neuronal populations
- Enables encoding sequences across a wide range of timescales (from milliseconds to seconds)
- Biologically plausible: elapsed time is encoded by unique, sparse spatiotemporal patterns of neural activity

### 2. Oscillatory Clock for Replay Speed Control
- Oscillatory background inputs serve as a clock signal
- Provides robust, flexible mechanism for controlling sequence replay speed
- Replay speed during wakefulness vs sleep correlates with global oscillatory activity (EEG/LFP rhythms)

### 3. Biologically Plausible Framework
- Fully spiking neuron model (no rate-code approximations)
- STDP-based learning maintains biological realism
- Extends the sTM model which represents each sequence element by synchronously-firing neuron ensembles

## Methodological Details

### sTM Model Architecture
- Each sequence element → small set of synchronously-firing neurons
- Active neuron set encodes element identity in sequential context
- Original sTM: learns order but not timing
- Extended sTM: learns order AND timing via population-specific duration encoding

### Replay Speed Modulation
- Oscillatory input frequency → replay speed
- Slower oscillations → slower replay (sleep-like)
- Faster oscillations → faster replay (wake-like)
- Mechanism: global oscillatory activity gates synaptic transmission or neuronal excitability

## Key Results
- Model successfully encodes and replays sequences with element-specific timing
- Replay speed flexibly modulated across wide range
- Temporal compression/expansion preserves sequence structure
- Sparse spatiotemporal activity patterns emerge as timing representation

## Activation Keywords
- spiking temporal memory
- sTM sequence learning
- spiking neuron timing
- replay speed control
- oscillatory clock SNN
- sequence timing neuroscience
- biologically plausible sequence learning

## Related Skills
- working-memory-heterogeneous-delays-v3
- attractor-models-language-reasoning
- spike-timing-neuronal-assemblies
