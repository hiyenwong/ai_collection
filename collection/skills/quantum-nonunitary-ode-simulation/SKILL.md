---
name: quantum-nonunitary-ode-simulation
description: "Quantum algorithm methodology for simulating nonunitary dynamics governed by nonautonomous linear ODEs without requiring explicit propagator knowledge, using quantum hardware dilation."
---

# Quantum Nonunitary ODE Simulation

## Description

Methodology for implementing quantum algorithms that simulate nonunitary dynamics governed by nonautonomous linear ordinary differential equations (ODEs) of the form dv/dt = A(t)v, where A(t) is non-skew-symmetric. Unlike existing approaches that require a priori knowledge of the explicit nonunitary propagator, this algorithm performs dilation directly on quantum hardware.

## Activation Keywords

- quantum nonunitary simulation
- nonautonomous ode quantum
- quantum algorithm dilation
- quantum ode solver
- 量子非幺正模拟
- non-skew-symmetric quantum

## Tools Used

- terminal: Execute quantum circuit simulation and compilation
- read_file: Read quantum algorithm specifications
- write_file: Create quantum circuits and simulation scripts
- skill_view: Load related quantum computing and ODE solving skills

## Core Concepts

### The Nonunitary Dynamics Problem

Nonautonomous linear ODEs: dv/dt = A(t)v where A(t) is non-skew-symmetric
- Common in open quantum systems, economic modeling, fluid dynamics
- Quantum hardware natively implements unitary transformations
- Nonunitary dynamics require embedding (dilation) in larger unitary system

### Existing Approach Limitations

Current quantum algorithms assume the nonunitary propagator is known in closed form and:
1. Calculate propagator on classical computer at each time step
2. Manipulate propagator classically
3. Embed into quantum circuit
This becomes intractable for time-dependent systems.

### New Algorithm Approach

The proposed algorithm:
1. Does NOT require a priori knowledge of the explicit propagator
2. Performs dilation directly on quantum hardware
3. Handles time-dependent A(t) without classical intermediate steps
4. Combines dilation techniques with quantum-native propagation

## Instructions for Agents

### Step 1: Problem Characterization

1. Identify the ODE system: dv/dt = A(t)v
2. Verify A(t) is non-skew-symmetric (nonunitary dynamics)
3. Determine if A(t) is time-dependent (nonautonomous)

### Step 2: Select Algorithm Type

1. If propagator known in closed form → use existing dilation methods
2. If propagator unknown or time-dependent → use hardware dilation algorithm

### Step 3: Implement Quantum Dilation

1. Map the nonunitary system to a larger Hilbert space
2. Construct unitary embedding that preserves dynamics
3. Implement dilation gates directly on quantum hardware
4. Verify correctness against classical simulation for small systems

### Step 4: Validate Results

1. Compare quantum simulation output with classical solver
2. Check conservation laws and physical constraints
3. Analyze scaling behavior with system size

## Error Handling

### Dilation Dimension Explosion

The dilation embedding can increase qubit requirements exponentially. Mitigation:
- Use approximate dilation for large systems
- Exploit sparsity in A(t)
- Consider hybrid classical-quantum approaches

### Hardware Noise Sensitivity

Nonunitary simulations are sensitive to quantum hardware noise. Mitigation:
- Use error mitigation techniques
- Validate against noise-free classical simulation
- Consider noise-resilient dilation constructions

## Resources

- arXiv: 2605.29052 - "A Quantum Algorithm for Simulating Nonunitary Dynamics Governed by Nonautonomous Linear Ordinary Differential Equations"
- Related skills: quantum-linear-differential-equation, carleman-vqls
