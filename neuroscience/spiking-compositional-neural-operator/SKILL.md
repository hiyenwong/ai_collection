# SCNO: Spiking Compositional Neural Operator

## Overview

**SCNO (Spiking Compositional Neural Operator)** is a modular neuromorphic architecture that combines spiking neural networks with compositional learning to solve partial differential equations (PDEs). It addresses three critical limitations of traditional neural operators: monolithic training (no knowledge reuse), energy intensity (GPU dependency), and catastrophic forgetting (performance degradation on previously learned tasks).

This skill provides a complete implementation guide for building SCNO models for PDE solving, particularly suited for nuclear engineering applications and other edge-deployed scientific computing scenarios.

---

## Core Architecture

SCNO consists of three main components:

### 1. Spiking Operator Blocks (Frozen Library)

Each block $\mathcal{B}_k$ is a spiking DeepONet trained on a single elementary PDE operator:

| Operator | Mathematical Form | Physical Meaning |
|----------|-------------------|------------------|
| **Convection** ($\nabla$) | $-c \cdot \partial_x u$ | Transport/advection |
| **Diffusion** ($\Delta$) | $\nu \cdot \partial_{xx} u$ | Spatial smoothing |
| **Reaction** ($f$) | $k_r \cdot u(1-u)$ | Local source/sink |

**Block Architecture:**
```
Input Function u₀ ∈ ℝᵐ
    ↓
Linear Projection
    ↓
LIF Layer 1 + Skip (γ₁)
    ↓
LIF Layer 2 + Skip (γ₂)
    ↓
LIF Layer 3 + Skip (γ₃)
    ↓
Linear Readout → Branch Coefficients b ∈ ℝᵖ
    ↓
Inner Product with Trunk Network t(y) ∈ ℝᵖ
    ↓
Block Output: Bₖ(u₀)(y) = bᵀt(y) + b₀
```

**Key Hyperparameters:**
- Number of LIF layers: $L = 3$
- Hidden dimension: 256
- Latent dimension: $p = 128$
- LIF timesteps: $T_s = 30$ (convection), $T_s = 20$ (diffusion/reaction)
- Initial decay rate: $\beta_{\text{init}} = 0.85$

### 2. Input-Conditioned Aggregator

Combines block outputs for coupled PDEs using a gated mixture:

```
û(y) = σ(g) · MLP([Bₖ₁(y), ..., Bₖₖ(y); c]) + (1 - σ(g)) · wᵀo(y)
```

Where:
- $g$: Learnable gate parameter
- $c = f_{\text{ctx}}(u_0) \in \mathbb{R}^{64}$: Compressed input context
- $o(y) = [\mathcal{B}_{k_1}(y), ..., \mathcal{B}_{k_K}(y)]$: Block outputs
- $\sigma(g)$: Sigmoid gate

**Aggregator Specifications:**
- Hidden dimension: 256
- GELU activation layers: 3
- Input context dimension: 64

### 3. Correction Network (Optional)

For strongly-coupled PDEs, a small correction network learns cross-coupling residuals:

```
G(u₀)(y) = û(y) + α · C(u₀, y)
```

**Correction Network Specifications:**
- Hidden dimension: 128
- GELU activation layers: 3
- Trainable parameters: ~95K
- Learnable scaling: $\alpha$ (initialized to 0.1)

---

## Training Methodology

### Stage 1: Block Training (One-Time, Per Operator)

Train each spiking block independently on its elementary PDE:

```python
# Pseudocode for block training
for block_type in ['convection', 'diffusion', 'reaction']:
    block = SpikingDeepONet(
        lif_layers=3,
        hidden_dim=256,
        latent_dim=128,
        Ts=30 if block_type == 'convection' else 20
    )
    
    # Train on elementary PDE
    for epoch in range(800):
        loss = MSE(block(initial_condition), ground_truth_solution)
        loss.backward()  # Surrogate gradient for LIF
        optimizer.step()
    
    # Freeze block permanently
    block.freeze()
    library[block_type] = block
```

