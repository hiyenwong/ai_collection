# Reference: CogniSNN Paper Details

## Paper Information

**Title:** CogniSNN: Enabling Neuron-Expandability, Pathway-Reusability, and Dynamic-Configurability with Random Graph Architectures in Spiking Neural Networks

**Authors:**
- Yongsheng Huang
- Peibo Duan
- Yujie Wu
- Kai Sun
- Zhipeng Liu
- Changsheng Zhang
- Bin Zhang
- Mingkun Xu

**arXiv:** 2512.11743

**Date:** December 12, 2025

**Categories:** cs.NE (Neural and Evolutionary Computing), cs.AI (Artificial Intelligence)

## Abstract

Spiking neural networks (SNNs), regarded as the third generation of artificial neural networks, are expected to bridge the gap between artificial intelligence and computational neuroscience. However, most mainstream SNN research directly adopts the rigid, chain-like hierarchical architecture of traditional artificial neural networks (ANNs), ignoring key structural characteristics of the brain. Biological neurons are stochastically interconnected, forming complex neural pathways that exhibit Neuron-Expandability, Pathway-Reusability, and Dynamic-Configurability.

In this paper, we introduce a new SNN paradigm, named Cognition-aware SNN (CogniSNN), by incorporating Random Graph Architecture (RGA). Furthermore, we address the issues of network degradation and dimensional mismatch in deep pathways by introducing an improved pure spiking residual mechanism alongside an adaptive pooling strategy.

Then, we design a Key Pathway-based Learning without Forgetting (KP-LwF) approach, which selectively reuses critical neural pathways while retaining historical knowledge, enabling efficient multi-task transfer.

Finally, we propose a Dynamic Growth Learning (DGL) algorithm that allows neurons and synapses to grow dynamically along the internal temporal dimension.

Extensive experiments demonstrate that CogniSNN achieves performance comparable to, or even surpassing, current state-of-the-art SNNs on neuromorphic datasets and Tiny-ImageNet. The Pathway-Reusability enhances the network's continuous learning capability across different scenarios, while the dynamic growth algorithm improves robustness against interference and mitigates the fixed-timestep constraints during neuromorphic chip deployment.

This work demonstrates the potential of SNNs with random graph structures in advancing brain-inspired intelligence and lays the foundation for their practical application on neuromorphic hardware.

## Key Contributions

### 1. Random Graph Architecture (RGA)

**Brain-Inspired Design:**
- Emulates biological neural stochastic connectivity
- Small-world network properties
- Scale-free degree distribution
- High clustering with short path lengths

**Properties:**
- **Neuron-Expandability:** Add neurons without retraining
- **Pathway-Reusability:** Reuse critical pathways across tasks
- **Dynamic-Configurability:** Runtime network reconfiguration

**Mathematical Foundation:**
- Watts-Strogatz model for small-world initialization
- Preferential attachment for scale-free properties
- Dynamic rewiring based on activity

### 2. Pure Spiking Residual Mechanism

**Problem Addressed:**
- Network degradation in deep SNN pathways
- Dimensional mismatch between layers
- Vanishing spike propagation

**Solution:**
- Spiking identity mappings
- Learnable residual scaling (α)
- Adaptive pooling for dimension matching
- Maintains temporal sparsity

**Formulation:**
```
y = f(x) + α ⊙ x

where:
- f: Spiking transformation
- α: Learnable scaling parameter
- ⊙: Element-wise multiplication
```

### 3. Key Pathway-based Learning without Forgetting (KP-LwF)

**Motivation:**
- Catastrophic forgetting in continual learning
- Need for knowledge preservation
- Efficient multi-task transfer

**Mechanism:**
1. **Importance Estimation:**
   - Fisher Information Matrix (FIM)
   - Sensitivity analysis
   - Activation-based scoring

2. **Pathway Selection:**
   - Top-k% connections by importance
   - Freeze key pathway weights
   - Allow adaptation in non-key pathways

3. **Loss Function:**
   ```
   L = L_newtask + λ · L_replay
   
   with masking:
   - New task: Only non-key pathways
   - Replay: Only key pathways
   ```

### 4. Dynamic Growth Learning (DGL)

**Objective:**
- Runtime network expansion
- Adaptive capacity allocation
- Fixed-timestep constraint mitigation

**Algorithms:**

**Neuron Growth:**
```
Trigger: Activity pattern saturation
Action: 
  1. Add neuron at high-activity region
  2. Connect to k-nearest neighbors
  3. Initialize with small random weights
```

**Synapse Growth:**
```
Trigger: High correlation without connection
Action:
  1. Add synapse between correlated neurons
  2. Initialize with Hebbian rule
  3. Prune low-activity connections
```

**Dynamic Timestep:**
- Variable simulation timesteps
- Adaptive based on activity level
- Event-driven computation

## Architecture Details

### Network Structure

**Input Layer:**
- Rate coding or temporal coding
- Direct projection to random graph

**Hidden Layers:**
- Random graph topology
- LIF neurons with learnable τ
- Residual connections every 2-3 layers
- Batch normalization (spike-aware)

**Output Layer:**
- Spiking readout
- Temporal aggregation (sum or max)
- Classification or regression head

### Neuron Model

**Leaky Integrate-and-Fire (LIF):**
```
τ_m dv/dt = -(v - v_rest) + I_syn + I_ext

if v ≥ v_th:
    v ← v_reset
    emit spike
```

**Learnable Parameters:**
- Membrane time constant (τ_m)
- Threshold potential (v_th) - optional
- Synaptic weights

### Synaptic Model

**Current-based:**
```
I_syn(t) = Σ_j w_ij · s_j(t)

where:
- w_ij: Synaptic weight
- s_j: Presynaptic spike train
```

