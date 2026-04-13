---
name: eeg2vision-multimodal-reconstruction-v3
description: "EEG2Vision: A modular, end-to-end EEG-to-image framework for 2D visual reconstruction from low-density EEG in cognitive neuroscience. Uses multimodal alignment and generative models for visual stimulus reconstruction. Activation: eeg2vision, EEG visual reconstruction, multimodal EEG, cognitive neuroscience, 脑电视觉重建, EEG图像重建, 多模态脑电."
version: v1.0.0
last_updated: 2026-04-13
source_paper: "EEG2Vision: A Multimodal EEG-Based Framework for 2D Visual Reconstruction in Cognitive Neuroscience" (arXiv:2604.08063v1, 2026-04-09)
---

# EEG2Vision: Multimodal EEG-to-Image Reconstruction

## Description

This skill implements EEG2Vision, a modular, end-to-end EEG-to-image framework for reconstructing 2D visual stimuli from non-invasive electroencephalography (EEG). Designed for cognitive neuroscience applications, it addresses challenges of low spatial resolution and high noise in realistic low-density electrode configurations.

**Key Innovation**:
- Modular architecture with clear separation of concerns
- End-to-end training from EEG to images
- Optimized for low-density EEG (practical setups)
- Multimodal alignment between neural and visual representations

## Activation Keywords

- eeg2vision
- EEG visual reconstruction
- multimodal EEG
- cognitive neuroscience
- 脑电视觉重建
- EEG图像重建
- 多模态脑电
- EEG-to-image
- visual decoding EEG

## Problem Domain

### Challenge
- Reconstructing visual stimuli from EEG is challenging due to:
  - Low spatial resolution of EEG
  - High noise levels
  - Volume conduction effects
  - Individual variability in neural responses
- Traditional methods often require high-density setups (>128 channels)
- Need for practical solutions with consumer-grade EEG devices

### Solution
- Modular framework with distinct preprocessing, encoding, and generation stages
- Multimodal alignment for robust feature learning
- End-to-end optimization for task-specific representations
- Support for low-density configurations (32-64 channels)

## Methodology

### Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    EEG2Vision Framework                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  Stage 1: EEG Preprocessing & Feature Extraction                  │
│  ┌─────────────────────────────────────────────────────────┐     │
│  │  Raw EEG ──▶ Filtering ──▶ Artifact Removal ──▶ Features│     │
│  │                                                          │     │
│  │  • Bandpass: 1-50 Hz                                     │     │
│  │  • ICA/SSP for artifact removal                          │     │
│  │  • Time-frequency features (STFT/wavelet)                │     │
│  │  • Spatial filtering (CSP, xDAWN)                        │     │
│  └─────────────────────────────────────────────────────────┘     │
│                              │                                    │
│                              ▼                                    │
│  Stage 2: Neural Encoding (EEG-to-Latent)                         │
│  ┌─────────────────────────────────────────────────────────┐     │
│  │  EEG Features ──▶ Temporal Encoder ──▶ Spatial Encoder  │     │
│  │                                                          │     │
│  │  • Temporal: LSTM/Transformer for time dynamics          │     │
│  │  • Spatial: CNN/GNN for electrode correlations           │     │
│  │  • Output: Neural embedding z_eeg                        │     │
│  └─────────────────────────────────────────────────────────┘     │
│                              │                                    │
│                              ▼                                    │
│  Stage 3: Multimodal Alignment                                    │
│  ┌─────────────────────────────────────────────────────────┐     │
│  │  Contrastive Learning: z_eeg ↔ z_image                   │     │
│  │                                                          │     │
│  │  • CLIP-style contrastive loss                           │     │
│  │  • Cross-modal attention                                 │     │
│  │  • Joint embedding space                                 │     │
│  └─────────────────────────────────────────────────────────┘     │
│                              │                                    │
│                              ▼                                    │
│  Stage 4: Image Generation                                        │
│  ┌─────────────────────────────────────────────────────────┐     │
│  │  Aligned Embedding ──▶ Decoder ──▶ Reconstructed Image  │     │
│  │                                                          │     │
│  │  • Generator: StyleGAN / Diffusion Model                 │     │
│  │  • Conditioning on EEG embedding                         │     │
│  │  • Output: 2D visual reconstruction                      │     │
│  └─────────────────────────────────────────────────────────┘     │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

