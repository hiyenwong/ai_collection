---
name: quantum-simulation-of-real-world-nonlinear-dynamics-via-koopman-method
description: 'Nonlinear dynamics is ubiquitous in nature, ranging from chemical pattern formation to ocean circulation, yet its simulation on quantum computers is fundamentally limited by the unitary nature of quan. Based on arXiv:2607.07338.'
---

# Quantum simulation of real-world nonlinear dynamics via Koopman method

**arXiv**: 2607.07338 | **Authors**: Baoyang Zhang, Dong An, Zhaoyuan Meng, Yefei Yu, Xiaoxiao Xiao et al. | **Utility**: 0.87

## Overview

Nonlinear dynamics is ubiquitous in nature, ranging from chemical pattern formation to ocean circulation, yet its simulation on quantum computers is fundamentally limited by the unitary nature of quantum evolution. We propose the quantum Koopman method, a data-driven framework that embeds nonlinear dynamics into a learned linear representation and implements the resulting evolution using shallow quantum circuits. This method learns Koopman observables from trajectory data, projects the lifted dynamics onto a finite-dimensional subspace, and decomposes the corresponding non-unitary propagator into parallel spectral channels. We utilize the Koopman method on a superconducting processor to simulate three distinct nonlinear systems, comprising reaction-diffusion dynamics, fluid motion on a sphere, and satellite-derived observations of Gulf Stream currents, employing up to 32 parallel circuits of 10 qubits. These quantum simulations capture the dominant multiscale patterns and statistical signatures of the underlying dynamics, and reveal a transition from performance limited by hardware noise in weakly nonlinear systems to performance limited by finite-dimensional Koopman representations as nonlinear scale interactions increase. This transition identifies a practical boundary for quantum-amenable nonlinear dynamics, establishing a hardware-validated route for simulating moderately nonlinear dynamics on near-term quantum hardware.

## Key Contributions

1. Nonlinear dynamics is ubiquitous in nature, ranging from chemical pattern formation to ocean circulation, yet its simulation on quantum computers is fundamentally limited by the unitary nature of quantum evolution.
2. We propose the quantum Koopman method, a data-driven framework that embeds nonlinear dynamics into a learned linear representation and implements the resulting evolution using shallow quantum circuits.
3. This method learns Koopman observables from trajectory data, projects the lifted dynamics onto a finite-dimensional subspace, and decomposes the corresponding non-unitary propagator into parallel spectral channels.
4. We utilize the Koopman method on a superconducting processor to simulate three distinct nonlinear systems, comprising reaction-diffusion dynamics, fluid motion on a sphere, and satellite-derived observations of Gulf Stream currents, employing up to 32 parallel circuits of 10 qubits.

## Implementation Notes

- **Keywords**: quantum, koopman
- **Categories**: quant-ph, cs.AI, physics.flu-dyn
- **Published**: 2026-07-08

## Activation Criteria

Use this skill when working on tasks involving: quantum, koopman.
