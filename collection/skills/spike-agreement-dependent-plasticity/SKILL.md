---
name: spike-agreement-dependent-plasticity
description: "Spike Agreement Dependent Plasticity (SADP) - biologically inspired learning rule for SNNs using population-level correlation metrics instead of precise spike timing. Activation triggers: spike agreement, synaptic plasticity, SNN learning, bio-inspired learning, population correlation, neuromorphic learning."
---

# Spike Agreement Dependent Plasticity (SADP)

> Biologically inspired synaptic learning rule for Spiking Neural Networks that relies on the agreement between pre- and post-synaptic spike trains rather than precise spike-pair timing, achieving superior performance with linear-time complexity.

## Metadata
- **Source**: arXiv:2508.16216 [cs.NE]
- **Authors**: Saptarshi Bej, Muhammed Sahad E, Gouri Lakshmi, Harshit Kumar, Pritam Kar, Bikas C Das
- **Published**: 2025-08-22
- **Categories**: cs.NE (Neural and Evolutionary Computing), cs.LG (Machine Learning)

## Core Methodology

### Key Innovation
Traditional STDP (Spike-Timing-Dependent Plasticity) relies on precise temporal correlations between individual pre- and post-synaptic spikes, which is computationally expensive and hardware-unfriendly. SADP generalizes STDP by:
- **Replacing pairwise timing** with **population-level correlation metrics**
- Using **Cohen's kappa** and other agreement statistics
- Achieving **linear-time complexity** $O(n)$ vs STDP's $O(n^2)$
- Enabling **hardware-efficient implementation** via bitwise logic

### Technical Framework

#### 1. Spike Train Representation
Instead of tracking individual spike times, SADP operates on spike train agreement:
- **Binary representation**: Spike trains as binary vectors
- **Population view**: Aggregated statistics over time windows
- **Agreement metric**: Statistical agreement between pre and post populations

#### 2. Cohen's Kappa as Plasticity Signal
$$\kappa = \frac{p_o - p_e}{1 - p_e}$$

Where:
- $p_o$: Observed agreement between spike trains
- $p_e$: Expected agreement (chance level)
- $\kappa \in [-1, 1]$: Agreement strength

#### 3. SADP Update Rule
$$\Delta w_{ij} = \eta \cdot \kappa(x_i, x_j) \cdot \text{spline}_w(t)$$

Where:
- $\eta$: Learning rate
- $\kappa(x_i, x_j)$: Agreement between pre ($x_i$) and post ($x_j$) spike trains
- $\text{spline}_w(t)$: Time-windowed spline kernel

#### 4. Spline-Based Kernels
- Derived from experimental iontronic organic memtransistor device data
- Captures temporal dependencies without precise timing
- Hardware-friendly continuous approximation

## Implementation Guide

### Prerequisites
- Python 3.8+
- PyTorch or TensorFlow
- NumPy, SciPy
- Optional: Brian2 or other SNN framework

### Step-by-Step Implementation

