## 2026-08-11 - Neuroscience Research (Cron Job)

### PTQ4SNN: Membrane-Aware Post-Training Quantization for Spiking Neural Networks
- [[ptq4snn-membrane-aware-post-training-quantization]] - PTQ4SNN membrane-aware SNN quantization framework for joint weight and membrane state quantization without retraining. (arXiv: 2608.07066)
  - Addresses critical gap in SNN deployment by quantizing both weights and recurrent membrane states using only small calibration set
  - Introduces Channel-wise Unified Scale Bridge constraining membrane scale as s_mem,c = s_w,c * 2^k_c for hardware efficiency
  - Implements Mixed-Precision Bit Allocation assigning 2/4/8-bit precision based on firing activity and quantization sensitivity
  - Supports both convolutional SNNs and spike-driven Transformers with reusable projection-LIF architecture
  - **Activation**: PTQ4SNN, membrane quantization, SNN quantization, post-training quantization, spiking neural networks, neuromorphic deployment, low-bit SNN

### FedDOSE: Federated Learning Framework Decomposing Site Effects for Modeling Brain Dynamic Functional Connectivity
- [[feddose-federated-learning-dynamic-functional-connectivity]] - Novel federated learning framework that explicitly decomposes site effects for dynamic functional connectivity analysis using Modularity-Guided Tucker Decomposition and class-specific prototypes with Optimal Transport barycenter formulation. (arXiv: 2608.07393)
  - Addresses statistical heterogeneity and site differences in multi-site fMRI datasets through explicit site effect decomposition
  - Introduces Modularity-Guided Tucker Decomposition to encode high-dimensional dFC tensors and capture modular-level spatio-temporal patterns
  - Uses class-specific prototypes aligned globally via Optimal Transport barycenter formulation and Procrustes analysis
  - Outperforms state-of-the-art methods in ASD and ADHD detection on ABIDE-I, ABIDE-II, and ADHD-200 datasets
  - **Activation**: FedDOSE federated learning, Dynamic functional connectivity dFC, Multi-site fMRI privacy, Modularity-Guided Tucker Decomposition, Optimal Transport barycenter fMRI

### International Transfer of Stochastic Cortical Self-Reconstruction
- [[international-transfer-stochastic-cortical-self-reconstruction]] - Stochastic Cortical Self-Reconstruction (SCSR) framework for personalized mapping of gray matter atrophy with cross-population transferability evaluation from UK Biobank to Chinese dataset. (arXiv: 2608.07092)
  - Estimates individualized healthy reference directly from observed cortical thickness at vertex level for subtle subject-specific deviation detection
  - Evaluates four training strategies: direct application, fine-tuning, training from scratch, and joint training across populations
  - Compares MLP and Spherical UNet reconstruction backbones with fine-tuned SUNet achieving highest discriminative performance (AUC = 0.848)
  - Demonstrates strong cross-population transferability with low reconstruction errors across lifespan despite narrow training age distribution
  - **Activation**: Stochastic Cortical Self-Reconstruction, SCSR personalized mapping, Gray matter atrophy vertex-level, Cross-population transfer neuroimaging, UK Biobank Chinese dataset

## 2026-08-10 - Neuroscience Research (Cron Job)

### PTQ4SNN: Membrane-Aware Post-Training Quantization for Spiking Neural Networks
- [[ptq4snn-membrane-aware-quantization]] - Framework that jointly quantizes weights and recurrent membrane states using channel-wise Unified Scale Bridge and Mixed-Precision Bit Allocation. (arXiv: 2608.07066)
  - Channel-wise Unified Scale Bridge constrains membrane scale as `s_mem,c = s_w,c * 2^k_c` for shift-compatible scale conversion
  - Mixed-Precision Bit Allocation assigns 2/4/8-bit precision to membrane channels based on firing activity and quantization sensitivity
  - Enables full low-bit SNN deployment while preserving accuracy under W4 weight quantization and ~4-bit membrane precision
  - **Activation**: PTQ4SNN, membrane-aware quantization, SNN quantization, post-training quantization spiking, membrane state quantization, unified scale bridge, mixed-precision SNN

