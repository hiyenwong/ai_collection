# Recent SNN Training Advances (May 2026)

## NeuroTrain: Comprehensive Taxonomy (arXiv:2605.15058)

### 6 Training Paradigms

1. **Surrogate-Gradient Backpropagation** — Replace non-differentiable spike function with smooth surrogate during backward pass. Common: sigmoid, arctan, triangular, Gaussian. Frameworks: snnTorch, SpyTorch, Norse.

2. **Local Learning Rules** — Pre/post-synaptic activity only. Hebbian, Anti-Hebbian, STDP.

3. **Three-Factor Learning Rules** — Δw = pre × post × modulator. Modulators: reward, attention, dopamine. Bridges local plasticity and global optimization.

4. **Biologically Inspired Plasticity** — Homeostatic plasticity, synaptic scaling, structural plasticity, metaplasticity.

5. **ANN-to-SNN Conversion** — Train ANN, convert via rate coding. Challenges: latency, accuracy gap.

6. **Non-Standard Optimization** — Evolutionary algorithms, RL, gradient-free.

### Comparison Matrix

| Criterion | Surrogate-GD | Local Rules | Three-Factor | ANN-to-SNN |
|-----------|-------------|-------------|--------------|------------|
| Biological plausibility | Low | High | Medium | Low |
| Hardware efficiency | Medium | High | High | High |
| Accuracy | High | Low-Medium | Medium | High |
| Training speed | Fast | Fast | Medium | Slow (2-phase) |
| Scalability | High | High | High | High |

### NeuroTrain Framework
- Built on snnTorch, modular architecture
- Unified API for benchmarking across datasets (MNIST, CIFAR, N-MNIST, DVS), architectures, and training regimes
- Addresses field-wide lack of standardized taxonomy and benchmark suite

## SeAl-KD: Selective Alignment Knowledge Distillation (arXiv:2605.14252)

### Core Insight
Not all timesteps matter equally. Intermediate predictions need not be individually correct when final aggregated output is correct.

### Method
- Equalize competing logits at erroneous timesteps
- Reweight temporal alignment by confidence × inter-timestep similarity
- Preserve useful temporal dynamics while correcting errors
- Evaluated on CIFAR-10/100, N-MNIST, DVS Gesture — consistent improvements over uniform KD
