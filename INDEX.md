## 2026-05-19 - Computer Science + Quantum (Cron Job - Hourly)

### AQKA: Active Quantum Kernel Acquisition Under a Shot Budget
- [[aqka-active-quantum-kernel-acquisition]] - Closed-form gradient-based optimal shot allocation for quantum kernel estimation (arXiv: 2605.14672)
  - 核心要点 1: Optimal shot allocation s_ij* ∝ |g_ij|√(K_ij(1-K_ij)) using KRR/SVM dual variables
  - 核心要点 2: Regime decomposition - AQKA dominates budget-limited, Nyström-QKE wins at saturating budgets
  - 核心要点 3: Live hardware results: +26-32 pts on 156-qubit Heron, advantage grows with N
  - **Activation**: AQKA, active quantum kernel, shot budget allocation, adaptive shot allocation, quantum kernel ridge regression, 2605.14672

## 2026-05-19 - Computer Science + Quantum (Hourly Cron Job)

### Shot-Based Quantum Encoding: A Data-Loading Paradigm for Quantum Neural Networks
- [[shot-based-quantum-encoding]] - NISQ data loading via shot distribution over input states (arXiv: 2604.06135)
  - 核心要点 1: SBQE allocates shots according to data-dependent classical distributions instead of deep encoding circuits
  - 核心要点 2: Achieves high expressivity with shallow circuits — optimizes the hardware-native resource (shots)
  - 核心要点 3: Outperforms angle/amplitude/basis encoding on expressivity-depth tradeoff
  - **Activation**: shot-based encoding, SBQE, quantum data loading, quantum neural network encoding, 2604.06135

### Soft-Quantum Algorithms
- [[soft-quantum-algorithms]] - Direct matrix element optimization bypassing gate-based VQC training (arXiv: 2604.06523)
  - 核心要点 1: Trains unitary matrix elements directly, avoiding gate decomposition overhead and barren plateaus
  - 核心要点 2: Efficient for few-qubit problems with large datasets — matrix size scales as 2^n
  - 核心要点 3: Post-training compilation step required to deploy on quantum hardware
  - **Activation**: soft-quantum, direct matrix optimization, quantum operation optimization, VQC alternatives, 2604.06523

### Do Quantum Transformers Help? A Systematic VQC Architecture Comparison
- [[vqc-architecture-comparison]] - Systematic comparison of FC-VQC, ResNet-VQC, QT, FQT on tabular benchmarks (arXiv: 2604.23931)
  - 核心要点 1: ResNet-VQC provides best accuracy-parameter tradeoff for most tabular tasks
  - 核心要点 2: Quantum transformers show promise but require more qubits than NISQ devices provide
  - 核心要点 3: No single architecture dominates — benchmark-dependent selection needed
  - **Activation**: VQC architecture, quantum transformer, variational quantum circuit comparison, quantum tabular learning, 2604.23931

## 2026-05-19 - Computer Science + Quantum (Cron Job)

### Winning Lottery Tickets in Neural Networks via a Quantum-Inspired Classical Algorithm
- [[quantum-inspired-lottery-tickets]] - Classical dequantization of quantum ML lottery ticket algorithm achieving polynomial-time sparse subnetwork selection via ridgelet transform sampling (arXiv: 2605.13979)
  - 核心要点 1: QML algorithm selects sparse subnetworks from large shallow NNs via ridgelet transform
  - 核心要点 2: Classical dequantized algorithm runs in O(poly(D)) vs O(exp(D)) naive approach
  - 核心要点 3: Achieves comparable empirical risk to exact sampling, much better than uniform sampling
  - **Activation**: quantum-inspired, lottery tickets, dequantization, ridgelet sampling, sparse subnetwork, 量子启发中奖彩票, 2605.13979

