## 2026-08-19 - Neuroscience Research (Cron Job)

### Learning Generalizable Reconstruction of High-Dimensional Neural Dynamics
- [[pca-dmd-neural-dynamics-reconstruction]] - PCA-DMD framework for scalable neural dynamics reconstruction with zero-shot cross-subject generalization. (arXiv: 2608.16569)
  - Segments LFP recordings into overlapping windows, projects into PCA space, learns Koopman evolution
  - Achieves 0.9504-0.9800 correlations in cross-subject zero-shot generalization
  - Scalable from 400k to 900k samples with stable performance
  - **Activation**: pca-dmd, neural dynamics reconstruction, koopman operator neuroscience

### Lonic: Algorithm-Hardware Co-Design for Energy-Efficient Fully Local Online SNN Training with INT4 Precision
- [[lonic-algorithm-hardware-codesign]] - Lonic INT4 algorithm-hardware co-design for energy-efficient SNN training (arXiv: 2608.12500)
  - INT4 low-precision fully local online SNN training algorithms
  - Reconfigurable multiplier-free integer PE arrays for hardware efficiency
  - Dual-optimization zero-gating strategy and temporal prefix-accelerated dataflow
  - **Activation**: lonic, INT4 SNN training, algorithm-hardware co-design

## 2026-08-19 - Systems Engineering Research (Cron Job)

### Threshold-Based Spiking Neural Networks for Event-Driven Status Update Systems
- [[threshold-based-snn-event-driven-status-update-systems]] - Optimal threshold policies for event-driven IoT status updates that jointly minimize Age of Information (AoI) and transmission energy. (arXiv: 2608.10640)
  - Proves existence of optimal threshold policy for MDP that jointly minimizes AoI and transmission energy
  - Proposes lightweight SNN architecture with explicit threshold policy representation and constant complexity
  - Enables more energy-efficient implementation than comparable ANNs while reliably learning optimal thresholds
  - Provides interpretable policy representation for event-driven IoT systems with randomly occurring wake-up events
  - **Activation**: threshold-based spiking neural network, event-driven status update, age of information optimization, energy-efficient IoT, SNN threshold policy, event-driven IoT, information freshness energy trade-off, distributed event-driven systems, interpretable control policies, MDP threshold policies

## 2026-08-19 - Neuroscience Research (Cron Job)

### Noisy group neurons with synchronous resetting for high-performance spiking neural networks
- [[noisy-group-neurons-synchronous-resetting]] - NGN model with population-level synchronous resetting and neural stochasticity for high-performance SNNs. (arXiv: 2608.17394)
  - Introduces Noisy Group Neuron (NGN) model that simultaneously addresses spatiotemporal information loss and gradient mismatching in deep SNNs
  - Achieves 87.35% accuracy on CIFAR10-DVS within only 10 inference time steps through mean-field backpropagation
  - Incorporates neural stochasticity as computational resource and enables practical high-performance neuromorphic computing
  - **Activation**: noisy group neurons, NGN model, synchronous resetting, SNN training, gradient mismatching, neuromorphic computing, arxiv:2608.17394

### Phase-based spatial ordinal patterns for characterizing oscillatory dynamics
- [[phase-based-spatial-ordinal-patterns-oscillatory-dynamics]] - Spatial ordinal patterns for oscillatory dynamics. (arXiv: 2608.17196)
  - Introduces framework based on spatial ordinal patterns acting directly on phase rather than amplitude
  - Defines spatial permutation entropy that quantifies diversity of spatiotemporal patterns at each time point
  - Distinguishes phase-locked states with identical global synchronization but distinct spatial organization
  - Successfully applied to resting-state EEG recordings to distinguish eyes-open vs eyes-closed conditions within individuals
  - **Activation**: phase-based spatial ordinal patterns, spatial permutation entropy, oscillatory dynamics analysis, brain network phase analysis, EEG phase synchronization, transient dynamics detection, regime transition analysis

## 2026-08-20 - Neuroscience Research (Cron Job)

### Spiking Sequence Machines and Transformers
- [[spiking-transformer-unification]] - Theoretical framework unifying SNNs and Transformers through shared computational primitives. (arXiv: 2605.00662)
  - Shows both architectures implement five shared functional operations: encoding, context maintenance, associative retrieval, storage, and decoding
  - Establishes Phase-Latency Isomorphism linking spike timing to sinusoidal positional encoding
  - Demonstrates cosine similarity as shared retrieval primitive between Spiking SDM and Transformer attention
  - **Activation**: spiking transformer, spike-timing attention, phase-latency isomorphism, sparse distributed memory SNN, positional encoding theory, sequence learning theory, SNN transformer unification, cosine similarity retrieval

## 2026-08-20 - Deep Learning Research (Cron Job)

### Efficient RLVR Scheduling via Graph-Structured Online Difficulty Estimation
- [[graph-structured-online-difficulty-estimation]] - Graph-based RLVR difficulty estimation without probing overhead (arXiv: 2608.17941)
  - Uses semantic similarity graphs with Potts prior and Beta-Binomial model for continuous difficulty updates
  - Shares rollout feedback across related samples using graph structure
  - Provides cold start mitigation and continuous updates without dedicated probing
  - **Activation**: rlvr, difficulty estimation, graph-based scheduling

### Efficient Resource Optimization for Split Federated Learning
- [[split-federated-learning-resource-optimization]] - Polynomial-time optimal model splitting for SFL (arXiv: 2608.17849)
  - Achieves global optimum for model splitting problem in polynomial time
  - Provides (1+ε)-approximation guarantee for joint resource allocation
  - Optimally balances energy and latency costs under resource constraints
  - **Activation**: split federated learning, resource optimization, model splitting

### rl-triton: High-Performance Triton GPU Kernels for Reinforcement Learning Credit Assignment
- [[rl-triton-gpu-kernels-credit-assignment]] - Unified credit assignment via associative scan in Triton (arXiv: 2608.17641)
  - Unifies 7 RL credit assignment algorithms under single computational primitive
  - Achieves 1.6–5.7× speedup over state-of-the-art implementations
  - Optimized memory access patterns reduce bandwidth requirements
  - **Activation**: rl-triton, gpu kernels, credit assignment, triton

### Iterative tensor network transformations for element-wise evaluation of elementary functions
- [[iterative-tensor-network-transformations]] - Nonlinear tensor train operations via iterative transforms (arXiv: 2608.17135)
  - Handles arbitrary element-wise nonlinear functions on tensor trains
  - Converges through iterative refinement with controllable accuracy
  - Demonstrated on 3D flow fields and Max-SAT up to 2^70 states
  - **Activation**: tensor networks, tensor train, nonlinear operations

### EDITBRIDGE: Towards Faithful and Efficient Ultra-High-Resolution Image Editing
- [[editbridge-ultra-hdr-image-editing]] - Faithful 4K image editing via diffusion bridge framework (arXiv: 2608.18063)
  - Uses block-wise sparse attention for O(n) complexity instead of O(n²)
  - Direct HR source conditioning prevents hallucination
  - Completes 4K editing in 61 seconds on single GPU
  - **Activation**: editbridge, ultra-hdr, image editing, diffusion bridge