---
name: eeg-structure-guided-diffusion-v2
description: "Structure-Guided Diffusion Model (SGDM v2) for EEG-based visual cognition reconstruction with enhanced cross-subject generalization. Activation: EEG diffusion reconstruction, visual cognition decoding, SGDM, brain-to-image, neural decoding."
---

# Structure-Guided Diffusion Model for EEG Visual Reconstruction

> A diffusion-based generative framework for reconstructing visual cognition from EEG signals, using structural guidance to improve image quality and semantic consistency.

## Metadata
- **Source**: arXiv:2604.22649v1
- **Authors**: Yongxiang Lian, Yueyang Cang, Pingge Hu, et al.
- **Published**: 2026-04-24

## Core Methodology

### Key Innovation
**Structure-Guided Diffusion Model (SGDM)** addresses the challenge of reconstructing visual perception from brain signals by:

1. **Dual-Stream Architecture**: Separately processing semantic and structural information
2. **Diffusion-Based Generation**: High-quality image synthesis conditioned on EEG features
3. **Cross-Subject Generalization**: Techniques for decoding across different individuals
4. **Hierarchical Guidance**: Multi-scale structural constraints for realistic outputs

### Technical Framework

#### Architecture Overview
```
SGDM Framework:
┌─────────────────────────────────────────────────────────────┐
│                       EEG Input                             │
└─────────────────────────┬───────────────────────────────────┘
                          ↓
        ┌─────────────────┼─────────────────┐
        ↓                 ↓                 ↓
   ┌─────────┐     ┌──────────┐     ┌──────────┐
   │Semantic │     │ Structural│     │ Temporal│
   │Encoder  │     │ Encoder   │     │ Encoder │
   └────┬────┘     └────┬─────┘     └────┬────┘
        │               │                 │
        └───────────────┼─────────────────┘
                          ↓
        ┌─────────────────┴─────────────────┐
        ↓                                   ↓
   ┌──────────────────────────────────────────────────┐
   │          Conditional Diffusion Model              │
   │  ┌────────────────────────────────────────────┐  │
   │  │  U-Net with Cross-Attention to EEG Features│  │
   │  │  - Semantic guidance (CLIP-like space)     │  │
   │  │  - Structural guidance (edge maps)         │  │
   │  │  - Temporal coherence constraints          │  │
   │  └────────────────────────────────────────────┘  │
   └─────────────────────────┬─────────────────────────┘
                              ↓
                     ┌────────────────┐
                     │ Reconstructed  │
                     │     Image      │
                     └────────────────┘
```

#### 1. Multi-Modal EEG Encoder
```python
class MultiModalEEGEncoder(nn.Module):
    """Extract multi-faceted features from EEG signals."""
    
    def __init__(self, eeg_channels=64, eeg_samples=512):
        super().__init__()
        
        # Semantic pathway - global meaning
        self.semantic_encoder = nn.Sequential(
            # Temporal convolution
            nn.Conv1d(eeg_channels, 128, kernel_size=25, padding=12),
            nn.BatchNorm1d(128),
            nn.ReLU(),
            nn.MaxPool1d(4),
            
            # Deeper feature extraction
            nn.Conv1d(128, 256, kernel_size=13, padding=6),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.MaxPool1d(4),
            
            # Global pooling
            nn.AdaptiveAvgPool1d(1),
            nn.Flatten(),
            nn.Linear(256, 512)  # Semantic embedding
        )
        
        # Structural pathway - spatial information
        self.structural_encoder = nn.Sequential(
            # Frequency-domain features
            self.FrequencyEncoder(),
            
            # Spatial convolution (treating channels as spatial)
            nn.Conv2d(1, 32, kernel_size=(5, 5), padding=2),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            
            nn.Conv2d(32, 64, kernel_size=(3, 3), padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            
            nn.AdaptiveAvgPool2d((8, 8)),
            nn.Flatten(),
            nn.Linear(64 * 8 * 8, 256)  # Structural embedding
        )
        
        # Temporal pathway - dynamics
        self.temporal_encoder = nn.LSTM(
            input_size=eeg_channels,
            hidden_size=128,
            num_layers=2,
            batch_first=True,
            bidirectional=True
        )
        self.temporal_proj = nn.Linear(256, 256)
    
    def forward(self, eeg_signal):
        """
        Args:
            eeg_signal: [batch, channels, time]
        Returns:
            semantic_emb: [batch, 512]
            structural_emb: [batch, 256]
            temporal_emb: [batch, 256]
        """
        # Semantic features
        semantic = self.semantic_encoder(eeg_signal)
        
        # Structural features (reshape for spatial processing)
        eeg_2d = eeg_signal.unsqueeze(1)  # [batch, 1, channels, time]
        structural = self.structural_encoder(eeg_2d)
        
        # Temporal features
        eeg_transposed = eeg_signal.transpose(1, 2)  # [batch, time, channels]
        lstm_out, _ = self.temporal_encoder(eeg_transposed)
        temporal = self.temporal_proj(lstm_out[:, -1, :])
        
        return semantic, structural, temporal
    
    class FrequencyEncoder(nn.Module):
        """Extract frequency-domain features."""
        
        def forward(self, x):
            # Apply FFT along time dimension
            fft_features = torch.fft.rfft(x, dim=-1)
            power = torch.abs(fft_features) ** 2
            
            # Band-power features (theta, alpha, beta, gamma)
            theta = power[:, :, 4:8].mean(dim=-1, keepdim=True)
            alpha = power[:, :, 8:13].mean(dim=-1, keepdim=True)
            beta = power[:, :, 13:30].mean(dim=-1, keepdim=True)
            gamma = power[:, :, 30:100].mean(dim=-1, keepdim=True)
            
            return torch.cat([theta, alpha, beta, gamma], dim=-1)
```