### Effective pruning of task-trained recurrent neural networks using noisy fluctuations and connection rescaling
- [[effective-pruning-task-trained-rnn-noisy-fluctuations]] - Noise-prune preserves task performance in RNNs. (arXiv: 2608.05464)
  - Biologically-plausible local pruning rule using noisy fluctuations to determine connection importance
  - Samples connections to preserve based on importance and strengthens retained connections
  - Outperforms magnitude-based pruning and matches/exceeds second-order methods
  - Optimal empirical rescaling factor is lower than theoretical prediction
  - **Activation**: noise-prune, RNN pruning, biologically plausible pruning, task-trained RNN, connection rescaling, noisy fluctuations

## 2026-08-10 - Anthropic Research (Cron Job)

### An off switch for dual-use knowledge in AI models
- [[off-switch-dual-use-knowledge-control]] - GRAM methodology for controlling dual-use knowledge in AI models with an off switch.
  - Gradient-Routed Auxiliary Modules (GRAM) provide selective control over harmful capabilities
  - Auxiliary modules can be disabled at inference time without affecting other model functions
  - Enables training with gradient routing to selectively enable/disable capabilities
  - **Activation**: off switch dual use, GRAM methodology, gradient-routed auxiliary modules, dual-use knowledge control, harmful capability disable, selective model control, Anthropic off switch

### Discovering cryptographic weaknesses with Claude
- [[discovering-cryptographic-weaknesses-claude]] - Methodology for discovering cryptographic weaknesses using Claude AI.
  - Systematic analysis of cryptographic code and protocols for potential weaknesses
  - Leverages Claude's pattern recognition to identify known vulnerability patterns and novel attack vectors
  - Constructs formal proofs or counterexamples to demonstrate identified weaknesses
  - **Activation**: discovering cryptographic weaknesses, Claude cryptography analysis, AI red teaming cryptography, cryptographic vulnerability discovery, automated crypto analysis, Anthropic frontier red team, cryptographic weakness identification

## 2026-08-10 - Quantum Reservoir Computing Thermodynamics (Cron Job)

### Thermodynamics of Quantum Reservoir Computing
- [[thermodynamics-quantum-reservoir-computing]] - Non-equilibrium thermodynamic framework linking predictive performance to energetic costs in quantum reservoir computing. Establishes fundamental trade-offs between computational capacity and thermodynamic dissipation (arXiv: 2608.02157)
  - Computational peak in quantum critical region originates from spectral resonance aligning internal transition frequencies with chaotic drive
  - Generalized Landauer bound reveals fundamental trade-off: critical resonance maximizes both predictive capacity and irreversible work
  - Quantum coherences amplify predictive capacity without demanding additional mechanical work
  - **Activation**: quantum reservoir computing thermodynamics, quantum critical region reservoir, informational dissipation quantum, Landauer bound temporal processing, quantum coherence predictive capacity
## 2026-08-10 - Systems Engineering Research (Cron Job)

### From Passive Mirrors to Active Agents: Holonic Digital Twins for Physical AI over Networks
- [[holonic-digital-twins-physical-ai-networks]] - HDT-Nets framework for Physical AI over Networks. Combines digital twins, wireless networks, and active inference for cyber-physical systems (arXiv: 2608.06227)
  - Hierarchical holonic agents spanning physical assets and network edge with local autonomy and collective intelligence
  - Causal Markov blankets determine multi-domain coordination across sensing, communication, and control
  - Active inference unifies perception, action, and learning by minimizing expected free energy
  - Category theory preserves semantic structure across heterogeneous agent representations
  - Integrated information theory quantifies collective intelligence evolution through coordinated learning
  - **Activation**: holonic digital twins, physical AI networks, HDT-Nets, active inference cyber-physical, causal Markov blankets

## 2026-08-11 - Neuroscience Research (Cron Job)

### PTQ4SNN: Membrane-Aware Post-Training Quantization for Spiking Neural Networks
- [[ptq4snn-membrane-aware-post-training-quantization]] - PTQ4SNN membrane-aware SNN quantization framework for joint weight and membrane state quantization without retraining. (arXiv: 2608.07066)
  - Addresses critical gap in SNN deployment by quantizing both weights and recurrent membrane states using only small calibration set
  - Introduces Channel-wise Unified Scale Bridge constraining membrane scale as s_mem,c = s_w,c * 2^k_c for hardware efficiency
  - Implements Mixed-Precision Bit Allocation assigning 2/4/8-bit precision based on firing activity and quantization sensitivity
  - Supports both convolutional SNNs and spike-driven Transformers with reusable projection-LIF architecture
  - **Activation**: PTQ4SNN, membrane quantization, SNN quantization, post-training quantization, spiking neural networks, neuromorphic deployment, low-bit SNN

