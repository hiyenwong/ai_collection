---
name: vs-gno-variable-spiking-graph-neural-operator
description: >
  Variable Spiking Graph Neural Operator (VS-GNO) for edge-deployable virtual
  sensing on irregular geometries. Integrates spectral-spatial graph convolution
  with Variable Spiking Neuron (VSN) and energy-error balance loss for
  sparse-to-dense reconstruction with controllable spiking sparsity. Achieves
  0.71% error at 15% spiking on complex engineering geometries.
triggers:
  - graph neural operator
  - virtual sensing
  - sparse-to-dense
  - irregular geometry
  - edge deployment
  - spiking neural network
  - variable spiking neuron
  - VSN
  - VS-GNO
  - neural operator
  - graph convolution
  - spectral-spatial
  - neuromorphic hardware
  - energy efficiency
  - engineering sensing
paper: arxiv 2604.16722
categories:
  - cs.LG
  - cs.NE
  - cs.CE
---

# Variable Spiking Graph Neural Operator (VS-GNO)

## 1. Overview

### Edge-Deployable Neural Operators for Virtual Sensing

Predicting full-field physics through real-time virtual sensing of engineering systems requires sparse-to-dense reconstruction over complex multiphysics on highly irregular geometries, with strict latency and energy constraints for edge deployment. Neural operators are a promising candidate, but few architectures explicitly address power consumption.

**Key innovation**: The paper (arXiv 2604.16722) presents the **Variable Spiking Graph Neural Operator (VS-GNO)**, which integrates:
1. **Spectral-spatial graph convolution** for processing irregular mesh geometries.
2. **Variable Spiking Neuron (VSN)** for controllable activation sparsity.
3. **Energy-error balance loss function** for trading accuracy against spiking activity.

Performance highlights:
- Non-spiking L₂ error baseline: **0.4%**
- Spectral-only spiking (15% avg spiking): **0.71% error**
- Full spiking (24.5% avg spiking): **1.04% error**

This positions VS-GNO as a step toward **energy-efficient, edge-deployable neural operators** for real-time sensing in complex engineering environments.

---

## 2. Core Methodology

### 2.1 Graph Neural Operator Backbone

Unlike grid-based neural operators (FNO, WNO), VS-GNO operates on **arbitrary graph meshes** representing irregular engineering geometries:

```
Sparse Sensor Nodes → Graph Neural Operator → Dense Full-Field Prediction
        ↓                      ↓                        ↓
   Limited sensors      Spectral-Spatial        Virtual sensor
   on physical part     Graph Convolution        reconstruction
```

The graph representation:
- **Nodes**: Spatial points on the engineering geometry.
- **Edges**: Connectivity from mesh discretization or k-nearest neighbors.
- **Features**: Physical quantities (temperature, pressure, velocity, etc.).

### 2.2 Spectral-Spatial Graph Convolution

VS-GNO employs a dual-branch convolution strategy:

| Branch | Domain | Purpose |
|---|---|---|
| **Spectral** | Graph Fourier (eigendecomposition of Laplacian) | Global frequency patterns |
| **Spatial** | Local neighborhood aggregation | Local geometric features |

**Spectral branch**:
1. Compute graph Laplacian L = D - A.
2. Eigendecomposition: L = UΛU^T.
3. Transform features to spectral domain: f̂ = U^T f.
4. Apply learned spectral kernel: ĝ = K(Λ) ⊙ f̂.
5. Inverse transform: g = U ĝ.

**Spatial branch**:
1. For each node, aggregate neighbors: h_i = Σ_j α_ij · MLP(f_i, f_j, e_ij).
2. Attention weights α_ij based on feature similarity and edge attributes.

The two branches are combined via a learned fusion mechanism.

### 2.3 Variable Spiking Neuron (VSN) Integration

The VSN replaces standard activation functions to introduce controllable sparsity:

