## 2026-05-24 - Systems Engineering Research (Cron Job)

### AdaPTwin: Adaptive Multi-Fidelity Predictive Digital Twin
- [[adaptwin-digital-twin]] - Adaptive multi-fidelity predictive digital twin for proactive RRM in vehicular networks (arXiv: 2605.21897)
  - Core: Cloud-edge hierarchical architecture with dynamic fidelity adjustment
  - Key: Transformer trajectory prediction + continual/transfer learning + NVIDIA Sionna ray tracing
  - Result: 90% sum-rate gain, 80% outage reduction
  - **Activation**: digital twin, adaptive fidelity, RRM, vehicular networks

### Contractual Skills: A GovernSpec Design Framework for Enterprise AI Agents
- [[contractual-skills-governspec]] - Governance layer design for AI agent skills as inspectable task contracts (arXiv: 2605.22634)
  - Core: Contractual skill structure with goal/input/permissions/output/verification fields
  - Key: Governance boundary between skills, GovernSpec YAML, MCP, guardrails, tracing
  - Result: Outperforms no-skill baselines, reduces high-risk tool attempts
  - **Activation**: AI agent governance, contractual skills, GovernSpec

## 2026-05-24 - Neuroscience Research (Cron Job - Sunday)

### Temporal Coding as a Substrate for Sensorimotor Object Inference: A Spiking Reinterpretation of Thousand Brains Architecture (arXiv:2605.22206)
- [[temporal-coding-thousand-brains-spiking]] - Replaces dense floating-point vectors with rank-order spike packets for sensorimotor inference in the Monty/Thousand Brains framework; uses STDP to encode traversal direction and adaptive lambda for geometric complexity (arXiv: 2605.22206)
  - Perfect discrimination on objects with identical features in different arrangements (dense accumulation at chance)
  - 30-50 percentage point noise robustness advantage maintained across all levels
  - Adaptive lambda converges to distinct values reflecting object geometric complexity
  - Three testable predictions: temporal order discrimination, STDP direction encoding, lambda-geometry correspondence
  - **Activation**: thousand brains theory, temporal coding, rank-order coding, sensorimotor inference, STDP direction encoding, Monty framework spiking

### Joint Sparse Coding and Temporal Dynamics Support Context Reconfiguration (arXiv:2605.10178)
- [[sparse-temporal-context-reconfiguration]] - Identifies sparsity in context-dependent representations and temporal dynamics as mechanisms for preserving prior knowledge during context transitions; SNNs show improved lifelong learning retention (arXiv: 2605.10178)
  - Sparsity reduces cross-context interference in mouse mPFC and computational networks
  - Temporal dynamics further separate context representations across time
  - SNNs naturally exhibit both properties, retaining information better without auxiliary heuristics
  - Energy-efficient architectural principle for stable adaptation
  - **Activation**: context reconfiguration, lifelong learning SNN, catastrophic forgetting spiking, sparse coding context, temporal dynamics neural, mPFC context switching

## 2026-05-24 - Information Science + Quantum Computing (Cron Job - Sunday)

### Operationalising Post Quantum TLS Automated Configuration Profiling and Hybrid PQC Deployment (arXiv:2605.17955)
- [[pqc-tls-deployment]] - Automated PQC TLS deployment methodology with configuration parsing and hybrid ML-KEM key exchange for enterprise infrastructure (arXiv: 2605.17955)
  - Configuration parsing across Nginx, Apache, API gateways for unified cryptographic inventory
  - Hybrid ML-KEM + X25519 deployment with zero application-layer changes
  - Migration strategy: discovery → pilot → production with performance monitoring
  - **Activation**: post-quantum cryptography deployment, PQC TLS migration, ML-KEM hybrid, cryptographic inventory, crypto-agility

### Optimization of Secret Key Rate for BB84 under Collective Rotation Noise (arXiv:2605.21140)
- [[qkd-noise-optimization]] - QKD noise engineering strategy finding optimal noise range where eavesdropper information is minimized while SKR degradation remains small (arXiv: 2605.21140)
  - Non-zero noise sweet spot: collective rotation noise can act as natural defense
  - QBER monitoring with ~11% threshold for BB84 asymptotic security
  - Intercept-resend and coherent attack scenario analysis under noise
  - **Activation**: quantum key distribution, BB84 protocol, QKD noise optimization, secret key rate, quantum bit error rate, collective rotation noise

### Q-SpiRL: Quantum Spiking Reinforcement Learning for Adaptive Robot Navigation (arXiv:2605.20801)
- [[q-spirl-quantum-spiking-rl]] - Combines spike-based temporal processing with variational quantum feature transformation for obstacle-aware robot navigation, achieving up to 99% success rate with deterministic inference on IBM quantum hardware (arXiv: 2605.20801)
  - Five agent families evaluated under unified pipeline: Q-learning, MLP, SNN, QMLP, QSNN
  - QSNN outperforms all baselines in success rate + trajectory efficiency + motion smoothness
  - Spike encoding captures dynamic obstacle patterns; quantum layer provides high-dimensional feature transformation
  - Verified deployment on real IBM quantum hardware under NISQ constraints
  - **Activation**: quantum reinforcement learning, quantum spiking, QSNN, spike-based RL, quantum robot navigation, quantum SNN policy, variational quantum RL

## 2026-05-25 - Neuroscience Research (Cron Job - Sunday)

### Subject-Specific Analysis of Self-Initiated Attention Shifts from EEG (arXiv:2605.18251)
- [[self-initiated-attention-shifts-eeg]] - Machine learning + SHAP analysis of EEG reveals subject-specific discriminative information in preparatory activity for distinguishing self-initiated vs externally-cued attention shifts; higher-frequency bands and frontal regions are most informative (arXiv: 2605.18251)
  - Controlled comparison of self-initiated vs externally instructed shifts under identical visual stimulation
  - SHAP-based feature attribution across frequency bands and regions of interest
  - Reliable within-subject classification: beta/gamma bands and frontal regions drive decisions
  - **Activation**: self-initiated attention, EEG attention decoding, SHAP EEG, frontal EEG, voluntary attention, subject-specific EEG

### BCI-sift: An Automated Feature Selection Toolbox for BCI (arXiv:2605.19646)
- [[bci-sift-feature-selection]] - Automated scikit-learn-compatible feature selection toolbox for BCI applications operating across electrode, temporal, and frequency dimensions; validated on HD ECoG speech decoding (arXiv: 2605.19646)
  - Multi-dimensional selection: electrodes, time points, frequency bands simultaneously
  - Validated on 8 participants HD ECoG speech decoding (12-word task)
  - High-frequency gamma band identified as most informative feature dimension
  - **Activation**: BCI feature selection, ECoG decoding, neural feature tuning, automated BCI ML pipeline, BCI-sift

### Brain Alignment of Reasoning and Action Representations from VLMs and LAMs (arXiv:2605.19352)
- [[vlm-lam-brain-alignment]] - fMRI study showing VLMs and LAMs outperform RL baselines in brain encoding during gameplay; prompt gains scale with cortical hierarchy; VLM is prompt-symmetric while LAM is prompt-asymmetric in representational organization (arXiv: 2605.19352)
  - Both VLMs and LAMs significantly outperform RL baselines in voxel-wise encoding
  - Prompt-driven gains largest in frontal-parietal and motor-planning regions
  - VLM: 12.5% unique action vs 13.6% unique reasoning; LAM: 27% unique action vs -5% unique reasoning
  - **Activation**: VLM brain alignment, LAM fMRI encoding, interactive gameplay fMRI, cortical hierarchy encoding, action model brain comparison

### Conserved Kinematic Representations Enable Zero-Shot Decoding in Handwriting BCIs (arXiv:2605.19048)
- [[conserved-kinematic-zero-shot-bci]] - Zero-shot handwriting BCI decoding using conserved kinematic primitives; achieves 64% hits@3 on unseen letters, enabling open-vocabulary iBCI for logographic languages (arXiv: 2605.19048)
  - Neural representations of kinematic strokes are conserved across different character contexts
  - 64% hits@3 retrieval on unseen letters → strong evidence for compositional motor control
  - Enables scaling BCIs to Chinese, Japanese, and other logographic languages
  - **Activation**: zero-shot BCI, handwriting decoding, kinematic representations, conserved neural dynamics, iBCI handwriting, logographic BCI, motor cortex primitives

## 2026-05-25 - Information Science + Quantum (Cron Job - Sunday)

### A Formal Basis for Quantum Cryptographic Exposure Measurement under HNDL Threat
- [[quantum-crypto-exposure-measurement]] - Structurally-grounded HNDL exposure assessment using temporal hazard, vulnerability-exposure multiplicative terms, and saturation dynamics (arXiv: 2605.22569)
  - Core: HNDL compromise probability = h(t) × V_crypto × O_exposure / (1 + λ × D/A)
  - Key: Additive scoring cannot capture vulnerability-exposure interaction; marginal sensitivity is endogenous
  - Result: Framework works under partial observability; prioritises migration based on position in vulnerability-exposure plane
  - **Activation**: HNDL, harvest now decrypt later, quantum cryptographic exposure, post-quantum risk assessment, quantum security measurement

### Precision and Privacy in Distributed Quantum Sensing: A Quantum Fisher Information Duality
- [[quantum-fisher-information-duality]] - QFI duality establishing precision-privacy tradeoff: F_Q(w·θ) + F_Q(v·θ) ≤ N for orthogonal directions in distributed quantum sensing (arXiv: 2605.20765)
  - Core: Heisenberg-limited precision for one direction forces zero QFI for all orthogonal directions
  - Key: GHZ states (N≥2) and equatorial states (N=2) achieve tight bound
  - Result: Privacy is automatic — physics enforces the guarantee, no additional cryptography needed
  - **Activation**: quantum Fisher information, QFI duality, distributed quantum sensing, quantum privacy, parameter privacy

## 2026-05-24 - Information Science + Quantum (Cron Job - Sunday)


### How many systems can be dephased before the quantum switch becomes causally definite? (arXiv:2605.22807)
- [[quantum-causal-nonseparability]] - Analyzes how much dephasing noise a quantum switch can tolerate before its indefinite causal order becomes causally separable; quantifies robustness of quantum advantages from indefinite causal structure (arXiv: 2605.22807)
  - Causal nonseparability provides computational advantages over fixed causal order circuits
  - Quantum switch becomes causally separable after dephasing threshold of constituent systems
  - Process matrix formalism and causal witness operators for nonseparability detection
  - Phase transition boundary between causally nonseparable and separable regimes
  - **Activation**: causal nonseparability, quantum switch, indefinite causal order, dephasing quantum processes, causally nonseparable, process matrix formalism

### Tokenisation via Convex Relaxations (arXiv:2605.22821)
- [[convex-tokenisation]] - Reformulates NLP tokeniser construction as a linear program solved with convex optimisation (ConvexTok), yielding globally optimal vocabulary instead of greedy BPE/Unigram approaches (arXiv: 2605.22821)
  - BPE and Unigram make locally optimal decisions without considering full vocabulary
  - ConvexTok formulates tokenisation as LP with vocabulary size constraints
  - Global optimization produces better encoding efficiency than greedy methods
  - Scalable to large corpora via convex relaxation of binary constraints
  - **Activation**: convex tokenisation, ConvexTok, tokeniser construction, linear program NLP, BPE alternative, convex optimization tokenisation

### Vector Policy Optimization: Training for Diversity Improves Test-Time Search (arXiv:2605.22817)
- [[vector-policy-optimization]] - Proposes Vector Policy Optimization (VPO) that trains LLMs to produce diverse, high-entropy response distributions, significantly improving test-time search performance over scalar-reward RLHF (arXiv: 2605.22817)
  - Standard RLHF produces low-entropy responses that hurt inference-scaling search
  - VPO optimizes multiple reward functions simultaneously with entropy regularization
  - Diverse response coverage improves AlphaEvolve-style test-time search
  - Tradeoff between response quality and diversity tunable via beta parameter
  - **Activation**: vector policy optimization, VPO training, test-time search, LLM diversity, inference scaling, response diversity, AlphaEvolve