**Training Configuration:**
- Optimizer: AdamW
- Scheduler: Cosine/ReduceLROnPlateau
- Loss: Mean Squared Error
- Training samples: 1,500 per operator
- Grid points: $m = 256$ on $\Omega = [0, 1]$
- Time steps: 100 ($\Delta t = 0.005$)

### Stage 2: Aggregator Training (Per Coupled PDE)

```python
# Pseudocode for aggregator training
def train_aggregator(coupled_pde, block_library):
    # Select relevant blocks
    blocks = select_blocks(coupled_pde, block_library)
    
    aggregator = InputConditionedAggregator(
        input_blocks=blocks,
        hidden_dim=256,
        context_dim=64
    )
    
    # Train only aggregator (blocks remain frozen)
    for epoch in range(epochs):
        predictions = aggregator.compose(initial_condition)
        loss = MSE(predictions, ground_truth)
        loss.backward()
        aggregator_optimizer.step()
    
    return aggregator
```

**Trainable Parameters:**
- Aggregator only: ~231K parameters
- Frozen blocks: 462K per block (amortized across compositions)

### Stage 3: Correction Training (For Strong Coupling)

```python
# Pseudocode for correction training
def train_correction(coupled_pde, aggregator, blocks):
    correction = CorrectionNetwork(
        hidden_dim=128,
        num_layers=3,
        activation='GELU'
    )
    
    alpha = torch.nn.Parameter(torch.tensor(0.1))
    
    for epoch in range(epochs):
        base = aggregator.compose(initial_condition)
        residual = correction(initial_condition, query_points)
        prediction = base + alpha * residual
        
        loss = MSE(prediction, ground_truth)
        loss.backward()
        
        # Only update correction + alpha
        correction_optimizer.step()
        alpha_optimizer.step()
    
    return correction, alpha
```

---

## Supported PDE Families

| PDE | Equation | Composition | Coupling Strength |
|-----|----------|-------------|-------------------|
| **Convection** | $\partial_t u + c \cdot \partial_x u = 0$ | $\nabla$ | Elementary |
| **Diffusion** | $\partial_t u = \nu \cdot \partial_{xx} u$ | $\Delta$ | Elementary |
| **Reaction** | $\partial_t u = k \cdot u(1-u)$ | $f$ | Elementary |
| **Conv-Diff** | $\partial_t u + c \cdot \partial_x u = \nu \cdot \partial_{xx} u$ | $\nabla + \Delta$ | Strong |
| **React-Diff** | $\partial_t u = \nu \cdot \partial_{xx} u + k \cdot u(1-u)$ | $f + \Delta$ | Weak |
| **Neutron Diff** | $\partial_t \phi = D \cdot \partial_{xx} \phi + (\nu\Sigma_f - \Sigma_a) \cdot \phi$ | $\Delta + f$ | Moderate |
| **Burgers** | $\partial_t u + u \cdot \partial_x u = \nu \cdot \partial_{xx} u$ | $\nabla + \Delta$ | Strong |
| **Adv-React** | $\partial_t u + c \cdot \partial_x u = k \cdot u(1-u)$ | $\nabla + f$ | Strong |

---

## Implementation Guide

### Prerequisites

```bash
pip install torch numpy matplotlib scikit-learn
# For neuromorphic deployment:
pip install lava-dl  # Intel Loihi support
```

### Core Classes

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class LIFNeuron(nn.Module):
    """
    Leaky Integrate-and-Fire neuron with learnable decay rate.
    
    Args:
        beta_init: Initial membrane decay rate (default: 0.85)
        threshold: Firing threshold (default: 1.0)
    """
    def __init__(self, beta_init=0.85, threshold=1.0):
        super().__init__()
        self.beta = nn.Parameter(torch.tensor(beta_init))
        self.threshold = threshold
        
    def forward(self, x, Ts):
        """
        Simulate LIF dynamics for Ts timesteps.
        
        Args:
            x: Input current (batch, features)
            Ts: Number of simulation timesteps
            
        Returns:
            spike_train: Spike activity over time
            membrane_trace: Membrane potential trace
        """
        batch_size, features = x.shape
        device = x.device
        
        # Initialize membrane potential
        mem = torch.zeros(batch_size, features, device=device)
        spike_train = []
        
        beta = torch.sigmoid(self.beta)  # Ensure 0 < beta < 1
        
        for t in range(Ts):
            # Update membrane potential
            mem = beta * mem + x
            
            # Generate spikes
            spike = (mem >= self.threshold).float()
            mem = mem * (1 - spike)  # Reset after spike
            
            spike_train.append(spike)
        
        return torch.stack(spike_train, dim=0), mem


