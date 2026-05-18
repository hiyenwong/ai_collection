---
name: warped-hierarchical-modular-neural-network
description: "Warped Hierarchical and Modular Dynamical Neural Network architecture. Operates in learned warped spaces to achieve efficient hierarchical and modular computation with long-range stability. Activation: warped space neural network, hierarchical modular, dynamical systems, timescale separation."
paper_source: "arXiv:2604.10606 (April 2026)"
version: v1.0.0
last_updated: 2026-04-15
---

# Warped Hierarchical and Modular Neural Network

A neural architecture that operates in learned warped spaces to naturally separate timescales, create functional modules, and maintain stable dynamics across long temporal horizons.

## Description

This architecture addresses key challenges in recurrent neural networks:
- **Timescale separation**: Different processing speeds for different features
- **Modularity**: Functional specialization in subnetworks
- **Long-range stability**: Maintaining coherent dynamics over time

By learning nonlinear coordinate transformations (warping functions), the network naturally emerges hierarchical structure and modular organization.

## Activation Keywords

- warped space neural network
- hierarchical modular architecture
- timescale separation
- dynamical systems learning
- warped coordinates RNN
- 扭曲空间神经网络
- 层次化模块化
- 时间尺度分离

## When to Use

- Tasks requiring multiple timescales
- Long-horizon prediction problems
- Hierarchical decision making
- Continual learning with modularity
- Cognitive modeling (working memory, planning)

## Core Methodology

### 1. Warping Function

Transform input to warped latent space:

```python
import torch
import torch.nn as nn

class WarpingFunction(nn.Module):
    """
    Learnable warping from input space to latent space
    
    φ: X → Z (nonlinear coordinate transformation)
    """
    
    def __init__(self, input_dim, latent_dim, n_layers=3):
        super().__init__()
        layers = []
        
        # Encoder
        for i in range(n_layers):
            in_d = input_dim if i == 0 else latent_dim
            out_d = latent_dim
            layers.extend([
                nn.Linear(in_d, out_d),
                nn.LayerNorm(out_d),
                nn.GELU()
            ])
        
        self.encoder = nn.Sequential(*layers)
        
        # Jacobian regularization weight
        self.jacobian_reg = 0.01
    
    def forward(self, x):
        """Warp input to latent space"""
        z = self.encoder(x)
        return z
    
    def inverse(self, z):
        """Inverse warping (approximate)"""
        # Can use learned decoder or iterative optimization
        pass
    
    def compute_jacobian(self, x):
        """Compute Jacobian matrix for regularization"""
        batch_size = x.shape[0]
        x.requires_grad_(True)
        
        z = self.forward(x)
        jacobian = torch.zeros(batch_size, z.shape[1], x.shape[1])
        
        for i in range(z.shape[1]):
            grad = torch.autograd.grad(
                z[:, i].sum(), x, create_graph=True, retain_graph=True
            )[0]
            jacobian[:, i, :] = grad
        
        return jacobian
```

### 2. Hierarchical Dynamics in Warped Space

