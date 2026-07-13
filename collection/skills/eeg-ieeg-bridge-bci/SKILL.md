---
name: eeg-ieeg-bridge-bci
description: >
  Bridging scalp EEG and intracranial EEG (iEEG) in BCI via pretrained neural models.
  Maps non-invasive scalp EEG to iEEG-quality representations, enabling high-fidelity
  BCI without invasive implants. Uses pretrained models to learn the scalp-to-cortical
  mapping.
  Activation: EEG iEEG bridge, scalp to intracranial, BCI translation, non-invasive BCI,
  cortical reconstruction, EEG-to-iEEG, 脑电皮层映射, 无创BCI
version: 1.0.0
metadata:
  hermes:
    source_paper: "Bridging scalp and intracranial EEG in BCI via pretrained neural models"
    arxiv_id: "2604.14202"
    tags: [eeg, ieeg, bci, translation, pretrained-models, non-invasive]
---

# EEG-to-iEEG Bridge for BCI

## Overview

Maps non-invasive scalp EEG signals to intracranial EEG (iEEG) quality representations using pretrained neural models. This enables high-fidelity BCI control without requiring invasive electrode implants.

## Core Problem

Scalp EEG suffers from:
- Low spatial resolution (smearing through skull)
- Volume conduction artifacts
- Limited frequency bandwidth
- Poor signal-to-noise ratio

iEEG provides high-quality signals but requires surgery. This approach bridges the gap.

## Methodology

### Stage 1: Shared Representation Learning
- Train on paired scalp-iEEG recordings
- Learn a shared latent space preserving neural information
- Use contrastive learning to align representations

### Stage 2: Scalp-to-iEEG Translation
```python
class EEG2iEEGBridge:
    def __init__(self, pretrained_encoder):
        self.encoder = pretrained_encoder  # frozen
        self.mapper = nn.Sequential(
            nn.Linear(latent_dim, hidden_dim),
            nn.GELU(),
            nn.Linear(hidden_dim, ieeg_dim)
        )
    
    def translate(self, scalp_eeg):
        latent = self.encoder(scalp_eeg)
        ieeg_repr = self.mapper(latent)
        return ieeg_repr
```

### Stage 3: BCI Decoding
- Use translated iEEG representations for downstream BCI tasks
- Achieves near-iEEG decoding accuracy from scalp signals

## Key Findings

- Pretrained representations significantly improve translation quality
- Temporal alignment between scalp and iEEG is critical
- Certain brain regions (motor, visual) translate better than others

## Applications

- Non-invasive BCI with iEEG-level performance
- Clinical monitoring without implants
- Research requiring high-quality EEG from many subjects

## Related Skills

- eeg-foundation-models, copilot-assisted-second-thought-bci
