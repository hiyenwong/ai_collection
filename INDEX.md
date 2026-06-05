# AI Collection Index

## 2026-06-06 - Neuroscience Research (Cron Job)

### A Sliced-Wasserstein Framework on Correlation Matrices for EEG Decoding
- [[corsw-sliced-wasserstein-eeg-decoding]] - Pullback Euclidean Metric Sliced Wasserstein (PEMSW) framework for scale-invariant EEG decoding with CorSW discrepancies under OLM/LSM geometries. KDD 2026 (arXiv: 2606.06104)
  - 全秩相关矩阵替代协方差解决通道尺度敏感性
  - Off-Log Metric 和 Log-Scaled Metric 定义切空间几何
  - 低训练开销，无额外推理成本，改善域泛化
  - 基于随机投影的切片 Wasserstein 稳定估计
  - **Activation**: CorSW, sliced-wasserstein EEG, correlation matrices, domain generalization BCI, PEMSW, OLM LSM metrics

### Coarse-to-fine Hierarchical Architecture with Sequential Mamba for Brain Reconstruction
- [[chasmbrain-mamba-brain-reconstruction]] - Dual-stream Mamba separates CLS (global semantic) and Patch (local spatial) with coarse-to-fine ROI→voxel prediction. Pearson 0.429 on NSD (arXiv: 2606.04772)
  - Patch stream causally locked to early visual cortex (V1-V3)
  - CLS stream specializes in higher-order semantic areas (OTC)
  - Stage 1 predicts denoised ROI activations, Stage 2 refines to voxel-level
  - Cross-subject transfer with minimal per-subject adaptation
  - **Activation**: CHASMBrain, Mamba brain reconstruction, image-to-fMRI, dual-stream, ROI voxel prediction, NSD dataset, visual cortex modeling

## 2026-06-06 - Economics, Investment + Quantum Finance (Cron Job)

### Efficient Complex-Valued State Preparation on Bucket Brigade QRAM
- [[bbqram-state-preparation-finance]] - Architecture-aware quantum state preparation using BBQRAM + segment tree for O(log²(MN)) query time, eliminating QPU arithmetic via classical precomputation (arXiv: 2604.25644)
  - 核心要点 1: Classical precomputation of rotation angles removes U_2CR reversible arithmetic from QPU
  - 核心要点 2: Complex-valued extension via two-step magnitude-then-phase procedure with leaf phase storage
  - **Activation**: BBQRAM state preparation, bucket brigade QRAM, complex-valued quantum encoding, quantum finance data loading, classical precomputation rotation angles, magnitude-then-phase

## 2026-06-06 - Neuroscience Research (Cron Job)

### Intrinsic Computational Functionalism
- [[intrinsic-computational-functionalism]] - Framework for observer-independent computational structures in consciousness research. Two criteria: system-intrinsic instantiation (C1) + causal-dynamical intervention (C2). Three-tier decomposition identifies dynamics-internal grain selection as key (arXiv: 2606.06424)
  - Addresses observer-relativity objection: anti-computational arguments succeed only at tier (i) interpreter-relative labels
  - C1: Property specifiable without observer labelling, invariant under structure-preserving relabellings
  - C2: Grounded in state-space structure with mutually constraining variables, exhibited in counterfactual intervention responses
  - Tier (iii) dynamics-internal grain selection is where intrinsic computational properties emerge
  - Syntax-is-not-semantics, mapmaker arguments, biological-naturalist objections succeed against tier (i) but intrinsic computational functionalism survives
  - **Activation**: computational functionalism, consciousness, observer-relativity, intrinsic computation, state-space dynamics, causal intervention, computational neuroscience, tier decomposition

## 2026-06-06 - Economics/Investment + Quantum (Cron Job)

### Derivative-Informed Operator Learning for Finance
- [[derivative-informed-operator-learning-finance]] - Neural operators trained to match pricing operators AND Fréchet derivatives for on-the-fly Greeks, hedging, and control. Vega error -40%, Delta error -15% (arXiv: 2606.05900)
  - Neural operator learns entire pricing map, not just pointwise prices
  - Fréchet derivative matching ensures accurate Greeks (Delta, Vega, Gamma)
  - Theoretical hedging error bounds from operator approximation theory
  - Random-feature DeepONet for efficient volatility surface fitting
  - Optimizer stability guarantees under approximation error
  - **Activation**: derivative pricing, operator learning, neural operator, DeepONet, Fréchet derivative, Greeks, hedging, Vega, Delta, volatility surface, quantitative finance