```python
class HierarchicalWarpedRNN(nn.Module):
    """
    RNN with hierarchical dynamics via warped space
    
    In warped coordinates, dynamics naturally separate into:
    - Fast modes (sensory processing)
    - Slow modes (context/abstract features)
    """
    
    def __init__(self, input_dim, latent_dim, n_hierarchy=3):
        super().__init__()
        self.latent_dim = latent_dim
        self.n_hierarchy = n_hierarchy
        
        # Warping function
        self.warp = WarpingFunction(input_dim, latent_dim)
        
        # Hierarchical recurrent weights
        # Block structure in warped coordinates creates timescale separation
        dims_per_level = latent_dim // n_hierarchy
        self.recurrent_weights = nn.ParameterList()
        self.time_constants = nn.ParameterList()
        
        for i in range(n_hierarchy):
            # Each level has its own recurrent dynamics
            w = nn.Parameter(torch.randn(dims_per_level, dims_per_level) * 0.01)
            self.recurrent_weights.append(w)
            
            # Learnable time constant (controls integration speed)
            tau = nn.Parameter(torch.ones(1) * (10.0 ** i))  # Slow for high levels
            self.time_constants.append(tau)
        
        # Cross-level connections (hierarchical)
        self.hierarchy_connections = nn.Parameter(
            torch.randn(n_hierarchy - 1, dims_per_level, dims_per_level) * 0.01
        )
    
    def forward(self, x, h_prev):
        """
        Forward pass with hierarchical dynamics
        
        Args:
            x: Input [batch, input_dim]
            h_prev: Previous hidden state [batch, latent_dim]
        
        Returns:
            h: New hidden state
        """
        # Warp input
        z_in = self.warp(x)
        
        # Split into hierarchical levels
        level_size = self.latent_dim // self.n_hierarchy
        h_levels = torch.split(h_prev, level_size, dim=-1)
        z_levels = torch.split(z_in, level_size, dim=-1)
        
        new_h_levels = []
        
        for i in range(self.n_hierarchy):
            # Current level dynamics
            tau = torch.sigmoid(self.time_constants[i]) * 100  # 0-100ms
            alpha = torch.exp(-1.0 / (tau + 1e-6))
            
            # Recurrent update
            h_new = alpha * h_levels[i] + (1 - alpha) * (
                torch.matmul(h_levels[i], self.recurrent_weights[i].T) +
                z_levels[i]
            )
            
            # Bottom-up influence from lower levels
            if i > 0:
                h_new = h_new + torch.matmul(
                    h_levels[i-1], 
                    self.hierarchy_connections[i-1].T
                )
            
            new_h_levels.append(h_new)
        
        h = torch.cat(new_h_levels, dim=-1)
        return h
```

### 3. Modular Structure via Warped Coordinates

```python
class ModularWarpedNetwork(nn.Module):
    """
    Network with modular structure in warped space
    
    Block-diagonal connectivity emerges from:
    - Specialized warping for each module
    - Sparse inter-module connections
    - Module-specific dynamics
    """
    
    def __init__(self, input_dim, n_modules, module_dim):
        super().__init__()
        self.n_modules = n_modules
        self.module_dim = module_dim
        self.total_dim = n_modules * module_dim
        
        # Module-specific warping functions
        self.module_warps = nn.ModuleList([
            WarpingFunction(input_dim // n_modules, module_dim)
            for _ in range(n_modules)
        ])
        
        # Intra-module dynamics (block diagonal)
        self.module_dynamics = nn.ModuleList([
            nn.GRUCell(module_dim, module_dim)
            for _ in range(n_modules)
        ])
        
        # Inter-module connections (sparse)
        self.inter_module = nn.Parameter(
            torch.randn(n_modules, n_modules, module_dim, module_dim) * 0.001
        )
        
        # Gating for inter-module communication
        self.communication_gate = nn.Sequential(
            nn.Linear(self.total_dim, n_modules * n_modules),
            nn.Sigmoid()
        )
    
    def forward(self, x, h_prev):
        """
        Modular forward pass with selective communication
        
        Args:
            x: Input [batch, input_dim]
            h_prev: Previous state [batch, total_dim]
        """
        batch_size = x.shape[0]
        
        # Split into modules
        x_modules = torch.split(x, x.shape[-1] // self.n_modules, dim=-1)
        h_modules = torch.split(h_prev, self.module_dim, dim=-1)
        
        # Compute communication gates
        comm_gates = self.communication_gate(h_prev)
        comm_gates = comm_gates.view(batch_size, self.n_modules, self.n_modules)
        
        new_h_modules = []
        
        for i in range(self.n_modules):
            # Warp module input
            z_i = self.module_warps[i](x_modules[i])
            
            # Intra-module dynamics
            h_intra = self.module_dynamics[i](z_i, h_modules[i])
            
            # Inter-module communication (gated)
            h_inter = torch.zeros_like(h_intra)
            for j in range(self.n_modules):
                if i != j:
                    gate = comm_gates[:, i, j:j+1]  # [batch, 1]
                    contrib = torch.matmul(
                        h_modules[j], 
                        self.inter_module[i, j].T
                    )
                    h_inter = h_inter + gate * contrib
            
            # Combine
            h_new = h_intra + 0.1 * h_inter  # Weak inter-module influence
            new_h_modules.append(h_new)
        
        return torch.cat(new_h_modules, dim=-1)
```

