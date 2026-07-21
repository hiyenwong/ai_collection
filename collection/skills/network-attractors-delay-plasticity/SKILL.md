---
name: network-attractors-delay-plasticity
description: "Network Attractors driven by Time-Delay Plasticity — framework for collective frequency selection and attractor formation via adaptive axonal delays (AADs), motivated by activity-dependent myelination in the brain. Uses delay-coupled phase oscillators on brain connectivity data. Activation: delay plasticity, adaptive axonal delay, network attractor, frequency selection, neural oscillation, myelination model, phase oscillator brain network"
---

# Network Attractors driven by Time-Delay Plasticity

**arXiv**: [2605.23520](https://arxiv.org/abs/2605.23520) | **Date**: 2026-05-22 | **Category**: nlin.AO

**Authors**: Stefan Ruschel, Emanuil Hristov, Hil G. E. Meijer, Stephen Coombes

## Overview

This paper develops a framework for **collective frequency selection and attractor formation** through **delay plasticity** in neural networks. The key mechanism is **adaptive axonal delays (AADs)**, motivated by **activity-dependent myelination** — the biological process where oligodendrocytes regulate myelin sheathing on axons, changing signal propagation speeds and thus communication delays between neurons.

**Key Insight**: While synaptic weights have been the dominant model of plasticity, axonal delays (regulated by myelination) provide an alternative, largely unexplored substrate for learning and network dynamics that operates on slower timescales.

## Core Methodology

### Adaptive Axonal Delay (AAD) Model

- Each connection has a delay d_ij that adapts based on neural activity
- Delay plasticity rule: d_ij adapts to minimize a frequency-dependent cost or maximize synchrony
- Operates on slower timescales than synaptic plasticity (consistent with myelin remodeling)

### Mathematical Framework

- **Delay-coupled phase oscillators** on brain connectivity data
- **Kuramoto-type models** with adaptive delays replacing fixed delays
- Collective frequency emerges dynamically through delay adaptation

### Key Phenomena Observed

1. **Frequency selection**: The network self-organizes to select collective oscillation frequencies
2. **Explosive network relaxation oscillations**: Sudden transitions between slow and fast oscillatory states
3. **Attractor formation**: Delay adaptation creates multistable attractor landscapes

## Results

- Demonstrated on **brain connectivity data** (empirical structural connectomes)
- Validated on **fully coupled ring networks** (theoretical analysis)
- Shows how slow delay plasticity can reorganize network dynamics fundamentally

## Broader Implications

- **Myelination as a learning mechanism**: Complements synaptic plasticity with a slower, structural form of adaptation
- **Frequency coding**: Suggests neural frequencies are not just readouts but are shaped by learning
- **Neurological relevance**: Links to demyelinating diseases (MS) where conduction delays are disrupted

## Relationship to Other Plasticity Mechanisms

| Plasticity Type | Timescale | Mechanism | AAD Analogy |
|----------------|-----------|-----------|-------------|
| Synaptic (STDP) | Fast (ms-s) | Weight change | Affects connection strength |
| Structural | Slow (min-hr) | Spine/dendrite growth | Affects connectivity |
| **Delay (AAD)** | **Slow (hr-day)** | **Myelination change** | **Affects timing/phase** |

## When to Use

This skill is relevant when:
- **Modeling** experience-dependent myelination in neural networks
- **Studying** collective frequency selection in brain networks
- **Analyzing** multistable attractors in delay-coupled systems
- **Building** phase oscillator models with adaptive delays
- **Investigating** the computational role of axonal conduction delays
- **Researching** plasticity mechanisms beyond synaptic weight change

## Activation Keywords
delay plasticity, adaptive axonal delay, AAD, network attractor, frequency selection, neural oscillation, myelination model, activity-dependent myelination, phase oscillator, delay-coupled oscillator, Kuramoto adaptive delays, explosive relaxation oscillations, multistable attractors, structural plasticity, conduction delay, brain connectivity data, collective frequency, time-delay system, neural dynamics beyond synaptic plasticity
