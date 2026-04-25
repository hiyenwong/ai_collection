---
name: intrinsic-neurosynaptic-memristive-spiking
version: 1.0.0
description: Self-organizing memristive networks generating neuronal population spiking dynamics with intrinsic neuro-synaptic resonance
trigger: memristive network, neuro-synaptic dynamics, spiking resonance, memristor spiking, self-organizing network, neuromorphic hardware
authors: [Yinhao Xu, Georg A. Gottwald, Zdenka Kuncic]
paper: https://arxiv.org/abs/2604.18015
date: 2026-04-20
tags: [memristive network, spiking dynamics, resonance, neuromorphic, self-organizing, neuro-synaptic]
---

# Intrinsic Neuro-Synaptic Spiking Dynamics in Memristive Networks

## Overview

Self-organizing memristive networks are physical circuits that dynamically reconfigure in response to external input signals. This work demonstrates that such networks naturally generate neuronal population spiking dynamics similar to biological neuronal systems, and reveals nonlinear resonance phenomena.

## Core Methodology

### 1. Memristive Network Model
- **Physical substrate**: Self-organizing memristive circuits with heterogeneous topology
- **Dynamics**: Intrinsic neuro-synaptic dynamics emerge from voltage-dependent memristance
- **Adaptation**: Circuitry reconfiguration in response to external input signals

### 2. Input Signal Analysis
- **DC input**: Steady-state spiking dynamics characterization
- **AC input**: Frequency-dependent response analysis
- **Resonance**: Nonlinear spike-like features maximized at matching frequency

### 3. Key Findings
1. Networks generate population spiking dynamics resembling biological systems
2. Nonlinear resonance occurs when input frequency matches intrinsic timescale
3. Optimal computational frequency = maximal frequency before resonance onset
4. Heterogeneous topology enables diverse spiking patterns

## Implementation Guide

### Memristive Network Setup
```
Network topology: Heterogeneous random graph
Node model: Memristive element with voltage-dependent conductance
Synapse model: State-dependent memristance with plasticity
Input: DC or AC driving signal
```

### Analysis Pipeline
1. Define network topology (adjacency matrix)
2. Initialize memristive states
3. Apply DC/AC input signal
4. Record node voltages and currents
5. Extract spiking events and population statistics
6. Analyze frequency response for resonance

### Resonance Detection
- Sweep input frequency across range
- Measure nonlinear spiking response amplitude
- Identify peak response frequency (resonance frequency)
- Determine optimal computational frequency (pre-resonance)

## Applications
- **Neuromorphic hardware design**: Physical spiking circuits
- **Brain-inspired computing**: Self-organizing computational substrates
- **Neural simulation**: Hardware-accelerated spiking network emulation
- **Reservoir computing**: Memristive reservoirs with tunable dynamics

## Key Parameters
- Network size and topology heterogeneity
- Memristive element parameters (on/off ratio, switching threshold)
- Input signal frequency and amplitude
- Intrinsic dynamical timescale

## References
- Xu, Gottwald, Kuncic. "Intrinsic Neuro-Synaptic Spiking Dynamics and Resonance in Memristive Networks" (arXiv:2604.18015, IJCNN 2026)
