---
name: energy-based-neurocomputation
description: Energy-based dynamical models for neurocomputation, learning, and optimization. Bridges control theory, neuroscience, and machine learning through gradient flows and energy landscapes.
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [neurocomputation, energy-based-models, dynamical-systems, control-theory, hopfield-networks, associative-memory, optimization]
    source_paper: "Energy-Based Dynamical Models for Neurocomputation, Learning, and Optimization (arXiv:2604.05042)"
    authors: "Arthur N. Montanari, Francesco Bullo, Dmitry Krotov, Adilson E. Motter"
    published: "2026-04-06"
---

# Energy-Based Dynamical Models for Neurocomputation

Tutorial on energy-based dynamical models that encode information through gradient flows and energy landscapes, bridging control theory, neuroscience, and machine learning.

## Overview

Recent advances at the intersection of control theory, neuroscience, and machine learning have revealed novel mechanisms by which dynamical systems perform computation. This methodology focuses on **energy-based dynamical models** that encode information through gradient flows and energy landscapes.

Key applications include:
- Model learning and training
- Memory retrieval
- Data-driven control
- Optimization

## Core Framework

### Energy-Based Models

Dynamical systems where computation emerges from energy minimization:

```
dx/dt = -∇E(x) + inputs
```

Where `E(x)` is an energy landscape shaping the dynamics.

### Classical Foundations

#### Hopfield Networks (Continuous-Time)

```python
class ContinuousHopfield:
    """
    Continuous-time Hopfield network
    """
    def __init__(self, n_neurons, tau=1.0):
        self.n = n_neurons
        self.tau = tau  # Time constant
        self.W = np.zeros((n_neurons, n_neurons))  # Symmetric weights
        self.theta = np.zeros(n_neurons)  # Thresholds
        
    def energy(self, x):
        """
        Hopfield energy function
        E(x) = -½ x^T W x + Σᵢ ∫₀ˣⁱ g⁻¹(s) ds - x^T θ
        """
        quadratic = -0.5 * x.T @ self.W @ x
        integral = np.sum(self.potential(x))
        bias = -x.T @ self.theta
        return quadratic + integral + bias
    
    def dynamics(self, x, I_ext=0):
        """
        dx/dt = (-x + f(Wx + θ + I_ext)) / τ
        """
        return (-x + self.activation(self.W @ x + self.theta + I_ext)) / self.tau
    
    def activation(self, u):
        """Sigmoid activation (monotonic, bounded)"""
        return np.tanh(u)
    
    def store_pattern(self, pattern):
        """Store pattern using Hebbian learning"""
        self.W += np.outer(pattern, pattern) / self.n
        np.fill_diagonal(self.W, 0)  # No self-connections
```

#### Boltzmann Machines

```python
class BoltzmannMachine:
    """
    Stochastic energy-based model
    """
    def __init__(self, n_visible, n_hidden):
        self.n_v = n_visible
        self.n_h = n_hidden
        self.W = np.random.randn(n_visible, n_hidden) * 0.01
        self.b_v = np.zeros(n_visible)
        self.b_h = np.zeros(n_hidden)
        
    def energy(self, v, h):
        """
        E(v, h) = -v^T W h - v^T b_v - h^T b_h
        """
        return -v.T @ self.W @ h - v.T @ self.b_v - h.T @ self.b_h
    
    def sample_h_given_v(self, v):
        """Sample hidden units given visible"""
        prob_h = sigmoid(self.W.T @ v + self.b_h)
        return (np.random.rand(self.n_h) < prob_h).astype(float)
    
    def sample_v_given_h(self, h):
        """Sample visible units given hidden"""
        prob_v = sigmoid(self.W @ h + self.b_v)
        return (np.random.rand(self.n_v) < prob_v).astype(float)
    
    def contrastive_divergence(self, data, k=1):
        """CD-k learning"""
        # Positive phase
        h0 = self.sample_h_given_v(data)
        
        # Negative phase (k steps Gibbs sampling)
        vk, hk = data, h0
        for _ in range(k):
            vk = self.sample_v_given_h(hk)
            hk = self.sample_h_given_v(vk)
        
        # Update weights
        self.W += learning_rate * (np.outer(data, h0) - np.outer(vk, hk))
```

## Modern Developments

### Dense Associative Memory

High-capacity storage beyond Hopfield networks:

```python
class DenseAssociativeMemory:
    """
    Modern Hopfield network with polynomial energy
    """
    def __init__(self, n_neurons, degree=2):
        self.n = n_neurons
        self.degree = degree
        self.patterns = []
        
    def energy(self, x):
        """
        E(x) = -Σₘ F(ξₘ · x)
        
        where F is a super-linear function (e.g., polynomial)
        """
        energies = []
        for pattern in self.patterns:
            overlap = np.dot(pattern, x)
            energies.append(self.F(overlap))
        return -np.sum(energies)
    
    def F(self, z):
        """Interaction function (polynomial)"""
        return z ** self.degree / self.degree
    
    def dynamics(self, x):
        """
        dx/dt = Σₘ F'(ξₘ · x) ξₘ - x
        """
        update = np.zeros(self.n)
        for pattern in self.patterns:
            overlap = np.dot(pattern, x)
            update += self.F_prime(overlap) * pattern
        return update - x
    
    def F_prime(self, z):
        """Derivative of F"""
        return z ** (self.degree - 1)
    
    def store(self, pattern):
        """Store pattern (capacity scales as n^(degree-1))"""
        self.patterns.append(pattern.copy())
```

### Oscillator-Based Networks

For large-scale optimization:

```python
class OscillatorNetwork:
    """
    Coupled oscillator network for optimization
    """
    def __init__(self, n_oscillators, coupling):
        self.n = n_oscillators
        self.coupling = coupling
        self.phases = np.random.uniform(0, 2*np.pi, n_oscillators)
        self.frequencies = np.random.randn(n_oscillators)
        
    def kuramoto_dynamics(self, t, phases):
        """
        dθᵢ/dt = ωᵢ + Σⱼ Kᵢⱼ sin(θⱼ - θᵢ)
        """
        coupling_term = np.zeros(self.n)
        for i in range(self.n):
            for j in range(self.n):
                coupling_term[i] += self.coupling[i,j] * np.sin(phases[j] - phases[i])
        
        return self.frequencies + coupling_term
    
    def solve_optimization(self, problem):
        """
        Map optimization problem to oscillator dynamics
        
        Minima of energy landscape ↔ Stable phase configurations
        """
        # Encode problem in coupling matrix
        self.coupling = self.encode_problem(problem)
        
        # Evolve to steady state
        solution_phases = self.integrate_to_steady_state()
        
        # Decode solution
        return self.decode_solution(solution_phases)
```

### Proximal-Descent Dynamics

For constrained reconstruction:

```python
class ProximalDescent:
    """
    Proximal descent for composite optimization
    """
    def __init__(self, data_fidelity, regularization, prox_operator):
        self.data_fidelity = data_fidelity
        self.regularization = regularization
        self.prox = prox_operator
        
    def dynamics(self, x, y, tau):
        """
        dx/dt = -∇f(x) + (1/τ)(prox_{τg}(x - τ∇f(x)) - x)
        
        where f is data fidelity, g is regularization
        """
        grad_f = self.gradient_data_fidelity(x, y)
        proximal_point = self.prox(x - tau * grad_f, tau)
        
        return -grad_f + (proximal_point - x) / tau
    
    def reconstruct(self, measurements, n_steps=1000):
        """Reconstruct signal from measurements"""
        x = self.initialize()
        
        for _ in range(n_steps):
            dx = self.dynamics(x, measurements, tau=0.1)
            x += 0.01 * dx
        
        return x
```

## Control-Theoretic Perspective

### Energy Shaping

```python
def energy_shaping_control(system, desired_energy, gains):
    """
    Design control to shape energy landscape
    
    u = -k ∇(E_actual - E_desired)
    """
    energy_error = system.energy() - desired_energy
    control_input = -gains * system.gradient_energy()
    
    return control_input
```

### Passivity-Based Design

Ensures stability through energy dissipation:

```python
def passivity_based_controller(system, port_variables):
    """
    Design passive controller
    
    Ensures dE/dt ≤ y^T u (passivity inequality)
    """
    y, u = port_variables
    
    # Controller ensures energy dissipation
    control_law = -damping_matrix @ y
    
    return control_law
```

## Applications

### Memory Systems
- High-capacity associative memory
- Content-addressable storage
- Error correction

### Optimization
- Combinatorial optimization
- Constraint satisfaction
- Resource allocation

### Learning
- Unsupervised feature learning
- Generative modeling
- Representation learning

### Control
- Data-driven control design
- Adaptive systems
- Robust control

## Advantages

1. **Scalability**: Parallel, distributed computation
2. **Robustness**: Graceful degradation, fault tolerance
3. **Energy Efficiency**: Analog implementation potential
4. **Interpretability**: Clear energy landscape semantics

## References

- Montanari, A. N., Bullo, F., Krotov, D., & Motter, A. E. (2026). Energy-Based Dynamical Models for Neurocomputation, Learning, and Optimization.

## Related

- [[hopfield-networks]]
- [[boltzmann-machines]]
- [[associative-memory]]
- [[neural-optimization]]
- [[control-theory]]