class SpikingDeepONetBlock(nn.Module):
    """
    Spiking DeepONet block for a single PDE operator.
    
    Architecture:
        - Linear projection → LIF layers with skips → Linear readout (branch)
        - MLP trunk network
        - Inner product + bias
    """
    def __init__(self, 
                 input_dim=256,
                 hidden_dim=256, 
                 latent_dim=128,
                 num_lif_layers=3,
                 Ts=20,
                 beta_init=0.85):
        super().__init__()
        
        self.Ts = Ts
        self.num_lif_layers = num_lif_layers
        
        # Branch network
        self.input_proj = nn.Linear(input_dim, hidden_dim)
        self.bn_input = nn.BatchNorm1d(hidden_dim)
        
        # LIF layers with skip connections
        self.lif_layers = nn.ModuleList([
            LIFNeuron(beta_init=beta_init) 
            for _ in range(num_lif_layers)
        ])
        
        self.skip_weights = nn.ParameterList([
            nn.Parameter(torch.tensor(0.5)) 
            for _ in range(num_lif_layers)
        ])
        
        self.bn_lif = nn.ModuleList([
            nn.BatchNorm1d(hidden_dim) 
            for _ in range(num_lif_layers)
        ])
        
        # Linear readout
        self.readout = nn.Linear(hidden_dim, latent_dim)
        self.bias = nn.Parameter(torch.zeros(1))
        
        # Trunk network (standard MLP)
        self.trunk = nn.Sequential(
            nn.Linear(1, hidden_dim),
            nn.Tanh(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.Tanh(),
            nn.Linear(hidden_dim, latent_dim)
        )
        
    def forward(self, u0, y):
        """
        Args:
            u0: Initial condition function (batch, input_dim)
            y: Query coordinates (batch, num_points, 1)
            
        Returns:
            predictions: Solution at query points (batch, num_points)
        """
        batch_size = u0.shape[0]
        num_points = y.shape[1]
        
        # Branch network
        x = self.input_proj(u0)
        x = self.bn_input(x)
        
        # LIF layers with residual connections
        for i, (lif, bn, gamma) in enumerate(
            zip(self.lif_layers, self.bn_lif, self.skip_weights)
        ):
            spikes, _ = lif(x, self.Ts)
            
            # Aggregate spikes over time
            spike_sum = spikes.sum(dim=0)  # (batch, hidden_dim)
            spike_sum = bn(spike_sum)
            
            # Skip connection with learnable weight
            gamma_sig = torch.sigmoid(gamma)
            x = (1 - gamma_sig) * spike_sum / self.Ts + gamma_sig * x
        
        # Branch coefficients
        b = self.readout(x)  # (batch, latent_dim)
        
        # Trunk network
        y_flat = y.reshape(-1, 1)  # (batch * num_points, 1)
        t = self.trunk(y_flat)  # (batch * num_points, latent_dim)
        t = t.reshape(batch_size, num_points, -1)
        
        # Inner product
        predictions = torch.einsum('bl,bnl->bn', b, t) + self.bias
        
        return predictions


class InputConditionedAggregator(nn.Module):
    """
    Input-conditioned aggregator for composing spiking blocks.
    
    Implements gated residual combination with input context.
    """
    def __init__(self, 
                 block_outputs,
                 hidden_dim=256,
                 context_dim=64):
        super().__init__()
        
        self.block_outputs = block_outputs
        
        # Input context encoder
        self.context_encoder = nn.Sequential(
            nn.Linear(256, hidden_dim),  # Assuming input_dim=256
            nn.GELU(),
            nn.Linear(hidden_dim, context_dim)
        )
        
        # Gating parameter
        self.gate = nn.Parameter(torch.zeros(1))
        
        # MLP path
        total_input = len(block_outputs) + context_dim
        self.mlp = nn.Sequential(
            nn.Linear(total_input, hidden_dim),
            nn.GELU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.GELU(),
            nn.Linear(hidden_dim, 1)
        )
        
        # Linear combination weights
        self.linear_weights = nn.Parameter(
            torch.ones(len(block_outputs)) / len(block_outputs)
        )
        
    def forward(self, initial_condition, query_points):
        """
        Args:
            initial_condition: (batch, input_dim)
            query_points: (batch, num_points, 1)
            
        Returns:
            aggregated_output: (batch, num_points)
        """
        # Get block outputs
        block_outs = []
        for block in self.block_outputs:
            out = block(initial_condition, query_points)
            block_outs.append(out)
        
        block_stack = torch.stack(block_outs, dim=-1)  # (batch, num_points, num_blocks)
        
        # Input context
        context = self.context_encoder(initial_condition)  # (batch, context_dim)
        context_expanded = context.unsqueeze(1).expand(-1, query_points.shape[1], -1)
        
        # Gated combination
        gate_val = torch.sigmoid(self.gate)
        
        # MLP path
        mlp_input = torch.cat([block_stack, context_expanded], dim=-1)
        mlp_out = self.mlp(mlp_input).squeeze(-1)  # (batch, num_points)
        
        # Linear path
        linear_out = torch.einsum('bmn,n->bm', block_stack, torch.softmax(self.linear_weights, dim=0))
        
        # Combined output
        output = gate_val * mlp_out + (1 - gate_val) * linear_out
        
        return output


class CorrectionNetwork(nn.Module):
    """
    Small correction network for learning cross-coupling residuals.
    
    Uses standard (non-spiking) neurons.
    """
    def __init__(self, 
                 context_dim=64,
                 hidden_dim=128,
                 num_layers=3):
        super().__init__()
        
        # Input: context + query coordinate features
        layers = []
        input_dim = context_dim + 1  # context + query coordinate
        
        for i in range(num_layers):
            layers.append(nn.Linear(input_dim, hidden_dim))
            layers.append(nn.GELU())
            input_dim = hidden_dim
        
        layers.append(nn.Linear(hidden_dim, 1))
        
        self.network = nn.Sequential(*layers)
        self.alpha = nn.Parameter(torch.tensor(0.1))
        
    def forward(self, context, query_points):
        """
        Args:
            context: (batch, context_dim)
            query_points: (batch, num_points, 1)
            
        Returns:
            residual: (batch, num_points)
        """
        batch_size, num_points, _ = query_points.shape
        
        # Expand context to match query points
        context_expanded = context.unsqueeze(1).expand(-1, num_points, -1)
        
        # Concatenate with query coordinates
        features = torch.cat([context_expanded, query_points], dim=-1)
        
        # Flatten for processing
        features_flat = features.reshape(-1, features.shape[-1])
        residual_flat = self.network(features_flat)
        
        # Reshape and scale
        residual = residual_flat.reshape(batch_size, num_points)
        
        return self.alpha * residual
```

### Complete SCNO Model

```python
class SCNO(nn.Module):
    """
    Complete Spiking Compositional Neural Operator.
    
    Combines frozen spiking blocks, aggregator, and optional correction.
    """
    def __init__(self, 
                 block_library,
                 use_correction=True):
        super().__init__()
        
        self.block_library = block_library
        self.use_correction = use_correction
        
        # Aggregator (to be configured per PDE)
        self.aggregator = None
        
        # Correction network
        if use_correction:
            self.correction = CorrectionNetwork()
        
    def configure_for_pde(self, operator_types):
        """
        Configure SCNO for a specific coupled PDE.
        
        Args:
            operator_types: List of operator types (e.g., ['nabla', 'delta'])
        """
        # Select blocks from library
        selected_blocks = [
            self.block_library[op] for op in operator_types
        ]
        
        # Create aggregator
        self.aggregator = InputConditionedAggregator(
            block_outputs=selected_blocks
        )
        
    def forward(self, initial_condition, query_points):
        """
        Args:
            initial_condition: (batch, input_dim)
            query_points: (batch, num_points, 1)
            
        Returns:
            solution: (batch, num_points)
        """
        # Base prediction from aggregator
        base_pred = self.aggregator(initial_condition, query_points)
        
        if self.use_correction and self.correction is not None:
            # Get context from aggregator
            context = self.aggregator.context_encoder(initial_condition)
            
            # Correction residual
            residual = self.correction(context, query_points)
            
            return base_pred + residual
        
        return base_pred
    
    def freeze_blocks(self):
        """Freeze all spiking blocks (call after training)."""
        for block in self.block_library.values():
            for param in block.parameters():
                param.requires_grad = False
```

---

## Training Loop

```python
def train_scno(scno_model, train_loader, val_loader, epochs=500):
    """
    Training loop for SCNO.
    
    Key: Only train aggregator and correction, blocks remain frozen.
    """
    optimizer = torch.optim.AdamW(
        filter(lambda p: p.requires_grad, scno_model.parameters()),
        lr=1e-3, weight_decay=1e-4
    )
    
    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
        optimizer, mode='min', factor=0.5, patience=20
    )
    
    for epoch in range(epochs):
        # Training
        scno_model.train()
        train_loss = 0.0
        
        for batch in train_loader:
            u0, y, u_true = batch  # initial condition, query points, ground truth
            
            optimizer.zero_grad()
            u_pred = scno_model(u0, y)
            loss = F.mse_loss(u_pred, u_true)
            
            loss.backward()
            optimizer.step()
            
            train_loss += loss.item()
        
        # Validation
        scno_model.eval()
        val_loss = 0.0
        with torch.no_grad():
            for batch in val_loader:
                u0, y, u_true = batch
                u_pred = scno_model(u0, y)
                val_loss += F.mse_loss(u_pred, u_true).item()
        
        scheduler.step(val_loss)
        
        if epoch % 50 == 0:
            print(f"Epoch {epoch}: Train Loss = {train_loss/len(train_loader):.6f}, "
                  f"Val Loss = {val_loss/len(val_loader):.6f}")
