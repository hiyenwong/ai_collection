---
name: sound-localization-equilibrium-dynamics
description: Equilibrium dynamics framework for microsecond-precision sound localization — represents ITD as stable equilibrium of neural population dynamics rather than classical place-coding.
trigger_words:
  - sound localization
  - interaural time differences
  - ITD equilibrium
  - binaural perception
  - equilibrium dynamics
  - neural population dynamics
  - Jeffress model alternative
  - microsecond precision sound
  - equilibrium ITD estimation
  - slow equilibrium dynamics
categories:
  - neuroscience
  - computational neuroscience
  - auditory processing
  - neural dynamics
created: "2026-07-12"
source: "arXiv:2607.03890v1 (submitted to Science)"
---

# Sound Localization from Slow Equilibrium Dynamics

## Paper

**Title:** Microsecond-precision sound localization emerges from slow equilibrium dynamics  
**Authors:** Toshio Irino  
**Published:** arXiv:2607.03890v1 (Submitted to Science, July 4, 2026)  
**Date:** July 4, 2026  

## Problem

Precise sound localization relies on microsecond sensitivity to interaural time differences (ITDs), yet binaural perception exhibits sluggish tracking of dynamic acoustic cues. How these properties coexist remains unresolved under the classical Jeffress model (1948) which relies on delay lines.

## Key Insight

**ITD is represented as a stable equilibrium of neural population dynamics** rather than by the classical place-coding framework originally proposed by Jeffress (1948).

## Framework

### Equilibrium Dynamics Model

In this framework:

- **Excitatory and inhibitory interactions** across frequency channels generate a population signal
- This signal drives a **dynamical system toward an equilibrium** corresponding to the estimated ITD
- Despite relying on **relatively slow temporal dynamics**, the model achieves microsecond-level precision
- Reproduces key physiological observations including **frequency-dependent best-delay distributions**
- **No explicit delay lines or precisely timed inhibition** required

### Contrast with Jeffress Model

| Feature | Jeffress Model (1948) | Equilibrium Dynamics (2026) |
|---------|----------------------|----------------------------|
| ITD encoding | Place code via delay lines | Dynamical equilibrium |
| Temporal precision | Requires precise timing | Achieved via slow dynamics |
| Inhibition timing | Precisely timed | General inhibitory interactions |
| Best-delay distribution | Requires anatomical structure | Emerges from dynamics |
| Dynamic cue tracking | Fast response | Matches observed sluggishness |

### Core Mechanism

1. **Multi-channel input:** Sound arrives at both ears with interaural time difference
2. **Cross-frequency interaction:** Excitatory and inhibitory interactions across frequency channels
3. **Population signal generation:** Combined activity creates a population-level signal
4. **Dynamical system evolution:** The population signal drives a dynamical system
5. **Equilibrium convergence:** System converges to stable equilibrium representing ITD estimate
6. **Microsecond precision:** Despite slow dynamics, equilibrium position is precise to microseconds

## Key Results

- Achieves **microsecond-level ITD precision** with slow temporal dynamics
- Reproduces **frequency-dependent best-delay distributions** observed physiologically
- Explains **sluggish tracking of dynamic acoustic cues** as natural property of equilibrium dynamics
- No need for **explicit delay lines** (anatomically controversial)
- No need for **precisely timed inhibition** (biologically implausible at microsecond scale)

## Significance

This work provides a potential explanation for how precise ITD sensitivity can arise from slow neural dynamics, resolving a long-standing paradox in auditory neuroscience. The equilibrium dynamics framework offers:

- **Biological plausibility:** No need for precise microsecond-timed circuit elements
- **Unified explanation:** Accounts for both precision and sluggishness
- **Computational efficiency:** Equilibrium computation is naturally parallelizable
- **Neuromorphic relevance:** Directly implementable in spiking network architectures

## Applications

### Auditory Processing
- Sound localization algorithms
- Binaural hearing models
- Auditory scene analysis

### Neuromorphic Engineering
- Event-driven sound localization chips
- Low-power auditory processing systems
- Bio-inspired audio processing

### Computational Neuroscience
- Modeling auditory brainstem circuits
- Understanding binaural processing
- Neural population dynamics analysis

## Implementation Notes

- The equilibrium dynamics framework can be implemented as:
  - **Coupled differential equations** for population activity
  - **Spiking neural networks** with appropriate excitatory/inhibitory connectivity
  - **Rate-based neural models** with stable fixed points
- Key parameters: interaction strengths across frequency channels, time constants, equilibrium stability

## Trigger Conditions

Use this skill when:
- Modeling sound localization or ITD estimation
- Building biologically plausible auditory processing models
- Designing neuromorphic sound localization systems
- Analyzing neural population dynamics for sensory estimation
- Comparing place-coding vs. dynamics-coding frameworks

## References

- Paper: arXiv:2607.03890v1 (Submitted to Science, July 4, 2026)
- Related: `equilibrium-dynamics-sound-localization` (Related equilibrium dynamics framework)
- Related: `kuramoto-oscillatory-phase-encoding` (Oscillatory phase encoding for neuro-inspired systems)
