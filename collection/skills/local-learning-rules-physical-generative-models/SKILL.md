---
name: local-learning-rules-physical-generative-models
description: "Local learning rules for out-of-equilibrium physical generative models using score-based generative modeling in driven nonlinear oscillator networks. Demonstrates that SGM driving protocols can be learned via local measurements without backpropagation. Activation: local learning rules, physical generative models, score-based generative, out-of-equilibrium, overdamped oscillators, MNIST generation, neuromorphic computing"
tags: [neuroscience, generative-models, local-learning, physical-computing, neuromorphic, score-matching, non-equilibrium-thermodynamics]
---

## Overview

This paper demonstrates that the out-of-equilibrium driving protocol of score-based generative models (SGMs) can be learned via local learning rules. The gradient with respect to the parameters of the driving protocol is computed directly from force measurements or from observed system dynamics, without requiring backpropagation through time. The framework is validated on a network of driven, nonlinear, overdamped oscillators coupled to a thermal bath, generating samples from Gaussian mixtures and MNIST digits.

## Key Contributions

### 1. Local Learning for Physical Generative Models
- **No backpropagation required**: Gradients computed from local force measurements
- **Physical implementation**: Learning occurs in the physical substrate itself
- **Thermodynamic consistency**: Respects non-equilibrium thermodynamics
- **Biological plausibility**: Local learning rules compatible with physical/biological systems

### 2. Score-Based Generative Modeling in Physical Systems
- **SGM in oscillators**: Implements score-based generative modeling in driven nonlinear oscillators
- **Overdamped dynamics**: Uses overdamped oscillators coupled to thermal bath
- **Driving protocol**: Time-dependent protocol that implements the reverse diffusion process
- **Local parameter updates**: Each oscillator updates its parameters based on local measurements

### 3. Empirical Validation
- **Gaussian mixture**: Successfully samples from 2D mixture of Gaussians
- **MNIST generation**: Trained on MNIST dataset to generate handwritten digits 0 and 1
- **Physical substrate**: Implemented in network of driven nonlinear oscillators
- **Thermal noise**: Operates in presence of thermal fluctuations

## Core Methodology

### Score-Based Generative Models (SGMs)
```
Forward Process (Diffusion):
  dx = -∇U(x)dt + √(2β(t))dW
  
  Where:
  - x: system state
  - U(x): potential energy landscape
  - β(t): noise schedule
  - W: Wiener process

Reverse Process (Generation):
  dx = [-∇U(x) - 2β(t)∇log p_t(x)]dt + √(2β(t))dW̄
  
  Where:
  - ∇log p_t(x): score function (learned)
  - W̄: reverse-time Wiener process
```

### Local Learning Rule Derivation
```
Objective: Learn driving protocol parameters θ

Gradient computation:
  ∂L/∂θ = <F_local · ∂x/∂θ>_t
  
  Where:
  - F_local: local force measurements at each oscillator
  - ∂x/∂θ: sensitivity of state to parameters
  - <·>_t: time average over trajectory

Key insight: The gradient can be estimated from:
1. Force measurements: Direct measurement of forces on oscillators
2. Observed dynamics: Inference from trajectory observations
```

### Physical Implementation
```
Oscillator Network:
- N nonlinear overdamped oscillators
- Coupled to thermal bath at temperature T
- Driven by time-dependent protocol s(t; θ)
- Each oscillator has local parameters θ_i

Local Learning:
- Each oscillator measures local force F_i
- Computes local gradient ∂L/∂θ_i
- Updates parameters: θ_i ← θ_i - η ∂L/∂θ_i
- No global error signal required
```

## Key Insights

### 1. Physical Systems Can Learn Generative Models
Physical systems far from equilibrium can implement score-based generative models and learn their parameters through local measurements, without requiring digital computation or backpropagation.

### 2. Local Measurements Suffice for Global Learning
Despite the global nature of the generative task, local force measurements at each oscillator provide sufficient information to learn the driving protocol, enabling distributed learning in physical substrates.

### 3. Non-Equilibrium Driving as Computational Resource
The out-of-equilibrium driving protocol is not just a means to an end—it is the computational substrate itself. Learning this protocol is equivalent to learning the generative model.

## Applications

### Neuromorphic Computing
- **Analog generative models**: Physical implementation of generative AI
- **Energy-efficient generation**: Leverage physical dynamics for sampling
- **In-memory learning**: Learning occurs in the physical substrate

### Biological Systems
- **Developmental biology**: Understanding how biological systems generate patterns
- **Neural development**: Local learning rules for circuit formation
- **Morphogenesis**: Physical processes that generate complex structures

### Materials Science
- **Self-organizing materials**: Materials that learn to generate target patterns
- **Active matter**: Programmable active matter systems
- **Metamaterials**: Learning material properties for target functionality

## Implementation Patterns

