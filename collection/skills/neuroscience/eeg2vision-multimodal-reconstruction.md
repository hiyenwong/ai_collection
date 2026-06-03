---
name: eeg2vision-multimodal-reconstruction
description: "Multimodal EEG-based framework for 2D visual reconstruction in cognitive neuroscience. Supports multiple EEG channel configurations with prompt-guided post-reconstruction boosting."
---

# EEG2Vision Skill

Modular, end-to-end EEG-to-image framework for reconstructing visual stimuli from non-invasive EEG recordings.

## Core Concept

EEG2Vision addresses the challenge of reconstructing visual stimuli from low-spatial-resolution, high-noise EEG signals, particularly under realistic low-density electrode configurations. The framework uses a multimodal approach combining EEG-conditioned diffusion with semantic boosting.

## Key Features

1. **Multi-Resolution Support**
   - 128 channels (high-density)
   - 64 channels
   - 32 channels
   - 24 channels (low-density, consumer-grade)

2. **Two-Stage Architecture**
   - Stage 1: EEG-conditioned diffusion reconstruction
   - Stage 2: Prompt-guided post-reconstruction boosting

3. **Semantic Enhancement**
   - Multimodal LLM extracts semantic descriptions from EEG
   - Image-to-image diffusion refines geometry
   - Preserves EEG-grounded structure

## Performance Metrics

| Channels | Top-1 Acc | FID | IS Improvement |
|----------|-----------|-----|----------------|
| 128 | 89% | 76.77 | baseline |
| 64 | ~75% | ~78 | +5% |
| 32 | ~55% | ~79 | +7% |
| 24 | 38% | 80.51 | +9.71% |

## Methodology

### Stage 1: EEG-Conditioned Diffusion
```python
# Base reconstruction from EEG features
initial_image = eeg_conditioned_diffusion(
    eeg_signal=preprocessed_eeg,
    channels=n_channels,
    condition_type="semantic"
)
```

### Stage 2: Semantic Boosting
```python
# Extract semantic description from EEG
semantic_prompt = multimodal_llm.extract_semantics(eeg_signal)

# Refine with image-to-image diffusion
boosted_image = image_to_image_diffusion(
    initial_image,
    prompt=semantic_prompt,
    preserve_structure=True
)
```

## Applications

- Real-time brain-to-image applications
- Consumer-grade EEG device compatibility
- Cognitive neuroscience research
- Visual perception studies
- Brain-computer interfaces

## Paper Reference

- **Title**: EEG2Vision: A Multimodal EEG-Based Framework for 2D Visual Reconstruction in Cognitive Neuroscience
- **arXiv**: 2604.08063
- **Authors**: Balloni et al.

## Activation Keywords

- eeg2vision
- EEG visual reconstruction
- brain-to-image
- multimodal EEG
- EEG diffusion model
