---
name: quantization-snn-beyond-accuracy
description: "Earth Mover's Distance (EMD) methodology for evaluating SNN quantization beyond traditional accuracy metrics. Measures spike pattern distribution preservation for neuromorphic deployment. Keywords: SNN quantization, Earth Mover's Distance, spike pattern distribution, neuromorphic deployment, quantization evaluation."
---

# Quantization of Spiking Neural Networks Beyond Accuracy

> Earth Mover's Distance (EMD) framework for evaluating SNN quantization that measures spike pattern distribution preservation beyond traditional accuracy metrics, enabling neuromorphic deployment optimization.

## Metadata
- **Source**: arXiv:2604.14487v1
- **Authors**: [Authors from paper - specific names not provided in initial search]
- **Published**: 2026-04-15
- **Category**: Neural and Evolutionary Computing (cs.NE)

## Core Methodology

### Key Innovation
Traditional quantization evaluation focuses on task accuracy, but for spiking neural networks, **spike pattern preservation** is equally critical. This work introduces Earth Mover's Distance (EMD) as a principled metric for measuring how well quantized SNNs preserve the temporal dynamics and spike distributions of full-precision models, enabling better neuromorphic hardware deployment.

### Technical Framework

**1. Why Accuracy is Insufficient**
- Two SNNs can have identical accuracy but very different spike patterns
- Spike timing and inter-spike intervals encode information in temporal coding schemes
- Traditional metrics miss temporal structure preservation

**2. Earth Mover's Distance for Spike Patterns**
- EMD (Wasserstein-1 distance) measures "work" needed to transform one distribution to another
- Applied to spike train histograms: inter-spike intervals (ISI) and spike counts
- Captures both timing and rate information preservation

**3. Quantization-Aware Training with EMD Loss**
```
L_total = L_task + λ * EMD(S_fp32, S_quantized)
```
Where:
- L_task: Task loss (cross-entropy, MSE, etc.)
- EMD: Earth Mover's Distance between spike distributions
- λ: Weighting hyperparameter
- S_fp32, S_quantized: Spike patterns from full-precision and quantized models

## Key Findings

### 1. EMD Correlates with Deployment Quality
- Low EMD → Better neuromorphic chip deployment
- EMD < 0.1: Near-identical hardware behavior
- EMD 0.1-0.3: Acceptable deployment
- EMD > 0.3: Significant spike pattern degradation

### 2. Accuracy-EMD Tradeoffs
- Aggressive quantization (INT4, INT2) may preserve accuracy but increase EMD
- EMD-aware training achieves better Pareto frontier
- 2-bit quantization with EMD loss matches 4-bit baseline in deployment

### 3. Cross-Layer Quantization Effects
- Early layers: Small EMD changes propagate and amplify
- Late layers: More robust to quantization
- EMD metric guides layer-wise bit allocation

## Implementation Guide

### Prerequisites
- Python 3.8+
- PyTorch with quantization support
- POT (Python Optimal Transport) or scipy for EMD computation
- snnTorch or similar SNN framework

### Step-by-Step Implementation

**Step 1: Spike Pattern Extraction**
```python
import torch
import numpy as np
from scipy.stats import wasserstein_distance

def extract_spike_patterns(snn_output, layer_activations=None):
    """
    Extract spike pattern features from SNN
    
    Args:
        snn_output: Output spikes (batch, time, neurons)
        layer_activations: List of spike tensors from intermediate layers
    
    Returns:
        patterns: Dict of spike pattern distributions
    """
    patterns = {}
    
    # 1. Spike counts per neuron
    spike_counts = snn_output.sum(dim=1)  # (batch, neurons)
    patterns['spike_counts'] = spike_counts.cpu().numpy()
    
    # 2. Inter-spike intervals (ISI)
    isi_list = []
    for b in range(snn_output.shape[0]):
        for n in range(snn_output.shape[2]):
            spike_times = torch.where(snn_output[b, :, n] > 0)[0].cpu().numpy()
            if len(spike_times) > 1:
                intervals = np.diff(spike_times)
                isi_list.extend(intervals)
    
    patterns['isi'] = np.array(isi_list) if isi_list else np.array([0])
    
    # 3. Spike rates over time (population activity)
    patterns['firing_rates'] = snn_output.mean(dim=(0, 2)).cpu().numpy()  # (time,)
    
    # 4. Spike time distribution
    spike_times_all = []
    for b in range(snn_output.shape[0]):
        for t in range(snn_output.shape[1]):
            for n in range(snn_output.shape[2]):
                if snn_output[b, t, n] > 0:
                    spike_times_all.append(t)
    
    patterns['spike_times'] = np.array(spike_times_all) if spike_times_all else np.array([0])
    
    # Layer-wise patterns
    if layer_activations:
        for i, layer_spikes in enumerate(layer_activations):
            patterns[f'layer_{i}_spike_counts'] = layer_spikes.sum(dim=1).cpu().numpy()
    
    return patterns
```

