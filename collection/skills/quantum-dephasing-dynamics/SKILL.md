---
name: quantum-dephasing-dynamics
description: "Analysis of dephasing effects on quantum correlations and coherence dynamics in oscillating quantum systems. Covers quantum steering, logarithmic negativity, and coherence measures under environmental decoherence. Use when analyzing quantum system robustness to noise, studying decoherence in quantum oscillators/neutrino systems, or evaluating quantum resource preservation."
---

# Quantum Dephasing Dynamics

Methodology from Bachain, Jaloum & Amazioug (2026) "Dephasing Effects on the Dynamical Evolution of Quantum Correlations and Coherence in Neutrino Oscillations" (arXiv:2605.05015).

## Core Framework

Analyze quantum resource dynamics under dephasing using three complementary measures:

### 1. Quantum Steering

- Quantifies the ability of one subsystem to remotely prepare states of another
- More robust than entanglement under certain noise conditions
- Directional: A→B steering ≠ B→A steering

### 2. Logarithmic Negativity

- Entanglement monotone for mixed states
- Computed from partial transpose of density matrix
- N(ρ) = log₂||ρ^{T_A}||₁

### 3. l₁-Norm Coherence

- Sum of absolute values of off-diagonal density matrix elements
- C_{l₁}(ρ) = Σ_{i≠j} |ρ_{ij}|
- Measures superposition strength in a reference basis

## Dephasing Model

Dephasing destroys off-diagonal elements of the density matrix:

```
ρ(t) = Σ_{ij} ρ_{ij}(0) · e^{-γ_{ij}·t} · |i⟩⟨j|
```

where γ_{ij} is the dephasing rate between states |i⟩ and |j⟩.

## Analysis Pipeline

```python
def analyze_quantum_dephasing(rho_0, hamiltonian, dephasing_rates, time_points):
    """
    Analyze quantum resource evolution under dephasing.
    
    Returns:
        Dict with steering, negativity, coherence vs time
    """
    results = {
        'steering_AB': [],
        'steering_BA': [],
        'negativity': [],
        'coherence_l1': [],
        'time': time_points
    }
    
    for t in time_points:
        # 1. Evolve density matrix under dephasing
        rho_t = evolve_dephasing(rho_0, hamiltonian, dephasing_rates, t)
        
        # 2. Compute quantum resources
        results['steering_AB'].compute_steering(rho_t, direction='AB')
        results['steering_BA'].compute_steering(rho_t, direction='BA')
        results['negativity'].compute_negativity(rho_t)
        results['coherence_l1'].compute_l1_coherence(rho_t)
    
    return results
```

## Key Findings

1. **Steering sudden death**: Quantum steering can vanish at finite time
2. **Negativity decay rate**: Depends on initial state structure
3. **Coherence hierarchy**: Different coherence measures decay at different rates
4. **Oscillation modulation**: System dynamics modulate dephasing effects

## When to Use

| Scenario | Recommended Analysis |
|----------|---------------------|
| Quantum communication channel | Steering + coherence |
| Quantum computation robustness | Negativity + coherence |
| Sensor noise characterization | All three measures |
| State preparation quality | Coherence l₁-norm |

## Pitfalls

- Steering criteria are sufficient but not necessary conditions
- l₁-coherence is basis-dependent
- Dephasing model assumes Markovian environment
- Non-Markovian effects can cause coherence revival

## Activation Keywords

- quantum dephasing, decoherence analysis
- quantum steering, logarithmic negativity
- coherence measures, quantum resources
- quantum noise, oscillator decoherence