### FedDOSE: Federated Learning Framework Decomposing Site Effects for Modeling Brain Dynamic Functional Connectivity
- [[feddose-federated-learning-dynamic-functional-connectivity]] - Novel federated learning framework that explicitly decomposes site effects for dynamic functional connectivity analysis using Modularity-Guided Tucker Decomposition and class-specific prototypes with Optimal Transport barycenter formulation. (arXiv: 2608.07393)
  - Addresses statistical heterogeneity and site differences in multi-site fMRI datasets through explicit site effect decomposition
  - Introduces Modularity-Guided Tucker Decomposition to encode high-dimensional dFC tensors and capture modular-level spatio-temporal patterns
  - Uses class-specific prototypes aligned globally via Optimal Transport barycenter formulation and Procrustes analysis
  - Outperforms state-of-the-art methods in ASD and ADHD detection on ABIDE-I, ABIDE-II, and ADHD-200 datasets
  - **Activation**: FedDOSE federated learning, Dynamic functional connectivity dFC, Multi-site fMRI privacy, Modularity-Guided Tucker Decomposition, Optimal Transport barycenter fMRI

### International Transfer of Stochastic Cortical Self-Reconstruction
- [[international-transfer-stochastic-cortical-self-reconstruction]] - Stochastic Cortical Self-Reconstruction (SCSR) framework for personalized mapping of gray matter atrophy with cross-population transferability evaluation from UK Biobank to Chinese dataset. (arXiv: 2608.07092)
  - Estimates individualized healthy reference directly from observed cortical thickness at vertex level for subtle subject-specific deviation detection
  - Evaluates four training strategies: direct application, fine-tuning, training from scratch, and joint training across populations
  - Compares MLP and Spherical UNet reconstruction backbones with fine-tuned SUNet achieving highest discriminative performance (AUC = 0.848)
  - Demonstrates strong cross-population transferability with low reconstruction errors across lifespan despite narrow training age distribution
  - **Activation**: Stochastic Cortical Self-Reconstruction, SCSR personalized mapping, Gray matter atrophy vertex-level, Cross-population transfer neuroimaging, UK Biobank Chinese dataset

## 2026-08-10 - Neuroscience Research (Cron Job)

### From Local Learning to Global Prediction Through Layered Surprise Cascades
- [[layered-surprise-cascades-predictive-coding]] - Biologically plausible predictive coding framework using local contrastive learning and activity cancellation. Builds on Forward-Forward algorithm with inverted objective for negative data (arXiv: 2608.05481)
  - Predictive representations emerge from simple local learning rules without explicit error neurons
  - Captures hallmark features of cortical computation like top-down modulation and surprise signaling
  - **Activation**: predictive coding, layered surprise cascades, forward-forward algorithm, hierarchical prediction, cortical computation, surprise signaling

### Convergent Evolution in Neural Representation Space: Emergent Order in Deep Belief Networks
- [[convergent-evolution-neural-representation-space]] - DBNs spontaneously organize representations by class without supervision. (arXiv: 2608.05996)
  - Class-specific clustering increases with network depth despite no label information during training
  - First hidden layers make class identity more accessible to linear and nonlinear probes
  - Deeper representations become increasingly compact and prototype-like with correlated feature directions
  - **Activation**: convergent evolution neural representation, deep belief networks unsupervised, class-specific clustering, emergent order DBN, generalized discrimination value, prototype-like representations

### Complexity and Stability of Neural Activity Across Aging and Neurodegenerative Disease
- [[complexity-stability-neural-activity-aging-disease]] - Distribution-level framework for understanding neural stability across cognition, aging, and disease. Uses Wasserstein distance to quantify temporal stability and intrinsic dimensionality to capture representational complexity (arXiv: 2608.05882)
  - Neural representations show constrained, condition-specific stability rather than unconstrained drift
  - Higher intrinsic dimensionality consistently associated with lower stability across datasets
  - Posterior regions show higher dimensionality and lower stability than frontal regions
  - Healthy aging shows increased dimensionality and reduced stability; MCI/Alzheimer's show joint collapse
  - **Activation**: neural stability, representational complexity, Wasserstein distance, intrinsic dimensionality, cognitive aging