```python
# Conceptual VSN mechanism
class VariableSpikingNeuron:
    def __init__(self, threshold, decay, refractory):
        self.threshold = threshold    # Firing threshold
        self.decay = decay            # Membrane decay factor
        self.refractory = refractory  # Refractory period
    
    def forward(self, x, membrane_state):
        # Integrate input
        membrane = self.decay * membrane_state + x
        
        # Spike generation with variable threshold
        spike = (membrane >= self.threshold).float()
        
        # Reset membrane after spike
        membrane = membrane * (1 - spike)
        
        return spike, membrane
```

Key properties:
- **Controllable sparsity**: Adjust threshold to control spike rate.
- **Surrogate gradient**: Differentiable approximation for backpropagation.
- **Per-layer configuration**: Each graph convolutional layer can have independent VSN parameters.

### 2.4 Energy-Error Balance Loss

The training objective balances reconstruction accuracy with spiking energy:

```
L_total = L_reconstruction + λ · L_energy

Where:
  L_reconstruction = ||y_pred - y_true||₂
  L_energy = mean(spike_rate)  # Average fraction of neurons firing
  λ = energy-error tradeoff coefficient
```

By tuning λ:
- **λ → 0**: Prioritize accuracy (approaches non-spiking baseline).
- **λ → ∞**: Minimize spiking (aggressive energy saving, more accuracy loss).

### 2.5 Spiking Configurations

VS-GNO supports two spiking modes:

| Mode | Layers with VSN | Spiking Rate | Error |
|---|---|---|---|
| **Spectral-only** | Spectral branch only | 15% average | 0.71% |
| **Full** | Both spectral + spatial | 24.5% average | 1.04% |
| **Non-spiking** | Standard activations | 0% | 0.40% |

The spectral-only mode is recommended for edge deployment — significant energy reduction with minimal accuracy degradation.

---

## 3. Implementation Guide

### 3.1 Problem Setup

```python
# Typical virtual sensing problem
class VirtualSensingConfig:
    # Geometry
    mesh_file = "engineering_part.msh"        # Irregular mesh
    sensor_locations = [10, 25, 47, 83, 156]  # Sparse sensor indices
    n_nodes = 5000                             # Total mesh nodes
    
    # Model
    hidden_dim = 64
    n_layers = 4
    spiking_mode = "spectral_only"  # or "full", "none"
    spike_threshold = 1.0
    spike_decay = 0.9
    
    # Training
    energy_weight = 0.01   # λ in energy-error balance loss
    learning_rate = 1e-3
    epochs = 500
```

### 3.2 Model Architecture

```python
# Conceptual VS-GNO architecture
import torch
import torch.nn as nn

class VSGNO(nn.Module):
    def __init__(self, in_dim, hidden_dim, out_dim, n_layers, 
                 spiking_mode="spectral_only"):
        super().__init__()
        self.encoder = nn.Linear(in_dim, hidden_dim)
        self.layers = nn.ModuleList([
            VSGNOLayer(hidden_dim, spiking_mode) 
            for _ in range(n_layers)
        ])
        self.decoder = nn.Linear(hidden_dim, out_dim)
    
    def forward(self, x, edge_index, batch):
        h = self.encoder(x)
        for layer in self.layers:
            h = layer(h, edge_index) + h  # Skip connection
        return self.decoder(h)

class VSGNOLayer(nn.Module):
    def __init__(self, hidden_dim, spiking_mode):
        super().__init__()
        self.spectral_conv = SpectralGraphConv(hidden_dim)
        self.spatial_conv = SpatialGraphConv(hidden_dim)
        self.fusion = nn.Linear(hidden_dim * 2, hidden_dim)
        
        # VSN in spectral branch (always)
        self.vsn_spectral = VariableSpikingNeuron(hidden_dim)
        
        # VSN in spatial branch (if full mode)
        self.vsn_spatial = (
            VariableSpikingNeuron(hidden_dim) 
            if spiking_mode == "full" else None
        )
    
    def forward(self, x, edge_index):
        # Spectral branch with spiking
        h_spec = self.spectral_conv(x)
        h_spec, spike_rate = self.vsn_spectral(h_spec)
        
        # Spatial branch
        h_spat = self.spatial_conv(x, edge_index)
        if self.vsn_spatial:
            h_spat, _ = self.vsn_spatial(h_spat)
        
        # Fuse
        return self.fusion(torch.cat([h_spec, h_spat], dim=-1))
```

