---
name: primate-ventral-visual-stream-dynamic
description: "Framework for modeling temporal dynamics in the primate ventral visual stream across intrinsic dynamics, dynamic visual stimuli, and active sensing during eye movements. Activation: primate vision, ventral visual stream, VVS dynamics, active sensing."
---

# Dynamic Computations in Primate Ventral Visual Stream

> Comprehensive framework for modeling dynamic neural computations in the primate ventral visual stream (VVS) beyond static snapshot approaches.

## Metadata
- **Source**: arXiv:2601.12258
- **Authors**: Matteo Dunnhofer, Maren Wehrheim, Hamidreza Ramezanpour, Sabine Muzellec, Kohitij Kar
- **Published**: 2026-01-18
- **Category**: q-bio.NC

## Core Methodology

### Three Domains of VVS Dynamics

#### 1. Intrinsic Dynamics
- Dynamics elicited by static images
- Recurrent interactions and intrinsic circuit dynamics
- Time-varying responses beyond feedforward processing

#### 2. Dynamic Visual Stimuli
- Responses to moving objects and changing scenes
- Temporal evolution of neural representations
- Motion processing and temporal integration

#### 3. Active Sensing During Eye Movements
- Saccadic eye movements and fixation dynamics
- Real-world vision with active sampling
- Top-down modulation during visual exploration

### Key Insights
- VVS responses are **rich dynamical signals** shaped by:
  - Retinal input
  - Intrinsic circuit dynamics
  - Recurrent interactions
  - Widespread top-down modulation

### Required Model Components
1. **Multi-area recurrence**: Interactions between visual areas
2. **Structured E/I interactions**: Excitatory/inhibitory balance
3. **Temporal objectives**: Natural behavior alignment
4. **Multi-timescale dynamics**: Fast and slow processing

## Implementation Guide

### Prerequisites
```python
import torch
import torch.nn as nn
import torchvision
```

### Current Static Approaches vs Dynamic Framework

