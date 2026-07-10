---
name: eeg-structure-guided-diffusion-v3
description: "Structure-Guided Diffusion Model (SGDM v3) for EEG-based visual cognition reconstruction with enhanced cross-subject generalization. Combines structurally supervised VAE, spatiotemporal EEG encoder with contrastive learning, and ControlNet-guided diffusion for high-fidelity image reconstruction from brain signals."
category: "ai_collection"
tags: ["EEG", "visual cognition", "diffusion model", "brain decoding", "ControlNet", "neural decoding", "brain-computer interface"]
activation: ["EEG diffusion reconstruction", "visual cognition decoding", "SGDM", "brain-to-image", "neural decoding", "EEG visual reconstruction"]
papers:
  - arxiv: "2604.22649"
    title: "Structure-Guided Diffusion Model for EEG-Based Visual Cognition Reconstruction"
    authors: ["Yongxiang Lian", "Yueyang Cang", "Pingge Hu", "Yuchen He", "Li Shi"]
    date: "2026-04-24"
---

# EEG Structure-Guided Diffusion Model (SGDM v3)

Structure-Guided Diffusion Model (SGDM) methodology for EEG-based visual cognition reconstruction. This skill enables decoding visual content from EEG signals using a two-stage generative mechanism combining structural VAE, spatiotemporal EEG encoding, and diffusion-based image generation.

## Overview

SGDM addresses the challenge of decoding visual information from electroencephalography (EEG) by incorporating explicit structural information into a diffusion-based generative framework. It extends neural decoding beyond low-dimensional or categorical outputs to high-fidelity image reconstruction.

### Key Capabilities

- **Abstract & Natural Image Reconstruction**: Works on both abstract visual objects (Kilogram dataset) and natural images (THINGS dataset)
- **Cross-Subject Generalization**: Enhanced generalization across diverse visual domains
- **Structural Information Integration**: Uses ControlNet to guide image generation with structural priors
- **Spatiotemporal EEG Encoding**: Captures hierarchical structural encoding patterns

## Architecture Components

### 1. Two-Stage Generative Mechanism

```
Stage 1: Structural VAE + EEG Encoder
├── Structurally Supervised Variational Autoencoder
│   └── Captures explicit structural geometry
└── Spatiotemporal EEG Encoder
    └── Contrastive learning for visual embedding alignment

Stage 2: ControlNet-Guided Diffusion
├── EEG Feature Integration
├── Structural Guidance via ControlNet
└── High-Fidelity Image Generation
```

### 2. Structural VAE (Structurally Supervised)

```python
class StructuralVAE(nn.Module):
    """VAE with structural supervision for shape-aware encoding."""
    
    def __init__(self, latent_dim=512, structural_dim=256):
        self.encoder = SpatialStructuralEncoder()
        self.structural_head = nn.Sequential(
            nn.Linear(latent_dim, structural_dim),
            nn.ReLU(),
            nn.Linear(structural_dim, structural_dim)
        )
        self.decoder = StructuralDecoder()
    
    def forward(self, x, structural_target):
        # Encode with structural awareness
        mu, logvar = self.encoder(x)
        z = self.reparameterize(mu, logvar)
        
        # Structural supervision
        structural_pred = self.structural_head(z)
        structural_loss = F.mse_loss(structural_pred, structural_target)
        
        # Decode
        recon = self.decoder(z)
        return recon, structural_loss, mu, logvar
```

### 3. Spatiotemporal EEG Encoder

```python
class SpatiotemporalEEGEncoder(nn.Module):
    """EEG encoder with temporal and spatial feature extraction."""
    
    def __init__(self, n_channels=64, n_timepoints=256, n_freq_bands=5):
        # Temporal convolution for time-series features
        self.temporal_conv = nn.Conv1d(n_channels, 128, kernel_size=25, padding=12)
        
        # Spatial attention for channel relationships
        self.spatial_attn = MultiHeadSpatialAttention(n_heads=8)
        
        # Frequency band processing (delta, theta, alpha, beta, gamma)
        self.freq_bands = nn.ModuleList([
            FrequencyBandEncoder(band) for band in ['delta', 'theta', 'alpha', 'beta', 'gamma']
        ])
        
        # Contrastive projection head
        self.projection = ContrastiveProjectionHead(512, 128)
    
    def forward(self, eeg_data):
        # Temporal features
        temp_feat = self.temporal_conv(eeg_data)
        
        # Spatial attention
        spat_feat = self.spatial_attn(temp_feat)
        
        # Multi-band frequency features
        freq_feats = []
        for encoder in self.freq_bands:
            freq_feats.append(encoder(eeg_data))
        freq_feat = torch.cat(freq_feats, dim=-1)
        
        # Fusion and projection
        combined = self.fusion_layer(spat_feat, freq_feat)
        embedding = self.projection(combined)
        
        return embedding
```