```

---

## Performance Metrics

### Accuracy (Relative L² Error)

| Model | Conv-Diff | React-Diff | Neutron Diff | Burgers | Adv-React |
|-------|-----------|------------|--------------|---------|-----------|
| SCNO (frozen) | 28.1% | 2.1% | 9.4% | 19.6% | 16.7% |
| **SCNO + Corr** | **14.1%** | **2.1%** | **4.6%** | **11.6%** | **4.1%** |
| Monolithic SNN | 10.7% | 5.5% | 13.7% | 15.3% | 6.2% |
| ANN DeepONet | 15.7% | 6.0% | 11.1% | 16.2% | 6.2% |

### Parameter Efficiency

| Component | Trainable Parameters |
|-----------|---------------------|
| Spiking Block (each) | 462K (frozen) |
| Aggregator | 231K |
| Correction Network | 95K |
| **Total (per new PDE)** | **95K-231K** |
| Monolithic Baseline | 462K |

**Result:** 5× fewer trainable parameters than monolithic approaches.

### Energy Analysis

| Model | Spike Count | Energy (0.9 pJ/spike) |
|-------|-------------|----------------------|
| Monolithic SNN | ~4.5M | ~4 nJ |
| SCNO (2 blocks) | ~9M | ~9 nJ |
| ANN DeepONet | N/A | ~1000 nJ (GPU) |

---

## Usage Examples

### Example 1: Training Elementary Blocks

```python
# Initialize block library
block_library = {}

