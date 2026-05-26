---
name: mindalign-eeg-visual-decoding
description: Tri-modal contrastive framework (EEG, vision, language) for zero-shot visual decoding. Achieves 54.1% Top-1 accuracy on 200-way benchmark, massively exceeding prior baselines. Use for brain-computer interface visual reconstruction, EEG-based image retrieval, non-invasive neural decoding.
tags: [eeg, visual-decoding, contrastive-learning, brain-computer-interface, zero-shot, multimodal, neuroscience, language-grounding]
version: "1.0"
source: "arXiv:2605.24523"
---

# MindAlign: Tri-Modal EEG-Vision-Language Visual Decoding

## Overview

**MindAlign** introduces a tri-modal contrastive framework that aligns EEG brain signals, visual images, and language descriptions in a unified latent space for **zero-shot visual decoding**. 

Key breakthrough: **54.1% Top-1 accuracy** on 200-way zero-shot benchmark vs prior SOTA of 32.4% (+67% relative improvement).

## When to Use

- Zero-shot visual decoding from EEG signals
- Brain-computer interface image retrieval
- Non-invasive neural representation alignment
- Multimodal brain signal analysis (EEG + vision + text)
- Studying neural correlates of visual object recognition
- Cross-subject generalization of visual decoders

## Architecture

```
EEG Signal (T×C) → EEG Encoder → e_eeg ∈ R^d
                                      ↓
Image → CLIP/CN-CLIP → e_img ∈ R^d  → Unified Latent Space (contrastive alignment)
                                      ↑
Text Description (LLM-generated) → e_txt ∈ R^d
```

### Two-Stage Design

**Stage 1: Masked Reconstruction Pre-training**
```python
# Pre-train EEG encoder without labels
# Mask random EEG segments → reconstruct
# Learns spatio-temporal regularities that transfer robustly

class EEGMaskedAutoencoder(nn.Module):
    def __init__(self, n_channels=128, n_timepoints=512, d_model=512):
        self.channel_embed = nn.Linear(1, d_model)
        self.time_embed = nn.Linear(1, d_model)
        self.transformer = TransformerEncoder(d_model, n_heads=8, n_layers=6)
        self.decoder = TransformerDecoder(d_model, n_heads=8, n_layers=4)
    
    def forward(self, eeg, mask_ratio=0.75):
        # Patch EEG into channel×time tokens
        tokens = self.tokenize(eeg)
        # Mask 75% of tokens
        visible_tokens, mask_idx = self.random_mask(tokens, mask_ratio)
        # Encode visible + reconstruct masked
        latent = self.transformer(visible_tokens)
        reconstructed = self.decoder(latent, mask_idx)
        loss = F.mse_loss(reconstructed, tokens[mask_idx])
        return loss, latent
```

**Stage 2: Tri-Modal Contrastive Alignment**
```python
class MindAlignTraining(nn.Module):
    def __init__(self, eeg_encoder, image_encoder, text_encoder, d=512):
        self.eeg_enc = eeg_encoder  # from Stage 1
        self.img_enc = image_encoder  # CN-CLIP (compact embedding geometry!)
        self.txt_enc = text_encoder  # LLM-generated descriptions
        
        # Subject-specific adaptation layers
        self.subject_adapters = nn.ModuleDict({
            f'subj_{i}': nn.Linear(d, d) for i in range(n_subjects)
        })
    
    def forward(self, eeg, images, texts, subject_ids):
        # EEG encoding with subject adaptation
        e_eeg = self.eeg_enc(eeg)
        e_eeg = self.subject_adapters[f'subj_{subject_ids[0]}'](e_eeg)
        
        e_img = self.img_enc(images)
        e_txt = self.txt_enc(texts)
        
        # Tri-modal contrastive loss
        loss = self.contrastive_loss_trimodal(e_eeg, e_img, e_txt)
        return loss
    
    def contrastive_loss_trimodal(self, e_eeg, e_img, e_txt, tau=0.07):
        # Normalize embeddings
        e_eeg = F.normalize(e_eeg, dim=-1)
        e_img = F.normalize(e_img, dim=-1)
        e_txt = F.normalize(e_txt, dim=-1)
        
        # EEG-Image alignment (primary signal)
        loss_ei = self.clip_loss(e_eeg, e_img, tau)
        
        # Text as semantic regularizer (secondary, lower weight)
        loss_et = self.clip_loss(e_eeg, e_txt, tau)
        loss_it = self.clip_loss(e_img, e_txt, tau)
        
        # Text supervision regularizes without overwhelming EEG-image signal
        alpha = 0.3  # text regularization weight
        return loss_ei + alpha * (loss_et + loss_it)
```

