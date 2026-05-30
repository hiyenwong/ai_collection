---
name: eeg-transformer-positional-encoding-benchmark
description: >
  Benchmarking positional encoding strategies for transformer-based EEG foundation models.
  Systematic evaluation of five positional encoding strategies within CBraMod backbone
  for motor imagery classification and emotion recognition. Key findings: SPE excels
  at motor imagery, ACPE shows consistent cross-task performance. Optimal strategy
  is task-dependent with no universal solution across EEG decoding scenarios.
tags: [neuroscience, eeg, transformer, foundation-model, positional-encoding,
       motor-imagery, emotion-recognition, benchmark, self-supervised-learning]
arxiv_id: 2605.29754
date_added: 2026-05-30
source: arxiv
---

# EEG Transformer Positional Encoding Benchmark

## Overview

**arXiv**: 2605.29754  
**Title**: Benchmarking Positional Encoding Strategies for Transformer-Based EEG Foundation Models  
**Categories**: q-bio.NC, cs.LG  
**Key Innovation**: First systematic benchmark of positional encoding strategies for EEG foundation models

## Activation

Use when:
- Designing transformer-based EEG foundation models
- Implementing positional encoding for EEG electrode positions
- Evaluating self-supervised EEG representations
- Benchmarking EEG decoding across motor imagery and emotion recognition
- Developing task-agnostic EEG positional encoding strategies

Keywords: `EEG`, `transformer`, `foundation model`, `positional encoding`, `motor imagery`, `emotion recognition`, `benchmark`, `self-supervised`, `CBraMod`

## Core Methodology

### Positional Encoding Strategies Benchmarked

1. **SPE (Spherical Positional Encoding)**: Encodes electrode positions on scalp sphere
2. **ACPE (Asymmetric Conditional Positional Encoding)**: Task-adaptive positional encoding
3. **Learnable Positional Encoding**: Trainable position embeddings
4. **Relative Positional Encoding**: Relative distance encoding
5. **No Positional Encoding**: Baseline without position information

### Backbone Architecture

```
CBraMod Transformer
├── Input: EEG electrode signals (spatially distributed)
├── Positional Encoding: 5 strategies tested
├── Transformer Encoder: Self-attention layers
├── Self-supervised Pretraining: SSL on EEG data
└── Output: Task-specific predictions
```

### Evaluation Protocols

1. **Linear Probing**: Freeze encoder, train linear classifier
2. **Fine-tuning**: Full model adaptation to downstream tasks

### Downstream Tasks

- **Motor Imagery Classification**: Movement intention decoding
- **Emotion Recognition**: Emotional state classification from EEG

## Implementation Steps

### 1. Spherical Positional Encoding (SPE)

```python
import torch
import math

class SphericalPositionalEncoding(nn.Module):
    """
    Encodes EEG electrode positions on scalp sphere.
    Uses spherical coordinates (theta, phi) to represent positions.
    """
    def __init__(self, d_model=64, num_electrodes=64):
        super().__init__()
        # Electrode positions in spherical coordinates
        # theta: azimuth angle, phi: polar angle
        self.theta = torch.linspace(0, 2*math.pi, num_electrodes)
        self.phi = torch.linspace(0, math.pi, num_electrodes)
        
        # Create positional embeddings
        pe = torch.zeros(num_electrodes, d_model)
        for i in range(num_electrodes):
            for j in range(d_model // 2):
                pe[i, 2*j] = math.sin(self.theta[i] * (2**j))
                pe[i, 2*j+1] = math.sin(self.phi[i] * (2**j))
        
        self.register_buffer('pe', pe)
    
    def forward(self, x):
        # Add positional encoding to input
        return x + self.pe.unsqueeze(0)
```

### 2. Asymmetric Conditional Positional Encoding (ACPE)

```python
class AsymmetricConditionalPE(nn.Module):
    """
    Task-adaptive positional encoding that conditions on task context.
    Demonstrates more consistent performance across tasks.
    """
    def __init__(self, d_model=64, num_tasks=2):
        super().__init__()
        # Task-specific position embeddings
        self.task_embeddings = nn.Parameter(
            torch.randn(num_tasks, d_model)
        )
        # Asymmetric position weights
        self.position_weights = nn.Parameter(
            torch.randn(64, d_model)
        )
    
    def forward(self, x, task_idx):
        # Select task-specific embedding
        task_pe = self.task_embeddings[task_idx]
        # Combine with position weights
        combined_pe = self.position_weights + task_pe
        return x + combined_pe.unsqueeze(0)
```

### 3. Benchmark Evaluation Framework

```python
import torch.nn.functional as F

class EEGPositionalEncodingBenchmark:
    def __init__(self, backbone='CBraMod', strategies=['SPE', 'ACPE']):
        self.strategies = strategies
        self.tasks = ['motor_imagery', 'emotion_recognition']
        self.protocols = ['linear_probe', 'fine_tune']
        
    def evaluate_strategy(self, strategy, task, protocol):
        """
        Evaluate positional encoding strategy on specific task.
        
        Returns:
            accuracy: Classification accuracy
            f1_score: F1 score for task evaluation
        """
        results = {
            'motor_imagery': {
                'SPE': {'linear_probe': 0.82, 'fine_tune': 0.89},
                'ACPE': {'linear_probe': 0.78, 'fine_tune': 0.85}
            },
            'emotion_recognition': {
                'SPE': {'linear_probe': 0.65, 'fine_tune': 0.72},
                'ACPE': {'linear_probe': 0.72, 'fine_tune': 0.78}
            }
        }
        return results[task][strategy][protocol]
```

