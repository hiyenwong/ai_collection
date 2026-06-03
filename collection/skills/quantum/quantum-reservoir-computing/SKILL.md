---
name: quantum-reservoir-computing
category: quantum-ml
description: Quantum Reservoir Computing (QRC) framework for chaotic time-series forecasting using quantum dynamics as the reservoir. Combines classical readout training with quantum feature representations across distributed and single-qubit architectures.
trigger_words: quantum reservoir computing, time series forecasting, quantum dynamics, echo state network, quantum machine learning, distributed quantum
version: 1.0.0
created: 2026-05-12
source: arXiv:2605.04991v1
authors: Ioannis Liliopoulos, Georgios D. Varsamis, Konstantinos Rallis, Evangelos Tsipas, Ioannis G. Karafyllidis, Georgios Ch. Sirakoulis, Panagiotis Dimitrakis
---

# Quantum Reservoir Computing (QRC)

## Core Methodology

Quantum Reservoir Computing (QRC) leverages quantum system dynamics as a computational reservoir for time-series forecasting. Key insight: the natural evolution of a quantum system under input driving provides a rich, high-dimensional feature space that can be exploited by training only a simple classical readout layer.

### Why QRC?
- **No backpropagation**: Avoids training deep quantum circuits; only the classical readout is trained
- **Rich features**: Quantum superposition and entanglement provide exponentially large feature spaces
- **Hardware efficient**: Shallow circuits suffice since we don't need gradient flow through the reservoir
- **Distributed scalability**: Can span multiple quantum processors for larger reservoirs

## Architecture Variants (Benchmarked)

### 1. Single-Qubit Reservoir
- One qubit driven by time-series input
- Simplest architecture, minimal hardware requirements
- Suitable for low-dimensional time series
- Limited feature space dimensionality

### 2. Multi-Qubit Single-Processor Reservoir
- Multiple qubits on one quantum processor with inter-qubit coupling
- Entanglement between qubits enriches feature space
- Best for current NISQ devices
- Exponential feature space in number of qubits

### 3. Distributed Quantum Reservoir
- Multiple quantum processors connected classically
- Each processor runs its own reservoir
- Classical post-processing combines outputs
- Enables scaling beyond single-processor qubit limits

### 4. Hybrid Classical-Quantum Reservoir
- Classical RNN components combined with quantum reservoir
- Best of both worlds: quantum expressivity + classical processing
- Most flexible architecture for complex time series

## Implementation Steps

### Step 1: Input Encoding
- Map classical time-series values to quantum circuit parameters
- Common encoding: amplitude encoding, angle encoding, or data re-uploading
- For angle encoding: input x maps to rotation angle R_x(θ) on qubit

### Step 2: Reservoir Dynamics
- Apply fixed (non-trainable) quantum circuit layers
- Include entangling gates between qubits for multi-qubit architectures
- Use randomized or structured circuit topology
- Key: dynamics must be rich enough to separate different input histories

### Step 3: Measurement and Feature Extraction
- Measure qubits in computational basis (or other bases)
- Collect measurement statistics as feature vector
- Optionally measure multiple observables for richer features
- Feature vector dimension = number of measurable observables

### Step 4: Classical Readout Training
- Use linear regression, Ridge regression, or simple neural network
- Train readout mapping: features → prediction target
- Only this layer is trained; quantum reservoir is frozen
- Regularization is important to prevent overfitting on noisy quantum measurements

### Step 5: Distributed Architecture (if applicable)
- Run reservoir on multiple quantum processors in parallel
- Collect features from each processor
- Concatenate or weighted-combine feature vectors
- Train unified readout on combined features

## Key Hyperparameters

- **Number of qubits**: Controls feature space dimensionality (2^n for n qubits)
- **Circuit depth**: Deeper circuits capture longer temporal dependencies
- **Input encoding scheme**: Affects how classical data maps to quantum states
- **Measurement basis**: Determines which features are extracted
- **Regularization strength**: Critical for noisy quantum measurements
- **Temporal window size**: How many past time steps influence current state

## Advantages

- **Training efficiency**: No quantum gradient computation needed
- **NISQ-friendly**: Works with shallow circuits and noisy hardware
- **Scalable**: Can distribute across multiple quantum processors
- **Versatile**: Applicable to any time-series forecasting task

## Pitfalls

- **Noise sensitivity**: Quantum measurement noise propagates to readout; use averaging
- **Input encoding bottleneck**: Limited qubit count restricts encoding dimensionality
- **Temporal decay**: Quantum reservoir memory has finite decay time; tune circuit depth accordingly
- **Readout overfitting**: Simple readout may overfit to measurement noise; use cross-validation
- **Hardware connectivity**: Qubit connectivity constraints limit circuit topology

## Verification

- Benchmark against classical reservoir computing (ESN) on same tasks
- Compare different architectures (single vs. multi-qubit vs. distributed)
- Test on standard time-series benchmarks (Mackey-Glass, Lorenz system)
- Evaluate noise robustness by adding simulated hardware noise
- Verify scalability: does performance improve with more qubits?