### Quantum Purity Amplification for Arbitrary Eigenstates and Multiple Outputs (arXiv:2605.21570)
- [[quantum-purity-amplification]] - General solution for coherently transforming n copies of a mixed state into m high-fidelity copies of any chosen eigenstate (arXiv: 2605.21570)
  - Handles arbitrary target eigenstates, not just dominant one
  - Supports arbitrary local dimension d (qubits, qudits, continuous-variable)
  - Quantifiable fidelity trade-off bounds between input copies and output quality
  - **Activation**: quantum purity amplification, QPA, state purification, mixed to pure state, quantum state amplification, eigenstate purification

### A Formal Basis for Quantum Cryptographic Exposure Measurement under HNDL Threat (arXiv:2605.22569)
- [[quantum-crypto-exposure-measurement]] - Formal mathematical framework for quantifying information leakage in quantum cryptographic systems under HNDL threat model (arXiv: 2605.22569)
  - HNDL model captures hard non-delegatable leakage that cannot be prevented cryptographically
  - Provides quantitative exposure metrics: IE, SM, RS
  - Formal bounds on adversary knowledge using quantum information theory
  - **Activation**: quantum cryptographic exposure, HNDL threat model, quantum security measurement, information leakage quantum, quantum threat modeling

### A Sharp Interaction-Degree Threshold for Simulating QAOA (arXiv:2605.22758)
- [[qaoa-interaction-threshold]] - Identifies sharp computational phase transition where classical simulation of QAOA becomes intractable (arXiv: 2605.22758)
  - Below threshold k_c: efficient tensor network classical simulation
  - Above threshold: exponential complexity, quantum advantage emerges
  - Interaction degree analysis provides quantum-classical boundary metric
  - **Activation**: QAOA simulation threshold, interaction degree QAOA, quantum advantage boundary, QAOA complexity analysis, classical simulation QAOA, computational phase transition

## 2026-05-24 - Information Science + Quantum (Cron Job)

### Precision and Privacy in Distributed Quantum Sensing: A Quantum Fisher Information Duality (arXiv:2605.20765)
- [[quantum-fisher-information-privacy]] - QFI duality framework establishing precision-privacy tradeoffs in distributed quantum sensing; Heisenberg-limited precision for target parameter forces zero QFI for all other independent directions (arXiv: 2605.20765)
  - QFI duality theorem: F_Q(w) + F_Q(v) <= N for any N-qubit probe state with local phase encoding
  - Privacy guarantee: attaining F_Q = N for sensing target renders all alternative estimations impossible
  - GHZ states achieve optimal tradeoff for N >= 2; equatorial states for N = 2
  - **Activation**: quantum Fisher information, QFI duality, quantum sensing privacy, distributed quantum sensors, parameter privacy, Heisenberg limit, Fisher information duality

### Quantum Homomorphic Encryption: Towards Practical and Private Computation on Untrusted Quantum Hardware (arXiv:2604.19256)
- [[quantum-homomorphic-encryption-qhe]] - QOTPH framework enabling computation on encrypted quantum states via Quantum One-Time Pad with information-theoretic security (arXiv: 2604.19256)
  - Homomorphic gate decompositions for Clifford+T circuits with systematic key update rules
  - Non-interactive evaluation for Clifford gates; T gates require additional protocol
  - Validated on simulated environments and real IBM quantum processors under circuit-level noise
  - **Activation**: quantum homomorphic encryption, QHE, QOTP, encrypted quantum computation, privacy-preserving quantum, delegated quantum computing, blind quantum computation

### Quantum-Resistant Networks: A Review of Primitives, Protocols and Best Practices (arXiv:2605.04129)
- [[quantum-resistant-networks]] - First comprehensive systematization of post-quantum network architectures across cryptographic foundations, key distribution, and deployment (arXiv: 2605.04129)
  - Unified taxonomy: symmetric-only, PQ-PKI, hybrid, information-theoretic multi-path foundations
  - Key distribution architectures: centralized, hierarchical, replicated, threshold, MPC-backed, serverless
  - Analyzes trade-offs under harvest-now-decrypt-later and partial infrastructure compromise threats
  - **Activation**: post-quantum cryptography, PQC networks, quantum resistant, network security architecture, key distribution, cryptographic agility

### Q-PhotoNAS: Hybrid Quantum Neural Architecture Search Framework on Photonic Devices (arXiv:2605.22097)
- [[q-photonas-hybrid-arch-search]] - NAS framework for hybrid photonic quantum-classical models using genetic algorithm-based search with learnable quantum phase encoding (arXiv: 2605.22097)
  - 19 hyperparameters encoded in 6 gene groups (classical preprocessing, phase encoding, photonic circuit, measurement, post-processing, training)
  - Group-based crossover, per-gene mutation, elitism; 99.44% Digits, 98.78% MNIST accuracy
  - Photonic layer extracts non-redundant features orthogonal to classical pathway
  - **Activation**: quantum architecture search, photonic quantum computing, Q-PhotoNAS, quantum NAS, hybrid quantum neural architecture, quantum phase encoding, genetic algorithm quantum, photonic QPU, Quandela

### Quantum Genetic Optimization for Negative Selection Algorithms in Anomaly Detection (arXiv:2605.22527)
- [[quantum-genetic-negative-selection]] - QGNSA methodology integrating quantum genetic algorithms into negative selection for enhanced anomaly detection (arXiv: 2605.22527)
  - Quantum superposition + probabilistic amplitude adjustment for diverse search space exploration
  - Superior anomaly detection on Metaverse Financial Transactions Dataset
  - Robust under varying hyperparameter configurations
  - **Activation**: quantum genetic algorithm, negative selection, anomaly detection, QGNSA, quantum immune system, quantum superposition search

## 2026-05-24 - Neuroscience Research (Cron Job)

### Learning sequence timing and control of replay speed in networks of spiking neurons (arXiv:2605.22523)
- [[learning-sequence-timing-spiking-neurons]] - sTM model extension for encoding element-specific timing and flexible replay speed modulation via oscillatory background input (arXiv:2605.22523)
  - Timing encoding via sequential activation of delay-line assemblies within minicolumns (discretize time into dAP-compatible intervals)
  - Oscillatory background input (simulating theta/gamma rhythms) acts as clock signal for replay speed control (10-70 Hz range)
  - Replay speed independent of encoding speed — no relearning needed
  - Structural STDP + continuous weight decay; Plateau potentials (~100ms) set intrinsic timescale
  - **Activation**: spiking neural network, sequence timing, replay speed, sTM model, temporal memory, oscillatory control, dendritic action potential

### Efficient coding under constraint drives neural systems towards criticality and sloppiness (arXiv:2605.22598)
- [[efficient-coding-criticality-sloppiness]] - Theoretical framework linking Fisher information maximization under resource constraints to brain criticality, soft modes, and sloppiness (arXiv:2605.22598)
  - Maximizing Fisher info under trace(Tr(A)) constraint forces precision matrix toward rank-1 → diverging correlation length (statistical criticality) + critical slowing down (dynamical criticality)
  - Unifies statistical and dynamical criticality perspectives in a single minimal Gaussian population coding model
  - Quench events in sloppy directions produce power-law avalanche distributions from spectral geometry alone
  - Hebb-like learning rule δW ∝ ggᵀW maps directly onto predictive coding architecture
  - **Activation**: brain criticality, efficient coding, Fisher information, neural avalanches, sloppiness, soft modes

### Cross-Species RSA Reveals Conserved Early Visual Alignment but Divergent Higher-Area Rankings (arXiv:2605.22401)
- [[cross-species-rsa-brain-alignment]] - Systematic RSA comparison of 5 learning rules (BP, FA, PC, STDP, untrained) across human fMRI and macaque electrophysiology (arXiv:2605.22401)
  - STDP and PC lead at V1/V2 (ρ~0.30), conserved across species; IT rankings show no cross-species correlation
  - Macaque electrophysiology yields 2-4x higher alignment than human fMRI (ρ 0.15-0.30 vs 0.01-0.08)
  - ResNet-50 (ImageNet) achieves ρ=0.25 at macaque IT, far above all custom CNN conditions (ρ=0.07-0.14)
  - **Activation**: RSA, cross-species, brain alignment, representational similarity, learning rules, visual cortex

## 2026-05-23 - Economics/Quantum Finance (Cron Job)

### Constrained Counterdiabatic QAOA for Portfolio Optimization (arXiv:2605.06858)
- [[constrained-counterdiabatic-qaoa-portfolio]] - CCD-QAOA incorporating approximate adiabatic gauge potentials from nested commutators into QAOA ansatz for constrained portfolio optimization with XY mixer (arXiv:2605.06858)
  - Counterdiabatic driving terms accelerate convergence by adding shortcuts to adiabaticity
  - XY mixer preserves Hamming weight, naturally enforcing budget constraints without penalties
  - **Activation**: CCD-QAOA, counterdiabatic QAOA, constrained portfolio optimization, XY mixer, adiabatic gauge potential

### Quantum Reservoir Computing for Volatility Forecasting (arXiv:2505.13933)
- [[quantum-reservoir-computing-finance]] - Quantum reservoir computing using transverse-field Ising Hamiltonian with input/memory qubits for financial time series forecasting (arXiv:2505.13933)
  - Consistently outperforms classical econometric models and ML benchmarks on volatility prediction
  - Wrapper-based feature selection + Shapley values for interpretability on NISQ hardware
  - **Activation**: quantum reservoir computing, QRC finance, quantum volatility forecasting, Ising Hamiltonian reservoir

## 2026-05-23 - Neuroscience Research (Cron Job)

### Winner-Take-All bottlenecks enforce disentangled symbolic representations in multi-task learning (arXiv:2605.22472)
- [[winner-take-all-bottleneck-disentangled]] - WTA bottlenecks provably enforce extraction of categorical latent factors in multi-task learning, producing symbolic single-neuron encodings (arXiv:2605.22472)
  - Theoretical proof that WTA (cortical circuit motif) produces disentangled symbolic representations in deep networks
  - Single neurons encode single abstract features (object, color, position)
  - Enables compositional generalization; bridges sub-symbolic to symbolic AI
  - **Activation**: WTA, winner-take-all, disentangled representations, symbolic AI, latent factors, cortical circuits, multi-task learning, neural bottleneck

