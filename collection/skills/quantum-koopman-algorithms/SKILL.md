---
name: quantum-koopman-algorithms
description: "Quantum Koopman Algorithms (QKAs) framework for simulating linear quantum and nonlinear classical system dynamics via observable-space methods. Includes Dynamic-QKA for initial-value problems and Spectral-QKA for eigenvalue analysis. arXiv: 2605.19054."
---

# Quantum Koopman Algorithms (QKAs)

**arXiv**: 2605.19054 (May 2026)
**Authors**: David Jennings, Kamil Korzekwa, Matteo Lostaglio, Guoming Wang
**Category**: quant-ph

## Overview

Observable-space framework of Quantum Koopman Algorithms (QKAs) for simulating dynamics of both linear quantum and nonlinear classical systems, based on approximately closed sets of observables and efficient coherent encodings of their Koopman-driven evolution.

## Two Strands of QKAs

### 1. Dynamic-QKA (Initial-Value Problem)
- Solves observables dynamics evolution
- For N free fermions linearly coupled to a bath: gate cost O(polylog(N))
- Exponential improvement over classical methods
- Reconstructs heat flows and decay rates

### 2. Spectral-QKA (Eigenvalue Analysis)
- Eigenvalue analysis of the Koopman operator
- Extracts eigen-frequencies of late-time nonlinear dynamics
- Uses windowed quantum ODE-solver for spectral methods

## Key Applications

### Free Fermion-Bath Systems
- Construct quantum algorithms with gate cost O(polylog(N))
- Exponential speedup vs classical simulation
- Application: reconstructing heat flows and decay rates in open quantum systems

### Nonlinear Classical Dynamics
- Novel nonlinear interaction-picture quantum algorithm
- Enables perturbative expansions around solvable nonlinear reference flows
- Goes beyond existing approaches that only apply to weakly nonlinear systems

### Spectral Methods
- Windowed quantum ODE-solver for extracting eigen-frequencies
- Applicable to late-time nonlinear dynamics analysis

## Activation
quantum koopman, QKA, observable-space dynamics, nonlinear dynamics simulation, quantum ODE solver, spectral analysis quantum

## Pitfalls
- Koopman operator approximation requires approximately closed sets of observables
- Gate cost O(polylog(N)) applies to specific system classes (free fermions + bath)
- Perturbative expansions need solvable nonlinear reference flows
- Windowed approach needed for late-time spectral extraction

## Reusable Patterns

### Pattern 1: Observable-Space Encoding
Instead of state-space simulation, encode dynamics in observable space using Koopman operator theory. This enables quantum algorithms to handle nonlinear classical systems that are otherwise intractable.

### Pattern 2: Two-Stage Algorithm Design
Separate initial-value problems (Dynamic-QKA) from spectral analysis (Spectral-QKA). Each uses different quantum primitives optimized for its task type.

### Pattern 3: Nonlinear Interaction Picture
Extend the interaction picture concept from quantum mechanics to handle nonlinear reference flows, enabling perturbative treatment of classically nonlinear systems on quantum hardware.
