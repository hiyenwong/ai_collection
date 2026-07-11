---
name: neural-operator-stability-discovery
description: "Neural operator framework for data-driven discovery of stability and receptivity properties in physical systems. Activation: neural operator, stability discovery, receptivity analysis, dynamical systems."
---

# Neural Operator Framework for Data-Driven Discovery of Stability and Receptivity in Physical Systems

> A neural operator approach to discovering stability and receptivity properties of dynamical systems directly from data, extending operator learning to characterize system responses to perturbations without requiring explicit governing equations.

## Metadata
- **Source**: arXiv:2604.19465
- **Authors**: Nirmal Prasanna, Arvind Santhanakrishnan
- **Published**: 2026-04-21
- **Category**: cs.LG (Machine Learning)

## Core Methodology

### Key Innovation
Traditional approaches to stability analysis require:
1. Explicit knowledge of governing equations
2. Linearization around fixed points
3. Eigenvalue analysis of Jacobian matrices

This framework **bypasses these requirements** by:
- Learning stability properties directly from trajectory data
- Using neural operators to capture infinite-dimensional dynamics
- Providing data-driven receptivity analysis
- Scaling to high-dimensional physical systems

### Technical Framework

**1. Stability Discovery via Neural Operators**
```
Input: State trajectories u(t) from dynamical system
Neural Operator G: Learns evolution operator u(t+Δt) = G(u(t))
Stability Analysis: Spectrum of learned operator indicates stability
```

**2. Receptivity Characterization**
- Perturbation response: How system reacts to small disturbances
- Sensitivity fields: Spatial distribution of receptivity
- Transient growth: Non-modal stability analysis

**3. Data-Driven Modal Analysis**
- Dynamic mode decomposition (DMD) enhanced with neural operators
- Nonlinear modal analysis without linearization
- Discovery of coherent structures

## Mathematical Foundation

### Neural Operator Learning

Given trajectory data {u(t₀), u(t₁), ..., u(tₙ)}, learn operator G such that:
```
u(t+Δt) ≈ G(u(t); θ)
```

Where G is parameterized as a neural operator:
```
G = Q ∘ σ_W_L ∘ ... ∘ σ_W_1 ∘ P
```

With:
- P: Lifting operator (finite to infinite dimensional)
- σ_W: Kernel integral operator with activation
- Q: Projection operator (infinite to finite dimensional)

### Stability Analysis

**Linearized Operator Spectrum**
```
δu(t+Δt) ≈ J_G(u*) δu(t)

Stability determined by eigenvalues λ of J_G:
- max|λ| < 1: Asymptotically stable
- max|λ| = 1: Marginally stable
- max|λ| > 1: Unstable
```

**Receptivity Analysis**
```
Resolvent norm: ||(zI - J_G)⁻¹||

Large resolvent norm indicates:
- Strong amplification of forcing at frequency z
- High receptivity to perturbations
- Potential for transient energy growth
```

## Implementation Guide

### Prerequisites
- Python 3.8+
- PyTorch or JAX for neural operators
- Knowledge of dynamical systems and stability theory
- Understanding of operator learning (FNO, DeepONet)

### Step-by-Step Implementation

**Step 1: Data Preparation**
```python
import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader

class DynamicalSystemDataset(Dataset):
    """
    Dataset for learning from trajectory data
    """
    def __init__(self, trajectories, dt=0.01):
        """
        trajectories: List of arrays (time_steps, spatial_points, state_vars)
        """
        self.pairs = []
        for traj in trajectories:
            for i in range(len(traj) - 1):
                self.pairs.append((traj[i], traj[i+1]))
        
    def __len__(self):
        return len(self.pairs)
    
    def __getitem__(self, idx):
        u_t, u_tp1 = self.pairs[idx]
        return torch.FloatTensor(u_t), torch.FloatTensor(u_tp1)
```

