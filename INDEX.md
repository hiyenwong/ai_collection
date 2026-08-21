## 2026-08-22 - Neuroscience Research (Cron Job)

### Decoding silent reading from non-invasive EEG
- [[eeg-silent-reading-decoding]] - EEG-based silent reading decoding framework for scalable inner speech BCI using contrastive learning (arXiv: 2608.20186)
  - Uses silent reading as scalable proxy task to overcome fundamental data problem in inner speech decoding
  - Demonstrates data-limited decoding that scales log-linearly with training data volume
  - Shows removing occipital/posterior-temporal electrodes reduces word-level gain by one-third
  - **Activation**: silent reading, EEG decoding, inner speech BCI, non-invasive brain-computer interface, contrastive decoder

### Spike-based Belief Propagation in Nonlinear Dynamical Systems
- [[spike-belief-propagation-nonlinear-dynamics]] - Bayesian control framework integrating spiking neural models with probabilistic inference for adaptive control (arXiv: 2608.19907)
  - Combines biologically inspired spiking dynamics with Bayesian inference for real-time state updates
  - Demonstrates goal-directed action planning through spike-driven dynamics on mountain car benchmark
  - Bridges computational neuroscience and probabilistic control theory
  - **Activation**: spike belief propagation, bayesian spiking control, nonlinear dynamical systems, probabilistic inference spiking, mountain car spiking

### Active Spiking Perception
- [[active-spiking-perception-3d-recognition]] - Active Spiking Perception framework for 3D recognition using membrane potential as decision-making mechanism (arXiv: 2608.19232)
  - Uses leaky integrate-and-fire (LIF) membrane potential as running belief over class for active chunk selection
  - Provides certified anytime interface with confidence-margin early exit and linear observation cost
  - Achieves 90.62% on ModelNet40 while adding only ~2% backbone parameters
  - **Activation**: active spiking perception, membrane potential decision making, 3D recognition spiking networks, anytime spiking inference, Bayesian spiking filters

## 2026-08-21 - Neuroscience Research (Cron Job)

### The Connectome and the Quest for the Functional Logic of the Drosophila Early Olfactory System
- [[drosophila-olfactory-connectome-functional-logic]] - Framework for understanding Drosophila olfactory system functional logic through connectome analysis, feedback loop abstractions, and natural odorant environment modeling (arXiv: 2608.19290)
  - Moves beyond static wiring diagrams to understand dense local feedback circuits governing input/output transformations
  - Requires explicit modeling of natural odorant environment with semantics and syntax for associative memory operations
  - Treats circuit as real-time, stage-by-stage cascade of giant local feedback loops respecting causality
  - **Activation**: drosophila olfactory, fruit fly connectome, olfactory feedback circuits, functional logic neural circuits
## 2026-08-19 - Neuroscience Research (Cron Job)

### Learning Generalizable Reconstruction of High-Dimensional Neural Dynamics
- [[pca-dmd-neural-dynamics-reconstruction]] - PCA-DMD framework for scalable neural dynamics reconstruction with zero-shot cross-subject generalization. (arXiv: 2608.16569)
  - Segments LFP recordings into overlapping windows, projects into PCA space, learns Koopman evolution
  - Achieves 0.9504-0.9800 correlations in cross-subject zero-shot generalization
  - Scalable from 400k to 900k samples with stable performance
  - **Activation**: pca-dmd, neural dynamics reconstruction, koopman operator neuroscience

### Lonic: Algorithm-Hardware Co-Design for Energy-Efficient Fully Local Online SNN Training with INT4 Precision### Lonic: Algorithm-Hardware Co-Design for Energy-Efficient Fully Local Online SNN Training with INT4 Precision
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

## 2026-08-20 - Neuroscience Research (Cron Job)

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

## 2026-08-22 - Deep Learning Research (Cron Job)

### Task-CoEvolve: Efficient Harness Optimization via Adaptive Validation
- [[task-coevolve-adaptive-validation-task-selection]] - Adaptive validation for LLM harness optimization. (arXiv: 2608.20169)
  - Uses adaptive validation set selection to optimize task-specific harnesses
  - Dynamically adjusts validation criteria based on model performance
  - Improves efficiency of LLM agent deployment and evaluation
  - **Activation**: task-coevolve, adaptive validation, LLM harness optimization, task selection

### Scale-Aware Pretraining of Time Series Foundation Models via Multi-Patch Token Alignment
- [[scale-aware-pretraining-time-series-foundation]] - Scale-aware pretraining for time series foundation models. (arXiv: 2608.20005)
  - Treats patch size as explicit notion of scale with contrastive-inspired alignment regularizer
  - Uses hybrid masking strategy combining random and contiguous masking
  - Achieves 9.2% improvement in MSE on LSTF benchmarks and 8.3% gain in GIFT-Eval MASE
  - **Activation**: scale-aware pretraining, time series foundation models, multi-patch token alignment, hybrid masking, heterogeneous time series

### RIPE++: Reinforced Keypoint Learning from Positive Pairs Only
- [[ripe-plus-plus-reinforced-keypoint-learning]] - Reinforced keypoint learning from positive pairs only. (arXiv: 2608.19693)
  - Derives both reward and penalty from single positive pair without contrasting against negatives
  - Learns discriminative detectors and descriptors from positive image pairs alone
  - Raises AUC@5 on MegaDepth1500 from 56.58 to 59.65
  - **Activation**: ripe++, reinforced keypoint learning, positive pairs only, geometric consistency reward, weakly-supervised matching

### Truncate Bad, Upweight Good: BoN-Style Distillation via Ranking
- [[truncate-upweight-distillation-rank-based]] - TUP: Rank-based distillation via truncation and upweighting. (arXiv: 2608.19748)
  - Truncates bottom portion of samples based on quality scores or rankings
  - Upweights remaining high-quality samples proportionally to their ranks
  - Flexible quality assessment through likelihood scores, reward model outputs, or human preferences
  - **Activation**: TUP distillation, truncate upweight good, rank-based distillation, BoN-style distillation, quality-based truncation