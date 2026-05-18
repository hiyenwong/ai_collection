---
name: leggett-garg-neural-dynamics
description: "Methodology for testing Leggett-Garg inequalities in neural dynamics to probe non-diffusive stochastic structure in single neurons. Use when studying whether neural computation exhibits non-classical behavior, analyzing stochastic models of neural dynamics beyond cable-equation/Wiener models, or exploring quantum-like phenomena in biological neural systems. Bridges quantum foundations and neuroscience."
---

# Leggett-Garg Tests in Neural Dynamics

## Description

Apply Leggett-Garg inequality testing to single-neuron dynamics to distinguish between classical diffusive (Wiener/cable-equation) models and non-diffusive stochastic models. When neural models violate LG inequalities, it suggests non-classical behavior in neural computation — opening new avenues for understanding the fundamental nature of neural processing.

Based on: Ghose, "Leggett-Garg Tests in Neural Dynamics: Probing Non-Diffusive Stochastic Structure in Single Neurons" (arXiv:2605.12126, 2026).

## Activation Keywords

- leggett-garg neural
- quantum neural dynamics
- non-diffusive neuron
- macrorealism neural
- temporal correlations neuron
- LG inequality neural
- 量子神经动力学
- 神经非扩散
- stochastic neuron model

## Tools Used

- exec: Run simulation/analysis code
- write: Create analysis scripts and reports

## Core Methodology

### Leggett-Garg Inequalities

LG inequalities test macrorealism — the assumption that a system has definite properties independent of measurement and that measurement doesn't disturb the system. Violation suggests non-classical temporal correlations.

The canonical LG inequality for dichotomic observable Q(t):

```
K = C(t1,t2) + C(t2,t3) - C(t1,t3) ≤ 1
```

where C(ti,tj) = ⟨Q(ti)Q(tj)⟩ are temporal correlation functions.

Classical systems satisfy K ≤ 1; quantum systems can reach K = 1.5 (Tsirelson-like bound).

### Application to Neural Dynamics

1. **Define dichotomic observable**: Map neural state (membrane potential, firing rate) to Q = ±1
   - Example: Q = +1 if V > threshold, Q = -1 otherwise

2. **Choose measurement times**: Select t1, t2, t3 at meaningful intervals relative to neural timescales

3. **Compute temporal correlations**: C(ti,tj) = ⟨Q(ti)Q(tj)⟩ from experimental or simulated data

4. **Test LG inequality**: Calculate K and check if K > 1

### Models That Violate LG Inequalities

- **Non-diffusive stochastic models**: Lévy flights, fractional Brownian motion
- **Models with memory**: Non-Markovian dynamics
- **Models with quantum-like phase coherence**

### Models That Satisfy LG Inequalities

- **Standard cable equation**: Wiener process diffusion
- **Markovian rate models**: Classical Hodgkin-Huxley variants
- **Ornstein-Uhlenbeck processes**: Linear Gaussian dynamics

## Experimental Design

### In Silico (Simulation)

```python
def test_lg_inequality(trajectory, t1, t2, t3, threshold=0):
    """Test Leggett-Garg inequality on neural trajectory data."""
    Q = np.where(trajectory > threshold, 1, -1)
    
    C12 = np.mean(Q[t1] * Q[t2])
    C23 = np.mean(Q[t2] * Q[t3])
    C13 = np.mean(Q[t1] * Q[t3])
    
    K = C12 + C23 - C13
    return K, C12, C23, C13
```

### Key Considerations

1. **Non-invasive measurability**: LG tests assume measurements don't disturb the system. In neural recordings, this is approximated by weak measurements or post-selection.

2. **Stationarity**: Correlations should be computed over stationary segments of data.

3. **Temporal resolution**: Measurement times must resolve the relevant neural dynamics (typically ms scale for single neurons).

4. **Ensemble averaging**: LG inequalities require averaging over many trials/realizations.

## Connection to Quantum Neuroscience

This methodology bridges quantum physics and neuroscience by:

1. **Testing quantum-like behavior**: If neurons violate LG inequalities, it suggests non-classical temporal structure in neural computation.

2. **Informing quantum-inspired models**: Results guide whether quantum cognition models or classical models better describe neural dynamics.

3. **Neuromorphic computing**: Non-classical neural dynamics may enable new computational paradigms in neuromorphic hardware.

## Related Quantum-Neural Concepts

- **Quantum cognition**: Hilbert space models of decision-making and cognition
- **Neuromorphic quantum computing**: Quantum circuits inspired by neural architectures
- **Quantum reservoir computing**: Fixed quantum dynamics with linear readout (see extreme-quantum-cognition skill)
- **Neural quantum states**: Variational Monte Carlo with neural network wavefunctions

## Examples

### Simulating LG Test on Neuron Model

```python
import numpy as np

# Simulate non-diffusive neural dynamics (Lévy flight)
def levy_neural_trajectory(T, alpha=1.5):
    """Generate non-diffusive neural trajectory."""
    steps = np.random.standard_t(df=alpha, size=T)
    return np.cumsum(steps)

# Simulate diffusive (classical) neural dynamics
def brownian_neural_trajectory(T):
    """Generate diffusive neural trajectory."""
    steps = np.random.randn(T)
    return np.cumsum(steps)

# Test on both models
for name, traj in [("Levy", levy_neural_trajectory(10000)),
                    ("Brownian", brownian_neural_trajectory(10000))]:
    K, c12, c23, c13 = test_lg_inequality(traj, 100, 200, 300)
    violation = "VIOLATES" if K > 1 else "SATISFIES"
    print(f"{name}: K = {K:.4f} ({violation} LG inequality)")
```

## Limitations

- LG inequality violation doesn't prove quantum behavior — other non-classical mechanisms (memory, nonlinearity) can also violate
- Experimental implementation in real neurons is extremely challenging
- Requires careful control of measurement back-action
- Interpretation depends on the specific neural model being tested
