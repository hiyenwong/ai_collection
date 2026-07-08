---
name: low-depth-nonmarkovian-simulation
description: "Low-depth quantum simulation of non-Markovian dynamics using trajectory mixing — trades entangling gates for statistical mixture of independent pure state trajectories to reduce circuit depth on NISQ hardware. Activation: non-Markovian simulation, trajectory mixing, low-depth quantum simulation, memory channel simulation, mixed unitary channels, near-term quantum hardware."
---

## Overview

This skill provides a methodology for simulating non-Markovian quantum dynamics and memory channels on near-term quantum hardware using trajectory mixing. The key insight is that for mixed unitary channels, entangling gate overhead can be traded for statistical mixtures of independent pure state trajectories, drastically reducing circuit depth while maintaining fidelity.

## Core Principle

### Trajectory Mixing for Mixed Unitary Channels

A mixed unitary channel can be decomposed as:
```
ρ → Σᵢ pᵢ Uᵢ ρ Uᵢ†
```

Instead of implementing this as a single coherent circuit with ancilla qubits (requiring entangling gates), we sample trajectories independently:
1. Sample index i with probability pᵢ
2. Apply unitary Uᵢ to the system
3. Repeat and average over many runs

This trades circuit depth for shot count — a favorable tradeoff on noisy hardware.

## Implementation Steps

### Step 1: Identify Mixed Unitary Structure

```python
from qiskit import QuantumCircuit
from qiskit.quantum_info import Choi, Kraus

def is_mixed_unitary(channel_matrix):
    """Check if a channel admits a mixed unitary decomposition"""
    choi = Choi(channel_matrix)
    # Decompose into Kraus operators
    kraus_ops = kraus_decomposition(choi)
    # Check if each Kraus operator is proportional to a unitary
    return all(is_unitary_proportional(K) for K in kraus_ops)
```

### Step 2: Trajectory Mixing Circuit

```python
def trajectory_mixing_circuit(unitaries, probabilities, n_shots):
    """
    Implement trajectory mixing for non-Markovian simulation.
    
    Args:
        unitaries: List of unitary circuits [U_1, U_2, ...]
        probabilities: Sampling probabilities [p_1, p_2, ...]
        n_shots: Number of independent trajectory runs
    """
    # No ancilla needed — just sample and apply
    results = []
    for _ in range(n_shots):
        idx = np.random.choice(len(unitaries), p=probabilities)
        circ = unitaries[idx]
        results.append(execute(circ))
    return average_results(results)
```

### Step 3: Non-Markovian Memory Channel Simulation

```python
def simulate_memory_channel(initial_state, time_steps, unitaries_per_step, probs_per_step):
    """
    Simulate non-Markovian dynamics with memory using trajectory mixing.
    
    Each time step applies a different mixed unitary channel,
    with correlations between steps capturing memory effects.
    """
    state = initial_state
    trajectory = []
    for t in range(time_steps):
        idx = np.random.choice(len(unitaries_per_step[t]), 
                               p=probs_per_step[t])
        state = unitaries_per_step[t][idx] @ state @ unitaries_per_step[t][idx].conj().T
        trajectory.append(state)
    return trajectory
```

### Step 4: Fidelity Benchmarking

```python
def benchmark_fidelity(target_state, simulated_state, noise_model):
    """
    Compare trajectory mixing vs ancilla-based implementation.
    Returns state fidelity and quantum correlation preservation metrics.
    """
    fidelity = state_fidelity(target_state, simulated_state)
    # Measure entanglement preservation
    concurrence = compute_concurrence(simulated_state)
    return {
        'fidelity': fidelity,
        'concurrence': concurrence,
        'circuit_depth': simulated_state.circuit_depth(),
        'entangling_gates': simulated_state.entangling_gate_count()
    }
```

## When to Use

- Simulating open quantum systems on NISQ hardware
- Non-Markovian dynamics with limited qubit resources
- Memory channel simulation without ancilla overhead
- Long-time quantum evolution simulations
- When entangling gate errors dominate other noise sources

## Advantages

1. **Circuit Depth Reduction**: Eliminates ancilla qubits and entangling gates for state preparation
2. **Noise Resilience**: Fewer entangling gates → higher state fidelity on noisy hardware
3. **Scalability**: Shot count scales linearly; circuit depth stays constant
4. **Quantum Correlation Preservation**: Better preservation of entanglement and coherence

## Limitations

- Only applicable to mixed unitary channels
- Requires more shots (statistical overhead)
- Not suitable for channels with non-unitary Kraus operators

## Key Reference

- arXiv:2607.05519 — "Low-depth simulation of non-Markovianity under quantum hardware noise"
- Noise model: Realistic hardware-calibrated noise profiles
- Valid for: Mixed unitary channels, memory channels, non-Markovian dynamics
