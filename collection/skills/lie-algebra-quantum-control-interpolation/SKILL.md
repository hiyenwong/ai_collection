---
name: lie-algebra-quantum-control-interpolation
description: "Lie algebra-based quantum optimal control interpolation methodology. Combines Lie group theory with feed-forward neural networks to generate quantum optimal control pulses for arbitrary unitary operations, bypassing explicit optimization at inference time. Demonstrated on superconducting qubits (2-4 qubits) and applied to Trotter propagators for neutrino collective flavor oscillations. Use when: quantum control pulse generation, scalable quantum simulation, Lie group control, neural network control mapping."
metadata:
  arxiv_id: "2606.02014"
  published: "2026-06-01"
  authors: ["Piero Luchi", "Francesco Pederiva"]
  categories: ["quant-ph"]
---

## Lie Algebra-Based Quantum Optimal Control Interpolation

**Paper**: Lie Algebra-Based Quantum Optimal Controls Interpolation (arXiv:2606.02014, 2026-06-01)

## Core Methodology

This paper presents a framework combining **Lie group theory** with **feed-forward neural networks** to efficiently generate quantum optimal control pulses for arbitrary unitary operations in superconducting qubit systems, bypassing the need for explicit optimization at inference time.

### Problem Statement

The exponential scaling of Hilbert space dimension (2^N) with qubit count makes standard quantum optimal control optimization (like GRAPE/GOAT) computationally prohibitive when large ensembles of distinct propagators must be processed — particularly acute in **Trotterized quantum simulation** where many time-step propagators need control pulses.

### Solution: Lie-NN Control Framework

**Phase 1: Lie Group Pre-computation**
- Parameterize the SU(2^N) unitary group via its Lie algebra su(2^N)
- Generate a representative set of target unitaries by sampling Lie algebra parameters
- Compute optimal control pulses for each sample using standard optimization (GRAPE)
- This creates a training dataset: {Lie parameters → optimal control pulses}

**Phase 2: Neural Network Training**
- Train feed-forward neural network to map Lie algebra parameters → control pulse sequences
- The network learns the complex nonlinear relationship between target propagators and their optimal controls
- **Key insight**: Lie algebra provides a compact, structured parameterization of the target space

**Phase 3: Inference (Zero Optimization)**
- For any new target unitary: compute its Lie algebra decomposition → feed to network → get control pulses
- **No optimization needed at inference time** — just forward pass through the trained network
- One model trained once serves as universal control-pulse generator for any compatible Hilbert space dimension

### Benchmark Results

| System | Qubits | Reconstruction Fidelity | Notes |
|--------|--------|------------------------|-------|
| Superconducting | 2 | High | Random propagators |
| Superconducting | 3 | High | Random propagators |
| Superconducting | 4 | High | Random propagators |
| Neutrino system | 4 | High | Collective flavor oscillations (Trotter propagators) |

**Physical benchmark**: Successfully reconstructed control pulses for Trotter propagators of a neutrino system undergoing collective flavor oscillations — demonstrating generalization across system types.

### Key Technical Details

**Lie Algebra Parameterization**:
- SU(d) has d²-1 generators (Pauli strings for qubit systems)
- Any unitary U = exp(i Σ θ_k G_k) where G_k are Lie algebra generators
- The coefficients θ_k form a compact representation of the target

**Network Architecture**:
- Input: Lie algebra parameters (θ₁, ..., θ_{d²-1})
- Output: Control pulse amplitudes at each time step
- Feed-forward with sufficient depth to capture nonlinear mapping

**Hardware Independence**:
- Model trained on hardware-specific random propagators
- Single model serves as universal generator for any target quantum system of compatible dimension
- Hardware-specific control constraints baked into training data

### Reusable Patterns

1. **Lie-NN Decoupling**: Separate the mathematical structure (Lie algebra) from the learning problem (neural mapping). Use Lie theory for target parameterization, not for pulse generation.

2. **Offline Optimization → Online Inference**: Move all expensive computation to offline training phase. Inference is just forward pass.

3. **Universal Control Generator**: One model trained on random propagators generalizes to physically meaningful targets (Trotter steps, Hamiltonian evolution, etc.)

4. **Structured Parameterization**: Lie algebra provides optimal compact representation — no redundant parameters, covers all reachable unitaries.

### Comparison with Related Methods

| Method | Offline Cost | Inference Cost | Scalability | Generalization |
|--------|-------------|----------------|-------------|----------------|
| GRAPE/GOAT | Per-target O(iterations) | Per-target | Poor (per-target) | N/A |
| RL-based control | Training | Forward pass | Moderate | Limited |
| **Lie-NN (this work)** | Pre-compute + train | **Forward pass** | **Good** | **Cross-system** |
| IRD-GrAPE | Per-target | Per-target | Moderate | System-specific |

### Application Scenarios

- **Trotterized Hamiltonian simulation**: Generate control pulses for all Trotter steps in one shot
- **Quantum algorithm compilation**: Map circuit gates to hardware pulses efficiently
- **Pulse library generation**: Build comprehensive pulse libraries for quantum compilers
- **Adaptive quantum simulation**: Rapidly switch between different simulated Hamiltonians

## Pitfalls

- **Hilbert space dimension limit**: Currently demonstrated up to 4 qubits. SU(2^N) has 4^N - 1 parameters — input dimension grows exponentially.
- **Hardware-specific**: Training data must match target hardware's control constraints and noise model.
- **Fidelity varies by region**: Some Lie algebra parameter combinations yield higher reconstruction fidelity than others — may need adaptive sampling.
- **Not a replacement for optimal control**: Still needs initial optimization to generate training data. Benefits accrue when many propagators need pulses.

## Activation

quantum control, Lie algebra control, quantum optimal control interpolation, GRAPE neural network, scalable quantum simulation, Trotter propagator control, feed-forward quantum control

## Cross-references

- [[quantum-optimal-control-irrep-distillation]] - IRD method for Dicke manifold control in Rydberg atom arrays (complementary: handles leakage, uses GrAPE optimization)
- [[drl-quantum-optimal-control]] - Deep reinforcement learning for quantum optimal control
- [[quantum-control-engineering]] - Engineering patterns for reliable quantum control
- [[pinn-quantum-pulse-optimization]] - Physics-informed neural networks for quantum pulse optimization
