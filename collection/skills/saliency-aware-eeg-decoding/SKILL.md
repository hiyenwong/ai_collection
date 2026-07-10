---
name: saliency-aware-eeg-decoding
description: "SIMON: Saliency-aware Integrative Multi-view Object-centric Neural Decoding for zero-shot EEG-to-image retrieval. Uses foreground segmentation, saliency prediction, Saliency-Aware Sampling (SAS), and foveated multi-view integration to overcome center-bias limitations in EEG-to-image retrieval. Trigger words: saliency-aware EEG decoding, SIMON, EEG-to-image retrieval, foveated view, multi-view neural decoding, Saliency-Aware Sampling, object-centric neural decoding, zero-shot EEG image, THINGS-EEG benchmark, geometric-semantic dissociation."
category: research
source:
  paper: "SIMON: Saliency-aware Integrative Multi-view Object-centric Neural Decoding"
  authors:
    - "YuSheng Lin"
    - "Ji-Hwa Tsai"
    - "Chun-Shu Wei"
  arxiv: "2605.00401"
  date: "2026-05-01"
  fields:
    - cs.CV
    - q-bio.NC
activation_keywords:
  en:
    - saliency-aware EEG decoding
    - SIMON
    - EEG-to-image retrieval
    - foveated view
    - multi-view neural decoding
    - Saliency-Aware Sampling
    - object-centric neural decoding
    - zero-shot EEG image
    - THINGS-EEG benchmark
    - geometric-semantic dissociation
    - EEG visual decoding
    - saliency prediction EEG
    - center bias EEG
    - foreground segmentation neural decoding
version: "1.0.0"
---

# SIMON: Saliency-aware Integrative Multi-view Object-centric Neural Decoding

> **Reference:** Lin, Y., Tsai, J.-H., & Wei, C.-S. *SIMON: Saliency-aware Integrative Multi-view Object-centric Neural Decoding.* arXiv:2605.00401 [cs.CV, q-bio.NC] (2026).
> **Code:** https://github.com/simonlink666/SIMON

## Overview

SIMON is a **saliency-aware multi-view framework for zero-shot EEG-to-image retrieval** that addresses a fundamental limitation in existing neural decoding methods: the assumption of fixed, center-focused viewing. This center bias creates a **geometric-semantic dissociation** between visual features and EEG responses, because human attention is content-driven rather than spatially uniform.

SIMON overcomes this by combining **foreground segmentation** and **saliency prediction** to select informative fixation centers, generating **foveated views** that emphasize object regions while suppressing background clutter. The framework achieves state-of-the-art performance on the THINGS-EEG benchmark in both intra-subject and inter-subject settings.

## The Problem: Center Bias in EEG-to-Image Retrieval

### The Geometric-Semantic Dissociation

Traditional EEG-to-image retrieval methods assume subjects look at the **center** of images during viewing. This creates a fundamental mismatch:

```
Center-bias assumption:    [  image center  ]
Actual human attention:    [    *object*     ]  ← attention follows salient content
Dissociation:              features ≠ EEG responses
```

**Why this matters:**
- Visual cortex responses are driven by **what** is attended, not **where** it is on screen
- Objects of interest rarely align with image centers
- Center-focused feature extraction misses salient object regions
- Background clutter dilutes the visual representation

### Consequences

| Issue | Impact on Decoding |
|---|---|
| Center-focused cropping | Misses off-center objects critical to EEG response |
| Uniform feature extraction | Background noise dilutes object-relevant signals |
| Fixed receptive field | Cannot adapt to content-driven attention shifts |
| Single-view representation | Loses multi-scale object information |

---

## Methodology

### 1. Foreground Segmentation + Saliency Prediction Pipeline

SIMON first processes each candidate image through two parallel analysis streams:

```
Input Image
    ├──► Foreground Segmentation ──► Object masks (binary regions)
    └──► Saliency Prediction ───────► Saliency map (attention weights)
                    │
                    ▼
           Combined Selection Map
```

**Foreground Segmentation:**
- Identifies discrete object regions within the image
- Produces binary masks separating foreground objects from background
- Reduces background clutter that would otherwise dilute visual features

**Saliency Prediction:**
- Estimates which regions attract human visual attention
- Produces a continuous saliency map over the image
- Prioritizes semantically informative regions for sampling

### 2. Saliency-Aware Sampling (SAS)

