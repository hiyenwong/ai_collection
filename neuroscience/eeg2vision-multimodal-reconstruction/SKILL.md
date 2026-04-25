---
name: eeg2vision-multimodal-reconstruction
description: "EEG2Vision - Modular end-to-end framework for reconstructing 2D visual stimuli from EEG signals. Supports multiple EEG channel configurations (128, 64, 32, 24 channels) with prompt-guided post-reconstruction enhancement. Enables visual decoding from non-invasive EEG for cognitive neuroscience and brain-computer interfaces. Activation: eeg2vision, eeg reconstruction, visual decoding, brain computer interface, image generation from eeg."
---

# EEG2Vision: Multimodal EEG-to-Image Reconstruction

## Overview

**EEG2Vision** is a modular, end-to-end framework for **reconstructing visual stimuli from non-invasive EEG signals**. It systematically evaluates reconstruction performance across different EEG resolutions (128, 64, 32, and 24 channels) and enhances visual quality through a **prompt-guided post-reconstruction boosting module**.

**Core Innovation**: First systematic evaluation of visual reconstruction across EEG channel configurations with diffusion-based enhancement.

## Key Features

### 1. Multi-Resolution EEG Support
- **128 channels**: Dense coverage, highest fidelity
- **64 channels**: Standard research setup
- **32 channels**: Mobile/wearable configurations
- **24 channels**: Consumer-grade devices

### 2. Modular Architecture
- **EEG Encoder**: Channel-adaptive feature extraction
- **Latent Mapping**: EEG to image latent space
- **Generator**: Diffusion-based image synthesis
- **Enhancement**: Prompt-guided post-processing

### 3. Prompt-Guided Enhancement
- **Semantic Guidance**: Text prompts improve reconstruction
- **Diffusion Boosting**: Iterative refinement
- **Quality Metrics**: SSIM, PSNR, FID evaluation

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│              EEG2Vision Architecture                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  EEG Input (Variable Channels)                                  │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  128ch │ 64ch │ 32ch │ 24ch                             │   │
│  └─────────────────────────────────────────────────────────┘   │
│                            │                                    │
│                            ▼                                    │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │              Channel-Adaptive Encoder                    │   │
│  │  - Spatial attention for electrode locations             │   │
│  │  - Temporal convolution for time-frequency               │   │
│  │  - Cross-channel correlation learning                    │   │
│  └─────────────────────────┬───────────────────────────────┘   │
│                            │                                    │
│                            ▼                                    │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │              EEG Feature Extractor                       │   │
│  │  Multi-scale temporal features:                          │   │
│  │  ┌────────┐ ┌────────┐ ┌────────┐                       │   │
│  │  │  Delta │ │  Theta │ │  Alpha │ ...                    │   │
│  │  │ 1-4Hz  │ │ 4-8Hz  │ │ 8-13Hz │                       │   │
│  │  └────────┘ └────────┘ └────────┘                       │   │
│  └─────────────────────────┬───────────────────────────────┘   │
│                            │                                    │
│                            ▼                                    │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │              Latent Space Mapping                        │   │
│  │  EEG features → Image latent space                       │   │
│  │  (Bridging the modality gap)                             │   │
│  └─────────────────────────┬───────────────────────────────┘   │
│                            │                                    │
│                            ▼                                    │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │              Diffusion Image Generator                   │   │
│  │  Latent Diffusion Model (LDM)                            │   │
│  │  - UNet with cross-attention                             │   │
│  │  - EEG conditioning via cross-attention                  │   │
│  │  - Iterative denoising process                           │   │
│  └─────────────────────────┬───────────────────────────────┘   │
│                            │                                    │
│                            ▼                                    │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │         Prompt-Guided Enhancement                        │   │
│  │  - Semantic prompt extraction from EEG                   │   │
│  │  - Diffusion-based refinement                            │   │
│  │  - Multi-step boosting                                   │   │
│  └─────────────────────────┬───────────────────────────────┘   │
│                            │                                    │
│                            ▼                                    │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │              Reconstructed Image                         │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Workflow

