---
name: spiking-event-driven-neuromorphic-mamba-asr
description: Spiking and Event-driven Neuromorphic Mamba Models for Efficient Speech Recognition — achieving 60-70% activation sparsity with minimal accuracy loss on ASR tasks.
version: 1.0.0
author: Hermes Agent (Cron Job)
license: MIT
date: 2026-06-03
arxiv: 2606.01135
paper_title: "Spiking and Event-driven Neuromorphic Mamba Models for Efficient Speech Recognition"
authors: "Tauseef Ahmed, Tao Sun, Jeronimo Castrillon, Kanishkan Vadivel, Guangzhi Tang"
venue: IJCNN 2026
metadata:
  hermes:
    tags: [snn, neuromorphic, asr, mamba, sparsity, event-driven, speech-recognition]
    related_skills: [spiking-mllm-multimodal-spiking, spikingjelly-framework, snn-performance-analysis]
---

# Spiking and Event-driven Neuromorphic Mamba for ASR

## Overview

This paper introduces spiking and event-driven neuromorphic variants of SpeechMamba for automatic speech recognition (ASR), achieving 60-70% activation sparsity with less than 1% accuracy degradation.

## Core Contributions

1. **Event-driven SpeechMamba**: FATReLU activation achieving >60% sparsity
2. **Spiking SpeechMamba**: >70% sparsity with 30% fewer parameters
3. **Cycle-accurate simulator**: Algorithm-hardware co-exploration tool

## Methods

### SpeechMamba Architecture
SpeechMamba = State-of-the-art ASR model using Mamba (selective state space model)

### Neuromorphic Modifications

#### 1. Event-driven SpeechMamba (FATReLU)
```python
# FATReLU: Fixed Activation Threshold ReLU
def fatrelu(x, threshold):
    return x if x > threshold else 0

# Creates sparse activations via thresholding
activation_sparsity = count_zero_activations / total_activations
```

**Results**: 60%+ sparsity, <1% accuracy loss on LibriSpeech

#### 2. Spiking SpeechMamba
```python
# Spiking conversion of Mamba
class SpikingMambaBlock:
    def __init__(self, input_size, hidden_size):
        self.spike_encoder = SpikeEncoder()
        self.ssm = SpikingSSM(hidden_size)
        self.spike_decoder = SpikeDecoder()
    
    def forward(self, x):
        spikes = self.spike_encoder(x)
        ssm_out = self.ssm(spikes)
        return self.spike_decoder(ssm_out)
```

**Results**: 70%+ sparsity, 30% fewer parameters

### Event-driven Simulator
```python
# Cycle-accurate neuromorphic simulator
class NeuromorphicSimulator:
    def simulate(self, model, input):
        # Track:
        # - Memory access patterns
        # - Computation cycles
        # - Activation statistics
        # - Energy estimates
        return performance_metrics
```

**Use**: Identify bottlenecks, co-design optimization

## Performance Results

| Model | Sparsity | Accuracy | Parameters |
|-------|----------|----------|------------|
| SpeechMamba (baseline) | ~0% | WER baseline | Original |
| Event-driven FATReLU | 60%+ | <1% loss | Same |
| Spiking SpeechMamba | 70%+ | ~1-2% loss | 30% fewer |

## Key Insights

### Activation Sparsity Benefits
1. **Memory**: Sparse activations reduce memory bandwidth
2. **Compute**: Skip zero-activation computations
3. **Energy**: Fewer operations = lower power

### Algorithm-Hardware Co-design
1. Simulator reveals bottlenecks
2. Optimize Mamba architecture for sparsity
3. >10% additional efficiency from co-design

## Applications

1. **Edge ASR**: Smartphones, smart home devices
2. **Real-time systems**: Low latency speech recognition
3. **Neuromorphic hardware**: Loihi, SpiNNaker deployment

## Implementation Patterns

### Threshold-based Sparsity
```python
# Threshold selection strategy
threshold = find_optimal_threshold(
    model, validation_data,
    target_sparsity=0.6,
    max_accuracy_loss=0.01
)
```

### Spike Encoding for Mamba
```python
# Rate coding for SSM inputs
def rate_code_signal(signal, time_window):
    spike_rate = abs(signal) / time_window
    return poisson_spike_train(spike_rate)
```

## References

- Ahmed et al. (2026): "Spiking and Event-driven Neuromorphic Mamba Models for Efficient Speech Recognition", IJCNN 2026
- SpeechMamba: Original state-space ASR model
- Mamba: Selective state space models for sequences

## Activation Keywords

`spiking mamba`, `event-driven ASR`, `FATReLU`, `activation sparsity`, `neuromorphic speech`, `LibriSpeech`, `spike encoding`, `cycle-accurate simulator`

## Pitfalls

1. **Threshold selection**: Too high = accuracy loss, too low = low sparsity
2. **Spike encoding**: Rate coding may lose temporal precision
3. **Hardware dependency**: Benefits vary by neuromorphic platform

## Further Reading

- [[spiking-mllm-multimodal-spiking]] - SpikeMLLM multimodal
- [[spikingjelly-framework]] - SpikingJelly training
- [[snn-performance-analysis]] - SNN performance metrics