### Quantum Feature Pyramid Gating for Seismic Image Segmentation
- [[quantum-feature-pyramid-gating]] - Hybrid quantum-classical image segmentation using multi-scale quantum feature extraction with adaptive gating mechanism (arXiv: 2605.15370)
  - 核心要点 1: Multi-scale feature pyramid with quantum feature encoding at each scale
  - 核心要点 2: Parameterized quantum circuits process encoded features, adaptive gates fuse quantum+classical
  - **Activation**: quantum feature pyramid, QFPG, quantum segmentation, hybrid quantum-classical, 量子特征金字塔, 2605.15370

### Wavelet Variance Equipartition as Threshold for Quantum Kernel TN-Simulability
- [[wavelet-variance-equipartition-quantum]] - Wavelet scaling exponent α as diagnostic for representation quality and classical simulability boundary of quantum kernels (arXiv: 2605.11557)
  - 核心要点 1: α=1/2 is sharp boundary — area-law (>1/2) admits classical emulation, volume-law (<1/2) is exponentially hard
  - 核心要点 2: VideoMAE latents show spatial tokens ~0.423, feature channels ~-0.123 (deep volume-law)
  - 核心要点 3: Shot noise wall: measurement budget M=Ω(d²) constrains quantum ML scalability
  - **Activation**: wavelet variance equipartition, scaling exponent, quantum kernel simulability, tensor network bond dimension, 小波方差等配分, 2605.11557

## 2026-05-19 - Neuroscience Research (Cron Job)

### Decoding Alignment without Encoding Alignment: A critique of similarity analysis in neuroscience
- [[decoding-encoding-alignment-critique]] - Fundamental critique of RSA/CKA/Procrustes showing decoding metrics saturate with small subpopulations and are blind to encoding manifold topology (arXiv: 2605.05907)
  - 核心要点 1: RSA/CKA/Procrustes can be saturated by 5% of neurons and miss functional architecture
  - 核心要点 2: Encoding manifold (neuron-centric) vs decoding manifold (stimulus-centric) duality
  - 核心要点 3: Causal evidence via MNIST — identical decoding scores with different encoding topologies
  - 核心要点 4: Gromov-Wasserstein distance as complementary metric for neural population comparison
  - **Activation**: decoding alignment critique, RSA limitations, CKA blindness, encoding manifold, neural population topology, Gromov-Wasserstein neural, 2605.05907

### Clockless Asynchronous Neuromorphic Computing on FPGA
- [[clockless-asynchronous-neuromorphic-computing]] - Scalable B-SNN architecture using autonomous Boolean spiking neurons on commercial FPGAs with nanosecond spike dynamics (arXiv: 2605.16114)
  - 核心要点 1: 196-neuron B-SNN with Dale's principle (20% inhibitory), receptive neurons (CM=2), local connectivity
  - 核心要点 2: Synaptic weights embedded in circuit topology (not registers) via delayed-path replication
  - 核心要点 3: Liquid State Machine on SHD audio classification; 2.07 ns spikes vs 10ns measurement clock
  - 核心要点 4: UDP/Ethernet real-time spike streaming; 10-100x lower power than clocked designs
  - **Activation**: clockless FPGA neuromorphic, Boolean spiking neuron, autonomous circuit SNN, asynchronous neuromorphic, 2605.16114

### Ensemble Engineering for Quantum Measurements
- [[ensemble-engineering-quantum-measurements]] - General framework mitigating destructive cancellation in NISQ quantum measurements by encoding sampling distribution in prepared quantum state (arXiv: 2605.03729)
  - 核心要点 1: Destructive cancellation is structural mismatch between ensemble weights and operator sign structure, not just statistical
  - 核心要点 2: Grover-type amplitude amplification + oracle-free shallow circuit for near-term hardware
  - 核心要点 3: Demonstrated on IBM quantum processors up to 20 qubits
  - **Activation**: quantum ensemble engineering, destructive cancellation, NISQ measurement, amplitude amplification, 2605.03729