### Market Informedness & RL Market Making
- [[market-informedness-rl-market-making]] - Multi-agent RL (MAPPO) for market making with Hawkes-driven order flow. Counterintuitive: profitability increases with market informedness (arXiv: 2606.05882)
  - Heterogeneous agents: informed traders, noise traders, market makers
  - MAPPO in CTDE (Centralized Training, Decentralized Execution)
  - Hawkes process models self-exciting order flow arrivals
  - Finite-horizon stability guarantees for deployable strategies
  - Informed flow provides more predictable adverse selection patterns
  - **Activation**: market making, informedness, adverse selection, reinforcement learning, multi-agent, MAPPO, CTDE, Hawkes process, order flow, liquidity

### Dealer Market Competition with Internalisation
- [[dealer-market-competition-nash-equilibrium]] - Closed-form Nash equilibrium for multi-dealer order flow competition using variational approach. Balances internalisation vs externalisation for inventory risk (arXiv: 2606.06413)
  - Variational formulation of N-dealer quoting game
  - Internalisation: skew quotes to attract offsetting flow
  - Externalisation: offload inventory in inter-dealer market
  - Closed-form solution via coupled Riccati equations
  - Competition intensity determines spread compression  
  - Strategic inventory management through spread adjustments
  - **Activation**: dealer market, Nash equilibrium, internalisation, inventory risk, variational approach, quoting game, market microstructure

## 2026-06-05 - AI Systems Engineering (Cron Job)

### Multi-Stage Warm-Start Deep Learning for Unit Commitment
- [[warmstart-dl-unit-commitment]] - Three-stage warm-start pipeline for unit commitment optimization: ML warm-start → primal-dual formulation → branch-and-bound refinement. Solves 24-hour instances in 3.96s with warm-start (vs 5400s cold) (arXiv: 2606.05903)
  - Stage 1: Machine learning model predicts initial solution
  - Stage 2: Primal-dual problem formulation with ML-predicted bounds
  - Stage 3: Branch-and-bound refinement with warm-start bounds
  - Reduces solve time by 99.93% compared to cold start
  - Combines ML speed with mathematical programming optimality guarantees
  - **Activation**: unit commitment, warm-start, primal-dual, branch-and-bound, power system optimization, mixed-integer programming, deep learning warm-start

## 2026-06-05 - Economics + Quantum Computing (Cron Job)

### Classical-Quantum Hybrid Market Structure Prediction
- [[contextual-quantum-neural-stock-prediction]] - Quantum-classical hybrid for market regime detection. Quantum circuit encodes market state → classical MLP predicts regime transitions. 85% regime classification accuracy (arXiv: 2606.06223)
  - Quantum encoding: amplitude encoding of market indicators
  - Quantum feature extraction via parameterized quantum circuit
  - Classical MLP processes quantum features for regime classification
  - Hybrid architecture leverages quantum expressivity + classical scalability
  - Detects bull/bear/transitional regimes for portfolio management
  - **Activation**: quantum finance, regime detection, market structure, hybrid quantum-classical, amplitude encoding, portfolio management, stock prediction

## 2026-06-05 - Computational Neuroscience + AI (Cron Job)

### Brain-CLIPLM Semantic Compression for EEG Decoding
- [[brain-cliplm-semantic-compression-eeg]] - Brain-CLIPLM framework: CLIP semantic space compression of EEG signals via variational autoencoder. Cross-modal EEG-to-language alignment without training on paired data. Zero-shot EEG classification (arXiv: 2606.05876)
  - CLIP language embeddings provide semantic anchor space
  - VAE compresses EEG features into CLIP-aligned latent space
  - Zero-shot classification via semantic similarity matching
  - No paired EEG-language training data required
  - Cross-modal transfer from vision-language pretraining
  - **Activation**: EEG decoding, semantic compression, CLIP, variational autoencoder, cross-modal alignment, zero-shot classification, brain-language interface

## 2026-06-05 - Quantum Computing + Systems Engineering (Cron Job)