#### 2. Structure-Guided Diffusion Model
```python
class StructureGuidedDiffusion(nn.Module):
    """Diffusion model conditioned on EEG features with structural guidance."""
    
    def __init__(self, image_size=256, channels=3, eeg_dim=1024):
        super().__init__()
        self.image_size = image_size
        self.channels = channels
        
        # Time embedding
        self.time_embed = nn.Sequential(
            SinusoidalPositionEmbeddings(256),
            nn.Linear(256, 512),
            nn.SiLU(),
            nn.Linear(512, 512)
        )
        
        # EEG feature projection
        self.eeg_proj = nn.Sequential(
            nn.Linear(eeg_dim, 512),
            nn.SiLU(),
            nn.Linear(512, 512)
        )
        
        # U-Net backbone with cross-attention
        self.unet = UNetWithCrossAttention(
            dim=64,
            init_dim=64,
            out_dim=channels,
            dim_mults=(1, 2, 4, 8),
            channels=channels,
            with_cross_attention=True,
            cross_attention_dim=512
        )
        
        # Structure guidance network
        self.structure_guide = StructureGuidanceModule()
    
    def forward(self, x, t, eeg_features, structure_hint=None):
        """
        Args:
            x: Noisy image [batch, channels, H, W]
            t: Timestep [batch]
            eeg_features: Concatenated EEG embeddings [batch, eeg_dim]
            structure_hint: Optional edge/sketch guidance [batch, 1, H, W]
        """
        # Time and EEG embeddings
        t_emb = self.time_embed(t)
        eeg_emb = self.eeg_proj(eeg_features)
        
        # Combine conditioning
        cond = t_emb + eeg_emb
        
        # Apply structure guidance if provided
        if structure_hint is not None:
            x = self.structure_guide(x, structure_hint)
        
        # U-Net forward with cross-attention to EEG
        output = self.unet(x, cond, context=eeg_emb)
        
        return output
    
    def p_losses(self, x_start, t, eeg_features, noise=None):
        """Compute diffusion loss."""
        if noise is None:
            noise = torch.randn_like(x_start)
        
        # Forward diffusion
        x_noisy = self.q_sample(x_start, t, noise)
        
        # Predict noise
        predicted_noise = self.forward(x_noisy, t, eeg_features)
        
        # Simple MSE loss
        loss = F.mse_loss(predicted_noise, noise)
        
        return loss
```

