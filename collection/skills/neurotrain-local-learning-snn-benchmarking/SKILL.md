---
name: neurotrain-local-learning-snn-benchmarking
description: "Comprehensive survey and open benchmarking framework for local learning rules in Spiking Neural Networks (SNNs). Covers taxonomy of training methods (direct training, ANN-to-SNN conversion, optimization), local learning paradigms, and the NeuroTrain framework for reproducible research. Activation: neurotrain, local learning SNN, SNN training survey, snn benchmarking, spiking neural network training rules, local learning rules."
---

# NeuroTrain: Local Learning Rules for Spiking Neural Networks with Open Benchmarking Framework

**arXiv:** 2605.15058v1 [cs.NE] | **Published:** 2026-05-14
**Authors:** Alessio Caviglia, Filippo Marostica, Roberta Bardini, Alessandro Savino, Stefano Di Carlo (Politecnico di Torino)

## Core Contribution

This paper provides (i) a unified taxonomy-driven review of SNN training algorithms with emphasis on local learning methods, and (ii) **NeuroTrain**, an open-source snnTorch-based framework for reproducible implementation, comparison, and benchmarking of SNN training rules.

## Taxonomy of SNN Training Methods

### Three Main Learning Strategies

1. **Direct SNN Training** — learning performed while explicitly simulating spiking dynamics during optimization
2. **ANN-to-SNN Conversion** — train a ReLU-ANN first, then convert activations to spiking neurons
3. **Optimization (Gradient-free)** — treat the network as a black box evaluated against a fitness function

### Categorization Axes

The taxonomy organizes training algorithms along explicit axes:

- **Training strategy** (direct / conversion / optimization)
- **Learning paradigm** (supervised / unsupervised / reinforcement learning)
- **Spatial locality** (local vs. non-local error propagation)
- **Temporal locality** (online vs. requiring full sequence storage)
- **Biological plausibility** (how closely the method maps to known synaptic plasticity)

### Key Training Algorithm Families

#### Direct Training Methods

1. **Surrogate Gradient BPTT**
   - Replace non-differentiable spike derivative ∂S[t]/∂U[t] with bounded proxy
   - Treat SNN as discretized RNN, unroll over time
   - Back-Propagation Through Time (BPTT) with surrogate gradients is the dominant approach
   - SuperSpike: spike-train distance optimization

2. **Eligibility Traces** (temporal credit assignment)
   - Factorize gradients into synapse-specific eligibility trace × learning signal
   - Enable online updates without storing entire unrolled trajectory
   - e-prop: forward-only learning with eligibility traces
   - FPTT (Forward Propagation Through Time): recast temporal credit as consensus problem

3. **Direct Feedback Alignment (DFA)**
   - Broadcast error to all layers simultaneously via fixed random projections
   - Avoids weight transport problem but still requires full forward pass completion

4. **Direct Random Target Projection (DRTP)**
   - Similar to DFA but with random target projection

5. **Auxiliary Local Classifiers**
   - Add local classifiers at intermediate layers
   - Spatial backpropagation with online temporal credit assignment

6. **Forward-Forward Algorithm** (adapted to SNNs)
   - Accumulated spike counts as goodness measure
   - Layer normalization between layers to decouple representations
   - Decouples learning across depth

#### Unsupervised Approaches

- **STDP-inspired mechanisms**: Spike-Timing-Dependent Plasticity
  - Early hierarchical SNNs with rank-order temporal coding
  - Limited to ~5 layers, accuracy on CIFAR-10 below supervised methods
  - Modern contrastive and generative approaches extend capabilities
- **Hebbian learning**: local correlation-based weight updates

#### Reinforcement Learning in SNNs

- **R-STDP** (Reward-modulated STDP): local reward-modulated rules
  - Theoretical foundations by Florian (2007), Izhikevich (2007)
  - Unified taxonomy: R-max, R-STDP, TD-STDP (Frémaux & Gerstner, 2016)
  - Limited to shallow architectures
- **Deep spiking RL**: hybrid actor-critic with surrogate gradients
  - DSQN (Deep Spiking Q-Network): competitive on 17 Atari games
  - Spiking world models: recent trend for closing performance gap

#### ANN-to-SNN Conversion