### Step 1: EEG Preprocessing

```python
from eeg2vision import EEGPreprocessor

# Initialize preprocessor for specific channel configuration
preprocessor = EEGPreprocessor(
    n_channels=64,  # 128, 64, 32, or 24
    fs=256,         # Sampling frequency (Hz)
    filter_band=(0.5, 45),  # Bandpass filter
    notch_freq=50,  # Line noise removal
    segment_length=512  # 2 seconds at 256Hz
)

# Load EEG data
eeg_data = preprocessor.load('subject_eeg.set')

# Preprocess
eeg_processed = preprocessor.apply(
    eeg_data,
    steps=['filter', 'notch', 'normalize', 'segment']
)

print(f"Processed EEG shape: {eeg_processed.shape}")
# Output: (n_trials, n_channels, n_times)
```

### Step 2: Channel Configuration Handling

```python
from eeg2vision import ChannelAdapter

# Adapt to different channel configurations
adapter = ChannelAdapter(
    target_channels=64,
    electrode_positions='standard_1020'
)

# If input has different channels
if eeg_processed.shape[1] != 64:
    eeg_adapted = adapter.interpolate(
        eeg_processed,
        source_positions=source_positions
    )
else:
    eeg_adapted = eeg_processed
```

### Step 3: EEG Feature Extraction

```python
from eeg2vision import EEGEncoder

# Initialize encoder
encoder = EEGEncoder(
    n_channels=64,
    n_times=512,
    n_bands=5,  # delta, theta, alpha, beta, gamma
    hidden_dim=512
)

# Extract features
eeg_features = encoder(eeg_adapted)

# Features include:
# - Spatial patterns (topography)
# - Spectral features (band power)
# - Temporal dynamics (ERP-like)
print(f"EEG features shape: {eeg_features.shape}")
```

### Step 4: Latent Space Mapping

```python
from eeg2vision import EEGToLatent

# Initialize mapper
mapper = EEGToLatent(
    eeg_dim=512,
    latent_dim=4 * 64 * 64,  # For 256x256 images at 1/4 resolution
    hidden_dims=[1024, 512, 256]
)

# Map EEG to image latent space
latent_code = mapper(eeg_features)
latent_image = latent_code.view(4, 64, 64)  # (channels, height, width)
```

### Step 5: Image Generation

```python
from eeg2vision import EEGDiffusionGenerator
from diffusers import DDIMScheduler

# Initialize diffusion model
generator = EEGDiffusionGenerator(
    latent_dim=4 * 64 * 64,
    num_inference_steps=50,
    guidance_scale=7.5
)

# Generate image
with torch.no_grad():
    generated_image = generator(
        latent_code=latent_code,
        eeg_condition=eeg_features,
        num_inference_steps=50
    )

print(f"Generated image shape: {generated_image.shape}")
# Output: (3, 256, 256)
```

### Step 6: Prompt-Guided Enhancement

```python
from eeg2vision import PromptGuidedEnhancement
from transformers import CLIPModel, CLIPTokenizer

# Initialize enhancement module
enhancer = PromptGuidedEnhancement(
    clip_model='openai/clip-vit-base-patch32',
    diffusion_steps=20
)

# Extract semantic prompt from EEG
semantic_prompt = enhancer.extract_prompt(eeg_features)
print(f"Extracted prompt: {semantic_prompt}")
# Example: "a red car on a street"

# Enhance with diffusion boosting
enhanced_image = enhancer.boost(
    image=generated_image,
    prompt=semantic_prompt,
    num_steps=20,
    strength=0.3  # Enhancement strength
)
```

### Step 7: Evaluation