```python
import numpy as np
import torch
import torch.nn as nn
from typing import Tuple, Optional

class SADPLearner:
    """
    Spike Agreement Dependent Plasticity for SNN training
    """
    def __init__(
        self,
        learning_rate: float = 0.01,
        time_window: int = 20,  # ms
        kernel_type: str = 'spline',
        device: str = 'cpu'
    ):
        self.learning_rate = learning_rate
        self.time_window = time_window
        self.kernel_type = kernel_type
        self.device = device
        
        # Pre-compute spline kernel
        self.kernel = self._create_spline_kernel(time_window)
    
    def _create_spline_kernel(self, window_size: int) -> torch.Tensor:
        """
        Create spline-based temporal kernel from memtransistor data
        
        Args:
            window_size: Temporal window size in time steps
        
        Returns:
            kernel: [window_size] spline kernel weights
        """
        # Simplified spline kernel - in practice, load from experimental data
        # The paper uses kernels derived from iontronic organic memtransistors
        t = torch.linspace(0, 1, window_size)
        
        # B-spline approximation (simplified)
        kernel = torch.sin(np.pi * t) * torch.exp(-2 * t)
        kernel = kernel / kernel.sum()
        
        return kernel
    
    def compute_spike_agreement(
        self,
        pre_spikes: torch.Tensor,
        post_spikes: torch.Tensor
    ) -> torch.Tensor:
        """
        Compute Cohen's kappa agreement between pre and post spike trains
        
        Args:
            pre_spikes: [num_pre, time_steps] binary spike trains
            post_spikes: [num_post, time_steps] binary spike trains
        
        Returns:
            agreement: [num_pre, num_post] agreement matrix
        """
        num_pre, T = pre_spikes.shape
        num_post = post_spikes.shape[0]
        
        # Compute observed agreement for each time step
        # For each pre-post pair, compute agreement over time
        agreement = torch.zeros(num_pre, num_post, device=self.device)
        
        for t in range(T):
            pre_t = pre_spikes[:, t].unsqueeze(1)  # [num_pre, 1]
            post_t = post_spikes[:, t].unsqueeze(0)  # [1, num_post]
            
            # Agreement: both spiked or both didn't spike
            agreement_t = (pre_t == post_t).float()
            
            # Weight by kernel
            if t < len(self.kernel):
                agreement += agreement_t * self.kernel[t]
        
        # Normalize by total weight
        agreement = agreement / self.kernel.sum()
        
        # Convert to Cohen's kappa
        # Observed agreement
        p_o = agreement
        
        # Expected agreement (chance level)
        pre_rate = pre_spikes.float().mean(dim=1, keepdim=True)  # [num_pre, 1]
        post_rate = post_spikes.float().mean(dim=0, keepdim=True)  # [1, num_post]
        p_e = pre_rate * post_rate + (1 - pre_rate) * (1 - post_rate)
        
        # Cohen's kappa
        kappa = (p_o - p_e) / (1 - p_e + 1e-8)
        
        return kappa
    
    def update_weights(
        self,
        weights: torch.Tensor,
        pre_spikes: torch.Tensor,
        post_spikes: torch.Tensor,
        spike_times: Optional[torch.Tensor] = None
    ) -> torch.Tensor:
        """
        Update synaptic weights using SADP
        
        Args:
            weights: [num_pre, num_post] current weights
            pre_spikes: [num_pre, time_steps] pre-synaptic spikes
            post_spikes: [num_post, time_steps] post-synaptic spikes
            spike_times: optional actual spike times for timing information
        
        Returns:
            delta_w: [num_pre, num_post] weight updates
        """
        # Compute agreement
        kappa = self.compute_spike_agreement(pre_spikes, post_spikes)
        
        # SADP update rule
        delta_w = self.learning_rate * kappa
        
        # Optional: time-dependent modulation
        if spike_times is not None:
            # Apply temporal kernel to weight updates
            time_weights = self._apply_temporal_kernel(spike_times)
            delta_w = delta_w * time_weights
        
        # Clip updates
        delta_w = torch.clamp(delta_w, -0.1, 0.1)
        
        return delta_w
    
    def _apply_temporal_kernel(self, spike_times: torch.Tensor) -> torch.Tensor:
        """
        Apply temporal kernel based on spike timing
        
        Args:
            spike_times: [num_pre, num_post] spike time differences
        
        Returns:
            time_weights: [num_pre, num_post] temporal modulation
        """
        # Simplified - in practice use actual spline kernel from paper
        time_weights = torch.exp(-torch.abs(spike_times) / self.time_window)
        return time_weights


class SADPLayer(nn.Module):
    """
    SNN layer with SADP learning
    """
    def __init__(
        self,
        in_features: int,
        out_features: int,
        time_steps: int = 100,
        threshold: float = 1.0,
        tau_mem: float = 20.0,  # membrane time constant
        **sadp_kwargs
    ):
        super().__init__()
        
        self.in_features = in_features
        self.out_features = out_features
        self.time_steps = time_steps
        self.threshold = threshold
        self.tau_mem = tau_mem
        
        # Synaptic weights
        self.weight = nn.Parameter(torch.randn(out_features, in_features) * 0.1)
        
        # SADP learner
        self.sadp = SADPLearner(**sadp_kwargs)
        
        # State variables
        self.reset_state()
    
    def reset_state(self):
        """Reset membrane potentials and spike history"""
        self.mem = None
        self.pre_spike_history = []
        self.post_spike_history = []
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Forward pass with spike recording
        
        Args:
            x: [batch, time_steps, in_features] input spikes
        
        Returns:
            spikes: [batch, time_steps, out_features] output spikes
        """
        batch_size = x.size(0)
        
        if self.mem is None:
            self.mem = torch.zeros(batch_size, self.out_features, device=x.device)
        
        output_spikes = []
        
        for t in range(self.time_steps):
            # Current input
            x_t = x[:, t, :]  # [batch, in_features]
            
            # Synaptic current
            current = torch.matmul(x_t, self.weight.t())  # [batch, out_features]
            
            # Leaky integrate
            self.mem = self.mem * np.exp(-1 / self.tau_mem) + current
            
            # Spike generation
            spike = (self.mem >= self.threshold).float()
            self.mem = self.mem * (1 - spike)  # Reset
            
            output_spikes.append(spike)
            
            # Record for SADP
            if self.training:
                # Aggregate over batch for learning
                self.pre_spike_history.append(x_t.mean(dim=0))
                self.post_spike_history.append(spike.mean(dim=0))
        
        return torch.stack(output_spikes, dim=1)
    
    def learn(self):
        """
        Perform SADP weight update after forward pass
        """
        if len(self.pre_spike_history) == 0:
            return
        
        # Convert to tensors
        pre_spikes = torch.stack(self.pre_spike_history, dim=1)  # [in_features, time]
        post_spikes = torch.stack(self.post_spike_history, dim=1)  # [out_features, time]
        
        # Compute weight updates for each output neuron
        for j in range(self.out_features):
            post_j = post_spikes[j:j+1]  # [1, time]
            
            # Compute agreement with all pre-synaptic neurons
            kappa = self.sadp.compute_spike_agreement(
                pre_spikes.t(),  # [time, in_features]
                post_j.t().expand(pre_spikes.size(1), -1).t()  # [in_features, time]
            )
            
            # Update weights
            self.weight.data[j] += self.sadp.learning_rate * kappa[0]
        
        # Clear history
        self.pre_spike_history = []
        self.post_spike_history = []


# Hardware-friendly bitwise implementation
class SADPHardware:
    """
    Hardware-efficient SADP using bitwise operations
    """
    @staticmethod
    def compute_agreement_bitwise(pre_spikes: np.ndarray, post_spikes: np.ndarray) -> float:
        """
        Compute spike agreement using bitwise XOR (fast on neuromorphic hardware)
        
        Args:
            pre_spikes: [time] binary array
            post_spikes: [time] binary array
        
        Returns:
            kappa: agreement score
        """
        # XOR gives disagreement
        disagreement = np.bitwise_xor(pre_spikes.astype(np.uint8), 
                                       post_spikes.astype(np.uint8))
        
        # Agreement = 1 - disagreement_rate
        p_o = 1.0 - np.mean(disagreement)
        
        # Expected agreement
        p_pre = np.mean(pre_spikes)
        p_post = np.mean(post_spikes)
        p_e = p_pre * p_post + (1 - p_pre) * (1 - p_post)
        
        # Cohen's kappa
        kappa = (p_o - p_e) / (1 - p_e + 1e-8)
        
        return kappa
```