### Core Components

1. **EEG Preprocessing Pipeline**
   - Bandpass filtering (1-50 Hz for visual evoked potentials)
   - Independent Component Analysis (ICA) for artifact removal
   - Re-referencing (average or Laplacian)
   - Epoching around stimulus onset

2. **Temporal Encoding**
   - Captures time dynamics of visual processing
   - Architectures: LSTM, GRU, or Transformer
   - Input: Time-series EEG epochs
   - Output: Temporal feature representations

3. **Spatial Encoding**
   - Models spatial correlations across electrodes
   - Architectures: CNN over electrode grids or Graph Neural Networks
   - Captures topographic patterns

4. **Multimodal Alignment Module**
   - Contrastive learning between EEG and image embeddings
   - InfoNCE loss for alignment
   - Creates shared representation space

5. **Image Generation**
   - Conditional generative model
   - Options: StyleGAN, Stable Diffusion, or custom decoder
   - Conditioned on aligned EEG embedding

## Workflow

### Step 1: Data Preparation
```python
# Load EEG and image data
eeg_data = load_eeg_recording(subject_id)
images = load_stimuli(image_ids)

# Preprocess EEG
epochs = preprocess_eeg(eeg_data, 
                       tmin=-0.1, tmax=0.5,
                       filter_band=(1, 50))
```

### Step 2: Feature Extraction
```python
# Extract time-frequency features
tf_features = extract_time_frequency(epochs)

# Apply spatial filtering
spatial_features = apply_spatial_filter(tf_features, method='csp')
```

### Step 3: Neural Encoding
```python
# Temporal encoding
temporal_repr = temporal_encoder(spatial_features)

# Spatial encoding
spatial_repr = spatial_encoder(spatial_features)

# Fusion
fused_features = fusion_module([temporal_repr, spatial_repr])
eeg_embedding = projection_head(fused_features)
```

### Step 4: Multimodal Training
```python
# Get image embeddings via pretrained encoder
image_embedding = clip_encoder(images)

# Contrastive loss
loss = contrastive_loss(eeg_embedding, image_embedding)
```

### Step 5: Image Generation
```python
# Generate image from EEG
generated_image = generator(eeg_embedding)
```

## Implementation Details

### EEG Preprocessing Parameters
| Parameter | Value | Description |
|-----------|-------|-------------|
| Sampling rate | 500-1000 Hz | Original recording |
| Filter band | 1-50 Hz | Visual evoked potentials |
| Epoch window | -100 to 500 ms | Relative to stimulus |
| Baseline | -100 to 0 ms | Pre-stimulus baseline |

### Model Architecture
- **Temporal Encoder**: 2-layer Transformer, 256 hidden dim
- **Spatial Encoder**: GNN with 3 graph convolution layers
- **Fusion**: Concatenation + MLP
- **Projection Head**: 2-layer MLP for embedding space
- **Generator**: StyleGAN2 conditioned on EEG embedding

### Training Configuration
- **Batch size**: 32-64 (depending on GPU memory)
- **Learning rate**: 1e-4 with cosine annealing
- **Loss weights**:
  - Contrastive: 1.0
  - Reconstruction: 1.0
  - Perceptual: 0.5
  - Adversarial: 0.1

## Performance Metrics

| Metric | Description | Target (Low-density EEG) |
|--------|-------------|------------------------|
| SSIM | Structural similarity | > 0.4 |
| PSNR | Peak signal-to-noise | > 15 dB |
| LPIPS | Perceptual similarity | < 0.5 |
| Top-5 Accuracy | Classification | > 60% |
| Semantic Consistency | CLIP similarity | > 0.6 |

