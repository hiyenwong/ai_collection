---
name: tgsn-eeg-dementia-diagnosis
description: "Task-guided Spatiotemporal Network (TGSN) with diffusion augmentation for EEG-based dementia diagnosis and MMSE prediction. Features multi-band feature fusion, gated spatiotemporal attention module, task-guided query module, and diffusion-based data augmentation. Use for Alzheimer's disease detection, Frontotemporal Dementia classification, VCI assessment, and MMSE score prediction. Keywords: EEG dementia diagnosis, TGSN, task-guided network, spatiotemporal attention, diffusion augmentation, Alzheimer's disease, MMSE prediction."
---

# TGSN: Task-Guided Spatiotemporal Network for EEG Dementia Diagnosis

Task-guided Spatiotemporal Network (TGSN) is a novel multi-task learning framework for EEG-based dementia diagnosis and MMSE (Mini-Mental State Examination) score prediction.

## Problem Statement

Dementia patients exhibit cognitive impairment assessed via MMSE, with underlying neurophysiological abnormalities reflected in EEG signals. However:

- **Multi-task interference**: Traditional approaches suffer from feature entanglement
- **Heterogeneous objectives**: Different tasks have conflicting optimization directions
- **Limited data**: Medical datasets are often small and imbalanced

## Core Innovation

### Four-Component Architecture

```
Input: Raw EEG Signal (multi-channel, time-series)
    ↓
┌─────────────────────────────────────────────┐
│ 1. Multi-band Feature Fusion Module        │
│    - Captures complementary spectral info   │
│    - Combines delta, theta, alpha, beta,    │
│      gamma band features                    │
└─────────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────────┐
│ 2. Diffusion Augmentation Module            │
│    - Pre-trained diffusion process          │
│    - Increases sample diversity             │
│    - Addresses limited data challenges      │
└─────────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────────┐
│ 3. Gated Spatiotemporal Attention Module    │
│    - Captures long-range spatial deps       │
│    - Models temporal dynamics               │
│    - Gates control information flow           │
└─────────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────────┐
│ 4. Task-Guided Query Module                 │
│    - Task-specific feature extraction       │
│    - Mitigates task interference            │
│    - Separate pathways per task             │
└─────────────────────────────────────────────┘
    ↓
Output: [Diagnosis Class, MMSE Score]
```

## Detailed Architecture

### 1. Multi-band Feature Fusion

**Spectral Band Decomposition**:

```python
class MultiBandFeatureFusion(nn.Module):
    """
    Extract and fuse features from multiple EEG frequency bands
    """
    def __init__(self, n_bands=5, n_channels=64):
        super().__init__()
        
        # Band-specific filters (learnable)
        self.band_filters = nn.ModuleList([
            BandFilter(low_freq, high_freq) 
            for low_freq, high_freq in [
                (0.5, 4),   # Delta
                (4, 8),     # Theta
                (8, 13),    # Alpha
                (13, 30),   # Beta
                (30, 100)   # Gamma
            ]
        ])
        
        # Band-specific feature extractors
        self.band_encoders = nn.ModuleList([
            TemporalConvNet(input_dim=n_channels, hidden_dim=128)
            for _ in range(n_bands)
        ])
        
        # Cross-band attention for fusion
        self.cross_band_attn = MultiHeadCrossBandAttention(
            n_heads=8, d_model=128
        )
    
    def forward(self, eeg_signal):
        # Decompose into frequency bands
        band_signals = []
        for filter_fn in self.band_filters:
            band_sig = filter_fn(eeg_signal)
            band_signals.append(band_sig)
        
        # Extract band-specific features
        band_features = []
        for i, encoder in enumerate(self.band_encoders):
            feat = encoder(band_signals[i])
            band_features.append(feat)
        
        # Fuse with cross-band attention
        fused = self.cross_band_attn(torch.stack(band_features, dim=1))
        
        return fused
```

### 2. Diffusion Augmentation Module

**Pre-trained Diffusion Process**:

```python
class DiffusionAugmentation(nn.Module):
    """
    Diffusion-based data augmentation for EEG
    """
    def __init__(self, noise_steps=1000, beta_start=1e-4, beta_end=0.02):
        super().__init__()
        
        # Diffusion schedule
        self.beta = torch.linspace(beta_start, beta_end, noise_steps)
        self.alpha = 1 - self.beta
        self.alpha_bar = torch.cumprod(self.alpha, dim=0)
        
        # Noise prediction network (U-Net architecture)
        self.noise_predictor = UNet1D(
            in_channels=64,
            model_channels=128,
            out_channels=64,
            num_res_blocks=2
        )
    
    def forward_diffusion(self, x, t):
        """Add noise according to diffusion schedule"""
        noise = torch.randn_like(x)
        alpha_bar_t = self.alpha_bar[t].view(-1, 1, 1)
        noisy = torch.sqrt(alpha_bar_t) * x + torch.sqrt(1 - alpha_bar_t) * noise
        return noisy, noise
    
    def reverse_diffusion(self, noisy, t):
        """Denoise step"""
        predicted_noise = self.noise_predictor(noisy, t)
        
        # Compute denoised sample
        alpha_t = self.alpha[t]
        alpha_bar_t = self.alpha_bar[t]
        beta_t = self.beta[t]
        
        x_pred = (noisy - torch.sqrt(1 - alpha_bar_t) * predicted_noise) / torch.sqrt(alpha_bar_t)
        x_prev = torch.sqrt(alpha_t) * x_pred + torch.sqrt(beta_t) * torch.randn_like(x_pred)
        
        return x_prev
    
    def augment(self, x, n_augmentations=5):
        """Generate augmented samples"""
        augmented = []
        for _ in range(n_augmentations):
            # Start from random noise
            current = torch.randn_like(x)
            # Reverse diffusion
            for t in reversed(range(self.noise_steps)):
                current = self.reverse_diffusion(current, t)
            augmented.append(current)
        return torch.cat(augmented, dim=0)
```

### 3. Gated Spatiotemporal Attention

**Long-range Dependencies & Temporal Dynamics**:

```python
class GatedSpatiotemporalAttention(nn.Module):
    """
    Captures spatial dependencies and temporal dynamics
    with gating mechanism
    """
    def __init__(self, d_model=128, n_heads=8, n_channels=64):
        super().__init__()
        
        # Spatial attention (across channels)
        self.spatial_attn = MultiHeadAttention(
            d_model=d_model,
            n_heads=n_heads
        )
        
        # Temporal attention (across time)
        self.temporal_attn = MultiHeadAttention(
            d_model=d_model,
            n_heads=n_heads
        )
        
        # Gating mechanism
        self.spatial_gate = nn.Sequential(
            nn.Linear(d_model, d_model),
            nn.Sigmoid()
        )
        self.temporal_gate = nn.Sequential(
            nn.Linear(d_model, d_model),
            nn.Sigmoid()
        )
        
        # Fusion
        self.fusion = nn.Linear(d_model * 2, d_model)
    
    def forward(self, x):
        # x: [batch, channels, time, features]
        
        # Spatial attention: attend across channels
        spatial_out = self.spatial_attn(x, x, x)  # [batch, time, features]
        spatial_gate = self.spatial_gate(spatial_out)
        spatial_gated = spatial_out * spatial_gate
        
        # Temporal attention: attend across time
        temporal_out = self.temporal_attn(
            x.transpose(1, 2), 
            x.transpose(1, 2), 
            x.transpose(1, 2)
        )  # [batch, channels, features]
        temporal_gate = self.temporal_gate(temporal_out)
        temporal_gated = temporal_out * temporal_gate
        
        # Fusion
        combined = torch.cat([spatial_gated, temporal_gated], dim=-1)
        output = self.fusion(combined)
        
        return output
```

### 4. Task-Guided Query Module

**Task-Specific Feature Extraction**:

```python
class TaskGuidedQueryModule(nn.Module):
    """
    Separates feature extraction for different tasks
    to mitigate interference
    """
    def __init__(self, d_model=128, n_tasks=2):
        super().__init__()
        self.n_tasks = n_tasks
        
        # Task-specific query projections
        self.task_queries = nn.ModuleList([
            nn.Linear(d_model, d_model) for _ in range(n_tasks)
        ])
        
        # Task-specific feature extractors
        self.task_encoders = nn.ModuleList([
            TransformerEncoder(d_model=d_model, n_layers=4)
            for _ in range(n_tasks)
        ])
        
        # Task-specific output heads
        self.task_heads = nn.ModuleList([
            TaskHead(task_id=i, d_model=d_model) 
            for i in range(n_tasks)
        ])
    
    def forward(self, shared_features, task_id=None):
        if task_id is not None:
            # Single task forward
            query = self.task_queries[task_id](shared_features)
            task_feat = self.task_encoders[task_id](query)
            output = self.task_heads[task_id](task_feat)
            return output
        else:
            # Multi-task forward
            outputs = []
            for i in range(self.n_tasks):
                query = self.task_queries[i](shared_features)
                task_feat = self.task_encoders[i](query)
                output = self.task_heads[i](task_feat)
                outputs.append(output)
            return outputs
```

## Complete Model

```python
class TGSN(nn.Module):
    """
    Task-guided Spatiotemporal Network for EEG Dementia Diagnosis
    """
    def __init__(self, 
                 n_channels=64,
                 n_bands=5,
                 d_model=128,
                 n_tasks=2):
        super().__init__()
        
        # Component 1: Multi-band feature fusion
        self.band_fusion = MultiBandFeatureFusion(n_bands, n_channels)
        
        # Component 2: Diffusion augmentation
        self.diffusion_aug = DiffusionAugmentation()
        
        # Component 3: Gated spatiotemporal attention
        self.spatiotemporal_attn = GatedSpatiotemporalAttention(d_model, n_channels)
        
        # Component 4: Task-guided query module
        self.task_module = TaskGuidedQueryModule(d_model, n_tasks)
    
    def forward(self, eeg, task_id=None, augment=False):
        # Step 1: Multi-band feature extraction
        band_features = self.band_fusion(eeg)
        
        # Step 2: Optional diffusion augmentation
        if augment and self.training:
            augmented = self.diffusion_aug.augment(band_features)
            band_features = torch.cat([band_features, augmented], dim=0)
        
        # Step 3: Spatiotemporal modeling
        spatiotemporal_features = self.spatiotemporal_attn(band_features)
        
        # Step 4: Task-guided outputs
        if task_id is not None:
            # Single task
            if task_id == 0:  # Classification
                output = self.task_module(spatiotemporal_features, task_id)
            else:  # Regression (MMSE)
                output = self.task_module(spatiotemporal_features, task_id)
        else:
            # Both tasks
            outputs = self.task_module(spatiotemporal_features)
        
        return outputs
```

## Training Strategy

### Multi-task Loss

```python
class TGSNLoss(nn.Module):
    """
    Combined loss for classification and regression tasks
    """
    def __init__(self, alpha=1.0, beta=1.0):
        super().__init__()
        self.alpha = alpha  # Classification weight
        self.beta = beta    # Regression weight
        self.ce_loss = nn.CrossEntropyLoss()
        self.mse_loss = nn.MSELoss()
    
    def forward(self, pred_class, pred_mmse, target_class, target_mmse):
        # Classification loss (diagnosis)
        loss_class = self.ce_loss(pred_class, target_class)
        
        # Regression loss (MMSE score)
        loss_mmse = self.mse_loss(pred_mmse, target_mmse)
        
        # Combined loss with task weights
        total_loss = self.alpha * loss_class + self.beta * loss_mmse
        
        return total_loss, loss_class, loss_mmse
```

### Training Configuration

```yaml
model:
  n_channels: 19  # Standard EEG montage
  n_bands: 5
  d_model: 128
  n_tasks: 2

training:
  epochs: 200
  batch_size: 32
  optimizer: AdamW
  lr: 1e-3
  weight_decay: 1e-4
  scheduler: cosine_with_warmup
  warmup_steps: 1000

data:
  dataset: XY02
  train_split: 0.8
  val_split: 0.1
  test_split: 0.1
  augmentation: true
  n_augmentations: 5
```

## Performance Results

### XY02 Dataset Results

**Classification Tasks**:

| Task | Accuracy | Improvement vs Baseline |
|------|----------|------------------------|
| AD vs FTD | **97.78%** | +16.39% |
| AD vs FTD vs VCI | **83.93%** | +8.28% |

**MMSE Prediction**:

| Task | RMSE | Improvement vs Baseline |
|------|------|------------------------|
| AD/FTD | **1.93** | -1.44 |
| AD/FTD/VCI | **2.38** | -1.43 |