### Training Loop

```python
def train_sadp_snn(
    model: SADPLayer,
    train_loader,
    epochs: int = 10,
    device: str = 'cpu'
):
    """
    Train SNN with SADP
    
    Args:
        model: SADP-enabled SNN layer
        train_loader: DataLoader with (input_spikes, labels)
        epochs: Number of training epochs
        device: 'cpu' or 'cuda'
    """
    model.to(device)
    
    for epoch in range(epochs):
        total_correct = 0
        total_samples = 0
        
        for batch_idx, (data, target) in enumerate(train_loader):
            data, target = data.to(device), target.to(device)
            
            # Forward pass
            model.reset_state()
            output = model(data)
            
            # SADP learning
            model.learn()
            
            # Classification (using readout layer)
            # Simplified - actual implementation would use rate coding
            spike_count = output.sum(dim=1)  # [batch, out_features]
            predicted = spike_count.argmax(dim=1)
            
            total_correct += (predicted == target).sum().item()
            total_samples += target.size(0)
            
            if batch_idx % 100 == 0:
                acc = 100. * total_correct / total_samples
                print(f'Epoch {epoch}, Batch {batch_idx}, Acc: {acc:.2f}%')
        
        print(f'Epoch {epoch} complete, Accuracy: {100. * total_correct / total_samples:.2f}%')
```

