---
name: global-mean-amplitude-snn-cim
description: "Global mean-amplitude feedback-enhanced spiking neural network coherent ising machine (GFSNN-CIM) with physics-driven amplitude stabilization. Solves Max-Cut with 27% improvement vs conventional SNN-CIM, validated on traffic assignment problems. Based on Jiang, Ma, Wang & Wang (arXiv: 2509.13917). Use when solving combinatorial optimization with spiking neural networks, implementing coherent ising machines, or applying mean-amplitude feedback stabilization to SNN optimizers."
---

# Global Mean-Amplitude Enhanced SNN Coherent Ising Machine

Physics-driven amplitude stabilization for spiking neural network-based coherent Ising machines. Based on Jiang et al. (arXiv: 2509.13917).

## Core Methodology

- Global mean-amplitude feedback enhances spiking neural network CIM
- Physics-driven amplitude stabilization prevents oscillation divergence
- 27% improvement in Max-Cut solution success rates vs conventional SNN-CIM
- Validated on traffic assignment problems (generalizes beyond Max-Cut)

## Architecture

1. SNN encodes Ising model spins as neuron states
2. Global mean-amplitude feedback stabilizes collective dynamics
3. Physics-driven amplitude correction enforces energy landscape convergence
4. Readout maps final spiking states to optimization solution

## When to Use

- Combinatorial optimization (Max-Cut, graph partitioning, traffic assignment)
- Coherent Ising Machine implementations
- Spiking neural network optimizers
- Physics-inspired neural computation
- Problems requiring amplitude stabilization in oscillatory networks

## Key Advantages

1. 27% success rate improvement over baseline SNN-CIM
2. Generalizes beyond Max-Cut to real-world optimization
3. Physics-driven (not learned) stabilization — no training required
4. Compatible with existing SNN hardware implementations

## Related Concepts

- Coherent Ising Machines (CIM)
- Spiking Neural Networks (SNN)
- Combinatorial Optimization
- Mean-Field Feedback
- Amplitude Stabilization

**Activation**: coherent ising machine, GFSNN-CIM, mean-amplitude feedback, spiking neural optimizer, physics-driven stabilization, Max-Cut SNN, arXiv:2509.13917
