---
name: cold-atom-medical-imaging
description: "Medical imaging classification using cold-atom (neutral-atom) reservoir computing with auto-encoders and surrogate-driven training. Use when: medical image classification with reservoir computing, quantum-inspired medical imaging, neutral-atom computing for healthcare, polyp detection with quantum reservoir, surrogate-driven training for medical AI, guided auto-encoder for medical images. Trigger: cold-atom medical imaging, reservoir computing healthcare, quantum reservoir medical classification, medical imaging reservoir, polyp detection AI, neutral-atom classification."
---

# Cold-Atom Medical Imaging

## Overview

Hybrid quantum-classical pipeline using neutral-atom reservoir computing for medical image classification (polyp detection). Combines guided auto-encoder for dimensionality reduction with cold-atom reservoir for classification, trained via surrogate-driven optimization.

## When to Use

- Medical image classification with reservoir computing
- Polyp detection in colonoscopy images
- Quantum/neuromorphic-inspired medical imaging pipelines
- Surrogate-driven training for compute-heavy medical models
- Dimensionality-reduced medical image classification

## Architecture

### Pipeline Components

```
Medical Image -> Guided Auto-Encoder -> Low-Dim Features -> Cold-Atom Reservoir -> Classification
```

1. **Guided Auto-Encoder**: Learns task-aware compressed representation
   - Encoder reduces high-res medical images to latent vectors
   - "Guided" means supervised signal shapes latent space
   - Dimensionality reduction critical for reservoir efficiency

2. **Cold-Atom Reservoir**: Physical quantum-inspired computing
   - Neutral atoms as dynamical system reservoir
   - Input features drive reservoir dynamics
   - Readout layer maps reservoir state to classification
   - Rich temporal dynamics capture subtle features

3. **Surrogate-Driven Training**: Efficient optimization
   - Surrogate model approximates expensive reservoir evaluation
   - Reduces wall-clock training time
   - Enables hyperparameter optimization

## Implementation Pattern

```python
# Step 1: Train guided auto-encoder
from sklearn.pipeline import Pipeline

encoder = GuidedAutoEncoder(
    latent_dim=32,
    supervision_weight=0.5
)
encoder.fit(medical_images, labels)

# Step 2: Extract features
latent_features = encoder.encode(medical_images)

# Step 3: Train reservoir classifier
reservoir = ColdAtomReservoir(
    n_atoms=100,
    connectivity=0.3,
    decay_rate=0.1
)
reservoir.fit(latent_features, labels)

# Step 4: Classify new images
predictions = reservoir.predict(
    encoder.encode(new_images)
)
```

## Key Advantages

- **Energy efficient**: Reservoir computing avoids backprop through dynamics
- **Fewer parameters**: Only readout layer is trained
- **Hardware ready**: Compatible with actual cold-atom platforms
- **Speed**: Inference is fast matrix operations after encoding

## Activation Keywords
- cold-atom medical imaging
- reservoir computing healthcare
- quantum reservoir medical classification
- medical imaging reservoir
- polyp detection AI
- neutral-atom classification
- surrogate-driven medical training
- guided auto-encoder medical