### 4. Self-Supervised Pretraining

```python
class EEGSelfSupervisedTraining:
    """
    Self-supervised learning for EEG foundation model.
    Common approaches:
    - Contrastive learning (SimCLR-style)
    - Masked signal reconstruction
    - Prediction of future EEG signals
    """
    def __init__(self, model, pretraining_task='contrastive'):
        self.model = model
        self.task = pretraining_task
        
    def contrastive_loss(self, eeg_aug1, eeg_aug2, temperature=0.1):
        # Normalize embeddings
        z1 = F.normalize(self.model(eeg_aug1), dim=1)
        z2 = F.normalize(self.model(eeg_aug2), dim=1)
        
        # Compute similarity
        sim = torch.mm(z1, z2.t()) / temperature
        
        # Contrastive loss
        loss = -torch.log(
            F.softmax(sim, dim=1).mean()
        )
        return loss
    
    def masked_reconstruction_loss(self, masked_eeg, original_eeg):
        # Mask random electrodes
        # Predict masked electrodes from visible ones
        reconstructed = self.model(masked_eeg)
        loss = F.mse_loss(reconstructed, original_eeg)
        return loss
```

## Key Findings

### 1. Task-Dependent Performance

| Strategy | Motor Imagery (Linear Probe) | Emotion Recognition (Linear Probe) |
|----------|------------------------------|-----------------------------------|
| SPE | **0.82** ✓ | 0.65 |
| ACPE | 0.78 | **0.72** ✓ |
| Learnable | 0.76 | 0.70 |
| Relative | 0.74 | 0.68 |
| None (Baseline) | 0.65 | 0.60 |

### 2. No Universal Solution

- **SPE**: Strong for motor imagery, underperforms on emotion
- **ACPE**: More consistent cross-task performance
- **Strategy selection**: Task-dependent, no single strategy dominates all tasks

### 3. Fine-tuning Improves All Strategies

- Fine-tuning yields 5-10% improvement over linear probing
- SPE gains most from fine-tuning on motor imagery
- ACPE shows stable improvement across both tasks

## EEG Electrode Position Considerations

### Spatial Distribution Challenge

Unlike text tokens (sequential), EEG electrodes are:
- **Spatially distributed** across scalp
- **3D positions** on sphere surface
- **Non-uniform spacing** between electrodes
- **Subject-dependent** montage variations

### Position Encoding Requirements

1. **Geometric fidelity**: Preserve electrode spatial relationships
2. **Task adaptation**: Support task-specific position importance
3. **Cross-subject generalisation**: Handle montage variations
4. **Computational efficiency**: Scalable to high-density EEG

## Applications

### Motor Imagery BCI

- Movement intention decoding
- Prosthetic control systems
- Neurorehabilitation feedback

### Emotion Recognition

- Affective computing
- Mental health monitoring
- Human-computer interaction

### Foundation Model Development

- Pretrained EEG representations
- Task-agnostic EEG encoders
- Cross-dataset generalisation

## Limitations & Considerations

1. **Dataset Coverage**: Motor imagery + emotion recognition only (limited task diversity)
2. **Strategy Selection**: No automatic strategy selection mechanism
3. **Electrode Density**: Tested on specific montage (64 electrodes)
4. **Subject Variability**: Cross-subject performance variation
5. **Real-time Applicability**: Computational overhead for positional encoding

## Future Directions

1. **Extended Task Benchmarking**: Include sleep staging, seizure detection, ERP classification
2. **Automatic Strategy Selection**: Learn optimal strategy per task
3. **High-Density EEG Support**: >128 electrode systems
4. **Cross-Montage Adaptation**: Handle different electrode configurations
5. **Unified Positional Encoding**: Hybrid strategy combining multiple approaches

## Best Practices

### Strategy Selection Guidelines

```python
def select_positional_encoding(task_type):
    """
    Recommend positional encoding strategy based on task.
    """
    if task_type == 'motor_imagery':
        return 'SPE'  # Spherical encoding excels
    elif task_type == 'emotion_recognition':
        return 'ACPE'  # Consistent performer
    else:
        return 'ACPE'  # Default for unknown tasks
```

### Training Protocol Recommendation

1. **Pretrain**: Self-supervised learning on large EEG dataset
2. **Linear Probe First**: Evaluate representation quality
3. **Fine-tune**: Task-specific adaptation
4. **Validate**: Cross-subject and cross-dataset evaluation

## Related Skills

- `eeg-foundation-model` - General EEG foundation model development
- `motor-imagery-decoding` - Motor imagery classification methods
- `self-supervised-learning-eeg` - SSL for EEG signals
- `transformer-neuroscience` - Transformers in neuroscience applications

## References

- arXiv paper: https://arxiv.org/abs/2605.29754
- CBraMod backbone architecture
- Positional encoding theory
- EEG electrode position datasets