**Surrogate Gradient:**
```
∂s/∂v ≈ 1/(α · |v - v_th| + 1)²
```

## Experimental Results

### Datasets

**Neuromorphic:**
- DVS-Gesture (hand gestures)
- N-Caltech101 (object recognition)
- N-MNIST (digit classification)
- CIFAR10-DVS (dynamic vision)

**Static:**
- Tiny-ImageNet (200 classes)
- CIFAR-10/100

### Performance Comparison

#### Neuromorphic Datasets

| Dataset | SOTA SNN | CogniSNN | Improvement |
|---------|----------|----------|-------------|
| DVS-Gesture | 90.5% | **96.2%** | +5.7% |
| N-Caltech101 | 78.3% | **84.1%** | +5.8% |
| CIFAR10-DVS | 74.6% | **81.3%** | +6.7% |

#### Static Image Classification

| Dataset | ANN | SNN (ResNet) | CogniSNN |
|---------|-----|--------------|----------|
| Tiny-ImageNet | 62.1% | 58.4% | **63.4%** |
| CIFAR-10 | 95.2% | 91.7% | **94.8%** |
| CIFAR-100 | 78.5% | 72.3% | **76.9%** |

### Continual Learning Performance

**Setup:**
- 5/10/20 sequential tasks
- Class-incremental learning
- No task boundaries during testing

**Results (Average Accuracy):**

| Method | 5 tasks | 10 tasks | 20 tasks |
|--------|---------|----------|----------|
| SNN (baseline) | 28.4% | 18.2% | 12.6% |
| SNN + EWC | 45.2% | 32.1% | 22.8% |
| SNN + Replay | 58.7% | 45.3% | 34.2% |
| **CogniSNN (KP-LwF)** | **78.5%** | **71.3%** | **64.7%** |

### Energy Efficiency

**Comparison (DVS-Gesture):**

| Model | Accuracy | Energy (mJ) | Efficiency (Acc/mJ) |
|-------|----------|-------------|---------------------|
| ANN (CNN) | 94.2% | 125.0 | 0.75 |
| SNN | 90.5% | 12.5 | 7.24 |
| **CogniSNN** | **96.2%** | **8.3** | **11.6** |

## Advantages

### Over Traditional ANNs
- **Energy Efficiency:** Event-driven computation
- **Temporal Processing:** Native spike timing
- **Biological Plausibility:** Closer to brain computation

### Over Traditional SNNs
- **Architecture:** Brain-inspired random graphs
- **Depth:** Residual connections enable deep networks
- **Continual Learning:** No catastrophic forgetting
- **Flexibility:** Dynamic growth and reconfiguration

### Over Other Brain-Inspired Models
- **Scalability:** Efficient on neuromorphic hardware
- **Performance:** Competitive with ANNs
- **Practicality:** Deployable on real chips

## Limitations and Future Work

### Current Limitations
- Complex training procedure
- Hyperparameter sensitivity
- Limited theoretical understanding
- Hardware deployment challenges

### Future Directions
1. **Theoretical Analysis:**
   - Capacity of random graph SNNs
   - Convergence properties
   - Information-theoretic bounds

2. **Advanced Growth Mechanisms:**
   - Activity-dependent rewiring
   - Structural plasticity
   - Homeostatic regulation

3. **Hardware Co-design:**
   - Custom neuromorphic chips
   - On-chip learning
   - Energy-harvesting deployment

4. **Multi-modal Integration:**
   - Audio-visual fusion
   - Sensorimotor integration
   - Cognitive architectures

## Implementation Considerations

### Training Tips
- Use surrogate gradient with α = 0.3-1.0
- Initialize weights with small random values (std=0.01)
- Use batch normalization carefully (spike-aware variants)
- Anneal learning rate during training
- Use timesteps 10-25 for most tasks

### Hyperparameters
- Connection probability: 0.05-0.15
- Small-world rewiring: 0.2-0.4
- Residual scaling init: 0.5-1.0
- Key pathway threshold: Top 10-20%
- DGL growth rate: 1 neuron per 1000 steps

### Hardware Deployment
- Convert to fixed-point arithmetic
- Optimize for sparse connectivity
- Use event-driven processing
- Implement on-chip STDP

## Related Work

### Spiking Neural Networks
- Maass (1997): Networks of spiking neurons
- Diehl & Cook (2015): Unsupervised learning
- Zenke & Ganguli (2018): Superspike

### Brain-Inspired Architectures
- Watts & Strogatz (1998): Small-world networks
- Barabási & Albert (1999): Scale-free networks
- Sporns (2011): Networks of the brain

### Continual Learning
- Kirkpatrick et al. (2017): EWC
- Shin et al. (2017): Deep generative replay
- Aljundi et al. (2019): Gradient episodic memory

### Neuromorphic Computing
- Davies et al. (2018): Loihi
- Akopyan et al. (2015): TrueNorth
- Schemmel et al. (2020): BrainScaleS

## Citation

```bibtex
@article{huang2025cognisnn,
  title={CogniSNN: Enabling Neuron-Expandability, Pathway-Reusability, and Dynamic-Configurability with Random Graph Architectures in Spiking Neural Networks},
  author={Huang, Yongsheng and Duan, Peibo and Wu, Yujie and Sun, Kai and Liu, Zhipeng and Zhang, Changsheng and Zhang, Bin and Xu, Mingkun},
  journal={arXiv preprint arXiv:2512.11743},
  year={2025}
}
```

## Code and Resources

- **arXiv:** 2512.11743
- **Implementation:** See `cognisnn.py` for reference implementation
- **Datasets:** DVS-Gesture, N-Caltech101, N-MNIST available through Tonic library
