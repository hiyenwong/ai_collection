---
name: finite-temp-quantum-krylov
description: "Finite-temperature quantum Krylov method for computing thermal properties of quantum many-body systems from real-time overlaps. Use when analyzing quantum many-body systems at finite temperatures, computing thermal observables, or avoiding thermal state preparation in quantum simulations."
---

# Finite-Temperature Quantum Krylov Method

Method for evaluating finite-temperature properties of quantum many-body systems without requiring thermal-state preparation at each target temperature.

## Core Concept

Traditional quantum approaches require thermal-state preparation at each target temperature, making low-temperature calculations demanding in terms of circuit depth and computational cost. This method uses real-time overlaps to extract finite-temperature properties.

## Activation Keywords

- finite-temperature quantum
- quantum Krylov method
- thermal properties quantum
- quantum many-body temperature
- real-time overlaps
- thermal state preparation alternative

## Mathematical Framework

### Quantum Krylov Subspace

The method constructs a Krylov subspace from real-time evolution:

```
|ψ(t)⟩ = e^(-iHt)|ψ₀⟩
```

Where:
- H is the Hamiltonian
- |ψ₀⟩ is an initial state (typically the ground state or a simple product state)
- t is real time

### Finite-Temperature Observables

Thermal expectation values are computed via:

```
⟨O⟩_β = Tr[O e^(-βH)] / Tr[e^(-βH)]
```

Where β = 1/(k_B T) is the inverse temperature.

### Real-Time Overlap Approach

Instead of preparing thermal states, the method:
1. Evolves initial states in real time
2. Computes overlaps between time-evolved states
3. Extracts thermal information from these overlaps using analytical continuation or spectral methods

## Implementation Steps

### Step 1: State Preparation

Prepare an initial state |ψ₀⟩:
- Ground state (for low-temperature physics)
- Random product state (for high-temperature regime)
- Symmetry-preserving initial state

### Step 2: Real-Time Evolution

Evolve the state for discrete time steps:

```python
# Pseudocode
for t in time_grid:
    |ψ(t)⟩ = time_evolve(H, |ψ₀⟩, t)
    overlaps[t] = compute_overlap(|ψ(t)⟩, |ψ₀⟩)
```

### Step 3: Overlap Collection

Collect real-time overlap data:
- ⟨ψ₀|ψ(t)⟩ (survival probability)
- ⟨ψ(t)|O|ψ(t)⟩ (time-dependent observables)
- Connected correlation functions

### Step 4: Thermal Extraction

Extract finite-temperature properties:

1. **Spectral Function Reconstruction**
   - Use maximum entropy or Prony methods
   - Extract density of states from overlap decay

2. **Partition Function Estimation**
   ```
   Z(β) ≈ Σ_n |⟨ψ₀|n⟩|² e^(-βE_n)
   ```

3. **Observable Computation**
   ```
   ⟨O⟩_β = Σ_n ⟨n|O|n⟩ |⟨ψ₀|n⟩|² e^(-βE_n) / Z(β)
   ```

## Advantages

1. **No Thermal State Preparation**: Avoids costly imaginary-time evolution
2. **Single Real-Time Evolution**: One time evolution yields all temperatures
3. **Lower Circuit Depth**: Real-time evolution often shallower than imaginary-time
4. **Continuous Temperature Access**: Extract any temperature from same data

## Limitations

1. **Analytic Continuation**: Requires careful handling of ill-posed inversion
2. **Signal-to-Noise**: Long-time overlaps may have poor signal quality
3. **Initial State Dependence**: Results depend on choice of |ψ₀⟩
4. **Spectral Resolution**: Limited by maximum evolution time

## Applications

- **Condensed Matter Physics**: Study quantum phase transitions at finite T
- **Quantum Chemistry**: Finite-temperature properties of molecules
- **Quantum Magnetism**: Thermal properties of spin systems
- **High-Energy Physics**: Finite-temperature field theories

## Tools Used

- exec: Run quantum simulation code (Qiskit, Cirq, PennyLane)
- python: Numerical analysis of overlaps, analytic continuation
- write: Save computed thermal properties, analysis results

## References

- arXiv:2604.10543v1 (2026) - "Finite-temperature quantum Krylov method from real-time overlaps"
- Quantum Krylov methods literature
- Maximum entropy methods for spectral reconstruction

## Related Skills

- quantum-simulation: General quantum simulation techniques
- quantum-many-body: Quantum many-body physics methods
- thermal-quantum-states: Thermal state preparation and manipulation
