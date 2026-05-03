---
name: brain-inspired-attention-mechanisms
description: "Brain-inspired attention mechanisms for neural networks - incorporating biological attention systems including thalamocortical circuits, pulvinar-mediated attention, basal forebrain modulation, and predictive processing. Implements biologically plausible attention for computer vision, NLP, and multi-modal AI. Activation: brain attention, thalamic attention, pulvinar, predictive attention, biological attention, neuromorphic attention, cortico-thalamic, saliency-based attention."
tags: ["brain-inspired", "attention-mechanisms", "thalamocortical", "predictive-processing", "saliency", "selective-attention", "biological-plausibility"]
---

# Brain-Inspired Attention Mechanisms

## Overview

Biological attention systems have evolved sophisticated mechanisms for selective information processing. This skill implements brain-inspired attention mechanisms that go beyond standard transformer self-attention, incorporating insights from thalamocortical circuits, predictive processing, and neuromodulatory systems.

## Biological Attention Systems

### 1. Thalamocortical Circuit

```
Biological Architecture:

Sensory Input → Thalamus → Primary Cortex
                    ↑           ↓
                  Gain       Feedback
                 Control      (Top-down)
                    ↑
               Higher-order
                 Thalamus
                    ↑
               Prefrontal
                 Cortex
```

**Key Functions:**
- **Gating**: Thalamus gates sensory input to cortex
- **Modulation**: Higher-order thalamus controls cortical gain
- **Routing**: Information routing to appropriate cortical areas

### 2. Pulvinar-Mediated Attention

```
Pulvinar (Posterior Thalamus):
    - Coordinates activity across cortical areas
    - Synchronizes relevant neural populations
    - Suppresses irrelevant information
```

### 3. Basal Forebrain Modulation

```
Basal Forebrain → Acetylcholine (ACh) → Cortex
    - Enhances signal-to-noise ratio
    - Promotes plasticity
    - Regulates arousal/attention state
```

## Brain-Inspired Attention Implementation