**Step 2: Neural Operator Architecture**
```python
import torch.nn as nn
import torch.nn.functional as F

class FourierLayer(nn.Module):
    """
    Fourier integral operator layer
    """
    def __init__(self, in_channels, out_channels, modes=12):
        super().__init__()
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.modes = modes
        
        # Complex weights for Fourier modes
        self.weights = nn.Parameter(
            torch.randn(in_channels, out_channels, modes, 2) * 0.02
        )
    
    def forward(self, x):
        """
        x: (batch, channels, spatial_points)
        """
        # FFT
        x_ft = torch.fft.rfft(x, dim=-1)
        
        # Multiply relevant Fourier modes
        out_ft = torch.zeros_like(x_ft)
        out_ft[:, :, :self.modes] = torch.einsum(
            "bix,iox->box",
            x_ft[:, :, :self.modes],
            torch.view_as_complex(self.weights)
        )
        
        # Inverse FFT
        x = torch.fft.irfft(out_ft, n=x.size(-1), dim=-1)
        return x

class StabilityNeuralOperator(nn.Module):
    """
    Neural operator for stability discovery
    """
    def __init__(self, in_channels=1, width=32, modes=12, num_layers=4):
        super().__init__()
        self.in_channels = in_channels
        self.width = width
        
        # Lifting layer
        self.lift = nn.Conv1d(in_channels, width, 1)
        
        # Fourier layers
        self.fourier_layers = nn.ModuleList([
            FourierLayer(width, width, modes) for _ in range(num_layers)
        ])
        
        # Local processing
        self.local_layers = nn.ModuleList([
            nn.Conv1d(width, width, 1) for _ in range(num_layers)
        ])
        
        # Projection layer
        self.project = nn.Conv1d(width, in_channels, 1)
    
    def forward(self, x):
        # Lift to higher dimensional space
        x = self.lift(x)
        x = F.gelu(x)
        
        # Apply Fourier and local layers
        for fourier, local in zip(self.fourier_layers, self.local_layers):
            x1 = fourier(x)
            x2 = local(x)
            x = x1 + x2
            x = F.gelu(x)
        
        # Project back
        x = self.project(x)
        return x
```

**Step 3: Training**
```python
def train_neural_operator(model, dataloader, epochs=100, lr=1e-3):
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer)
    
    for epoch in range(epochs):
        total_loss = 0
        for u_t, u_tp1 in dataloader:
            optimizer.zero_grad()
            
            # Forward prediction
            u_pred = model(u_t)
            
            # Loss: prediction error
            loss = F.mse_loss(u_pred, u_tp1)
            
            loss.backward()
            optimizer.step()
            
            total_loss += loss.item()
        
        avg_loss = total_loss / len(dataloader)
        scheduler.step(avg_loss)
        
        if epoch % 10 == 0:
            print(f"Epoch {epoch}: Loss = {avg_loss:.6f}")
```

**Step 4: Stability Analysis**
```python
def analyze_stability(model, equilibrium_state, num_samples=100):
    """
    Analyze stability around equilibrium using learned operator
    """
    model.eval()
    
    # Create perturbations around equilibrium
    spatial_points = equilibrium_state.shape[-1]
    perturbations = []
    
    for _ in range(num_samples):
        # Random perturbation
        eps = torch.randn_like(equilibrium_state) * 0.01
        u_perturbed = equilibrium_state + eps
        
        # Evolve through operator
        with torch.no_grad():
            u_next = model(u_perturbed)
        
        # Compute growth rate
        initial_norm = torch.norm(eps)
        final_norm = torch.norm(u_next - equilibrium_state)
        growth = final_norm / (initial_norm + 1e-10)
        
        perturbations.append(growth.item())
    
    # Stability indicator
    max_growth = max(perturbations)
    mean_growth = np.mean(perturbations)
    
    stability = {
        'max_growth_rate': max_growth,
        'mean_growth_rate': mean_growth,
        'is_stable': max_growth < 1.1,
        'perturbation_responses': perturbations
    }
    
    return stability
```