## EEG Encoder Architecture

### Key Components

```python
class EEGEncoder(nn.Module):
    def __init__(self, n_channels=128, d_model=512):
        # 1. Graph-attention over EEG channels
        self.channel_graph_attn = GraphAttentionLayer(
            n_channels, d_model,
            adjacency='functional_connectivity'  # from prior neuroscience
        )
        
        # 2. Temporal-spatial convolutional embeddings
        self.spatial_conv = nn.Conv1d(n_channels, d_model, kernel_size=1)
        self.temporal_conv = nn.Conv1d(d_model, d_model, 
                                        kernel_size=25, padding=12)
        
        # 3. Subject-specific normalization
        self.subject_norm = SubjectBatchNorm(d_model, n_subjects)
    
    def forward(self, eeg, subject_id):
        # eeg: (B, C, T) - batch, channels, timepoints
        
        # Spatial processing with graph attention
        h_spatial = self.channel_graph_attn(eeg)  # (B, C, d)
        
        # Temporal convolution
        h_temporal = self.temporal_conv(
            self.spatial_conv(eeg)
        )  # (B, d, T)
        
        # Pool over time → single embedding
        h = h_temporal.mean(dim=-1)  # (B, d)
        
        # Subject normalization
        h = self.subject_norm(h, subject_id)
        
        return h
```

## LLM Text Generation

Critical insight: **Generate textual descriptions using LLM for each image class**

```python
def generate_image_descriptions(image_classes, model='gpt-4'):
    """Generate rich textual descriptions for contrastive training."""
    descriptions = {}
    
    template = """Describe the image of '{class_name}' in detail, 
    including:
    1. Visual appearance and shape
    2. Color and texture
    3. Typical context/scene
    4. Distinctive features
    Keep description factual and visually-grounded (3-4 sentences)."""
    
    for cls in image_classes:
        response = model.generate(template.format(class_name=cls))
        descriptions[cls] = response
    
    return descriptions

# Example descriptions used as semantic regularizer
# "An apple is a round fruit with smooth red/green skin..."
# "A hammer has a metal head attached to a wooden handle..."
```

## Key Finding: Compact Embeddings Win

```python
# CRITICAL: CN-CLIP (compact) >> CLIP ViT-L/14 (large)
# Counter-intuitive but important for EEG-image alignment

image_encoders_comparison = {
    'CN-CLIP (compact)': {'top1': 54.1, 'top5': 83.4},
    'CLIP ViT-B/32': {'top1': 41.2, 'top5': 72.1},  
    'CLIP ViT-L/14': {'top1': 38.7, 'top5': 69.3},  # WORSE despite larger!
    'prior_SOTA': {'top1': 32.4, 'top5': 64.0}
}

# Why compact wins:
# - EEG embedding dimension is naturally compact
# - Compact image embedding geometry → better alignment with EEG space
# - Large models have "too much" visual detail EEG can't encode
```

## Benchmark Results

| Method | Top-1 (200-way) | Top-5 (200-way) |
|--------|-----------------|-----------------|
| EEGClip (2022) | 15.6% | 42.3% |
| BraVL (2023) | 24.8% | 56.1% |
| ATMS (2024) | 32.4% | 64.0% |
| **MindAlign (2026)** | **54.1%** | **83.4%** |

Significance: Wilcoxon p < 0.01 vs all baselines, confirmed on Things-EEG2 and Things-MEG datasets.

## Implementation Steps

