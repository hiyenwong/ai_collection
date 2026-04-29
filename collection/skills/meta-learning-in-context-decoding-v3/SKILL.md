---
name: meta-learning-in-context-decoding-v3
description: >
  Meta-learning In-Context Enables Training-Free Cross Subject Brain Decoding.
  Uses meta-learned in-context learning to decode brain signals across subjects
  without any subject-specific training. Supports visual decoding from fMRI/EEG
  signals with zero-shot generalization.
  Activation: meta-learning brain decoding, in-context learning, cross-subject,
  training-free decoding, zero-shot brain decoding, visual reconstruction,
  元学习脑解码, 跨被试解码, 零样本解码
version: 1.0.0
metadata:
  hermes:
    source_paper: "Meta-learning In-Context Enables Training-Free Cross Subject Brain Decoding"
    arxiv_id: "2604.08537"
    tags: [meta-learning, brain-decoding, cross-subject, in-context, zero-shot]
---

# Meta-Learning In-Context Brain Decoding

## Overview

Enables training-free cross-subject brain decoding through meta-learned in-context learning. The model learns to adapt to new subjects at inference time by conditioning on a small number of reference examples, eliminating the need for per-subject fine-tuning.

## Core Innovation

Traditional brain decoders require subject-specific training data. This approach:
1. Meta-learns a general decoding prior across many subjects
2. At inference, adapts to new subjects via in-context examples
3. Achieves competitive accuracy with zero subject-specific training

## Architecture

```
Meta-Training: [Subject A examples] + [Subject B examples] + ... → Learn decoding prior

Inference: [New subject context examples] + [Target brain signal] → Decoded output
```

## In-Context Adaptation

```python
class MetaInContextDecoder:
    def __init__(self, base_model):
        self.base = base_model
    
    def decode(self, brain_signal, context_signals, context_labels):
        # Concatenate context as "prompt"
        input_seq = torch.cat([context_signals, brain_signal], dim=1)
        # Model attends to context to adapt
        output = self.base(input_seq)
        # Extract prediction for target position
        return output[:, -1, :]
```

## Key Advantages

- **Zero-shot generalization**: No training data needed for new subjects
- **Few-shot improvement**: Adding more context examples improves accuracy
- **Scalable**: Works across different recording modalities
- **Practical**: Eliminates per-subject calibration sessions

## Applications

- Rapid BCI deployment (no calibration)
- Clinical neuroimaging across diverse populations
- Multi-subject neuroscience studies
- Visual reconstruction from brain activity

## Related Skills

- eeg-ieeg-bridge, eeg-foundation-models, brain-foundation-model-batch-effects
