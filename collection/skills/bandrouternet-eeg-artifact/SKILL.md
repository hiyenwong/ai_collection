---
name: bandrouternet-eeg-artifact
description: "BandRouteNet adaptive frequency-aware neural network for EEG artifact removal. Jointly exploits band-specific processing and full-band contextual modeling for EOG/EMG artifact denoising. Features band-wise denoising with routing mechanism and full-band conditioner. Use for neurological diagnosis, BCI applications, and EEG signal enhancement. Keywords: EEG denoising, artifact removal, EOG, EMG, band routing, frequency-aware, brain-computer interface."
---

# BandRouteNet: EEG Artifact Removal

BandRouteNet is an adaptive frequency-aware neural network for EEG denoising that jointly exploits band-specific processing and full-band contextual modeling to remove EOG (electrooculographic) and EMG (electromyographic) artifacts.

## Problem Statement

EEG signals are highly susceptible to artifact contamination:
- **EOG artifacts**: Eye movements and blinks
- **EMG artifacts**: Muscle activity
- **Challenges**: Diverse and temporally varying distributions, distinct spectral characteristics across frequency bands

Traditional methods fail because:
1. Different artifact sources exhibit unique spectral signatures
2. Artifacts vary temporally and across subjects
3. Simple filtering destroys neural signal components

## Core Architecture

### Three-Component Design

```
Input: Noisy EEG Signal
    ↓
┌─────────────────────────────────────┐
│  1. Band-wise Denoising Pathway     │
│     - Split into frequency bands    │
│     - Band-specific artifact removal│
│     - Routing mechanism             │
└─────────────────────────────────────┘
    ↓
┌─────────────────────────────────────┐
│  2. Full-band Conditioner           │
│     - Global temporal context       │
│     - Conditional parameters        │
│     - Signal-level refinement       │
└─────────────────────────────────────┘
    ↓
Output: Clean EEG Signal
```

### Band-wise Processing

**Frequency Band Decomposition**:
- Delta (0.5-4 Hz): Deep sleep, unconsciousness
- Theta (4-8 Hz): Drowsiness, meditation
- Alpha (8-13 Hz): Relaxed awareness
- Beta (13-30 Hz): Active thinking
- Gamma (30-100 Hz): Higher cognitive functions

**Routing Mechanism**:
```python
class BandRouter(nn.Module):
    """
    Adaptively determines where and to what extent 
    denoising should be applied within each band
    """
    def __init__(self, n_bands, hidden_dim):
        super().__init__()
        self.band_attention = nn.MultiheadAttention(n_bands, num_heads=4)
        self.routing_weights = nn.Linear(hidden_dim, n_bands)
    
    def forward(self, band_features):
        # Compute attention across bands
        attn_out, weights = self.band_attention(
            band_features, band_features, band_features
        )
        
        # Generate routing decisions
        routing = torch.sigmoid(self.routing_weights(attn_out))
        return routing  # [batch, time, n_bands]
```

### Full-band Conditioner

**Global Context Extraction**:
```python
class FullBandConditioner(nn.Module):
    """
    Processes original noisy EEG to extract global temporal context
    """
    def __init__(self, input_dim, hidden_dim):
        super().__init__()
        self.temporal_encoder = nn.LSTM(
            input_dim, hidden_dim, 
            num_layers=2, 
            bidirectional=True
        )
        self.context_proj = nn.Linear(hidden_dim*2, hidden_dim)
    
    def forward(self, noisy_eeg):
        # Extract global temporal context
        encoded, _ = self.temporal_encoder(noisy_eeg)
        
        # Generate conditional parameters
        conditional_params = self.context_proj(encoded)
        
        # Coarse-grained signal refinement
        refined = self.signal_refinement(encoded, noisy_eeg)
        
        return conditional_params, refined
```

## Complete Model Architecture

```python
class BandRouteNet(nn.Module):
    """
    Complete BandRouteNet implementation
    """
    def __init__(self, 
                 n_channels=64, 
                 n_bands=5,
                 hidden_dim=128):
        super().__init__()
        
        # Band decomposition
        self.band_filters = self._create_band_filters()
        
        # Band-wise processing branches
        self.band_processors = nn.ModuleList([
            BandProcessor(hidden_dim) for _ in range(n_bands)
        ])
        
        # Routing mechanism
        self.router = BandRouter(n_bands, hidden_dim)
        
        # Full-band conditioner
        self.conditioner = FullBandConditioner(n_channels, hidden_dim)
        
        # Fusion and reconstruction
        self.fusion = nn.Linear(n_bands * hidden_dim + hidden_dim, n_channels)
    
    def forward(self, noisy_eeg):
        # Decompose into bands
        band_signals = []
        for filter_fn in self.band_filters:
            band_sig = filter_fn(noisy_eeg)
            band_signals.append(band_sig)
        
        # Process each band
        band_features = []
        for i, processor in enumerate(self.band_processors):
            feat = processor(band_signals[i])
            band_features.append(feat)
        
        # Routing decisions
        routing_weights = self.router(torch.stack(band_features, dim=-1))
        
        # Full-band conditioning
        conditional_params, coarse_refined = self.conditioner(noisy_eeg)
        
        # Modulate band-wise pathway
        modulated_features = []
        for i, feat in enumerate(band_features):
            modulated = feat * routing_weights[..., i:i+1] * conditional_params
            modulated_features.append(modulated)
        
        # Fusion and reconstruction
        fused = torch.cat(modulated_features + [coarse_refined], dim=-1)
        clean_eeg = self.fusion(fused)
        
        return clean_eeg
```