### Convergent Evolution in Algorithmic Space
- [[convergent-evolution-algorithmic-space]] - Framework for analyzing convergent evolution in neural network weight structures during training. Uses matching-based comparison with permutation-invariant features and Hungarian matching to align hidden neurons, then applies structural distance metrics to identify task-specific attractors in weight space (arXiv: 2608.05985)
  - Permutation-invariant alignment using coarse features followed by Hungarian matching refinement
  - Task-specific attractors demonstrated across MNIST, Fashion-MNIST, and KMNIST datasets
  - Early morphogenesis shows rapid accuracy improvement before structural separation is visible
  - Coordinated weight drift begins early while coarse morphology remains unchanged
  - **Activation**: convergent evolution, algorithmic space, structural weight space, neural network comparison

### IRIS: A Visual Cortex-Inspired Framework for Analyzing Orientation Selectivity in Vision Transformers
- [[iris-visual-cortex-framework-vit]] - IRIS framework providing neuroscience-inspired metrics (RSS, ORS, orientation tuning bandwidth) to quantify how orientation selectivity emerges in ViTs and tracks biologically-grounded features during training (arXiv: 2608.05122)
  - Neuroscience-inspired metrics: RSS, ORS, and orientation tuning bandwidth for systematic analysis
  - Training paradigm is strongest determinant of orientation selectivity regardless of model scale  
  - Early-to-middle layers recruit orientation-selective units while deeper layers lose selectivity
  - Provides mechanistic heuristic for downstream task fine-tuning based on layer selectivity patterns
  - **Activation**: IRIS framework, orientation selectivity, vision transformers, visual cortex, representational similarity

## 2026-07-25 - Neuroscience Research (Cron Job)

### CogniSNN: Enabling Neuron-Expandability, Pathway-Reusability, and Dynamic-Configurability with Random Graph Architectures in Spiking Neural Networks
- [[cognisnn-random-graph-architecture]] - CogniSNN framework for scalable spiking neural networks with random graph architectures enabling neuron-expandability, pathway-reusability, and dynamic-configurability (arXiv: 2512.11743)
  - Introduces Random Graph Architecture (RGA) to overcome rigid hierarchical limitations of traditional ANNs
  - Implements Key Pathway-based Learning without Forgetting (KP-LwF) using Betweenness Centrality for continual learning
  - Features Dynamic Growth Learning (DGL) algorithm for temporal dimension structural plasticity
  - **Activation**: cognisnn, random graph architecture, neuron expandability, pathway reusability, dynamic configurability
## 2026-08-11 - Deep Learning Research (Cron Job)

### Beyond Isolation: Unlocking Reinforcement Learning Component Synergy for Sample-Efficient Continuous Control
- [[roser-rl-component-synergy]] - ROSER framework coordinating Model-based Representation, Optimization Stability, and Experience Replay for sample-efficient RL. (arXiv: 2608.07086v1)
  - Efficacy of RL components exhibits significant task-dependency
  - Naive stacking of SOTA techniques often triggers emergent challenges like compounded non-stationarity
  - Achieves 17.60% gains over naive component stacking across continuous-control benchmarks
  - **Activation**: roser, rl component synergy, sample-efficient, continuous control, model-based representation, optimization stability, experience replay

### Simple-OPD: Demystifying Warm-up for On-policy Distillation
- [[simple-opd-on-policy-distillation]] - Plug-and-play initialization method using teacher-compatible CoT with LoRA for OPD warm-up. (arXiv: 2608.06802v1)
  - Effective warm-up relies on teacher-compatible chain-of-thought supervision rather than just correct answers
  - Even incorrect teacher rollouts provide comparable benefits to correct ones
  - LoRA with near-saturation training duration better balances in-domain adaptation and out-of-distribution generalization
  - **Activation**: simple-opd, on-policy distillation, warm-up, teacher-compatible CoT, LoRA warm-up, chain-of-thought transfer

### Beyond Foundation Models: Dimension-Aware Neural Architecture Search with Small-Data Representation Models for Cryocooler Lifetime Prediction
- [[fsd-rm-small-data-representation]] - FSD-RM paradigm using established encoders with dimension-aware NAS for small-data representation learning. (arXiv: 2608.06993v1)
  - Uses proven architectures (CNN1D, LSTM, GRU, Transformer) suitable for small-data regimes
  - Employs dimension-aware neural architecture search to jointly optimize model capacity and input dimensionality
  - Achieves competitive predictive performance while reducing training cost and model complexity
  - **Activation**: fsd-rm, small-data, representation learning, dimension-aware nas, telemetry, cryocooler, time-series
