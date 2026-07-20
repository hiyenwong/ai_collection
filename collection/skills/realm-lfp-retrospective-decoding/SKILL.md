---
name: realm-lfp-retrospective-decoding
description: "REALM methodology for LFP-based behavior decoding using retrospective distillation. Use when: building causal LFP decoding models, offline-to-online distillation for neural signals, Mamba-based neural sequence modeling, BCI decoding without spike signals, reducing bandwidth/power in implantable BCIs, behavior decoding from local field potentials. Activation: LFP decoding, REALM, retrospective distillation, causal neural decoding, wireless BCI, Mamba neural model, spike-free decoding."
---

# REALM: Retrospective Encoder Alignment for LFP Modeling

Methodology for causal LFP-based behavior decoding via retrospective distillation.

## Problem

Spike signals dominate BCI decoding but have high power/bandwidth costs. LFPs offer lower energy and bandwidth but causal LFP models show reduced accuracy vs. non-causal architectures.

## Solution: REALM Framework

Transfer knowledge from offline bidirectional model to causal real-time model via retrospective distillation.

## Architecture

### Teacher Model (Offline)
- **Backbone**: Bidirectional Mamba-2
- **Pretraining**: Masked autoencoding objective across multiple sessions
- **Purpose**: Capture rich bidirectional temporal dependencies

### Student Model (Real-time)
- **Backbone**: Compact causal Mamba-2
- **Training**: Combined objective of representation alignment + task supervision
- **Purpose**: Real-time causal decoding with minimal parameters

### Distillation Pipeline
```
Bidirectional Teacher (offline)
    ↓ representation alignment + task supervision
Causal Student (real-time)
    ↓ behavior decoding output
```

## Key Results

- Outperforms causal AND non-causal LFP-based SOTA methods
- Significant parameter count reduction
- Significant training time reduction
- Competitive with spike-based decoding using LFP-only signals

## Workflow

1. **Pretrain Teacher**: Multi-session bidirectional Mamba-2 with masked autoencoding
2. **Distill to Student**: Align representations + task supervision
3. **Deploy**: Compact causal model for real-time wireless BCI

## Implementation Notes

- Mamba-2 state space model captures long-range temporal dependencies efficiently
- Masked autoencoding pretraining leverages unlabeled multi-session data
- Representation alignment preserves teacher's internal representations
- Task supervision ensures decoding accuracy is maintained
- Suitable for next-generation wireless implantable BCIs

## Activation Keywords

- LFP decoding
- REALM
- retrospective distillation
- causal neural decoding
- wireless BCI
- Mamba neural model
- spike-free decoding
- behavior decoding LFP
- local field potential decoding
