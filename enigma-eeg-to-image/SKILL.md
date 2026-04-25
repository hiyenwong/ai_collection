---
name: enigma-eeg-to-image
description: "ENIGMA: EEG-to-Image in 15 Minutes using <1% parameters — efficient multi-subject visual reconstruction from EEG. Lightweight alternative to diffusion-based EEG-to-image methods."
tags: ["eeg", "visual reconstruction", "multi-subject", "lightweight", "brain-computer interface"]
---

# ENIGMA: EEG-to-Image in 15 Minutes Using Less Than 1% of the Parameters

## Paper Information

- **Title:** ENIGMA: EEG-to-Image in 15 Minutes Using Less Than 1% of the Parameters
- **Authors:** Reese Kneeland, Wangshu Jiang, Ugo Bruzadin Nunes, Paul Steven Scotti, Arnaud Delorme, Jonathan Xu
- **Published:** 2026-02-10
- **arXiv:** [2602.10361](https://arxiv.org/abs/2602.10361)
- **Categories:** q-bio.NC, cs.AI, cs.CV, cs.HC

## Core Problem

Existing EEG-to-image decoding models require:
- Large amounts of per-subject calibration data
- Massive parameter counts (expensive to train and deploy)
- Research-grade EEG hardware for decent performance
- Cannot be quickly deployed on new subjects with consumer hardware

## Key Innovation

ENIGMA is a multi-subject EEG-to-image decoding model that achieves SOTA performance while requiring **less than 1% of trainable parameters** compared to previous approaches.

## Architecture

```
Raw EEG → Subject-Unified Spatio-Temporal Backbone 
       → Multi-Subject Latent Alignment Layers 
       → MLP Projector 
       → Visual Latent Space → Image Reconstruction
```

### Three Core Components:

1. **Subject-Unified Spatio-Temporal Backbone**
   - Single shared encoder for all subjects
   - Processes raw EEG spatio-temporal patterns
   - Eliminates per-subject model duplication

2. **Multi-Subject Latent Alignment Layers**
   - Lightweight alignment modules per subject
   - Map individual brain signals to shared representation space
   - Minimal parameters, maximum transfer

3. **MLP Projector**
   - Maps aligned EEG features to visual latent space
   - Simple but effective bridge between neural and visual domains

## Performance Highlights

- **SOTA on THINGS-EEG2** (research-grade benchmark)
- **SOTA on AllJoined-1.6M** (consumer-grade benchmark)
- **15-minute fine-tuning** on new subjects
- **<1% trainable parameters** vs. previous methods
- First EEG-to-image study with **extensive human behavioral evaluation**
- Works on both research-grade and **consumer-grade EEG hardware**

## Benchmarks

| Benchmark | Hardware Type | Result |
|-----------|--------------|--------|
| THINGS-EEG2 | Research-grade | SOTA |
| AllJoined-1.6M | Consumer-grade | SOTA |

## Evaluation Metrics

Uses standardized fMRI-to-image reconstruction metrics plus:
- Behavioral evaluation via human raters (first for EEG-to-image)
- Extensive ablation studies on architectural choices

## Why This Matters

1. **Practical BCI:** Makes visual decoding deployable on affordable hardware
2. **Efficiency:** Dramatically reduces compute requirements
3. **Rapid Deployment:** New subjects need only 15 minutes of data
4. **Consumer-Grade Works:** Proves useful results on accessible EEG devices

## Comparison with Existing Methods

| Aspect | Previous Methods | ENIGMA |
|--------|----------------|--------|
| Parameters | Full model per approach | <1% of previous |
| New Subject Time | Hours of calibration | 15 minutes |
| Hardware Required | Research-grade | Works on consumer-grade |
| Architecture | Complex, multi-stage | Simple backbone + alignment |

## Trigger Words

- enigma eeg-to-image
- eeg visual reconstruction lightweight
- multi-subject eeg decoding
- consumer-grade eeg image reconstruction
- eeg image 15 minutes
- lightweight brain-computer interface

## Related Skills

- **eeg2vision-multimodal-eeg-framework-2d-visual**: Diffusion-based EEG-to-image
- **enigma-eeg-to-image**: Lightweight alternative (this skill)
- **brain3d-eeg-decoding**: EEG-to-3D visual reconstruction
- **brain-omnifunctional-foundation-model**: Omnifunctional foundation model
- **brain-dit-universal-multi-state**: fMRI foundation model

## Implementation Notes

For implementing ENIGMA-style approaches:

1. Use a shared spatio-temporal encoder across subjects
2. Add lightweight per-subject alignment layers (not full models)
3. Project to an existing visual latent space (CLIP, DINO features)
4. Fine-tune quickly on new subjects with minimal data
5. Evaluate with both automated metrics and human behavioral studies

## Key Takeaways

- Simpler architectures can outperform complex ones for EEG decoding
- Multi-subject learning is key to rapid deployment
- Consumer-grade EEG can produce useful results with the right architecture
- Human behavioral evaluation is essential for validating reconstruction quality