## Workflow

### Step 1: Training with Curvature Regularization

```python
def train_warped_network(model, train_loader, epochs=100):
    """
    Train warped hierarchical modular network
    """
    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3)
    
    for epoch in range(epochs):
        for x, y in train_loader:
            optimizer.zero_grad()
            
            # Forward pass
            output, hiddens = model(x)
            
            # Task loss
            task_loss = F.mse_loss(output, y)
            
            # Curvature regularization (smooth warping)
            curvature_loss = 0
            for h in hiddens:
                # Penalize large Jacobians (encourage smoothness)
                jacobian = model.warp.compute_jacobian(h)
                curvature_loss += torch.norm(jacobian, p='fro')
            
            # Total loss
            loss = task_loss + 0.01 * curvature_loss
            
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimizer.step()
```

### Step 2: Timescale Analysis

```python
def analyze_timescales(model, test_data):
    """
    Analyze emergent timescales in trained model
    """
    # Compute Jacobian at fixed points
    with torch.no_grad():
        h = model.get_initial_state()
        
        # Linearize dynamics
        jacobian = compute_dynamics_jacobian(model, h)
        
        # Eigenvalue analysis
        eigenvalues = torch.linalg.eigvals(jacobian)
        
        # Timescales from eigenvalues
        timescales = -1.0 / eigenvalues.real
        
        return {
            'timescales': timescales,
            'n_fast': (timescales < 10).sum(),
            'n_slow': (timescales > 100).sum()
        }
```

### Step 3: Modular Structure Extraction

```python
def extract_modules(model, activity_data):
    """
    Extract functional modules from network activity
    """
    # Compute correlation matrix
    corr_matrix = torch.corrcoef(activity_data.T)
    
    # Community detection (e.g., spectral clustering)
    from sklearn.cluster import SpectralClustering
    
    clustering = SpectralClustering(
        n_clusters=model.n_modules,
        affinity='precomputed'
    )
    modules = clustering.fit_predict(corr_matrix.cpu().numpy())
    
    return modules
```

## Applications

### Hierarchical Reinforcement Learning

```python
class HierarchicalAgent:
    """
    Agent with hierarchical policy using warped network
    """
    
    def __init__(self, state_dim, action_dim):
        # Low-level: fast motor control
        # High-level: slow goal planning
        self.network = HierarchicalWarpedRNN(
            state_dim, 
            latent_dim=256,
            n_hierarchy=3
        )
    
    def act(self, state):
        # High level (slow): selects subgoal
        # Middle level: plans path to subgoal
        # Low level (fast): motor commands
        pass
```

### Continual Learning

```python
class ModularContinualLearner:
    """
    Continual learning with modular structure
    
    New tasks allocated to new modules or reuse existing
    """
    
    def learn_task(self, task_data, task_id):
        # Check if existing modules can handle task
        module_scores = self.evaluate_modules(task_data)
        
        if max(module_scores) > threshold:
            # Reuse best module
            module_id = argmax(module_scores)
        else:
            # Allocate new module
            module_id = self.add_module()
        
        # Train only selected module
        self.train_module(module_id, task_data)
```

## Advantages

| Feature | Benefit |
|---------|---------|
| **Timescale Separation** | Natural hierarchy emerges |
| **Modularity** | Functional specialization |
| **Stability** | Geometric constraints prevent chaos |
| **Flexibility** | Warping adapts to task structure |
| **Interpretability** | Clear module/timescale organization |

## References

- Paper: "Relaxing in Warped Spaces: Generalized Hierarchical and Modular Dynamical Neural Network" (arXiv:2604.10606)
- Timescale Separation: Singh et al. (2022) - Hierarchical representations in neural networks
- Warped Spaces: Haarnoja et al. (2018) - Latent space policies