# Train convection block
convection_pde = ConvectionPDE(c=1.0)
convection_block = SpikingDeepONetBlock(Ts=30)
train_elementary_block(convection_block, convection_pde, epochs=800)
block_library['nabla'] = convection_block

# Train diffusion block
diffusion_pde = DiffusionPDE(nu=0.1)
diffusion_block = SpikingDeepONetBlock(Ts=20)
train_elementary_block(diffusion_block, diffusion_pde, epochs=800)
block_library['delta'] = diffusion_block

# Freeze all blocks
for block in block_library.values():
    for param in block.parameters():
        param.requires_grad = False
```

### Example 2: Solving Coupled PDE (Reaction-Diffusion)

```python
# Configure SCNO for reaction-diffusion
scno = SCNO(block_library, use_correction=True)
scno.configure_for_pde(['delta', 'f'])  # diffusion + reaction

# Train aggregator and correction
react_diff_pde = ReactionDiffusionPDE(nu=0.1, k=1.0)
train_loader = create_dataloader(react_diff_pde, n_samples=1500)
val_loader = create_dataloader(react_diff_pde, n_samples=400)

train_scno(scno, train_loader, val_loader, epochs=500)

# Inference
u0_test = generate_initial_condition()
y_query = torch.linspace(0, 1, 100).unsqueeze(-1)
u_pred = scno(u0_test.unsqueeze(0), y_query.unsqueeze(0))
```

### Example 3: Nuclear Neutron Diffusion

```python
# 1-group neutron diffusion: ∂ₜϕ = D·∂ₓₓϕ + (νΣf - Σa)·ϕ
# Composed from diffusion + reaction blocks