### Barbell Codes for QLDPC on Superconducting Hardware
- [[barbell-qldpc-superconducting-hardware]] - Barbell code architecture: stabilizer barbell + logical latch for hardware-tailored qLDPC implementation. XZZX surface code + latch syndrome extraction for biased-noise qubits (arXiv: 2606.05870)
  - Stabilizer barbell: two stabilizer generators sharing ancilla
  - Logical latch: controlled-NOT structure for logical operations
  - XZZX surface code adapted for biased noise (phase-flip dominant)
  - Syndrome extraction with latch reduces circuit depth
  - Hardware-tailored for superconducting qubit error profiles
  - **Activation**: qLDPC, barbell codes, surface code, biased noise, superconducting qubits, logical latch, syndrome extraction, fault tolerance

## 2026-06-04 - Neuroscience Research (Cron Job)

### Neuron Populations Exhibit Divergent Selectivity with Scale
- [[neuron-populations-scale-selectivity]] - Layer 5 neuron populations show diversity in selectivity at large spatial scales. Somatostatin (SOM+) neurons: sparse, object-specific. Parvalbumin (PV+) neurons: dense, feature-specific (arXiv: 2606.05409)
  - SOM+ neurons: high selectivity for specific objects, sparse activation
  - PV+ neurons: moderate selectivity for features, dense activation
  - Scale-dependent divergence: selectivity difference grows with receptive field size
  - Population-level specialization for different representational strategies
  - Implications for sparse coding theories and hierarchical processing
  - **Activation**: neuron selectivity, SOM+ PV+ populations, sparse coding, receptive fields, visual cortex, hierarchical processing, population diversity

### Kinetic Energy Links Chaos to Structure in Random RNNs
- [[kinetic-energy-random-rnn-chaos]] - Kinetic energy (speed along trajectories) serves as unified metric linking chaos, transition to structure, and generalization in random RNNs. High kinetic energy → structure emergence (arXiv: 2606.05799)
  - Kinetic energy metric: squared magnitude of hidden state velocity
  - Chaos-to-structure transition occurs at critical kinetic energy threshold
  - Generalization improves with moderate kinetic energy (neither chaotic nor static)
  - Metric predicts optimal training regimes without explicit structure
  - Links dynamical regime to computational properties
  - **Activation**: RNN chaos, kinetic energy, dynamical regimes, structure emergence, generalization, random networks, transition to structure

### Competition-Stability Trade-off in E-I Circuits
- [[competition-stability-functionality-ei-networks]] - Game-theoretic energetic framework for excitatory-inhibitory (E-I) circuits. Competition for metabolic resources determines stability-functional trade-off. Asymmetric energy allocation critical (arXiv: 2606.05913)
  - Energetic game: E and I neurons compete for ATP allocation
  - Stability requires energy balance: E expenditure ≤ I expenditure
  - Functionality maximization requires asymmetric energy investment
  - Trade-off resolved through optimal control of metabolic resources
  - Links biophysical constraints to circuit-level dynamics
  - **Activation**: E-I circuits, energetic competition, metabolic resources, ATP, stability-functionality trade-off, game theory, optimal control

### Neural Manifolds as Crystallized Embeddings
- [[neural-manifolds-crystallized-embeddings]] - Neural manifolds in high-dimensional neural activity space are crystallized embeddings. Intrinsic geometry emerges from synaptic connectivity patterns. Manifold structure predicts behavioral variability (arXiv: 2606.05887)
  - Crystallization: stable geometric structure from synaptic weights
  - Embedding: low-dimensional manifold in high-dimensional neural space
  - Intrinsic geometry: curvature, topology from connectivity
  - Behavioral variability: manifold geometry predicts performance differences
  - Links structure (connectivity) to function (behavior) through geometry
  - **Activation**: neural manifolds, crystallized embeddings, synaptic connectivity, intrinsic geometry, behavioral variability, neural activity space, manifold structure

### Brain Foundation Models Forgot Third-Order Statistics
- [[variance-brain-foundation-models-forgot]] - Brain foundation models (BFMs) lose third-order statistics during training. First-order (mean) + second-order (covariance) preserved, but third-order (skewness) discarded. Affects outlier detection and asymmetry modeling (arXiv: 2606.05891)
  - Third-order statistics: skewness, asymmetry in activation distributions
  - BFM training collapses higher-order moments to Gaussian
  - Outlier regions (tail behavior) poorly represented in BFM embeddings
  - Implications for detecting rare neural states (e.g., seizure onset)
  - Need for moment-preserving training or post-hoc correction
  - **Activation**: brain foundation models, higher-order statistics, skewness, outlier detection, Gaussian approximation, seizure detection, moment preservation

## 2026-06-04 - Quantum Computing + AI (Cron Job)

