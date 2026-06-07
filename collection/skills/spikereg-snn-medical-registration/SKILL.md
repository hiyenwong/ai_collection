---
name: spikereg-snn-medical-registration
version: "1.0"
description: "SpikeReg: Energy-efficient 3D deformable medical image registration using Spiking Neural Networks with ANN-to-SNN conversion and surrogate gradient fine-tuning."
triggers:
  - spikereg
  - spiking neural network medical image registration
  - deformable registration SNN
  - neuromorphic medical imaging
  - energy efficient brain MRI registration
  - ANN to SNN conversion medical
  - sparse event-driven geometric prediction
  - SNN registration U-Net
source: "arXiv:2605.25144"
authors: ["SpikeReg authors"]
---

# SpikeReg: Energy-Efficient 3D Deformable Medical Image Registration with Spiking Neural Networks

## Overview

SpikeReg is the **first systematic application of Spiking Neural Networks (SNNs) to 3D deformable medical image registration**. It demonstrates that dense geometric prediction — aligning 3D brain MRI volumes — can be performed under sparse event-driven computation, achieving ANN-comparable accuracy with a **55.5× projected arithmetic-energy reduction**.

**Key Result**: SpikeReg reaches Dice 0.7474 ± 0.032 on OASIS Learn2Reg, matching the ANN teacher (0.7480 ± 0.037, p=0.67) at only 12.8% mean spike rate.

## Core Methodology

### Architecture: Spiking U-Net
- Convert existing analog ANN registration network to SNN architecture
- **Layer-wise weight transfer**: copy pretrained ANN weights directly to SNN
- **Activation-percentile threshold calibration**: set firing thresholds based on ANN activation percentiles to preserve representational fidelity
- U-Net encoder-decoder with skip connections, all layers operate with Leaky Integrate-and-Fire (LIF) neurons

### Three-Stage Training Pipeline
1. **Train ANN teacher** on registration task (local cross-correlation + diffusion regularization)
2. **ANN-to-SNN conversion**: layer-wise weight transfer + threshold calibration
3. **Surrogate gradient fine-tuning**: optimize combined loss:
   - Local cross-correlation (registration accuracy)
   - Diffusion regularization (deformation smoothness)
   - Spike-rate sparsity penalty (energy efficiency)

### Surrogate Gradient Fine-Tuning
```python
loss = local_cross_correlation(fixed, moved) \
     + lambda_reg * diffusion_regularization(displacement) \
     + lambda_sparsity * mean_spike_rate

# Surrogate gradient for non-differentiable spike function
# Uses straight-through estimator: dL/dU = dL/dS where S in {0,1}
```

## Negative Findings (Important for Practitioners)

1. **Displacement distillation hurts performance**: Training the SNN to mimic ANN displacement fields (knowledge distillation on outputs) degrades registration quality. Use registration loss directly instead.

2. **Label-Dice ANN teachers fail to transfer**: ANN models trained with Dice-based losses (common in segmentation) do not transfer well through rate-code conversion. Use reconstruction/correlation losses for ANN teachers.

## Energy Analysis

**SynOps/MAC proxy model**:
- SNN energy ≈ spike_rate × MAC_energy
- At 12.8% mean spike rate: 55.5× energy reduction vs. dense ANN
- Based on conservative loop-based operation assumption
- Real neuromorphic hardware (Intel Loihi 2, etc.) may achieve further gains

## Implementation Guide

### Step 1: ANN Teacher Training
```python
import torch
import torch.nn as nn

class RegistrationUNet(nn.Module):
    def __init__(self, in_channels=2, features=[16,32,64,128]):
        # Standard U-Net for deformable registration
        # Input: concatenated fixed+moving volume
        # Output: 3D displacement field
        pass

# Loss function
def registration_loss(fixed, moved, disp, lambda_reg=0.01):
    lcc = -local_cross_correlation(fixed, moved)
    reg = diffusion_regularization(disp)
    return lcc + lambda_reg * reg
```

### Step 2: ANN-to-SNN Conversion
```python
import spikingjelly.activation_based as sj

def convert_ann_to_snn(ann_model, calibration_data, percentile=99.9):
    """
    Layer-wise weight transfer with activation-percentile threshold calibration
    """
    snn_model = SpikingUNet(...)
    
    # Copy weights
    for snn_layer, ann_layer in zip(snn_model.layers, ann_model.layers):
        snn_layer.weight.data = ann_layer.weight.data.clone()
    
    # Calibrate thresholds
    ann_model.eval()
    with torch.no_grad():
        for data in calibration_data:
            activations = ann_model.get_activations(data)
            for layer_name, acts in activations.items():
                threshold = torch.quantile(acts.abs(), percentile/100)
                snn_model.get_layer(layer_name).threshold = threshold
    
    return snn_model
```

### Step 3: Surrogate Gradient Fine-Tuning
```python
def snn_registration_loss(fixed, moved, disp, spikes, 
                            lambda_reg=0.01, lambda_sparsity=1e-4):
    lcc = -local_cross_correlation(fixed, moved)
    reg = diffusion_regularization(disp)
    sparsity = mean_spike_rate(spikes)
    return lcc + lambda_reg * reg + lambda_sparsity * sparsity

# Training with BPTT through time
optimizer = torch.optim.Adam(snn_model.parameters(), lr=1e-4)
for epoch in range(num_epochs):
    for fixed, moving in dataloader:
        sj.functional.reset_net(snn_model)
        disp, spikes = snn_model(fixed, moving)
        moved = spatial_transform(moving, disp)
        loss = snn_registration_loss(fixed, moved, disp, spikes)
        loss.backward()
        optimizer.step()
```

## Dataset & Evaluation

- **OASIS Learn2Reg**: 3D brain MRI registration benchmark
- 19 validation image pairs
- Metric: Dice overlap of anatomical segmentations
- SpikeReg: 0.7474 ± 0.032 (same as ANN teacher 0.7480 ± 0.037)

## Pitfalls & Notes

1. **Do NOT use displacement distillation** — direct registration loss works better
2. **ANN teacher choice matters** — must use reconstruction/correlation losses, not segmentation-based Dice
3. **Threshold calibration is critical** — use representative calibration set from target domain
4. **Spike-rate sparsity tradeoff** — higher lambda_sparsity → lower energy but potentially lower Dice
5. **Timestep count** — more timesteps improve accuracy but increase latency; tune T (typically 4-8)

## Applications

- Neuromorphic medical devices with battery/power constraints
- Real-time intraoperative registration on edge hardware
- Multi-modal brain atlas alignment
- Longitudinal brain MRI change detection

## Why This Matters

This paper opens a **new frontier**: dense, geometrically-precise prediction (not just classification) on neuromorphic hardware. It proves that registration — which requires sub-voxel accurate displacement field estimation — is achievable with binary spikes, breaking the assumption that SNNs are limited to classification tasks.
