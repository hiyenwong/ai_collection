---
name: energy-based-neurocomputation
description: "Energy-based dynamical models for neurocomputation, learning, and optimization. Unified framework connecting Hopfield networks, Boltzmann machines, and continuous neural dynamics through energy minimization. Activation: energy-based model, Hopfield network, equilibrium propagation, neural computation, associative memory, energy minimization."
---

# Energy-Based Dynamical Models for Neurocomputation

A unified framework for energy-based dynamical models (EBDMs) that bridges neuroscience-inspired computation with modern machine learning. EBDMs provide a principled approach to neural computation through energy minimization dynamics.

## Core Concept

Energy-based models define computation through **energy landscapes**, where:
- **Low-energy states** represent stable patterns/memories
- **Dynamics** follow energy gradients (descent/ascent)
- **Learning** shapes the energy landscape

This framework unifies:
- Hopfield networks (discrete, symmetric)
- Boltzmann machines (stochastic, probabilistic)
- Continuous neural dynamics (differential equations)

## Energy Function

### General Form

```
E(x; θ) = E_data(x) + E_constraint(x; θ)
```

Where:
- `x`: State vector (neural activities)
- `θ`: Parameters (weights, biases)
- `E_data`: Data-dependent energy
- `E_constraint`: Prior/constraints

### Continuous Neural Dynamics

```python
import torch
import torch.nn as nn

class EnergyBasedNeuralNetwork(nn.Module):
    """Continuous-time energy-based neural network."""
    
    def __init__(self, n_neurons, tau=1.0):
        super().__init__()
        self.n_neurons = n_neurons
        self.tau = tau
        
        # Symmetric weights for energy well-definedness
        self.W = nn.Parameter(torch.randn(n_neurons, n_neurons) * 0.1)
        self.b = nn.Parameter(torch.zeros(n_neurons))
        
        # Ensure symmetry: W = (W + W^T) / 2
        self.W.data = (self.W.data + self.W.data.T) / 2
    
    def energy(self, x):
        """Compute energy of state x."""
        # Quadratic form: E = -0.5 * x^T W x - b^T x + 0.5 * x^T x
        quadratic = -0.5 * torch.sum(x @ self.W * x, dim=-1)
        linear = -torch.sum(self.b * x, dim=-1)
        norm = 0.5 * torch.sum(x ** 2, dim=-1)
        return quadratic + linear + norm
    
    def dynamics(self, x, external_input=None):
        """Compute energy gradient (dynamics)."""
        # dx/dt = -∇E(x) + input
        # ∇E = -Wx - b + x = x - Wx - b
        grad = x - x @ self.W - self.b
        
        if external_input is not None:
            grad += external_input
        
        return grad / self.tau
    
    def forward(self, x0, n_steps=100, dt=0.1):
        """Run dynamics to equilibrium."""
        x = x0
        for _ in range(n_steps):
            dx = self.dynamics(x) * dt
            x = x + dx
            # Optional: apply activation (e.g., tanh for bounded states)
            x = torch.tanh(x)
        return x
```

## Three Core Capabilities

### 1. Pattern Completion (Associative Memory)

```python
class AssociativeMemory(EBNM):
    """Energy-based associative memory."""
    
    def store_patterns(self, patterns):
        """Store patterns as energy minima."""
        # Hebbian learning: W_ij = sum over patterns of (x_i * x_j)
        n_patterns = len(patterns)
        for p in patterns:
            self.W.data += torch.outer(p, p) / n_patterns
        
        # Maintain symmetry
        self.W.data = (self.W.data + self.W.data.T) / 2
        
        # Remove self-connections
        self.W.data.fill_diagonal_(0)
    
    def recall(self, partial_pattern, n_steps=50):
        """Complete partial pattern."""
        # Initialize with partial pattern
        x = partial_pattern.clone()
        
        # Run to energy minimum
        x_equilibrium = self.forward(x, n_steps=n_steps)
        
        return x_equilibrium
```

### 2. Learning via Equilibrium Propagation