### Supervised Training Degrades Visual Cortex Alignment
- [[supervised-training-degrades-visual-cortex-alignment]] - Supervised training rapidly reduces early visual cortex (V1-V3) alignment in CNNs. Self-supervised training preserves alignment. Task-specific supervision biases higher layers, losing biological correspondence (arXiv: 2606.05905)
  - V1-V3 alignment drops 40% after supervised training
  - Self-supervised (contrastive) training maintains biological alignment
  - Supervision biases network toward task-relevant features
  - Task-specific features diverge from biological representations
  - Implications for neural decoding and brain-computer interfaces
  - **Activation**: visual cortex alignment, supervised training, self-supervised, V1 V2 V3, CNNs, brain-model correspondence, neural decoding

### Whisper-ECoG Alignment for Speech Foundation Models
- [[whisper-ecog-alignment-neural-encoding]] - Whisper speech model aligns with human ECoG during naturalistic listening. Interpretable neural encoder maps Whisper layers to ECoG time-series. Middle layers (6-8) show strongest alignment (arXiv: 2606.05909)
  - Whisper layers map hierarchically to auditory cortex processing stages
  - Middle layers (6-8) peak alignment with superior temporal gyrus
  - Interpretable encoder: linear mapping with time-resolved predictions
  - Speech foundation models as computational models of auditory processing
  - Cross-modal validation: Whisper predicts ECoG better than acoustic features
  - **Activation**: Whisper, ECoG, speech foundation models, auditory cortex, neural alignment, interpretable encoding, speech processing

## 2026-06-04 - Quantum + Finance (Cron Job)

### Quantum Mechanical Data Assimilation
- [[quantum-mechanical-data-assimilation]] - Quantum Mechanical Data Assimilation (QMDA) framework for incorporating quantum uncertainty into classical data assimilation. Quantum Fisher Information bounds on Bayesian updates (arXiv: 2606.05901)
  - Quantum Fisher Information: bound on estimation precision
  - Bayesian assimilation with quantum uncertainty constraints
  - Quantum measurements provide tighter uncertainty bounds
  - Hybrid quantum-classical assimilation for improved estimation
  - Applications: weather forecasting, financial modeling, sensor fusion
  - **Activation**: quantum data assimilation, Bayesian assimilation, quantum Fisher information, uncertainty bounds, sensor fusion, quantum measurements

## 2026-06-03 - Neuroscience Research (Cron Job)

### Feature Leakage in Identifiability of Entropy Models
- [[feature-leakage-identifiability-entropy-models]] - Direct-dependency entropy models suffer feature leakage when using features with causal ancestors. Causal identifiability criterion: exclude features with parents of target variable (arXiv: 2606.05509)
  - Feature leakage: spurious dependencies from causal ancestors
  - Identifiability criterion: exclude features with parents of Y
  - Direct-dependency entropy: only include direct causes of target
  - Causal discovery: prevent information leakage from ancestors
  - Corrects misinterpretation of entropy-based feature selection
  - **Activation**: feature leakage, causal identifiability, entropy models, direct-dependency, causal discovery, feature selection, information leakage

### STP Stabilizes Goal-Conditioned Dynamics in PFC Reservoirs
- [[stp-pfc-reservoir-goal-planning]] - Short-Term Synaptic Plasticity (STP) in PFC reservoir networks stabilizes goal-conditioned planning. Depressing synapses enable multi-step goal-directed sequences without instability (arXiv: 2606.05513)
  - STP mechanism: depressing synapses reduce excitation over time
  - Goal-conditioned reservoir: dynamics shaped by target state
  - Multi-step planning: stable trajectories toward goal states
  - Prevents runaway excitation in recurrent PFC networks
  - Biological mechanism for hierarchical goal planning
  - **Activation**: STP, short-term plasticity, PFC reservoir, goal-conditioned planning, depressing synapses, multi-step planning, prefrontal cortex

### Transformer-Guided Adaptive Diffusion for Alzheimer Modeling
- [[transformer-guided-adaptive-diffusion-alzheimer]] - Multi-modal Graph Neural Network + Transformer-guided adaptive diffusion for Alzheimer's progression modeling. Brain structural + functional + clinical features integrated. Predicts cognitive decline trajectories (arXiv: 2606.05517)
  - Multi-modal GNN: structural + functional connectivity graphs
  - Transformer: adaptive diffusion schedule for temporal evolution
  - Clinical features: age, genetics, biomarkers integrated
  - Cognitive decline: trajectory prediction with uncertainty quantification
  - Alzheimer's progression: multi-scale modeling from molecular to network
  - **Activation**: Alzheimer's, GNN, transformer diffusion, multi-modal brain networks, cognitive decline, progression modeling, adaptive diffusion