### 4. Contrastive Learning Alignment

```python
class EEGVisualContrastiveLoss(nn.Module):
    """NT-Xent loss for EEG-visual embedding alignment."""
    
    def __init__(self, temperature=0.5):
        self.temperature = temperature
    
    def forward(self, eeg_embed, visual_embed):
        # Normalize embeddings
        eeg_embed = F.normalize(eeg_embed, dim=-1)
        visual_embed = F.normalize(visual_embed, dim=-1)
        
        # Compute similarity matrix
        sim_matrix = torch.matmul(eeg_embed, visual_embed.T) / self.temperature
        
        # Positive pairs are diagonal
        labels = torch.arange(len(eeg_embed)).to(eeg_embed.device)
        
        # NT-Xent loss
        loss_i = F.cross_entropy(sim_matrix, labels)
        loss_t = F.cross_entropy(sim_matrix.T, labels)
        
        return (loss_i + loss_t) / 2
```

### 5. ControlNet-Guided Diffusion

```python
class SGDM(nn.Module):
    """Structure-Guided Diffusion Model."""
    
    def __init__(self, base_diffusion, controlnet):
        self.base_diffusion = base_diffusion  # Stable Diffusion or similar
        self.controlnet = controlnet  # Structural conditioning
        self.eeg_encoder = SpatiotemporalEEGEncoder()
    
    def forward(self, eeg_data, structural_condition, timestep):
        # Encode EEG to visual embedding space
        eeg_embed = self.eeg_encoder(eeg_data)
        
        # ControlNet processes structural condition
        control_features = self.controlnet(structural_condition, timestep)
        
        # UNet with EEG embedding and structural guidance
        noise_pred = self.base_diffusion.unet(
            sample=latent,
            timestep=timestep,
            encoder_hidden_states=eeg_embed,
            down_block_additional_residuals=control_features
        )
        
        return noise_pred
```

## Training Pipeline

### Stage 1: EEG-Visual Alignment Pretraining

```python
def train_eeg_visual_alignment(eeg_encoder, vae, dataloader, epochs=100):
    optimizer = AdamW(list(eeg_encoder.parameters()) + list(vae.parameters()), lr=1e-4)
    contrastive_loss = EEGVisualContrastiveLoss()
    
    for epoch in range(epochs):
        for batch in dataloader:
            eeg_data = batch['eeg']  # (B, C, T)
            visual_images = batch['image']  # (B, 3, H, W)
            
            # Encode visual through VAE
            visual_embed = vae.encode(visual_images)
            
            # Encode EEG
            eeg_embed = eeg_encoder(eeg_data)
            
            # Contrastive alignment
            loss = contrastive_loss(eeg_embed, visual_embed)
            
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
```

### Stage 2: Diffusion Model Training

```python
def train_sgdm(sgdm, dataloader, epochs=200):
    optimizer = AdamW(sgdm.parameters(), lr=1e-5)
    
    for epoch in range(epochs):
        for batch in dataloader:
            eeg_data = batch['eeg']
            images = batch['image']
            structural_cond = batch['structural_map']
            
            # Add noise
            noise = torch.randn_like(images)
            timesteps = torch.randint(0, 1000, (images.shape[0],))
            noisy_images = sgdm.base_diffusion.add_noise(images, noise, timesteps)
            
            # Predict noise with EEG guidance
            noise_pred = sgdm(eeg_data, structural_cond, timesteps)
            
            loss = F.mse_loss(noise_pred, noise)
            
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
```

## Implementation Guide