### QBalance: Multi-Objective Quantum Workflow Optimization
- [[qbalance-workflow-optimization]] - Reproducible multi-objective strategy selection for quantum compilation, noise suppression, and error mitigation (arXiv: 2605.02966)
  - 核心要点 1: Formulates quantum compilation as weighted multi-objective optimization over circuits, backends, and policies
  - 核心要点 2: Non-dominated Pareto selection, Bayesian candidate ordering, survival-product error proxy
  - **Activation**: QBalance, quantum workflow optimization, quantum compilation strategy, NISQ compilation, 2605.02966

### Adaptive Bistable Qubit Control
- [[adaptive-bistable-qubit-control]] - 1-bit feedback protocol for operating bistable qubits with TLS defects using FPGA real-time control at ~136 kHz (arXiv: 2605.03187)
  - 核心要点 1: Estimates qubit bistable frequency from single single-shot measurement — reaches Shannon information limit
  - 核心要点 2: 77% error reduction in gate fidelity suppression, validated on superconducting qubit
  - 核心要点 3: Scalable to large qubit arrays via parallel FPGA feedback channels
  - **Activation**: bistable qubit, TLS defect mitigation, 1-bit feedback, adaptive qubit control, FPGA quantum control, 2605.03187

### Embedded Quantum Machine Learning in Embedded Systems
- [[embedded-quantum-machine-learning]] - Feasibility analysis and hybrid architectures for embedding quantum ML workloads in resource-constrained embedded systems (arXiv: 2603.12540)
  - 核心要点 1: Explores hybrid classical-quantum architectures for embedded deployment
  - 核心要点 2: Addresses resource constraints in edge quantum computing scenarios
  - **Activation**: embedded quantum ML, edge quantum computing, hybrid quantum-classical embedded, 2603.12540

### Diagonal Adaptive Non-local Observables on Quantum Neural Networks
- [[diagonal-adaptive-non-local-observables]] - Reduces k-local observable complexity from O(4^k) to O(2^k) while preserving full ANO expressivity via diagonal canonical representation (arXiv: 2605.15410)
  - 核心要点 1: 对角可观测量是 ANO 空间在酉相似变换下的规范代表元，保持等效表达能力
  - 核心要点 2: 将 k 局部可观测量复杂度从 O(4^k) 降至 O(2^k)，显著降低经典优化成本
  - **Activation**: diagonal ANO, quantum observable optimization, VQA function space, adaptive quantum measurements, 2605.15410

## 2026-05-19 - Neuroscience Research (Cron Job)

### Hippocampal-Entorhinal Inspired World Model
- [[hippocampal-entorhinal-world-model]] - Brain-inspired hierarchical world model for structure abstraction and generalization from video (arXiv: 2605.15733)
  - Simultaneously infers latent transitions and constructs predictive visual world model
  - HPC-MEC coupling dissociates relational structures (MEC) from integrated episodic scenes (HPC)
  - **Activation**: hippocampal-entorhinal model, world model, structure abstraction, HPC-MEC coupling

### Cortical Microcircuit Information Flux Optimization
- [[cortical-microcircuits-information-flux-optimization]] - Simulation-based reverse engineering of cortical microcircuit optimization for information flux (arXiv: 2605.14680)
  - Reverse engineering study of whether cortical microcircuits are optimized for information transmission
  - Simulation-based approach comparing natural vs. optimized circuit configurations
  - **Activation**: cortical microcircuit, information flux, reverse engineering, circuit optimization

### Clockless FPGA Neuromorphic Scaling
- [[clockless-fpga-neuromorphic-scaling]] - Scalable neuromorphic architecture via autonomous time-continuous spiking dynamics in clockless digital circuits on commercial FPGAs, eliminating need for custom ASIC (arXiv: 2605.16114)
  - Boolean spiking neurons with E/I synaptic weights emerge autonomous spiking dynamics
  - Competitive accuracy on audio classification (84.5% SHD) with 2 orders of magnitude lower power
  - Cascadable multi-FPGA architecture enables scalable deployment
  - **Activation**: clockless FPGA neuromorphic, scalable asynchronous spiking, Boolean neuron FPGA, energy-efficient neuromorphic hardware