### QIF Neurons Outperform LIF in Gradient Descent Training
- [[qif-neurons-superior-lif-gradient-descent]] - Quadratic Integrate-and-Fire (QIF) neurons exhibit continuous differentiability, enabling stable gradient descent. LIF suffers discontinuity at threshold. QIF superior for SNN training (arXiv: 2606.05521)
  - QIF model: quadratic voltage dynamics with smooth threshold crossing
  - Continuous differentiability: stable gradients through firing events
  - LIF model: discontinuous reset causes gradient instability
  - Gradient descent: QIF converges faster and more stably than LIF
  - Implications for deep spiking neural network training
  - **Activation**: QIF, LIF, gradient descent, spiking neural networks, differentiability, threshold dynamics, SNN training

### Multi-Scale Real-Time Neural Decoding
- [[mrine-multiscale-realtime-neural-decoding]] - Multiscale Recurrent Inference Network for Encoding (MRINE) framework for real-time neural decoding. Multi-scale temporal + spatial inference with recurrent refinement. Streaming prediction with low latency (arXiv: 2606.05525)
  - Multi-scale temporal: short (ms) + medium (s) + long (min) dynamics
  - Recurrent inference: iterative refinement of decoding estimates
  - Real-time: streaming prediction without batch processing
  - Low latency: millisecond-level response time for BCI applications
  - Scalable: handles high-dimensional neural data (1000+ channels)
  - **Activation**: neural decoding, real-time, multi-scale, recurrent inference, streaming prediction, BCI, low latency, MRINE

### SNN Safety Thresholds for Autonomous Driving
- [[snn-safety-thresholds-automated-driving]] - Spiking Neural Network surrogate safety thresholds for autonomous driving. SNN-based safety envelope prediction. Energy-efficient safety monitoring with spiking dynamics (arXiv: 2606.05529)
  - SNN surrogate: energy-efficient safety threshold prediction
  - Safety envelope: spatial-temporal boundaries for safe operation
  - Surrogate thresholds: learned SNN replaces analytical safety checks
  - Autonomous driving: real-time safety monitoring with spiking latency
  - Energy-efficient: SNN reduces computational overhead vs ANNs
  - **Activation**: SNN safety, autonomous driving, safety thresholds, surrogate safety, energy-efficient, safety envelope, spiking dynamics

### QIF Superior to LIF: Continuous Differentiability Advantage
- [[qif-superior-lif-gradient-descent]] - Quadratic Integrate-and-Fire (QIF) neurons superior to LIF due to continuous differentiability. Smooth threshold crossing enables stable gradient-based training. QIF gradient descent converges faster (arXiv: 2606.05521, duplicate entry)
  - Continuous differentiability: smooth transition at firing threshold
  - Gradient stability: QIF avoids LIF reset discontinuity
  - Training convergence: faster convergence with QIF vs LIF
  - Mathematical analysis: proof of gradient continuity
  - **Activation**: QIF, LIF, gradient descent, continuous differentiability, spiking neurons, threshold dynamics, gradient stability

## 2026-06-02 - Neuroscience Research (Cron Job)

### Feature Life History Scaffold: Understanding Neural Feature Trajectories
- [[feature-life-history-scaffold]] - Feature life history methodology reveals how features emerge, mature, and fade during training. Scaffold model: early features → stable core → late task-specific features (arXiv: 2606.04505)
  - Feature trajectory: temporal evolution of feature representations
  - Scaffold model: layered feature emergence across training epochs
  - Early features: generalizable, low-level representations
  - Stable core: persistent features across training stages
  - Late features: task-specific, high-level representations
  - **Activation**: feature trajectories, life history, neural feature evolution, scaffold model, training dynamics, feature emergence

### Extended Predictive Coding with Exponential Family
- [[extended-predictive-coding-free-energy-exponential-family]] - Extended Predictive Coding (PC) framework using exponential family distributions. Free energy minimization with non-Gaussian priors. Handles skewed neural distributions better than Gaussian PC (arXiv: 2606.04509)
  - Exponential family: Poisson, exponential, gamma distributions
  - Free energy: generalized for non-Gaussian predictive coding
  - Skewed distributions: better modeling of neural firing rates
  - Predictive coding: hierarchical inference with flexible priors
  - Plasticity: local learning rules from exponential family PC
  - **Activation**: predictive coding, exponential family, free energy, non-Gaussian, skewed distributions, hierarchical inference, local plasticity

