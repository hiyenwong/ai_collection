---
name: visual-imagery-decoding-fmri
description: "Latent functional alignment approach for decoding visual imagery from fMRI data. Maps imagery-evoked activity into pretrained perception decoder conditioning space, with retrieval-based augmentation for limited supervision. Activation: visual imagery decoding, fMRI imagination, latent alignment, brain imagery, DynaDiff, NSD imagery, 视觉想象解码, 脑成像想象重建"
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [neuroscience, fmri, decoding, imagery, diffusion-models, brain-computer]
    source_paper: "Seeing the imagined: a latent functional alignment in visual imagery decoding from fMRI data (arXiv:2604.15374v1)"
---

# Visual Imagery Decoding from fMRI via Latent Functional Alignment

## Source Paper
- **Title**: Seeing the imagined: a latent functional alignment in visual imagery decoding from fMRI data
- **Authors**: Fabrizio Spera, Tommaso Boccato, Michal Olak
- **arXiv**: 2604.15374v1
- **Published**: 2026-04-15
- **PDF**: https://arxiv.org/abs/2604.15374

## Overview
Adapts state-of-the-art perception decoders (DynaDiff) to reconstruct imagined visual content from fMRI data using latent functional alignment. Maps imagery-evoked brain activity into the pretrained model's conditioning space while keeping remaining components frozen. Includes retrieval-based augmentation to handle limited imagery-perception supervision.

## Key Contributions
1. **Latent functional alignment**: Maps imagery fMRI into perception decoder's latent space
2. **Frozen pretrained decoder**: Leverages powerful perception models without retraining
3. **Retrieval-based augmentation**: Selects semantically related perception trials to augment limited imagery data
4. **Consistent improvement** across 4 subjects on Imagery-NSD benchmark

## Core Concepts

### The Perception-Imagery Gap
Perception decoders trained on viewing data don't transfer well to imagery because:
- Imagery activates a subset of visual cortex regions
- Mental representations are less structured than perception
- Limited paired imagery-perception supervision available

### Latent Functional Alignment Solution
Instead of training a decoder from scratch, learn a mapping from imagery fMRI patterns to the latent conditioning space of a pretrained perception decoder:

```python
import numpy as np
from sklearn.linear_model import Ridge

class LatentFunctionalAlignment:
    """Map imagery fMRI to pretrained decoder latent space."""
    
    def __init__(self, n_voxels, latent_dim=768):
        self.n_voxels = n_voxels
        self.latent_dim = latent_dim
    
    def train_alignment(self, fmri_data, latent_targets, alpha=100000):
        """Train alignment using paired imagery-perception data.
        
        Args:
            fmri_data: (n_samples, n_voxels) fMRI patterns during imagery
            latent_targets: (n_samples, latent_dim) from pretrained decoder
        """
        ridge = Ridge(alpha=alpha)
        ridge.fit(fmri_data, latent_targets)
        self.ridge_model = ridge
        return ridge
    
    def transform(self, fmri_imagery):
        """Map imagery fMRI to latent conditioning vector."""
        return self.ridge_model.predict(fmri_imagery)


class RetrievalAugmentation:
    """Augment imagery training with related perception trials."""
    
    def __init__(self, perception_fmri, perception_latents):
        from sklearn.metrics.pairwise import cosine_similarity
        self.perception_fmri = perception_fmri
        self.perception_latents = perception_latents
        self.similarity_fn = cosine_similarity
    
    def find_related(self, imagery_fmri, k=5):
        """Find k most related perception trials for an imagery sample."""
        similarities = self.similarity_fn(
            imagery_fmri.reshape(1, -1), 
            self.perception_fmri
        )[0]
        top_k_indices = np.argsort(similarities)[-k:]
        return self.perception_latents[top_k_indices]
    
    def augment_dataset(self, imagery_fmri, imagery_latents, k=5):
        """Create augmented training set."""
        augmented_latents = [imagery_latents]
        for i in range(len(imagery_fmri)):
            related = self.find_related(imagery_fmri[i:i+1], k=k)
            augmented_latents.append(related)
        return np.concatenate(augmented_latents, axis=0)
```

### Complete Decoding Pipeline

```python
class ImageryDecoder:
    """Complete visual imagery decoding pipeline."""
    
    def __init__(self, n_voxels, latent_dim=768):
        self.alignment = LatentFunctionalAlignment(n_voxels, latent_dim)
        self.augmentation = None
    
    def fit(self, imagery_fmri, imagery_latents, 
            perception_fmri=None, perception_latents=None, k=5):
        """Train the imagery decoder with optional augmentation."""
        if perception_fmri is not None:
            self.augmentation = RetrievalAugmentation(
                perception_fmri, perception_latents
            )
            aug_latents = self.augmentation.augment_dataset(
                imagery_fmri, imagery_latents, k=k
            )
        else:
            aug_latents = imagery_latents
        
        self.alignment.train_alignment(imagery_fmri, aug_latents)
    
    def decode(self, fmri_imagery):
        """Decode imagery fMRI to latent conditioning vector."""
        return self.alignment.transform(fmri_imagery)
```

## Evaluation Metrics
| Metric | Description |
|--------|-------------|
| AlexNet(2) | High-level semantic similarity |
| AlexNet(5) | Mid-level visual features |
| EfficientNet | Modern feature similarity |
| InceptionScore | Image quality and diversity |
| CLIP | Text-image alignment |

## Applications
1. **BCI for communication**: Decoding imagined content for locked-in patients
2. **Dream reconstruction**: Exploring neural basis of visual imagination
3. **Creative AI assistance**: Brain-to-image generation from mental imagery
4. **Cognitive neuroscience**: Understanding imagery vs perception neural codes

## Key Datasets
- **Imagery-NSD**: fMRI during visual mental imagery
- **Natural Scenes Dataset (NSD)**: Large-scale perception fMRI

## Activation Keywords
- visual imagery decoding
- fMRI imagination
- latent functional alignment
- DynaDiff imagery
- brain-to-image imagination
- NSD imagery benchmark
- 视觉想象解码
- 脑成像想象重建
- 潜在功能对齐
- 功能磁共振想象