scno_neutron = SCNO(block_library, use_correction=True)
scno_neutron.configure_for_pde(['delta', 'f'])

# Physical parameters
D = 1.0  # Diffusion coefficient
sigma_a = 0.1  # Absorption cross-section
nu_sigma_f = 0.12  # Fission production

neutron_pde = NeutronDiffusion(D, sigma_a, nu_sigma_f)
train_loader = create_dataloader(neutron_pde, n_samples=1500)

train_scno(scno_neutron, train_loader, val_loader, epochs=500)

# Expected result: ~4.6% relative L² error
```

---

## Key Advantages

### 1. Zero Forgetting

Frozen blocks ensure previously learned operators maintain identical performance when new blocks are added:

```python
# Phase 1: Train convection
block_library = {'nabla': convection_block}
error_after_phase1 = evaluate(block_library['nabla'], convection_pde)  # 8.6%

# Phase 2: Add diffusion
diffusion_block = train_new_block('diffusion')
block_library['delta'] = diffusion_block
error_after_phase2 = evaluate(block_library['nabla'], convection_pde)  # Still 8.6%

# Phase 3: Add reaction
reaction_block = train_new_block('reaction')
block_library['f'] = reaction_block
error_after_phase3 = evaluate(block_library['nabla'], convection_pde)  # Still 8.6%
```

### 2. Modular Expansion

```python
def add_new_physics(new_operator_type, training_data):
    """
    Add new physics to SCNO without affecting existing blocks.
    """
    # 1. Train new block
    new_block = SpikingDeepONetBlock(Ts=20)
    train_elementary_block(new_block, training_data)
    new_block.freeze()
    
    # 2. Add to library
    block_library[new_operator_type] = new_block
    
    # 3. Train aggregator for compositions involving new block
    # Existing compositions remain unchanged
    
    return block_library
```

### 3. Interpretable Coupling Strength

The learned $\alpha$ parameter indicates coupling strength:

| PDE | $\alpha$ | Interpretation |
|-----|----------|----------------|
| React-Diff | 0.09 | Weak coupling (blocks sufficient) |
| Neutron Diff | 0.39 | Moderate coupling |
| Burgers | 0.43 | Strong coupling |
| Adv-React | 0.46 | Strong coupling |

Use $\alpha$ as diagnostic: $\alpha > 0.3$ indicates correction network is essential.

---

## Limitations and Future Work

### Current Limitations

1. **Accuracy on Strong Coupling:** Convection-diffusion (14.1% vs 10.7% monolithic)
2. **1D Only:** Extension to 2D/3D requires graph-based operators
3. **Hybrid Deployment:** Correction network uses standard neurons
4. **GPU Training:** Surrogate gradients require GPU; inference is neuromorphic

### Recommended Extensions

```python
# 2D extension (conceptual)
class GraphSpikingBlock(nn.Module):
    """
    Graph-based spiking operator for 2D/3D PDEs.
    Uses message passing on unstructured grids.
    """
    def __init__(self, node_features, edge_features):
        super().__init__()
        self.graph_conv = SpikingGraphConv(node_features, edge_features)
        self.lif = LIFNeuron()
        