SAS selects fixation centers by combining foreground and saliency information:

```python
class SaliencyAwareSampling:
    """
    Selects fixation centers by combining foreground segmentation
    and saliency prediction to guide foveated view generation.
    """
    def __init__(self, foreground_model, saliency_model,
                 n_fixations=5, sampling_mode='weighted'):
        self.foreground_model = foreground_model
        self.saliency_model = saliency_model
        self.n_fixations = n_fixations
        self.sampling_mode = sampling_mode

    def __call__(self, image):
        # Step 1: Get foreground object masks
        fg_mask = self.foreground_model(image)

        # Step 2: Get saliency prediction map
        saliency_map = self.saliency_model(image)

        # Step 3: Combine into weighted selection map
        # Foreground regions are up-weighted, background suppressed
        selection_map = self._combine_maps(fg_mask, saliency_map)

        # Step 4: Sample fixation centers from selection map
        fixations = self._sample_fixations(
            selection_map,
            n=self.n_fixations,
            mode=self.sampling_mode
        )

        return fixations, selection_map

    def _combine_maps(self, fg_mask, saliency_map):
        """Foreground-weighted saliency combination."""
        # Boost saliency within foreground regions
        combined = saliency_map * (1.0 + fg_mask.weight_boost)
        # Suppress background
        combined = combined * (fg_mask + epsilon)
        return combined / combined.sum()

    def _sample_fixations(self, selection_map, n, mode):
        """Sample n fixation centers from the selection map."""
        if mode == 'weighted':
            # Probabilistic sampling proportional to saliency
            coords = np.unravel_index(
                np.random.choice(
                    selection_map.size,
                    size=n,
                    p=selection_map.flatten(),
                    replace=False
                ),
                selection_map.shape
            )
        elif mode == 'topk':
            # Select highest-saliency locations
            coords = np.unravel_index(
                np.argsort(selection_map.flatten())[-n:],
                selection_map.shape
            )
        return coords
```

**Sampling Granularity Trade-offs:**

| Granularity | Fixations | Pros | Cons |
|---|---|---|---|
| Coarse | 3-4 | Fast, less redundancy | May miss details |
| Medium | 5-7 | Balanced coverage | Moderate compute |
| Fine | 8-12 | Comprehensive | Redundant views, slower |

### 3. Foveated View Generation

For each fixation center, SIMON generates a foveated view that mimics human visual acuity — high resolution at the fixation point, decreasing toward periphery:

```python
def create_foveated_view(image, fixation_center,
                         center_size=128, peripheral_size=224,
                         falloff='gaussian'):
    """
    Generate a foveated view centered on a fixation point.

    Creates a multi-resolution crop that emphasizes the fixation
    region with higher effective resolution while maintaining
    peripheral context.
    """
    cy, cx = fixation_center

    # Center crop (high-acuity foveal region)
    center_crop = crop_center(image, cy, cx, center_size)

    # Peripheral crop (broader context)
    peripheral_crop = crop_center(image, cy, cx, peripheral_size)

    # Create Gaussian attention mask (center-weighted)
    y, x = np.mgrid[:peripheral_size, :peripheral_size]
    center_y, center_x = peripheral_size // 2, peripheral_size // 2
    sigma = peripheral_size / 4.0
    mask = np.exp(-((x - center_x)**2 + (y - center_y)**2) / (2 * sigma**2))

    # Apply mask to create foveated effect
    foveated = peripheral_crop * mask[..., np.newaxis]

    # Blend center detail with foveated periphery
    blended = blend_views(center_crop, foveated)

    return blended
```

**View Characteristics:**
- **Foveal region**: High-resolution, detail-preserving center crop
- **Parafoveal region**: Gradually decreasing resolution
- **Peripheral region**: Context maintained but de-emphasized
- **Result**: Each view emphasizes the object region while suppressing background

### 4. Multi-View Integration Architecture

SIMON integrates information from multiple foveated views into a unified representation:

