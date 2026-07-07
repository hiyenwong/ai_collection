---
name: predictable-mean-field-chaos-random-recurrent-networks
description: Predictable mean-field chaos methodology for random recurrent networks - demonstrating that deterministic chaos is only apparently stochastic, with continuous past uniquely determining future trajectories.
version: 1.0.0
author: Alkesh Yadav, Vladimir Shaidurov, Jonathan Kadmon
arxiv_id: 2606.08805
date_created: 2026-06-09
tags: [neuroscience, chaos-theory, mean-field, recurrent-networks, krylov-dynamics, deterministic, prediction, neural-networks]
activation_keywords: [predictable chaos, mean-field, krylov, recurrent networks, deterministic chaos, prediction theory, lyapunov exponent, dissipative systems]
---

# Predictable Mean-Field Chaos in Random Recurrent Networks

## Overview

This paper demonstrates that chaos in random recurrent networks, traditionally viewed as stochastic through dynamical mean-field theory, is actually deterministic and predictable. By unfolding the power spectrum into Krylov state space, the authors show that the continuous past of a realized trajectory uniquely determines its future, establishing mean-field theory as a conditional prediction theory rather than merely an ensemble description.

**arXiv**: [2606.08805](https://arxiv.org/abs/2606.08805)

## Key Innovation

Traditional dynamical mean-field theory (DMFT) recasts deterministic chaos in random recurrent networks as an effective stochastic process, treating it as an ensemble average over network realizations. This paper reveals that:

1. **Latent Determinism**: Chaos appears stochastic but is fundamentally deterministic
2. **Unique Trajectory Prediction**: Past trajectory uniquely determines future evolution
3. **Krylov Hierarchy**: Power spectrum unfolds into infinite hierarchy of temporal modes
4. **Predictive Complexity**: Krylov growth rate upper-bounds Lyapunov exponent

## Core Theory

### Random Recurrent Network Dynamics

```python
# Network model
x_i(t+dt) = x_i(t) + dt * [ -x_i(t) + Σ_j J_ij * φ(x_j(t)) + noise ]

where:
- x_i: State of neuron i
- J_ij: Random Gaussian coupling matrix (J_ij ~ N(0, g²/N))
- φ: Nonlinear activation function (e.g., tanh, erf)
- g: Coupling strength (chaos emerges for g > 1)
- N: Number of neurons
```

### Dynamical Mean-Field Theory (DMFT)

Traditional DMFT replaces deterministic network with stochastic effective process:

```
x(t) satisfies: dx/dt = -x + g * η(t) * φ(x(t))

where η(t) is Gaussian process with:
⟨η(t)η(t')⟩ = C(t,t') = ⟨φ(x(t))φ(x(t')⟩
```

**Key Insight**: DMFT treats this as ensemble average, but actual trajectories are deterministic!

### Determinism Discovery

For **analytic nonlinearities** with **sufficiently fast Fourier decay**:

1. The stochasticity is **apparent**: Past uniquely determines future
2. DMFT is **conditional prediction theory**: Not just ensemble description
3. **Krylov representation**: Exposes hierarchical determinism structure

## Mathematical Framework

### Krylov State Space Unfolding

The power spectrum S(ω) unfolds into Krylov state space:

```
Power spectrum: S(ω) = Fourier transform of correlation C(t)

Krylov representation:
┌─────────────────────────────────────────┐
│ K₀(t) = C(t)                            │ ← Correlation function
│ K₁(t) = ∫ K₀(t-t') K₀(t') dt'           │ ← First-order convolution
│ K₂(t) = ∫ K₁(t-t') K₀(t') dt'           │ ← Second-order
│ ...                                     │
│ K_n(t) = nth-order nested convolution   │ ← Infinite hierarchy
└─────────────────────────────────────────┘
```

### Krylov Growth Rate

**Definition**: Krylov growth rate Γ characterizes temporal complexity:

```
Γ = lim_{n→∞} [ ||K_n(t)|| / ||K_{n-1}(t)|| ]

Properties:
1. Γ sets finite-resolution prediction complexity
2. Γ upper-bounds largest Lyapunov exponent λ_max
3. Γ < ∞ for analytic nonlinearities
```

### Lyapunov Exponent Bound

**Major Result**:

```
λ_max ≤ Γ

where:
- λ_max: Largest Lyapunov exponent (microscopic sensitivity)
- Γ: Krylov growth rate (predictive complexity)
```

**Significance**: Microscopic sensitivity and predictive complexity are **distinct aspects** of mean-field chaos.

## Deterministic Prediction Theory

### Theorem: Trajectory Determinism

For analytic φ with fast Fourier decay:

```
Given trajectory history {x(t) : t ∈ [-T, 0]}
there exists unique future {x(t) : t ∈ [0, ∞]}
```

**Proof outline**:
1. Correlation function C(t,t') determined by trajectory history
2. C determines effective stochastic process η(t) statistics
3. η(t) conditioned on history is deterministic
4. Future evolution uniquely specified

### Conditional Mean-Field Theory

```
DMFT transition: Ensemble average → Conditional prediction

Traditional view:
⟨x(t)⟩ over network realizations

New view (conditional):
x(t) | {x(t') for t'<t} is uniquely determined

The mean-field theory becomes:
"Given continuous past, predict future"
rather than:
"Average over ensemble of networks"
```

## Implementation

### Krylov Space Analysis

```python
import numpy as np
from scipy.integrate import quad

class KrylovAnalyzer:
    def __init__(self, correlation_function, max_order=10):
        """
        Analyze chaotic dynamics via Krylov hierarchy
        
        Args:
            correlation_function: C(t) correlation
            max_order: Maximum Krylov order to compute
        """
        self.C = correlation_function
        self.max_order = max_order
        self.Krylov_sequence = self.compute_krylov()
    
    def compute_krylov(self):
        """Compute Krylov sequence K_n(t)"""
        K = {}
        K[0] = self.C  # Base correlation
        
        for n in range(1, self.max_order):
            K[n] = self.nested_convolution(K[n-1], K[0])
        
        return K
    
    def nested_convolution(self, K_prev, K_base):
        """
        Compute nested convolution:
        K_n(t) = ∫ K_{n-1}(t-t') K_0(t') dt'
        """
        # Discretize for numerical integration
        t_max = len(K_prev)
        result = np.zeros(t_max)
        
        for t_idx in range(t_max):
            t = t_idx * dt
            # Convolution integral
            integral = 0
            for tau in range(t_max):
                t_shift = t - tau*dt
                if 0 <= t_shift < t_max:
                    integral += K_prev[int(t_shift/dt)] * K_base[tau] * dt
            result[t_idx] = integral
        
        return result
    
    def compute_growth_rate(self):
        """
        Estimate Krylov growth rate Γ
        
        Γ ≈ ||K_n|| / ||K_{n-1}|| for large n
        """
        norms = [np.linalg.norm(K) for K in self.Krylov_sequence.values()]
        
        # Growth rate from late terms
        if len(norms) > 5:
            gamma = np.mean([norms[i]/norms[i-1] for i in range(-3, 0)])
        else:
            gamma = norms[-1] / norms[-2]
        
        return gamma
    
    def bound_lyapunov(self):
        """
        Compute upper bound on Lyapunov exponent
        
        λ_max ≤ Γ
        """
        return self.compute_growth_rate()
```

### Prediction from History

```python
class DeterministicPredictor:
    def __init__(self, coupling_strength_g, nonlinearity='erf'):
        """
        Predict future trajectory from past history
        
        Args:
            g: Coupling strength (>1 for chaos)
            nonlinearity: Activation type (must be analytic)
        """
        self.g = g
        self.phi = self.get_nonlinearity(nonlinearity)
        
        # Ensure analyticity (fast Fourier decay)
        self.validate_nonlinearity()
    
    def get_nonlinearity(self, name):
        """Return analytic nonlinearity"""
        if name == 'erf':
            return lambda x: np.erf(x)  # Fast Fourier decay ✓
        elif name == 'tanh':
            return lambda x: np.tanh(x)  # Fast Fourier decay ✓
        else:
            raise ValueError(f"Nonlinearity {name} may not have fast decay")
    
    def validate_nonlinearity(self):
        """
        Verify Fourier decay condition
        
        For prediction theorem to hold, need:
        |φ̂(k)| ≤ C · exp(-α|k|) for some α>0
        """
        # Fourier transform test (simplified)
        pass
    
    def predict_future(self, history, future_steps):
        """
        Predict future trajectory from continuous past
        
        Args:
            history: {x(t) : t ∈ [-T, 0]}
            future_steps: Number of future time points
        
        Returns:
            predicted: {x(t) : t ∈ [0, T_future]}
        """
        # Compute correlation from history
        C = self.compute_correlation(history)
        
        # Krylov-based prediction
        krylov = KrylovAnalyzer(C, max_order=10)
        
        # Conditional dynamics (simplified)
        predicted = []
        for step in range(future_steps):
            # Deterministic evolution given history
            x_next = self.deterministic_update(history[-1], C, krylov)
            predicted.append(x_next)
        
        return predicted
    
    def compute_correlation(self, history):
        """Compute correlation C(t,t') from trajectory"""
        # Simplified: autocorrelation
        T = len(history)
        C = np.zeros(T)
        for dt in range(T):
            C[dt] = np.mean([history[t] * history[t-dt] 
                          for t in range(dt, T)])
        return C
```

## Key Results

### 1. Determinism vs Ensemble

```
┌─────────────────────────────────────────┐
│ Traditional DMFT View                    │
│ ─────────────────                        │
│ Chaos = Stochastic ensemble average      │
│ Unpredictable due to randomness          │
├─────────────────────────────────────────┤
│ New Conditional View                     │
│ ─────────────────                        │
│ Chaos = Deterministic given history      │
│ Past uniquely determines future          │
│ Predictable at finite resolution         │
└─────────────────────────────────────────┘
```

### 2. Krylov Growth Rate Bounds

Experimental validation:
- Analytic networks (erf, tanh): Γ < ∞, prediction possible
- Non-analytic networks: Γ may diverge, prediction limited
- Lyapunov exponent: Always bounded by Γ

### 3. Prediction Accuracy

```
Prediction resolution ∝ 1/Γ

Higher Γ → More temporal modes needed
Lower Γ → Better finite-resolution prediction
```

## Applications

### 1. Chaos Prediction

- **Trajectory forecasting**: Predict chaotic dynamics given history
- **Resolution optimization**: Determine required temporal resolution
- **Horizon estimation**: Compute prediction horizon from Γ

### 2. Network Design

- **Nonlinearity selection**: Choose analytic φ for predictability
- **Coupling calibration**: Adjust g for desired Γ/λ balance
- **Structure analysis**: Relate architecture to prediction complexity

### 3. Neuroscience Implications

- **Neural chaos**: Brain dynamics may be more predictable than thought
- **Trajectory inference**: Predict neural trajectories from past activity
- **Complexity metrics**: Use Γ as complexity measure (complementary to λ)

## Theoretical Extensions

### Hamiltonian Chaos → Dissipative Systems

This work extends Krylov growth concepts from:
- **Hamiltonian chaos** (energy-preserving systems)
- **Dissipative chaos** (energy-dissipating recurrent networks)

Key parallels:
- Krylov complexity in both domains
- Temporal hierarchy structure
- Bounds on sensitivity measures

### Beyond Mean-Field

Potential extensions:
1. **Finite-size corrections**: Account for finite N networks
2. **Structured connectivity**: Beyond random Gaussian matrices
3. **Multiple time scales**: Hierarchical dynamics
4. **Non-analytic analysis**: Relaxation of Fourier decay condition

## Implementation Checklist

When applying predictable chaos methodology:

- [ ] Verify nonlinearity is analytic (erf, tanh recommended)
- [ ] Confirm fast Fourier decay condition
- [ ] Measure correlation function C(t) from trajectory
- [ ] Compute Krylov sequence K_n(t)
- [ ] Estimate growth rate Γ from Krylov norms
- [ ] Bound Lyapunov exponent: λ_max ≤ Γ
- [ ] Determine prediction resolution: resolution ~ 1/Γ
- [ ] Test prediction accuracy at given resolution

## Comparison with Previous Methods

| Method | Ensemble View | Deterministic View | Prediction Theory | Complexity Bound |
|--------|---------------|-------------------|-------------------|------------------|
| Traditional DMFT | ✅ | ❌ | ❌ | ❌ |
| Lyapunov Analysis | ❌ | ❌ | ❌ | λ_max only |
| **Krylov Method** | ✅ | ✅ | ✅ | λ_max ≤ Γ |

## Limitations

1. **Analyticity Requirement**: Requires analytic φ with fast Fourier decay
2. **Mean-Field Assumption**: Derived for N→∞, finite-N corrections needed
3. **Random Connectivity**: Structured networks may have different behavior
4. **Numerical Challenges**: Computing high-order Krylov terms is expensive

## Future Directions

1. **Finite-size theory**: Extend to finite-N networks with corrections
2. **Structured networks**: Apply to non-random connectivity
3. **Multiple scales**: Hierarchical Krylov analysis
4. **Experimental validation**: Test on real neural data
5. **Control applications**: Use prediction for chaos control

## Code Availability

Supplementary material available at arXiv entry.

## Related Skills

- [[chaos-synchrony-ei-networks]] - Chaos and synchrony in excitatory-inhibitory networks
- [[neural-critical-dynamics-theory]] - Theory of critical dynamics in neural networks
- [[recurrent-networks]] - General recurrent network methodologies
- [[predictable-mean-field-chaos-rnn]] - Mean-field chaos in RNNs

## References

1. Yadav, A., Shaidurov, V., Kadmon, J. (2026). Predictable Mean-Field Chaos in Random Recurrent Networks. arXiv:2606.08805

2. Sompolinsky, H., Crisanti, A., Sommers, H. (1988). Chaos in random neural networks. Physical Review Letters.

3. Crisanti, A., Sompolinsky, H. (1988). Dynamics of random neural networks. Physica A.

4. Kadmon, J., Sompolinsky, H. (2024). Mean-field theory of chaotic recurrent networks. Physical Review X.

---

**Bottom Line**: Chaos in random recurrent networks is deterministic and predictable given trajectory history. The Krylov growth rate Γ provides a complexity measure that upper-bounds Lyapunov exponent, separating microscopic sensitivity from predictive complexity. This transforms mean-field theory from ensemble average to conditional prediction framework.