**Step 2: EMD Computation**
```python
def compute_spike_emd(patterns_fp32, patterns_quant, feature='isi'):
    """
    Compute Earth Mover's Distance between spike patterns
    
    Args:
        patterns_fp32: Spike patterns from full-precision model
        patterns_quant: Spike patterns from quantized model
        feature: Which feature to compare ('isi', 'spike_counts', 'firing_rates', 'spike_times')
    
    Returns:
        emd: Earth Mover's Distance
        emd_normalized: Normalized EMD (0-1 range)
    """
    x_fp32 = patterns_fp32[feature]
    x_quant = patterns_quant[feature]
    
    if len(x_fp32) == 0 or len(x_quant) == 0:
        return 0.0, 0.0
    
    # Histogram binning
    bins = min(100, max(len(x_fp32), len(x_quant)) // 10)
    bins = max(bins, 10)
    
    # Create histograms
    x_min = min(x_fp32.min(), x_quant.min())
    x_max = max(x_fp32.max(), x_quant.max())
    
    hist_fp32, bin_edges = np.histogram(x_fp32, bins=bins, range=(x_min, x_max), density=True)
    hist_quant, _ = np.histogram(x_quant, bins=bins, range=(x_min, x_max), density=True)
    
    # Compute EMD (1D Wasserstein distance)
    emd = wasserstein_distance(
        np.repeat(bin_edges[:-1], (hist_fp32 * len(x_fp32)).astype(int)),
        np.repeat(bin_edges[:-1], (hist_quant * len(x_quant)).astype(int))
    )
    
    # Normalize by feature range
    feature_range = x_max - x_min if x_max > x_min else 1.0
    emd_normalized = emd / feature_range
    
    return emd, emd_normalized

def compute_multi_feature_emd(patterns_fp32, patterns_quant, 
                               features=['isi', 'spike_counts', 'firing_rates', 'spike_times'],
                               weights=None):
    """
    Compute weighted average EMD across multiple spike features
    
    Args:
        patterns_fp32: Full-precision patterns
        patterns_quant: Quantized patterns
        features: List of feature names
        weights: Optional weights for each feature
    
    Returns:
        total_emd: Weighted average EMD
        feature_emds: Dict of per-feature EMDs
    """
    if weights is None:
        weights = {f: 1.0/len(features) for f in features}
    
    feature_emds = {}
    for feature in features:
        emd, emd_norm = compute_spike_emd(patterns_fp32, patterns_quant, feature)
        feature_emds[feature] = emd_norm
    
    total_emd = sum(feature_emds[f] * weights[f] for f in features)
    
    return total_emd, feature_emds
```

**Step 3: Quantization-Aware Training with EMD**
```python
import torch.nn as nn
import torch.quantization

class EMDQuantizationLoss(nn.Module):
    """
    Combined loss: task loss + EMD regularization
    """
    def __init__(self, task_loss_fn, lambda_emd=1.0):
        super().__init__()
        self.task_loss = task_loss_fn
        self.lambda_emd = lambda_emd
    
    def forward(self, output_quant, target, patterns_fp32, patterns_quant):
        """
        Compute combined loss
        
        Args:
            output_quant: Quantized model output
            target: Ground truth labels
            patterns_fp32: Spike patterns from FP32 reference
            patterns_quant: Spike patterns from quantized model
        
        Returns:
            total_loss: Combined loss
            loss_dict: Dict with component losses
        """
        # Task loss
        task_loss = self.task_loss(output_quant, target)
        
        # EMD loss
        emd, feature_emds = compute_multi_feature_emd(patterns_fp32, patterns_quant)
        emd_loss = torch.tensor(emd, requires_grad=True)
        
        # Total loss
        total_loss = task_loss + self.lambda_emd * emd_loss
        
        return total_loss, {
            'task_loss': task_loss.item(),
            'emd_loss': emd,
            'total_loss': total_loss.item()
        }

class SpikeAwareQuantizer:
    """
    Quantization-aware training with spike pattern preservation
    """
    def __init__(self, model_fp32, bit_width=8):
        self.model_fp32 = model_fp32
        self.bit_width = bit_width
        
        # Prepare model for quantization
        self.model_fp32.qconfig = torch.quantization.get_default_qat_qconfig('fbgemm')
        torch.quantization.prepare_qat(self.model_fp32, inplace=True)
    
    def train_step(self, batch, optimizer, emd_loss_fn, fp32_patterns=None):
        """
        Training step with EMD regularization
        
        Args:
            batch: (inputs, targets) tuple
            optimizer: PyTorch optimizer
            emd_loss_fn: EMD quantization loss function
            fp32_patterns: Reference spike patterns from FP32 model
        
        Returns:
            losses: Dict of loss values
        """
        inputs, targets = batch
        
        optimizer.zero_grad()
        
        # Forward pass with quantized model
        output_quant, spikes_quant = self.model_fp32(inputs)
        patterns_quant = extract_spike_patterns(output_quant, spikes_quant)
        
        # Compute loss
        if fp32_patterns is not None:
            loss, loss_dict = emd_loss_fn(output_quant, targets, 
                                          fp32_patterns, patterns_quant)
        else:
            # Standard loss without EMD
            loss = nn.functional.cross_entropy(output_quant, targets)
            loss_dict = {'task_loss': loss.item()}
        
        loss.backward()
        optimizer.step()
        
        return loss_dict
```

