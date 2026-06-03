---
name: drosophila-orientation-dynamical-system
description: "Dynamical system approach to modeling Drosophila central complex neural network for heading direction encoding. Ring-connectivity model with bump attractor dynamics, stochastic extensions with Brownian noise and Markovian switching. Provides mathematically tractable framework for understanding population coding of angular position. Use when: ring attractor, heading direction, Drosophila neuroscience, bump attractor, switching diffusion, stochastic neural dynamics, insect navigation, population coding, central complex."
version: 1.0.0
---

# Drosophila Orientation: Dynamical System Approach

## Core Insight

The Drosophila central complex uses ring-connectivity neural architecture to encode heading direction as stable "bump" attractors. This work provides rigorous mathematical analysis of deterministic bump dynamics and extends to stochastic settings with noise and switching external cues.

## Deterministic Model: Ring Attractor

### Reduced Recurrent Neural Activity Model
```python
import numpy as np
from scipy.integrate import odeint

def ring_attractor(theta, W, I_ext, tau=1.0):
    """
    Ring attractor dynamics on angular domain [0, 2π).
    
    Args:
        theta: Angular position
        W: Ring connectivity weight matrix (cosine-tuned)
        I_ext: External input current
        tau: Time constant
    """
    N = len(W)
    def dynamics(r, t):
        # r: N-dimensional firing rate vector
        input_current = W @ r + I_ext
        drdt = (-r + np.maximum(0, input_current)) / tau
        return drdt
    return dynamics

def cosine_connectivity(N, J0=-1.0, J1=2.0):
    """Generate ring connectivity matrix with cosine tuning."""
    angles = np.linspace(0, 2*np.pi, N, endpoint=False)
    W = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            W[i, j] = J0/N + J1/N * np.cos(angles[i] - angles[j])
    return W
```

### Bump Solution Analysis
- **Existence**: Stable localized bump solutions exist for J1 > |J0| (excitatory coupling dominates)
- **Global stability**: Bump attractors are globally exponentially stable in parameter regime
- **Encoding**: Bump peak position encodes fly's heading direction

## Stochastic Extension: Switching Diffusion

### Brownian Noise + Markov Switching
```python
import numpy as np

class SwitchingDiffusionRingAttractor:
    """
    Ring attractor with:
    1. Additive Brownian noise (sensory variability)
    2. Markovian switching mechanism (time-varying external cues)
    """
    def __init__(self, N, J0, J1, sigma, switch_rates):
        self.N = N
        self.W = cosine_connectivity(N, J0, J1)
        self.sigma = sigma  # noise intensity
        self.switch_rates = switch_rates  # transition rate matrix
        self.state = 0  # current Markov state
    
    def step(self, r, dt):
        """Euler-Maruyama step for switching diffusion."""
        # Current external input based on Markov state
        I_ext = self._external_input(self.state)
        
        # Deterministic drift
        drift = (-r + np.maximum(0, self.W @ r + I_ext)) * dt
        
        # Brownian noise
        noise = self.sigma * np.sqrt(dt) * np.random.randn(self.N)
        
        # Markov switching
        if np.random.random() < self._switch_probability(dt):
            self.state = self._transition(self.state)
        
        return r + drift + noise
    
    def _external_input(self, markov_state):
        """Different external cue configurations."""
        angles = np.linspace(0, 2*np.pi, self.N, endpoint=False)
        return np.cos(angles - markov_state * np.pi/4)
```

## Mathematical Results

1. **Well-posedness**: Existence and uniqueness of solutions for switching diffusion system
2. **Infinitesimal generator**: Characterized for the piecewise linear drift system
3. **Invariant measure**: Proven existence of stationary distribution
4. **Bump robustness**: Bump attractors persist under noise and switching stimuli

## Applications
- Insect navigation modeling
- Ring attractor network design
- Heading direction encoding
- Stochastic neural dynamics analysis
- Bio-inspired navigation systems

## Results (arXiv:2604.13411, Apr 2026)
- Deterministic analysis: parameter regimes for global stability of bump solutions
- Stochastic analysis: well-posedness, invariant measure for switching diffusion
- Numerical validation in both low and high dimensions
- Authors: S. Ismail, B. Ambrosio, M.A. Aziz-Alaoui, Y. Souleiman
- Categories: math.DS (Dynamical Systems)

## Activation Keywords
- Drosophila orientation
- ring attractor
- bump attractor
- heading direction
- central complex
- switching diffusion
- stochastic neural dynamics
- insect navigation
- population coding heading

## References
- Ismail et al., "A dynamical system approach to modeling neural network activity in Drosophila orientation", arXiv:2604.13411, Apr 2026