```python
from eeg2vision import evaluate_reconstruction

# Load ground truth image
ground_truth = load_image('stimulus_image.jpg')

# Evaluate
metrics = evaluate_reconstruction(
    generated=enhanced_image,
    ground_truth=ground_truth,
    metrics=['ssim', 'psnr', 'lpips', 'fid']
)

print("Reconstruction Metrics:")
print(f"  SSIM: {metrics['ssim']:.4f}")
print(f"  PSNR: {metrics['psnr']:.2f} dB")
print(f"  LPIPS: {metrics['lpips']:.4f}")
print(f"  FID: {metrics['fid']:.2f}")
```

## Training

### Stage 1: EEG Encoder Training

```python
from eeg2vision import EEG2VisionTrainer

# Initialize trainer
trainer = EEG2VisionTrainer(
    encoder=encoder,
    mapper=mapper,
    generator=generator,
    lr=1e-4,
    batch_size=32
)

# Training loop
for epoch in range(num_epochs):
    for batch in train_loader:
        eeg = batch['eeg'].to(device)
        image = batch['image'].to(device)
        
        # Forward pass
        reconstructed = model(eeg)
        
        # Reconstruction loss
        loss = F.mse_loss(reconstructed, image)
        
        # Perceptual loss
        perceptual_loss = perceptual_loss_fn(reconstructed, image)
        
        # Total loss
        total_loss = loss + 0.1 * perceptual_loss
        
        trainer.step(total_loss)
```

### Stage 2: Diffusion Fine-tuning

```python
# Fine-tune diffusion model with EEG conditioning
diffusion_trainer = DiffusionTrainer(
    generator=generator,
    noise_scheduler=DDIMScheduler(),
    lr=1e-5
)

for epoch in range(num_epochs):
    for batch in train_loader:
        eeg = batch['eeg']
        image = batch['image']
        
        # Add noise
        noise = torch.randn_like(image)
        timesteps = torch.randint(0, 1000, (image.shape[0],))
        noisy_image = scheduler.add_noise(image, noise, timesteps)
        
        # Predict noise with EEG conditioning
        pred_noise = generator(noisy_image, timesteps, eeg)
        
        # Loss
        loss = F.mse_loss(pred_noise, noise)
        
        diffusion_trainer.step(loss)
```

## Multi-Resolution Evaluation

```python
from eeg2vision import MultiResolutionEvaluator

# Evaluate across channel configurations
configs = [128, 64, 32, 24]
evaluator = MultiResolutionEvaluator()

results = {}
for n_ch in configs:
    # Load model for this configuration
    model = load_model(f'eeg2vision_{n_ch}ch.pth')
    
    # Evaluate
    results[n_ch] = evaluator.evaluate(
        model=model,
        test_loader=get_test_loader(n_ch),
        metrics=['ssim', 'psnr', 'lpips']
    )

# Compare results
import pandas as pd
df = pd.DataFrame(results).T
print(df)

# Typical results:
#      ssim  psnr   lpips
# 128  0.65  18.5   0.25
# 64   0.62  17.8   0.28
# 32   0.55  16.2   0.35
# 24   0.50  15.0   0.42
```

## Use Cases

1. **Brain-Computer Interfaces**: Visualize mental imagery
2. **Cognitive Neuroscience**: Study visual processing
3. **Dream Decoding**: Reconstruct visual dream content
4. **Communication Aid**: For locked-in patients
5. **Memory Research**: Visualize remembered scenes

## Research Paper Reference

**Title**: EEG2Vision: A Multimodal EEG-Based Framework for 2D Visual Reconstruction in Cognitive Neuroscience  
**Authors**: Emanuele Balloni, Emanuele Frontoni, Chiara Matti, et al.  
**arXiv**: 2604.08063v1  
**Published**: 2026-04-09  
**Categories**: cs.CV

**Key Contributions**:
1. First systematic evaluation across EEG channel configurations
2. Modular end-to-end architecture
3. Prompt-guided post-reconstruction enhancement
4. Support for low-density EEG (24 channels)

## References

- See [references/paper-details.md](references/paper-details.md) for full paper analysis
- See [references/diffusion-models.md](references/diffusion-models.md) for LDM background