### 1. Data Preparation

```python
class EEGImageDataset(Dataset):
    """Dataset for paired EEG and image data."""
    
    def __init__(self, eeg_dir, image_dir, subjects=None):
        self.eeg_data = load_eeg_data(eeg_dir, subjects)
        self.images = load_images(image_dir)
        
        # Precompute structural conditions (edge maps, segmentation)
        self.structural_conditions = self.compute_structural_maps(self.images)
    
    def compute_structural_maps(self, images):
        """Extract structural information (edges, segments)."""
        structural_maps = []
        for img in images:
            # Edge detection
            edges = cv2.Canny(img, 100, 200)
            # Semantic segmentation (optional)
            segments = segment_image(img)
            structural_maps.append({
                'edges': edges,
                'segments': segments
            })
        return structural_maps
    
    def preprocess_eeg(self, eeg_raw):
        """Standard EEG preprocessing pipeline."""
        # Bandpass filter (1-100 Hz)
        eeg_filtered = bandpass_filter(eeg_raw, 1, 100)
        
        # Artifact removal (ICA or regression-based)
        eeg_cleaned = remove_artifacts(eeg_filtered)
        
        # Normalization
        eeg_normalized = (eeg_cleaned - eeg_cleaned.mean()) / eeg_cleaned.std()
        
        return eeg_normalized
```

### 2. Inference Pipeline

```python
def reconstruct_from_eeg(sgdm, eeg_data, num_inference_steps=50):
    """Generate image from EEG recording."""
    
    # Encode EEG
    eeg_embed = sgdm.eeg_encoder(eeg_data)
    
    # Initialize latent noise
    latents = torch.randn(1, 4, 64, 64)  # SD latent size
    
    # Denoising loop
    for t in tqdm(scheduler.timesteps):
        # ControlNet guidance
        structural_cond = extract_structural_guidance(eeg_data)
        control_feat = sgdm.controlnet(structural_cond, t)
        
        # UNet prediction
        noise_pred = sgdm.base_diffusion.unet(
            latents, t, encoder_hidden_states=eeg_embed,
            down_block_additional_residuals=control_feat
        ).sample
        
        # Step scheduler
        latents = scheduler.step(noise_pred, t, latents).prev_sample
    
    # Decode to image
    image = sgdm.base_diffusion.vae.decode(latents).sample
    
    return image
```

### 3. Cross-Subject Adaptation

```python
class CrossSubjectAdapter(nn.Module):
    """Lightweight adapter for cross-subject generalization."""
    
    def __init__(self, base_encoder, hidden_dim=256):
        super().__init__()
        self.base_encoder = base_encoder
        # Subject-specific adaptation layers
        self.adapter = nn.Sequential(
            nn.Linear(base_encoder.output_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, base_encoder.output_dim)
        )
    
    def forward(self, eeg_data, subject_id=None):
        base_features = self.base_encoder(eeg_data)
        # Apply subject-specific transformation
        adapted_features = self.adapter(base_features)
        return base_features + 0.1 * adapted_features  # Residual connection
```

## Evaluation Metrics

### Quantitative Metrics

```python
def evaluate_sgdm(sgdm, test_dataloader):
    metrics = {
        'ssim': [],      # Structural similarity
        'lpips': [],     # Learned perceptual similarity
        'fid': [],       # Frechet Inception Distance
        'pixel_mse': []  # Pixel-level MSE
    }
    
    for batch in test_dataloader:
        eeg_data = batch['eeg']
        ground_truth = batch['image']
        
        # Generate reconstruction
        reconstructed = reconstruct_from_eeg(sgdm, eeg_data)
        
        # Compute metrics
        metrics['ssim'].append(compute_ssim(reconstructed, ground_truth))
        metrics['lpips'].append(compute_lpips(reconstructed, ground_truth))
        metrics['pixel_mse'].append(F.mse_loss(reconstructed, ground_truth).item())
    
    # Aggregate
    return {k: np.mean(v) for k, v in metrics.items()}
```

### Qualitative Analysis