```python
class EquilibriumPropagation:
    """
    Learning in energy-based models through two phases.
    
    Based on Scellier & Bengio (2017).
    """
    
    def __init__(self, model, beta=1.0):
        self.model = model
        self.beta = beta  # Clamping factor
    
    def free_phase(self, x_init):
        """
        Phase 1: Free dynamics (no clamping).
        
        System settles to free equilibrium: s^0
        """
        s_free = self.model.forward(x_init, n_steps=100)
        return s_free
    
    def clamped_phase(self, x_init, target):
        """
        Phase 2: Clamped dynamics (output clamped to target).
        
        System settles to clamped equilibrium: s^β
        """
        # Clamped energy: E' = E + β * loss(s, target)
        s_clamped = x_init.clone()
        
        for _ in range(100):
            grad = self.model.dynamics(s_clamped)
            
            # Add clamping force on output units
            loss_grad = self.beta * (s_clamped - target)
            
            s_clamped = s_clamped + 0.1 * (grad - loss_grad)
        
        return s_clamped
    
    def compute_gradients(self, s_free, s_clamped):
        """
        Compute parameter gradients.
        
        ∂L/∂θ = (1/β) * (∂E(s^β)/∂θ - ∂E(s^0)/∂θ)
        """
        # Energy gradients at both equilibria
        grad_free = torch.autograd.grad(
            self.model.energy(s_free).sum(),
            self.model.parameters()
        )
        
        grad_clamped = torch.autograd.grad(
            self.model.energy(s_clamped).sum(),
            self.model.parameters()
        )
        
        # Weight update
        gradients = [
            (g_clamped - g_free) / self.beta
            for g_free, g_clamped in zip(grad_free, grad_clamped)
        ]
        
        return gradients
    
    def train_step(self, x_batch, y_batch, optimizer):
        """Single training step."""
        # Free phase
        s_free = self.free_phase(x_batch)
        
        # Clamped phase
        s_clamped = self.clamped_phase(x_batch, y_batch)
        
        # Compute gradients
        gradients = self.compute_gradients(s_free, s_clamped)
        
        # Update parameters
        for param, grad in zip(self.model.parameters(), gradients):
            param.grad = grad
        
        optimizer.step()
```

### 3. Optimization-Based Inference

```python
class EnergyBasedInference:
    """Use energy minimization for probabilistic inference."""
    
    def __init__(self, energy_model):
        self.energy = energy_model
    
    def map_inference(self, observations, latent_init):
        """
        Maximum a posteriori (MAP) inference.
        
        Find latent variables that minimize energy given observations.
        """
        latent = latent_init
        
        for _ in range(1000):
            # Compute energy and gradient
            energy = self.energy(observations, latent)
            grad = torch.autograd.grad(energy, latent)[0]
            
            # Gradient descent on latent variables
            latent = latent - 0.01 * grad
        
        return latent
    
    def sampling(self, n_samples, n_steps=1000, step_size=0.01):
        """
        Sample from energy-based distribution using Langevin dynamics.
        
        p(x) ∝ exp(-E(x))
        """
        samples = []
        x = torch.randn(n_samples, self.energy.n_neurons)
        
        for _ in range(n_steps):
            # Compute gradient
            energy = self.energy(x)
            grad = torch.autograd.grad(energy.sum(), x)[0]
            
            # Langevin update
            noise = torch.randn_like(x) * np.sqrt(2 * step_size)
            x = x - step_size * grad + noise
            
            if _ > n_steps // 2:  # Burn-in
                samples.append(x.clone())
        
        return torch.stack(samples)
```

## Modern Extensions

### Modern Hopfield Network (Dense Associative Memory)

```python
class ModernHopfieldNetwork:
    """
    Dense Associative Memory with polynomial energy.
    
    Demircigil et al. (2017), Ramsauer et al. (2021)
    """
    
    def __init__(self, dim, n_patterns, beta=1.0):
        self.patterns = nn.Parameter(torch.randn(n_patterns, dim))
        self.beta = beta
    
    def energy(self, x):
        """Polynomial energy: E = -sum_i (pattern_i · x)^n"""
        # Dot products with all patterns
        similarities = torch.matmul(self.patterns, x)
        
        # Energy: negative sum of exponentiated similarities
        energy = -torch.logsumexp(self.beta * similarities, dim=0)
        
        return energy
    
    def update(self, x):
        """Update rule via attention."""
        # Softmax attention over patterns
        similarities = torch.matmul(self.patterns, x)
        attention = F.softmax(self.beta * similarities, dim=0)
        
        # New state: weighted combination of patterns
        x_new = torch.matmul(attention.T, self.patterns)
        
        return x_new
    
    def retrieve(self, query, n_steps=10):
        """Retrieve pattern from query."""
        x = query
        for _ in range(n_steps):
            x = self.update(x)
        return x
```

## Biological Connections

| EBDM Component | Biological Analog |
|----------------|-------------------|
| Energy minimum | Attractor state |
| Gradient descent | Neural dynamics |
| Symmetric weights | Reciprocal connections |
| External input | Sensory drive |
| Noise | Synaptic noise |

## Applications

1. **Content-addressable memory**: Pattern completion and denoising
2. **Constraint satisfaction**: Solving CSPs via energy minimization
3. **Generative modeling**: Learning data distributions
4. **Neuromorphic computing**: Energy-efficient inference

## References

- Energy-Based Dynamical Models for Neurocomputation, Learning, and Optimization. arXiv:2604.05042
- Scellier & Bengio (2017). Equilibrium propagation
- Hopfield (1982). Neural networks and physical systems
- Ramsauer et al. (2021). Hopfield Networks is All You Need

## Activation Keywords

- energy-based model
- Hopfield network
- equilibrium propagation
- associative memory
- energy minimization
- continuous neural dynamics
- attractor network
