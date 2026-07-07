---
name: gibbs-state-analysis
description: "Analysis of high-temperature Gibbs states with rapid mixing and external field effects. Studies entanglement structure, computational complexity, and thermalization dynamics. Use when: (1) Analyzing Gibbs states at high temperature, (2) Studying external field effects on quantum entanglement, (3) Investigating rapid mixing Lindbladians, (4) Understanding thermalization crossover scales."
---

# Gibbs State Analysis

Analysis of quantum Gibbs states with focus on rapid mixing and external field effects.

## Gibbs State Definition

### Thermal Equilibrium State

```
ρ_G = exp(-βH) / Z
Z = Tr[exp(-βH)]
β = 1/(k_B T)  (inverse temperature)
```

High temperature: β small, state接近 maximally mixed
Low temperature: β large, state接近 ground state

## Key Findings

### External Field Effect on Entanglement

**Without external field:**
- High-temperature Gibbs states are provably separable
- No entanglement beyond short-range correlations

**With external field (strength h):**
- External field induces entanglement
- Crossover scale: h ≍ β⁻¹ log(1/β)
- Entanglement emerges when field strength exceeds thermal fluctuations

### Rapid Mixing

**Quasi-local Lindbladian:**
- Describes thermalization dynamics
- Satisfies rapid mixing condition
- Convergence time: polynomial in system size

**Rapid mixing criterion:**
```
||ρ(t) - ρ_G|| ≤ ε for t = O(log(N/ε))
```

Where N is system size, ε is error tolerance.

## Mathematical Framework

### External Field Hamiltonian

```
H = H_interaction + H_field

H_field = Σ_j h_j σ_j^z  (on-site potential)
```

Upper bound: |h_j| ≤ h

### Entanglement Crossover

**Critical field strength:**
```
h_c ∼ β⁻¹ log(1/β)
```

Below h_c: Separable Gibbs state
Above h_c: Entangled Gibbs state

**Physical interpretation:**
- Thermal noise suppresses entanglement
- External field polarizes spins, reducing thermal noise
- Above crossover, polarization enables entanglement

### Lindbladian Dynamics

Thermalization Lindbladian:
```
dρ/dt = L(ρ)
L(ρ) = -i[H, ρ] + Σ_k (L_k ρ L_k† - {L_k† L_k, ρ}/2)
```

Quasi-local property:
- Lindblad operators L_k have exponentially decaying spatial extent
- Enables efficient simulation

## Implementation Patterns

### Pattern 1: Gibbs State Preparation

```python
def prepare_gibbs_state(H, beta, method='lindbladian'):
    """
    Prepare Gibbs state via thermalization.
    
    Methods:
    - 'lindbladian': Rapid mixing simulation
    - 'imaginary_time': Imaginary time evolution
    - 'metropolis': Quantum Metropolis algorithm
    """
    
    if method == 'lindbladian':
        # Construct thermalizing Lindbladian
        L = construct_rapid_mixing_lindbladian(H, beta)
        
        # Evolve to steady state
        rho = maximally_mixed_state()
        rho = evolve_lindbladian(rho, L, convergence_threshold=1e-6)
        
    elif method == 'imaginary_time':
        # Imaginary time evolution: ρ → exp(-βH)ρ
        rho = imaginary_time_evolution(H, beta)
        rho /= np.trace(rho)  # Normalize
    
    return rho
```

### Pattern 2: Entanglement Detection

```python
def detect_entanglement_in_gibbs(H, beta, h_field):
    """
    Detect if Gibbs state is entangled.
    
    Check:
    1. Compare field strength to crossover scale
    2. Compute entanglement witness
    3. Verify separability criteria
    """
    
    # Compute crossover scale
    h_c = 1.0 / beta * np.log(1.0 / beta)
    
    if h_field < h_c:
        return "Likely separable (below crossover)"
    
    # Prepare Gibbs state
    rho_G = prepare_gibbs_state(H, beta)
    
    # Test entanglement witness
    witness = compute_entanglement_witness(rho_G)
    
    if witness < 0:
        return "Entangled"
    else:
        return "Separable or witness inconclusive"
```

### Pattern 3: Rapid Mixing Verification

```python
def verify_rapid_mixing(L, system_size, target_error=1e-6):
    """
    Verify Lindbladian satisfies rapid mixing.
    
    Compute:
    - Mixing time T_mix
    - Decay rate of correlations
    - Spatial locality of Lindblad operators
    """
    
    # Simulate thermalization
    rho_init = random_initial_state()
    rho_final = evolve_lindbladian(rho_init, L)
    
    # Compute mixing time
    T_mix = compute_convergence_time(rho_init, rho_final, target_error)
    
    # Check polynomial scaling
    expected_scaling = np.log(system_size / target_error)
    
    if T_mix <= expected_scaling:
        return f"Rapid mixing verified: T_mix = {T_mix} ≤ O(log N)"
    else:
        return f"Slow mixing: T_mix = {T_mix}"
```

## Research Applications

1. **Quantum Thermodynamics**: Study thermalization dynamics
2. **Entanglement Phase Transitions**: Entanglement vs temperature
3. **Quantum Annealing**: Gibbs state preparation for optimization
4. **Error Correction**: Thermal noise analysis

## References

See [lindbladian_dynamics.md](references/lindbladian_dynamics.md) for thermalization Lindbladians.

## Source

Based on arxiv:2604.08408 - "Rapid mixing for high-temperature Gibbs states with arbitrary external fields" by Ainesh Bakshi & Xinyu Tan.