#### 3. Structure Guidance Module
```python
class StructureGuidanceModule(nn.Module):
    """Inject structural information into diffusion process."""
    
    def __init__(self, image_size=256):
        super().__init__()
        
        # Edge detection and enhancement
        self.edge_encoder = nn.Sequential(
            nn.Conv2d(1, 32, 3, padding=1),
            nn.ReLU(),
            nn.Conv2d(32, 64, 3, padding=1),
            nn.ReLU(),
            nn.Conv2d(64, 32, 3, padding=1)
        )
        
        # Multi-scale structure integration
        self.structure_fusion = nn.ModuleList([
            self._make_fusion_layer(channels=32, scale=2**i)
            for i in range(4)
        ])
    
    def _make_fusion_layer(self, channels, scale):
        """Create structure fusion layer at given scale."""
        return nn.Sequential(
            nn.Conv2d(channels + 3, channels, 3, padding=1),
            nn.GroupNorm(8, channels),
            nn.SiLU(),
            nn.Conv2d(channels, 3, 1)
        )
    
    def forward(self, x, structure_hint):
        """
        Args:
            x: Image tensor [batch, 3, H, W]
            structure_hint: Edge/sketch [batch, 1, H, W]
        """
        # Encode structure
        structure_emb = self.edge_encoder(structure_hint)
        
        # Multi-scale fusion
        outputs = []
        current_x = x
        
        for fusion_layer in self.structure_fusion:
            # Resize structure to match current scale
            h, w = current_x.shape[2:]
            structure_resized = F.interpolate(
                structure_emb, size=(h, w), mode='bilinear'
            )
            
            # Concatenate and fuse
            combined = torch.cat([current_x, structure_resized], dim=1)
            current_x = fusion_layer(combined)
            outputs.append(current_x)
            
            # Downsample for next scale
            current_x = F.avg_pool2d(current_x, 2)
        
        # Return finest scale
        return outputs[0]
```

#### 4. Cross-Subject Training
```python
class CrossSubjectTrainer:
    """Training with cross-subject generalization."""
    
    def __init__(self, model, num_subjects=10):
        self.model = model
        self.num_subjects = num_subjects
        
        # Subject-specific adapters
        self.subject_adapters = nn.ModuleList([
            SubjectAdapter(eeg_dim=1024, adapter_dim=256)
            for _ in range(num_subjects)
        ])
        
        # Domain discriminator for adversarial training
        self.domain_discriminator = DomainDiscriminator()
    
    def train_step(self, batch, subject_id):
        """Training step with domain adaptation."""
        eeg, image = batch
        
        # Apply subject-specific adapter
        adapted_eeg = self.subject_adapters[subject_id](eeg)
        
        # Standard diffusion loss
        t = torch.randint(0, self.timesteps, (eeg.size(0),))
        diffusion_loss = self.model.p_losses(image, t, adapted_eeg)
        
        # Adversarial domain confusion loss
        domain_pred = self.domain_discriminator(adapted_eeg)
        domain_loss = F.cross_entropy(
            domain_pred, 
            torch.full_like(domain_pred[:, 0].long(), subject_id)
        )
        
        # Gradient reversal for domain confusion
        confusion_loss = -0.1 * domain_loss
        
        total_loss = diffusion_loss + confusion_loss
        
        return total_loss, {
            'diffusion': diffusion_loss.item(),
            'domain': domain_loss.item()
        }
```

## Implementation Guide

### Prerequisites
- Python 3.9+
- PyTorch 2.0+
- diffusers library
- MNE (for EEG preprocessing)
- CLIP (for semantic supervision)

### Installation
```bash
pip install torch torchvision diffusers
pip install mne scikit-learn
pip install clip-by-openai
```

### Step-by-Step Implementation

#### Step 1: EEG Preprocessing
```python
import mne
import numpy as np

def preprocess_eeg(raw_eeg, sfreq=1000, l_freq=1, h_freq=100):
    """Preprocess raw EEG for SGDM."""
    
    # Bandpass filter
    raw_eeg.filter(l_freq=l_freq, h_freq=h_freq)
    
    # Remove artifacts with ICA
    ica = mne.preprocessing.ICA(n_components=20, random_state=42)
    ica.fit(raw_eeg)
    ica.apply(raw_eeg)
    
    # Extract epochs aligned to stimulus onset
    events = mne.find_events(raw_eeg)
    epochs = mne.Epochs(
        raw_eeg, events, 
        tmin=0, tmax=0.5,  # 500ms post-stimulus
        baseline=(0, 0),
        preload=True
    )
    
    return epochs.get_data()  # [n_epochs, n_channels, n_times]
```

#### Step 2: Train the Model
```python
from torch.utils.data import DataLoader

# Initialize model
model = StructureGuidedDiffusion(
    image_size=256,
    channels=3,
    eeg_dim=1024
)

encoder = MultiModalEEGEncoder()

# Training configuration
optimizer = torch.optim.AdamW(
    list(model.parameters()) + list(encoder.parameters()),
    lr=1e-4
)

scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
    optimizer, T_max=100000
)

# Training loop
def train_epoch(dataloader, model, encoder, optimizer):
    model.train()
    total_loss = 0
    
    for batch_idx, (eeg, images) in enumerate(dataloader):
        # Encode EEG
        semantic, structural, temporal = encoder(eeg)
        eeg_features = torch.cat([semantic, structural, temporal], dim=1)
        
        # Sample timestep
        t = torch.randint(0, 1000, (eeg.size(0),), device=eeg.device)
        
        # Compute loss
        loss = model.p_losses(images, t, eeg_features)
        
        # Optimize
        optimizer.zero_grad()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(
            list(model.parameters()) + list(encoder.parameters()), 
            max_norm=1.0
        )
        optimizer.step()
        
        total_loss += loss.item()
    
    return total_loss / len(dataloader)
```