### Functional Ensembles in Deep Spiking Networks
- [[functional-ensembles-deep-spiking-networks]] - Functional ensembles as computational units in deep spiking networks. Ensemble-level dynamics replace single-neuron computation. Sparse ensemble activation improves efficiency (arXiv: 2606.04513)
  - Functional ensemble: group of neurons with shared computational role
  - Ensemble dynamics: population-level computation vs single-neuron
  - Sparse activation: few ensembles active per task
  - Deep SNNs: hierarchical ensemble organization
  - Efficiency: ensemble-level reduces redundancy
  - **Activation**: functional ensembles, deep spiking networks, ensemble dynamics, sparse activation, hierarchical organization, population computation

### Neuroscience June 2026 Synthesis
- [[neuroscience-june-2026-synthesis]] - 2026年6月神经科学核心发现综述 — 神经元群体scaling law、QIF训练稳定性、STP目标条件动力学、CorSW EEG解码、CHASMBrain Mamba重建、量子认知建模等前沿进展的系统整合 (Multiple arXiv papers)
  - Neuron populations: scale-dependent selectivity divergence (SOM+ vs PV+)
  - QIF training: continuous differentiability superiority over LIF
  - STP goal planning: short-term plasticity stabilizes PFC reservoirs
  - Feature life history: scaffold model of feature trajectory evolution
  - Extended PC: exponential family for non-Gaussian predictive coding
  - Quantum cognition: GKSL master equation for cognitive modeling
  - CHASMBrain: dual-stream Mamba for visual cortex reconstruction
  - CorSW: sliced Wasserstein for scale-invariant EEG decoding
  - **Activation**: neuroscience synthesis, June 2026, neuron populations, QIF, STP, feature trajectories, predictive coding, quantum cognition, Mamba brain, CorSW EEG

## 2026-06-01 - Neuroscience Research (Cron Job)

### Brain Learning Utilizes Non-Ideal Factors
- [[brain-learning-non-ideal-factors]] - Brain learning principles utilizing non-ideal factors (noise, variability, delays). Biological systems leverage imperfections for robust learning. Noise-enhanced plasticity, variability-driven adaptation (arXiv: 2606.03705)
  - Non-ideal factors: neuronal noise, synaptic variability, transmission delays
  - Noise-enhanced plasticity: stochastic resonance in learning
  - Variability-driven adaptation: diverse responses improve robustness
  - Delays as computational resource: temporal coding benefits
  - Brain optimization: leveraging imperfections vs eliminating them
  - **Activation**: brain learning, non-ideal factors, neuronal noise, variability, delays, stochastic resonance, robust learning

### MindVoice: Neural Speech Reconstruction
- [[mindvoice-neural-speech-reconstruction]] - MindVoice framework for reconstructing intelligible speech from neural activity. End-to-end decoder from intracranial EEG to audio waveforms. Natural speech synthesis with neural features (arXiv: 2606.03709)
  - Intracranial EEG: high-resolution neural recordings during speech production
  - End-to-end decoder: neural → acoustic features → waveform synthesis
  - Intelligibility: reconstructed speech understandable by humans
  - Natural synthesis: prosody and phoneme accuracy
  - Speech BCI: neural-to-speech communication interface
  - **Activation**: speech reconstruction, neural decoding, intracranial EEG, speech synthesis, BCI, MindVoice, neural-to-speech

### Misalignment Between Backpropagation and Brain Hierarchy
- [[misalignment-backpropagation-brain-hierarchy]] - Misalignment between backpropagation gradient flow and brain visual hierarchy. Gradient descent mismatches biological cortical organization. Supervised training diverges from biological processing (arXiv: 2606.03713)
  - Gradient flow: backpropagation order reversed from sensory hierarchy
  - Brain hierarchy: V1 → V2 → V4 → IT, gradients flow IT → V4 → V2 → V1
  - Misalignment: computational optimization vs biological organization
  - Self-supervised: better alignment than supervised training
  - Implications: biological constraints on AI architectures
  - **Activation**: backpropagation, brain hierarchy, gradient misalignment, visual cortex, biological organization, self-supervised, cortical hierarchy