```
                    ┌─────────────────────┐
                    │   Candidate Image    │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │  SAS (5-7 fixations)│
                    └──────────┬──────────┘
                               │
            ┌──────────────────┼──────────────────┐
            │                  │                  │
     ┌──────▼──────┐   ┌──────▼──────┐   ┌──────▼──────┐
     │ View 1      │   │ View 2      │   │ View N      │
     │ (foveated)  │   │ (foveated)  │   │ (foveated)  │
     └──────┬──────┘   └──────┬──────┘   └──────┬──────┘
            │                  │                  │
     ┌──────▼──────┐   ┌──────▼──────┐   ┌──────▼──────┐
     │ Visual Enc. │   │ Visual Enc. │   │ Visual Enc. │
     │ (e.g., CLIP)│   │ (shared)    │   │ (shared)    │
     └──────┬──────┘   └──────┬──────┘   └──────┬──────┘
            │                  │                  │
            └──────────────────┼──────────────────┘
                               │
                    ┌──────────▼──────────┐
                    │  View Aggregation   │
                    │  (mean / attn /     │
                    │   learned pooling)  │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │  Unified Image      │
                    │  Embedding          │
                    └─────────────────────┘
```

**Aggregation Strategies:**

```python
class MultiViewAggregator(nn.Module):
    """Aggregates embeddings from multiple foveated views."""

    def __init__(self, dim=768, method='attention'):
        super().__init__()
        self.method = method
        if method == 'attention':
            self.attention = nn.MultiheadAttention(dim, num_heads=8)
            self.query = nn.Parameter(torch.randn(1, 1, dim))
        elif method == 'learned_pool':
            self.pool = nn.Sequential(
                nn.Linear(dim, dim),
                nn.GELU(),
                nn.Linear(dim, dim)
            )

    def forward(self, view_embeddings):
        """
        Args:
            view_embeddings: [n_views, batch, dim]
        Returns:
            aggregated: [batch, dim]
        """
        if self.method == 'mean':
            return view_embeddings.mean(dim=0)

        elif self.method == 'attention':
            # Cross-attention with learnable query
            attn_out, _ = self.attention(
                self.query.expand(-1, view_embeddings.size(1), -1),
                view_embeddings,
                view_embeddings
            )
            return attn_out.squeeze(0)

        elif self.method == 'learned_pool':
            pooled = self.pool(view_embeddings)
            return pooled.mean(dim=0)
```

### 5. Zero-Shot EEG-to-Image Retrieval

The retrieval pipeline matches EEG signals to candidate images without task-specific fine-tuning:

```python
class SIMONRetrieval:
    """Zero-shot EEG-to-image retrieval using SIMON framework."""

    def __init__(self, eeg_encoder, visual_encoder,
                 sas_module, view_aggregator, projection_dim=768):
        self.eeg_encoder = eeg_encoder       # EEG → embedding
        self.visual_encoder = visual_encoder  # Image view → embedding
        self.sas = sas_module                # Saliency-Aware Sampling
        self.aggregator = view_aggregator     # Multi-view fusion
        # Linear projection to shared space (learned during training)
        self.eeg_proj = nn.Linear(eeg_encoder.output_dim, projection_dim)
        self.img_proj = nn.Linear(visual_encoder.output_dim, projection_dim)

    def encode_eeg(self, eeg_signal):
        """Encode EEG signal into shared embedding space."""
        raw_emb = self.eeg_encoder(eeg_signal)
        return self.eeg_proj(raw_emb)

    def encode_image(self, image):
        """Encode image via saliency-aware multi-view pipeline."""
        # SAS selects fixation centers
        fixations, saliency_map = self.sas(image)

        # Generate foveated views
        views = [create_foveated_view(image, f) for f in fixations]

        # Encode each view
        view_embs = [self.visual_encoder(v) for v in views]
        view_embs = torch.stack(view_embs, dim=0)  # [n_views, batch, dim]

        # Aggregate multi-view embeddings
        aggregated = self.aggregator(view_embs)

        return self.img_proj(aggregated)

    def retrieve(self, query_eeg, candidate_images, top_k=1):
        """Retrieve top-k matching images for a query EEG."""
        # Encode query
        q_emb = self.encode_eeg(query_eeg)  # [batch, dim]

        # Encode all candidates
        c_embs = torch.stack([
            self.encode_image(img) for img in candidate_images
        ], dim=0)  # [n_candidates, dim]

        # Compute similarity scores
        scores = cosine_similarity(q_emb.unsqueeze(1), c_embs)  # [batch, n_candidates]

        # Return top-k indices
        top_k_idx = torch.topk(scores, k=top_k, dim=-1).indices
        return top_k_idx
```

---

## Performance on THINGS-EEG Benchmark

### Main Results