### Oscillator Network Simulation
```python
# Pseudocode for physical generative model
class PhysicalGenerativeModel:
    def __init__(self, n_oscillators, temperature, coupling_matrix):
        self.N = n_oscillators
        self.T = temperature
        self.K = coupling_matrix  # Coupling matrix
        self.theta = np.random.randn(self.N)  # Local parameters
        
    def forward_diffusion(self, x0, beta_schedule, dt):
        """Forward diffusion process"""
        x = x0.copy()
        trajectory = [x]
        
        for t in range(len(beta_schedule)):
            beta = beta_schedule[t]
            force = self.compute_force(x)
            noise = np.sqrt(2 * beta * dt) * np.random.randn(self.N)
            x = x + force * dt + noise
            trajectory.append(x)
        
        return trajectory
    
    def reverse_generation(self, score_network, beta_schedule, dt):
        """Reverse process for generation"""
        x = np.random.randn(self.N)  # Start from noise
        trajectory = [x]
        
        for t in reversed(range(len(beta_schedule))):
            beta = beta_schedule[t]
            force = self.compute_force(x)
            score = score_network(x, t)
            noise = np.sqrt(2 * beta * dt) * np.random.randn(self.N)
            x = x + (force + 2 * beta * score) * dt + noise
            trajectory.append(x)
        
        return trajectory
    
    def compute_force(self, x):
        """Compute forces on oscillators"""
        # Potential gradient
        grad_U = self.compute_potential_gradient(x)
        
        # Coupling forces
        coupling_force = self.K @ x
        
        return -grad_U + coupling_force
    
    def local_learning_rule(self, trajectory, learning_rate):
        """Local learning from trajectory"""
        for t in range(len(trajectory) - 1):
            x = trajectory[t]
            dx = trajectory[t+1] - x
            
            # Local force measurements
            F_local = self.compute_force(x)
            
            # Local gradient estimate
            grad_theta = F_local * dx / learning_rate
            
            # Local parameter update
            self.theta -= learning_rate * grad_theta
```

### MNIST Generation
```python
# Pseudocode for MNIST generation
class MNISTGenerator:
    def __init__(self, image_size=28):
        self.n_pixels = image_size * image_size
        self.model = PhysicalGenerativeModel(
            n_oscillators=self.n_pixels,
            temperature=1.0,
            coupling_matrix=self.get_coupling()
        )
    
    def train(self, mnist_data, epochs=100):
        """Train on MNIST digits 0 and 1"""
        for epoch in range(epochs):
            for img in mnist_data:
                # Forward diffusion
                beta_schedule = self.get_beta_schedule()
                trajectory = self.model.forward_diffusion(img, beta_schedule, dt=0.01)
                
                # Local learning
                self.model.local_learning_rule(trajectory, learning_rate=0.001)
    
    def generate(self, n_samples=10):
        """Generate new digits"""
        samples = []
        for _ in range(n_samples):
            beta_schedule = self.get_beta_schedule()
            trajectory = self.model.reverse_generation(
                score_network=self.get_score_network(),
                beta_schedule=beta_schedule,
                dt=0.01
            )
            samples.append(trajectory[-1].reshape(28, 28))
        return samples
```

## Validation Metrics

### Generation Quality
- **Sample diversity**: Variety of generated samples
- **Sample quality**: Visual quality and realism
- **Mode coverage**: Coverage of data distribution modes
- **FID score**: Fréchet Inception Distance (for images)

### Learning Efficiency
- **Convergence speed**: Number of iterations to converge
- **Sample efficiency**: Data efficiency of learning
- **Computational cost**: Energy and time requirements

### Physical Metrics
- **Thermodynamic efficiency**: Energy dissipation per sample
- **Entropy production**: Rate of entropy production
- **Distance from equilibrium**: How far from equilibrium the system operates

## Related Work

### Score-Based Generative Models
- Song et al. (2019): Generative modeling by estimating gradients of the data distribution
- Song et al. (2021): Score-based generative modeling through SDEs
- Ho et al. (2020): Denoising diffusion probabilistic models

### Physical Learning
- Hermans et al. (2020): A tutorial on training recurrent neural networks with backpropagation through time
- Bohté et al. (2018): Unsupervised learning by competing hidden units
- Stern et al. (2022): Learning in the manifold of physical systems

### Neuromorphic Computing
- Maass (1997): Networks of spiking neurons: The third generation of neural network models
- Indiveri et al. (2011): Neuromorphic silicon neuron circuits
- Schuman et al. (2017): A survey of neuromorphic computing and neural networks in hardware

## Future Directions

1. **Larger networks**: Scale to thousands of oscillators
2. **Complex datasets**: Generate more complex data distributions
3. **Hardware implementation**: Implement in physical oscillator networks
4. **Hybrid systems**: Combine with digital computation for enhanced capabilities

## References

- arXiv:2506.19136
- Authors: Cyrill Bösch, Geoffrey Roeder, Marc Serra-Garcia, Ryan P. Adams
- Published: 2025-06-24 (updated 2026-07-07)
- Categories: cs.LG, cond-mat.mes-hall, cs.ET, cs.NE