## Applications

1. **Cognitive Neuroscience Research**
   - Studying visual perception mechanisms
   - Understanding EEG correlates of vision
   - Cross-subject analysis

2. **Brain-Computer Interfaces**
   - Visual prosthetics
   - Communication devices for locked-in patients
   - Neurofeedback training

3. **Clinical Applications**
   - Visual deficit assessment
   - Rehabilitation monitoring
   - Diagnosis aid

4. **Consumer Technology**
   - EEG-based image retrieval
   - Attention-aware interfaces
   - Gaming applications

## Tools Used

- **mne-python**: EEG preprocessing and analysis
- **torch/torchvision**: Deep learning framework
- **diffusers**: Diffusion models for generation
- **transformers**: CLIP and multimodal models
- **scipy**: Signal processing
- **matplotlib**: Visualization

## References

### Source Paper
- **Title**: EEG2Vision: A Multimodal EEG-Based Framework for 2D Visual Reconstruction in Cognitive Neuroscience
- **arXiv**: 2604.08063v1
- **Published**: April 9, 2026
- **Authors**: Emanuele Balloni, Emanuele Frontoni, Chiara Matti, et al.

### Related Work
- Previous EEG visual decoding methods
- Multimodal learning literature
- Generative models for image synthesis
- Cognitive neuroscience of vision

## Limitations

- Reconstruction quality depends on EEG signal quality
- Requires stimulus-locked epochs
- Limited to seen (not imagined) visual stimuli
- Subject-specific calibration recommended
- Low-density EEG provides lower resolution than high-density setups

## Best Practices

1. **Data Quality**
   - Ensure good electrode impedance (< 5 kΩ)
   - Minimize movement artifacts
   - Use appropriate filtering

2. **Training Data**
   - Collect sufficient examples per stimulus class
   - Balance stimulus categories
   - Consider individual differences

3. **Evaluation**
   - Use held-out test sets
   - Report cross-subject performance
   - Include perceptual metrics

4. **Interpretability**
   - Visualize learned spatial patterns
   - Analyze temporal dynamics
   - Correlate with known ERP components

## Future Directions

- Extension to imagined visual stimuli
- Real-time decoding for BCI applications
- Integration with other modalities (fNIRS, MEG)
- Cross-dataset generalization
- Interpretability improvements

## Code Example

```python
import torch
from eeg2vision import EEG2VisionFramework

# Initialize framework
model = EEG2VisionFramework(
    eeg_channels=64,
    temporal_encoder='transformer',
    spatial_encoder='gnn',
    generator='stylegan2'
)

# Load pretrained weights
model.load_state_dict(torch.load('eeg2vision_v1.pth'))

# Process EEG data
eeg_epochs = preprocess_eeg(raw_eeg_data)

# Generate images
with torch.no_grad():
    reconstructed_images = model.reconstruct(eeg_epochs)

# Visualize results
visualize_reconstruction(stimuli, reconstructed_images)
```

## Keywords
EEG, visual reconstruction, multimodal learning, cognitive neuroscience, brain-computer interface, generative models, contrastive learning, StyleGAN, diffusion models, visual perception, evoked potentials

---

_Last updated: 2026-04-13_
_Paper date: 2026-04-09_


## Instructions for Agents

1. **理解需求**：分析用户请求的具体场景
2. **选择方法**：根据上下文选择合适的技术方案
3. **执行操作**：按照技能描述实施具体步骤
4. **验证结果**：检查结果是否符合预期


## Examples

### Example 1: Basic Usage

**User:** 请帮我应用此技能

**Agent:** 我将按照标准流程执行...

### Example 2: Advanced Usage

**User:** 有更复杂的场景需要处理

**Agent:** 针对复杂场景，我将采用以下策略...
