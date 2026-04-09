# spatiotemporal-dynamical-computation - A Spatiotemporal Perspective on Dynamical Computation in Neural Information Processing Systems

## Description

A theoretical framework that formalizes the connection between motion and flowing neural dynamics using equivariant neural network theory. Shows that traveling waves are not just useful but necessary for accurate processing of signals undergoing motion, and that recurrent connectivity must realize homomorphic representations of stimulus flows.

**Source:** arXiv:2409.13669v2
**Utility:** 0.91

## Activation Keywords

- spatiotemporal computation
- traveling waves neural
- equivariant neural network
- dynamical computation
- motion flow dynamics
- homomorphic representation
- recurrent traveling waves

## Core Concepts

### 1. Spatiotemporal Flows Framework

```
Stimulus Flow → Recurrent Connectivity → Homomorphic Representation → Equivariant Processing
```

**Key insight:** Traveling waves are faithful dynamic representations of stimulus flows.

### 2. Equivariant Neural Network Theory

| Concept | Description |
|---------|-------------|
| **Equivariance** | Output transforms predictably under input transformation |
| **Homomorphic representation** | Hidden state dynamics realize stimulus flow structure |
| **Recurrent connectivity** | Necessary for structured equivariant processing |

### 3. Motion Spaces

**Physical Motion:**
- Visual motion in retinotopic space
- Physical motion in motor space

**Abstract Motion:**
- Motion in representational spaces
- Flow transformations in abstract domains

### 4. Traveling Waves as Dynamic Representations

| Wave Type | Function |
|-----------|----------|
| **Forward waves** | Propagate information forward |
| **Backward waves** | Feedback and correction |
| **Lateral waves** | Lateral integration |

### 5. Biological Inductive Bias

**Natural inclination towards traveling wave dynamics:**
- Efficiency in spatiotemporally-structured world
- Generalization to new flow patterns
- Stability in dynamic processing

## Step-by-Step Instructions

### 1. Equivariant Network Design

```python
import numpy as np
import torch
import torch.nn as nn

class EquivariantRecurrentLayer(nn.Module):
    """
    Recurrent layer that realizes homomorphic representation of flow.
    
    Args:
        input_dim: Input dimension
        hidden_dim: Hidden state dimension
        flow_dim: Flow transformation dimension
    """
    def __init__(self, input_dim, hidden_dim, flow_dim):
        super().__init__()
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.flow_dim = flow_dim
        
        # Input projection
        self.input_proj = nn.Linear(input_dim, hidden_dim)
        
        # Recurrent connectivity (homomorphic to flow)
        self.recurrent = nn.Linear(hidden_dim, hidden_dim)
        
        # Flow transformation layer
        self.flow_transform = nn.Linear(flow_dim, hidden_dim)
        
    def forward(self, x, h_prev, flow):
        """
        Equivariant forward pass.
        
        Args:
            x: Input [batch, seq_len, input_dim]
            h_prev: Previous hidden state [batch, hidden_dim]
            flow: Flow transformation [batch, flow_dim]
        
        Returns:
            h_new: New hidden state
        """
        # Input contribution
        h_input = self.input_proj(x)
        
        # Recurrent contribution (homomorphic to flow)
        h_recurrent = self.recurrent(h_prev)
        
        # Flow modulation
        h_flow = self.flow_transform(flow)
        
        # Combine
        h_new = h_input + h_recurrent + h_flow
        h_new = torch.tanh(h_new)
        
        return h_new
```

### 2. Traveling Wave Dynamics

```python
class TravelingWaveNetwork(nn.Module):
    """
    Network that implements traveling wave dynamics for equivariant processing.
    
    Args:
        spatial_dim: Spatial dimension (e.g., visual space)
        hidden_dim: Hidden state dimension
        wave_speed: Wave propagation speed
    """
    def __init__(self, spatial_dim, hidden_dim, wave_speed=1.0):
        super().__init__()
        self.spatial_dim = spatial_dim
        self.hidden_dim = hidden_dim
        self.wave_speed = wave_speed
        
        # Spatial layers
        self.spatial_layers = nn.ModuleList([
            nn.Linear(hidden_dim, hidden_dim) for _ in range(spatial_dim)
        ])
        
        # Wave propagation matrix
        self.propagation = self._create_propagation_matrix()
        
    def _create_propagation_matrix(self):
        """
        Create wave propagation matrix.
        
        Returns:
            Propagation matrix that shifts activation across space
        """
        # Shift matrix for wave propagation
        shift_matrix = np.zeros((self.spatial_dim, self.spatial_dim))
        for i in range(self.spatial_dim - 1):
            shift_matrix[i, i + 1] = 1  # Forward propagation
            shift_matrix[i + 1, i] = 0.5  # Backward propagation
            
        return torch.tensor(shift_matrix, dtype=torch.float32)
    
    def forward(self, spatial_input):
        """
        Propagate traveling wave across spatial dimension.
        
        Args:
            spatial_input: Input [batch, spatial_dim, hidden_dim]
        
        Returns:
            wave_output: Wave output [batch, spatial_dim, hidden_dim]
        """
        # Apply wave propagation
        wave_state = spatial_input.clone()
        
        for t in range(self.wave_speed):
            # Propagate wave
            wave_state = torch.matmul(self.propagation, wave_state)
            
            # Apply spatial transformations
            for i, layer in enumerate(self.spatial_layers):
                wave_state[:, i] = layer(wave_state[:, i])
        
        return wave_state
```