- Train deep ReLU-ANN (VGG, ResNet), replace activations with LIF/IF neurons
- Quantize-aware training (QKDs): first method to achieve zero conversion loss
- **Advantages**: easiest route to deploying pretrained models on neuromorphic hardware, highest accuracies on static datasets
- **Limitations**: network never trains on spike-based representations, can't exploit temporal coding or adapt to event-driven inputs

### Locality Spectrum

| Method | Spatial Locality | Temporal Locality | Hardware Mapping |
|--------|-----------------|-------------------|------------------|
| STDP | Local | Local | Excellent |
| R-STDP | Local | Local | Good |
| Eligibility Traces | Non-local | Local | Moderate |
| DFA/DRTP | Non-local | Non-local | Limited |
| Surrogate BPTT | Non-local | Non-local | Limited |
| ANN-SNN Conversion | Non-local | N/A | Good |

## NeuroTrain Framework

### Architecture

Built on **snnTorch** + **PyTorch**, NeuroTrain enforces clear separation:

1. **Dataloaders** — dataset loading and preprocessing
2. **Models** — network architectures (SNN models)
3. **Trainers** — training rules/algorithms (the core contribution)
4. **Benchmarking Engine** — automates experiments by combining trainers, models, dataloaders

### Design Principles

- **Encapsulation**: learning rules are decoupled from network models
- **Incompatibility handling**: defined within objects, exposed to engine during experiments
- **Reproducibility**: unified framework eliminates algorithm-specific evaluation scripts
- **Extensibility**: open resource for community contributions

### Goal

Move beyond isolated, algorithm-specific evaluation scripts toward an open benchmarking ecosystem for the SNN community — similar to the role shared benchmarks play in deep learning.

## Key Findings

1. **Locality-Performance Tradeoff**: Relaxing spatial locality generally improves training performance on challenging benchmarks, but reduces neuromorphic hardware compatibility
2. **Surrogate gradients dominate** direct training for complex tasks
3. **Local learning remains essential** for online adaptation and low-power deployment
4. **No unified benchmarking framework** existed prior to NeuroTrain — field was fragmented
5. **Gradient-free methods** useful for black-box optimization but limited scalability
6. **Spiking RL** spans wide locality range: R-STDP (fully local) → e-prop (temporally local) → surrogate BPTT (non-local)

## Open Challenges

1. **Closing the performance gap** between highly local, hardware-friendly rules and globally trained deep spiking systems
2. **Standardized benchmarking** across methods, datasets, and metrics
3. **Temporal coding exploitation** in conversion-based approaches
4. **Large-scale SNN architectures** with local learning rules
5. **Continual learning** with spiking plasticity mechanisms

## Technical Implementation Details

### Surrogate Gradient Pipeline
- SNN → discretized RNN → unroll over time → surrogate gradient in backward pass
- Key: replace Heaviside step function derivative with smooth approximation (sigmoid, piecewise linear, etc.)

### Eligibility Trace Mechanism
- Gradient factorization: `∂L/∂w = eligibility_trace × learning_signal`
- Eligibility trace: forward-computed state variable at each synapse
- Learning signal: broadcast (possibly global) error or reward

### STDP Mechanism
- Pre-synaptic spike timing relative to post-synaptic spike determines weight change
- Δw ∝ f(Δt_pre - Δt_post)
- Causal: pre before post → potentiation (LTP)
- Anti-causal: post before pre → depression (LTD)

## Activation Keywords

- neurotrain
- local learning SNN
- SNN training survey
- snn benchmarking
- spiking neural network training rules
- local learning rules
- surrogate gradient SNN
- eligibility traces SNN
- STDP SNN training
- e-prop
- ANN to SNN conversion
- reward-modulated STDP
- R-STDP
- snnTorch
- neuromorphic computing training

## Related Skills

- **spiking-neural-network-analysis**: Analyze SNN papers and extract patterns
- **spikingjelly-framework**: SNN deep learning framework usage
- **snn-learning-survey**: Comprehensive survey of SNN learning rules
- **spiking-computational-neuroscience-survey**: SNN applications in computational neuroscience
- **brain-inspired-snn-pattern-analysis**: Extract patterns from brain-inspired SNN papers

## References

- arXiv: [2605.15058](https://arxiv.org/abs/2605.15058)
- PDF: [Download](https://arxiv.org/pdf/2605.15058)
- License: CC BY 4.0