#### Step 3: Reconstruct Images
```python
def reconstruct_from_eeg(model, encoder, eeg_signal, num_samples=5):
    """Generate image reconstructions from EEG."""
    
    model.eval()
    with torch.no_grad():
        # Encode EEG
        semantic, structural, temporal = encoder(eeg_signal)
        eeg_features = torch.cat([semantic, structural, temporal], dim=1)
        
        # Repeat for multiple samples
        eeg_features = eeg_features.repeat(num_samples, 1)
        
        # Generate with DDPM sampling
        images = sample(model, eeg_features, steps=50)
    
    return images

@torch.no_grad()
def sample(model, eeg_features, steps=50, image_size=256):
    """DDPM sampling."""
    device = eeg_features.device
    batch_size = eeg_features.size(0)
    
    # Start from noise
    x = torch.randn(batch_size, 3, image_size, image_size, device=device)
    
    # Reverse diffusion
    for t in reversed(range(steps)):
        t_batch = torch.full((batch_size,), t, device=device)
        
        # Predict noise
        predicted_noise = model(x, t_batch, eeg_features)
        
        # Denoise step
        alpha_t = alphas[t]
        alpha_t_prev = alphas[t-1] if t > 0 else torch.tensor(1.0)
        beta_t = betas[t]
        
        x = (x - beta_t * predicted_noise / (1 - alpha_t).sqrt()) / alpha_t.sqrt()
        
        if t > 0:
            noise = torch.randn_like(x)
            x = x + beta_t.sqrt() * noise
    
    return x
```

## Applications

### 1. Brain-Computer Interfaces
- Visual prosthetics for the blind
- Communication aids for locked-in patients
- Cognitive state monitoring

### 2. Neuroscience Research
- Studying visual perception mechanisms
- Understanding neural representations
- Comparing human and model vision

### 3. Assistive Technologies
- Visual memory reconstruction
- Dream visualization
- Enhanced reality systems

### 4. Clinical Diagnostics
- Visual agnosia assessment
- Rehabilitation progress tracking
- Cognitive load monitoring

## Evaluation Metrics

| Metric | Description | Target |
|--------|-------------|--------|
| SSIM | Structural similarity | > 0.6 |
| PSNR | Peak signal-to-noise | > 20 dB |
| CLIP Score | Semantic similarity | > 0.7 |
| FID | Frechet Inception Distance | < 50 |
| Classification Accuracy | Semantic correctness | > 80% |

## Pitfalls

### Limitations
1. **Low Spatial Resolution**: EEG has inherent spatial blurring
2. **Individual Variability**: Cross-subject generalization challenging
3. **Stimulus-Specific**: Performance varies by visual category
4. **Temporal Limitations**: Best for static images, limited for video

### Known Issues
| Issue | Cause | Solution |
|-------|-------|----------|
| Blurry reconstructions | EEG spatial resolution | Multi-modal fusion, structural guidance |
| Subject-specific artifacts | Individual brain differences | Domain adaptation, subject embeddings |
| Category bias | Training data imbalance | Balanced sampling, augmentation |
| Temporal misalignment | Variable neural latencies | Temporal alignment network |

### Comparison with fMRI-Based Methods
```
                    EEG (SGDM)    fMRI    MEG
Temporal Resolution   ms           s       ms
Spatial Resolution    cm           mm      cm
Portability          High         Low     Medium
Cost                 Low          High    High
Reconstruction Quality Medium      High    Medium
```

## Related Skills
- `eeg-diffusion-visual-reconstruction`: Diffusion-based EEG reconstruction
- `eeg2vision-multimodal-eeg-framework-2d-visual': EEG-to-image framework
- `in-context-brain-decoding`: Training-free brain decoding
- `neural-encoding-evaluation-meeg': Neural encoding evaluation

## References
- Lian, Y., et al. (2026). Structure-Guided Diffusion Model for EEG-Based Visual Cognition Reconstruction. arXiv:2604.22649.
- Shen, G., et al. (2019). Deep image reconstruction from human brain activity.
- Chen, T., et al. (2020). Generative pretraining from pixels.
