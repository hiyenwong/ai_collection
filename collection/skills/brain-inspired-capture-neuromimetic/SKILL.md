---
name: brain-inspired-capture-neuromimetic
description: "Brain-Inspired Capture (BI-Cap) methodology for visual decoding of neurophysiological signals. Neuromimetic perceptual simulation paradigm that aligns neural and visual modalities by emulating Human Visual System (HVS) processing. Activation: visual decoding, brain-to-image, neuromimetic, BI-Cap, HVS, brain-computer interface, perceptual simulation."
---

# Brain-Inspired Capture (BI-Cap)

> Neuromimetic perceptual simulation framework for zero-shot brain-to-image retrieval, aligning neural and visual modalities by emulating Human Visual System processing.

## Metadata
- **Source**: arXiv:2604.17927
- **Authors**: Feixue Shao, Guangze Shi, Xueyu Liu, Yongfei Wu, Mingqiang Wei
- **Published**: 2026-04-20
- **GitHub**: https://github.com/flysnow1024/BI-Cap

## Core Methodology

### Key Innovation
BI-Cap addresses the systematic and stochastic gaps between neural and visual modalities by implementing a neuromimetic pipeline that simulates Human Visual System (HVS) processing. The framework introduces evidence-driven latent space representation to model uncertainty and ensure robust neural embeddings.

### Technical Framework

#### 1. Neuromimetic Perceptual Pipeline
Four biologically plausible transformations:

| Transformation | Description |
|---------------|-------------|
| Dynamic Transform | Simulates saccadic eye movements and attention shifts |
| Static Transform | Models fixation-based stable perception |
| Multi-scale Processing | Emulates hierarchical visual cortex processing |
| Temporal Integration | Captures temporal dynamics of visual perception |

#### 2. Mutual Information-Guided Dynamic Blur Regulation
- **Purpose**: Simulate adaptive visual processing under varying attention states
- **Mechanism**: Uses mutual information between neural embeddings and visual features to guide dynamic blur kernel selection
- **Benefit**: Mimics foveated vision with higher resolution at fixation points

#### 3. Evidence-Driven Latent Space Representation
- **Problem Addressed**: Non-stationarity of neural activity in EEG/fMRI signals
- **Solution**: Explicit uncertainty modeling through evidence learning
- **Implementation**: Evidential deep learning framework that quantifies epistemic uncertainty

### Architecture Components

```
Input: Neural Signal (EEG/fMRI)
    ↓
[Neural Encoder] → Neural Embeddings
    ↓
[Evidence Layer] → Evidence Distribution
    ↓
[Uncertainty Modeling] → Mean + Variance
    ↓
[Neuromimetic Pipeline]
    - Dynamic Transform (attention simulation)
    - Static Transform (fixation modeling)
    - MI-guided Blur Regulation
    ↓
[Cross-Modal Alignment] ← Visual Features
    ↓
Output: Retrieved/Generated Image
```

## Implementation Guide

### Prerequisites
- Python 3.8+
- PyTorch 2.0+
- EEG/fMRI preprocessing tools (MNE-Python, Nilearn)
- Pretrained visual encoder (CLIP, DINO, etc.)

### Step-by-Step Implementation

#### 1. Neural Signal Preprocessing
```python
import mne
from scipy import signal

def preprocess_eeg(eeg_raw, fs=1000):
    """Preprocess EEG signals for BI-Cap input."""
    # Bandpass filter (1-100 Hz)
    eeg_filtered = mne.filter.filter_data(
        eeg_raw, sfreq=fs, l_freq=1, h_freq=100
    )
    
    # Epoch segmentation
    epochs = mne.make_fixed_length_epochs(
        eeg_filtered, duration=2.0, overlap=0.5
    )
    
    return epochs.get_data()
```