## Applications

### 1. Pattern Recognition
- **MNIST Classification**: High accuracy with minimal time steps
- **Fashion-MNIST**: Robust to image variations
- **Spoken Digit Recognition**: Audio processing with spikes

### 2. Neuromorphic Hardware
- **Intel Loihi**: Efficient on-chip learning
- **IBM TrueNorth**: Massive parallel processing
- **Custom ASICs**: Low-power edge devices
- **Memristive Crossbars**: In-memory computation

### 3. Edge AI
- **Real-time Processing**: Low latency inference
- **Ultra-low Power**: Event-driven computation
- **Always-on Sensors**: Battery-powered devices

### 4. Brain-Machine Interfaces
- **Neural Decoding**: Learn from biological spikes
- **Adaptive Control**: Online learning
- **Long-term Stability**: Reduced weight drift

## Pitfalls

1. **Hyperparameter Sensitivity**: Time window and kernel parameters matter
   - *Mitigation*: Cross-validation, grid search, or meta-learning

2. **Hardware Variability**: Memtransistor characteristics vary
   - *Mitigation*: Device-specific kernel calibration, robust training

3. **Sparse Activity**: Very sparse spikes can lead to zero gradients
   - *Mitigation*: Activity regularization, minimum spike rate constraints

4. **Scaling Challenges**: Large networks need careful initialization
   - *Mitigation*: Layer-wise pre-training, weight normalization

5. **Binary vs Analog**: Pure binary spikes lose timing precision
   - *Mitigation*: Multi-bit spike encoding, temporal binning

## Related Skills
- stdp-learning: Traditional spike-timing-dependent plasticity
- snn-training: General SNN training methods
- neuromorphic-computing: Hardware implementations
- memristor-snn: Memristor-based SNN learning

## References
```bibtex
@article{bej2025sadp,
  title={Spike Agreement Dependent Plasticity: A scalable Bio-Inspired learning paradigm for Spiking Neural Networks},
  author={Bej, Saptarshi and E, Muhammed Sahad and Lakshmi, Gouri and Kumar, Harshit and Kar, Pritam and Das, Bikas C},
  journal={arXiv preprint arXiv:2508.16216},
  year={2025}
}
```

## Further Reading
- STDP: Bi & Poo, "Synaptic modification by correlated activity"
- Neuromorphic Hardware: Davies et al., "Loihi: A Neuromorphic Manycore Processor"
- Memtransistors: Yang et al., "Memristive Devices for Computation"
- Spline Kernels: de Boor, "A Practical Guide to Splines"