### 3.3 Training with Energy-Error Balance

```python
def train_vsgno(model, dataloader, optimizer, energy_weight):
    for batch in dataloader:
        pred = model(batch.x, batch.edge_index, batch.batch)
        
        # Reconstruction loss
        loss_recon = F.mse_loss(pred, batch.y)
        
        # Energy loss (average spike rate)
        loss_energy = model.get_avg_spike_rate()
        
        # Combined loss
        loss = loss_recon + energy_weight * loss_energy
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
```

---

## 4. Applications

| Application | Description | Geometry Type |
|---|---|---|
| Thermal sensing | Sparse thermocouple → full temperature field | Turbine blade, heat sink |
| Structural monitoring | Sparse strain gauges → full stress field | Complex mechanical parts |
| Fluid dynamics | Sparse pressure taps → full pressure field | Pipe networks, valves |
| Electromagnetic sensing | Sparse probes → full EM field | Antenna, waveguide |
| Multiphysics coupling | Temperature + pressure + flow | Engine components |

---

## 5. Comparison with Related Neural Operators

| Method | Geometry Support | Spiking | Edge-Aware | Irregular Mesh | Error at Low Sparsity |
|---|---|---|---|---|---|
| **VS-GNO** | Graph (irregular) | Yes (VSN) | Yes | ✓ | 0.71% @ 15% spiking |
| VS-WNO | Grid (wavelet) | Yes (VSN) | Yes | ✗ | Varies |
| FNO | Grid (Fourier) | No | No | ✗ | N/A |
| DeepONet | Arbitrary | No | No | Partial | N/A |
| GNO | Graph | No | No | ✓ | N/A |

---

## 6. Pitfalls

### 6.1 Graph Eigendecomposition Cost
- Spectral graph convolution requires eigendecomposition of the graph Laplacian.
- **Cost: O(N³)** for N nodes — prohibitive for very large meshes.
- **Mitigation**: Pre-compute eigenvectors for fixed geometries; use Chebyshev polynomial approximation for large graphs.

### 6.2 Spiking Degradation on Regression
- Spiking neurons were originally designed for classification (binary output).
- For regression (continuous field prediction), spiking introduces quantization noise.
- **Mitigation**: Use membrane potential as continuous readout alongside binary spikes; keep spectral-only mode for better accuracy.

### 6.3 Mesh Dependency
- Model performance depends on mesh quality and resolution.
- Transferring between different mesh discretizations requires retraining or interpolation.
- **Mitigation**: Use consistent meshing protocols; train with mesh augmentation.

### 6.4 Sensor Placement Sensitivity
- Virtual sensing quality depends critically on where physical sensors are placed.
- Optimal sensor placement is a separate combinatorial optimization problem.
- **Mitigation**: Use information-theoretic sensor placement strategies before training VS-GNO.

---

## 7. References

- **This paper**: Howes, W., Ahmed, F., Kobayashi, K., Chakraborty, S., Alam, S.B. "Neuroscience Inspired Graph Operators Towards Edge-Deployable Virtual Sensing for Irregular Geometries." arXiv 2604.16722, 2026.

- **Variable Spiking Neuron**: Prior work on VSN for controllable spiking sparsity.

- **Graph Neural Operator**: Li, Z., et al. "Neural Operator: Graph Kernel Network for Partial Differential Equations." ICLR, 2021.

- **Fourier Neural Operator**: Li, Z., et al. "Fourier Neural Operator for Parametric PDEs." ICLR, 2021.

---

## 8. Related Skills

- vs-wno-variable-spiking-wavelet: Variable Spiking Wavelet Neural Operator for grid-based PDEs
- spiking-compositional-neural-operator: Spiking Compositional Neural Operator
- neuromorphic-low-power-ai: Neuromorphic computing approaches
- adaptive-spiking-neuron-asn: Adaptive Spiking Neuron methodology