```python
class StaticVVSModel(nn.Module):
    """Traditional feedforward model for static snapshots."""
    def __init__(self):
        super().__init__()
        self.backbone = torchvision.models.resnet50(pretrained=True)
    
    def forward(self, static_image):
        # Single snapshot processing
        return self.backbone(static_image)

class DynamicVVSModel(nn.Module):
    """
    Dynamic model for temporal visual processing.
    
    Components:
    - Recurrent connections for temporal integration
    - Multi-area processing
    - Structured E/I dynamics
    - Active sensing (eye movements)
    """
    def __init__(self, num_areas=4, hidden_dim=512, num_timescales=3):
        super().__init__()
        self.num_areas = num_areas
        self.num_timescales = num_timescales
        
        # Multi-area recurrent processing
        self.areas = nn.ModuleList([
            RecurrentArea(hidden_dim, num_timescales) 
            for _ in range(num_areas)
        ])
        
        # Inter-area connections
        self.connections = InterAreaConnections(num_areas, hidden_dim)
        
        # Active sensing module (eye movement prediction)
        self.active_sensing = ActiveSensingModule(hidden_dim)
        
    def forward(self, video_sequence, eye_position=None):
        """
        Process dynamic visual input.
        
        Args:
            video_sequence: [T, C, H, W] temporal frames
            eye_position: [T, 2] gaze position for active sensing
            
        Returns:
            area_outputs: List of [T, hidden_dim] per area
            eye_movements: [T, 2] predicted saccades
        """
        T = video_sequence.shape[0]
        states = [[None for _ in range(self.num_timescales)] 
                  for _ in range(self.num_areas)]
        outputs = [[] for _ in range(self.num_areas)]
        eye_movements = []
        
        for t in range(T):
            # Extract features from current frame
            feat = self.extract_features(video_sequence[t])
            
            # Update active sensing (predict next fixation)
            if t < T - 1:
                saccade = self.active_sensing(
                    feat, eye_position[t] if eye_position is not None else None
                )
                eye_movements.append(saccade)
            
            # Process through areas with recurrence
            for i, area in enumerate(self.areas):
                # Inter-area inputs
                recurrent_input = self.connections(states, i)
                
                # Multi-timescale processing
                states[i] = area(feat, states[i], recurrent_input)
                outputs[i].append(states[i][-1])  # Fastest timescale
        
        return [torch.stack(o) for o in outputs], torch.stack(eye_movements)

class RecurrentArea(nn.Module):
    """
    Single area with structured E/I dynamics and multi-timescale processing.
    """
    def __init__(self, dim, num_timescales=3):
        super().__init__()
        self.num_timescales = num_timescales
        
        # Excitatory cells at different timescales
        self.exc = nn.ModuleList([
            TimescaleGRUCell(dim, dim, tau=10**i)  # 1, 10, 100 ms
            for i in range(num_timescales)
        ])
        
        # Inhibitory cells (single fast timescale)
        self.inh = nn.GRUCell(dim * num_timescales, dim)
        
        # E/I balance parameters
        self.ei_balance = nn.Parameter(torch.zeros(dim))
        
    def forward(self, input_feat, prev_states, recurrent_input):
        """
        Process input with structured E/I dynamics.
        
        Args:
            input_feat: Current input [batch, dim]
            prev_states: List of [batch, dim] per timescale
            recurrent_input: Inter-area recurrent input [batch, dim]
        
        Returns:
            new_states: Updated states for each timescale
        """
        # Process each timescale
        exc_states = []
        for i, (exc_cell, prev) in enumerate(zip(self.exc, prev_states or [None]*self.num_timescales)):
            if prev is None:
                prev = torch.zeros_like(input_feat)
            state = exc_cell(input_feat + recurrent_input, prev)
            exc_states.append(state)
        
        # Combine all timescales for inhibition
        combined_exc = torch.cat(exc_states, dim=-1)
        inh_state = self.inh(combined_exc, torch.zeros_like(input_feat) 
                            if prev_states[0] is None else prev_states[0])
        
        # Apply E/I balance with learned modulation
        new_states = []
        for i, exc in enumerate(exc_states):
            # Different inhibition strength per timescale
            balance = torch.sigmoid(self.ei_balance * (i + 1))
            modulated = exc - balance * inh_state
            new_states.append(torch.relu(modulated))
        
        return new_states

class TimescaleGRUCell(nn.Module):
    """GRU cell with configurable timescale constant."""
    def __init__(self, input_size, hidden_size, tau=10.0):
        super().__init__()
        self.tau = tau  # Timescale in ms
        self.gru = nn.GRUCell(input_size, hidden_size)
        
    def forward(self, input, hidden):
        # Standard GRU update
        new_hidden = self.gru(input, hidden)
        
        # Timescale integration (leaky integration)
        alpha = 1.0 / self.tau
        return hidden + alpha * (new_hidden - hidden)

class InterAreaConnections(nn.Module):
    """Structured connections between visual areas."""
    def __init__(self, num_areas, dim):
        super().__init__()
        self.num_areas = num_areas
        
        # Feedforward (lower to higher) and feedback (higher to lower)
        self.feedforward = nn.ModuleList([
            nn.Linear(dim, dim) for _ in range(num_areas - 1)
        ])
        self.feedback = nn.ModuleList([
            nn.Linear(dim, dim) for _ in range(num_areas - 1)
        ])
        
    def forward(self, states, target_area):
        """Compute recurrent input for target area."""
        inputs = []
        
        # Feedforward from lower areas
        if target_area > 0 and states[target_area - 1] is not None:
            ff_input = self.feedforward[target_area - 1](
                states[target_area - 1][-1]  # Fastest timescale
            )
            inputs.append(ff_input)
        
        # Feedback from higher areas
        if target_area < self.num_areas - 1 and states[target_area + 1] is not None:
            fb_input = self.feedback[target_area](
                states[target_area + 1][-1]
            )
            inputs.append(fb_input)
        
        if inputs:
            return sum(inputs) / len(inputs)
        return torch.zeros_like(states[0][0]) if states[0] else None

class ActiveSensingModule(nn.Module):
    """Predicts eye movements for active visual exploration."""
    def __init__(self, dim):
        super().__init__()
        self.saccade_predictor = nn.Sequential(
            nn.Linear(dim + 2, 256),  # +2 for current position
            nn.ReLU(),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Linear(128, 2),  # Delta x, y
            nn.Tanh()  # Bounded saccade amplitude
        )
        
    def forward(self, visual_features, current_position):
        if current_position is None:
            current_position = torch.zeros(2)
        
        combined = torch.cat([visual_features, current_position], dim=-1)
        saccade = self.saccade_predictor(combined)
        
        return saccade
```

