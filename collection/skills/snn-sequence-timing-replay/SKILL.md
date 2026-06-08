---
name: snn-sequence-timing-replay
description: >
  Biologically plausible spiking neural network model for learning sequence
  timing and controlling replay speed. Extends the spiking Temporal Memory (sTM)
  model with element-specific duration encoding via sequential activation of
  neuronal populations, and uses oscillatory background inputs as a clock signal
  for flexible speed control. Use when working with: spiking neural networks for
  sequence learning, temporal memory models, sequence replay in SNNs, timing
  encoding in neural populations, oscillatory control of replay speed, STDP-based
  sequence learning, sleep replay mechanisms, hippocampal replays.
arxiv_id: "2605.22523"
published: "2026-05-21"
authors: "Melissa Lober, Younes Bouhadjar, Markus Diesmann, Tom Tetzlaff"
tags: [spiking neural network, sequence learning, temporal memory, replay, STDP, oscillations, timing, sTM model, neuromorphic computing]
---

# Learning Sequence Timing and Control of Replay Speed in Networks of Spiking Neurons

**arXiv:2605.22523** (Lober, Bouhadjar, Diesmann, Tetzlaff, May 2026)  
**Category**: q-bio.NC (Neurons and Cognition)

## Core Idea

Sequences are fundamental to brain function (sensory perception, language, motor control). The **spiking Temporal Memory (sTM) model** learns sequence order but not precise **timing**. This paper extends sTM with:

1. **Element-specific duration encoding** — each sequence element activates a distinct chain of neuronal sub-populations, encoding both identity AND duration
2. **Oscillatory speed control** — background oscillations (like brain rhythms) serve as a clock to flexibly modulate replay speed, from slow (wakefulness) to fast (sleep)

## Architecture

### Standard sTM Model (Baseline)

- Each sequence element → synchronized burst from a small **assembly** of neurons
- Assembly identity encodes the element in its sequential context
- **Spike-timing-dependent plasticity (STDP)** learns order by strengthening excitatory connections between sequentially activated assemblies
- **Inhibition** prevents runaway excitation and enforces winner-take-all dynamics

### Extended sTM with Timing (This Paper)

**Duration encoding**: Instead of each element activating a single assembly, the element activates a **chain** of assemblies in sequence. The length of the chain (number of sequential assemblies activated) encodes the element's duration.

- Short duration → short chain (few assemblies)
- Long duration → long chain (many assemblies)
- Each assembly in the chain fires for a fixed base interval; the total duration = chain length × base interval

**Speed control via oscillations**: Adding oscillatory background input to all neurons.

- **High-frequency oscillations** → shorter interspike intervals → faster chain traversal → faster replay
- **Low-frequency oscillations** → longer interspike intervals → slower chain traversal → slower replay
- The oscillation frequency globally modulates the speed of replay across all chains

## Key Mechanisms

### 1. STDP-Based Assembly Formation

```
Pre-before-post: Δw = A⁺·exp(-Δt/τ⁺)   (potentiation)
Post-before-pre: Δw = A⁻·exp(-Δt/τ⁻)   (depression)
```

After learning, assemblies form: groups of neurons with strong recurrent excitatory connections that fire synchronously when activated. Each assembly is defined by its unique set of synaptic weights.

### 2. Chain Encoding of Duration

```
Element E1 (short):   A1 → A2
Element E2 (medium):  B1 → B2 → B3
Element E3 (long):    C1 → C2 → C3 → C4
```

Each assembly (A1, A2, B1, etc.) is a distinct group. The chain's length encodes duration. During learning, the chain structure emerges through STDP: when assembly A1 fires, it drives A2, which then drives A3, etc.

### 3. Oscillatory Clock Signal

Neurons receive a common oscillatory drive `I_osc(t) = A·sin(2π·f·t)`. This modulates the membrane potential:

- **Near threshold**: oscillation determines WHEN the neuron fires
- **Higher amplitude**: tighter phase locking to oscillation
- **Frequency modulation**: changing `f` changes the timing of all spikes

### 4. Replay Speed Modulation

During recall, the same oscillatory input controls the speed:

| Oscillation Frequency | Replay Speed | Biological Correlate |
|---|---|---|
| 2–4 Hz (theta) | 1× (slow) | Wakeful encoding, exploration |
| 8–12 Hz (alpha) | 1.5–2× | Relaxed wakefulness |
| 150–250 Hz (sharp-wave ripples) | 10–20× (fast) | Sleep consolidation, hippocampal replay |

The replay speed is proportional to oscillation frequency across a wide range — the mechanism is **robust and continuously tunable**.

## Key Results

1. **Timing learned successfully**: The model learns both the order AND duration of sequence elements purely through local plasticity rules (STDP).

2. **Wide timescale range**: Sequences with element durations spanning 10 ms to 1000 ms can be learned and replayed.

3. **Oscillatory speed control**: Replay speed varies linearly with oscillation frequency (verified over 5 Hz – 200 Hz range).

4. **Biologically plausible**: All mechanisms use only local learning rules (STDP) and biologically realistic inputs (oscillatory drive). No global error signal or supervisor.

5. **Robust to noise**: The mechanism works reliably with Poisson input noise and realistic synaptic failure rates.

## Relation to Hippocampal Replay

Hippocampal replay during sleep (sharp-wave ripple events) compresses awake experiences 10-20×. This model provides a mechanistic explanation:

- During wakefulness: theta oscillations provide the clock → slow replay
- During sleep: sharp-wave ripples provide fast oscillations → compressed replay (10-20×)
- The SAME learned assembly chain supports both slow and fast replay — speed is determined by the oscillatory context, not by different synaptic strengths

## Practical Implications

### For Neuromorphic Computing

- **Event-based sequence learning**: SNNs naturally suited for temporal pattern learning
- **On-chip speed control**: A single oscillatory signal can globally modulate replay speed
- **Power-efficient**: Oscillation-controlled timing avoids per-neuron timer circuits

### For Neuroscience

- **Testable prediction**: Elapsed time encoding via sequential assembly activation should be observable in hippocampal/temporal cortex recordings during sequence tasks
- **Sleep replay mechanism**: Oscillation frequency differences between theta and sharp-wave ripples explain replay speed differences

## Activation Keywords

- spiking temporal memory
- sTM model
- sequence timing SNN
- replay speed modulation
- oscillatory clock neural
- STDP sequence learning
- temporal encoding spiking neurons
- hippocampal replay timing
- sharp-wave ripple compression
- chain assembly encoding