### 1. Thalamic Gating Attention

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class ThalamicGatingAttention(nn.Module):
    """
    Attention mechanism inspired by thalamic gating.
    
    The thalamus acts as a gate between sensory input and cortex,
    controlled by top-down attention signals.
    """
    
    def __init__(self, dim, num_heads=8, gate_bias=-3.0):
        super().__init__()
        self.dim = dim
        self.num_heads = num_heads
        self.head_dim = dim // num_heads
        self.scale = self.head_dim ** -0.5
        
        # Gating mechanism (thalamic function)
        self.gate_threshold = nn.Parameter(torch.tensor(gate_bias))
        
        # Projections
        self.q_proj = nn.Linear(dim, dim)
        self.k_proj = nn.Linear(dim, dim)
        self.v_proj = nn.Linear(dim, dim)
        self.out_proj = nn.Linear(dim, dim)
        
        # Gating control (higher-order thalamus)
        self.gate_control = nn.Sequential(
            nn.Linear(dim, dim // 4),
            nn.ReLU(),
            nn.Linear(dim // 4, num_heads),
            nn.Sigmoid()
        )
        
    def forward(self, x, context=None, return_gates=False):
        """
        Args:
            x: Input (batch, seq_len, dim)
            context: Top-down control signal (batch, dim)
        
        Returns:
            output: Attended features
            gates: Gating values (optional)
        """
        batch, seq_len, _ = x.shape
        
        # Compute queries, keys, values
        Q = self.q_proj(x).view(batch, seq_len, self.num_heads, self.head_dim)
        K = self.k_proj(x).view(batch, seq_len, self.num_heads, self.head_dim)
        V = self.v_proj(x).view(batch, seq_len, self.num_heads, self.head_dim)
        
        Q = Q.transpose(1, 2)  # (batch, heads, seq, head_dim)
        K = K.transpose(1, 2)
        V = V.transpose(1, 2)
        
        # Attention scores
        attn_scores = torch.matmul(Q, K.transpose(-2, -1)) * self.scale
        
        # Thalamic gating: determine which inputs reach cortex
        if context is not None:
            # Context-dependent gate control
            gate_control = self.gate_control(context)  # (batch, heads)
            gate_control = gate_control.view(batch, self.num_heads, 1, 1)
        else:
            gate_control = torch.sigmoid(-self.gate_threshold)
        
        # Soft attention with gating
        attn_weights = F.softmax(attn_scores, dim=-1)
        
        # Apply gate (thalamic filter)
        gated_attn = attn_weights * gate_control
        
        # Normalize after gating
        gated_attn = gated_attn / (gated_attn.sum(dim=-1, keepdim=True) + 1e-8)
        
        # Apply to values
        output = torch.matmul(gated_attn, V)
        output = output.transpose(1, 2).contiguous().view(batch, seq_len, self.dim)
        output = self.out_proj(output)
        
        if return_gates:
            return output, gate_control.squeeze()
        return output
```

### 2. Pulvinar Synchronization Attention

```python
class PulvinarSynchronizationAttention(nn.Module):
    """
    Attention inspired by pulvinar-mediated inter-areal synchronization.
    
    The pulvinar synchronizes activity across cortical areas,
    enhancing communication between relevant neural populations.
    """
    
    def __init__(self, dim, num_areas=4, sync_strength=0.5):
        super().__init__()
        self.dim = dim
        self.num_areas = num_areas
        self.area_dim = dim // num_areas
        self.sync_strength = sync_strength
        
        # Area-specific processing
        self.area_projections = nn.ModuleList([
            nn.Linear(self.area_dim, self.area_dim)
            for _ in range(num_areas)
        ])
        
        # Synchronization mechanism (pulvinar function)
        self.pulvinar = nn.Sequential(
            nn.Linear(dim, dim // 2),
            nn.LayerNorm(dim // 2),
            nn.ReLU(),
            nn.Linear(dim // 2, num_areas * num_areas)  # Area-to-area weights
        )
        
        # Phase synchronization
        self.phase_encoder = nn.Linear(dim, dim)
        
    def forward(self, x):
        """
        Synchronize processing across multiple "cortical areas".
        
        Args:
            x: (batch, seq, dim)
        
        Returns:
            synchronized: (batch, seq, dim)
        """
        batch, seq_len, _ = x.shape
        
        # Split into cortical areas
        areas = x.view(batch, seq_len, self.num_areas, self.area_dim)
        
        # Area-specific processing
        processed_areas = []
        for i, proj in enumerate(self.area_projections):
            area_out = proj(areas[:, :, i, :])
            processed_areas.append(area_out)
        
        # Compute synchronization weights (pulvinar role)
        global_repr = x.mean(dim=1)  # Global representation
        sync_weights = self.pulvinar(global_repr)  # (batch, areas^2)
        sync_weights = sync_weights.view(batch, self.num_areas, self.num_areas)
        sync_weights = F.softmax(sync_weights, dim=-1)
        
        # Synchronize areas
        synchronized = []
        for i in range(self.num_areas):
            # Weighted combination of all areas
            synced = sum(
                sync_weights[:, i, j].view(batch, 1, 1) * processed_areas[j]
                for j in range(self.num_areas)
            )
            synchronized.append(synced)
        
        # Recombine
        output = torch.stack(synchronized, dim=2).view(batch, seq_len, self.dim)
        
        # Add phase synchronization
        phase = torch.sigmoid(self.phase_encoder(x))
        output = output * phase + x * (1 - phase)
        
        return output
```

### 3. Basal Forebrain Modulated Attention

```python
class BasalForebrainModulatedAttention(nn.Module):
    """
    Attention with arousal/state modulation inspired by basal forebrain.
    
    The basal forebrain provides neuromodulatory input (ACh) that:
    - Enhances SNR in attended channels
    - Promotes plasticity
    - Regulates overall arousal
    """
    
    def __init__(self, dim, num_states=3):  # low, medium, high arousal
        super().__init__()
        self.dim = dim
        self.num_states = num_states
        
        # Arousal state estimation
        self.arousal_estimator = nn.Sequential(
            nn.Linear(dim, dim // 4),
            nn.ReLU(),
            nn.Linear(dim // 4, num_states)
        )
        
        # State-specific attention parameters
        self.state_gains = nn.Parameter(torch.ones(num_states, dim))
        self.state_thresholds = nn.Parameter(torch.zeros(num_states, dim))
        
        # Plasticity modulation (meta-learning aspect)
        self.plasticity_gate = nn.Sequential(
            nn.Linear(dim, dim),
            nn.Sigmoid()
        )
        
    def forward(self, x, return_state=False):
        """
        Modulate attention based on arousal state.
        
        Args:
            x: (batch, seq, dim)
        
        Returns:
            modulated: (batch, seq, dim)
            arousal: (batch, num_states) - arousal probabilities
        """
        batch, seq_len, _ = x.shape
        
        # Estimate arousal state
        global_x = x.mean(dim=1)
        arousal_logits = self.arousal_estimator(global_x)
        arousal_probs = F.softmax(arousal_logits, dim=-1)  # (batch, num_states)
        
        # Compute state-dependent modulation
        # Weight gains by arousal probability
        weighted_gains = torch.matmul(
            arousal_probs, self.state_gains
        ).unsqueeze(1)  # (batch, 1, dim)
        
        weighted_thresholds = torch.matmul(
            arousal_probs, self.state_thresholds
        ).unsqueeze(1)
        
        # Apply modulation (ACh-like effect)
        # Enhance signal, shift threshold
        modulated = x * (1 + 0.5 * torch.tanh(weighted_gains))
        modulated = modulated - weighted_thresholds
        
        # Plasticity modulation (which dimensions to update)
        plasticity = self.plasticity_gate(global_x).unsqueeze(1)
        # Store for potential meta-learning
        self.last_plasticity = plasticity
        
        if return_state:
            return modulated, arousal_probs
        return modulated
```

### 4. Predictive Processing Attention

```python
class PredictiveProcessingAttention(nn.Module):
    """
    Attention based on predictive processing/free energy principle.
    
    Attention is directed to minimize prediction error,
    similar to how the brain processes sensory input.
    """
    
    def __init__(self, dim, num_levels=3, precision_learning=True):
        super().__init__()
        self.dim = dim
        self.num_levels = num_levels
        self.precision_learning = precision_learning
        
        # Hierarchical prediction levels
        self.predictors = nn.ModuleList([
            nn.Linear(dim, dim) for _ in range(num_levels)
        ])
        
        # Precision (inverse variance) for each level
        self.precision = nn.ParameterList([
            nn.Parameter(torch.ones(dim)) for _ in range(num_levels)
        ])
        
        # Prediction error projection
        self.error_proj = nn.ModuleList([
            nn.Linear(dim * 2, dim) for _ in range(num_levels)
        ])
        
        # Top-down priors
        self.prior_proj = nn.Linear(dim, dim)
        
    def forward(self, x, prior=None):
        """
        Process input through hierarchical predictive coding.
        
        Args:
            x: Sensory input (batch, seq, dim)
            prior: Top-down prior (batch, dim)
        
        Returns:
            posterior: Updated beliefs
            total_error: Prediction error (for loss)
        """
        batch, seq_len, _ = x.shape
        
        # Initialize prior if not provided
        if prior is None:
            prior = torch.zeros(batch, self.dim, device=x.device)
        
        total_error = 0
        current = x.mean(dim=1)  # Aggregate input
        
        # Hierarchical predictive processing
        for level in range(self.num_levels):
            # Generate prediction
            prediction = self.predictors[level](prior)
            
            # Compute prediction error
            error = current - prediction
            weighted_error = error * torch.sigmoid(self.precision[level])
            
            # Update beliefs (posterior)
            posterior_input = torch.cat([current, weighted_error], dim=-1)
            posterior = self.error_proj[level](posterior_input)
            
            # Update prior for next level
            prior = posterior
            current = posterior
            
            # Accumulate weighted error
            total_error = total_error + (error ** 2).mean()
        
        # Expand back to sequence
        output = posterior.unsqueeze(1).expand(-1, seq_len, -1)
        
        return output, total_error
    
    def free_energy_loss(self, x, target):
        """
        Compute variational free energy (prediction error + KL divergence).
        """
        output, prediction_error = self.forward(x)
        
        # Reconstruction loss (accuracy term)
        recon_loss = F.mse_loss(output, target)
        
        # Complexity term (regularization)
        complexity = sum(p.abs().mean() for p in self.precision)
        
        # Free energy
        free_energy = recon_loss + prediction_error + 0.01 * complexity
        
        return free_energy
```

## Integrated Brain-Inspired Attention Block

```python
class BrainInspiredAttentionBlock(nn.Module):
    """
    Comprehensive attention block integrating multiple brain-inspired mechanisms.
    """
    
    def __init__(self, dim, num_heads=8, num_areas=4):
        super().__init__()
        
        # Layer normalization
        self.norm1 = nn.LayerNorm(dim)
        self.norm2 = nn.LayerNorm(dim)
        self.norm3 = nn.LayerNorm(dim)
        
        # Brain-inspired attention components
        self.thalamic_attn = ThalamicGatingAttention(dim, num_heads)
        self.pulvinar_sync = PulvinarSynchronizationAttention(dim, num_areas)
        self.basal_forebrain = BasalForebrainModulatedAttention(dim)
        self.predictive = PredictiveProcessingAttention(dim)
        
        # Feedforward
        self.ffn = nn.Sequential(
            nn.Linear(dim, dim * 4),
            nn.GELU(),
            nn.Dropout(0.1),
            nn.Linear(dim * 4, dim),
            nn.Dropout(0.1)
        )
        
        # Integration weights (learnable)
        self.integration_weights = nn.Parameter(torch.ones(4))
        
    def forward(self, x, return_components=False):
        """
        Apply brain-inspired attention mechanisms.
        
        Args:
            x: (batch, seq, dim)
        
        Returns:
            output: (batch, seq, dim)
        """
        # Normalize
        x_norm = self.norm1(x)
        
        # Apply attention mechanisms
        thalamic_out = self.thalamic_attn(x_norm)
        pulvinar_out = self.pulvinar_sync(x_norm)
        basal_out = self.basal_forebrain(x_norm)
        pred_out, pred_error = self.predictive(x_norm)
        
        # Weighted integration
        weights = F.softmax(self.integration_weights, dim=0)
        
        integrated = (
            weights[0] * thalamic_out +
            weights[1] * pulvinar_out +
            weights[2] * basal_out +
            weights[3] * pred_out
        )
        
        # Residual
        x = x + integrated
        
        # Feedforward
        x = x + self.ffn(self.norm3(x))
        
        if return_components:
            return x, {
                'thalamic': thalamic_out,
                'pulvinar': pulvinar_out,
                'basal': basal_out,
                'predictive': pred_out,
                'prediction_error': pred_error,
                'weights': weights
            }
        
        return x
```

## Vision-Specific: Saliency-Based Attention

```python
class BiologicalSaliencyAttention(nn.Module):
    """
    Saliency-based attention inspired by visual cortex and superior colliculus.
    
    Combines:
    - Bottom-up saliency (unusual features)
    - Top-down goal modulation
    - Inhibition of return
    """
    
    def __init__(self, dim, spatial_size=(14, 14)):
        super().__init__()
        self.dim = dim
        self.H, self.W = spatial_size
        
        # Bottom-up saliency (V1-like features)
        self.saliency_net = nn.Sequential(
            nn.Conv2d(dim, dim // 2, 3, padding=1),
            nn.ReLU(),
            nn.Conv2d(dim // 2, dim // 4, 3, padding=1),
            nn.ReLU(),
            nn.Conv2d(dim // 4, 1, 1)
        )
        
        # Center-surround (on-center/off-surround)
        self.center_surround = nn.Conv2d(1, 1, 5, padding=2, bias=False)
        # Initialize with difference-of-Gaussians
        with torch.no_grad():
            self.center_surround.weight.data = self._create_dog_kernel()
        
        # Top-down goal modulation
        self.goal_proj = nn.Linear(dim, self.H * self.W)
        
        # Inhibition of return (IOR)
        self.register_buffer('ior_mask', torch.ones(1, 1, self.H, self.W))
        self.ior_decay = 0.9
        
    def _create_dog_kernel(self):
        """Create Difference-of-Gaussians kernel."""
        x = torch.arange(5).float() - 2
        xx, yy = torch.meshgrid(x, x, indexing='ij')
        
        # Center (narrow Gaussian)
        center = torch.exp(-(xx**2 + yy**2) / (2 * 0.5**2))
        # Surround (wide Gaussian)
        surround = torch.exp(-(xx**2 + yy**2) / (2 * 1.5**2))
        
        dog = center - 0.5 * surround
        return dog.unsqueeze(0).unsqueeze(0)
    
    def forward(self, x, goal=None):
        """
        Args:
            x: (batch, dim, H, W) feature map
            goal: (batch, dim) goal embedding for top-down modulation
        
        Returns:
            attended: (batch, dim, H, W)
            saliency_map: (batch, H, W)
        """
        batch = x.shape[0]
        
        # Bottom-up saliency
        saliency = self.saliency_net(x)  # (batch, 1, H, W)
        saliency = torch.sigmoid(saliency)
        
        # Apply center-surround
        saliency = self.center_surround(saliency)
        saliency = F.relu(saliency)
        
        # Top-down goal modulation
        if goal is not None:
            goal_map = self.goal_proj(goal).view(batch, 1, self.H, self.W)
            saliency = saliency + torch.sigmoid(goal_map)
        
        # Apply inhibition of return
        saliency = saliency * self.ior_mask
        
        # Normalize
        saliency_flat = saliency.view(batch, -1)
        saliency_flat = F.softmax(saliency_flat, dim=-1)
        saliency = saliency_flat.view(batch, 1, self.H, self.W)
        
        # Update IOR mask (inhibit attended location)
        with torch.no_grad():
            self.ior_mask = self.ior_mask * self.ior_decay + (1 - saliency) * (1 - self.ior_decay)
        
        # Apply attention
        attended = x * saliency
        
        return attended, saliency.squeeze(1)
```

## Training with Attention Monitoring

```python
class BrainInspiredAttentionTrainer:
    """
    Training framework with attention monitoring and regularization.
    """
    
    def __init__(self, model, optimizer, lambda_arousal=0.01, lambda_diversity=0.1):
        self.model = model
        self.optimizer = optimizer
        self.lambda_arousal = lambda_arousal
        self.lambda_diversity = lambda_diversity
        
    def train_step(self, x, y):
        """Training step with brain-inspired regularization."""
        self.optimizer.zero_grad()
        
        # Forward with component tracking
        if hasattr(self.model, 'return_components'):
            output, components = self.model(x, return_components=True)
        else:
            output = self.model(x)
            components = {}
        
        # Task loss
        task_loss = F.cross_entropy(output, y)
        
        # Arousal regularization (prefer medium arousal)
        if 'arousal' in components:
            # Penalize extreme arousal states
            arousal = components['arousal']
            target_arousal = torch.tensor([0.1, 0.8, 0.1], device=arousal.device)
            arousal_loss = F.kl_div(arousal.log(), target_arousal.expand_as(arousal))
        else:
            arousal_loss = 0
        
        # Prediction error regularization
        if 'prediction_error' in components:
            pred_error = components['prediction_error']
            pred_loss = pred_error * self.lambda_arousal
        else:
            pred_loss = 0
        
        # Total loss
        total_loss = task_loss + self.lambda_arousal * arousal_loss + pred_loss
        
        total_loss.backward()
        self.optimizer.step()
        
        return {
            'task_loss': task_loss.item(),
            'total_loss': total_loss.item(),
            'accuracy': (output.argmax(dim=1) == y).float().mean().item()
        }
```

## References

1. Halassa, M. M., & Kastner, S. (2017). Thalamic functions in distributed cognitive control. Nature Neuroscience.
2. Saalmann, Y. B., & Kastner, S. (2011). Cognitive and perceptual functions of the visual thalamus. Neuron.
3. Friston, K. (2010). The free-energy principle: a unified brain theory? Nature Reviews Neuroscience.
4. Buschman, T. J., & Miller, E. K. (2007). Top-down versus bottom-up control of attention in the prefrontal and posterior parietal cortices. Science.
5. Itti, L., & Koch, C. (2001). Computational modelling of visual attention. Nature Reviews Neuroscience.
6. Shipp, S. (2003). The functional logic of cortico-pulvinar connections. Philosophical Transactions of the Royal Society.

## Activation Keywords

- brain attention
- thalamic attention
- pulvinar synchronization
- basal forebrain modulation
- predictive processing attention
- biological attention
- neuromorphic attention
- saliency attention
- cortico-thalamic attention
- free energy attention

## Tools Used

- `read` - Read research papers and implementation guides
- `write` - Save attention mechanism implementations and configuration files
- `exec` - Run Python scripts for training brain-inspired attention models

## Instructions for Agents

Follow these steps when helping users implement brain-inspired attention:

1. **Identify the attention type**: Determine which biological attention mechanism is most relevant (thalamic gating, pulvinar synchronization, basal forebrain modulation, or predictive processing)
2. **Select the implementation**: Use the corresponding code from this skill
3. **Integrate with the user's model**: Adapt the attention block to their architecture
4. **Validate**: Run training with the new attention mechanism and compare against baseline

## Examples

### Example 1: Thalamic Gating Attention

```
User: "实现基于丘脑门控的注意力机制"

Execute:
1. Explain the thalamocortical gating concept
2. Provide the ThalamicGatingAttention implementation
3. Show how to integrate into a vision model
4. Demonstrate training with attention monitoring
```

### Example 2: Predictive Processing Attention

```
User: "How to implement predictive processing attention?"

Execute:
1. Explain the free-energy principle basis
2. Provide the PredictiveProcessingAttention implementation
3. Show the prediction error computation
4. Demonstrate integration with the user's model
```
