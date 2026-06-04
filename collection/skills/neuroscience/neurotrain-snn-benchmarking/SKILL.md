---
name: neurotrain-snn-benchmarking
description: "Comprehensive SNN training algorithm taxonomy and open benchmarking framework from NeuroTrain paper (arXiv:2605.15058). Covers surrogate-gradient backpropagation, local/three-factor learning rules, predictive coding, and neuromodulated plasticity. Use when: analyzing SNN training methods, comparing learning rules, benchmarking spiking networks, evaluating biological plausibility vs computational efficiency, implementing local learning in SNNs."
---

# NeuroTrain: SNN Training Taxonomy & Benchmarking

## Paper Reference
**arXiv**: 2605.15058
**Title**: NeuroTrain: Surveying Local Learning Rules for Spiking Neural Networks with an Open Benchmarking Framework
**Authors**: Alessio Caviglia, Filippo Marostica, Roberta Bardini

## SNN Training Algorithm Taxonomy

### 1. Surrogate-Gradient Backpropagation
- **Mechanism**: Replace non-differentiable spike function with smooth surrogate during backward pass
- **Common surrogates**: sigmoid, atan, exponential, piecewise linear
- **Pros**: End-to-end differentiable, high accuracy on standard benchmarks
- **Cons**: Biologically implausible, high memory for BPTT, not hardware-friendly
- **Use when**: Maximum accuracy needed, no hardware constraints

### 2. Local Learning Rules
- **STDP variants**: Pair-based, triplet, voltage-dependent, reward-modulated
- **Hebbian rules**: Correlation-based weight updates using pre/post activity
- **Pros**: Biologically plausible, low memory, online-capable, hardware-friendly
- **Cons**: Lower accuracy on complex tasks, limited credit assignment
- **Key finding**: Competitive accuracy on image classification with significantly lower memory footprint than backprop

### 3. Three-Factor Learning Rules
- **Mechanism**: Pre-synaptic * Post-synaptic * Modulatory signal (dopamine/error)
- **Bridges**: Hebbian plasticity and supervised learning
- **Implementation**: 
  ```python
  # Three-factor update
  delta_w = pre_spike * post_trace * modulatory_signal
  w += learning_rate * delta_w
  ```
- **Use when**: Need biological plausibility with supervised signal

### 4. Predictive Coding
- **Principle**: Minimize prediction error at each layer
- **Energy efficiency**: Local computation, no global error backpropagation
- **Edge deployment**: Suitable for neuromorphic hardware with power constraints
- **Implementation pattern**:
  ```python
  # Each layer predicts next layer's activity
  prediction = W @ current_state
  error = target - prediction
  weight_update = error @ current_state.T  # Local Hebbian
  ```

### 5. Neuromodulated Plasticity
- **Mechanism**: Global neuromodulator (dopamine, acetylcholine) gates local plasticity
- **Temporal credit assignment**: Solves distal reward problem
- **Biological basis**: Matches experimental findings in cortex

## Benchmarking Framework Guidelines

### Evaluation Dimensions
1. **Accuracy**: Classification/regression performance on standard datasets
2. **Memory footprint**: Parameters + activations during training
3. **Compute efficiency**: FLOPs, energy consumption estimates
4. **Biological plausibility**: How closely matches known neural mechanisms
5. **Hardware compatibility**: Suitability for neuromorphic deployment
6. **Scalability**: Performance with network size and task complexity

### Standard Datasets for SNN Benchmarking
- **Static images**: MNIST, CIFAR-10, CIFAR-100, ImageNet subsets
- **Dynamic/Temporal**: N-MNIST, SHD, DVS-Gesture, Event-based datasets
- **Neuroscience**: Brain-computer interface datasets

### Reproducibility Checklist
- Fixed random seeds across all experiments
- Same network architecture across methods
- Consistent dataset splits
- Reported hyperparameter search ranges
- Training time/compute budget comparison

## Performance Trade-offs Summary

| Method | Accuracy | Memory | Bio-plausible | Hardware-friendly |
|--------|----------|--------|---------------|-------------------|
| Surrogate BP | High | High | Low | Low |
| Local (STDP) | Medium | Low | High | High |
| Three-factor | Medium-High | Low | High | High |
| Predictive Coding | Medium | Low-Med | High | High |
| Neuromodulated | Medium | Low | Very High | High |

## Implementation Patterns

### Converting ANN to SNN
```python
# Rate-based conversion
def ann_to_snn(ann_weights, T=100):
    snn_weights = ann_weights  # Direct transfer
    # Run with Poisson or rate encoding over T timesteps
    return snn_weights
```

### Local Learning with Eligibility Traces
```python
# Eligibility trace for temporal credit assignment
eligibility = decay * eligibility + pre_spike * post_trace
delta_w = learning_rate * eligibility * reward_prediction_error
```

## Related Skills
- **snn-learning-survey**: Comprehensive SNN learning rules
- **spikingjelly-framework**: SNN implementation framework
- **multi-plasticity-snn-training**: Multi-plasticity synergistic training
- **three-factor-snn-learning**: Three-factor learning rules