## Training Strategy

### Loss Function

```python
class BandRouteLoss(nn.Module):
    """
    Combined loss for artifact removal
    """
    def __init__(self, alpha=0.5, beta=0.3):
        super().__init__()
        self.alpha = alpha  # Time-domain weight
        self.beta = beta    # Frequency-domain weight
    
    def forward(self, pred, target, noisy):
        # Time-domain MSE
        time_loss = F.mse_loss(pred, target)
        
        # Frequency-domain loss (spectral convergence)
        pred_fft = torch.fft.rfft(pred, dim=-1)
        target_fft = torch.fft.rfft(target, dim=-1)
        freq_loss = F.l1_loss(torch.abs(pred_fft), torch.abs(target_fft))
        
        # Artifact suppression loss
        residual = noisy - pred
        artifact_penalty = torch.mean(torch.abs(residual - (noisy - target)))
        
        return time_loss + self.alpha * freq_loss + self.beta * artifact_penalty
```

### Training Configuration

```yaml
model:
  n_channels: 64
  n_bands: 5
  hidden_dim: 128
  parameters: 0.2M  # Highly parameter-efficient

training:
  optimizer: AdamW
  lr: 1e-3
  batch_size: 32
  epochs: 100
  scheduler: cosine
  
data:
  dataset: EEGDenoiseNet
  train_split: 0.8
  augmentation: True
```

## Performance Metrics

### EEGDenoiseNet Benchmark Results

| Condition | RRMSE ↓ | SNR_imp ↑ |
|-----------|---------|-----------|
| EOG only  | 0.12    | 18.5 dB   |
| EMG only  | 0.15    | 15.2 dB   |
| Mixed     | 0.14    | 16.8 dB   |

**Comparison with SOTA**:
- Outperforms all baseline methods
- Only 0.2M trainable parameters (highly efficient)
- Robust across artifact types

## Usage Examples

### Example 1: Real-time EEG Denoising

```python
import torch
import numpy as np

# Load pretrained model
model = BandRouteNet.from_pretrained('bandrouternet_eeg')
model.eval()

# Process real-time EEG stream
def denoise_eeg_chunk(noisy_chunk):
    """
    Denoise a chunk of EEG data
    
    Args:
        noisy_chunk: [batch, channels, time] tensor
    
    Returns:
        clean_chunk: Denoised EEG
    """
    with torch.no_grad():
        noisy_tensor = torch.FloatTensor(noisy_chunk)
        clean_tensor = model(noisy_tensor)
    return clean_tensor.numpy()

# Real-time processing loop
for eeg_chunk in eeg_stream:
    clean_eeg = denoise_eeg_chunk(eeg_chunk)
    process_clean_signal(clean_eeg)
```

### Example 2: BCI Application

```python
# Preprocess EEG for motor imagery BCI
raw_eeg = load_bci_data()  # [channels, time]

# Remove artifacts
clean_eeg = model(torch.FloatTensor(raw_eeg).unsqueeze(0))

# Extract features for classification
features = extract_motor_imagery_features(clean_eeg)
prediction = bci_classifier.predict(features)
```

### Example 3: Clinical EEG Analysis

```python
# Load clinical EEG recording
eeg_data = mne.io.read_raw_edf('patient_eeg.edf')

# Apply BandRouteNet denoising
clean_data = []
for epoch in eeg_data.iter_epochs():
    denoised = model(epoch.get_data())
    clean_data.append(denoised)

# Analyze denoised data for seizure detection
seizure_detected = detect_seizures(np.concatenate(clean_data))
```

## Deployment Considerations

### Resource-Constrained Applications

- **Model size**: 0.2M parameters (~800KB)
- **Inference time**: <10ms per window on CPU
- **Memory**: <2MB RAM
- **Power**: Suitable for mobile/wearable devices

### Optimization for Edge Deployment

```python
# Quantization
model_int8 = torch.quantization.quantize_dynamic(
    model, {nn.Linear}, dtype=torch.qint8
)

# ONNX export for cross-platform deployment
torch.onnx.export(
    model_int8, 
    dummy_input, 
    'bandrouternet.onnx',
    opset_version=11
)
```

## References

- Paper: arXiv:2604.24428v1 [eess.SP]
- Title: "BandRouteNet: An Adaptive Band Routing Neural Network for EEG Artifact Removal"
- Author: Phat Lam
- Dataset: EEGDenoiseNet benchmark

## Related Skills

- `eeg-brain-connectivity-bci`: EEG functional connectivity for BCI
- `brain-network-controllability`: Brain network control theory
- `bci-rehabilitation-protocols`: BCI rehabilitation optimization

## Activation Keywords

- EEG denoising
- artifact removal
- EOG EMG removal
- BandRouteNet
- frequency-aware EEG
- brain-computer interface signal processing
- 脑电信号去噪
- 伪影去除