### Deep Learning for Sequential Decision under Uncertainty
- [[deep-learning-sequential-decision-uncertainty]] - Deep learning methodologies for sequential decision-making under uncertainty. Recurrent policies, attention mechanisms, Bayesian neural networks for uncertainty estimation (arXiv: 2606.03717)
  - Sequential decisions: time-dependent choices with incomplete information
  - Recurrent policies: LSTM/GRU for temporal state tracking
  - Attention mechanisms: selective focus on relevant history
  - Bayesian NNs: uncertainty quantification in policy networks
  - Applications: robotics, finance, healthcare decisions
  - **Activation**: sequential decisions, uncertainty, deep learning, recurrent policies, attention, Bayesian neural networks, decision-making

### LLM Reorganizes Representational Geometry in ICL
- [[llm-reorganize-representational-geometry-icl]] - Large language models reorganize representational geometry during in-context learning (ICL). Geometry shifts from pre-training structure to task-specific organization. Dynamic representational adaptation (arXiv: 2606.03721)
  - In-context learning: adapting to new tasks without weight updates
  - Representational geometry: spatial structure of embedding space
  - Geometry reorganization: pre-training → task-specific geometry
  - Dynamic adaptation: geometry evolves with context examples
  - Interpretation: ICL as geometry transformation, not weight update
  - **Activation**: LLM, in-context learning, representational geometry, geometry reorganization, dynamic adaptation, embedding space

### Cross-Scale Spatial Generative Neurodegeneration Modeling
- [[cross-scale-spatial-generative-neurodegeneration]] - Cross-scale spatially-aware generative modeling for neurodegenerative disease progression. Multi-scale from molecular to whole-brain. Spatial gradients of pathology spread (arXiv: 2606.03725)
  - Multi-scale: molecular (tau) → cellular (neurons) → network (connectome) → whole-brain
  - Spatial gradients: pathology spreads along anatomical pathways
  - Generative modeling: diffusion-based progression simulation
  - Neurodegeneration: Alzheimer's, Parkinson's progression patterns
  - Predictive: forecasting disease trajectory from early biomarkers
  - **Activation**: neurodegeneration, multi-scale modeling, spatial gradients, generative diffusion, Alzheimer's, Parkinson's, progression prediction

### Multimodal Brain Network Foundation Model
- [[multimodal-brain-network-foundation-model]] - Multimodal brain network foundation model integrating structural + functional + diffusion MRI. Joint learning across modalities with graph neural networks. Cross-modal transfer for brain analysis (arXiv: 2606.03729)
  - Multimodal: structural MRI (anatomy), functional MRI (activity), diffusion MRI (connectivity)
  - Joint learning: shared representation across modalities
  - Graph neural networks: brain network modeling from connectivity
  - Cross-modal transfer: knowledge transfer between MRI modalities
  - Foundation model: pre-trained on large multi-site datasets
  - **Activation**: brain foundation model, multimodal MRI, structural functional diffusion, graph neural networks, cross-modal transfer, brain network

### Cortico-Subcortical Memory Limited Learning
- [[cortex-subcortex-memory-limited-learning]] - Cortico-subcortical dissociation in memory-limited learning. Cortex handles pattern separation, subcortex handles pattern completion. Complementary learning systems with different capacities (arXiv: 2606.03733)
  - Cortex: pattern separation, sparse representations, high capacity
  - Subcortex (hippocampus, striatum): pattern completion, dense representations
  - Memory limited: bounded capacity in learning systems
  - Complementary systems: cortex + subcortex different roles
  - Learning trade-off: separation vs completion balance
  - **Activation**: cortico-subcortical, memory limited learning, pattern separation, pattern completion, hippocampus, striatum, complementary systems

### Dual-Spectral Flow Matching for fMRI Generation
- [[dual-spectral-flow-matching-fmri-generation]] - Dual-Spectral Flow Matching (DSFM) for fMRI time series generation. Spatial + temporal spectral flow matching. High-fidelity synthetic fMRI for data augmentation (arXiv: 2606.03737)
  - Spatial spectral: frequency-domain spatial patterns
  - Temporal spectral: frequency-domain temporal dynamics
  - Flow matching: continuous trajectory interpolation in spectral space
  - fMRI generation: synthetic brain activity with realistic dynamics
  - Data augmentation: increasing training data for brain models
  - **Activation**: fMRI generation, flow matching, dual-spectral, spatial temporal, synthetic brain activity, data augmentation