### 1. Data Preparation
```python
# Load Things-EEG2 dataset
from datasets import load_dataset

dataset = load_dataset('things-eeg2')
# 40 subjects × 200 test objects × 80 trials each

# Preprocess EEG
def preprocess_eeg(raw_eeg, sfreq=1000, target_sfreq=250):
    # Band-pass filter 0.1-100 Hz
    filtered = mne.filter.filter_data(raw_eeg, sfreq, 0.1, 100)
    # Downsample
    resampled = mne.filter.resample(filtered, up=target_sfreq, down=sfreq)
    # Epoch: -0.2 to 0.8s post-stimulus
    epochs = epoch_data(resampled, events, tmin=-0.2, tmax=0.8)
    return epochs
```

### 2. Stage 1 Pre-training
```python
model = EEGMaskedAutoencoder(n_channels=128, n_timepoints=250)
optimizer = AdamW(model.parameters(), lr=1e-4, weight_decay=0.01)

for epoch in range(100):
    for eeg_batch in unlabeled_eeg_loader:
        loss, _ = model(eeg_batch, mask_ratio=0.75)
        loss.backward()
        optimizer.step()
```

### 3. Stage 2 Contrastive Training
```python
eeg_encoder = model.encoder  # from Stage 1
img_encoder = load_cn_clip()   # CN-CLIP
txt_encoder = load_text_encoder()

mindalign = MindAlignTraining(eeg_encoder, img_encoder, txt_encoder)

# Generate text descriptions
descriptions = generate_image_descriptions(all_image_classes)

for epoch in range(50):
    for eeg, images, subject_ids in labeled_loader:
        texts = [descriptions[img_class] for img_class in image_classes]
        loss = mindalign(eeg, images, texts, subject_ids)
        loss.backward()
```

### 4. Zero-Shot Decoding
```python
def zero_shot_decode(eeg_trial, image_gallery, model):
    """
    Given an EEG trial, find the most similar image from gallery.
    """
    e_eeg = model.eeg_enc(eeg_trial)  # (d,)
    e_imgs = model.img_enc(image_gallery)  # (N, d)
    
    similarities = F.cosine_similarity(e_eeg.unsqueeze(0), e_imgs)
    top_k_idx = similarities.topk(5).indices
    
    return image_gallery[top_k_idx]
```

## Neurophysiological Alignment

The paper validates that decoding patterns match established neuroscience:

```python
# Visual processing stages reflected in EEG timing:
# 50-100ms: early visual features (low-level)
# 100-200ms: object recognition (mid-level)
# 200-500ms: semantic categorization (high-level)

# MindAlign's temporal attention peaks align with these windows
temporal_importance = analyze_temporal_attention(model)
# Shows peak at ~150ms (N170) and ~300ms (P300) - matches neuroscience literature
```

## Pitfalls

- **Subject variability**: EEG varies enormously across subjects; subject adapters are critical
- **CN-CLIP key**: Using larger/different image encoders significantly degrades performance
- **Text balance**: Too much text weight overwhelms EEG-image signal (α=0.3 optimal)
- **Masked pretraining**: Stage 1 without sufficient unlabeled data will hurt Stage 2
- **Things-EEG2 specific**: Timing window (-0.2 to 0.8s) tuned for this dataset; adjust for other paradigms
- **Compact geometry rule**: Always test multiple image encoders; compact usually beats large for EEG alignment

## Extensions

```python
# Extend to continuous video decoding
# Extend to MEG (paper validates on Things-MEG)
# Multi-subject generalization without subject adapters (cross-subject zero-shot)
# Real-time BCI applications (streaming EEG decoding)
```

## Key References

- **Primary**: Chen et al. (2026). "MindAlign: Bridging EEG, Vision, and Language for Zero-Shot Visual Decoding." arXiv:2605.24523
- Things-EEG2 dataset: Gifford et al. (2022)
- CN-CLIP: Yang et al. (2022)
- CLIP: Radford et al. (2021)
- Code: https://github.com/anon-eeg/eeg_image_decoding

## Activation Keywords

EEG visual decoding, brain-computer interface, zero-shot image retrieval, contrastive learning, tri-modal alignment, EEG-vision-language, Things-EEG2, masked autoencoder pretraining, neural image reconstruction, non-invasive BCI, MindAlign, EEG zero-shot
