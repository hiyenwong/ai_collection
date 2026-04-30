---
name: sgdm-eeg-visual-cognition
description: Structure-Guided Diffusion Model (SGDM) for EEG-based visual cognition reconstruction methodology. Integrates structural guidance with diffusion models for decoding both objective perception and subjective cognitive content from EEG signals. Applicable to BCI, visual decoding, brain-computer interfaces. Triggers - EEG, visual reconstruction, diffusion model, brain-computer interface, BCI, neural decoding.
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [neuroscience, eeg, visual-decoding, diffusion-model, bci, brain-computer-interface, neural-decoding]
    source_paper: "Structure-Guided Diffusion Model for EEG-Based Visual Cognition Reconstruction (arXiv:2604.22649v1)"
    citations: 0
    published: 2026-04-24
---

# Structure-Guided Diffusion Model for EEG-Based Visual Cognition Reconstruction

## Overview
Decoding visual information from electroencephalography (EEG) is a fundamental challenge in neuroscience and brain-computer interface (BCI) research. The Structure-Guided Diffusion Model (SGDM) addresses limitations of existing methods by capturing structural features and differentiating objective perception from subjective cognition.

## Core Innovation

### Structure-Guided Framework
Unlike traditional EEG-to-image methods limited to natural images and categorical representations, SGDM:
- Captures fine-grained structural features
- Differentiates between objective perception (sensory input) and subjective cognition (mental imagery)
- Enables reconstruction of both perceived and imagined visual content

### Methodology Components

1. **EEG Signal Encoding**: Neural encoding of temporal-spatial EEG patterns
2. **Structural Guidance**: Explicit structural constraints during diffusion process
3. **Dual-Pathway Decoding**: Separate pathways for perception vs. cognition reconstruction
4. **Diffusion Prior**: Leveraging pre-trained diffusion models with EEG-guided conditioning

## Implementation Pattern

```python
import torch
from diffusers import StableDiffusionPipeline
import numpy as np

class SGDMReconstructor:
    """
    Structure-Guided Diffusion Model for EEG visual reconstruction.
    """
    def __init__(self, eeg_encoder, diffusion_model, guidance_scale=7.5):
        self.eeg_encoder = eeg_encoder  # Pre-trained EEG encoder
        self.diffusion = diffusion_model
        self.guidance_scale = guidance_scale
        
    def encode_eeg(self, eeg_signal):
        """Encode raw EEG to latent representation."""
        # EEG: (batch, channels, time)
        # Extract temporal-spatial features
        temporal_features = self.temporal_conv(eeg_signal)
        spatial_features = self.spatial_attention(temporal_features)
        return self.projection(spatial_features)
    
    def reconstruct_visual(self, eeg_signal, mode='perception'):
        """
        Reconstruct visual content from EEG.
        
        Args:
            eeg_signal: Raw EEG data (batch, channels, time)
            mode: 'perception' for objective perception, 'cognition' for subjective cognition
        """
        # Encode EEG
        eeg_latent = self.encode_eeg(eeg_signal)
        
        # Add structural guidance based on mode
        structural_guidance = self.get_structural_prior(mode)
        
        # Generate with diffusion
        image = self.diffusion(
            prompt_embeds=eeg_latent,
            guidance_scale=self.guidance_scale,
            structural_guidance=structural_guidance
        )
        return image
    
    def get_structural_prior(self, mode):
        """Get structural prior based on reconstruction mode."""
        # Perception: focus on low-level visual features
        # Cognition: focus on high-level semantic features
        if mode == 'perception':
            return self.perception_structure_prior
        else:
            return self.cognition_structure_prior
```

## Key Techniques

### 1. EEG Feature Extraction
- **Temporal Convolution**: Capture temporal dynamics in EEG signals
- **Spatial Attention**: Weight electrode channels based on task relevance
- **Multi-scale Fusion**: Combine features from different frequency bands

### 2. Structural Guidance
- **Edge-aware Guidance**: Preserve structural boundaries
- **Semantic-aware Guidance**: Align with high-level semantic concepts
- **Dual-pathway Architecture**: Separate processing for perception/cognition

### 3. Diffusion Conditioning
- **Classifier-free Guidance**: Balance EEG signal fidelity and image quality
- **Cross-modal Alignment**: Align EEG embeddings with visual latent space
- **Progressive Refinement**: Iterative improvement through diffusion steps

## Applications

1. **Brain-Computer Interfaces**: Direct thought-to-image communication
2. **Visual Prosthetics**: Reconstructing visual experience for the blind
3. **Dream Decoding**: Reconstructing mental imagery during sleep
4. **Neuroscience Research**: Understanding visual processing in the brain

## Advantages Over Existing Methods

| Aspect | Traditional Methods | SGDM |
|--------|---------------------|------|
| Image Types | Natural images only | Any visual content |
| Content | Categorical only | Structural + semantic |
| Perception/Cognition | Combined | Separable |
| Feature Capture | Limited | Fine-grained structural |

## Experimental Considerations

### EEG Recording
- High-density EEG (64+ channels recommended)
- Sampling rate: >=500 Hz
- Reference: Average or linked mastoids

### Preprocessing
- Bandpass filter: 0.1-100 Hz
- Artifact removal: ICA or regression-based
- Epoching: -200ms to +800ms post-stimulus

### Training Data
- Paired EEG-image recordings
- Diverse visual stimuli
- Both perception and imagination conditions

## References

- Structure-Guided Diffusion Model for EEG-Based Visual Cognition Reconstruction, arXiv:2604.22649v1, 2026-04-24
- Authors: Yongxiang Lian, Yueyang Cang, Pingge Hu
- Categories: cs.NE, cs.CV

## Related Skills
- eeg-visual-decoding
- brain-computer-interface
- diffusion-models-neuroscience
- neural-encoding-evaluation-meeg
