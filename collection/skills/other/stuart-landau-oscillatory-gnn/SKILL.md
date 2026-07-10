---
name: stuart-landau-oscillatory-gnn
description: "Complex-Valued Stuart-Landau Graph Neural Network (SLGNN) — oscillatory GNN grounded in Stuart-Landau oscillator dynamics near Hopf bifurcations. Retains both amplitude and phase dynamics for rich phenomena like amplitude regulation and multistable synchronization. Activation: Stuart-Landau GNN, SLGNN, oscillatory graph neural network, Hopf bifurcation GNN, amplitude-phase GNN."
---

# Stuart-Landau Oscillatory Graph Neural Network

> Complex-valued GNN architecture grounded in Stuart-Landau oscillator dynamics near Hopf bifurcations, generalizing phase-only Kuramodel-based OGNNs by allowing node feature amplitudes to evolve dynamically.

## Metadata
- **Source**: arXiv:2511.08094
- **Authors**: Kaicheng Zhang, David N. Reynolds, Piero Deidda, Francesco Tudisco
- **Published**: 2025-11-11
- **Category**: cs.LG

## Core Methodology

### Key Innovation
Stuart-Landau oscillators are canonical models of limit-cycle behavior near Hopf bifurcations. Unlike harmonic oscillators and phase-only Kuramoto models, Stuart-Landau oscillators retain both amplitude AND phase dynamics, enabling rich phenomena like amplitude regulation and multistable synchronization.

### Technical Framework

1. **Stuart-Landau Oscillator Dynamics**
   - Canonical form: dz/dt = (μ + iω)z - (1 + iβ)|z|²z + coupling terms
   - z ∈ ℂ: complex state with amplitude |z| and phase arg(z)
   - μ: Hopf bifurcation parameter (controls stability)
   - ω: natural frequency
   - β: nonlinear frequency correction

2. **SLGNN Architecture**
   - Each node i has complex state z_i = r_i · e^(iφ_i)
   - Amplitude r_i evolves dynamically (unlike Kuramoto where |z|=1)
   - Phase φ_i captures synchronization patterns
   - Coupling through graph adjacency: Σ_j A_ij · f(z_i, z_j)

3. **Key Advantages over Kuramoto OGNNs**
   - **Amplitude dynamics**: Nodes can regulate signal strength, not just phase alignment
   - **Multistable synchronization**: Multiple stable synchronized states possible
   - **Hopf parameter control**: Tunable hyperparameter for oscillation onset
   - **Rich bifurcation structure**: Can model transitions between regimes

4. **Training**
   - Complex-valued message passing with Stuart-Landau update rules
   - Backpropagation through complex ODE solver or discrete approximation
   - Hyperparameters: Hopf parameter μ, coupling strength K, nonlinear correction β

### Code Example
```python
import torch

class StuartLandauLayer(nn.Module):
    """Single SLGNN layer with Stuart-Landau oscillator dynamics."""
    
    def __init__(self, in_dim, hopf_param=0.1, coupling_strength=1.0, beta=0.5):
        super().__init__()
        self.mu = hopf_param      # Bifurcation parameter
        self.K = coupling_strength # Coupling strength
        self.beta = beta           # Nonlinear frequency correction
        self.omega = nn.Parameter(torch.randn(in_dim))  # Natural frequencies
    
    def forward(self, z, adjacency, dt=0.1):
        """
        z: complex tensor [num_nodes, dim]
        adjacency: [num_nodes, num_nodes]
        """
        # Stuart-Landau dynamics: dz/dt = (μ + iω)z - (1 + iβ)|z|²z
        linear_term = (self.mu + 1j * self.omega) * z
        nonlinear_term = (1 + 1j * self.beta) * (z.abs()**2) * z
        
        # Coupling from neighbors
        coupled = self.K * torch.matmul(adjacency, z)
        
        # Euler integration step
        dz = (linear_term - nonlinear_term + coupled) * dt
        return z + dz
    
    def get_phase(self, z):
        return torch.angle(z)
    
    def get_amplitude(self, z):
        return z.abs()
```

## Applications
- **Node classification**: Complex-valued features capture richer patterns
- **Graph classification**: Amplitude+phase dynamics improve discriminative power
- **Graph regression**: Predict continuous targets on graphs
- **Neuroscience modeling**: Mesoscopic brain modeling with oscillatory dynamics
- **Oversmoothing mitigation**: Oscillatory dynamics prevent feature homogenization

## Pitfalls
- **Complex arithmetic**: Requires complex-valued neural network support
- **Hopf parameter sensitivity**: Small changes in μ can cause regime transitions
- **Numerical stability**: ODE integration needs careful timestep selection
- **Training complexity**: Complex gradients require specialized optimizers

## Related Skills
- kuramoto-brain-network
- complex-valued-kuramoto-control
- brain-inspired-attention-mechanisms