#### 2. Evidence-Driven Neural Encoder
```python
import torch
import torch.nn as nn

class EvidenceDrivenEncoder(nn.Module):
    """Evidence-driven neural encoder with uncertainty modeling."""
    
    def __init__(self, input_dim=128, hidden_dim=512, latent_dim=256):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(hidden_dim, latent_dim * 2)  # Mean and evidence
        )
        
    def forward(self, x):
        # Output: [mean, evidence]
        output = self.encoder(x)
        mean, evidence = torch.chunk(output, 2, dim=-1)
        
        # Softplus for positive evidence
        evidence = torch.nn.functional.softplus(evidence)
        
        # Calculate variance as inverse of evidence
        variance = 1.0 / (evidence + 1e-6)
        
        return mean, variance, evidence
```

#### 3. MI-Guided Dynamic Blur
```python
import torch.nn.functional as F

def mi_guided_blur(visual_features, neural_embeddings, sigma_range=(0.1, 2.0)):
    """Apply mutual information-guided dynamic blur."""
    # Calculate mutual information
    mi_score = calculate_mutual_information(
        visual_features, neural_embeddings
    )
    
    # Map MI to blur kernel size
    blur_sigma = mi_to_blur_sigma(mi_score, sigma_range)
    
    # Apply Gaussian blur
    blurred = F.gaussian_blur(
        visual_features, 
        kernel_size=int(blur_sigma * 6) + 1,
        sigma=blur_sigma
    )
    
    return blurred

def mi_to_blur_sigma(mi_score, sigma_range):
    """Map mutual information score to blur sigma."""
    # Higher MI → smaller blur (focus attention)
    # Lower MI → larger blur (diffuse attention)
    min_mi, max_mi = 0.0, 1.0
    min_sigma, max_sigma = sigma_range
    
    normalized = (mi_score - min_mi) / (max_mi - min_mi)
    sigma = max_sigma - normalized * (max_sigma - min_sigma)
    
    return sigma
```

#### 4. Cross-Modal Alignment Training
```python
class BICapModel(nn.Module):
    """Complete BI-Cap model for brain-to-image retrieval."""
    
    def __init__(self, neural_dim=128, visual_dim=512):
        super().__init__()
        self.neural_encoder = EvidenceDrivenEncoder(neural_dim)
        self.visual_encoder = load_pretrained_clip()  # or DINO
        
    def forward(self, neural_signal, visual_batch):
        # Encode neural signal with uncertainty
        neural_mean, neural_var, _ = self.neural_encoder(neural_signal)
        
        # Encode visual batch
        visual_features = self.visual_encoder(visual_batch)
        
        # Apply neuromimetic pipeline
        visual_simulated = self.neuromimetic_pipeline(
            visual_features, neural_mean
        )
        
        # Compute contrastive loss with uncertainty
        loss = self.evidence_contrastive_loss(
            neural_mean, neural_var, visual_simulated
        )
        
        return loss
    
    def evidence_contrastive_loss(self, neural_mean, neural_var, visual_feat):
        """Contrastive loss accounting for uncertainty."""
        # Scale similarities by inverse uncertainty
        similarity = torch.matmul(neural_mean, visual_feat.t())
        uncertainty_weight = 1.0 / (neural_var + 1e-6)
        
        weighted_sim = similarity * uncertainty_weight
        
        # Cross-entropy loss with temperature
        labels = torch.arange(len(neural_mean))
        loss = F.cross_entropy(weighted_sim / 0.07, labels)
        
        return loss
```

## Applications
- **Brain-Computer Interfaces**: Zero-shot visual decoding for BCIs
- **Neurotechnology**: Real-time neural signal interpretation
- **Cognitive Neuroscience**: Understanding visual perception mechanisms
- **Medical Imaging**: Reconstructing perceived visual stimuli from patient data

## Performance
- **Zero-shot brain-to-image retrieval**: +9.2% relative improvement
- **Cross-dataset generalization**: +8.0% on unseen datasets
- **Uncertainty modeling**: Robustness to non-stationary neural signals

## Pitfalls
- **Data Quality**: Requires high-quality, artifact-free neural recordings
- **Individual Variability**: May require subject-specific fine-tuning
- **Temporal Resolution**: EEG provides better temporal but lower spatial resolution than fMRI
- **Computational Cost**: Evidence-driven layers increase inference time

## Related Skills
- brain-dit-fmri-foundation-model
- eeg2vision-multimodal-reconstruction
- meta-learning-in-context-brain-decoding