# Physics-informed training (integrating SPINONet)
def physics_informed_block_training(block, pde):
    """
    Combine SCNO composition with SPINONet physics-informed training.
    """
    def loss_fn(u_pred, u_true, x, t):
        data_loss = MSE(u_pred, u_true)
        physics_loss = pde.residual(u_pred, x, t)
        return data_loss + 0.1 * physics_loss
```

---

## Deployment on Neuromorphic Hardware

### Intel Loihi 2 Configuration

```python
# Lava-DL configuration for Loihi 2
def configure_for_loihi(block_library):
    """
    Convert trained blocks to Lava processes for Loihi 2.
    """
    from lava.magma.core.processes.ports import InPort, OutPort
    from lava.magma.core.process import AbstractProcess
    
    loihi_blocks = {}
    for name, block in block_library.items():
        # Export weights
        weights = extract_spiking_weights(block)
        
        # Create LIF process
        lif_process = LIFProcess(
            shape=(256,),  # Hidden dimension
            du=block.lif_layers[0].beta.item(),
            dv=0.0,
            bias_mant=0,
            bias_exp=0,
            vth=1.0
        )
        loihi_blocks[name] = lif_process
    
    return loihi_blocks
```

### Energy Estimation

```python
def estimate_energy_usage(scno_model, num_samples=1000):
    """
    Estimate energy consumption on neuromorphic hardware.
    """
    total_spikes = 0
    
    for _ in range(num_samples):
        # Count spikes in each block
        for block in scno_model.block_library.values():
            spikes = count_spikes(block, input_sample)
            total_spikes += spikes
    
    # Loihi 2: ~0.9 pJ per spike
    energy_per_inference = total_spikes / num_samples * 0.9e-12  # Joules
    
    return energy_per_inference
```

---

## References

1. **SCNO Paper:** Roy et al., "SCNO: Spiking Compositional Neural Operator -- Towards a Neuromorphic Foundation Model for Nuclear PDE Solving", arXiv:2604.11625, 2026

2. **DeepONet:** Lu et al., "Learning nonlinear operators via DeepONet based on the universal approximation theorem of operators", Nature Machine Intelligence, 2021

3. **FNO:** Li et al., "Fourier neural operator for parametric partial differential equations", ICLR, 2021

4. **SPINONet:** Garg et al., "SPINONet: Scalable spiking physics-informed neural operator", arXiv:2603.21674, 2026

5. **CompNO:** Hmida et al., "CompNO: A novel foundation model approach for solving partial differential equations", Applied Sciences, 2026

6. **Loihi 2:** Davies et al., "Advancing neuromorphic computing with Loihi: A survey of results and outlook", Proc. IEEE, 2021

---

## Citation

```bibtex
@article{roy2026scno,
  title={SCNO: Spiking Compositional Neural Operator -- Towards a Neuromorphic Foundation Model for Nuclear PDE Solving},
  author={Roy, Samrendra and Chakraborty, Souvik and Rizwan-uddin and Alam, Syed Bahauddin},
  journal={arXiv preprint arXiv:2604.11625},
  year={2026}
}
```

---

## Summary

SCNO represents a paradigm shift in neural operator design by combining:
- **Modularity:** Reusable spiking blocks for elementary operators
- **Energy Efficiency:** Spike-based computation compatible with neuromorphic hardware
- **Continual Learning:** Zero forgetting through frozen block architecture
- **Interpretability:** Learned coupling strength ($\alpha$) as physics diagnostic

This architecture is particularly valuable for nuclear engineering applications requiring real-time PDE solving on edge devices, enabling digital twins that can adapt to evolving physics without retraining from scratch.