### Cross-Dataset Generalization

Validation on **DS004504 dataset** demonstrates strong cross-dataset generalization capability.

## Usage Examples

### Example 1: Training on Custom Dataset

```python
import torch
from torch.utils.data import DataLoader

# Initialize model
model = TGSN(n_channels=19, n_bands=5, d_model=128)

# Prepare data
train_dataset = EEGDementiaDataset(
    data_dir='./data/XY02',
    split='train',
    transform=True
)
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)

# Training loop
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3)
criterion = TGSNLoss(alpha=1.0, beta=1.0)

for epoch in range(200):
    model.train()
    for batch in train_loader:
        eeg, target_class, target_mmse = batch
        
        # Forward pass
        pred_class, pred_mmse = model(eeg, augment=True)
        
        # Compute loss
        loss, loss_class, loss_mmse = criterion(
            pred_class, pred_mmse, target_class, target_mmse
        )
        
        # Backward pass
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
```

### Example 2: Inference

```python
model.eval()
with torch.no_grad():
    # Load test EEG
    test_eeg = load_eeg('patient_001.edf')
    
    # Predict diagnosis
    pred_class, pred_mmse = model(test_eeg)
    
    # Get diagnosis
    diagnosis = torch.argmax(pred_class, dim=1)
    diagnosis_label = ['AD', 'FTD', 'VCI'][diagnosis.item()]
    
    # Get MMSE score
    mmse_score = pred_mmse.item()
    
    print(f"Diagnosis: {diagnosis_label}")
    print(f"Predicted MMSE: {mmse_score:.2f}")
```

### Example 3: Model Interpretation

```python
from captum.attr import IntegratedGradients

# Interpret model predictions
ig = IntegratedGradients(model)

# Compute attributions
attributions, delta = ig.attribute(
    test_eeg,
    target=0,  # Class index
    return_convergence_delta=True
)

# Visualize important channels and time points
plot_attributions(attributions, channel_names=eeg_channels)
```

## Deployment

### Model Export

```python
# Export to ONNX for deployment
torch.onnx.export(
    model,
    dummy_input,
    'tgsn_dementia.onnx',
    input_names=['eeg_signal'],
    output_names=['diagnosis', 'mmse_score'],
    dynamic_axes={
        'eeg_signal': {0: 'batch_size', 2: 'time_steps'}
    }
)
```

### Clinical Integration

```python
# Clinical API wrapper
class TGSNClinicalAPI:
    def __init__(self, model_path='tgsn_dementia.onnx'):
        self.session = onnxruntime.InferenceSession(model_path)
    
    def diagnose(self, eeg_data):
        """
        Clinical diagnosis endpoint
        
        Args:
            eeg_data: Preprocessed EEG [channels, time]
        
        Returns:
            diagnosis: AD, FTD, or VCI
            confidence: Prediction confidence
            mmse: Predicted MMSE score
        """
        inputs = {self.session.get_inputs()[0].name: eeg_data}
        outputs = self.session.run(None, inputs)
        
        diagnosis = np.argmax(outputs[0])
        confidence = np.max(softmax(outputs[0]))
        mmse = outputs[1][0]
        
        return {
            'diagnosis': ['AD', 'FTD', 'VCI'][diagnosis],
            'confidence': float(confidence),
            'mmse_score': float(mmse)
        }
```

## References

- Paper: arXiv:2604.23964v1 [cs.LG]
- Title: "Task-guided Spatiotemporal Network with Diffusion Augmentation for EEG-based Dementia Diagnosis and MMSE Prediction"
- Authors: Xiaoyu Zheng, Xu Tian, Bin Jiao, et al.
- Datasets: XY02, DS004504 (OpenNeuro)

## Related Skills

- `bandrouternet-eeg-artifact`: EEG artifact removal
- `homology-morphometry-brain-atrophy`: Topological brain analysis
- `brain-network-controllability`: Brain network control theory

## Activation Keywords

- EEG dementia diagnosis
- TGSN
- task-guided network
- diffusion augmentation EEG
- spatiotemporal attention
- Alzheimer's EEG classification
- MMSE prediction
- 脑电图痴呆诊断
- 时空注意力网络
