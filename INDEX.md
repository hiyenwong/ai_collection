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

### Leveraging unlabelled data for generalizable neural population decoding
- [[mojo-ssl-neural-decoding]] - MOJO framework for joint SSL-SL neural decoding using unlabelled data. (arXiv: 2607.14086)
  - Combines self-supervised learning via masked autoencoding with supervised learning objectives
  - Superior performance over purely SL-trained models, especially with limited labelled data
  - Enables few-shot finetuning with minimal labelled data from new sessions
  - Generalizes beyond spiking data to human electrocorticography during speech
  - **Activation**: MOJO framework, masked autoencoder neural decoding, self-supervised spiking neural networks, joint SSL-SL neural training, unlabelled neural data decoding, few-shot neural decoding, cross-modal neural foundation models

### Spiking Sequence Machines and Transformers
- [[spiking-transformer-unification]] - Theoretical framework unifying SNNs and Transformers through shared computational primitives. (arXiv: 2605.00662)
  - Shows both architectures implement five shared functional operations: encoding, context maintenance, associative retrieval, storage, and decoding
  - Establishes Phase-Latency Isomorphism linking spike timing to sinusoidal positional encoding
  - Demonstrates cosine similarity as shared retrieval primitive between Spiking SDM and Transformer attention
  - **Activation**: spiking transformer, spike-timing attention, phase-latency isomorphism, sparse distributed memory SNN, positional encoding theory, sequence learning theory, SNN transformer unification, cosine similarity retrieval

### Synaptic delays modulate population phase and amplitude responses in oscillatory excitatory-inhibitory networks
- [[synaptic-delays-oscillatory-ei-networks]] - Synaptic delays regulate collective response of neuronal populations to transient perturbations in PING regime E-I networks. (arXiv: 2608.15077)
  - Demonstrates frequency-coherence trade-off: increasing delay slows oscillations while enhancing synchrony
  - Shows differential delay-dependent modulation: inhibitory perturbations show stronger phase/amplitude effects than excitatory
  - Uses network Phase Response Curves (nPRCs) and Amplitude Response Curves (nARCs) for comprehensive analysis
  - **Activation**: synaptic delays oscillatory networks, delay-dependent phase response, nPRC nARC computation, PING regime synaptic delay

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

## 2026-08-20 - Systems Engineering Research (Cron Job)

### Extending and Unifying the Fundamental Tasks of Hamilton-Jacobi Reachability Analysis
- [[hamilton-jacobi-reachability-analysis]] - Generalized Reach-Avoid (GRA) task framework that extends and unifies canonical Hamilton-Jacobi Reachability tasks (arXiv: 2608.18060v1)
  - Introduces GRA as common primitive for fundamental HJR tasks
  - Enables computation of value functions for composite tasks including timed temporal logic
  - Provides PDE perspective showing GRA represents all sufficiently regular HJ-PDE solutions
  - **Activation**: Hamilton-Jacobi reachability, control systems verification, GRA tasks

### The geometric Laplace transform: Definition, existence and properties of the Geometric Algebra Laplace transform
- [[geometric-laplace-transform-systems]] - Geometric Algebra Laplace transform framework for system modeling and analysis (arXiv: 2608.18043v1)
  - First rigorous definition of Laplace transform within Geometric Algebra framework
  - Enables transformation of ODEs from real domain to Laplace domain in GA
  - Direct application to electrical circuit modeling and analysis
  - **Activation**: geometric algebra Laplace transform, GA system modeling, electrical circuit GA analysis

## 2026-08-21 - Neuroscience Research (Cron Job)

### Accurate Decoding of Natural Sentences from Non-Invasive Brain Recordings
- [[brain2qwerty-v2-noninvasive-decoding]] - Brain2Qwerty v2: non-invasive MEG sentence decoding (arXiv: 2608.18114)
  - Decodes natural sentences from real-time MEG with 39% average WER, best participant achieves 50% accuracy with ≤1 word error
  - Leverages character/word/sentence-level representations and AI-driven pipeline refinement via LLM fine-tuning
  - Performance log-linearly improves with data volume, bridging gap with intracranial approaches
  - **Activation**: brain2qwerty, non-invasive bci, meg decoding, brain-to-text