```python
def analyze_spatiotemporal_patterns(sgdm, eeg_data):
    """Analyze EEG encoding patterns."""
    
    # Extract hierarchical features
    features = sgdm.eeg_encoder.extract_features(eeg_data)
    
    # Visualize spatial patterns
    spatial_attention = features['spatial_attention']
    plt.figure(figsize=(12, 6))
    sns.heatmap(spatial_attention.mean(dim=0).cpu().numpy())
    plt.title('Spatial Attention Patterns')
    
    # Analyze temporal dynamics
    temporal_features = features['temporal']
    for i, band in enumerate(['delta', 'theta', 'alpha', 'beta', 'gamma']):
        plt.subplot(2, 3, i+1)
        plt.plot(temporal_features[band].mean(dim=0).cpu().numpy())
        plt.title(f'{band} Band Activity')
    
    return features
```

## Best Practices

### EEG Data Quality

1. **Preprocessing Pipeline**:
   - Bandpass filter: 1-100 Hz
   - Notch filter: 50/60 Hz for line noise
   - ICA for artifact removal
   - Common average referencing

2. **Channel Selection**:
   - Visual cortex channels (O1, O2, Oz, PO7, PO8)
   - Temporal-parietal channels for semantic processing
   - Remove noisy channels based on variance

3. **Temporal Windows**:
   - Use 0-500ms post-stimulus for early visual processing
   - Extend to 1000ms for semantic content
   - Overlapping windows for continuous decoding

### Model Optimization

1. **Contrastive Learning**:
   - Temperature: 0.5 (tune based on dataset)
   - Batch size: At least 256 for stable contrastive learning
   - Data augmentation for EEG (time shifts, channel dropout)

2. **Diffusion Training**:
   - Start with pretrained Stable Diffusion weights
   - LoRA fine-tuning for efficiency
   - Gradient checkpointing for memory efficiency

3. **ControlNet Design**:
   - Use edge maps + segmentation masks
   - Condition strength: 0.8-1.2 (tune per subject)
   - Multi-scale structural guidance

## Applications

### Brain-Computer Interface

```python
class RealTimeEEGDecoder:
    """Real-time EEG-to-image decoding for BCI."""
    
    def __init__(self, sgdm_model, buffer_size=256):
        self.model = sgdm_model
        self.buffer = CircularBuffer(buffer_size)
        self.preprocessor = EEGPreprocessor()
    
    def process_stream(self, eeg_stream):
        for sample in eeg_stream:
            self.buffer.add(sample)
            
            if self.buffer.is_full():
                # Process window
                eeg_window = self.buffer.get_data()
                eeg_processed = self.preprocessor.process(eeg_window)
                
                # Generate visualization
                with torch.no_grad():
                    image = reconstruct_from_eeg(self.model, eeg_processed)
                
                yield image
```

### Cognitive State Monitoring

```python
def monitor_visual_attention(eeg_data, sgdm, attention_anchors):
    """Monitor attention by comparing EEG to anchor images."""
    
    # Reconstruct current mental image
    current_image = reconstruct_from_eeg(sgdm, eeg_data)
    
    # Compare to attention anchors
    similarities = {}
    for name, anchor_img in attention_anchors.items():
        sim = compute_semantic_similarity(current_image, anchor_img)
        similarities[name] = sim
    
    # Determine focus
    focus = max(similarities, key=similarities.get)
    confidence = similarities[focus]
    
    return focus, confidence, similarities
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Blurry reconstructions | Increase diffusion steps, check ControlNet conditioning |
| Cross-subject poor performance | Use subject adaptation layers, increase training data |
| EEG noise sensitivity | Improve preprocessing, add robust training augmentations |
| Semantic drift | Ensure alignment loss weight is sufficient |
| Slow inference | Use DDIM scheduler, enable model quantization |

## References

- Lian et al. (2026). Structure-Guided Diffusion Model for EEG-Based Visual Cognition Reconstruction. arXiv:2604.22649
- Rombach et al. (2022). High-Resolution Image Synthesis with Latent Diffusion Models. CVPR.
- Zhang et al. (2023). Adding Conditional Control to Text-to-Image Diffusion Models. ICCV.

## Keywords

EEG visual reconstruction, brain decoding, diffusion model, ControlNet, neural decoding, brain-computer interface, spatiotemporal encoding, contrastive learning, structural guidance
