---
name: realm-lfp-retrospective-decoding
description: REALM (Retrospective Encoder Alignment for LFP Modeling) — causal LFP-based behavior decoding via retrospective knowledge distillation from bidirectional Mamba-2 teacher.
---

# REALM: Retrospective Encoder Alignment for LFP Modeling

**Source**: Wu, Bu, Ma, Du. "REALM: Retrospective Encoder Alignment for LFP Modeling." arXiv:2605.14867, 2026.

## Overview

REALM is the **first foundation model pre-trained exclusively on Local Field Potentials (LFP)** for high-fidelity motor decoding without spikes in real-time, resource-constrained BCIs. It bridges the offline-to-online deployment gap using retrospective knowledge distillation.

## Key Problem

- Spike-based BCIs require >30kHz sampling → tens of milliwatts power → incompatible with wireless implantable devices
- LFPs offer sub-milliwatt operation but historically show lower decoding accuracy
- Existing neural decoding models (NDT2, NDT3) are **non-causal** (bidirectional) → unsuitable for real-time use
- The offline-to-online deployment gap in neural decoding mirrors what speech recognition solved a decade ago

## Three-Stage Pipeline

### Stage 1: Self-Supervised Pretraining

- **Bidirectional Mamba-2 teacher** pretrained on 130 hours of LFP data
- **6 subjects, 3 datasets** (Makin, Flint, etc.)
- **Continuous Masked Autoencoding (CMAE)** objective
- Neural tokenizer: TCN → ECA → Session-specific spatial embeddings + Shared value embeddings
- Input: Raw LFP at 100Hz, 96 channels (Utah array), 500-timestep windows

### Stage 2: Retrospective Knowledge Distillation

- Compress non-causal BiMamba-2 teacher into **strictly causal Mamba-2 students** (2.1M–10.5M params)
- Combined objective: Representation alignment + Task supervision
- Generalizes to bidirectional setting as well (REALM-bi)
- Achieves 10× faster convergence with half the parameters vs. CrossModalDistill

### Stage 3: Fine-tuning & Evaluation

- Per-session supervised/unsupervised fine-tuning
- Zero-shot evaluation on held-out sessions
- Behavior prediction: 2D cursor velocity decoding

## Neural Tokenizer Architecture

```
Raw LFP (B×96×1×500)
    ↓ Conv1D (per-channel, K=3, d_ch=8)
    ↓ ECA (Efficient Channel Attention, k=5)
    ↓ Session-specific spatial embedding
    ↓ Shared value embedding
Token embeddings
```

**Causal ECA**: Running mean over [1,t] instead of full window for real-time compatibility.

## Mamba-2 Architecture

REALM uses **Mamba-2** (SSD - Selective State Space with Diagonal) as the backbone:

- **BiMamba-2 teacher**: Bidirectional (forward + backward SSD layers concatenated)
- **Causal Mamba-2 student**: Single forward SSD pass only
- Skip linear connections for residual learning
- LayerNorm before projection

## Results

| Model | R² Score | Params | Training Time | Causal |
|-------|---------|--------|--------------|--------|
| REALM-causal (Makin) | New SOTA | 2.1M-10.5M | Fast | ✓ |
| REALM-bi (offline) | 0.776 | ~5M | 10× faster | ✗ |
| CrossModalDistill | 0.763 | ~10M | Baseline | ✗ |
| Kalman Filter | Lower | Minimal | Instant | ✓ |

REALM-bi surpasses CrossModalDistill (R²=0.763) which requires spike supervision, while using half the parameters and converging 10× faster.

## Real-Time Deployment

First purely LFP-based decoder achieving real-time performance on:
- **NVIDIA Jetson Orin Nano**: Full sampling rate decoding
- **Raspberry Pi 5**: End-to-end causal pipeline

This demonstrates feasibility for fully-implantable, battery-free wireless BCI systems.

## Why This Matters

1. **LFP-only foundation model**: No prior work pre-trained foundation models on LFP alone
2. **Causal real-time decoding**: First demonstration of LFP-based decoder running in real-time on portable hardware
3. **No spike dependency**: Does not require paired spike recordings during training (unlike CrossModalDistill)
4. **Retrospective distillation**: Proves structured representation transfer bridges offline-to-online gap
5. **Energy efficiency**: Compatible with on-skull energy harvesting, inductive recharging, thermoelectric scavenging

## Implementation Guide

### Core Components

```python
# Neural Tokenizer
class NeuralTokenizer:
    def __init__(self, channels=96, d_ch=8, kernel=3, eca_k=5):
        self.conv1d = Conv1d(1, d_ch, kernel, padding=1)  # per-channel
        self.eca = EfficientChannelAttention(eca_k)
        self.shared_value_emb = Linear(...)
        self.session_spatial_emb = Embedding(...)  # session-specific
    
    def forward(self, x, session_id):
        # x: (B, C, 1, T) raw LFP
        h = gelu(self.conv1d(x))  # (B, C, d_ch, T)
        h = self.eca(h)  # channel-attended
        tokens = self.shared_value_emb(h) + self.session_spatial_emb(session_id)
        return tokens

# Retrospective Distillation Loss
def distillation_loss(teacher_out, student_out, task_labels):
    repr_align = MSE(teacher_hidden, student_hidden)
    task_loss = MSE(student_velocity, task_labels)
    return repr_align + task_loss
```

### Training Strategy

1. **Pretrain teacher**: CMAE on 130h multi-session LFP (bidirectional Mamba-2)
2. **Distill student**: Freeze teacher, train causal Mamba-2 student with combined loss
3. **Fine-tune**: Per-session supervised fine-tuning on behavior prediction
4. **Evaluate**: Held-out sessions, zero-shot transfer

### Key Design Choices

- **Window size**: 500 timesteps at 100Hz (5 seconds of LFP)
- **Channel count**: 96 (Utah array standard)
- **Student params**: 2.1M–10.5M (vs. teacher ~10M+)
- **Representation alignment**: Layer-by-layer feature matching

## Pitfalls

1. **Causality constraint**: Student must be strictly causal — no future information access
2. **Session-specific embeddings**: Requires careful handling for cross-session generalization
3. **LFP quality**: Signal quality depends on electrode state; chronic implantation effects matter
4. **Teacher-student gap**: Distillation quality depends on teacher pretraining quality
5. **Edge hardware limits**: Jetson Nano/RPi5 have memory constraints; model must fit in RAM

## Activation

- REALM
- LFP decoding
- local field potential
- causal neural decoding
- retrospective distillation
- Mamba-2 BCI
- wireless BCI
- offline-to-online neural decoding
- LFP foundation model
- behavior decoding