### Training with Temporal Objectives

```python
def train_dynamic_vvs(model, dataloader, epochs=100):
    """
    Train with temporal objectives reflecting natural behavior.
    """
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)
    
    for epoch in range(epochs):
        for batch in dataloader:
            video, labels, eye_positions = batch
            
            # Forward pass
            area_outputs, predicted_saccades = model(video, eye_positions)
            
            # Multi-objective loss
            # 1. Classification (highest area)
            classification_loss = F.cross_entropy(
                area_outputs[-1], labels
            )
            
            # 2. Temporal consistency (smoothness)
            temporal_loss = temporal_consistency_loss(area_outputs)
            
            # 3. Active sensing prediction
            saccade_loss = F.mse_loss(predicted_saccades[:-1], eye_positions[1:])
            
            # 4. Representational alignment with brain data (optional)
            neural_loss = alignment_loss(area_outputs, neural_recordings)
            
            total_loss = (
                classification_loss + 
                0.1 * temporal_loss + 
                0.5 * saccade_loss +
                0.01 * neural_loss
            )
            
            optimizer.zero_grad()
            total_loss.backward()
            optimizer.step()

def temporal_consistency_loss(area_outputs):
    """Encourage smooth temporal evolution."""
    losses = []
    for output in area_outputs:
        # L2 smoothness penalty
        diff = output[1:] - output[:-1]
        losses.append(torch.mean(diff**2))
    return sum(losses)

def alignment_loss(model_outputs, neural_data):
    """Align model representations with neural recordings."""
    # Can use RSA, CKA, or other alignment metrics
    from sklearn.metrics import r2_score
    
    model_repr = model_outputs[-1].detach().cpu().numpy()
    neural_repr = neural_data
    
    # Compute representational similarity
    model_rdm = 1 - np.corrcoef(model_repr)
    neural_rdm = 1 - np.corrcoef(neural_repr)
    
    return np.mean((model_rdm - neural_rdm)**2)
```

## Key Missing Ingredients

1. **Behavioral context integration**: Task-dependent modulation
2. **Multi-scale temporal processing**: From milliseconds to seconds
3. **Predictive coding**: Top-down predictions and prediction errors
4. **Attention mechanisms**: Selective processing of relevant information
5. **Reward-based learning**: Reinforcement learning for active sensing

## Comparison with Static Models

| Aspect | Static Models | Dynamic VVS Models |
|--------|--------------|-------------------|
| Input | Single image | Video sequences |
| Processing | Feedforward | Recurrent + feedback |
| Temporal | Time-averaged | Time-resolved |
| Eye movements | None | Active saccadic sampling |
| Brain alignment | Snapshot responses | Temporal dynamics |
| Real-world | Limited | Natural vision conditions |

## Pitfalls
- **Computational cost**: Recurrent processing is slower than feedforward
- **Training instability**: Multi-timescale dynamics can be hard to train
- **Data requirements**: Need video datasets with temporal labels
- **Hyperparameter sensitivity**: E/I balance and timescales need careful tuning

## Related Skills
- vision-bottleneck-v1
- primary-visual-cortex-v1-functions
- untrained-cnns-match-backprop-v1
- neural-population-dynamics

## References
- arXiv:2601.12258 - Modeling Dynamic Computations in the Primate Ventral Visual Stream