### The Complex Brain Hypothesis: Resolving the Entropy-Content Conundrum in Minimal Phenomenal Experience
- [[complex-brain-hypothesis-resolving-entropy-content]] - Theoretical framework resolving the conflict between Entropic Brain Hypothesis and content-free conscious states via topological complexity metrics (arXiv: 2605.16146)
  - Minimal Phenomenal Experiences (MPEs) challenge EBH: high entropy but no content
  - Proposes topological complexity metrics to separate phenomenological content from entropy
  - Bridges computational neuroscience with consciousness studies
  - **Activation**: complex brain hypothesis, minimal phenomenal experience, entropic brain, consciousness entropy


### Implicit Behavioral Decoding from Spike Forecasts
- [[implicit-behavioral-decoding-spike-forecasts]] - Joint neural population forecasting and behavioral decoding from spiking activity (arXiv: 2605.12999)
  - Single model handles both spike forecasting and behavioral readout implicitly
  - Eliminates separate forecast → decode pipelines for closed-loop BCI systems
  - **Activation**: spike forecast behavioral, implicit behavioral decoding, closed-loop BCI

## 2026-05-19 - Deep Learning Research (Cron Job)
## 2026-05-19 - Neuroscience Research (Cron Job)

### Implicit Behavioral Decoding from Next-Step Spike Forecasts at Population Scale
- [[spike-forecast-behavioral]] - Joint neural population forecasting and behavioral decoding from spiking activity (arXiv: 2605.12999)
  - Single model handles both spike forecasting and behavioral readout implicitly
  - Eliminates separate forecast → decode pipelines for closed-loop BCI systems
  - **Activation**: spike forecast behavioral, implicit behavioral decoding, closed-loop BCI, population neural forecasting

### Mechanistic Interpretability of EEG Foundation Models via Sparse Autoencoders
- [[eeg-sae-interpretability]] - Extracting clinically interpretable features from EEG foundation model activations using SAE decomposition (arXiv: 2605.13930)
  - First application of SAE-based interpretability to EEG foundation models
  - Discovers human-interpretable features: sleep spindles, epileptiform patterns, frequency-band encodings
  - **Activation**: EEG foundation model interpretability, sparse autoencoder EEG, mechanistic interpretability, clinical EEG auditing

### STS: Efficient Sparse Attention with Speculative Token Sparsity
- [[speculative-sparse-attention-sts]] - Training-free sparse attention using draft model attention scores to construct dynamic token-and-head-wise sparsity masks for LLM inference, achieving 2.67x speedup at ~90% sparsity (arXiv: 2605.15508)
  - Cross-model attention correlation: small draft model predicts important tokens for large target model
  - Integrates with speculative decoding — no extra inference cost
  - Maintains accuracy at high sparsity levels unlike static pruning
  - **Activation**: speculative sparse attention, draft model sparsity, attention mask training-free, long context LLM inference

### DualKV: Shared-Prompt Flash Attention for Efficient RL Training
- [[dualkv-shared-prompt-flash-attention]] - FlashAttention kernel variant eliminating shared-prompt replication during GRPO/DAPO training, achieving 1.63-3.82x speedup and raising MFU from 36% to 76% (arXiv: 2605.15422)
  - Causal masking makes prompt representations invariant across N rollout sequences
  - Fused CUDA kernels process prompt once across all rollouts
  - Data pipeline repacks N(P+R) tokens into P+NR per micro-batch
  - **Activation**: dualkv, shared prompt flash attention, GRPO training speedup, RL kernel optimization

### Probabilistic Chunk Masking for Efficient VLA RL
- [[vla-probabilistic-chunk-masking]] - Drop-in GRPO modification using success-failure action variance to allocate gradient computation to informative trajectory chunks, achieving 2.38x speedup while backpropagating through <20% of chunks (arXiv: 2605.16154)
  - Success-failure action variance proxies per-phase gradient variance
  - No reward model or learned critic required
  - 60% lower peak activation memory
  - **Activation**: probabilistic chunk masking, efficient GRPO, VLA RL, gradient variance

