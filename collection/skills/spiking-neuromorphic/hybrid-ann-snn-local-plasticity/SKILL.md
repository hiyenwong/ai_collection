---
name: "hybrid-ann-snn-local-plasticity"
description: "Hybrid ANN-SNN pipeline with local plasticity: couples pretrained ANN encoders with spiking classifiers using biologically-inspired local learning rules, bypassing end-to-backprop. Use when building energy-efficient spiking neural networks from pretrained models, implementing local Hebbian/plasticity rules, or converting ANN features to spike trains."
metadata:
  arxiv_id: "2606.20151"
  published: "2026-06-18"
  authors: ""
  tags: [spiking-neural-network, local-plasticity, ann-snn-conversion, neuromorphic, rate-coding]
---

# Hybrid ANN-SNN Pipeline with Local Plasticity

## Core Idea

Combine a pretrained ANN encoder (e.g., EfficientNet) with a spiking classifier trained using local, biologically-plausible learning rules. This bypasses end-to-end backpropagation while achieving performance comparable to deep networks (99.09% on 64-class ImageNet).

## Architecture

```
Input → [Pretrained ANN Encoder] → Rate Coding → [Spiking Classifier] → Output
                              (activations → spike trains)   (local learning rules)
```

## Key Components

### 1. ANN Encoder Selection
- Use any pretrained feature extractor (EfficientNet, ResNet, etc.)
- Extract intermediate layer activations as feature embeddings
- No fine-tuning needed — encoder stays frozen

### 2. Rate Coding Conversion
- Convert continuous ANN activations to spike trains
- Higher activation → higher firing rate
- Temporal window determines spike count resolution
- Trade-off: longer windows = more accurate but higher latency

### 3. Spiking Classifier (CoLaNET)
- Spiking neural network with local learning rules
- Receives spike trains from rate-coded ANN features
- Trained independently — no gradient flow back to encoder

### 4. Local Learning Rules
- Hebbian plasticity: strengthen co-active connections
- Spike-timing dependent plasticity (STDP)
- Local error signals without global backpropagation
- Biologically plausible — no weight transport problem

## Workflow

1. **Select pretrained encoder**: Choose based on task domain and feature requirements
2. **Extract features**: Run input through encoder, capture activations
3. **Configure rate coder**: Set temporal window and firing rate mapping
4. **Build spiking classifier**: Design SNN architecture for the task
5. **Train with local rules**: Apply Hebbian/STDP learning to SNN weights
6. **Evaluate**: Measure accuracy vs energy efficiency trade-offs

## Advantages

- **Biological plausibility**: No end-to-end backpropagation
- **Energy efficiency**: SNN inference is sparse and event-driven
- **Leverages pretrained models**: Benefits from large-scale pretraining
- **Modular**: Encoder and classifier can be developed independently
- **Scalable**: Local rules parallelize naturally

## Pitfalls

- **Information loss in rate coding**: Continuous values discretized to spikes
- **Temporal latency**: Rate coding requires time windows for accuracy
- **Local rule limitations**: May not capture complex feature interactions
- **Hyperparameter sensitivity**: Learning rates, thresholds, time constants need careful tuning
- **Task dependency**: Works best when pretrained features are already discriminative

## Activation Keywords

- hybrid ann snn
- local plasticity
- spiking neural network conversion
- rate coding
- biologically plausible learning
- CoLaNET
- hebbian spiking
- snn classifier
- neuromorphic pipeline