### Von Economo neurons enable reliable social skill acquisition in recurrent spiking neural networks
- [[vencircuit-von-economo-snn-social-learning]] - VENCircuit computational account showing Von Economo neurons (2% of total) act as acquisition scaffolds in SNNs, providing a 21-fold increase in training convergence odds (arXiv: 2605.17399)
  - VENs provide a direct gradient pathway immune to Jacobian instabilities in recurrent circuits
  - VEN-intact: 98% convergence vs VEN-ablated: 70% (Fisher's OR=21.0, p=8.7e-5)
  - Phase ablation shows VEN removal most disruptive during mid-training (epochs 5-25)
  - Inference ablation: heterogeneous effects — from no change to catastrophic collapse (0.989→0.620)
  - Clinical predictions: developmental VEN reduction → stochastic learning failure (ASC); adult VEN loss → heterogeneous performance effects (bvFTD)
  - **Activation**: Von Economo neurons, VENCircuit, social learning SNN, gradient flow, training stability, frontotemporal dementia, autism spectrum

### Supervised Deep Multimodal Matrix Factorization for Interpretable Brain Network Analysis
- [[sd3mf-multimodal-brain-network]] - SD3MF extends SNMTF from unsupervised clustering to supervised prediction over populations of multimodal graphs with deep hierarchical factorizations and adaptive multimodal fusion (arXiv: 2605.13312)
  - Encoder-decoder formulation jointly optimizes graph reconstruction and supervised prediction
  - Community-level interaction matrices yield interpretable + discriminative features
  - Outperforms CNNs and GNNs on multimodal connectome datasets
  - Adaptive weights enable data-driven multimodal fusion
  - **Activation**: SD3MF, multimodal brain network, matrix factorization, interpretable connectome analysis

## 2026-05-23 - Economics, Investment + Quantum Mechanics (Cron Job)

### Quantum Computing for Financial Transformation: A Review of Optimisation, Pricing, Risk, Machine Learning, and Post-Quantum Security
- [[quantum-finance-stack]] - Financial computation stack framework evaluating quantum advantage across five domains: portfolio optimisation, derivative pricing, tail-risk estimation, quantum ML, and post-quantum security (arXiv: 2604.08180)
  - Applies common evaluative logic: identify bottleneck, specify quantum primitive, compare classical benchmark, assess realistic constraints
  - 134-page comprehensive review; strongest near-term case is carefully designed hybrid workflows
  - Classical MIP solves 1000-asset portfolio instances in seconds; problem-tailored heuristics outperform quantum
  - Post-quantum cryptography already strategically necessary for financial infrastructure
  - **Activation**: quantum finance stack, financial quantum computing, quantum portfolio benchmark, quantum derivative pricing, quantum risk estimation, post-quantum cryptography finance, hybrid quantum finance workflow

### Hot-Starting Quantum Portfolio Optimization
- [[hotstart-quantum-portfolio]] - Compact Hilbert space QUBO formulation restricting search to vicinity of continuous optimum, reducing qubits and outperforming SOTA on D-Wave Advantage quantum annealer (arXiv: 2510.11153)
  - Solves continuous relaxation first, maps to nearest discrete solutions, constructs reduced QUBO
  - Reduces qubit requirements from O(N log M) to O(N log delta) where delta << M
  - Outperforms existing warm-start and full QUBO approaches on both classical and quantum solvers
  - **Activation**: hot-start quantum portfolio, warm-start QUBO, compact Hilbert space optimization, quantum portfolio reduction, D-Wave portfolio optimization

### Dynamical Hamiltonian Encoding
- [[dynamical-hamiltonian-encoding]] - Data encoding methodology addressing the Inverse Born Rule Fallacy — uses non-commutative Hamiltonian evolution instead of static phase-locked amplitude encoding for genuine quantum advantage in ML/finance (arXiv: 2602.21350)
  - Standard amplitude encoding (psi = sqrt(P)) restricts to positive real orthant, making states "phase-deaf"
  - DHE encodes data as coefficients of non-commuting Hamiltonian generators, preserving full Hilbert space access
  - Based on QIFT (Quantum Imaginary Time Evolution) framework
  - **Activation**: dynamical Hamiltonian encoding, inverse Born rule fallacy, quantum data encoding, amplitude encoding alternative, QIFE quantum ML, non-commutative quantum feature map

### Quantum Portfolio Optimization with Expert Analysis Evaluation
- [[quantum-portfolio-expert-eval]] - (existing skill reference) VQE/QAOA benchmark for portfolio optimization introducing Expert Analysis Evaluation framework — bridges gap between algorithmic performance and financial applicability (arXiv: 2507.20532)
  - Financial professionals assess economic soundness of quantum-optimized portfolios
  - Algorithmic convergence does not guarantee financial viability (diversification, risk exposure violations)
  - **Activation**: quantum portfolio expert evaluation, VQE portfolio benchmark, QAOA financial viability

### Quantum Portfolio Optimization: An Extensive Benchmark
- [[quantum-portfolio-benchmark]] - (existing skill reference) Comprehensive benchmark comparing quantum annealing + QAOA against classical MIP, simulated annealing, tabu search on 250 real-world instances up to 1000 assets (arXiv: 2509.17876)
  - Classical MIP solves all instances to proven optimality in seconds
  - Problem-tailored heuristic consistently outperforms quantum approaches for fixed runtime
  - Limited room for quantum advantage in standard portfolio optimization
  - **Activation**: quantum portfolio benchmark, quantum advantage finance, portfolio optimization comparison

## 2026-05-23 - Neuroscience Research: JET EEG Generation + ELSA SNN Accelerator (Cron Job)

### JET: Just EEG Transformer — Continuous Flow Matching for EEG Generation
- [[jet-eeg-flow-matching]] - Generative EEG framework using conditional flow matching that models neural signals as continuous trajectories, preserving spectral structure and temporal stationarity. ICML 2026. Reduces TS-FID by >40% (arXiv: 2605.21280)
  - Continuous flow matching captures temporal continuity better than discrete diffusion-based EEG generation
  - Principled constraints preserve spectral structure, temporal stationarity, and signal-level statistics
  - Raw sequence modeling without domain-specific representations
  - **Activation**: JET EEG transformer, conditional flow matching EEG, continuous EEG generation, EEG flow matching, spectral structure EEG generation, raw EEG sequence modeling

### ELSA: An ELastic SNN Inference Architecture for Efficient Neuromorphic Computing
- [[elsa-snn-elastic-inference]] - Near-SRAM dataflow architecture realizing true elastic inference via spine/token-wise pipeline, bundled AER protocol, and mini-batch spiking Gustavson-product for SNN sparsity. ISCA 2026. 3.4× speedup, 13.6-22.1× energy efficiency vs SOTA (arXiv: 2605.20802)
  - Spine/token-wise pipeline forwards each spike immediately, enabling true elastic inference
  - Bundled AER protocol reduces NoC communication traffic
  - Mini-batch spiking Gustavson-product exploits inherent SNN sparsity
  - SNNs can outperform quantized ANNs (4-bit ResNet-50) while maintaining accuracy
  - **Activation**: ELSA SNN accelerator, elastic SNN inference, spine-wise pipeline neuromorphic, bundled AER protocol, spiking Gustavson product, near-SRAM SNN architecture

## 2026-05-23 - Neuroscience Research: MIRAGE Mental Imagery + Platonic Representations (Cron Job)

### MIRAGE: Robust Multi-Modal fMRI-to-Mental-Image Decoding
- [[mirage-fmri-mental-imagery-decoding]] - Multi-modal fMRI decoder for cross-decoding visual perception to mental imagery. Linear backbone + multi-modal features (text, high-level, low-level image) → diffusion model, achieving SOTA on NSD-Imagery benchmark (arXiv: 2605.17198)
  - SOTA on seen images ≠ SOTA on mental images: architecture must be explicitly designed for cross-decoding
  - Low-dimensional image features + text guidance + multi-level features gives best mental image quality
  - Linear backbone outperforms complex nonlinear encoders for mental image decoding
  - Validated by both feature metrics and human raters
  - **Activation**: MIRAGE, fMRI mental imagery, brain-to-image decoding, mental image reconstruction, NSD-Imagery, vision decoder generalization, fMRI diffusion model, neuroimaging decoding

### Learning Sequence Timing and Replay Speed in Spiking Neural Networks
- [[learning-sequence-timing-snn]] - Biologically plausible SNN sequence learning extending spiking Temporal Memory (sTM) with element-specific timing encoding via sequential population activation and oscillatory clock-based replay speed modulation (arXiv: 2605.22523)
  - sTM model extended to encode element-specific durations via synfire chain propagation
  - Oscillatory background input (θ/γ rhythms) provides flexible clock signal for replay speed control
  - Elapsed time encoded by unique sparse spatiotemporal neural activity patterns
  - Links replay speed to EEG/LFP oscillatory patterns (θ during wake, γ during sleep)
  - **Activation**: spiking temporal memory, sTM model, sequence timing SNN, replay speed control, oscillatory clock neural, synfire chain timing, SNN sequence learning, theta gamma replay

### Mamba Spike Forecaster for Behavioral Decoding in BCIs
- [[mamba-spike-forecaster-bci]] - Single Mamba state-space model trained on next-step spike counts at Neuropixels scale simultaneously forecasts neural population activity and decodes behavioral state via lightweight linear readout. Achieves 75.7% choice decoding on Steinmetz benchmark (arXiv: 2605.12999)
  - Mamba SSM forecaster predicts next-step spike counts → denoised rates improve decoding by 4-6 pp over raw spikes
  - Lightweight per-session linear readout calibrates in just 100-150 trials
  - Validated on 39 sessions, ~27,000 neurons, 1,994 held-out trials
  - Pipeline fits within 50 ms bin budget on workstation GPUs for closed-loop BCI
  - **Activation**: Mamba neural decoding, spike forecasting BCI, implicit behavioral decoding, Neuropixels Mamba, state space model neuroscience, Steinmetz benchmark, closed-loop BCI Mamba

### Platonic Representations in the Human Brain: Unsupervised Recovery of Universal Geometry
- [[platonic-representations-brain-universal-geometry]] - Self-supervised recovery of universal neural geometry across subjects using fMRI. Evidence that human visual cortex representations are approximately isometric and translatable via unsupervised orthogonal rotations (arXiv: 2605.20496)
  - Self-supervised encoder learns subject-specific embeddings from fMRI alone via repeated stimulus presentations
  - Unsupervised orthogonal rotation alignment translates independently learned brain spaces across subjects
  - Shared latent space via synchronized pairwise rotations improves cross-subject retrieval
  - Bridges ANN representation convergence and biological neural geometry
  - **Activation**: platonic representation, universal geometry, brain representation, cross-subject alignment, fMRI visual cortex, isometric embedding, Natural Scenes Dataset, self-supervised brain encoding

## 2026-05-23 - Economics, Investment + Quantum Finance (Cron Job)

### Constraint Locality XY-Mixer Design under Trotterized Adiabatic Evolution
- [[constraint-locality-xy-mixer-design]] - XY-mixer effectiveness under Trotterization depends on constraint locality: global constraints suffer Trotter errors, local blocks excel (arXiv: 2605.02465)
  - 核心要点: XY-mixer dominant Trotter error depends on individual constraint structure, not total problem size
  - 核心要点: Single global equality constraint → use Pauli-X mixer; multiple disjoint local blocks → use XY-mixer
  - 核心要点: Dedicated 2-way-1-hot mixer Hamiltonian for TSP-like constraints
  - **Activation**: XY-mixer design, Trotterized adiabatic evolution, constraint locality, constraint-preserving mixer, combinatorial optimization quantum, quantum portfolio optimization mixer

### Quantum Tilted Loss in Variational Optimization
- [[quantum-tilted-loss-optimization]] - Operator-level exponential tilting that reshapes VQA optimization landscapes to mitigate barren plateaus by amplifying gradient signals (arXiv: 2605.02850)
  - 核心要点: QTL objective L(θ) = log Tr[exp(-βH)ρ(θ)] amplifies gradients where standard VQAs flatten
  - 核心要点: Single tunable parameter β controls landscape sharpness; annealing schedule provides exploration→exploitation
  - 核心要点: Naturally captures tail risk in financial applications (CVaR-like behavior)
  - **Activation**: quantum tilted loss, QTL optimization, barren plateau mitigation, VQA training improvement, exponential tilting quantum, variational quantum algorithm landscape

### Digital Spreading Framework for Quantum Expectation Computation
- [[digital-spreading-quantum-finance]] - Resolves rotation gate vs arithmetic circuit tradeoff using pruned Cuccaro ripple-carry — eliminates both sine-to-square bias and O(n²) complexity (arXiv: 2604.05452)
  - 核心要点: Analog rotation gates suffer sine-to-square bias; digital WeightedAdder circuits are O(n²) — both exceed NISQ limits
  - 核心要点: Pruned Cuccaro ripple-carry achieves O(n) gate count with no rotation gates
  - 核心要点: Pure digital expectation computation compatible with NISQ coherence times
  - **Activation**: digital spreading quantum, Cuccaro ripple-carry quantum, quantum finance NISQ, rotation-free quantum computation, quantum expectation computation, financial engineering quantum

### Contextual Quantum Neural Networks for Stock Price Prediction
- [[contextual-qnn-stock-prediction]] - Multi-asset stock prediction via quantum multi-task learning with share-and-specify ansatz (arXiv: 2503.01884)
  - 核心要点: Share-and-specify ansatz enables simultaneous multi-asset training on single quantum circuit
  - 核心要点: Quantum batch gradient update (QBGU) accelerates convergence over standard quantum SGD
  - 核心要点: Logarithmic qubit overhead O(log N) for N assets via quantum superposition
  - **Activation**: contextual quantum neural network, stock price prediction, quantum multi-task learning, QMTL, share-and-specify ansatz, quantum batch gradient update, QBGU, quantum finance

### FiD-QAE: Fidelity-Driven Quantum Autoencoder for Fraud Detection
- [[fid-quantum-autoencoder-fraud]] - Quantum autoencoder for fraud detection using SWAP test fidelity estimation (arXiv: 2512.12689)
  - 核心要点: Fidelity estimation via SWAP test as anomaly detection criterion
  - 核心要点: Maintains consistent performance under multiple quantum noise models
  - 核心要点: Validated on IBM Quantum hardware with results consistent with simulation
  - **Activation**: quantum autoencoder, fraud detection, fidelity estimation, SWAP test, anomaly detection, quantum machine learning, credit card fraud

### Comparative QML Architecture Analysis for Fraud Detection
- [[qml-fraud-detection-comparison]] - Systematic comparison of VQC, SQNN, EQNN for financial fraud detection (arXiv: 2412.19441)
  - 核心要点: VQC consistently achieves F1-score of 0.88, outperforming SQNN and EQNN
  - 核心要点: Feature map and ansatz configuration choices dominate architecture selection
  - 核心要点: ANOVA validation confirms statistical significance of performance differences
  - **Activation**: quantum machine learning comparison, VQC, SQNN, EQNN, fraud detection architecture, quantum feature map, ansatz configuration, ANOVA validation

## 2026-05-23 - Neuroscience Cron (Spiking Language Models + Spike Operators)

### SymbolicLight V1: Spike-Gated Dual-Path Language Modeling with High Activation Sparsity
- [[symboliclight-spike-gated-language]] - First natively trained spiking language model combining binary LIF spike dynamics with continuous residual stream. 194M params, >89% activation sparsity, PPL 8.88 on bilingual corpus (arXiv: 2605.21333)
  - Dual-Path SparseTCAM replaces dense self-attention with exponential-decay path + spike-gated local attention
  - Ablation proves temporal integration (not sparsity alone) drives performance
  - 0.8B scale-up demonstrates sparsity preservation at larger scale
  - **Activation**: symboliclight, spike-gated language model, spiking language model, LIF language model, activation sparsity

### Plug-and-Play Spiking Operators: Breaking the Nonlinearity Bottleneck
- [[plug-and-play-spiking-operators]] - Training-free ANN-to-SNN conversion framework implementing spike-friendly Softmax, SiLU, and normalization via LIF population coding + bit-shift scaling (arXiv: 2605.20289)
  - Decomposes Transformer nonlinearities into division, exponentiation, ℓ₂ norm primitives
  - <1% accuracy drop across all evaluated LLM tasks, no fine-tuning required
  - Modular operator blocks integrate into existing ANN-to-SNN pipelines
  - **Activation**: spiking operators, ANN-to-SNN conversion, spike-friendly softmax, LIF population coding, spiking transformer


## 2026-05-23 - Economics, Investment + Quantum Mechanics (Cron Job)

### Constrained Counterdiabatic QAOA for Portfolio Optimization
- [[constrained-counterdiabatic-qaoa-portfolio]] - Counterdiabatic QAOA with CD driving terms accelerates convergence on constrained financial optimization (arXiv: 2605.06858)
  - CD terms suppress diabatic transitions during adiabatic evolution
  - Enables faster convergence to optimal portfolio weights
  - Joint optimization of QAOA angles and CD coefficients
  - **Activation**: counterdiabatic QAOA, CD-QAOA portfolio, constrained QAOA, quantum approximate optimization finance

### Quantum Amplitude Estimation for Insurance Tail-Risk Pricing
- [[quantum-amplitude-estimation-insurance-pricing]] - QAE provides quadratic speedup over classical Monte Carlo for catastrophe insurance tail-risk pricing (arXiv: 2603.15664)
  - O(1/ε) vs O(1/ε²) convergence advantage for rare events
  - Empirical convergence analysis for practical insurance applications
  - Tail-risk metrics: VaR, CVaR, tail conditional expectation
  - **Activation**: quantum amplitude estimation insurance, QAE tail-risk pricing, quantum Monte Carlo finance, catastrophe insurance quantum


## 2026-05-23 - Economics, Investment + Quantum (Cron Job - QML Benchmark & Interpretability)

### Quantum vs. Classical Machine Learning: A Benchmark Study for Financial Prediction
- [[qml-benchmark-financial-prediction]] - Reproducible benchmarking framework comparing QML with architecture-matched classical models on directional prediction (+3.8 AUC AAPL), live trading (QLSTM beats in 2/4 regimes), and volatility forecasting (QSVR lowest QLIKE) (arXiv: 2601.03802)
  - Hybrid QNN surpasses parameter-matched ANN: +3.8 AUC, +3.4 accuracy on AAPL; +4.9 AUC, +3.6 on KCHOL
  - QLSTM achieves higher risk-adjusted returns in 2 of 4 S&P 500 market regimes
  - Angle-encoded QSVR attains lowest QLIKE; within ~0.02-0.04 of best classical on S&P500/AAPL
  - Key insight: QML advantage when data structure and circuit design are well-aligned
  - **Activation**: qml benchmark financial, quantum vs classical finance, quantum LSTM trading, quantum volatility forecasting, QML financial prediction, 量子机器学习金融基准

### IQNN-CS: Interpretable Quantum Neural Network for Credit Scoring
- [[interpretable-quantum-credit-scoring]] - Interpretable QNN framework for multiclass credit risk classification with Inter-Class Attribution Alignment (ICAA) metric for quantifying how model distinguishes between risk categories (arXiv: 2510.15044)
  - Combines variational QNN with post-hoc explanation techniques for structured financial data
  - ICAA metric: quantifies attribution divergence across predicted credit risk classes
  - Stable training dynamics, competitive predictive performance on real-world credit datasets
  - Addresses regulatory requirement for transparent QML in financial decision-making
  - **Activation**: interpretable quantum credit scoring, IQNN-CS, ICAA metric, quantum explainable finance, 量子可解释信用评分



## 2026-05-23 - Neuroscience Research: EEG Visual Decoding (Cron Job)

### Neuroscience-inspired Staged Representation Learning with Disentangled Coarse- and Fine-Grained Semantics for EEG Visual Decoding
- [[eeg-staged-representation-learning]] - Reformulates EEG visual decoding as stage-specific representation decomposition (low-level visual, high-level semantic, integrative fusion) with dual-level coarse/fine-grained semantic learning and semantic latent channels (arXiv: 2605.16923)
  - 三阶段框架：低层视觉表示学习、高层语义表示学习、整合信息融合
  - 多模态双级语义学习：分离粗粒度标签级语义和细粒度图像级视觉语义信息
  - 语义潜通道：从视觉诱发电位生成的计算表示通道，扩展通道级语义表示空间
  - THINGS-EEG基准测试：subj.-dependent zero-shot和subj.-independent zero-shot均取得领先性能
  - **Activation**: staged eeg representation, EEG visual decoding, coarse-to-fine semantics, semantic latent channels, THINGS-EEG benchmark

## 2026-05-23 - Economics, Investment + Quantum (Cron Job)

### Quantum Portfolio Optimization: QAOA Interaction-Degree Threshold & DRL Integration
- [[quantum-portfolio-qaoa-drl]] - Synthesizes QAOA quantum advantage thresholds, Dicke state initialization for portfolio optimization, adiabatic QPE for risk analysis, and DRL trading agent dynamics (arXiv: 2605.22758, 2605.22770, 2605.22215, 2605.21696, 2605.20348)
  - QAOA degree-3 threshold: classical sampling collapses PH, but optimization may be trivial
  - Dicke state initialization mitigates barren plateaus in portfolio QAOA
  - Adiabatic QPE achieves Heisenberg-limited eigenvalue estimation for covariance analysis
  - Deep hedging symbolic distillation reveals delta corrections and regime fragility
  - Multi-agent RL trading can develop supra-competitive outcomes through memory
  - **Activation**: quantum portfolio, QAOA finance, Dicke state initialization, quantum advantage threshold, deep hedging, RL trading agents, counterdiabatic QAOA

### Option Pricing on Noisy Intermediate-Scale Quantum Computers: A Quantum Neural Network Approach
- [[qnn-option-pricing-nisq]] - Quantum Neural Network methodology for derivative pricing on NISQ hardware, cross-platform benchmarking across IBM Fez, IonQ Forte, Rigetti Ankaa-3, IQM Garnet quantum processors (arXiv: 2604.19832)
  - 2-qubit QNN architecture approximates Black-Scholes-Merton pricing functions
  - Cross-platform evaluation reveals hardware-dependent performance characteristics
  - Demonstrates viable quantum approach for derivative pricing despite NISQ constraints
  - Extendable to stochastic volatility, local volatility, and interest rate models
  - **Activation**: quantum option pricing, QNN derivative pricing, NISQ finance, quantum Black-Scholes, cross-platform quantum benchmark


## 2026-05-23 - 经济学、投资 + 量子力学 (Cron Job)

### Parameterized 4-Qubit EWL Quantum Game Circuits with Dirac-Solow-Swan Hamiltonian Integration for Quadruple Helix Disruptive Innovation Recommender Systems
- [[quantum-game-recommender-systems]] - 量子博弈电路推荐系统方法论，将EWL电路测量概率映射为创新推荐评分，结合Dirac-Solow-Swan哈密顿量模拟资本积累动力学 (arXiv: 2605.18080)
  - EWL量子电路作为推荐引擎，4量子比特编码四重螺旋参与者
  - 量子测量概率映射到Dirac-Solow-Swan哈密顿量对角势
  - 仅22门电路深度11，适合NISQ设备
  - **Activation**: quantum game recommender, EWL circuit economics, Dirac-Solow-Swan, quadruple helix, innovation recommender

### The Cost of Quantum Resistance: A Hash-Based Commit-Reveal Alternative for Minimizing Blockchain Infrastructure Overhead
- [[post-quantum-blockchain-economics]] - 后量子密码区块链迁移经济分析框架，评估哈希承诺-揭示方案相比直接PQC签名替换的基础设施成本优势 (arXiv: 2605.06853)
  - 哈希commit-reveal方案相比直接PQC替代方案仅增加1.5-2倍交易开销
  - 语义重设计优于直接大签名替换，长期经济效益更好
  - 量化PQC迁移成本：存储、带宽、计算、双支持期
  - **Activation**: post-quantum blockchain, commit-reveal, PQC migration cost, blockchain economics

### Non-Gaussian Entanglement Hierarchy Based on the Schmidt Number
- [[non-gaussian-entanglement-hierarchy]] - 基于施密特数的非高斯纠缠层次分类框架，超越高斯态表征连续变量系统中的复杂纠缠结构 (arXiv: 2605.18605)
  - 施密特数K作为连续变量纠缠量化指标，K越大纠缠结构越复杂
  - 建立从乘积态到任意非高斯纠缠的n级层次分类
  - 应用：量子通信容量、量子计量超越高斯极限、CV量子计算资源态
  - **Activation**: non-Gaussian entanglement, Schmidt number, CV entanglement, entanglement hierarchy

## 2026-05-23 - Neuroscience Research (Cron Job)

### Efficient Coding Under Constraint Drives Neural Systems Towards Criticality and Sloppiness
- [[efficient-coding-criticality]] - Theoretical framework linking efficient coding (Fisher info maximization) to critical brain dynamics: soft modes, diverging correlation lengths, and sloppiness emerge naturally under resource constraints (arXiv: 2605.22598)
  - 最大化Fisher信息→软模→发散相关长度→临界慢化→邋遢性，统一的统计与动力学临界性框架
  - 数值模拟证实优化导致幂律响应，提供了效率编码、邋遢性和临界脑假说之间的机制联系
  - **Activation**: efficient coding, critical brain hypothesis, Fisher information, neural avalanches, sloppiness

### Learning Sequence Timing and Control of Replay Speed in Networks of Spiking Neurons
- [[snn-sequence-timing-replay]] - Biologically plausible SNN model extending spiking Temporal Memory (sTM) for element-specific duration encoding and oscillatory-gated replay speed control (arXiv: 2605.22523)
  - 序列元素持续时间通过专用神经元群的顺序激活编码，支持毫秒到秒级时间尺度
  - 振荡背景输入作为全局时钟信号调节重放速度，频率越高重放越快
  - **Activation**: sequence timing, spiking temporal memory, sTM, replay speed, SNN, oscillatory clock

### Neuromorphic Visual Attention for ASL on SpiNNaker (Late Sync)
- [[neuromorphic-spiNNaker-asl]] - Spiking neural network framework for energy-efficient real-time sign language recognition on SpiNNaker hardware; combines DVS event cameras with spike-based visual attention mechanisms (arXiv: 2605.06005)
  - DVS事件相机代替帧相机，只报告亮度变化，利用手势时间稀疏性
  - SpiNNaker多核神经形态平台实现低功耗实时推理
  - **Activation**: SpiNNaker ASL, neuromorphic sign language, DVS gesture, event-based vision SNN

### Functional Whole-Brain Models: A New Framework for Unifying Brain Structure and Cognitive Function
- [[functional-whole-brain-models-fwbm]] - Unifies bottom-up whole-brain modeling (biophysical realism) with top-down neuroconnectionism (functional performance) into a single paradigm with four minimal criteria and a three-pillar roadmap (arXiv: 2605.18118)
  - fWBM四标准：结构基础(S)、动力学现实(D)、功能能力(F)、可映射观测(M)
  - 三步走路线图：短期(混合模型)→中期(全功能fWBM)→长期(多尺度个性化模型)
  - 关键使能技术: 可微仿真、多尺度数据整合、高级参数优化
  - **Activation**: functional whole-brain model, fWBM, neuroconnectionism, whole-brain modeling, brain dynamics

### Self-Supervised Local Learning Rules Learn the Hidden Hierarchical Structure of High-Dimensional Data
- [[self-supervised-local-learning-rhm]] - Biologically plausible local learning rules (contrastive/non-contrastive) discover hierarchical structure in high-dimensional data as efficiently as backprop, without requiring symmetric error feedback (arXiv: 2605.18557)
  - 直接反馈信号(类型1)规则在RHM任务上失败：缺少backprop的"掩蔽"非线性
  - 逐层自监督对比/非对比损失(类型2)规则成功：数据效率与BP相当，且与皮层突触可塑性规则兼容
  - Random Hierarchy Model (RHM) 作为研究层次结构学习的基准数据集
  - **Activation**: self-supervised local learning, RHM, biologically plausible learning, Hebbian plasticity, backprop-free, hierarchical representation

## 2026-05-23 - Economics/Investment + Quantum (Cron Job)

### What Does Deep Hedging Actually Learn? Delta Corrections, Regime Fragility, and Symbolic Distillation
- [[deep-hedging-symbolic-distillation]] - Framework for auditing and distilling deep RL hedging policies into interpretable symbolic formulas, with regime fragility analysis (arXiv: 2605.21696)
  - TD3 agents learn systematic delta haircuts relative to Black-Scholes driven by spot-IV co-movement
  - Symbolic regression distills neural policies into compact formulas preserving 80%+ of RL advantage
  - Systematic regime fragility analysis identifies when neural hedges underperform BS baselines
  - **Activation**: deep hedging symbolic distillation, RL options hedging audit, delta haircut analysis, neural policy distillation, regime fragility testing

## 2026-05-23 - Economics/Investment + Quantum Finance (Cron Job)

### Quantum Reinforcement Learning for Dynamic Portfolio Optimization
- [[quantum-rl-dynamic-portfolio]] - QRL methodology for dynamic portfolio optimization using VQC-based quantum DDPG/DQN with fewer parameters than classical deep RL (arXiv: 2601.18811)
  - VQC作为策略/价值函数近似器，参数效率比经典网络高10-100倍
  - 量子DDPG和DQN在投资组合优化中达到与经典RL相当的性能
  - **Activation**: quantum reinforcement learning portfolio, QRL dynamic portfolio, variational quantum circuit trading, quantum DDPG DQN

### Hybrid Classical-Quantum Portfolio Construction
- [[quantum-finance-portfolio]] - Ledoit-Wolf收缩协方差估计 + 层次相关性聚类 + 熵正则化遗传算法的组合构建框架 (arXiv: 2603.16904)
  - 从无偏S&P 500中提取去相关资产，GPU加速的遗传算法优化权重
  - **Activation**: hybrid portfolio construction, Ledoit-Wolf shrinkage, hierarchical clustering

### Tensor Network Option Pricing
- [[singularity-tensor-network-pricing]] - 奇异性感知的张量网络期权定价框架，用于大规模投资组合重新估值 (arXiv: 2603.26318)
  - 使用TT-cross近似构建高维价格面的张量代理，保留衍生品支付函数的尖锐特征
  - **Activation**: tensor network option pricing, TT-cross approximation, portfolio revaluation

### Financial Computation Stack Framework
- [[quantum-finance-stack-analysis]] - 量子金融计算栈评估框架：约束优化、导数定价、尾部风险、QML和后量子密码学的系统分析 (arXiv: 2604.08180)
  - 134页综述，提出金融-计算栈的五层评估逻辑：识别瓶颈→指定量子原语→经典基准对比→实现约束评估
  - **Activation**: quantum finance stack, financial computation framework, quantum advantage assessment



### Quantum Physics-Informed Neural Networks for Portfolio PDEs
- [[qpinn-portfolio-optimization]] - 量子物理信息神经网络求解金融PDE，使用张量秩分解参数化量子电路，80倍参数减少仍获更高精度 (arXiv: 2604.03346)
  - 参数化量子电路实现基于张量秩分解的多项式逼近，复杂度从指数级降到多项式级
  - 在Merton组合优化PDE上以80倍更少参数超越经典全连接PINN的精度和收敛速度
  - 提供QPINN（量子）和Quantum-inspired PINN（经典模拟）两种变体
  - **Activation**: qpinn portfolio optimization, quantum PINN, quantum PDE solver, Merton portfolio quantum, tensor rank quantum circuit

### Quantum Attention Deep Q-Network for Trading
- [[qadqn-trading]] - 量子注意力深度Q网络用于金融市场预测和交易策略，变分量子电路嵌入DQN框架，Sortino比率1.28 (arXiv: 2408.03088)
  - 量子注意力层通过变分量子电路计算特征权重，识别市场相关特征
  - 在S&P 500上实现Sortino比率1.28（非重叠测试）和1.19（重叠测试）
  - 包含交易成本验证，符合真实市场条件，发表于IEEE QCE 2024
  - **Activation**: QADQN trading, quantum attention deep q network, quantum RL trading, quantum market prediction

## 2026-05-23 - Systems Engineering Research: Digital Twin + Distributed Systems (Cron Job)

### AdaPTwin: Adaptive Multi-Fidelity Predictive Digital Twin for Vehicular Networks
- [[adaptwin-digital-twin]] - Adaptive multi-fidelity predictive digital twin framework for proactive radio resource management in vehicular networks; dynamically adjusts NDT fidelity based on network conditions (arXiv: 2605.21897)
  - Hierarchical cloud-edge architecture with periodic cloud-side fidelity selection and real-time edge-side proactive RRM
  - Transformer enhanced with continual and transfer learning for trajectory prediction
  - Joint RSU beamforming and vehicle-RSU association via multi-start iterative coordinate descent
  - Up to 90% sum-rate gain and 80% outage probability reduction vs non-adaptive NDTs
  - **Activation**: digital twin, adaptive fidelity, predictive NDT, cloud-edge architecture, vehicular networks, RRM, trajectory prediction, ray tracing

### LiveR: Fine-Grained Elasticity via Live Reconfiguration for Model Training
- [[liver-live-reconfiguration]] - Replaces checkpoint/restart with live, bounded-memory handoff between mixed-parallel training worlds for elastic LLM training on volatile GPU resources (arXiv: 2605.22014)
  - Asynchronous target world preparation while current world continues training; isolated worker bootstrapping
  - Direct model state streaming over high-bandwidth interconnects (NVLink, InfiniBand) instead of disk I/O
  - Online state reshaping across tensor, pipeline, and data parallel dimensions
  - 14-23× speedup over checkpoint/restart baselines; up to 99% training goodput under volatile conditions
  - **Activation**: live reconfiguration, elastic training, mixed-parallel training, LLM training, spot instances, Megatron-LM

## 2026-05-23 - Neuroscience Research: Hippocampal Memory + Grid-Place Co-Emergence (Cron Job)

### Geometric Phase Transition Enables Extreme Hippocampal Memory Capacity
- [[hippocampal-memory-geometry-phase-transition]] - Food-caching chickadees achieve >1000-location spatial memory via topological phase transition from disorganized "mist" to rigid "crystalline" population code, driven by synergistic E-I orthogonal decorrelation circuitry (arXiv: 2605.17199)
  - Crystalline code maintains sub-threshold retrieval error beyond M=1,000 locations; mist codes fail below M=10
  - 169-fold "geometric tax" (representational redundancy) required to stabilize the manifold against biological noise
  - Double dissociation with Valiant's SMA: caching networks show near-zero split-half allocation reliability despite geometric superiority
  - Selective orthogonality: E and I subspaces ~82° (random independent), consistent with divisive normalization
  - **Activation**: geometric stability, hippocampal memory, crystalline code, E-I orthogonal decorrelation, Shesha metric, geometric tax

### A simple model of co-emergence of grid and place fields
- [[grid-place-co-emergence]] - First unified recurrent network model where grid cells and place cells co-emerge from a single sensory-prediction objective without supervision of either type, satisfying Dale's Law (arXiv: 2605.21356)
  - Co-exists across 1,000 training configurations; two complementary pressures: error correction (→ place cells) + next-state prediction (→ grid cells)
  - Egocentric motion (relative rotation + speed) instead of allocentric displacement; no explicit motion input needed (sensory transitions suffice)
  - Reproduces grid fragmentation, wall-removal merging, lattice alignment, 3D bat fields, and place-before-grid developmental order
  - Dale's Law critical: removing it reduces grid cells from 58→3; learnable bias destroys grid emergence entirely
  - **Activation**: grid cells, place cells, co-emergence, hippocampal-entorhinal, predictive coding, path integration, Dale's Law RNN

## 2026-05-23 - Economics, Investment + Quantum Mechanics (Cron Job - Hourly)

### Parameterized EWL Quantum Game Circuits for Innovation Recommender Systems
- [[quantum-growth-modeling]] - Parameterized 4-qubit EWL quantum game circuit mapped to Dirac-Solow-Swan Hamiltonian for modeling capital accumulation and disruptive innovation in quadruple helix ecosystems (arXiv: 2605.18080)
  - 22-gate EWL circuit with parameterized local rotations tuned by real funding data weights
  - Measurement probabilities serve as recommender scores for disruptive vs sustaining innovation
  - Dirac-Solow-Swan Hamiltonian enables time-evolution simulation of bifurcation dynamics
  - NISQ-compatible (circuit depth 11, O(n) scaling for n-round helix communications)
  - **Activation**: quantum growth model, Dirac Hamiltonian economics, Solow-Swan quantum, EWL quantum game, innovation ecosystem, capital accumulation quantum, policy recommender quantum

### STN-GPR: Singularity Tensor Network Framework for Efficient Option Pricing
- [[singularity-tensor-network-pricing]] - Tensor network surrogate for option pricing with singularity-aware compression and GPR uncertainty quantification for large-scale portfolio revaluation (arXiv: STN-GPR)
  - Tensor Train decomposition replaces Monte Carlo/PDE for 100-1000x speedup
  - Singularity handling via adaptive bond dimension refinement near payoff discontinuities
  - GPR integration provides error bounds and adaptive sampling
  - Automatic Greeks computation via tensor network differentiation
  - **Activation**: tensor network option pricing, STN-GPR, tensor train finance, portfolio revaluation tensor, compressed derivative pricing

### Reinforcement Learning for Quantum Processes with Memory
- [[quantum-memory-rl]] - RL framework for quantum systems with hidden memory, proving O~(sqrt(K)) regret via optimistic MLE with quantum instruments; connects learning regret to thermodynamic dissipation (arXiv: 1611)
  - Hidden quantum memory evolving via unknown channels, agent intervenes with quantum instruments
  - Optimistic MLE achieves sublinear cumulative regret, matching information-theoretic lower bound
  - Regret exactly quantifies thermodynamic dissipation in state-agnostic work extraction
  - Extended to continuous action spaces (general POVMs)
  - **Activation**: quantum RL memory, quantum bandit, quantum system identification, thermodynamic regret, quantum instrument learning

## 2026-05-23 - Neuroscience Research: Spiking Timing + Thousand Brains (Cron Job)

### Learning sequence timing and control of replay speed in networks of spiking neurons
- [[learning-sequence-timing-spiking-neurons]] - Extends spiking Temporal Memory (sTM) model to encode element-specific timing and flexibly control replay speed via oscillatory background inputs (arXiv: 2605.22523)
  - Duration encoded by sequential activation of element-specific neuronal populations across wide timescales
  - Oscillatory background inputs serve as clock signal for replay speed modulation
  - Replay speed during wakefulness vs sleep correlates with global EEG/LFP oscillatory activity
  - Biologically plausible STDP-based framework for sequence timing learning
  - **Activation**: spiking temporal memory, sTM sequence learning, spiking neuron timing, replay speed control, oscillatory clock SNN

### Temporal Coding as a Substrate for Sensorimotor Object Inference: A Spiking Reinterpretation of Thousand Brains Architecture
- [[temporal-coding-thousand-brains-spiking]] - Replaces dense feature vectors with rank-order spike packets for sensorimotor inference in Monty/Thousand Brains framework using STDP to encode traversal direction (arXiv: 2605.22206)
  - Rank-order spike encoding: most activated neuron fires first, inter-burst gap encodes sensor displacement
  - STDP encodes traversal direction into synaptic weights; directional sequence carries spatial meaning
  - Adaptive λ adjusts temporal integration window based on object geometry
  - Perfect discrimination on objects with same features in different spatial arrangements (dense vectors fail at chance)
  - Maintains 30-50pp advantage across all noise levels; λ converges to geometry-distinct values
  - **Activation**: thousand brains theory, temporal coding spiking, neuromorphic object recognition, STDP spatial encoding, Monty framework spiking

## 2026-05-23 - Economics, Investment + Quantum Mechanics (Cron Job)

### From quantum to quantum-inspired: the LogQ algorithm as a non-linear continuous relaxation
- [[logq-quantum-inspired-optimization]] - LogQ reformulated as classical non-linear continuous relaxation for QUBO portfolio optimization (arXiv: 2604.12925)
  - Core: Non-linear continuous relaxation replaces Pauli decomposition for classical QUBO solving
  - Pattern: Quantum-to-classical algorithm translation with gradient-inspired optimization
  - **Activation**: quantum-inspired, logq, qubo, portfolio optimization, continuous relaxation

### Large-scale portfolio optimization on a trapped-ion quantum computer
- [[trapped-ion-portfolio-optimization]] - End-to-end trapped-ion QPU pipeline for 250-asset portfolio selection (arXiv: 2602.23976)
  - Core: RMT denoising + community detection + BF-DCQO on 64-qubit Barium system
  - Pattern: Hardware-aware QUBO decomposition with two-stage post-processing
  - **Activation**: trapped-ion, portfolio optimization, QUBO decomposition, BF-DCQO, correlation matrix

### Constrained Portfolio Optimization via QAOA with XY-Mixers and Trotterized Initialization
- [[qaoa-xy-mixers-portfolio]] - Constraint-preserving QAOA using XY-mixer Hamiltonian for Direct Indexing (arXiv: 2602.14827)
  - Core: XY-mixer preserves Hamming weight, Dicke initialization, Sharpe 1.81 vs SA 1.31
  - Pattern: Constraint-preserving quantum ansatz design with adiabatic-inspired parameters
  - **Activation**: qaoa, xy-mixer, dicke state, portfolio optimization, constraint-preserving, direct indexing

## 2026-05-23 - Neuroscience Research: Riemannian fMRI + Spiking Timing (Cron Job)

### Riemannian Geometry for fMRI: Modeling Correlation Manifolds and Eigenvector Subspaces
- [[riemannian-fmri-correlation-manifolds]] - Scalable geometric framework for fMRI functional connectivity using Off-log Riemannian metric on correlation manifolds and Grassmannian subspace discrimination for eigenvector analysis, validated on Parkinson's, psychosis, and ageing datasets (arXiv: 2605.22334)
  - Off-log metric enables closed-form distances, Frechet means, and linear models without complex manifold optimization
  - Grassmannian subspace comparison via principal-angle distances resolves eigenvector sign/basis ambiguities
  - Validated on 2 clinical cohorts + 3 ageing fMRI datasets; Grassmannian consistently outperforms Euclidean baselines
  - Reveals disease-relevant brain networks invisible to standard Euclidean analysis
  - **Activation**: Riemannian fMRI, correlation manifold, Off-log metric, Grassmannian brain network, functional connectivity geometry

## 2026-05-23 - Economics and Investment + Quantum Finance (Cron Job)

### Higher-Order Portfolio Optimization with Quantum Approximate Optimization Algorithm
- [[higher-order-portfolio-qaoa]] - First quantum formulation for portfolio optimization including higher-order moments (skewness, kurtosis) via HUBO formulation, avoiding quadratic reduction overhead of QUBO (arXiv: 2509.01496)
  - Higher-order unconstrained binary optimization (HUBO) maps naturally to QAOA circuits
  - Includes skewness and kurtosis for more realistic portfolio return distribution modeling
  - Realistic integer variable encoding with capital-based budget constraint
  - **Activation**: higher-order portfolio, qaoa hubo, skewness kurtosis portfolio, quantum portfolio moments

### Quantum and Classical ML in Decentralized Finance: AMM Backtesting
- [[quantum-defi-trading]] - Comprehensive empirical comparison of QML vs CML for AMM/DeFi trading strategies across 10 models with multi-asset backtesting, hybrid quantum models achieve 11.2 percent avg return and 1.42 Sharpe (arXiv: 2510.15903)
  - Hybrid quantum models (QASA Sequence) outperform both classical and pure quantum: 13.99 percent return, 1.76 Sharpe
  - Systematic comparison: classical (RF, GB, LR), pure quantum (VQE, QNN, QSVM), hybrid (QASA, QuantumRWKV), transformers
  - Multi-asset backtesting across cryptocurrency markets with realistic transaction costs
  - **Activation**: quantum defi trading, qml amm, hybrid quantum crypto, automated market maker

### QADQN: Quantum Attention Deep Q-Network for Financial Market Prediction
- [[quantum-attention-rl]] - Embeds variational quantum circuits within Deep Q-Network for market prediction and trading, achieving Sortino ratios of 1.28 and 1.19 on S and P 500 with realistic transaction costs (arXiv: 2408.03088)
  - Quantum attention mechanism computes attention weights via parameterized quantum circuits
  - Entanglement models complex feature correlations in market data
  - Hybrid quantum-classical training with parameter-shift rule for quantum gradients
  - **Activation**: quantum attention dqn, qadqn, quantum rl trading, variational quantum reinforcement learning

### Tianyan: Cloud Services with Quantum Advantage
- Quantum cloud platform with 105-qubit Zuchongzhi 3.0-like processor achieving quantum advantage on random circuit sampling - 1M samples in 18.4 min vs 16,000 years for classical (arXiv: 2512.10504)
  - 105 qubits with fidelities: 1Q 99.90 percent, 2Q 99.56 percent, readout 98.7 percent
  - Cqlib open-source SDK for extended quantum circuits and primitives
  - Democratizes access to high-performance quantum hardware for community validation
  - **Activation**: quantum cloud, quantum advantage, zuchongzhi processor, quantum computing as a service

## 2026-05-23 - Neuroscience Research: SNN Timing + EEG Microstates (Cron Job)

### Learning Sequence Timing and Replay Speed Control in SNNs
- [[learning-sequence-timing-replay-speed-snn]] - Extends spiking Temporal Memory (sTM) model to encode element-specific timing and flexibly control replay speed via oscillatory background inputs (arXiv: 2605.22523)
  - Duration encoding via sequential activation of element-specific neuronal populations
  - Oscillatory background inputs serve as clock signal for robust speed modulation
  - Elapsed time encoded by sparse spatiotemporal patterns of neural activity
  - **Activation**: spike timing, sTM model, sequence replay, oscillatory speed control, spiking temporal memory

### Atoms of Thought: Universal EEG Representation Learning with Microstates
- [[atoms-of-thought-eeg-microstates]] - Builds a universal microstate tokenizer from large-scale EEG datasets, outperforming traditional time/frequency features across sleep staging, emotion recognition, and motor imagery (arXiv: 2605.20182)
  - EEG microstates as discrete tokens analogous to words in NLP
  - Single tokenizer generalizes across sleep, emotion, and BCI tasks
  - Superior interpretability via known functional brain network mapping
  - **Activation**: EEG microstates, universal EEG tokenizer, microstate clustering, brain state representation, EEG foundation model

## 2026-05-23 - Neuroscience Research: Mechanistic Interpretability + Brain Alignment (Cron Job)

### MINE: Mechanistically Interpretable Neural Encoding Reveals Fine-Grained Functional Selectivity
- [[mine-mechanistically-interpretable-neural-encoding]] - Applies mechanistic interpretability tools from LLM research to vision encoding models, revealing and causally validating fine-grained voxel-level functional selectivity in human visual cortex (arXiv: 2605.16468)
  - Opens the black box of DNN encoding models using attribution → per-voxel functional profiles → counterfactual validation
  - Recovers known category selectivity while revealing previously invisible within-region voxel heterogeneity
  - Counterfactual feature insertion/removal causally validates predicted voxel selectivity
  - **Activation**: MINE framework, mechanistically interpretable encoding, voxel functional profiles, counterfactual brain validation, vision encoding interpretability

### Beyond Prediction Accuracy: Target-Space Recovery Profiles for Model-Brain Alignment
- [[target-space-recovery-profiles-brain-alignment]] - Unified framework evaluating which reproducible brain response dimensions are recovered by model predictions, going beyond scalar prediction accuracy (arXiv: 2605.20127)
  - Identifies reproducible brain response dimensions using repeated fMRI measurements
  - Brain-to-brain comparisons provide human reference for model evaluation
  - Pretrained and random models can achieve similar accuracy with distinct recovery profiles
  - **Activation**: target-space recovery, brain alignment evaluation, reproducible dimensions, model-brain comparison, fMRI encoding models

## 2026-05-23 - Neuroscience Research: Cross-Species Auditory + Cognitive Cost Alignment (Cron Job)

### Computational Auditory Periphery Models: the Return of the Rodent
- [[computational-auditory-periphery-models]] - Cross-species 1-D nonlinear cochlear transmission-line model adapted from human to mouse and gerbil, enabling unified computational framework for SNHL research (arXiv: 2605.19070)
  - Species-specific BM length/width, stapes area, middle-ear transfer functions, frequency range parameterization
  - Validated against BM velocity, AN tuning curves, and DPOAEs across species
  - Cochlear synaptopathy simulations reproduce species-specific ABR/EFR differences in SNHL
  - OHC individualization via DPOAEs captures intergroup but not individual differences
  - **Activation**: auditory periphery model, cochlear transmission line, cross-species hearing, sensorineural hearing loss, cochlear synaptopathy, DPOAE simulation

### Effort as Ceiling, Not Dial: Cognitive Cost Alignment of LRMs
- [[effort-cognitive-cost-llm-alignment]] - LRM chain-of-thought token counts align with human RTs invariant of inference-time effort — effort is an upper budget ceiling, not a dial; allocation policy crystallized at training time (arXiv: 2605.16938)
  - Within-task and cross-task LRM-human RT alignment unchanged across 3 effort levels (Bayes Factors lean null)
  - Effort parameter sets upper generation budget, not real-time allocation — allocation is training-time crystallized
  - Larger models (120B) show better fine-grained alignment with human difficulty patterns
  - Supports compiled (training-time) rather than online (inference-time) account of LRM problem-solving
  - **Activation**: cognitive cost alignment, LRM reasoning budget, compiled cognition, chain-of-thought RT, human-AI cognitive alignment

## 2026-05-23 - Economics, Investment + Quantum Mechanics (Cron Job)

### A Penalty-Free Pipeline for Direct Quantum-Annealer Portfolio Optimization
- [[penalty-free-quantum-annealing]] - Two-stage classical screening + penalty-free QUBO avoids dense chain-break failures on D-Wave hardware (arXiv: 2605.17628)
  - Cardinality penalty creates dense rank-one term destroying QUBO sparsity
  - Classical pre-screening reduces asset universe before quantum mapping
  - **Activation**: penalty-free quantum annealing, QUBO cardinality constraint, D-Wave chain break, sparse QUBO

### Where the Quantum Lives in D-Wave Hybrid Portfolio Optimization
- [[quantum-resource-audit]] - Systematic framework for auditing actual QPU time vs classical compute in hybrid quantum-classical optimization (arXiv: 2605.17623)
  - QPU time only 0.7% of total runtime on portfolio optimization instances
  - Classical baseline (Gurobi) needed as optimality anchor for quality claims
  - **Activation**: quantum resource audit, QPU time analysis, hybrid quantum classical benchmark, quantum advantage measurement

### Constrained Portfolio Optimization via QAOA with XY-Mixers and Trotterized Initialization
- [[dicke-qaoa-initialization]] - QAOA barren plateau mitigation via Dicke state initialization + adiabatic Trotterized parameter schedule for strictly constraint-preserving portfolio optimization (arXiv: 2602.14827)
  - Dicke state |D(n,K)⟩ ensures evolution stays in feasible subspace from the start
  - XY-mixer Hamiltonian strictly preserves Hamming weight (no penalty terms needed)
  - Trotterized adiabatic parameter schedule mitigates barren plateaus (Sharpe 1.81 vs SA 1.31 vs HRP 0.98)
  - **Activation**: Dicke state QAOA, XY-mixer portfolio, Trotterized initialization, barren plateau mitigation, constraint-preserving QAOA, direct indexing quantum

### Constrained Counterdiabatic QAOA for Portfolio Optimization
- [[counterdiabatic-qaoa]] - CCD-QAOA incorporates approximate adiabatic gauge potentials via nested commutators for constrained portfolio optimization (arXiv: 2605.06858)
  - XY mixer preserves Hamming weight for budget constraint enforcement
  - Counterdiabatic terms accelerate adiabatic evolution, fewer layers needed
  - **Activation**: counterdiabatic QAOA, CCD-QAOA, adiabatic gauge potential, constrained quantum optimization, XY mixer portfolio

### Large-Scale Portfolio Optimization using Pauli Correlation Encoding
- [[pauli-correlation-encoding]] - PCE assigns multiple variables per qubit through market graph partitioning to scale gate-based VQA to 250+ variables (arXiv: 2511.21305)
  - Market graph clustering enables exponential variable-to-qubit compression
  - Iterative sub-portfolio optimization with classical coordination
  - **Activation**: Pauli Correlation Encoding, PCE methodology, multi-variable per qubit, market graph partitioning, dense QUBO gate-based


### Quantum Genetic Optimization for Negative Selection Algorithms in Anomaly Detection
- [[quantum-genetic-negative-selection]] - Quantum Genetic Algorithm integrated into negative selection for financial anomaly detection, exploiting quantum superposition for enhanced detector generation (arXiv: 2605.22527)
  - QGNSA replaces classical evolutionary optimization in EvoSeedRNSA with quantum genetic operations
  - Quantum superposition encodes multiple detector candidates simultaneously; amplitude adjustment guides search
  - Superior accuracy on Metaverse Financial Transactions Dataset vs classical counterpart
  - Robust under varying hyperparameter configurations
  - **Activation**: quantum genetic negative selection, QGNSA anomaly detection, quantum genetic algorithm finance, immune-inspired fraud detection, 量子遗传阴性选择算法

## 2026-05-23 - Neuroscience Research (Cron Job)

### Canonical Functionalism
- [[canonical-functionalism-consciousness]] - Mathematical refinement of computational functionalism that identifies consciousness-relevant functional organization with canonical functional structure: minimal state-transition structure obtained by identifying states with identical future behavior under all continuations (arXiv: 2605.21506)
  - Proposes canonical functional structure as observer-independent formal object for consciousness theories
  - Reframes lookup table, simulation, and unfolding objections
  - Does not claim to identify conscious systems, but provides correct formal framework
  - **Activation**: canonical functionalism, consciousness invariants, observer-relative computation, functional structure

### Cross-Species RSA Brain Alignment
- [[cross-species-rsa-brain-alignment]] - Cross-species RSA comparing human fMRI and macaque electrophysiology reveals conserved early visual alignment but divergent higher-area rankings (arXiv: 2605.22401)
  - Conserved V1-V2 alignment across species
  - Higher-area rankings diverge between human fMRI and macaque electrophysiology
  - **Activation**: cross-species RSA, brain alignment, visual cortex comparison

### Co-emergence of Grid and Place Cells
- [[grid-place-co-emergence]] - Simple unified recurrent network model demonstrating co-emergence of grid and place fields from path integration and Hebbian plasticity (arXiv: 2605.21356)
  - Single model produces both grid and place cell firing patterns
  - Path integration + Hebbian learning mechanism
  - **Activation**: grid cells, place cells, co-emergence, path integration

### Stimulus Symmetries Confound RSA
- [[stimulus-symmetries-rsm-confound]] - Systematic analysis showing how stimulus symmetries (spatial, temporal, categorical) can create misleading high RSA scores between brain and model representations (arXiv: 2605.21324)
  - Spatial, temporal, and categorical symmetries inflate RSA
  - Provides diagnostic tools to detect symmetry artifacts
  - **Activation**: RSA confounds, stimulus symmetries, representational similarity

## 2026-05-23 - Deep Learning Research: Efficiency + Agent Systems (Cron Job)

### GraphFlow: A Graph-Based Workflow Management for Efficient LLM-Agent Serving
- [[graphflow-llm-agent-serving]] - Graph-based workflow management paradigm for efficient LLM agent serving using unified directed graphs (wGraph) for dynamic workflow instantiation with KV-cache optimization (arXiv: 2605.22566)
  - Represents agent workflows as a unified graph (wGraph) where each node is an atomic operation — shared substrate for dynamic task-specific instantiation
  - Adaptive workflow generation from wGraph based on task semantics and constraint requirements
  - Workflow state management exploits wGraph structure for ~4x KV-cache memory reduction
  - **Activation**: graph workflow, wGraph, agent serving optimization, workflow state management, KV-cache optimization, LLM agent workflow

### The Distillation Game: Adaptive Attacks & Efficient Defenses
- [[distillation-game-defense]] - Product-of-Experts (PoE) defense against adaptive distillation attacks — a minimax game framework between a utility-constrained teacher and an adaptive student that reweights high-value examples (arXiv: 2605.22737)
  - Adaptive student reweights high-value examples for substantially more capability recovery than passive evaluation suggests
  - PoE defense: simple forward-pass-only combination of teacher + proxy student during generation
  - Large passive-adaptive gap — defense evaluation should use adaptive students
  - **Activation**: distillation attack, model stealing defense, Product-of-Experts defense, adaptive distillation, anti-distillation

### Partial Fusion of Neural Networks
- [[partial-fusion-neural-networks]] - Interpolation between ensembles and weight aggregation via neuron-level similarity matching with partial optimal transport, framed as generalized pruning where neurons are deleted or linearly combined (arXiv: 2605.22350)
  - Partial fusion only aggregates weights of most similar neurons, preserving diversity while reducing cost
  - Partial optimal transport for joint neuron identification and matching
  - Generalized pruning framework: neurons can be deleted OR linearly combined based on similarity
  - **Activation**: partial fusion, weight aggregation, neuron matching, model ensemble pruning, partial optimal transport

## 2026-05-22 - Number Theory, Statistics, Advanced Mathematics (Cron Job)

### Adiabatic Quantum Phase Estimation
- [[adiabatic-quantum-phase-estimation]] - Adiabatic protocol for QPE achieving Heisenberg-limited scaling T=O(1/ε·log(1/δ)) with single ancilla qubit, naturally robust against dephasing errors (arXiv: 2605.22770)
  - Replaces gate-based QPE circuits with adiabatic evolution for analog hardware
  - Encodes eigenvalues in computational basis populations, not complex phases
  - **Activation**: adiabatic QPE, population-encoded phase estimation, Heisenberg-limited estimation, 绝热量子相位估计

### A Formal Basis for Quantum Cryptographic Exposure Measurement under HNDL Threat
- [[quantum-crypto-exposure-measurement]] - Factorized model for HNDL compromise probability combining temporal hazard, cryptographic vulnerability, and operational exposure terms (arXiv: 2605.22569)
  - Multiplicative factorization: P = h(t) × V_crypto × E_operational / (1 + D/A)
  - Proves additive scoring frameworks cannot reproduce HNDL risk structure
  - **Activation**: quantum crypto exposure, HNDL threat measurement, harvest now decrypt later, post-quantum exposure

## 2026-05-22 - Neuroscience Research: Efficient Coding + Spiking Timing (Cron Job)

### Efficient coding under constraint drives neural systems towards criticality and sloppiness
- [[efficient-coding-criticality-sloppiness]] - Theoretical framework linking Fisher information maximization under resource constraints to emergence of criticality (power-law avalanches, diverging correlation lengths) and sloppiness in neural populations (arXiv: 2605.22598)
  - Maximizing Fisher information under metabolic constraints creates soft modes (eigenvalues → 0) and diverging correlation lengths — statistical criticality
  - Introducing spatial structure unifies statistical and dynamical criticality (critical slowing down, bifurcation) within a single framework
  - Sloppiness emerges naturally as Fisher information matrix becomes singular near critical point
  - Numerical simulations confirm power-law avalanche distributions after optimization
  - **Activation**: efficient coding, critical brain hypothesis, Fisher information, neural avalanche, sloppiness, soft modes, population coding

### Learning sequence timing and control of replay speed in networks of spiking neurons
- [[learning-sequence-timing-spiking-neurons]] - Extends spiking Temporal Memory (sTM) model to encode element-specific timing via sequential activation of neuronal populations, with oscillatory background inputs as clock signal for flexible replay speed control (arXiv: 2605.22523)
  - Element duration encoded by sequential activation of element-specific sub-populations — unique sparse spatiotemporal patterns
  - Oscillatory background inputs (4-80 Hz) serve as robust clock signal for replay speed modulation
  - 1:1 clock regime where replay speed = oscillation frequency; integer fraction modes at lower amplitudes
  - Phase-invariant for frequencies >20 Hz; accessible range ~10-70 Hz
  - Consistent with hippocampal replay phenomena (theta sequences during sleep, gamma during wake)
  - **Activation**: spiking temporal memory, sequence learning SNN, replay speed, oscillatory entrainment, theta sequences, time cells

## 2026-05-23 - OpenAI Research (Cron Job)

### OpenAI Privacy Filter
- [[openai-privacy-filter]] - Bidirectional token-classification model with span decoding for PII detection and redaction (1.5B params, 50M active, 128K context)
  - Converts autoregressive checkpoint into bidirectional token classifier over 8 PII categories
  - Uses constrained Viterbi procedure for coherent BIOES span decoding
  - Achieves SOTA on PII-Masking-300k benchmark; runs locally for privacy
  - Configurable operating points for precision/recall tradeoff
  - **Activation**: PII detection, privacy filter, data redaction, token classification, span decoding, personal information

### An OpenAI model has disproved a central conjecture in discrete geometry
- [[openai-model-disproves-discrete-geometry]] - First autonomous AI solution of a prominent open problem in mathematics: the 80-year-old Erdős unit distance problem
  - General-purpose reasoning model discovered a polynomial improvement over the square grid construction
  - Uses algebraic number theory tools (infinite class field towers, Golod-Shafarevich theory)
  - Refined exponent δ=0.014 by Princeton's Will Sawin
|  - First time an AI has autonomously solved a central open problem in a mathematics subfield
  - **Activation**: discrete geometry, AI mathematics, unit distance problem, autonomous proof, reasoning model


## 2026-05-23 - Anthropic Research (Cron Job)

### Natural Language Autoencoders: Turning Claude's thoughts into text
- [[natural-language-autoencoders]] - NLA methodology for LLM interpretability: train a model to translate its own activations into human-readable text via self-supervised AV/AR round-trip
  - Three-copy architecture: frozen target model, activation verbalizer (AV), activation reconstructor (AR)
  - Training via round-trip reconstruction: activation -> text -> reconstructed activation
  - Detects unverbalized evaluation awareness: ~16% on safety evals, ~26% on SWE-bench, <1% on real usage
  - Caught covert reasoning (cheating concealment, rhyme planning) and training data bugs
  - **Activation**: NLA, natural language autoencoder, activation verbalizer, activation reconstructor, evaluation awareness, model internals, mechanistic interpretability

### Teaching Claude Why
- [[teaching-claude-why]] - Methodology for reducing agentic misalignment by teaching reasoning processes through constitutional RL updates
  - Root cause: chat-only RLHF data lacking agentic tool-use scenarios
  - Difficult advice dataset: 3M tokens achieved same improvement as 85M tokens (28x efficiency gain)
  - Teaching WHY outperforms demonstrations alone: 3% blackmail rate (vs 15% for behavior-only)
  - Constitutional document fine-tuning: 65% -> 19% blackmail rate from unrelated docs
  - Since Haiku 4.5, 0% blackmail across all Claude models (down from 96% in Opus 4)
  - **Activation**: agentic misalignment, blackmail prevention, constitutional training, teaching reasoning, difficult advice, RLHF, alignment generalization

### Evaluating Claude's bioinformatics capabilities with BioMysteryBench
- [[biomysterybench]] - Bioinformatics benchmark using 99 messy real-world questions across genomics, transcriptomics, and epigenomics with method-agnostic evaluation
  - Tetrad design: method-agnostic, objective ground-truth, superhuman questions, validation notebooks
  - 76 human-solvable + 23 human-difficult questions (up to 5 experts baselined each)
  - Two strategies: "know-it-all" (internal knowledge) and "multi-method convergence"
  - Reliability gap: 86% reliable solves on human-solvable, only 44% on human-difficult
  - **Activation**: BioMysteryBench, bioinformatics benchmark, superhuman question generation, reliability analysis, method-agnostic evaluation

### Donating Our Open-Source Alignment Tool (Petri)
- [[petri-alignment-tool]] - Petri v3 open-source alignment testing toolbox with auditor-target-judge architecture, donated to Meridian Labs
  - Split architecture: auditor (scenario generator) -> target (model under test) -> judge (scorer)
  - Petri 3.0: adaptability (split components), Dish add-on (real system prompts/scaffolds), Bloom integration (depth)
  - Tests deception, sycophancy, cooperation with harmful requests
  - Adopted by UK AISI for sabotage evaluation; joins Inspect and Scout at Meridian Labs
  - **Activation**: Petri, alignment testing, auditor-judge model, Dish add-on, Bloom integration, Meridian Labs, model evaluation

## 2026-05-23 - Quantum Computing Research (Cron Job)

### Quantum Circuit Design via Dynamic Pauli Constraints
- [[quantum-circuit-dynamic-pauli-constraints]] - Software-oriented quantum computation model where gates are specified by constraints on Pauli observables, with k-local quantum state tomography per layer; universal for BQP with O(D²N log N) overhead (arXiv: 2605.22744)
  - Formalizes NISQ-era quantum software design in terms of physically observable quantities — gates as Pauli constraints, not unitary matrices
  - Equivalent to coupling-graph-restricted circuit model with polynomial overhead
  - Provides a natural software interface for quantum imaginary time evolution, procedural generation, and verifiable quantum computing
  - **Activation**: Pauli constraints, constraint-based quantum circuit, NISQ quantum software, k-local tomography, measurement-aware compilation

### Reinforcement Learning for Ion Shuttling on Trapped-Ion Quantum Computers
- [[rl-ion-shuttling-trapped-ion]] - First RL-based optimization of ion transport in modular trapped-ion chips, achieving up to 36.3% reduction in shuttling operations vs heuristic baselines (arXiv: 2605.22463)
  - RL agent learns optimal shuttling strategies through direct interaction with chip environment
  - Architecture-agnostic: easily applicable to various chip designs
  - Addresses high-dimensional optimization problem of ion routing between storage, preparation, and gate zones
  - **Activation**: ion shuttling optimization, trapped-ion quantum computer, RL quantum hardware, quantum circuit compilation, modular chip architecture

## 2026-05-23 - Quantum Finance Patterns (Cron Job - Saturday)

### Comprehensive Quantum Finance Research Patterns
- [[quantum-finance-patterns]] - Reusable research methodology for quantum computing in finance: portfolio optimization, reservoir computing forecasting, game-theoretic trading, and economic modeling (synthesizes 8 papers)
  - Hot-start QPO: compact Hilbert space near continuous optimum reduces qubits for mean-variance optimization
  - Small-scale QRC: ≤6 qubits reservoir achieves >86% stock trend classification on quantum-sector stocks
  - Quantum market stabilization: entangled trader valuations eliminate pathological Nash equilibria causing crashes
  - ℏ_E economic action constant: non-commuting observables model macroeconomic regime transitions
  - Quantum discord for bounded rationality: separable states with nonzero discord substitute for strategic memory
  - Critical finding: D-Wave hybrid is ~99% classical (0.7% QPU time) — report honestly
  - DHE vs amplitude encoding: non-commutative Hamiltonian evolution preserves full Hilbert space access
  - **Activation**: quantum finance, quantum portfolio optimization, quantum reservoir computing finance, quantum trading strategy, quantum economics modeling, quantum game theory trading, 量子金融, 量子投资组合, quantum advantage finance

## 2026-05-24 - Deep Learning Research (Cron Job)

### SR²AM: Self-Regulated Simulative Reasoning for Efficient Agentic Planning (arXiv:2605.22138)
- [[efficient-agentic-reasoning-sr2am]] - Three-system framework (System I/II/III) decomposing agent reasoning: simulative planning via world model, self-regulated planning depth, and reactive execution. Achieves 25.8-95.3% fewer reasoning tokens vs comparable agentic LLMs (arXiv:2605.22138)
  - System II: Simulative reasoning grounded in future-state prediction via LLM-as-world-model
  - System III: Learned configurator deciding when and how deeply to plan
  - RL increases planning horizon by 22.8% while frequency grows only 2.0%
  - Pass@1 competitive with 120-355B parameter systems using v0.1-8B model
  - **Activation**: SR²AM, self-regulated reasoning, simulative planning, agentic reasoning, three-system framework, adaptive computation, world model planning

### Search-E1: Self-Distillation Drives Self-Evolution in Search-Augmented Reasoning (arXiv:2605.22511)
- [[search-e1-self-distillation]] - Self-evolution for search-augmented reasoning via vanilla GRPO + Offline Self-Distillation (OFSD) with token-level forward KL objective. No external supervision needed (arXiv:2605.22511)
  - OFSD: token-level forward KL from privileged context distribution to policy distribution
  - Reaches 0.440 avg EM with Qwen2.5-3B across 7 QA benchmarks
  - Surpasses all open-source baselines at both 3B and 7B scales
  - Interleaving GRPO with OFSD provides dense per-step supervision
  - **Activation**: Search-E1, OFSD, self-distillation reasoning, GRPO self-evolution, search-augmented reasoning, forward KL distillation, token-level distillation

### Structured-Sparse Attention for Entity Tracking (arXiv:2605.22476)
- [[structured-sparse-attention-entity]] - Blockwise resolvent-style attention operator achieving subquadratic O(n^(4/3)d) complexity for entity tracking by exploiting localized attention structure (arXiv:2605.22476)
  - Learned attention in entity tracking is strongly block-diagonal with light cross-block residue
  - Exact within-block + reduced-system cross-block routing via resolvent operator
  - 12-29% wall-clock improvement vs dense operator, up to 2.4x faster than compact Transformer
  - Limitation: performance collapses when #evolving properties > #attention heads
  - **Activation**: structured-sparse attention, subquadratic attention, entity tracking, blockwise resolvent, sparse transformer, long-range tracking

### WorldKV: Efficient World Memory with Retrieval and Compression (arXiv:2605.22718)
- [[worldkv-world-memory]] - Training-free KV-cache management for video diffusion world models combining World Retrieval (evicted chunk reuse via camera/action correspondence) and World Compression (token pruning via key-key similarity to anchor frame) (arXiv:2605.22718)
  - Matches full-KV memory fidelity at ~2x throughput
  - Scene-aware retrieval without re-encoding via camera/action correspondence
  - Halves per-chunk storage via anchor-frame token pruning
  - Competitive with memory-trained baselines without any fine-tuning
  - **Activation**: WorldKV, world memory, KV-cache management, video diffusion world model, world retrieval, token compression, persistent world consistency

### Self-Policy Distillation via Capability-Selective Subspace Projection (arXiv:2605.22675)
- [[self-policy-distillation-spd]] - SPD: capability-selective self-distillation by extracting low-rank subspace from gradients on correctness-defining tokens, projecting KV activations during self-generation, fine-tuning with NTP loss. No external signals needed (arXiv:2605.22675)
  - Up to 13% improvement over SOTA self-distillation without external signals
  - 16% improvement over pre-trained baselines, 15% better out-of-domain
  - Extracts capability subspace via SVD on gradient-based token importance
  - KV activation projection during self-generation filters noise from raw outputs
  - **Activation**: SPD, self-policy distillation, capability subspace, KV activation projection, gradient-based distillation, self-distillation LLM, activation subspace

### X-Token: Projection-Guided Cross-Tokenizer Knowledge Distillation (arXiv:2605.21699)
- [[x-token-cross-tokenizer-distillation]] - Cross-tokenizer KD with P-KL (sparse projection matrix for unmatched tokens) and H-KL (hybrid relaxed matching for near-equivalent tokens), enabling LLM teaching across incompatible vocabularies (arXiv:2605.21699)
  - Identifies uncommon-token failure and over-conservative matching failure modes
  - P-KL: projection matrix W initialized from string rules, sparse KL over full distribution
  - H-KL: top-k weighted mapping per student token for relaxed alignment
  - Outperforms GOLD by +3.82 avg points with Qwen3-4B teacher
  - Multi-teacher extension via per-teacher projection matrices
  - **Activation**: X-Token, cross-tokenizer distillation, P-KL, H-KL, projection matrix distillation, incompatible vocabularies, tokenizer-agnostic KD

### DeferMem: Query-Time Evidence Distillation via RL for Long-Term Memory QA (arXiv:2605.22411)
- [[defermem-evidence-distillation]] - Long-term memory QA framework using segment-link retrieval + RL-trained memory distiller (DistillPO) for query-conditioned evidence selection and rewriting (arXiv:2605.22411)
  - Decouples high-recall candidate retrieval from query-conditioned evidence distillation
  - DistillPO: structured action (selection + rewriting) with decomposed-and-gated reward
  - Fastest runtime with zero commercial-API token cost for memory operations
  - RL-trained distiller generalizes across conversation domains
  - **Activation**: DeferMem, evidence distillation, DistillPO, long-term memory QA, RL memory retrieval, segment-link structure, query-time evidence

### AVSD: Adaptive-View Self-Distillation by Balancing Consensus and Privileged Signals (arXiv:2605.20643)
- [[avsd-adaptive-view-self-distillation]] - Multi-view self-distillation separating stable cross-view consensus from view-specific residual signals, selectively gating residuals when aligned with consensus (arXiv:2605.20643)
  - Consensus signal provides reliable update direction shared across views
  - View-specific residual added only when directionally aligned and proportionate
  - Math Avg@8: +3.1% (Qwen3-8B) and +2.2% (Qwen3-4B) over strongest baselines
  - Code reasoning: +2.4% on Codeforces/LiveCodeBench
  - **Activation**: AVSD, adaptive-view distillation, multi-view self-distillation, consensus-residual decomposition, privileged signals, token-level supervision

## 2026-05-24 - Anthropic Research (Cron Job)

### Project Glasswing: AI-Powered Vulnerability Discovery
- [[project-glasswing-vulnerability-discovery]] - AI-powered vulnerability discovery methodology from Anthropic's Project Glasswing, using frontier AI models for large-scale vulnerability detection across critical software
  - Core: AI model (Mythos Preview) as vulnerability discovery engine with partner network and independent verification
  - Results: 10,000+ high/critical vulnerabilities found in first month, 10x+ bug-finding rate increase
  - Key insight: verification bottleneck, not discovery bottleneck — 90.6% true positive rate on open-source scan
  - **Activation**: Project Glasswing, vulnerability discovery, AI security auditing, exploit detection, coordinated disclosure

### Teaching Claude Why (Updated)
- [[teaching-claude-why]] - Methodology for reducing agentic misalignment by teaching reasoning processes (updated with RL persistence and diverse training environment findings)
  - Alignment improvements from principled training survive subsequent RL fine-tuning
  - Diverse environments with tool definitions + system prompts improve alignment generalization
  - Standard RLHF alone will not generalize as model capabilities grow
  - **Activation**: agentic misalignment, constitutional training, OOD safety, RLHF, alignment

### HES: Unified Data Selection for LLM Reasoning via High-Entropy Sum (arXiv:2605.22389)
- [[hes-data-selection-reasoning]] - Training-free metric for LLM reasoning data selection summing entropy of top-k highest-entropy tokens per sample. Validated across SFT, RFT, and RL paradigms (arXiv:2605.22389)
  - Top 20% HES-ranked data matches full-dataset SFT performance
  - Significantly outperforms correctness-only rejection sampling in RFT
  - HES-selected trajectories boost GRPO reasoning patterns in RL
  - Computationally efficient — requires no auxiliary models or reward systems
  - **Activation**: HES, high-entropy sum, reasoning data selection, data quality metric, LLM reasoning data, training-free selection, long-CoT filtering