**Step 5: Receptivity Analysis**
```python
def receptivity_analysis(model, base_state, frequencies):
    """
    Analyze receptivity to forcing at different frequencies
    """
    model.eval()
    receptivity = []
    
    for freq in frequencies:
        # Create harmonic forcing
        x = np.linspace(0, 2*np.pi, base_state.shape[-1])
        forcing = np.sin(freq * x)
        forcing_tensor = torch.FloatTensor(forcing).unsqueeze(0).unsqueeze(0)
        
        # Apply forcing and evolve
        perturbed = base_state + 0.1 * forcing_tensor
        
        with torch.no_grad():
            response = model(perturbed)
        
        # Measure amplification
        input_amplitude = torch.norm(forcing_tensor)
        response_amplitude = torch.norm(response - base_state)
        amplification = response_amplitude / (input_amplitude + 1e-10)
        
        receptivity.append({
            'frequency': freq,
            'amplification': amplification.item()
        })
    
    return receptivity
```

## Applications

### 1. Fluid Dynamics
- Hydrodynamic stability analysis
- Turbulence transition prediction
- Flow control design

### 2. Climate Modeling
- Climate regime stability
- Tipping point detection
- Sensitivity analysis

### 3. Robotics
- Gait stability for legged robots
- Balance control analysis
- Manipulation stability

### 4. Power Systems
- Grid stability assessment
- Oscillation mode identification
- Control parameter tuning

## Case Studies

### Case 1: Cylinder Wake Flow
```python
# Load flow simulation data
wake_data = load_cylinder_wake_simulation()

# Train neural operator
model = StabilityNeuralOperator(in_channels=2, width=64, modes=16)
train_neural_operator(model, wake_data, epochs=200)

# Analyze von Kármán vortex shedding stability
equilibrium = compute_mean_flow(wake_data)
stability = analyze_stability(model, equilibrium)

print(f"Flow stability: {'Stable' if stability['is_stable'] else 'Unstable'}")
print(f"Maximum growth rate: {stability['max_growth_rate']:.4f}")
```

### Case 2: Thermal Convection
```python
# Rayleigh-Bénard convection analysis
rb_data = load_thermal_convection_data()

# Discover stability boundaries
rayleigh_numbers = [1000, 2000, 3000, 4000]
stabilities = []

for Ra in rayleigh_numbers:
    data = rb_data[Ra]
    model = StabilityNeuralOperator(in_channels=1, width=32, modes=8)
    train_neural_operator(model, data, epochs=100)
    
    equilibrium = data.mean_state
    stability = analyze_stability(model, equilibrium)
    stabilities.append((Ra, stability['is_stable']))

# Find critical Rayleigh number
critical_Ra = find_transition(stabilities)
print(f"Critical Rayleigh number: {critical_Ra}")
```

## Pitfalls

**Data Quality Requirements**
- Requires sufficient trajectory coverage
- Long time series needed for accurate operator learning
- Solution: Use multiple initial conditions, ensemble learning

**High-Dimensional Systems**
- Computational cost scales with spatial resolution
- Solution: Use dimensionality reduction (POD) as preprocessing

**Non-Stationary Systems**
- Slowly varying systems may violate stationarity assumptions
- Solution: Time-windowed analysis, adaptive operators

**Interpretability**
- Learned operators are black-box
- Solution: Extract linearized operators for eigenvalue analysis

## Related Skills
- fourier-neural-operator
- deeponet-operator-learning
- dynamical-systems-analysis
- stability-theory-control
- fluid-dynamics-ml

## References
```bibtex
@article{prasanna2026neural,
  title={A Neural Operator Framework for Data-Driven Discovery of Stability and Receptivity in Physical Systems},
  author={Prasanna, Nirmal and Santhanakrishnan, Arvind},
  journal={arXiv preprint arXiv:2604.19465},
  year={2026}
}
```

## Activation Triggers
- neural operator stability
- data-driven stability analysis
- receptivity discovery
- dynamical systems operator learning
- stability without equations