### Self-evolving Agent Experience (DrugSAGE)
- [[self-evolving-agent-experience]] - Framework for LLM agents that accumulates cross-task memory of verified skills, statistical evidence, and error-fix patterns, enabling zero-test-time search on new tasks (arXiv: 2605.15461)
  - Memory components: verified skills, statistical evidence, error-fix records
  - Direct transfer of working solutions without search
  - Outperforms baselines by 10-30% in zero-search regime
  - **Activation**: self-evolving agent, cross-task memory, experience reuse, agent skill accumulation

### Compound LLM Agent Design in Adversarial POMDPs
- [[compound-llm-agent-design]] - Systematic study of 12 agent configurations revealing deliberation cascade pattern and that programmatic state abstraction delivers highest returns per token (arXiv: 2605.16205)
  - Deliberation cascade: distributing deliberation across hierarchy degrades performance up to 3.4x
  - Hierarchy without deliberation achieves best absolute performance
  - Context engineering more cost-effective than deliberation
  - **Activation**: compound agent design, deliberation cascade, hierarchical agents, RPTS, adversarial POMDP

### Stepwise Reasoning with External Subgraph Generation
- [[stepwise-reasoning-subgraph]] - Stepwise reasoning framework building query-specific subgraphs from external KBs to ground intermediate reasoning steps, improving LLM accuracy and factual reliability (arXiv: 2605.16117)
  - Three-stage: subgraph construction → progressive reasoning → trajectory combination
  - Reduces hallucination by grounding in structured knowledge
  - **Activation**: stepwise reasoning, subgraph generation, knowledge grounding, external KB reasoning

### Federated Learning of SNNs under Heterogeneous Temporal Resolutions
- [[federated-snn-heterogeneous-temporal]] - Federated learning framework for SNNs addressing temporal resolution mismatch across edge devices, enabling local-resolution training with global model compatibility (arXiv: 2605.15355)
  - Naive FedAvg fails when clients have different sampling rates
  - Adaptation methods recover accuracy lost to temporal mismatch
  - Applies to SNNs and broader class of stateful-neuron networks
  - **Activation**: federated SNN, temporal resolution mismatch, heterogeneous edge FL

### RecMem: Recurrence-based Memory Consolidation for LLM Agents
- [[recurrence-memory-consolidation]] - Memory consolidation storing interactions in subconscious layer, only invoking LLM when sustained recurrence detected, reducing token cost by up to 87% while exceeding accuracy (arXiv: 2605.16045)
  - Lightweight embedding for subconscious storage, LLM only for recurring patterns
  - Semantic refinement recovers fine-grained facts omitted by compression
  - Drop-in replacement for consolidation step in existing memory systems
  - **Activation**: recmem, recurrence memory consolidation, lazy memory, agent memory efficiency

### Cortical Microcircuit Information Flux Optimization
- [[cortical-microcircuits-information-flux-optimization]] - Simulation-based reverse engineering of whether cortical microcircuits are optimized for information flux (arXiv: 2605.14680)
  - Investigates if biological cortical circuits operate near information transmission optima
  - Uses mutual information between successive network states as optimization objective
  - **Activation**: cortical microcircuit optimization, information flux neural networks, reverse engineering brain circuits
## 2026-05-18 - Neuroscience + Quantum Mechanics (Cron Job - 23:00)

### Diagonal Adaptive Non-local Observables on Quantum Neural Networks
- [[diagonal-ano-quantum-observables]] - Diagonal adaptive non-local observables for VQAs: reduces O(n²) to O(n) parameters while retaining full expressivity via canonical diagonal representation (arXiv: 2605.15410)
  - Diagonal observables are canonical representatives of ANO space modulo unitary similarity
  - Equivalent expressivity to full Hermitian ANO with far fewer parameters
  - Faster convergence and easier classical optimization
  - Hardware-friendly: diagonal measurements native on most platforms
  - **Activation**: diagonal ANO, adaptive non-local observables, VQA parameter efficiency, quantum measurement design, observable adaptivity

