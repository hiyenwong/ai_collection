---
name: cambrain-realtime-eeg-inference
description: CaMBRAIN methodology for real-time continuous EEG inference using causal Mamba state space models. First model enabling long-range streaming inference of variable-length EEG signals with >10x higher throughput.
version: 1.0.0
author: arXiv paper extraction
arxiv_id: 2605.28792
activation_keywords:
  - EEG
  - real-time inference
  - state space model
  - Mamba
  - causal model
  - continuous EEG
  - streaming inference
  - brain activity monitoring
  - neural signal processing
tags:
  - neuroscience
  - EEG
  - state-space-models
  - causal-inference
  - real-time-processing
  - deep-learning
  - computational-neuroscience
related_skills:
  - jet-eeg-flow-matching
  - eeg-foundation-model-adapters
  - mamba-spike-forecaster-bci
  - eeg-ieeg-bridge-bci
---

# CaMBRAIN: Real-time, Continuous EEG Inference with Causal State Space Models

**arXiv ID**: [2605.28792](https://arxiv.org/abs/2605.28792)
**Authors**: Abhilash Durgam, Nyle Siddiqui, Jeffrey A. Chan-Santiago, Qiushi Fu, Elakkat D. Gireesh, Mubarak Shah
**Submission Date**: 2026-05-27
**Categories**: cs.AI, cs.HC, cs.LG

## Overview

CaMBRAIN is the first **Causal, Mamba-based state space model (SSM)** capable of real-time inference of EEG signals. It addresses critical limitations in existing EEG deep learning approaches:

1. **Quadratic scaling problem**: Traditional attention-based models scale quadratically with sequence length
2. **Fixed-length input constraint**: Raw EEG must be processed in sliding windows, preventing global signal understanding

## Core Innovation

### Key Arguments

- **Bidirectional approaches are needlessly expensive** for EEG processing
- EEG is inherently **causal and unidirectional** - past signals influence future, not vice versa
- **Causal SSM architecture** is more appropriate than bidirectional attention

### Technical Challenge

EEG exhibits **extreme temporal dynamics**:
- Crucial events can be extremely brief (fractions of a second)
- Events separated by long intervals (minutes)
- Current self-supervised objectives optimize for signal reconstruction
- These objectives **fail to train hidden state** to retain salient long-range context

## Methodology

### Multi-Stage Self-Supervised Training Pipeline

Designed specifically for streaming SSMs to:

1. **Encourage long-range memory retention**
2. **Preserve linear-time complexity** of state space models
3. **Explicitly train hidden state** for streaming inference context

### Architecture Components

- **Causal Mamba backbone**: Unidirectional processing aligned with EEG temporal structure
- **Streaming-friendly design**: Continuous inference without sliding-window limitations
- **Linear-time complexity**: O(n) scaling vs O(n²) attention

## Performance Results

**State-of-the-art** across 3 different EEG datasets:
- **>10x higher throughput** than existing models
- First model enabling **long-range, continuous inference** of variable-length EEG signals
- Real-time processing capability

## Technical Details

### Comparison with Existing Approaches

| Method | Complexity | Streaming | Global Context | EEG Suitability |
|--------|------------|-----------|----------------|-----------------|
| Attention-based | O(n²) | No | Limited | Poor |
| Bidirectional SSM | O(n) | No | Good | Overkill |
| **CaMBRAIN (Causal SSM)** | O(n) | Yes | Strong | Optimal |

### Use Cases

1. **Real-time brain activity monitoring**
2. **Continuous EEG analysis** (hours of data)
3. **Event detection** in long EEG recordings
4. **Streaming inference** for clinical applications

## Implementation Guidance

### When to Use

- Long EEG recordings (>seconds to hours)
- Real-time processing requirements
- Memory-constrained environments
- Streaming inference scenarios
- Clinical EEG monitoring

### Integration Patterns

1. **Replace sliding-window EEG models** with streaming inference
2. **Combine with EEG foundation models** for pre-training
3. **Use with event detection pipelines** for real-time monitoring
4. **Integrate with clinical systems** for continuous patient monitoring

## Research Context

### Related Work

- EEG foundation models (LaBraM, NeuroBERT)
- State space models (Mamba, S4)
- Self-supervised EEG learning
- Brain-computer interfaces

### Novel Contributions

1. **First causal EEG SSM** argument
2. **Multi-stage streaming training** pipeline
3. **>10x throughput improvement**
4. **Variable-length continuous inference** capability

## Practical Applications

### Clinical
- ICU patient monitoring
- Seizure detection in long recordings
- Sleep stage analysis
- Anesthesia depth monitoring

### Research
- Large-scale EEG dataset analysis
- Real-time BCI systems
- Neural dynamics studies
- Brain state tracking

## Code & Resources

- **Paper**: https://arxiv.org/abs/2605.28792
- **PDF**: https://arxiv.org/pdf/2605.28792v1
- **Categories**: cs.AI, cs.HC, cs.LG

## Key Takeaways

1. **Causality matters**: EEG is inherently unidirectional - bidirectional models are inefficient
2. **Hidden state training**: Self-supervised objectives must explicitly train memory retention
3. **Linear complexity**: Streaming SSMs enable real-time processing at scale
4. **Global context**: Variable-length inference overcomes sliding-window limitations