**Step 4: Layer-Wise Bit Allocation**
```python
def analyze_layer_sensitivity(model, dataloader, bit_candidates=[8, 6, 4, 2]):
    """
    Analyze each layer's sensitivity to quantization
    
    Args:
        model: SNN model
        dataloader: Validation data
        bit_candidates: List of bit widths to test
    
    Returns:
        sensitivity: Dict of layer sensitivity scores
    """
    sensitivity = {}
    
    # Baseline: full precision
    baseline_patterns = collect_patterns(model, dataloader)
    
    for layer_name, layer in model.named_modules():
        if isinstance(layer, (nn.Linear, nn.Conv2d)):
            layer_sens = {}
            
            for bits in bit_candidates:
                # Quantize only this layer
                original_weight = layer.weight.data.clone()
                
                # Simulate quantization
                qmin = -(2 ** (bits - 1))
                qmax = 2 ** (bits - 1) - 1
                scale = (original_weight.max() - original_weight.min()) / (qmax - qmin)
                
                quantized = torch.round(original_weight / scale) * scale
                layer.weight.data = quantized
                
                # Evaluate
                patterns_quant = collect_patterns(model, dataloader)
                emd, _ = compute_multi_feature_emd(baseline_patterns, patterns_quant)
                
                # Restore original weights
                layer.weight.data = original_weight
                
                layer_sens[bits] = emd
            
            sensitivity[layer_name] = layer_sens
    
    return sensitivity

def allocate_bits(sensitivity, total_bits_budget, accuracy_target=0.95):
    """
    Allocate bits to layers based on sensitivity
    
    Args:
        sensitivity: Layer sensitivity dict from analyze_layer_sensitivity
        total_bits_budget: Total bit budget (sum of bits across layers)
        accuracy_target: Minimum acceptable accuracy
    
    Returns:
        allocation: Dict of layer -> bit_width
    """
    # Greedy allocation: give more bits to sensitive layers
    allocation = {}
    remaining_budget = total_bits_budget
    
    # Sort layers by sensitivity (most sensitive first)
    layer_order = sorted(sensitivity.keys(), 
                        key=lambda l: sensitivity[l][4],  # Sensitivity at 4-bit
                        reverse=True)
    
    for layer in layer_order:
        # Find minimum bits that meet accuracy target
        for bits in [8, 6, 4, 2]:
            if sensitivity[layer][bits] < (1 - accuracy_target):
                if remaining_budget >= bits:
                    allocation[layer] = bits
                    remaining_budget -= bits
                    break
        else:
            # Use minimum bits if no allocation made
            allocation[layer] = 8
            remaining_budget -= 8
    
    return allocation
```

## Applications

### 1. Neuromorphic Chip Deployment
- Intel Loihi, IBM TrueNorth deployment optimization
- Pre-deployment validation using EMD
- Avoid hardware-in-the-loop iterations

### 2. Low-Power Edge Devices
- Wearable neuromorphic sensors
- Battery-powered SNN inference
- Aggressive quantization with EMD guarantees

### 3. SNN Model Compression
- Model compression for deployment
- Tradeoff between size and temporal fidelity
- EMD-guided pruning and quantization

### 4. Temporal Coding SNNs
- Time-to-first-spike (TTFS) coding
- Rank-order encoding
- Phase coding preservation

## Pitfalls

### 1. Computational Cost
- **Issue**: EMD computation is expensive compared to simple metrics
- **Mitigation**: Use histogram approximation, subsample spike data

### 2. Feature Selection
- **Issue**: Which spike features matter depends on coding scheme
- **Mitigation**: Task-specific feature importance analysis

### 3. Reference Model
- **Issue**: EMD requires full-precision reference
- **Mitigation**: Use distilled or ensemble reference

### 4. Temporal Resolution
- **Issue**: Spike timing precision affects EMD computation
- **Mitigation**: Match temporal resolution to neuromorphic hardware

## Related Skills
- snn-fpga-hardware-software-codesign
- spike-sparsity-deployment-cost
- event-driven-neuromorphic-transceiver
- neuromorphic-power-converter-health

## References
```bibtex
@article{2026quantizationsnn,
  title={Quantization of Spiking Neural Networks Beyond Accuracy},
  journal={arXiv preprint arXiv:2604.14487},
  year={2026}
}
```
