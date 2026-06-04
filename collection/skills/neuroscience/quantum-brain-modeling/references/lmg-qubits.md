# Dynamic Synaptic Modulation of LMG Qubits — Detail Reference

**Source**: arXiv:2602.16003 (2026-02-17)

## LMG Hamiltonian with Synaptic Feedback

```
H = - (λ/N) Σᵢⱼ σᵢᶻ σⱼᶻ - h Σᵢ σᵢˣ + f(s) · Mᶻ
```

- **N**: Number of qubits (neuronal population size)
- **λ**: All-to-all coupling strength
- **h**: Transverse field (external drive)
- **Mᶻ**: Collective magnetization operator
- **f(s)**: Activity-dependent synaptic feedback function
- **s**: Synaptic efficacy variable with homeostatic dynamics

## Synaptic-Efficacy Feedback Mechanism

Key innovation: homeostatic control via dynamic synaptic modulation.
- Synaptic efficacy `s` adapts based on population activity
- Provides negative feedback stabilizing collective dynamics
- Implements activity-dependent homeostasis — prevents runaway excitation
- Creates stable set points for population activity

## Three Computational Primitives

| Primitive | Mechanism | Application |
|-----------|-----------|-------------|
| **Stable Set Points** | Homeostatic feedback stabilizes magnetization | Memory storage, attractor states |
| **Controllable Oscillations** | Feedback-induced limit cycles | Rhythmogenesis, temporal coding |
| **Size-Dependent Robustness** | Collective mode stability scales with N | Scalable quantum computation |

## Phase Structure Insights

1. **Feedback Expands Paramagnetic Phase**: Synaptic feedback substantially expands the paramagnetic region at the expense of ferromagnetic phases compared to feedback-free LMG.
2. **Longitudinal Field Coupling**: When synaptic feedback couples to longitudinal magnetization, the effect on phase boundaries is markedly enhanced.
3. **Critical Boundary Displacement**: Homeostatic control displaces critical boundaries, enabling tunable access to different quantum phases.
4. **Scalability**: Collective mode stability increases with population size N, providing size-dependent robustness.

## Synaptic Efficacy Update Rule

```python
def synaptic_efficacy_update(s_current, population_activity, target_activity, learning_rate, decay):
    error = population_activity - target_activity
    ds = -learning_rate * error - decay * s_current
    return s_current + ds
```

## Pitfalls
- Finite-size effects significant for N < 50; use exact diagonalization for small populations
- Excessive feedback gain causes oscillatory instability; ensure stability criteria on learning_rate and decay
- Mean-field analysis breaks down for small N
- Synaptic feedback dynamics assumed classical — full quantum treatment pending
- All-to-all connectivity assumption may not reflect biological neural wiring
