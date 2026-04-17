---
name: wta-spiking-transformer-language
description: Winner-Take-All (WTA) Spiking Transformer for language modeling. Introduces two softmax-free, spike-driven self-attention modules: WTA Spiking Self-Attention (WSSA) and Causal WTA Spiking Self-Attention (CWSSA). Designs encoder-only (WE-Spikingformer) for masked language modeling and decoder-only (WD-Spikingformer) for causal language modeling. Trained end-to-end for NLP tasks without softmax attention, enabling energy-efficient neuromorphic deployment.
version: 0.1.0
arxiv: 2604.11321v1
title: "Winner-Take-All Spiking Transformer for Language Modeling"
tags:
  - spiking-transformer
  - winner-take-all
  - language-modeling
  - softmax-free
  - self-attention
  - neuromorphic
  - energy-efficient
  - spiking-neural-networks
---

# WTA Spiking Transformer for Language Modeling

## Overview

This skill implements Winner-Take-All (WTA) spiking transformers — a novel architecture that replaces softmax attention with softmax-free, spike-driven self-attention mechanisms. Two core modules are defined:

1. **WSSA** — WTA Spiking Self-Attention (bidirectional, for encoder)
2. **CWSSA** — Causal WTA Spiking Self-Attention (causal/masked, for decoder)

These form the basis of two architectures:
- **WE-Spikingformer** — Encoder-only, for masked language modeling (MLM)
- **WD-Spikingformer** — Decoder-only, for causal language modeling (CLM)

## Key Problem Addressed

Existing spiking transformers for language modeling rely heavily on **softmax-based spiking self-attention**, which incurs high energy costs and is unsuitable for neuromorphic hardware deployment. WTA mechanisms eliminate softmax entirely while maintaining competitive performance across 16 NLP datasets.

## Architecture

- **WSSA (Encoder Attention)**: Bidirectional WTA competition across all tokens; k-winners selected per attention head
- **CWSSA (Decoder Attention)**: Causal masking ensures each token only attends to preceding tokens; WTA selection within causal window
- **Spiking FFN**: Feed-forward network uses spiking neurons instead of ReLU/GeGLU
- **Integer Training & Spike Inference**: Trained with integer-valued representations; inference uses binary spikes

## When to Use

- Energy-efficient language modeling on neuromorphic hardware
- Sparse attention mechanisms without softmax computation
- Masked language modeling (WE-Spikingformer) or causal language modeling (WD-Spikingformer)
- Research into spike-driven transformer alternatives

## Validated Tasks

Experiments span 16 datasets across:
- Natural Language Understanding (GLUE, SuperGLUE tasks)
- Question Answering
- Commonsense Reasoning
