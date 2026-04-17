---
name: snn-working-memory-heterogeneous-delays-v3
description: Implement working memory in recurrent spiking neural networks using heterogeneous synaptic delays. Each synapse has D=41 delay channels modeled as a weight tensor W ∈ R^{N×N×D}, trained end-to-end with surrogate-gradient BPTT. Memory is stored as sequential chains of overlapping Spiking Motifs — contiguous windows of length D that uniquely predict spikes at the next timestep.
version: 0.1.0
arxiv: 2604.14096v1
title: "Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays"
tags:
  - spiking-neural-networks
  - working-memory
  - heterogeneous-delays
  - surrogate-gradient
  - BPTT
  - neuromorphic
  - spiking-motifs
---

# Working Memory via Heterogeneous Synaptic Delays in SNNs

## Overview

This skill implements a recurrent spiking neural network (SNN) that achieves perfect working memory by equipping every synapse with heterogeneous delays. Each synapse has D = 41 delay channels, forming a 3D weight tensor **W** ∈ ℝ^{N×N×D}. The network is trained end-to-end using surrogate-gradient backpropagation through time (BPTT).

## Key Mechanism: Spiking Motifs

Memory is stored as **sequential chains of overlapping Spiking Motifs**:
- Each motif is a contiguous window of length D timesteps
- A motif at time t uniquely predicts the spike pattern at time t+1
- Overlapping motifs chain together to reconstruct arbitrary target spike patterns
- Recall emerges first near the clamped initialization window and propagates forward in time

## Architecture

- **Neurons**: N = 512 recurrent spiking neurons (LIF dynamics)
- **Delays**: D = 41 heterogeneous delay channels per synapse
- **Weight tensor**: W ∈ ℝ^{N×N×D}
- **Training**: Surrogate-gradient BPTT with temporal precision
- **Memory capacity**: M = 16 arbitrary target spike patterns
- **Sequence length**: T = 1000 timesteps
- **Performance**: Mean F1 = 1.0 on synthetic benchmark

## When to Use

- Implementing persistent working memory in neuromorphic hardware
- Storing and recalling precise temporal spike patterns
- Energy-efficient temporal pattern recognition at the edge
- Research into biologically plausible memory mechanisms in spiking networks

## Core Components

1. **Heterogeneous Delay Layer**: Each synapse (i,j) has D independent delay channels, each with its own trainable weight
2. **LIF Neuron Model**: Standard leaky integrate-and-fire with membrane potential dynamics
3. **Surrogate Gradient**: Differentiable approximation of the non-differentiable spike function for BPTT
4. **Motif-Based Memory Encoding**: Target patterns decomposed into overlapping D-length windows
5. **Clamped Initialization**: Network state clamped during an initial window to seed recall dynamics