| Setting | Metric | SIMON | Previous Best |
|---|---|---|---|
| **Intra-subject** | Top-1 Accuracy | **69.7%** | ~64% |
| **Inter-subject** | Top-1 Accuracy | **19.6%** | ~15% |

**Dataset:** THINGS-EEG — large-scale EEG dataset with natural image stimuli, multiple subjects, controlled viewing conditions.

### Robustness Analysis

The paper validates SIMON's robustness across multiple dimensions:

**1. Sampling Granularity:**
- Performance is stable across 3-12 fixations
- Diminishing returns beyond 7-8 fixations
- 5 fixations offers best speed-accuracy trade-off

**2. EEG Channel Topology:**
- Robust across different channel configurations
- Works with standard 64-channel and high-density 128-channel setups
- Channel selection based on visual cortex coverage improves efficiency

**3. Visual Encoder Backbones:**
- Compatible with CLIP ViT-B/16, ViT-L/14, and other vision encoders
- Larger encoders improve absolute performance but relative gain from SAS remains consistent

**4. Brain Encoder Backbones:**
- Works with various EEG encoding architectures
- Benefits are independent of the specific brain encoder choice

---

## Related Work Comparison

| Method | Approach | Center Bias? | Multi-View? | Saliency-Aware? |
|---|---|---|---|---|
| **Traditional EEG-to-Image** | Single center crop | ❌ Yes | ❌ No | ❌ No |
| **Foveation-based** | Fixed center foveation | ⚠️ Partial | ⚠️ Limited | ❌ No |
| **Brain-score alignment** | Global feature matching | ❌ Yes | ❌ No | ❌ No |
| **CLIP-based retrieval** | Text-conditioned matching | ❌ Yes | ❌ No | ❌ No |
| **SIMON (Ours)** | SAS + foveated views | ✅ No | ✅ Yes | ✅ Yes |

**Key Differentiators:**
1. **Content-driven fixation selection** — not spatially uniform
2. **Foreground-aware** — suppresses background clutter
3. **Object-centric** — focuses on semantically meaningful regions
4. **Multi-view integration** — captures object information at multiple scales
5. **Zero-shot capable** — no task-specific fine-tuning required

---

## Implementation Guidelines

### Prerequisites

```bash
# Core dependencies
pip install torch torchvision
pip install transformers  # for CLIP visual encoder
pip install timm          # alternative vision encoders
pip install mne           # EEG preprocessing
pip install scikit-image  # segmentation utilities

# Saliency prediction (choose one)
pip install pytorch-saliency  # or custom saliency model
pip install segment-anything  # SAM for foreground segmentation
```

### Pipeline Configuration

```yaml
# simon_config.yaml
model:
  eeg_encoder:
    type: "conformer"           # or "eegnet", "deep4net"
    n_channels: 64
    sampling_rate: 500
    output_dim: 768

  visual_encoder:
    type: "clip_vit_b_16"       # or "vit_l_14"
    pretrained: true
    output_dim: 512

  projection_dim: 768

salient_aware_sampling:
  foreground_model: "sam_vit_b" # Segment Anything Model
  saliency_model: "dnet"        # or "salient_object_detection"
  n_fixations: 5
  sampling_mode: "weighted"     # "weighted" or "topk"

foveated_views:
  center_size: 128
  peripheral_size: 224
  falloff: "gaussian"
  sigma_ratio: 0.25

aggregation:
  method: "attention"           # "mean", "attention", "learned_pool"
  n_heads: 8

training:
  loss: "info_nce"              # contrastive loss
  temperature: 0.07
  optimizer: "adamw"
  lr: 1e-4
  epochs: 50
  batch_size: 64
  scheduler: "cosine"
```

### EEG Preprocessing

```python
import mne
import numpy as np

def preprocess_eeg(raw_eeg, sfreq=500, low_cut=1, high_cut=100,
                   notch_freq=60, epochs_window=(-0.1, 0.8)):
    """Standard EEG preprocessing pipeline for THINGS-EEG."""
    # Create MNE Raw object
    info = mne.create_info(ch_names=raw_eeg.ch_names,
                           sfreq=sfreq, ch_types='eeg')
    raw = mne.io.RawArray(raw_eeg.data, info)

    # Filtering
    raw.filter(l_freq=low_cut, h_freq=high_cut)
    raw.notch_filter(freqs=notch_freq)

    # Re-reference (common average)
    raw.set_eeg_reference('average')

    # Epoch around stimulus onset
    events = raw_eeg.events
    epochs = mne.Epochs(raw, events, tmin=epochs_window[0],
                        tmax=epochs_window[1], baseline=(None, 0))

    return epochs.get_data()  # [n_epochs, n_channels, n_times]
```