### Brain-IT-VQA: Visual Question Answering from fMRI
- [[brain-it-vqa-fmri-visual-question-answering]] - Brain-IT-VQA framework for visual question answering from fMRI. Decoding visual content + answering questions directly from brain activity. End-to-end neural to language pipeline (arXiv: 2606.03741)
  - Visual decoding: reconstructing image content from fMRI
  - Question answering: generating answers from brain activity
  - End-to-end: fMRI → visual features → language → answer
  - Brain-to-language: direct neural to text interface
  - VQA task: answering questions about viewed images
  - **Activation**: brain VQA, fMRI decoding, visual question answering, brain-to-language, neural interface, visual content reconstruction

## 2026-05-31 - Neuroscience Research (Cron Job)

### Uncommon Self-Knowledge in Consciousness
- [[uncommon-self-knowledge-consciousness]] - Uncommon Self-Knowledge (USK) consciousness theory. Self-knowledge as rare information: higher-order thoughts about self. Partial information decomposition for consciousness quantification (arXiv: 2606.02905)
  - Self-knowledge: rare, higher-order representation of system state
  - Uncommon information: partial information decomposition metrics
  - USK criterion: consciousness requires uncommon self-knowledge
  - Mathematical framework: quantify consciousness via information theory
  - Higher-order thoughts: meta-representations of self
  - **Activation**: consciousness, self-knowledge, uncommon information, partial information decomposition, higher-order thoughts, USK theory

### Embodied VR Feedback Reshapes Neural Representations
- [[embodied-vr-feedback-reshapes-neural-representations]] - Embodied virtual reality feedback reshapes neural representations in motor imagery BCI. First-person avatar feedback improves motor cortex activation patterns. Enhanced embodiment improves decoding (arXiv: 2606.02909)
  - Embodied VR: first-person avatar feedback during motor imagery
  - Neural reshaping: motor cortex activation patterns adapt to avatar
  - Motor imagery: imagined movements decoded to BCI commands
  - Enhanced embodiment: improved sensorimotor representation
  - BCI decoding: higher accuracy with embodied VR feedback
  - **Activation**: embodied VR, motor imagery BCI, neural reshaping, avatar feedback, motor cortex, embodiment, first-person

### Supervised Training Degrades Visual Cortex Alignment
- [[supervised-training-degrades-visual-cortex-alignment]] - (Duplicate entry, see 2026-06-04)

### Cineneuron: Hierarchical fMRI Video Reconstruction
- [[cineneuron-fmri-video-reconstruction]] - CineNeuron: hierarchical framework for semantically enhanced video reconstruction from fMRI. Multi-stage decoding: semantic concepts → spatial features → temporal dynamics (arXiv: 2606.02913)
  - Hierarchical decoding: semantic → spatial → temporal stages
  - Semantic concepts: high-level meaning extraction from fMRI
  - Spatial features: object position and scene layout reconstruction
  - Temporal dynamics: motion and action sequence generation
  - Video reconstruction: dynamic visual content from brain activity
  - **Activation**: fMRI video reconstruction, Cineneuron, hierarchical decoding, semantic spatial temporal, dynamic brain decoding, video generation

### Subcortical Shape-Cognition Aging Associations
- [[subcortical-shape-cognition-aging]] - Subcortical brain structure shape variations associated with cognitive aging. Shape metrics predict cognitive decline beyond volume measures. Morphometry reveals aging patterns (arXiv: 2606.02917)
  - Subcortical structures: hippocampus, thalamus, amygdala shape
  - Shape metrics: curvature, surface complexity, deformation
  - Cognitive aging: memory, executive function decline prediction
  - Beyond volume: shape better predictor than size measures
  - Morphometry: detailed structural analysis for aging biomarkers
  - **Activation**: subcortical shape, cognitive aging, morphometry, hippocampus, thalamus, shape metrics, aging biomarkers

### Circulate-Firing SNN Direct Training
- [[circulate-firing-snn-direct-training]] - Direct training algorithm for SNNs with circulate-firing mechanism. Gradient-based learning without surrogate gradients. Stable training with continuous firing dynamics (arXiv: 2606.02921)
  - Circulate-firing: continuous spiking dynamics without reset
  - Direct training: gradient descent without surrogate approximation
  - Stable learning: smooth gradient flow through firing events
  - No surrogate: eliminates approximation errors in SNN training
  - Performance: competitive with surrogate gradient methods
  - **Activation**: SNN training, circulate-firing, direct gradient, surrogate gradients, spiking dynamics, continuous firing

### SN...[truncated]
