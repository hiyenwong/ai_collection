---
name: neurotrain-local-learning-snn-benchmarking
description: >
  NeuroTrain methodology for surveying and benchmarking local learning rules
  in Spiking Neural Networks (SNNs). Covers comprehensive taxonomy of SNN
  training algorithms (surrogate-gradient BP, local/three-factor rules,
  bio-inspired plasticity, ANN-to-SNN conversion, non-standard optimization)
  and provides open-source snnTorch-based benchmarking framework.
  Use when: benchmarking SNN training algorithms, comparing local learning
  rules, implementing biologically plausible plasticity, or surveying SNN
  training methods. arXiv: 2605.15058
  Activation: NeuroTrain, SNN benchmarking, local learning rules,
  surrogate gradient, three-factor learning, snnTorch, SNN training taxonomy.
---

# NeuroTrain: SNN Local Learning Rules Survey & Benchmarking

## Paper Reference

- **Title:** NeuroTrain: Surveying Local Learning Rules for Spiking Neural Networks with an Open Benchmarking Framework
- **arXiv:** 2605.15058 (2026-05-14)
- **Authors:** Alessio Caviglia, Filippo Marostica, Roberta Bardini, Alessandro Savino, Stefano Di Carlo

## SNN Training Taxonomy

### 1. Surrogate-Gradient Backpropagation (SGBP)
- **Mechanism:** Smooth surrogate derivatives replace non-differentiable Heaviside during BP
- **Key methods:** SuperSpike (arctan), STE (Straight-Through Estimator), Multi-Gaussian
- **Locality:** Global error signal, non-local weight updates
- **Hardware:** GPU-friendly, less neuromorphic-compatible
- **Pros:** High accuracy, end-to-end trainable
- **Cons:** Biologically implausible, memory-intensive (BPTT)

### 2. Local Learning Rules
- **Mechanism:** Weight updates depend only on pre/post-synaptic activity + local eligibility traces
- **Key methods:** Hebbian, STDP, anti-Hebbian, Oja's rule
- **Locality:** Fully local (synapse-level)
- **Hardware:** Neuromorphic-compatible (Loihi, SpiNNaker)
- **Pros:** Biologically plausible, online learning, low memory
- **Cons:** Lower accuracy on complex tasks

### 3. Three-Factor Learning
- **Mechanism:** Local eligibility trace × global modulatory signal (reward/error)
- **Key methods:** Reward-modulated STDP (R-STDP), e-prop, three-factor Hebbian
- **Locality:** Semi-local (eligibility local, modulation global)
- **Hardware:** Compatible with neuromorphic + gradient hardware
- **Pros:** Balance of biological plausibility and learning power
- **Cons:** Requires global signal design

### 4. Bio-Inspired Plasticity
- **Mechanism:** Homeostatic scaling, metaplasticity, structural plasticity
- **Key methods:** BCM rule, synaptic scaling, dendritic computation
- **Focus:** Long-term stability, avoiding catastrophic forgetting
- **Use case:** Continual learning, lifelong adaptation

### 5. ANN-to-SNN Conversion
- **Mechanism:** Train ANN, convert weights to SNN via rate coding
- **Key methods:** Direct weight transfer, threshold balancing, latency reduction
- **Pros:** Leverages mature ANN training, good accuracy
- **Cons:** High latency, temporal dynamics lost

### 6. Non-Standard Optimization
- **Evolutionary:** NEAT, genetic algorithms for SNN topology + weights
- **Reinforcement:** Q-learning with spiking policies
- **Bayesian:** Probabilistic spiking models

## Benchmarking Framework (NeuroTrain)

### Architecture
- **Base:** snnTorch library
- **Design:** Modular, extendable pipeline
- **Components:**
  - Dataset loaders (MNIST, CIFAR-10, N-MNIST, DVS-Gesture)
  - Architecture templates (feedforward, convolutional, recurrent SNN)
  - Training algorithm implementations
  - Evaluation metrics (accuracy, spike count, energy proxy, latency)

### Evaluation Dimensions
1. **Accuracy:** Task performance on standard benchmarks
2. **Efficiency:** Spike sparsity, energy proxy (synaptic ops)
3. **Biological Plausibility:** Locality index, temporal credit assignment depth
4. **Hardware Suitability:** Neuromorphic compatibility score
5. **Scalability:** Training time, memory footprint vs. network size

## Open Challenges

1. **Unified Metrics:** No consensus on "fair" comparison across heterogeneous methods
2. **Temporal Credit Assignment:** Local rules struggle with long-range dependencies
3. **Hardware-Algorithm Co-Design:** Gap between algorithm performance and hardware realization
4. **Scalability:** Most local rules tested on small networks (<10K neurons)
5. **Theoretical Understanding:** Limited convergence guarantees for local learning

## Practical Recommendations

### For Neuromorphic Deployment
- Prefer three-factor learning or local STDP variants
- Avoid BPTT-based methods (memory overhead)
- Use rate coding for inference stability

### For Maximum Accuracy
- Use surrogate-gradient BP (SuperSpike or Multi-Gaussian surrogate)
- Consider ANN-to-SNN conversion for well-understood tasks
- Hybrid approaches: SGBP for training, local rules for fine-tuning

### For Continual Learning
- Three-factor learning with homeostatic plasticity
- Structural plasticity for growing/shrinking networks
- Avoid catastrophic forgetting with synaptic consolidation