### Training Loop

```python
import torch
import torch.nn.functional as F
from torch.utils.data import DataLoader

def info_nce_loss(eeg_emb, img_emb, temperature=0.07):
    """InfoNCE contrastive loss for EEG-image matching."""
    # Normalize embeddings
    eeg_emb = F.normalize(eeg_emb, dim=-1)
    img_emb = F.normalize(img_emb, dim=-1)

    # Compute similarity matrix
    logits = torch.matmul(eeg_emb, img_emb.T) / temperature

    # Labels: diagonal is positive pairs
    labels = torch.arange(eeg_emb.size(0), device=eeg_emb.device)

    # Cross-entropy loss (both directions)
    loss_img = F.cross_entropy(logits, labels)
    loss_eeg = F.cross_entropy(logits.T, labels)

    return (loss_img + loss_eeg) / 2

def train_step(model, eeg_batch, image_batch, optimizer):
    """Single training step."""
    optimizer.zero_grad()

    # Forward pass
    eeg_emb = model.encode_eeg(eeg_batch)
    img_embs = torch.stack([model.encode_image(img)
                            for img in image_batch], dim=0)

    # Contrastive loss
    loss = info_nce_loss(eeg_emb, img_embs)

    # Backward pass
    loss.backward()
    optimizer.step()

    return loss.item()
```

### Evaluation

```python
def evaluate_retrieval(model, test_eeg, test_images,
                       top_k_list=[1, 5, 10]):
    """Evaluate retrieval accuracy on test set."""
    model.eval()
    results = {f"Top-{k}": 0 for k in top_k_list}

    with torch.no_grad():
        # Pre-compute image embeddings
        img_embs = torch.stack([
            model.encode_image(img) for img in test_images
        ], dim=0)

        for i, eeg in enumerate(test_eeg):
            # Encode query EEG
            q_emb = model.encode_eeg(eeg.unsqueeze(0))

            # Compute similarities
            scores = F.cosine_similarity(
                q_emb, img_embs, dim=-1
            )

            # Get ranked indices
            ranked = torch.argsort(scores, descending=True)

            # Check if ground truth (i) is in top-k
            for k in top_k_list:
                if i in ranked[:k]:
                    results[f"Top-{k}"] += 1

    # Convert to accuracy
    n_samples = len(test_eeg)
    for k in top_k_list:
        results[f"Top-{k}"] /= n_samples

    return results
```

---

## When to Use This Skill

- **Zero-shot EEG-to-image retrieval** — decoding visual content from EEG without task-specific training
- **Brain-computer interfaces for visual content** — reconstructing what a user is looking at
- **Neural decoding with non-center-focused attention** — when subjects attend to objects anywhere in the visual field
- **Cross-subject neural decoding** — inter-subject generalization with attention variability
- **Saliency-guided visual feature extraction** — any task where attention-aware feature sampling improves performance
- **Object-centric representation learning** — focusing on foreground objects vs. background

## When NOT to Use

- Center-fixed visual paradigms (e.g., RSVP, central fixation tasks)
- Non-visual EEG decoding tasks (motor imagery, sleep staging, etc.)
- When computational resources are extremely limited (multi-view adds overhead)
- When only single-view representations are needed

## Paper Reference

- **arXiv:** 2605.00401v1 [cs.CV, q-bio.NC]
- **Title:** SIMON: Saliency-aware Integrative Multi-view Object-centric Neural Decoding
- **Authors:** YuSheng Lin, Ji-Hwa Tsai, Chun-Shu Wei
- **Date:** 2026-05-01
- **Code:** https://github.com/simonlink666/SIMON

## Related Skills

- `eeg-structure-guided-diffusion` — EEG-guided image generation via structured diffusion
- `eeg2vision-multimodal-eeg-framework-2d-visual` — Multimodal EEG-to-2D visual generation framework
- `brain-inspired-capture-evidence-driven-neuromimetic-perceptual` — Brain-inspired neuromimetic perceptual capture
- `cross-subject-eeg-decoding` — Cross-subject generalization for EEG decoding
- `simon-saliency-neural-decoding` — Original SIMON neural decoding skill (ai_collection)
