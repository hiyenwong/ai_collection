---
name: ei-network-chaos-synchrony-theory
description: >
  Extended Sompolinsky-Crisanti-Sommers (SCS) chaos theory for Excitatory-Inhibitory
  recurrent networks with target-specific inhibition. Derives mean-field theory for
  E/I networks, identifies three dynamical regimes (quiescence, asynchronous chaos,
  coherent oscillations), and shows coherent oscillations suppress chaos.
  Activation: chaos-synchrony, SCS theory, E/I balance, target-specific inhibition,
  dynamical mean-field theory, neural phase diagram, recurrent network dynamics,
  excitation-inhibition balance, neural chaos theory, 兴奋抑制平衡, 混沌同步
---

# E/I Network Chaos-Synchrony Theory

Extended SCS theory for recurrent Excitatory-Inhibitory networks with target-specific
inhibition. Provides theoretical framework for understanding dynamical regime transitions
in biological neural circuits.

## Background: Classic SCS Theory

The seminal Sompolinsky-Crisanti-Sommers (SCS) theory showed that random recurrent
networks undergo a transition from quiescence to asynchronous chaos as connectivity
strength increases. This established the link between:
- Random connectivity → dynamical instability → internally generated fluctuations

## Extended Framework: Target-Specific Inhibition

### Network Architecture
```
Two-population firing-rate network:
├── Excitatory neurons (E) → self-excitation + cross-excitation
└── Inhibitory neurons (I) → target-specific inhibition (breaks E-I balance)
```

### Key Parameters
- **g_E**: Excitatory coupling strength
- **g_I**: Inhibitory coupling strength
- **η**: Target-specificity of inhibition
- **E-I balance ratio**: Determines dynamical regime

## Three Dynamical Regimes

### Regime 1: Inhibition-Dominated / Strictly Balanced
- **Behavior**: Quiescent activity OR asynchronous chaos
- **Characteristics**:
  - Mean activity → 0 (quiescent)
  - Fluctuation-driven chaos with vanishing mean
  - Similar to classic SCS but with E/I structure

### Regime 2: Excitation-Dominated (Synchronous Chaos)
- **Behavior**: Persistent activity + synchronous chaos
- **Characteristics**:
  - Non-vanishing mean activity
  - Chaotic fluctuations around the mean
  - Stability matrix eigenvalues determine transition

### Regime 3: Excitation-Dominated (Coherent Oscillations)
- **Behavior**: Persistent activity + coherent oscillations
- **Characteristics**:
  - Periodic mean trajectory
  - **Key finding**: Chaotic fluctuations are SUPPRESSED
  - Onset of oscillations eliminates chaos (input-induced suppression)

## Critical Discovery: Chaos Suppression by Oscillations

Coherent oscillations do NOT coexist with chaotic fluctuations.
Instead, oscillation onset SUPPRESSES the chaotic component.

This is reminiscent of input-induced suppression of chaos:
- Periodic drive → entrainment → chaos suppression
- Similar to Poincaré-Lindqvist behavior in forced oscillators

## Mean-Field Theory Derivation

### Self-Consistent Equations
```
Mean activities: m_E(t), m_I(t)
Autocorrelations: C_E(τ), C_I(τ)
```

The DMF equations:
1. `m_E(t) = ∫ Dz φ(√(C_E(0))z + m_E(t))`
2. `m_I(t) = ∫ Dz φ(√(C_I(0))z + m_I(t))`
3. `C_α(τ) = g_α² ∫ Dz' Dz φ(...)φ(...)` (α ∈ {E, I})

### Stability Analysis
- **Mean-driven instability**: Eigenvalues of stability matrix cross real axis
- **Fluctuation-driven instability**: Largest Lyapunov exponent becomes positive
- **Phase boundaries**: Determined by coupling strengths and target-specificity

## Phase Diagram

```
                    g_I (inhibition)
                    ↑
                    │
    Quiescent       │     Asynchronous
    ────────────────┤     Chaos
                    │
    ────────────────┤──────────────────
    Coherent        │     Synchronous
    Oscillations    │     Chaos
                    │
                    └──────────────────→ g_E (excitation)
```

## Computational Applications

### 1. Brain State Transitions
- Sleep-wake transitions (quiescence → chaos)
- Seizure dynamics (chaos → oscillations)
- Cognitive switching (regime transitions)

### 2. Neuromodulation Control
- Neuromodulators as parameters shifting the system between regimes
- Dopamine: shifts E/I balance
- Acetylcholine: modulates target-specificity

### 3. Network Design
- Designing reservoirs for specific computational regimes
- Optimal regime for different tasks (memory vs. computation)

## Implementation Patterns

### Stability Matrix Construction
```python
import numpy as np
from scipy.linalg import eigvals

def stability_matrix(g_E, g_I, eta, m_E, m_I, phi_prime):
    """Construct stability matrix for E/I network."""
    J_EE = g_E * (1 - eta) * phi_prime(m_E)
    J_EI = -g_I * eta * phi_prime(m_I)
    J_IE = g_E * eta * phi_prime(m_E)
    J_II = -g_I * (1 - eta) * phi_prime(m_I)
    
    J = np.array([[J_EE, J_EI],
                  [J_IE, J_II]])
    return J

def check_stability(J):
    """Check stability via eigenvalue analysis."""
    eigenvalues = eigvals(J)
    max_real = max(np.real(eigenvalues))
    return max_real < 0  # Stable if all eigenvalues have negative real part
```

### Phase Diagram Computation
```python
def compute_phase_diagram(g_E_range, g_I_range, eta=0.5):
    """Compute phase diagram over parameter space."""
    phase_map = np.zeros((len(g_E_range), len(g_I_range)))
    
    for i, g_E in enumerate(g_E_range):
        for j, g_I in enumerate(g_I_range):
            m_E, m_I = solve_mean_field(g_E, g_I, eta)
            J = stability_matrix(g_E, g_I, eta, m_E, m_I)
            lyap = largest_lyapunov(g_E, g_I, m_E, m_I)
            
            if max(np.real(eigvals(J))) < 0:
                if lyap < 0:
                    phase_map[i, j] = 0  # Quiescent
                else:
                    phase_map[i, j] = 1  # Asynchronous chaos
            else:
                if lyap < 0:
                    phase_map[i, j] = 2  # Coherent oscillations
                else:
                    phase_map[i, j] = 3  # Synchronous chaos
    
    return phase_map
```

## Key Insights

1. **Target-specific inhibition** is a key control parameter for large-scale dynamics
2. **E-I structure** fundamentally changes the SCS phase diagram
3. **Coherent oscillations** emerge as a distinct regime, not just a variant of chaos
4. **Chaos suppression** by oscillations is a robust phenomenon
5. **Biological plausibility**: E/I segregation is ubiquitous in cortex

## Related Skills

- **chaos-synchrony-ei-networks**: Dynamical mean-field theory for E/I networks
- **neural-population-dynamics**: Methods for analyzing neural population dynamics
- **rhythm-switching-adaptive-time-constants-rnn**: RNN rhythm switching mechanisms
- **hermes-brain-connectivity**: Brain connectivity analysis tools

## References

- Martorell et al., "From Chaos to Synchrony in Recurrent Excitatory-Inhibitory Networks with Target-Specific Inhibition", arXiv:2605.14916 (2026)
- Sompolinsky, Crisanti, Sommers, "Chaos in Random Neural Networks", PRL (1988)
- Rajan, Abbott, Sompolinsky, "Stimulus-dependent suppression of chaos in recurrent neural networks", PRE (2010)
