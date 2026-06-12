---
name: laya-eeg-foundation
description: >
  Laya: A LeJEPA approach to EEG via Latent Prediction over Reconstructed Activity.
  Self-supervised EEG foundation model using Joint Embedding Predictive Architecture (JEPA)
  with latent-space prediction for EEG representation learning. Enables transfer learning
  across EEG tasks without labeled data.
  Activation: EEG foundation model, self-supervised EEG, JEPA, EEG pretraining,
  EEG representation learning, brain signal embedding, 脑电基础模型, 自监督脑电
version: 1.0.0
metadata:
  hermes:
    source_paper: "Laya: A LeJEPA Approach to EEG via Latent Prediction over Reconstructed Activity"
    arxiv_id: "2603.16281"
    tags: [eeg, foundation-model, self-supervised, japa, representation-learning]
---

# Laya EEG Foundation Model

## Overview

Self-supervised EEG foundation model using LeJEPA (Latent JEPA) architecture. Predicts latent representations of future/reconstructed EEG activity, learning general-purpose neural embeddings transferable across BCI, clinical, and cognitive neuroscience tasks.

## Architecture

```
EEG Input → Encoder → Latent z_t
                      ↓
              Predictor → ẑ_{t+Δ}
                      ↑
        Context Encoder → z_{t+Δ}
```

## Key Design Principles

1. **Latent-Space Prediction**: Predict future latents rather than raw EEG, avoiding blurry reconstructions
2. **Multi-Scale Temporal Context**: Capture both short-term dynamics and long-range dependencies
3. **Subject-Invariant Features**: Learn representations that generalize across individuals
4. **Channel-Agnostic Handling**: Robust to varying EEG channel configurations

## Training Pipeline

```python
class LeJEPAEEG:
    def __init__(self, encoder_dim=256, predictor_dim=128):
        self.encoder = EEGEncoder(dim=encoder_dim)
        self.context_encoder = EEGEncoder(dim=encoder_dim)  # stop-grad
        self.predictor = Predictor(encoder_dim, predictor_dim)
    
    def forward(self, eeg_target, eeg_context):
        z_target = self.encoder(eeg_target)          # no grad through context
        z_context = self.context_encoder(eeg_context) # stop-gradient
        z_pred = self.predictor(z_context)
        loss = mse_loss(z_pred, z_target.detach())
        return loss
```

## Applications

- Zero-shot EEG classification
- Transfer learning for BCI
- Cross-subject generalization
- Clinical EEG anomaly detection

## Related Skills

- eeg-ieeg-bridge, meta-learning-in-context-brain-decoding, eeg-foundation-model-adapters
