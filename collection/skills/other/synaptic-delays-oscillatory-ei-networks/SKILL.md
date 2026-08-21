---
name: synaptic-delays-oscillatory-ei-networks
description: "Synaptic delays in oscillatory E-I networks."
metadata:
  arxiv_id: "2608.15077"
  published: "2026-08-18"
  authors: "Parsa Shahab Rad, Mojtaba Madadi Asl, Alireza Valizadeh"
  tags: [neuroscience, brain network, neural dynamics, spiking neural network, computational neuroscience, synaptic delays, oscillatory networks, PING, nPRC, nARC]
license: Complete terms in LICENSE.txt
---

# Synaptic Delays Modulate Population Phase and Amplitude Responses in Oscillatory Excitatory-Inhibitory Networks

## Overview

This skill implements the methodology from arXiv paper 2608.15077 "Synaptic delays modulate population phase and amplitude responses in oscillatory excitatory-inhibitory networks" by Parsa Shahab Rad, Mojtaba Madadi Asl, and Alireza Valizadeh.

The research investigates how synaptic delays regulate the collective response of neuronal populations to transient perturbations in conductance-based excitatory-inhibitory spiking networks operating in the pyramidal-interneuron gamma (PING) regime.

## Key Contributions

### Core Findings
- **Frequency-Coherence Trade-off**: Increasing synaptic delay slows network oscillations while enhancing population synchrony, demonstrating a fundamental trade-off between oscillation frequency and coherence
- **Excitatory Perturbation Response**: Relatively robust phase responses across delays but pronounced delay-dependent reduction in amplitude enhancement
- **Inhibitory Perturbation Response**: Substantially stronger delay-dependent modulation of both phase resetting and amplitude suppression
- **Whole-Network Stimulation**: Combines features of both excitatory and inhibitory responses

### Methodology
- **Network Phase Response Curves (nPRCs)**: Quantify changes in oscillation timing due to perturbations
- **Network Amplitude Response Curves (nARCs)**: Quantify changes in population coherence due to perturbations  
- **Systematic Delay Variation**: Comprehensive analysis across different synaptic delay values
- **Targeted Perturbations**: Applied to excitatory population, inhibitory population, or entire network

## Implementation Guidelines

### When to Apply This Framework
- Analyzing delay-dependent control mechanisms in oscillatory brain networks
- Studying gamma oscillations and PING dynamics in cortical circuits
- Investigating synaptic delay effects on network synchronization and stability
- Designing neuromorphic systems with realistic synaptic transmission delays
- Modeling transient perturbation responses in E-I balanced networks

### Computational Setup
1. **Network Model**: Conductance-based excitatory-inhibitory spiking network in PING regime
2. **Delay Parameter**: Systematically vary synaptic delay (typically 1-10ms range)
3. **Perturbation Protocol**: Apply brief external perturbations to specific populations
4. **Response Measurement**: Compute nPRCs and nARCs from population activity
5. **Analysis**: Correlate delay values with phase resetting and amplitude modulation

### Key Parameters to Monitor
- **Oscillation Frequency**: How delay affects network rhythm frequency
- **Population Synchrony**: Coherence measures (e.g., Kuramoto order parameter)
- **Phase Resetting Magnitude**: nPRC amplitude across delay conditions  
- **Amplitude Modulation**: nARC responses to different perturbation types
- **Delay-Dependent Sensitivity**: Differential effects on E vs I perturbations

## Applications

### Neuroscience Research
- Understanding cortical gamma oscillation regulation mechanisms
- Interpreting EEG/MEG phase-amplitude coupling in cognitive tasks
- Modeling neurological disorders with altered synaptic transmission
- Investigating developmental changes in synaptic delay maturation

### Neuromorphic Engineering
- Designing delay-aware spiking neural network architectures
- Optimizing communication protocols in neuromorphic hardware
- Implementing biologically realistic temporal coding schemes
- Developing delay-based learning rules for SNNs

### Clinical Implications
- Biomarker development for disorders with synaptic dysfunction
- Target identification for neuromodulation therapies
- Understanding pharmacological effects on synaptic transmission
- Predicting network-level effects of conduction velocity changes

## Pitfalls and Considerations

### Model Limitations
- Assumes homogeneous populations; real networks have heterogeneity
- Focuses on PING regime; other oscillation mechanisms may differ
- Conductance-based model complexity vs simpler integrate-and-fire models
- Limited to local network effects; ignores long-range connectivity

### Experimental Validation
- Requires precise measurement of synaptic delays in vivo
- Population response curves need sufficient trial averaging
- Distinguishing E vs I perturbation effects can be technically challenging
- Species and brain region differences in baseline parameters

### Computational Challenges
- High-dimensional parameter space for comprehensive analysis
- Long simulation times for statistical reliability
- Sensitivity to initial conditions and network size effects
- Numerical stability with very short or very long delays

## Related Skills

- `kuramoto-brain-network`: For general oscillator synchronization analysis
- `ei-network-chaos-synchrony-theory`: For E-I network dynamics beyond oscillatory regimes  
- `spiking-neural-network-analysis`: For general SNN methodology and implementation
- `brain-oscillation-synchronization-framework`: For unified oscillation analysis framework

## Original Paper Reference

- **Title**: Synaptic delays modulate population phase and amplitude responses in oscillatory excitatory-inhibitory networks
- **Authors**: Parsa Shahab Rad, Mojtaba Madadi Asl, Alireza Valizadeh
- **arXiv**: [2608.15077](https://arxiv.org/abs/2608.15077) [q-bio.NC]
- **Subjects**: Neurons and Cognition (q-bio.NC)

## Activation Keywords

- synaptic delays oscillatory networks
- delay-dependent phase response
- nPRC nARC computation
- PING regime synaptic delay
- excitatory-inhibitory delay modulation
- gamma oscillation delay control
- population synchrony synaptic transmission
- oscillatory brain network delays