---
name: neurotrain-local-learning-snn-benchmarking
description: >
  Comprehensive taxonomy and benchmarking framework for Spiking Neural Network (SNN)
  local learning rules. Covers surrogate-gradient backpropagation, local/three-factor
  learning rules, biologically inspired plasticity mechanisms, ANN-to-SNN conversion,
  and non-standard optimization. Based on NeuroTrain survey (arXiv:2605.15058).
  Activation: SNN training, local learning rules, spiking neural network benchmarking,
  surrogate gradient, three-factor learning, STDP, neurotrain, snnTorch, local plasticity,
  脉冲神经网络训练, 局部学习规则, 替代梯度, 三因素学习
---

# NeuroTrain: SNN Local Learning Rules Taxonomy & Benchmarking

Comprehensive framework for understanding, comparing, and implementing local learning
rules for Spiking Neural Networks (SNNs). Based on the NeuroTrain survey and open-source
benchmarking framework.

## SNN Training Taxonomy

### 1. Surrogate-Gradient Backpropagation
- **Principle**: Approximate the non-differentiable spike function with a smooth surrogate
- **Key methods**: SLAYER, SuperSpike, e-prop
- **Locality**: Backward pass requires global error signal
- **Strengths**: High accuracy, compatible with deep architectures
- **Weaknesses**: Biologically implausible, requires backward weight transport

### 2. Local Learning Rules
- **Principle**: Weight updates depend only on pre/post-synaptic activity and local signals
- **Key methods**:
  - Spike-Timing-Dependent Plasticity (STDP)
  - Temporal Difference Learning
  - Eligibility Trace-based methods
- **Locality**: Fully local — suitable for neuromorphic hardware
- **Strengths**: Biological plausibility, energy efficiency, online learning
- **Weaknesses**: Lower accuracy on complex tasks, limited scalability

### 3. Three-Factor Learning
- **Principle**: Weight update = f(pre_activity, post_activity, modulatory_signal)
- **Key methods**:
  - Reward-modulated STDP
  - Feedback Alignment (local error)
  - e-prop with local eligibility traces
- **Locality**: Local with global broadcast signal
- **Strengths**: Biological plausibility (dopamine as modulator), RL-compatible
- **Weaknesses**: Requires global signal broadcast

### 4. ANN-to-SNN Conversion
- **Principle**: Train ANN first, then convert to equivalent SNN
- **Key methods**: Rate-based conversion, spike-based conversion
- **Strengths**: Leverages mature ANN training, high accuracy
- **Weaknesses**: High latency, no temporal processing, conversion overhead

### 5. Biologically Inspired Plasticity
- **Key mechanisms**:
  - Homeostatic plasticity (synaptic scaling)
  - Metaplasticity (plasticity of plasticity)
  - Structural plasticity (synapse formation/pruning)
  - Astrocyte-mediated plasticity

## NeuroTrain Framework Architecture

```
NeuroTrain (snnTorch-based)
├── Dataset module (MNIST, CIFAR, N-MNIST, etc.)
├── Model module (feedforward, recurrent, convolutional SNNs)
├── Learning module (taxonomy-implemented algorithms)
├── Evaluation module (accuracy, energy, latency, spike sparsity)
└── Benchmark module (cross-algorithm comparison)
```

## Key Benchmarking Dimensions

### 1. Accuracy
- Classification accuracy on standard benchmarks
- Trade-off with biological plausibility

### 2. Energy Efficiency
- Total spike count (proxy for energy)
- Operations per inference
- Hardware deployment efficiency

### 3. Training Dynamics
- Convergence speed
- Sample efficiency
- Stability during training

### 4. Scalability
- Performance with network depth/width
- Performance with temporal horizon
- Memory requirements

## Practical Implementation Patterns

### STDP Implementation (snnTorch)
```python
import snntorch as snn
import snntorch.functional as SF

# Pre/post-synaptic spike traces
pre_trace = torch.zeros_like(w)
post_trace = torch.zeros_like(w)

# STDP weight update
def stdp_update(w, pre_spikes, post_spikes, 
                pre_trace, post_trace,
                lr=0.01, tau_trace=20.0):
    # Trace updates
    pre_trace = pre_trace * torch.exp(-dt/tau_trace) + pre_spikes
    post_trace = post_trace * torch.exp(-dt/tau_trace) + post_spikes
    
    # Hebbian term (pre → post)
    dw_hebbian = lr * torch.outer(post_spikes, pre_trace)
    
    # Anti-Hebbian term (post → pre)
    dw_anti = -lr * torch.outer(post_trace, pre_spikes)
    
    return w + dw_hebbian + dw_anti
```

### Three-Factor Learning with Eligibility Traces
```python
# Eligibility trace (local memory of pre/post coincidence)
eligibility = torch.zeros_like(w)

def three_factor_update(w, eligibility, modulatory_signal, lr=0.01):
    # Update eligibility: e_t = ρ*e_{t-1} + pre * post
    eligibility = rho * eligibility + pre_spikes * post_spikes
    
    # Apply modulatory signal (reward, error, dopamine)
    dw = lr * modulatory_signal * eligibility
    
    return w + dw, eligibility
```

## Hardware Suitability Matrix

| Method | Loihi 2 | SpiNNaker | BrainScaleS | GPU | CPU |
|--------|---------|-----------|-------------|-----|-----|
| STDP | ✅ | ✅ | ✅ | ❌ | ❌ |
| Three-factor | ✅ | ✅ | ⚠️ | ⚠️ | ⚠️ |
| Surrogate | ❌ | ❌ | ❌ | ✅ | ⚠️ |
| ANN→SNN | ❌ | ❌ | ⚠️ | ✅ | ✅ |

## Open Challenges

1. **Scaling local rules**: How to achieve deep network performance with purely local learning?
2. **Credit assignment**: Can local rules approximate backpropagation quality?
3. **Hybrid approaches**: Combining global supervision with local plasticity
4. **Hardware-aware design**: Co-designing algorithms with neuromorphic constraints
5. **Temporal credit**: Long-range temporal dependencies in local learning

## Related Skills

- **snn-learning-survey**: Comprehensive SNN learning rule overview
- **spikingjelly-framework**: SNN deep learning framework
- **decolle-snn-learning**: Deep continuous local learning

## References

- Caviglia et al., "NeuroTrain: Surveying Local Learning Rules for Spiking Neural Networks with an Open Benchmarking Framework", arXiv:2605.15058 (2026)
- Zenke et al., "E-prop: Approximate gradients for spike trains", Nature Communications (2021)
- Bellec et al., "A solution to the learning dilemma for recurrent networks of spiking neurons", Nature Communications (2020)
