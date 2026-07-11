---
name: scalable-qst-neural-architectures
description: Benchmarking neural network architectures for scalable Quantum State Tomography with memristor-based acceleration patterns
version: "1.0"
source: "arXiv:2507.23007"
arxiv_id: "2507.23007"
authors: "Erbing Hua, Steven van Ommen et al."
published: "2025-07-30"
categories: "quant-ph"
created: "2026-07-08"
trigger_words:
  - quantum state tomography
  - QST benchmarking
  - memristor acceleration
  - quantum diagnostics
  - neural quantum states
  - SVAE
  - computation in memory
---

# Scalable QST Neural Architectures

## Overview

Comprehensive benchmarking of neural network architectures for Quantum State Tomography (QST). Identifies which architectures scale effectively with qubit number and which fail to maintain high fidelity as system size increases.

**Paper**: "Neural Network Architectures for Scalable Quantum State Tomography: Benchmarking and Memristor-Based Acceleration" (arXiv:2507.23007)

## Architecture Benchmarking Results

### Scaling Performance

- **CNN**: Scales most robustly, achieves highest fidelities for both pure and mixed states
- **CGAN**: Scales robustly, achieves highest fidelities
- **SVAE** (Spiking Variational Autoencoder): Moderate fidelity, strong candidate for embedded low-power hardware

### Two Quantum Measurement Strategies

1. Pure state reconstruction
2. Mixed state reconstruction

## Key Findings

1. Many prior QST performance claims relied on architectural assumptions rather than systematic validation
2. CNN and CGAN architectures maintain high fidelity as qubit count increases
3. SVAE offers a path to energy-efficient embedded quantum diagnostics
4. Practical quantum diagnostics will require embedded, energy-efficient computation

## Hardware Acceleration Pattern

### Memristor-based Computation-in-Memory (CiM)

- Mitigates memory bottlenecks in QST neural networks
- Reduces energy consumption for scalable in-situ QST
- Enables quantum-classical co-design that is both computationally and physically scalable

## Implementation Notes

- QST practical use limited by exponential Hilbert space growth
- Number of measurements required for informational completeness grows exponentially
- Architecture choice matters more than hyperparameter tuning for scalability
- Embedded low-power implementations (SVAE + memristor CiM) are critical for real-world deployment

## When to Use

- Designing QST systems for multi-qubit quantum devices
- Choosing neural architectures for quantum state reconstruction
- Building energy-efficient embedded quantum diagnostic tools
- Quantum-classical co-design for scalable quantum systems