### 3. Homomorphic Flow Processing

```python
class HomomorphicFlowProcessor(nn.Module):
    """
    Processor that maintains homomorphic structure to stimulus flows.
    
    Args:
        flow_type: Type of flow (visual, motor, abstract)
        input_dim: Input dimension
        hidden_dim: Hidden dimension
    """
    def __init__(self, flow_type, input_dim, hidden_dim):
        super().__init__()
        self.flow_type = flow_type
        
        # Flow encoder
        self.flow_encoder = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim)
        )
        
        # Recurrent dynamics (homomorphic to flow)
        self.recurrent_dynamics = nn.Linear(hidden_dim, hidden_dim, bias=False)
        
        # Output decoder
        self.decoder = nn.Linear(hidden_dim, input_dim)
        
    def process_sequence_with_flow(self, sequence, flow_params):
        """
        Process sequence with explicit flow transformation.
        
        Args:
            sequence: Input sequence [batch, seq_len, input_dim]
            flow_params: Flow parameters [batch, flow_dim]
        
        Returns:
            output: Processed output [batch, seq_len, input_dim]
            hidden_states: Hidden states [batch, seq_len, hidden_dim]
        """
        batch_size, seq_len, _ = sequence.shape
        hidden_dim = self.flow_encoder(sequence[:, 0]).shape[-1]
        
        hidden_states = torch.zeros(batch_size, seq_len, hidden_dim)
        outputs = torch.zeros(batch_size, seq_len, sequence.shape[-1])
        
        h = self.flow_encoder(sequence[:, 0])
        
        for t in range(seq_len):
            # Encode input
            h_input = self.flow_encoder(sequence[:, t])
            
            # Recurrent update (homomorphic to flow)
            h_recurrent = self.recurrent_dynamics(h)
            
            # Combine
            h = h_input + h_recurrent
            
            hidden_states[:, t] = h
            outputs[:, t] = self.decoder(h)
        
        return outputs, hidden_states
```

### 4. Equivariance Verification

```python
def verify_equivariance(model, input_tensor, transformation):
    """
    Verify that model is equivariant to transformation.
    
    Args:
        model: Neural network model
        input_tensor: Test input
        transformation: Flow transformation
    
    Returns:
        equivariance_error: Error measure of equivariance
    """
    # Output on original input
    output_original = model(input_tensor)
    
    # Apply transformation to input
    input_transformed = transformation(input_tensor)
    
    # Output on transformed input
    output_transformed = model(input_transformed)
    
    # Apply same transformation to output
    output_should_be = transformation(output_original)
    
    # Compute equivariance error
    error = torch.norm(output_transformed - output_should_be)
    
    return error.item()
```

### 5. Motion Space Analysis

```python
def analyze_motion_space(activity_data, motion_type='visual'):
    """
    Analyze motion space from neural activity.
    
    Args:
        activity_data: Neural activity [time, space, units]
        motion_type: Type of motion (visual, motor, abstract)
    
    Returns:
        flow_structure: Identified flow structure
    """
    # Compute traveling wave patterns
    spatial_correlation = np.corrcoef(activity_data.transpose(1, 0, 2).reshape(
        activity_data.shape[1], -1
    ))
    
    # Identify wave direction
    wave_direction = np.argmax(spatial_correlation, axis=1)
    
    # Compute wave speed
    temporal_correlation = np.corrcoef(activity_data.transpose(0, 1, 2).reshape(
        activity_data.shape[0], -1
    ))
    wave_speed = np.mean(np.abs(np.diff(temporal_correlation)))
    
    flow_structure = {
        'wave_direction': wave_direction,
        'wave_speed': wave_speed,
        'spatial_correlation': spatial_correlation,
        'motion_type': motion_type
    }
    
    return flow_structure
```

## Tools Used

- `numpy` - Numerical computations
- `torch` - PyTorch neural networks
- `scipy` - Scientific computing
- `exec` - Run analysis scripts
- `read` - Load activity data

## Example Use Cases

### 1. Equivariant Network Training

```python
# Create equivariant network
model = EquivariantRecurrentLayer(input_dim=64, hidden_dim=128, flow_dim=32)

# Verify equivariance
error = verify_equivariance(model, test_input, flow_transform)
print(f"Equivariance error: {error:.4f}")
```

### 2. Traveling Wave Analysis

```python
# Create wave network
wave_net = TravelingWaveNetwork(spatial_dim=10, hidden_dim=64, wave_speed=5)

# Propagate wave
wave_output = wave_net(spatial_input)
print(f"Wave shape: {wave_output.shape}")
```

### 3. Flow Processing

```python
# Process sequence with flow
processor = HomomorphicFlowProcessor('visual', input_dim=64, hidden_dim=128)
output, hidden = processor.process_sequence_with_flow(sequence, flow_params)
```

## Related Skills

- `kuramoto-brain-network` - Oscillatory dynamics
- `time-varying-brain-connectivity` - Temporal dynamics
- `neural-dynamics-universal-translator` - Neural dynamics analysis

## References

- Keller, T. A. (2024). "A Spatiotemporal Perspective on Dynamical Computation in Neural Information Processing Systems" arXiv:2409.13669v2 [q-bio.NC]

---

**Created:** 2026-03-29 18:05
**Author:** Aerial (from arXiv:2409.13669v2)