### Extreme Quantum Cognition Machines
- [[extreme-quantum-cognition]] - Quantum learning architecture for deliberative decision making with dynamical attention, noise-tolerant to contradictory data (arXiv: 2603.05430)
  - Fixed quantum dynamics as nonlinear feature map, learning only in linear readout
  - Input-dependent Hamiltonian attention modulates quantum evolution
  - No barren plateaus, inherent noise regularization
  - **Activation**: extreme quantum cognition, EQCM, quantum reservoir computing, quantum extreme learning, dynamical attention quantum

### Deep Boltzmann Quantum States for Spin Glasses
- [[deep-boltzmann-quantum-states]] - Neural quantum states + Boltzmann machine for frustrated quantum many-body systems (arXiv: 2605.15899)
  - Captures complex entanglement in classical/quantum spin glasses
  - Boltzmann architecture naturally models competing interactions and frustration
  - Unified framework for classical and quantum disordered systems
  - **Activation**: cortical microcircuit optimization, information flux neural networks, reverse engineering brain circuits

### Letting the Neural Code Speak: Automated Neuron Characterization via Language
- [[neural-code-language-interpretability]] - Closed-loop framework translating neuron activations into semantic descriptions using neural digital twins (arXiv: 2605.12485)
  - 核心要点 1: Natural language replaces mathematical models for characterizing neurons in higher visual areas
  - 核心要点 2: Closed-loop: generate captions → semantic hypothesis → synthesize images → verify in silico
  - 核心要点 3: V4 neurons achieve 96.1% activation / 97.6% suppression with language-generated images vs ~10% random
  - **Activation**: neural code speak, automated neuron characterization, language-based neural description, neural digital twin, 2605.12485

## 2026-05-18 - Neuroscience + Quantum Mechanics (Cron Job - 23:00)

### Scalable neuromorphic computing from autonomous spiking dynamics in a clockless reconfigurable chip
- [[clockless-neuromorphic-snn]] - Clockless asynchronous Boolean spiking neural networks on FPGA achieving nanosecond-scale spike dynamics with 100x energy efficiency over clocked implementations (arXiv: 2605.16114)
  - Boolean spiking neurons with configurable excitatory/inhibitory weights and propagation delays
  - Quasi-analog dynamics emerge from autonomous time-continuous evolution of digital logic (no global clock)
  - 84.5% accuracy on SHD audio classification, competitive with analog neuromorphic state-of-the-art
  - 2 orders of magnitude lower power than digital FPGA SNN implementations
  - **Activation**: clockless neuromorphic, boolean spiking neuron, async spiking network, liquid state machine FPGA, energy-efficient SNN hardware

### Structure Abstraction and Generalization in a Hippocampal-Entorhinal Inspired World Model
- [[hpc-mec-world-model]] - Brain-inspired hierarchical world model using HPC-MEC coupling for structure abstraction and zero-shot generalization from real-world video (arXiv: 2605.15733)
  - MEC encodes abstract relational structures via CANN; HPC binds content-specific episodic information
  - Inverse model learns latent transitions from observation-only videos (no action labels needed)
  - Demonstrates zero-shot transfer: extract transitions from human videos, apply to novel objects/scenes
  - 84 FPS inference on A100; trained on SSv2 (220K videos), evaluated on OmniObject3D and robotics benchmarks
  - **Activation**: hpc-mec world model, hippocampal entorhinal model, structure abstraction, cognitive map AI, grid cell model, latent transition reuse

     1|## 2026-05-18 - Polariton BEC Quantum Neuromorphic (Cron Job - 22:01)
     2|
     3|### Polariton BECs: Theory and Concepts
     4|- [[polariton-bec-quantum-neuromorphic]] - Polariton Bose-Einstein condensate theory for room-temperature quantum neuromorphic computing, driven-dissipative dynamics, and optical neural networks (arXiv: 2605.16256)
     5|  - Polaritons are WISI (Weakly-Interacting, Strongly-Interfering) particles combining light interference with exciton interactions
     6|