### Transcranial magnetic stimulation of visual-motion area V5/MT modulates sensory thalamus responses during visual speech recognition
- [[tms-v5-mt-modulates-thalamus-visual-speech]] - TMS of V5/MT modulates thalamus during visual speech recognition. (arXiv: 2608.19034)
  - Demonstrates causal role of visual-motion area V5/MT in modulating lateral geniculate nucleus (LGN) responses during visual speech recognition
  - Inhibitory TMS over V5/MT significantly reduced LGN signal modulation between visual speech and color tasks
  - V5/MT stimulation reduced task-dependent functional connectivity between V5/MT and LGN
  - **Activation**: transcranial magnetic stimulation, visual speech recognition, corticothalamic feedback, lateral geniculate nucleus, V5/MT area, fMRI thalamus

### The Role of Grid Cells in Reducing Spatial Aliasing in Hippocampal Place Representations
- [[grid-cells-reduce-spatial-aliasing-hippocampal-place]] - Grid cells reduce spatial aliasing in place representations. (arXiv: 2608.18569)
  - Grid cells achieve 94-99% reduction in spatial aliasing compared to BVC-only baseline
  - Greatest improvement occurs in environments with highest visual symmetry
  - Demonstrates complementary information from grid cells vs boundary-based inputs
  - **Activation**: grid cells, place cells, spatial aliasing, boundary vector cells, hippocampal representations, spatial navigation

## 2026-08-21 - Deep Learning Research (Cron Job)

### MLREF: Efficient Module Reuse for Reward Design in Reinforcement Learning via Large Language Models
- [[mlref-module-reward-evolution-framework]] - MLREF framework for efficient module reuse in reward design using LLMs to evolve specialized reward modules. (arXiv: 2608.18827)
  - Evolves specialized reward modules using LLMs instead of handcrafting or end-to-end learning
  - Enables modular composition of reward functions for complex multi-objective tasks
  - Achieves superior performance on WebArena benchmark compared to standard approaches
  - **Activation**: mlref, reward design, reinforcement learning, module reuse, llm reward evolution

### Beyond Teacher Likelihood: Group-Calibrated On-Policy Distillation for Long-Context Reasoning
- [[gc-opd-group-calibrated-on-policy-distillation]] - Group-Calibrated On-Policy Distillation (GC-OPD) framework addressing teacher-student distribution shift in long-context reasoning. (arXiv: 2608.19181)
  - Addresses distribution shift between teacher and student in long-context reasoning tasks
  - Introduces group calibration to maintain alignment across different context lengths
  - Improves performance on long-context benchmarks like LongBench and GovReports
  - **Activation**: gc-opd, on-policy distillation, long-context reasoning, group calibration, teacher-student alignment

### Open-MOPD: Diagnosing and Fixing Capability Imbalance in Multi-Teacher On-Policy Distillation
- [[open-mopd-multi-teacher-on-policy-distillation]] - Open-MOPD framework for diagnosing and fixing capability imbalance in multi-teacher on-policy distillation. (arXiv: 2608.19098)
  - Diagnoses capability integration gap where standard M-OPD captures only 35.6% of available headroom
  - Implements token-share balancing, gap-aware dynamic budget allocation, and student reward refresh
  - Improves headroom recovery from 35.6% to 83.4% in a single deployable student
  - **Activation**: open-mopd, multi-teacher distillation, capability imbalance, on-policy distillation, generalist student

### Monroe: A Molecular Foundation Model for In-Context Probabilistic Inference
- [[monroe-molecular-foundation-model]] - Monroe molecular foundation model for in-context probabilistic inference using prior-data-fitted models (TabPFN). (arXiv: 2608.18982)
  - Pre-trained on 81+ million molecules from PM6 quantum chemistry dataset
  - Uses enhanced graph representation with stereochemistry awareness
  - Integrates with TabPFN for in-context few-shot learning without fine-tuning
  - Achieves significant improvements on activity cliff benchmarks for drug discovery
  - **Activation**: monroe, molecular foundation model, in-context learning, TabPFN, bioassay prediction
## 2026-08-21 - Systems Engineering Research (Cron Job)

### Distributionally Robust MPC for Networked Control Systems with Partial Observability
- [[distributionally-robust-mpc-partial-observability]] - Distributionally robust MPC methodology combining Wasserstein ambiguity sets with recursive feasibility guarantees for systems with partial observability and model uncertainty (arXiv: 2608.05103)
  - 30% model mismatch tolerance while maintaining constraint satisfaction
  - 40% sensor dropout resilience with recursive feasibility guarantees
  - **Activation**: distributionally robust mpc, partial observability control, wasserstein ambiguity sets
