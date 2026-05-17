---
name: ei-network-chaos-synchrony-theory
description: >
  Extended Sompolinsky-Crisanti-Sommers (SCS) chaos theory framework for
  excitatory-inhibitory (E-I) recurrent networks with target-specific
  inhibition. Covers dynamical mean-field analysis, phase diagrams,
  mean-driven and fluctuation-driven instabilities, and the suppression
  of chaos by coherent oscillations. Use when analyzing E/I balance in
  neural networks, studying chaos-to-order transitions in recurrent
  networks, modeling target-specific inhibition effects, extending SCS
  theory to structured networks, or investigating synchronous vs
  asynchronous chaotic regimes.
---

# Extended SCS Chaos Theory for E-I Networks

Based on Martorell et al. (2026), arXiv:2605.14916. Extends the seminal
Sompolinsky-Crisanti-Sommers (SCS) theory from random homogeneous recurrent
networks to two-population firing-rate networks with segregated excitatory
and inhibitory neurons and target-specific inhibitory couplings.

## Core Framework

### Model Architecture

```
dx_i/dt = -x_i + sum_j J_ij * phi(x_j)
```

Two populations (E, I) with connectivity matrices having variances:
- **g_EE**: Excitatory-to-excitatory variance
- **g_EI**: Excitatory-to-inhibitory variance  
- **g_IE**: Inhibitory-to-excitatory variance
- **g_II**: Inhibitory-to-inhibitory variance

Key innovation: **target-specific inhibition** breaks the standard
excitation-inhibition balance assumption, allowing differential targeting.

### Dynamical Mean-Field Theory (DMFT)

Self-consistent equations for macroscopic observables:

```
m_a(t) = <phi_a(x_a(t))>_a  (mean activity of population a)
C_a(t,t') = <x_a(t) x_a(t')>_a  (autocorrelation)
```

Where `a ∈ {E, I}` and the average is over disorder realizations.

### Phase Diagram — Three Classes

**1. Inhibition-dominated / Strictly balanced:**
- Only quiescent activity or asynchronous chaos
- No persistent states

**2. Excitation-dominated (two sub-regimes):**
- Persistent activity + synchronous chaos (non-vanishing mean activity)
- Persistent activity + coherent oscillations
- Determined by stability-matrix eigenvalues

**3. Key finding: Coherent oscillations SUPPRESS chaos**
- Chaotic fluctuations around periodic mean trajectory do NOT coexist
- Onset of coherent oscillations eliminates the chaotic component
- Input-induced suppression of chaos mechanism

## Stability Analysis

```python
import numpy as np
from scipy.integrate import odeint

def stability_matrix(g_EE, g_EI, g_IE, g_II, m_E, m_I):
    """Compute Jacobian at fixed point for E-I network."""
    phi_prime_E = 1 - m_E**2  # tanh derivative
    phi_prime_I = 1 - m_I**2
    J = np.array([
        [g_EE * phi_prime_E - 1, -g_EI * phi_prime_I],
        [g_IE * phi_prime_E, -g_II * phi_prime_I - 1]
    ])
    return J

def classify_regime(g_EE, g_EI, g_IE, g_II, m_E=0.1, m_I=0.1):
    """Classify dynamical regime from connectivity parameters."""
    J = stability_matrix(g_EE, g_EI, g_IE, g_II, m_E, m_I)
    eigvals = np.linalg.eigvals(J)
    max_real = max(eigvals.real)

    if max_real < -0.01:
        return "quiescent"
    elif max_real < 0.01:
        if any(eigvals.imag != 0):
            return "coherent_oscillations"
        else:
            return "asynchronous_chaos"
    else:
        if any(eigvals.imag != 0):
            return "synchronous_chaos"
        else:
            return "persistent_activity"
```

## DMFT Self-Consistent Iteration

```python
def dmft_iteration(g, n_steps=1000, dt=0.1, max_iter=50, tol=1e-6):
    """Iterative DMFT for autocorrelation C(t)."""
    C = np.ones(n_steps)
    
    for iteration in range(max_iter):
        noise = generate_gaussian_process(C, n_steps, dt)
        x = np.zeros(n_steps)
        for t in range(1, n_steps):
            dx = -x[t-1] * dt + phi(x[t-1]) * dt + noise[t] * dt
            x[t] = x[t-1] + dx
        
        C_new = np.zeros(n_steps)
        for tau in range(n_steps):
            C_new[tau] = np.mean(x[:n_steps-tau] * x[tau:])
            
        if np.max(np.abs(C_new - C)) < tol:
            break
        C = 0.5 * (C + C_new)
    
    return C
```

## Key Insights

1. **Target-specific inhibition is a control parameter**: Determines phase boundary between chaos and order
2. **Chaos suppression by oscillations**: Oscillations actively suppress chaotic fluctuations (no coexistence)
3. **Phase transition control**: Tuning g_IE/g_EI ratio drives networks between computational regimes
4. **Generalization path**: Extends to multi-population networks, structured connectivity, time-dependent inputs

## Activation Keywords

- E-I network chaos
- excitatory inhibitory balance
- SCS theory extension
- Sompolinsky Crisanti Sommers
- target-specific inhibition
- chaos synchrony transition
- dynamical mean field neural
- recurrent network phase diagram
- asynchronous chaos neural
- fluctuation-driven instability
