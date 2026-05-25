## 2026-05-26 - Neuroscience + Quantum (Cron Job)

### Quantum Genetic Optimization for Negative Selection Algorithms in Anomaly Detection
- [[quantum-genetic-negative-selection]] - Quantum genetic algorithm for anomaly detection via negative selection optimization (arXiv: 2605.22527)
  - QGA replaces classical GA in negative selection detector generation
  - Quantum superposition encodes exponential candidate space in O(n) qubits
  - Rotation gate amplitude adjustment controls exploration vs convergence
  - **Activation**: quantum genetic algorithm, negative selection, anomaly detection, artificial immune system, QGA, QGNSA
## 2026-05-25 - Neuroscience + Quantum Mechanics (Cron Job - Monday)

### ORCHID: Kuramoto-Based Quantum Consensus Protocol
- [[orchid-kuramoto-quantum-consensus]] - Bio-inspired distributed consensus mapping neuroscientific binding problem onto Byzantine fault tolerance using Kuramoto synchronization + Quantum Secret Sharing (arXiv: 2605.12126)
  - Maps neural oscillator synchrony → consensus nodes, gamma-band binding → consensus trigger
  - Kuramoto order parameter r(t) > θ_b triggers binding/consensus event
  - QSS fidelity phase transition at coherence c* ≈ 0.82
  - r_max = 0.988 at K=3.0, 100% consensus at 0-40% Byzantine faults, O(n·k) message complexity
  - **Activation**: ORCHID consensus, Kuramoto brain synchronization, quantum secret sharing consensus, neuro-inspired blockchain, binding problem distributed systems, gamma-band binding

### SPATE: Spiking-Phase Adaptive Temporal Encoding for Quantum Machine Learning
- [[spiking-phase-quantum-encoding]] - Spike-driven temporal encoding converting real-valued features into LIF spike trains and mapping spike statistics to quantum rotations, with encoding-centric evaluation protocol (arXiv: 2604.11022)
  - Converts tabular features into LIF spike trains, maps spike statistics to quantum rotation gates
  - Augmented with temporal qubits through controlled phase operations for temporal structure
  - Encoding-centric evaluation: CKTA, Fisher separability, silhouette score, TVpair collapse
  - Achieves CKTA 0.966 vs 0.632 (angle encoding) on Blobs; accuracy 0.826/AUC 0.978 on Wine
  - **Activation**: SPATE, spike encoding, quantum machine learning, temporal encoding, LIF neuron, spiking neural network, QML encoding, phase encoding, quantum feature representation, spike-to-phase, IJCNN

### SQDR-CNN: Spiking-Quantum Data Re-upload Convolutional Neural Network
- [[sqdr-cnn-spiking-quantum]] - Parameter-efficient hybrid architecture enabling joint training of convolutional SNNs and quantum circuits with surrogate gradient and quantum data-reupload, using only 0.5% of parameters (arXiv: 2512.03895)
  - End-to-end joint training without pretrained SNN encoders or dataset subsetting
  - Surrogate gradient technique enables backprop through non-differentiable spiking activity
  - Quantum data-reupload: single-qubit circuit with N re-uploads ≈ N-qubit expressivity
  - Achieves 86% of SOTA SNN accuracy with 0.5% of parameters; robust under noisy simulation
  - **Activation**: SQNN, surrogate gradient, quantum data-reupload, hybrid quantum-classical, SNN backpropagation, convolutional SNN, parameter-efficient, SQDR-CNN

### BrainDyn: A Sheaf Neural ODE for Generative Brain Dynamics
- [[braindyn-sheaf-neural-ode]] - Sheaf neural ODE framework for generative brain dynamics modeling across fMRI, EEG, and simulated spiking data (arXiv: 2605.19324)
  - Combines cellular sheaf theory (learnable edge-specific restriction maps) with neural ODEs for continuous-time brain dynamics
  - LSTM-encoded temporal history → sheaf Laplacian message passing → neural ODE continuous-time evolution
  - Evaluated on PNC fMRI (1188 subjects), TUSZ EEG, and NEST spiking simulations
  - Outperforms CNN-LSTM, BIOT (transformer), EvolveGCN, ODEBRAIN across modalities
  - Sheaf representation supports in silico perturbation prediction (virtual testbeds for stimulation studies)
  - **Activation**: braindyn, sheaf neural ODE, brain dynamics forecasting, neural ODE brain, sheaf Laplacian, generative brain model, in silico perturbation, continuous-time neural dynamics

### Selective Alignment Knowledge Distillation for Spiking Neural Networks
- [[sealkd-snn-knowledge-distillation]] - Not All Timesteps Matter Equally: selective temporal alignment KD for SNNs that provides corrective guidance to erroneous timesteps while preserving useful temporal dynamics (arXiv: 2605.14252)
  - Selective class-level alignment: equalizes competing logits only at erroneous timesteps
  - Selective temporal alignment: confidence-weighted and inter-timestep similarity reweighting
  - Preserves SNN's own learned temporal dynamics at correctly-predicted timesteps
  - Consistent improvements across static image (CIFAR, ImageNet) and neuromorphic event-based (DVS-CIFAR10, DVS-Gesture) datasets
  - **Activation**: sealkd, selective alignment knowledge distillation, SNN knowledge distillation, temporal alignment SNN, spiking neural network distillation

### Canonical Functionalism: Defining Functional Structure without Observer-Relative Semantic Maps
- [[canonical-functionalism-consciousness]] - Mathematical refinement of computational functionalism identifying consciousness-relevant organization with canonical functional structure (minimal state-transition from counterfactual roles), avoiding observer-relativity problems (arXiv: 2605.21506)
  - Canonical functional structure: merge states with identical future behavior under all possible continuations
  - Provides precise mathematical object over which functionalist theories of consciousness should be formulated
  - Reframes lookup-table/simulation/unfolding objections as structural criterion questions
  - **Activation**: canonical functionalism, consciousness theory, computational functionalism, consciousness invariants, functional structure consciousness

## 2026-05-25 - Systems Engineering Research (Cron Job - Monday)

### LiveR: Fine-Grained Elasticity via Live Reconfiguration for Model Training
- [[liver-live-reconfiguration]] - Live reconfiguration runtime for elastic LLM training replacing stop-and-restart with live, bounded-memory handoff between mixed-parallel worlds (arXiv: 2605.22014)
  - Core: Parallel Worlds + Mock Process Groups + Streaming Resharding + Atomic Switch
  - Key: Background Shadow World preparation while Active World continues training
  - Result: 14×-23× speedup, ~7s downtime (vs 150s+), ~99% training efficiency under volatility
  - **Activation**: live reconfiguration, elastic training, LLM training, mixed parallelism, spot instances, distributed systems

### Leggett-Garg Tests in Neural Dynamics: Probing Non-Diffusive Stochastic Structure in Single Neurons
- [[leggett-garg-neural-dynamics]] - LGI testing methodology for distinguishing diffusive vs persistent stochastic neural dynamics, revealing memory and non-Markovian structure (arXiv: 2605.12126)
  - Leggett-Garg inequality as temporal probe of neural dynamics (analogue of Bell-type constraints)
  - Kac-type finite-velocity processes → Telegrapher's equation → Dirac-like envelope equations
  - LGI violation indicates persistent stochastic transport, not microscopic quantum coherence
  - Applicable to single-neuron electrophysiology and cable-equation model validation
  - **Activation**: leggett-garg, neural dynamics, non-diffusive, persistent stochastic, Kac process, Telegrapher equation, temporal correlation, non-Markovian

### Quantum Photonic Neural Networks in Time
- [[quantum-photonic-neural-networks]] - Time-bin-encoded QPNN architecture with depth-independent hardware scaling (arXiv: 2603.23798)
  - Same number of photonic elements regardless of network size or depth
  - Time-bin encoding replaces spatial encoding for resource-efficient quantum neural networks
  - Nonlinear photonic circuits trained to process quantum information
  - Loss and phase noise modeling for realistic hardware imperfections
  - **Activation**: quantum photonic neural network, QPNN, time-bin encoding, photonic quantum computing, nonlinear photonic circuit, brain-inspired quantum

### Quantum circuit design via dynamic Pauli constraints
- [[dynamic-pauli-constraints-quantum]] - Novel quantum computation model using Pauli observable constraints for gate specification with built-in tomography; universal for BQP with O(D^2 N log N) overhead (arXiv: 2605.22744)
  - Gates specified as constraints on Pauli observables with built-in pairwise/k-local state tomography per layer
  - Proven equivalent to coupling-graph-restricted circuits (BQP universal) with polynomial overhead
  - Natural interface for NISQ-era quantum software via physically observable quantities
  - **Activation**: pauli constraints, quantum circuit design, NISQ quantum software, observable-based gates, quantum state tomography, coupling graph, BQP equivalence


### Learning Sequence Timing and Control of Replay Speed in Networks of Spiking Neurons
- [[sequence-timing-snn-replay]] - Spiking neural network methodology for encoding temporal sequences through sequential activation of element-specific neuronal populations with controllable replay speed via STDP (arXiv: 2605.22523)
  - Element-specific population encoding: each sequence element represented by dedicated neuronal population
  - STDP-based temporal learning: spike-timing-dependent plasticity learns temporal relationships
  - Replay speed control: network reproduces sequences at different speeds while preserving temporal structure
  - Wide timescale encoding from milliseconds to seconds
  - **Activation**: sequence timing, replay speed, spiking neurons, STDP, temporal encoding, sequence learning, temporal abstraction

### Temporal Coding for Sensorimotor Object Inference (Spiking Thousand Brains)
- [[temporal-coding-thousand-brains-spiking]] - Replaces dense vectors with rank-order spike packets for sensorimotor inference in Thousand Brains architecture using STDP for directional encoding (arXiv: 2605.22206)
  - Rank-order spike packets replace dense vector representations for energy-efficient encoding
  - STDP learns traversal direction between sensory states for active object inference
  - Adaptive lambda parameter adjusts per object geometry
  - Applicable to robotic tactile exploration, haptic perception, and edge AI
  - **Activation**: temporal coding, thousand brains, sensorimotor inference, spike packets, STDP, rank-order coding, active sensing

## 2026-05-25 - Neuroscience (Cron Job)

### Guiding Multi-Objective Genetic Programming with Description Length Improves Symbolic Regression Solutions
- [[description-length-genetic-programming]] - DL/FBF model selection for GPSR preventing structural bloat (arXiv: 2605.22374)
  - Description Length with Fisher-information encoding outperforms AIC/BIC for compact expression selection
  - Use DL/FBF as post-selection on Pareto front, NOT as direct fitness (causes premature convergence)
  - **Activation**: description length genetic programming, DL model selection symbolic regression, 描述长度遗传编程

### A Multi-Scale Information Geometry Reveals the Structure of Mutual Information in Neural Populations
- [[multi-scale-info-geometry-neural]] - Novel framework connecting information geometry and mutual information through a unique Riemannian geometry emerging from coarse-graining of neural population responses (arXiv: 2605.06304)
  - Multi-scale Fisher information metric extends classic framework from fine to coarse stimulus distinctions
  - Geometry exactly related to mutual information: expanded directions = well-encoded, contracted = poorly encoded
  - Metric tensor estimated via diffusion models, enabling practical application to large populations
  - Eigenvectors reveal interpretable stimulus features contributing most to information transmission
  - Applied to visual cortical responses to natural images, yielding robust, modelling-choice-independent features
  - **Activation**: information geometry, neural population code, Fisher information metric, representational geometry, multi-scale encoding, mutual information neural, diffusion models neuroscience

### Efficient Coding Under Constraint Drives Neural Systems Towards Criticality and Sloppiness
- [[efficient-coding-criticality-sloppiness]] - Normative theory showing efficient coding under resource constraints drives neural systems towards critical states with power-law avalanches and sloppiness (arXiv: 2605.22598)
  - Efficient coding under finite neurons and energy budgets places system at critical point of phase transition
  - Criticality → power-law neural avalanches (scale-free dynamics)
  - Criticality → sloppiness (parameter redundancy, robustness to variation)
  - Unifies normative theory (efficient coding) with mechanistic observations (criticality)
  - Bridges efficient coding, criticality, and sloppiness in a single framework
  - **Activation**: efficient coding, criticality, neural avalanche, power law, sloppiness, self-organized criticality, brain criticality, normative theory

### Geometric Phase Transition Enables Extreme Hippocampal Memory Capacity
- [[geometric-phase-transition-hippocampal-memory]] - Hippocampal spatial memory capacity emerges from a discrete stiffening of population geometry, transitioning from disorganized to crystalline collective coding (arXiv: 2605.17199)
  - Geometric phase transition in place cell ensembles: disorganized → crystalline arrangement
  - Exponential memory capacity in crystalline phase vs. linear in disorganized phase
  - First-order transition: once started, geometry locks in rapidly (discrete stiffening)
  - Order parameter: spatial correlation length of place field arrangement
  - Explains extreme hippocampal capacity (10^5+ distinct spatial representations)
  - **Activation**: geometric phase transition, hippocampus, population geometry, spatial memory, place cells, grid cells, memory capacity, collective coding, crystalline neural representation

## 2026-05-24 - Information Science + Quantum Mechanics (Cron Job - Sunday)

### A Formal Basis for Quantum Cryptographic Exposure Measurement under HNDL Threat
- [[hndl-exposure-measurement]] - Multiplicative factorization framework for Harvest-Now-Decrypt-Later threat exposure, proving additive scoring frameworks are structurally inadequate (arXiv: 2605.22569)
  - HNDL compromise probability factorizes into temporal hazard × crypto vulnerability × operational exposure / saturation denominator
  - Marginal sensitivity is endogenous to vulnerability-exposure plane position, not fixed global constant
  - Defense-attack intensity ratio governs saturation — diminishing returns beyond certain defense level
  - **Activation**: HNDL, harvest now decrypt later, quantum cryptographic exposure, post-quantum risk, multiplicative scoring, defense-attack ratio

### Precision and Privacy in Distributed Quantum Sensing: A QFI Duality
- [[quantum-fisher-privacy-duality]] - QFI duality framework showing Heisenberg-limited precision forces zero QFI for all other directions, achieving parameter privacy by construction (arXiv: 2605.20765)
  - Fundamental tradeoff: F_Q(w^T θ) + F_Q(v^T θ) ≤ N for orthogonal sensing directions
  - GHZ states saturate bound for N≥2, maximizing precision and privacy simultaneously
  - Privacy emerges from quantum measurement limits, not encryption protocols
  - **Activation**: quantum Fisher information, QFI duality, distributed quantum sensing privacy, GHZ state sensing, Heisenberg limit privacy

### Stream randomness extraction against quantum side information
- [[stream-randomness-extraction-quantum]] - Converts block-wise quantum randomness extractors to on-the-fly stream implementations via offline pre-computed XOR masks, preserving security against quantum side information (arXiv: 2605.09556)
  - Eliminates QRNG latency and buffering overhead while maintaining identical security guarantees
  - Supports Toeplitz, circulant, and modified Toeplitz matrix constructions
  - Offline pre-computation shifts computational burden away from real-time processing
  - **Activation**: quantum randomness extraction, QRNG stream processing, Toeplitz hashing, quantum side information, real-time QRNG

## 2026-05-24 - Neuroscience Research (Cron Job)

### Functional Whole-Brain Models: A New Framework for Unifying Brain Structure and Cognitive Function
- [[functional-whole-brain-models-fwbm]] - Unified fWBM paradigm bridging bottom-up whole-brain modeling and top-down neuroconnectionism for biologically realistic, task-performing brain models (arXiv: 2605.18118)
  - Four minimal criteria: structural grounding, continuous-time dynamics, functional competence, mappable observables
  - Three-pillar roadmap across short/mid/long-term horizons for model integration
  - Scientific/clinical opportunities: connectome-constrained learning, biophysics-informed deep learning, oscillatory network computation
  - **Activation**: functional whole-brain model, fWBM, whole-brain modeling, neuroconnectionism, connectome-constrained neural network, biophysics-informed deep learning, brain structure-function integration

### Stimulus Symmetries Can Confound Representational Similarity Analyses (arXiv:2605.21324)
- [[stimulus-symmetries-rsm-confound]] - Demonstrates that stimulus symmetries in neural network inputs cause functionally-equivalent representations to produce different, drifting RSM geometries, challenging RSM-based analyses of neural codes (arXiv: 2605.21324)
  - Symmetries in network inputs create gauge freedom — functionally-equivalent codes yield different RSMs
  - SGD/regularization produces sparse drifting codes, causing RSMs to drift over training
  - Effects persist in image-trained autoencoders with latent symmetry
  - Challenges assumption that functionally-equivalent representations are related by a simple rotation
  - **Activation**: representational similarity analysis, RSM gauge dependence, stimulus symmetry, RSA confound, neural code comparison, drifting representations, representational geometry

### Beyond Prediction Accuracy: Target-Space Recovery Profiles for Evaluating Model-Brain Alignment (arXiv:2605.20127)
- [[target-space-recovery-profiles-brain-alignment]] - Framework that identifies which reproducible brain response dimensions are recovered by model predictions, going beyond scalar prediction accuracy for evaluating brain-model alignment (arXiv: 2605.20127)
  - Uses repeated fMRI measurements to identify reproducible response dimensions across trial splits
  - Early-to-intermediate visual cortex contains a low-dimensional set of reproducible dimensions
  - Pretrained and randomly initialized models can match prediction accuracy but show distinct recovery profiles
  - Brain-to-brain comparisons provide a diagnostic human reference for evaluating model alignment
  - **Activation**: brain alignment, model evaluation, fMRI encoding models, prediction accuracy, response dimensions, representational similarity, Natural Scenes Dataset, target-space recovery

### Self-Supervised Local Learning Rules Learn the Hidden Hierarchical Structure of High-Dimensional Data
- [[self-supervised-local-learning-hierarchy]] - Biologically plausible local self-supervised learning rules match backprop data efficiency on hierarchical data, while DFA methods fail due to missing input-specific masking (arXiv: 2605.18557)
  - Local self-supervised contrastive/non-contrastive loss solves RHM tasks as well as BP
  - DFA and variants fail on hierarchical tasks due to ignoring input-specific masking
  - Layerwise loss functions enable local learning rules compatible with cortical plasticity
  - **Activation**: local learning rules, biologically plausible learning, self-supervised representation learning, Random Hierarchy Model, Direct Feedback Alignment failure, local plasticity

### MINE: Mechanistically Interpretable Neural Encoding Reveals Fine-Grained Functional Selectivity in Human Visual Cortex (arXiv:2605.16468)
- [[mine-neural-encoding-mechanistic-interpretability]] - Applies mechanistic interpretability tools (feature attribution, counterfactual editing) to voxel-level neural encoding models, enabling causal validation and discovery of fine-grained functional organization within category-selective brain regions (arXiv: 2605.16468)
  - Language-aligned image representations predict each voxel's response and produce semantically interpretable descriptions of driving features
  - Per-image features generalize into stable per-voxel functional profiles validated through generative image synthesis
  - Counterfactual insertion/removal of predicted features shifts voxel activation causally, confirmed via per-voxel profile-guided editing
  - Reveals unique voxel-level functional selectivity within well-studied regions (FFA, PPA) beyond known categorical preferences
  - **Activation**: mechanistically interpretable neural encoding, MINE framework, voxel-level mechanistic interpretability, counterfactual brain encoding, fMRI feature attribution, functional selectivity profiling, language-aligned encoding model, fine-grained visual cortex organization

### Are Cortical Microcircuits Optimized for Information Flux? — A Simulation-Based Reverse Engineering Study (arXiv:2605.14680)
- [[cortical-microcircuit-information-flux-optimization]] - Simulation-based reverse engineering of cortical layer 5 microcircuits showing that the embedding network enhances information flux via effective bias shifts and Recurrence Resonance, with implications for reservoir computing design (arXiv: 2605.14680)
  - Embedding network amplifies mutual information between successive network states in core population beyond isolated core performance
  - Two-component mechanism: effective DC biases push core neurons to high-entropy regime; stochastic fluctuations via Recurrence Resonance prevent attractor trapping
  - Recurrence Resonance identified as a novel dynamical phenomenon where optimal recurrent noise maximizes information flux
  - Self-organized local bias optimization can exceed biologically embedded configurations
  - **Activation**: cortical information flux, microcircuit reverse engineering, Recurrence Resonance, layer 5 microcolumn, embedding network dynamics, entropy-driven neural dynamics, reservoir computing design, core-embedding architecture

## 2026-05-24 - Information Science + Quantum Mechanics (Cron Job - Sunday Evening)

### Vector Policy Optimization: Training for Diversity Improves Test-Time Search
- [[vector-policy-optimization]] - VPO methodology trains LLMs with multi-objective reward vectors to maintain response diversity for inference-time search procedures (arXiv: 2605.22817)
  - Scalar reward optimization leads to low-entropy response distributions that fail at test-time search
  - Vector rewards + diversity bonus term enables coverage of solution space across varied task-specific rewards
  - Integrates with GRPO: vector-valued advantages + diversity bonus in policy gradient update
  - **Activation**: vector policy optimization, response diversity training, test-time compute scaling, multi-objective RL fine-tuning, AlphaEvolve search, inference-time diversity

### Tokenisation via Convex Relaxations
- [[convex-tokenization]] - ConvexTok formulates tokenizer construction as a linear program instead of greedy BPE/Unigram, achieving globally optimal vocabulary selection (arXiv: 2605.22821)
  - LP formulation with coverage + vocabulary size constraints provides theoretical optimality bounds
  - Consistently improves bits-per-byte (BpB) over greedy tokenization methods
  - Flexible constraint system allows domain-specific tokenization optimization
  - **Activation**: convex tokenization, tokenizer optimization, BPE alternative, linear program tokenizer, bits-per-byte improvement, globally optimal vocabulary

### Dominant vibronic relaxation channels in a europium-based molecular qubit
- [[molecular-qubit-vibronic-engineering]] - Parameter-free DFT+TD-DFT+Redfield framework for predicting T1 relaxation times and identifying dominant decoherence pathways in molecular spin qubits (arXiv: 2605.21520)
  - Reproduces experimental T1_long=41.39s within factor 1.4 (calculated 55.88s at 4.2K) for Eu molecular qubit
  - Identifies dpphen rocking mode (332 cm-1) as dominant vibronic coupling channel
  - EFG derivative analysis identifies nitrate-rocking mode (181 cm-1) as primary nuclear spin environment modulator
  - Ligand rigidification and substitution strategies suggested for coherence optimization
  - **Activation**: molecular qubit T1 relaxation, vibronic coupling qubit, DFT qubit decoherence, Redfield theory spin relaxation, europium spin qubit, ligand design quantum coherence


## 2026-05-24 - Information Science + Quantum Mechanics (Cron Job)

### Exact Hidden Paths in Noisy High Dimensional Path Spaces (arXiv: 2605.22477)
- [[exact-hidden-path-recovery]] - Mathematical framework for exact recovery of noisy hidden paths in high-dimensional discrete path spaces using path integral interference (arXiv: 2605.22477)
  - Core point 1: Path integral phase interference cancels noise while amplifying signal
  - Core point 2: Enables exact recovery where classical SNR methods fail
  - **Activation**: hidden path recovery, path integral cryptography, noise resilient signal recovery, high dimensional path analysis

### Information Extraction of Nested Complex Structure of Quantum Cascade Lasers via Large Language Models (arXiv: 2605.09927)
- [[llm-information-extraction-quantum-devices]] - LLM-based automated extraction of nested device parameters from quantum/scientific literature (arXiv: 2605.09927)
  - Core point 1: Structured LLM prompts extract multi-level nested data (structure, materials, performance)
  - Core point 2: Cross-validation across paper sections resolves conflicts
  - **Activation**: LLM information extraction, nested structure extraction, quantum device parameters, literature mining

### A Toolbox to Understand the Physics of Quantum Data Management (arXiv: 2605.14719)
- [[quantum-data-management-toolbox]] - Framework connecting quantum device physics with data management abstractions for quantum database design (arXiv: 2605.14719)
  - Core point 1: No-cloning and measurement collapse fundamentally change database operations
  - Core point 2: Hybrid classical-quantum approach is practical path forward
  - **Activation**: quantum data management, quantum database, quantum storage, quantum indexing, hybrid database

## 2026-05-24 - Information Science + Quantum Mechanics (Cron Job - Sunday)

### Precision and Privacy in Distributed Quantum Sensing: A Quantum Fisher Information Duality
- [[quantum-fisher-information-duality]] - QFI duality methodology establishing fundamental precision-privacy trade-offs in distributed quantum sensor networks (arXiv: 2605.20765)
  - F_Q(w^T θ) + F_Q(v^T θ) ≤ N for any N-qubit probe state with orthogonal sensing directions
  - Heisenberg-limited precision forces zero QFI for all other independent directions — precision IS privacy
  - GHZ states (N≥2) and equatorial states (N=2) achieve the tight bound
  - **Activation**: quantum fisher information duality, precision privacy quantum sensing, QFI duality, distributed quantum sensing privacy

### Quantum Entanglement Halves the Oblivious Update Bandwidth
- [[quantum-entanglement-distributed-storage]] - Quantum entanglement-assisted distributed storage achieving 2x bandwidth reduction for oblivious updates using CSS codes (arXiv: 2605.19248)
  - Classical lower bound α bits → quantum α/2 bits-equivalent with shared entanglement
  - CSS codes achieve the bound via superdense coding: one qudit per helper carries 2× classical capacity
  - Matching converse proves α/2 is fundamental quantum limit
  - **Activation**: quantum entanglement distributed storage, oblivious update bandwidth, CSS code storage, superdense coding bandwidth

### Overcoming Barren Plateaus in Variational Quantum Circuits using a Two-Step Least Squares Approach
- [[two-step-vqc-optimization]] - Two-stage convex initialization + nonconvex refinement framework for reliable VQA training (arXiv: 2601.18060)
  - Convex initialization shapes Hilmaton landscape into smooth, low-energy basin with detectable gradients
  - Riemannian manifold optimization reduces condition number dependence of quantum least squares matrix
  - Applied to BB84 QKD cryptanalysis for optimal cloning strategies
  - **Activation**: two-step VQC optimization, convex initialization quantum circuits, barren plateau mitigation two-stage, Riemannian manifold quantum optimization

## 2026-05-24 - Information Science (Cron Job)
### Quantum Genetic Optimization for Negative Selection Algorithms in Anomaly Detection
- [[quantum-genetic-negative-selection]] - QGNSA methodology integrating quantum genetic algorithms into negative selection for enhanced anomaly detection using quantum superposition and amplitude adjustment (arXiv: 2605.22527)
  - Q-bit chromosome encoding enables superposition search over multiple detector candidates simultaneously
  - Probabilistic amplitude adjustment via quantum rotation gates optimizes detector generation efficiency
  - Significantly outperforms classical and evolutionary NSAs in detection rate and false positive rate
  - **Activation**: QGNSA, quantum genetic negative selection, quantum anomaly detection, immune detector, quantum superposition search

### Reinforcement Learning for Ion Shuttling on Trapped-Ion Quantum Computers
- [[rl-ion-shuttling]] - RL-based ion shuttling optimization for modular trapped-ion quantum chips with distinct functional zones (arXiv: 2605.22463)
  - First use of reinforcement learning for ion transport optimization on trapped-ion quantum computers
  - High-dimensional routing problem where classical optimal solutions become intractable
  - RL policy learned for real-time shuttling decisions with state fidelity preservation
  - **Activation**: ion shuttling, trapped-ion RL, quantum ion transport, ion routing optimization

### Quantum Circuit Design via Dynamic Pauli Constraints
- [[dynamic-pauli-constraints-qc]] - Software-oriented quantum circuit model using Pauli observable constraints with k-local tomography, equivalent to BQP with O(D²N log N) overhead (arXiv: 2605.22744)
  - Gates specified by Pauli observable constraints instead of direct unitary operations
  - Each disjoint layer accompanied by pairwise or k-local quantum state tomography
  - Proven universal for BQP with polynomial overhead on near-term hardware
  - **Activation**: dynamic Pauli constraints, quantum circuit tomography, Pauli observable, coupling graph circuit

### Semidefinite Programming for Optimal Quantum Cloning
- [[sdpc-quantum-cloning]] - Computational framework reformulating quantum cloning as SDP over CPTP maps via Choi-Jamiolkowski isomorphism with primal-dual optimality certification (arXiv: 2605.21274)
  - Choi matrix representation enables optimization over quantum channels as positive matrix optimization
  - Strong duality provides numerical certification of global optimality without analytical proofs
  - Kraus operators automatically extracted from optimal Choi matrix via spectral decomposition
  - **Activation**: quantum cloning SDP, Choi-Jamiolkowski cloning, CPTP map optimization, Kraus extraction

### Q-PhotoNAS: Hybrid Quantum Neural Architecture Search on Photonic Devices
- [[q-photonas-quantum-nas]] - Automated NAS framework for hybrid photonic quantum-classical models combining genetic algorithm search with learnable phase encoding (arXiv: 2605.22097)
  - Replaces manually tuned architectures with automated search over preprocessing, encoding, and circuit structure
  - Genetic algorithm-based search with hardware compatibility constraints
  - Learnable phase encoding jointly optimized with quantum circuit parameters
  - **Activation**: Q-PhotoNAS, photonic quantum NAS, quantum neural architecture search, learnable phase encoding

### Equivalence of Privacy and Stability with Generalization Guarantees in Quantum Learning
- [[quantum-learning-privacy-generalization]] - Unified information-theoretic framework connecting privacy, stability, and generalization in quantum learning (arXiv: 2602.01177)
  - Epsilon-quantum differentially private learning algorithms are provably stable
  - Quantum mutual information bounds expected generalization error
  - **Activation**: quantum privacy generalization, quantum learning stability, quantum differential privacy

### Fully Homomorphic Encryption on Llama 3 model for privacy preserving LLM inference
- [[fhe-privacy-preserving-llm]] - FHE patterns for privacy-preserving LLM inference with lattice-based cryptography (arXiv: 2604.12168)
  - BFV/BGV/CKKS scheme selection patterns for ML workloads
  - SIMD batching and bootstrapping strategies for deep networks
  - **Activation**: fully homomorphic encryption, FHE LLM inference, privacy preserving ML

### Rethinking quantum smooth entropies: Tight one-shot analysis of quantum privacy amplification
- [[quantum-privacy-amplification]] - One-shot quantum privacy amplification using redefined smooth entropies (arXiv: 2603.04493)
  - Smooth min/max entropy bounds for finite-key security guarantees
  - Composable security framework for QKD protocols
  - **Activation**: quantum privacy amplification, quantum smooth entropies, one-shot quantum security

     1|## 2026-05-25 - Information Science + Quantum Physics (Monday Cron Job)
     2|
     3|### Sudden death of entanglement, rebirth of magic (arXiv:2605.22603)
     4|- [[magic-entanglement-complementarity]] - Local Markovian noise irreversibly destroys entanglement but can 'rebirth' magic (non-stabilizerness) through dissipation; stabilizer membership is not preserved by local channels, enabling noise-induced magic-state distillation via parity-syndrome extraction (arXiv: 2605.22603)
     5|  - Core: Magic-entanglement complementarity γₑ + γ₊ = 1 under amplitude damping on n-qubit GHZ states
     6|  - Key insight: Dissipation pushes states both into and out of stabilizer polytope; reborn magic in separable states can be concentrated for distillation
     7|  - Result: Magic-generators vs magic-insulators classification of pure stabilizer states under local dissipation
     8|  - **Activation**: magic entanglement complementarity, stabilizer polytope, magic state distillation, amplitude damping GHZ, quantum resource theory, non-stabilizerness, noise-induced magic
     9|
    10|### How many systems can be dephased before the quantum switch becomes causally definite? (arXiv:2605.22807)
    11|- [[causal-nonseparability-dephasing]] - Quantum processes with indefinite causal order retain causal nonseparability if any non-future system remains undephased, but become causally separable when all systems or only the future system is kept (arXiv: 2605.22807)
    12|  - Core: Sharp threshold — single non-future system preservation suffices for causal nonseparability in both bipartite and multipartite QC-QCs
    13|  - Key insight: Future system alone is insufficient; past and intermediate systems are essential for maintaining indefinite causal order
    14|  - Result: Minimal resource preservation strategy for quantum switch protocols under dephasing noise
    15|  - **Activation**: causal nonseparability, quantum switch, indefinite causal order, dephasing robustness, QC-QC, quantum causality, process matrix
    16|
    17|## 2026-05-24 - Neuroscience Research (Sunday Cron Job)
    18|
    19|### Learning sequence timing and control of replay speed in networks of spiking neurons (arXiv:2605.22523)
    20|- [[learning-sequence-timing-snn]] - Extends spiking Temporal Memory (sTM) model to encode precise element-specific timing via sequential population activation and control replay speed via oscillatory background inputs, linking replay speed to EEG/LFP oscillatory activity (arXiv: 2605.22523)
    21|  - Core: Element-specific duration via sequential activation of neuronal populations + oscillatory clock signal (θ/γ rhythms) for speed modulation
    22|  - Key insight: Elapsed time encoded by unique sparse spatiotemporal patterns; replay speed correlates with brain state oscillations
    23|  - Result: Biologically plausible basis for encoding and replaying complex temporal sequences across wide timescales
    24|  - **Activation**: spiking temporal memory, sTM, sequence timing SNN, replay speed control, oscillatory clock, hippocampal replay, synfire chain timing, sparse spatiotemporal encoding, theta gamma replay
    25|
    26|### Untrained CNNs Match Backpropagation at V1: A Systematic RSA Comparison of Four Learning Rules Against Human fMRI (arXiv:2604.16875)
    27|- [[untrained-cnns-match-backpropagation-v1-rsa]] - Systematic RSA comparison showing untrained random-weights CNN (rho=0.076) exceeds backprop (rho=0.034) at V1/V2 (p<0.001); STDP achieves highest V1 alignment among trained rules (arXiv: 2604.16875)
    28|  - Core: Four learning rules (BP, FA, PC, STDP) + untrained baseline compared against THINGS-fMRI (720 stimuli, 3 subjects)
    29|  - Key insight: Early visual alignment is architecture-driven, not learning-rule-driven — CNN structure itself encodes V1-matching priors
    30|  - Result: All rules converge at IT; learning rules differentiate only at intermediate areas
    31|  - **Activation**: untrained CNN V1 alignment, RSA brain comparison, architecture-driven brain alignment, STDP V1, THINGS-fMRI, random weights V1 match
    32|
    33|### Riemannian geometry meets fMRI: the advantages of modeling correlation manifolds and eigenvector subspaces (arXiv:2605.22334)
    34|- [[riemannian-fmri-correlation-manifolds]] - Scalable geometric framework for fMRI functional connectivity using the Off-log metric (closed-form correlation manifold analysis) and Grassmannian subspace discrimination for eigenvector comparisons (arXiv: 2605.22334)
    35|  - Core: Off-log diffeomorphism maps correlation matrices to symmetric hollow matrices enabling closed-form distances, Fréchet means, and linear models without manifold optimization
    36|  - Key insight: Permutation-invariant log-Euclidean geometry on the elliptope solves the scalability problem of existing Riemannian methods for high-dimensional neuroimaging
    37|  - Grassmannian method: Principal-angle distances between Laplacian eigenvectors resolve sign/basis ambiguities, consistently outperforming Euclidean baselines
    38|  - Results: Validated on Parkinson's (22 HC vs 22 PD), psychosis (26 HC vs 26 NAP), and 3 aging fMRI datasets (cam-CAN, HCPAging, NKI; ~1309 subjects total)
    39|  - **Activation**: Riemannian geometry fMRI, Off-log metric, correlation manifold, Grassmannian discriminant, functional connectivity manifold, elliptope geometry, brain age prediction, brain network topology
    32|
    33|## 2026-05-24 - Information Science + Quantum Computing Research (Sunday Cron Job)
    34|
    35|### A Graph-Based Forensic Framework for Inferring Hardware Noise of Cloud Quantum Backend (arXiv:2512.14541)
    36|- [[quantum-forensic-gnn]] - GNN-based forensic framework that predicts per-qubit and per-qubit-link error rates of unseen cloud quantum backends using only topology and transpilation features, achieving ~22% mismatch for single-qubit and ~18% for qubit-link errors (arXiv: 2512.14541)
    37|  - Core: GNN regressors trained on IBM 27-qubit devices predict error rates from user-visible features (topology + transpilation output)
    38|  - Key insight: Cloud quantum providers may redirect jobs to more error-prone regions while presenting stale calibration data — forensic inference from user-visible artifacts closes this transparency gap
    39|  - Result: Strong ranking agreement (high Spearman correlation); identifies weak links and high-noise qubits robustly under temporal noise drift
    40|  - **Activation**: quantum forensic, GNN quantum noise, cloud quantum security, IBM quantum verification, hardware noise inference, quantum backend audit, quantum error rate prediction
    41|
    42|### Experimental demonstration of scalable quantum cryptographic conferencing (arXiv:2512.06661)
    43|- [[scalable-quantum-crypto-conferencing]] - Experimental QCC eliminating coincidence detection requirement for GHZ-state measurement, achieving 331.5 km range (66.3 dB loss) with 5.4 bit/s secure key rates, surpassing multi-user repeaterless bound (arXiv: 2512.06661)
    44|  - Core: Construct GHZ state by correlating detection events within coherence time instead of requiring simultaneous coincidence detection
    45|  - Key innovation: Three-party phase compensation + precise temporal/polarization alignment in time-bin-phase encoding framework enables scalable multi-user quantum communication
    46|  - Result: 3.3x range extension over previous 100 km limit; establishes new regime for metropolitan quantum networks
    47|  - **Activation**: quantum cryptographic conferencing, QCC, GHZ state measurement, multi-user quantum network, time-bin encoding, phase compensation, metropolitan quantum network
    48|
    49|### Equivalence of Privacy and Stability with Generalization Guarantees in Quantum Learning (arXiv:2602.01177)
    50|- [[quantum-learning-privacy-generalization]] - Unified framework establishing ε-quantum differential privacy → stability → generalization chain, with quantum mutual information bounds and Information-Theoretic Admissibility for dishonest algorithms (arXiv: 2602.01177)
    51|  - Core: E[gen_error] ≤ √(2·I(S;h)/n) via quantum mutual information; ε-QDP implies stability
    52|  - Key insight: Privacy-stability-generalization equivalence in quantum learning, extending Esposito et al. (2021) to quantum domain
    53|  - Result: ITA framework characterizes privacy limits for algorithms oblivious to dataset instances
    54|  - **Activation**: quantum learning privacy, quantum generalization bounds, quantum differential privacy stability, information-theoretic admissibility, quantum mutual information learning
    55|
    56|### How Entanglement Reshapes the Geometry of Quantum Differential Privacy (arXiv:2601.19126)
    57|- [[quantum-differential-privacy-geometry]] - Framework analyzing how quantum entanglement deforms the geometry of quantum differential privacy, characterizing entanglement-modified privacy-utility tradeoffs (arXiv: 2601.19126)
    58|  - Core: Privacy region deformation ε_entangled = ε_separable · g(E(ρ_AB)) dependent on entanglement structure
    59|  - Key insight: Entanglement can both enhance (masking via correlations) and degrade (side channels via Bell measurements) privacy
    60|  - Result: Privacy-utility Pareto frontier shaped by entanglement type and degree
    61|  - **Activation**: quantum differential privacy geometry, entanglement privacy tradeoff, quantum DP entanglement, quantum privacy geometry
    62|
    63|### Toward Covert Quantum Computing (arXiv:2605.14325) - Enhanced
    64|- [[covert-quantum-computing-crosstalk]] - Enhanced skill for computational covertness in multi-tenant quantum computers with discrete isoperimetric analysis and long-range crosstalk side channel characterization (arXiv: 2605.14325)
    65|  - Core: Border qubit scaling O(√n) for detection info; quantum-strategy framework for adversarial analysis
    66|  - Key finding: Long-range crosstalk via drive/control line leakage creates additional detection channel beyond border qubits
    67|  - Result: Verified on IQM Emerald (54-qubit) and IBM ibm_fez (156-qubit Heron 2)
    68|  - **Activation**: covert quantum computing, quantum crosstalk analysis, multi-tenant quantum security, quantum side channel, border qubit scaling
    69|
    70|## 2026-05-24 - Neuroscience Research (Cron Job - Saturday)
    71|
    72|### A simple model of co-emergence of grid and place fields (arXiv:2605.21356)
    73|- [[grid-place-cell-co-emergence]] - First unified recurrent network model implementing Dale's Law (every neuron is either excitatory or inhibitory) trained via masked next-observation prediction to co-emerge both grid and place cells from a single architecture (arXiv: 2605.21356)
    74|  - Core: Single RNN with Dale's Law → self-supervised masked prediction → simultaneous emergence of grid-like and place-like spatial representations
    75|  - Key insight: Grid and place cells co-emerge through reciprocal connectivity — one does not cause the other, resolving the chicken-and-egg problem
    76|  - Result: Biologically realistic spatial representations without explicit spatial labels or architectural specialization for each cell type
    77|  - Comparison: Unifies previously separate accounts of grid and place cell origin within a single computational framework
    78|  - **Activation**: grid cell co-emergence, place cell model, Dale's Law neural networks, entorhinal-hippocampal circuit, spatial navigation self-supervised learning, grid cell emergence from prediction, MEC-HPC unified model
    79|
    80|### MIRAGE: Robust Multi-Modal fMRI-to-Image for Mental Imagery Reconstruction (arXiv:2605.17198)
    81|- [[mirage-fmri-mental-imagery-decoding]] - Robust multi-modal architecture for translating fMRI-to-image models from seen visual decoding to mental imagery reconstruction; shows SOTA seen-image performance ≠ SOTA mental imagery performance and proposes domain-aligned multi-modal fusion (arXiv: 2605.17198)
    82|  - Core: Multi-modal backbone integration + multi-loss training (reconstruction, perceptual, domain alignment, adversarial) → shared latent space for seen and imagined brain activity
    83|  - Key insight: Modern vision decoders that excel at seen image reconstruction can fail at mental imagery — different neural representations require different decoding strategies
    84|  - Result: MIRAGE outperforms single-backbone baselines on both seen and imagery conditions (up to 15% relative improvement on imagery)
    85|  - Evaluation: NSD-Imagery dataset with comprehensive metrics (pixcorr, SSIM, LPIPS, CLIP score) across seen and imagined conditions
    86|  - **Activation**: mental imagery fMRI decoding, seen-to-imagery transfer brain decoding, MIRAGE architecture, fMRI visual reconstruction, brain decoding domain generalization, NSD-Imagery dataset
    87|
    88|## 2026-05-24 - Quantum Computing Research (Cron Job)
    89|
    90|### Sparse Mamba Decoder for Surface Code Quantum Error Correction (arXiv:2605.17156)
    91|- [[sparse-mamba-qec-decoder]] - Defect-centric neural decoder using Mamba state-space backbone processes only k active detection events (O(k) complexity) instead of full O(d²R) syndrome array; 95-467x faster than Tesseract near-MLD with up to 49% reduced logical error rate (arXiv: 2605.17156)
    92|  - Core: 13-dimensional feature embedding per detection event → Mamba selective scan → near-constant 24-57μs latency across d=3-9
    93|  - Key insight: at p~0.1%, <5% syndrome entries are active — existing dense decoders waste computation on empty syndrome
    94|  - Result: MWPM logical error rate reduced up to 49% at d≤5 under SI1000 noise; 232-463x faster than Belief Matching
    95|  - Sycamore experimental dataset: ensemble matches/surpasses dense Mamba decoder baseline
    96|  - 7.5-16M parameters on commodity NVIDIA GPUs, no specialized accelerators
    97|  - **Activation**: sparse mamba decoder, SMD, QEC neural decoder, surface code Mamba, defect-centric decoding, sparse syndrome processing, quantum error correction state space model
    98|
    99|## 2026-05-24 - Systems Engineering Research (Cron Job)
   100|
   101|### AdaPTwin: Adaptive Multi-Fidelity Predictive Digital Twin
   102|- [[adaptwin-digital-twin]] - Adaptive multi-fidelity predictive digital twin for proactive RRM in vehicular networks (arXiv: 2605.21897)
   103|  - Core: Cloud-edge hierarchical architecture with dynamic fidelity adjustment
   104|  - Key: Transformer trajectory prediction + continual/transfer learning + NVIDIA Sionna ray tracing
   105|  - Result: 90% sum-rate gain, 80% outage reduction
   106|  - **Activation**: digital twin, adaptive fidelity, RRM, vehicular networks
   107|
   108|### Contractual Skills: A GovernSpec Design Framework for Enterprise AI Agents
   109|- [[contractual-skills-governspec]] - Governance layer design for AI agent skills as inspectable task contracts (arXiv: 2605.22634)
   110|  - Core: Contractual skill structure with goal/input/permissions/output/verification fields
   111|  - Key: Governance boundary between skills, GovernSpec YAML, MCP, guardrails, tracing
   112|  - Result: Outperforms no-skill baselines, reduces high-risk tool attempts
   113|  - **Activation**: AI agent governance, contractual skills, GovernSpec
   114|
   115|## 2026-05-24 - Neuroscience Research (Cron Job - Sunday)
   116|
   117|### Temporal Coding as a Substrate for Sensorimotor Object Inference: A Spiking Reinterpretation of Thousand Brains Architecture (arXiv:2605.22206)
   118|- [[temporal-coding-thousand-brains-spiking]] - Replaces dense floating-point vectors with rank-order spike packets for sensorimotor inference in the Monty/Thousand Brains framework; uses STDP to encode traversal direction and adaptive lambda for geometric complexity (arXiv: 2605.22206)
   119|  - Perfect discrimination on objects with identical features in different arrangements (dense accumulation at chance)
   120|  - 30-50 percentage point noise robustness advantage maintained across all levels
   121|  - Adaptive lambda converges to distinct values reflecting object geometric complexity
   122|  - Three testable predictions: temporal order discrimination, STDP direction encoding, lambda-geometry correspondence
   123|  - **Activation**: thousand brains theory, temporal coding, rank-order coding, sensorimotor inference, STDP direction encoding, Monty framework spiking
   124|
   125|### Joint Sparse Coding and Temporal Dynamics Support Context Reconfiguration (arXiv:2605.10178)
   126|- [[sparse-temporal-context-reconfiguration]] - Identifies sparsity in context-dependent representations and temporal dynamics as mechanisms for preserving prior knowledge during context transitions; SNNs show improved lifelong learning retention (arXiv: 2605.10178)
   127|  - Sparsity reduces cross-context interference in mouse mPFC and computational networks
   128|  - Temporal dynamics further separate context representations across time
   129|  - SNNs naturally exhibit both properties, retaining information better without auxiliary heuristics
   130|  - Energy-efficient architectural principle for stable adaptation
   131|  - **Activation**: context reconfiguration, lifelong learning SNN, catastrophic forgetting spiking, sparse coding context, temporal dynamics neural, mPFC context switching
   132|
   133|## 2026-05-24 - Information Science + Quantum Computing (Cron Job - Sunday)
   134|
   135|### 4D and 5D Layer Codes through Color Routing (arXiv:2605.18961)
   136|- [[layer-codes-color-routing]] - CSS code construction generalizing Layer codes to d dimensions using color routing, saturates BPT bounds exactly (arXiv: 2605.18961)
   137|  - Core: From D-dim qLDPC with barrier Δ → (D+1)-dim Layer code with parameters [[n^{(D+1)/D}, k, d^{(D+1)/D}]] and barrier Δ·n^{1/D}
   138|  - Key: Color routing resolves check layer structure and line defects that blocked previous generalization attempts
   139|  - Result: Exact BPT bound saturation in d>3 dimensions; modular architecture for network patches
   140|  - **Activation**: layer codes, color routing, qLDPC codes, CSS codes, BPT bounds, quantum error correction, dimensional generalization
   141|
   142|### Operationalising Post Quantum TLS Automated Configuration Profiling and Hybrid PQC Deployment (arXiv:2605.17955)
   143|- [[pqc-tls-deployment]] - Automated PQC TLS deployment methodology with configuration parsing and hybrid ML-KEM key exchange for enterprise infrastructure (arXiv: 2605.17955)
   144|  - Configuration parsing across Nginx, Apache, API gateways for unified cryptographic inventory
   145|  - Hybrid ML-KEM + X25519 deployment with zero application-layer changes
   146|  - Migration strategy: discovery → pilot → production with performance monitoring
   147|  - **Activation**: post-quantum cryptography deployment, PQC TLS migration, ML-KEM hybrid, cryptographic inventory, crypto-agility
   148|
   149|### Optimization of Secret Key Rate for BB84 under Collective Rotation Noise (arXiv:2605.21140)
   150|- [[qkd-noise-optimization]] - QKD noise engineering strategy finding optimal noise range where eavesdropper information is minimized while SKR degradation remains small (arXiv: 2605.21140)
   151|  - Non-zero noise sweet spot: collective rotation noise can act as natural defense
   152|  - QBER monitoring with ~11% threshold for BB84 asymptotic security
   153|  - Intercept-resend and coherent attack scenario analysis under noise
   154|  - **Activation**: quantum key distribution, BB84 protocol, QKD noise optimization, secret key rate, quantum bit error rate, collective rotation noise
   155|
   156|### Q-SpiRL: Quantum Spiking Reinforcement Learning for Adaptive Robot Navigation (arXiv:2605.20801)
   157|- [[q-spirl-quantum-spiking-rl]] - Combines spike-based temporal processing with variational quantum feature transformation for obstacle-aware robot navigation, achieving up to 99% success rate with deterministic inference on IBM quantum hardware (arXiv: 2605.20801)
   158|  - Five agent families evaluated under unified pipeline: Q-learning, MLP, SNN, QMLP, QSNN
   159|  - QSNN outperforms all baselines in success rate + trajectory efficiency + motion smoothness
   160|  - Spike encoding captures dynamic obstacle patterns; quantum layer provides high-dimensional feature transformation
   161|  - Verified deployment on real IBM quantum hardware under NISQ constraints
   162|  - **Activation**: quantum reinforcement learning, quantum spiking, QSNN, spike-based RL, quantum robot navigation, quantum SNN policy, variational quantum RL
   163|
   164|## 2026-05-25 - Neuroscience Research (Cron Job - Sunday)
   165|
   166|### Subject-Specific Analysis of Self-Initiated Attention Shifts from EEG (arXiv:2605.18251)
   167|- [[self-initiated-attention-shifts-eeg]] - Machine learning + SHAP analysis of EEG reveals subject-specific discriminative information in preparatory activity for distinguishing self-initiated vs externally-cued attention shifts; higher-frequency bands and frontal regions are most informative (arXiv: 2605.18251)
   168|  - Controlled comparison of self-initiated vs externally instructed shifts under identical visual stimulation
   169|  - SHAP-based feature attribution across frequency bands and regions of interest
   170|  - Reliable within-subject classification: beta/gamma bands and frontal regions drive decisions
   171|  - **Activation**: self-initiated attention, EEG attention decoding, SHAP EEG, frontal EEG, voluntary attention, subject-specific EEG
   172|
   173|### BCI-sift: An Automated Feature Selection Toolbox for BCI (arXiv:2605.19646)
   174|- [[bci-sift-feature-selection]] - Automated scikit-learn-compatible feature selection toolbox for BCI applications operating across electrode, temporal, and frequency dimensions; validated on HD ECoG speech decoding (arXiv: 2605.19646)
   175|  - Multi-dimensional selection: electrodes, time points, frequency bands simultaneously
   176|  - Validated on 8 participants HD ECoG speech decoding (12-word task)
   177|  - High-frequency gamma band identified as most informative feature dimension
   178|  - **Activation**: BCI feature selection, ECoG decoding, neural feature tuning, automated BCI ML pipeline, BCI-sift
   179|
   180|### Brain Alignment of Reasoning and Action Representations from VLMs and LAMs (arXiv:2605.19352)
   181|- [[vlm-lam-brain-alignment]] - fMRI study showing VLMs and LAMs outperform RL baselines in brain encoding during gameplay; prompt gains scale with cortical hierarchy; VLM is prompt-symmetric while LAM is prompt-asymmetric in representational organization (arXiv: 2605.19352)
   182|  - Both VLMs and LAMs significantly outperform RL baselines in voxel-wise encoding
   183|  - Prompt-driven gains largest in frontal-parietal and motor-planning regions
   184|  - VLM: 12.5% unique action vs 13.6% unique reasoning; LAM: 27% unique action vs -5% unique reasoning
   185|  - **Activation**: VLM brain alignment, LAM fMRI encoding, interactive gameplay fMRI, cortical hierarchy encoding, action model brain comparison
   186|
   187|### Conserved Kinematic Representations Enable Zero-Shot Decoding in Handwriting BCIs (arXiv:2605.19048)
   188|- [[conserved-kinematic-zero-shot-bci]] - Zero-shot handwriting BCI decoding using conserved kinematic primitives; achieves 64% hits@3 on unseen letters, enabling open-vocabulary iBCI for logographic languages (arXiv: 2605.19048)
   189|  - Neural representations of kinematic strokes are conserved across different character contexts
   190|  - 64% hits@3 retrieval on unseen letters → strong evidence for compositional motor control
   191|  - Enables scaling BCIs to Chinese, Japanese, and other logographic languages
   192|  - **Activation**: zero-shot BCI, handwriting decoding, kinematic representations, conserved neural dynamics, iBCI handwriting, logographic BCI, motor cortex primitives
   193|
   194|## 2026-05-25 - Information Science + Quantum (Cron Job - Sunday)
   195|
   196|### A Formal Basis for Quantum Cryptographic Exposure Measurement under HNDL Threat
   197|- [[quantum-crypto-exposure-measurement]] - Structurally-grounded HNDL exposure assessment using temporal hazard, vulnerability-exposure multiplicative terms, and saturation dynamics (arXiv: 2605.22569)
   198|  - Core: HNDL compromise probability = h(t) × V_crypto × O_exposure / (1 + λ × D/A)
   199|  - Key: Additive scoring cannot capture vulnerability-exposure interaction; marginal sensitivity is endogenous
   200|  - Result: Framework works under partial observability; prioritises migration based on position in vulnerability-exposure plane
   201|  - **Activation**: HNDL, harvest now decrypt later, quantum cryptographic exposure, post-quantum risk assessment, quantum security measurement
   202|
   203|### Precision and Privacy in Distributed Quantum Sensing: A Quantum Fisher Information Duality
   204|- [[quantum-fisher-information-duality]] - QFI duality establishing precision-privacy tradeoff: F_Q(w·θ) + F_Q(v·θ) ≤ N for orthogonal directions in distributed quantum sensing (arXiv: 2605.20765)
   205|  - Core: Heisenberg-limited precision for one direction forces zero QFI for all orthogonal directions
   206|  - Key: GHZ states (N≥2) and equatorial states (N=2) achieve tight bound
   207|  - Result: Privacy is automatic — physics enforces the guarantee, no additional cryptography needed
   208|  - **Activation**: quantum Fisher information, QFI duality, distributed quantum sensing, quantum privacy, parameter privacy
   209|
   210|## 2026-05-24 - Information Science + Quantum (Cron Job - Sunday)
   211|
   212|
   213|### How many systems can be dephased before the quantum switch becomes causally definite? (arXiv:2605.22807)
   214|- [[quantum-causal-nonseparability]] - Analyzes how much dephasing noise a quantum switch can tolerate before its indefinite causal order becomes causally separable; quantifies robustness of quantum advantages from indefinite causal structure (arXiv: 2605.22807)
   215|  - Causal nonseparability provides computational advantages over fixed causal order circuits
   216|  - Quantum switch becomes causally separable after dephasing threshold of constituent systems
   217|  - Process matrix formalism and causal witness operators for nonseparability detection
   218|  - Phase transition boundary between causally nonseparable and separable regimes
   219|  - **Activation**: causal nonseparability, quantum switch, indefinite causal order, dephasing quantum processes, causally nonseparable, process matrix formalism
   220|
   221|### Tokenisation via Convex Relaxations (arXiv:2605.22821)
   222|- [[convex-tokenisation]] - Reformulates NLP tokeniser construction as a linear program solved with convex optimisation (ConvexTok), yielding globally optimal vocabulary instead of greedy BPE/Unigram approaches (arXiv: 2605.22821)
   223|  - BPE and Unigram make locally optimal decisions without considering full vocabulary
   224|  - ConvexTok formulates tokenisation as LP with vocabulary size constraints
   225|  - Global optimization produces better encoding efficiency than greedy methods
   226|  - Scalable to large corpora via convex relaxation of binary constraints
   227|  - **Activation**: convex tokenisation, ConvexTok, tokeniser construction, linear program NLP, BPE alternative, convex optimization tokenisation
   228|
   229|### Vector Policy Optimization: Training for Diversity Improves Test-Time Search (arXiv:2605.22817)
   230|- [[vector-policy-optimization]] - Proposes Vector Policy Optimization (VPO) that trains LLMs to produce diverse, high-entropy response distributions, significantly improving test-time search performance over scalar-reward RLHF (arXiv: 2605.22817)
   231|  - Standard RLHF produces low-entropy responses that hurt inference-scaling search
   232|  - VPO optimizes multiple reward functions simultaneously with entropy regularization
   233|  - Diverse response coverage improves AlphaEvolve-style test-time search
   234|  - Tradeoff between response quality and diversity tunable via beta parameter
   235|  - **Activation**: vector policy optimization, VPO training, test-time search, LLM diversity, inference scaling, response diversity, AlphaEvolve
   236|### Quantum Purity Amplification for Arbitrary Eigenstates and Multiple Outputs (arXiv:2605.21570)
   237|- [[quantum-purity-amplification]] - General solution for coherently transforming n copies of a mixed state into m high-fidelity copies of any chosen eigenstate (arXiv: 2605.21570)
   238|  - Handles arbitrary target eigenstates, not just dominant one
   239|  - Supports arbitrary local dimension d (qubits, qudits, continuous-variable)
   240|  - Quantifiable fidelity trade-off bounds between input copies and output quality
   241|  - **Activation**: quantum purity amplification, QPA, state purification, mixed to pure state, quantum state amplification, eigenstate purification
   242|
   243|### A Formal Basis for Quantum Cryptographic Exposure Measurement under HNDL Threat (arXiv:2605.22569)
   244|- [[quantum-crypto-exposure-measurement]] - Formal mathematical framework for quantifying information leakage in quantum cryptographic systems under HNDL threat model (arXiv: 2605.22569)
   245|  - HNDL model captures hard non-delegatable leakage that cannot be prevented cryptographically
   246|  - Provides quantitative exposure metrics: IE, SM, RS
   247|  - Formal bounds on adversary knowledge using quantum information theory
   248|  - **Activation**: quantum cryptographic exposure, HNDL threat model, quantum security measurement, information leakage quantum, quantum threat modeling
   249|
   250|### A Sharp Interaction-Degree Threshold for Simulating QAOA (arXiv:2605.22758)
   251|- [[qaoa-interaction-threshold]] - Identifies sharp computational phase transition where classical simulation of QAOA becomes intractable (arXiv: 2605.22758)
   252|  - Below threshold k_c: efficient tensor network classical simulation
   253|  - Above threshold: exponential complexity, quantum advantage emerges
   254|  - Interaction degree analysis provides quantum-classical boundary metric
   255|  - **Activation**: QAOA simulation threshold, interaction degree QAOA, quantum advantage boundary, QAOA complexity analysis, classical simulation QAOA, computational phase transition
   256|
   257|## 2026-05-24 - Information Science + Quantum (Cron Job)
   258|
   259|### Precision and Privacy in Distributed Quantum Sensing: A Quantum Fisher Information Duality (arXiv:2605.20765)
   260|- [[quantum-fisher-information-privacy]] - QFI duality framework establishing precision-privacy tradeoffs in distributed quantum sensing; Heisenberg-limited precision for target parameter forces zero QFI for all other independent directions (arXiv: 2605.20765)
   261|  - QFI duality theorem: F_Q(w) + F_Q(v) <= N for any N-qubit probe state with local phase encoding
   262|  - Privacy guarantee: attaining F_Q = N for sensing target renders all alternative estimations impossible
   263|  - GHZ states achieve optimal tradeoff for N >= 2; equatorial states for N = 2
   264|  - **Activation**: quantum Fisher information, QFI duality, quantum sensing privacy, distributed quantum sensors, parameter privacy, Heisenberg limit, Fisher information duality
   265|
   266|### Quantum Homomorphic Encryption: Towards Practical and Private Computation on Untrusted Quantum Hardware (arXiv:2604.19256)
   267|- [[quantum-homomorphic-encryption-qhe]] - QOTPH framework enabling computation on encrypted quantum states via Quantum One-Time Pad with information-theoretic security (arXiv: 2604.19256)
   268|  - Homomorphic gate decompositions for Clifford+T circuits with systematic key update rules
   269|  - Non-interactive evaluation for Clifford gates; T gates require additional protocol
   270|  - Validated on simulated environments and real IBM quantum processors under circuit-level noise
   271|  - **Activation**: quantum homomorphic encryption, QHE, QOTP, encrypted quantum computation, privacy-preserving quantum, delegated quantum computing, blind quantum computation
   272|
   273|### Quantum-Resistant Networks: A Review of Primitives, Protocols and Best Practices (arXiv:2605.04129)
   274|- [[quantum-resistant-networks]] - First comprehensive systematization of post-quantum network architectures across cryptographic foundations, key distribution, and deployment (arXiv: 2605.04129)
   275|  - Unified taxonomy: symmetric-only, PQ-PKI, hybrid, information-theoretic multi-path foundations
   276|  - Key distribution architectures: centralized, hierarchical, replicated, threshold, MPC-backed, serverless
   277|  - Analyzes trade-offs under harvest-now-decrypt-later and partial infrastructure compromise threats
   278|  - **Activation**: post-quantum cryptography, PQC networks, quantum resistant, network security architecture, key distribution, cryptographic agility
   279|
   280|### Q-PhotoNAS: Hybrid Quantum Neural Architecture Search Framework on Photonic Devices (arXiv:2605.22097)
   281|- [[q-photonas-hybrid-arch-search]] - NAS framework for hybrid photonic quantum-classical models using genetic algorithm-based search with learnable quantum phase encoding (arXiv: 2605.22097)
   282|  - 19 hyperparameters encoded in 6 gene groups (classical preprocessing, phase encoding, photonic circuit, measurement, post-processing, training)
   283|  - Group-based crossover, per-gene mutation, elitism; 99.44% Digits, 98.78% MNIST accuracy
   284|  - Photonic layer extracts non-redundant features orthogonal to classical pathway
   285|  - **Activation**: quantum architecture search, photonic quantum computing, Q-PhotoNAS, quantum NAS, hybrid quantum neural architecture, quantum phase encoding, genetic algorithm quantum, photonic QPU, Quandela
   286|
   287|### Quantum Genetic Optimization for Negative Selection Algorithms in Anomaly Detection (arXiv:2605.22527)
   288|- [[quantum-genetic-negative-selection]] - QGNSA methodology integrating quantum genetic algorithms into negative selection for enhanced anomaly detection (arXiv: 2605.22527)
   289|  - Quantum superposition + probabilistic amplitude adjustment for diverse search space exploration
   290|  - Superior anomaly detection on Metaverse Financial Transactions Dataset
   291|  - Robust under varying hyperparameter configurations
   292|  - **Activation**: quantum genetic algorithm, negative selection, anomaly detection, QGNSA, quantum immune system, quantum superposition search
   293|
   294|## 2026-05-24 - Neuroscience Research (Cron Job)
   295|
   296|### Learning sequence timing and control of replay speed in networks of spiking neurons (arXiv:2605.22523)
   297|- [[learning-sequence-timing-spiking-neurons]] - sTM model extension for encoding element-specific timing and flexible replay speed modulation via oscillatory background input (arXiv:2605.22523)
   298|  - Timing encoding via sequential activation of delay-line assemblies within minicolumns (discretize time into dAP-compatible intervals)
   299|  - Oscillatory background input (simulating theta/gamma rhythms) acts as clock signal for replay speed control (10-70 Hz range)
   300|  - Replay speed independent of encoding speed — no relearning needed
   301|  - Structural STDP + continuous weight decay; Plateau potentials (~100ms) set intrinsic timescale
   302|  - **Activation**: spiking neural network, sequence timing, replay speed, sTM model, temporal memory, oscillatory control, dendritic action potential
   303|
   304|### Efficient coding under constraint drives neural systems towards criticality and sloppiness (arXiv:2605.22598)
   305|- [[efficient-coding-criticality-sloppiness]] - Theoretical framework linking Fisher information maximization under resource constraints to brain criticality, soft modes, and sloppiness (arXiv:2605.22598)
   306|  - Maximizing Fisher info under trace(Tr(A)) constraint forces precision matrix toward rank-1 → diverging correlation length (statistical criticality) + critical slowing down (dynamical criticality)
   307|  - Unifies statistical and dynamical criticality perspectives in a single minimal Gaussian population coding model
   308|  - Quench events in sloppy directions produce power-law avalanche distributions from spectral geometry alone
   309|  - Hebb-like learning rule δW ∝ ggᵀW maps directly onto predictive coding architecture
   310|  - **Activation**: brain criticality, efficient coding, Fisher information, neural avalanches, sloppiness, soft modes
   311|
   312|### Cross-Species RSA Reveals Conserved Early Visual Alignment but Divergent Higher-Area Rankings (arXiv:2605.22401)
   313|- [[cross-species-rsa-brain-alignment]] - Systematic RSA comparison of 5 learning rules (BP, FA, PC, STDP, untrained) across human fMRI and macaque electrophysiology (arXiv:2605.22401)
   314|  - STDP and PC lead at V1/V2 (ρ~0.30), conserved across species; IT rankings show no cross-species correlation
   315|  - Macaque electrophysiology yields 2-4x higher alignment than human fMRI (ρ 0.15-0.30 vs 0.01-0.08)
   316|  - ResNet-50 (ImageNet) achieves ρ=0.25 at macaque IT, far above all custom CNN conditions (ρ=0.07-0.14)
   317|  - **Activation**: RSA, cross-species, brain alignment, representational similarity, learning rules, visual cortex
   318|
   319|## 2026-05-23 - Economics/Quantum Finance (Cron Job)
   320|
   321|### Constrained Counterdiabatic QAOA for Portfolio Optimization (arXiv:2605.06858)
   322|- [[constrained-counterdiabatic-qaoa-portfolio]] - CCD-QAOA incorporating approximate adiabatic gauge potentials from nested commutators into QAOA ansatz for constrained portfolio optimization with XY mixer (arXiv:2605.06858)
   323|  - Counterdiabatic driving terms accelerate convergence by adding shortcuts to adiabaticity
   324|  - XY mixer preserves Hamming weight, naturally enforcing budget constraints without penalties
   325|  - **Activation**: CCD-QAOA, counterdiabatic QAOA, constrained portfolio optimization, XY mixer, adiabatic gauge potential
   326|
   327|### Quantum Reservoir Computing for Volatility Forecasting (arXiv:2505.13933)
   328|- [[quantum-reservoir-computing-finance]] - Quantum reservoir computing using transverse-field Ising Hamiltonian with input/memory qubits for financial time series forecasting (arXiv:2505.13933)
   329|  - Consistently outperforms classical econometric models and ML benchmarks on volatility prediction
   330|  - Wrapper-based feature selection + Shapley values for interpretability on NISQ hardware
   331|  - **Activation**: quantum reservoir computing, QRC finance, quantum volatility forecasting, Ising Hamiltonian reservoir
   332|
   333|## 2026-05-23 - Neuroscience Research (Cron Job)
   334|
   335|### Winner-Take-All bottlenecks enforce disentangled symbolic representations in multi-task learning (arXiv:2605.22472)
   336|- [[winner-take-all-bottleneck-disentangled]] - WTA bottlenecks provably enforce extraction of categorical latent factors in multi-task learning, producing symbolic single-neuron encodings (arXiv:2605.22472)
   337|  - Theoretical proof that WTA (cortical circuit motif) produces disentangled symbolic representations in deep networks
   338|  - Single neurons encode single abstract features (object, color, position)
   339|  - Enables compositional generalization; bridges sub-symbolic to symbolic AI
   340|  - **Activation**: WTA, winner-take-all, disentangled representations, symbolic AI, latent factors, cortical circuits, multi-task learning, neural bottleneck
   341|
   342|### Von Economo neurons enable reliable social skill acquisition in recurrent spiking neural networks
   343|- [[vencircuit-von-economo-snn-social-learning]] - VENCircuit computational account showing Von Economo neurons (2% of total) act as acquisition scaffolds in SNNs, providing a 21-fold increase in training convergence odds (arXiv: 2605.17399)
   344|  - VENs provide a direct gradient pathway immune to Jacobian instabilities in recurrent circuits
   345|  - VEN-intact: 98% convergence vs VEN-ablated: 70% (Fisher's OR=21.0, p=8.7e-5)
   346|  - Phase ablation shows VEN removal most disruptive during mid-training (epochs 5-25)
   347|  - Inference ablation: heterogeneous effects — from no change to catastrophic collapse (0.989→0.620)
   348|  - Clinical predictions: developmental VEN reduction → stochastic learning failure (ASC); adult VEN loss → heterogeneous performance effects (bvFTD)
   349|  - **Activation**: Von Economo neurons, VENCircuit, social learning SNN, gradient flow, training stability, frontotemporal dementia, autism spectrum
   350|
   351|### Supervised Deep Multimodal Matrix Factorization for Interpretable Brain Network Analysis
   352|- [[sd3mf-multimodal-brain-network]] - SD3MF extends SNMTF from unsupervised clustering to supervised prediction over populations of multimodal graphs with deep hierarchical factorizations and adaptive multimodal fusion (arXiv: 2605.13312)
   353|  - Encoder-decoder formulation jointly optimizes graph reconstruction and supervised prediction
   354|  - Community-level interaction matrices yield interpretable + discriminative features
   355|  - Outperforms CNNs and GNNs on multimodal connectome datasets
   356|  - Adaptive weights enable data-driven multimodal fusion
   357|  - **Activation**: SD3MF, multimodal brain network, matrix factorization, interpretable connectome analysis
   358|
   359|## 2026-05-23 - Economics, Investment + Quantum Mechanics (Cron Job)
   360|
   361|### Quantum Computing for Financial Transformation: A Review of Optimisation, Pricing, Risk, Machine Learning, and Post-Quantum Security
   362|- [[quantum-finance-stack]] - Financial computation stack framework evaluating quantum advantage across five domains: portfolio optimisation, derivative pricing, tail-risk estimation, quantum ML, and post-quantum security (arXiv: 2604.08180)
   363|  - Applies common evaluative logic: identify bottleneck, specify quantum primitive, compare classical benchmark, assess realistic constraints
   364|  - 134-page comprehensive review; strongest near-term case is carefully designed hybrid workflows
   365|  - Classical MIP solves 1000-asset portfolio instances in seconds; problem-tailored heuristics outperform quantum
   366|  - Post-quantum cryptography already strategically necessary for financial infrastructure
   367|  - **Activation**: quantum finance stack, financial quantum computing, quantum portfolio benchmark, quantum derivative pricing, quantum risk estimation, post-quantum cryptography finance, hybrid quantum finance workflow
   368|
   369|### Hot-Starting Quantum Portfolio Optimization
   370|- [[hotstart-quantum-portfolio]] - Compact Hilbert space QUBO formulation restricting search to vicinity of continuous optimum, reducing qubits and outperforming SOTA on D-Wave Advantage quantum annealer (arXiv: 2510.11153)
   371|  - Solves continuous relaxation first, maps to nearest discrete solutions, constructs reduced QUBO
   372|  - Reduces qubit requirements from O(N log M) to O(N log delta) where delta << M
   373|  - Outperforms existing warm-start and full QUBO approaches on both classical and quantum solvers
   374|  - **Activation**: hot-start quantum portfolio, warm-start QUBO, compact Hilbert space optimization, quantum portfolio reduction, D-Wave portfolio optimization
   375|
   376|### Dynamical Hamiltonian Encoding
   377|- [[dynamical-hamiltonian-encoding]] - Data encoding methodology addressing the Inverse Born Rule Fallacy — uses non-commutative Hamiltonian evolution instead of static phase-locked amplitude encoding for genuine quantum advantage in ML/finance (arXiv: 2602.21350)
   378|  - Standard amplitude encoding (psi = sqrt(P)) restricts to positive real orthant, making states "phase-deaf"
   379|  - DHE encodes data as coefficients of non-commuting Hamiltonian generators, preserving full Hilbert space access
   380|  - Based on QIFT (Quantum Imaginary Time Evolution) framework
   381|  - **Activation**: dynamical Hamiltonian encoding, inverse Born rule fallacy, quantum data encoding, amplitude encoding alternative, QIFE quantum ML, non-commutative quantum feature map
   382|
   383|### Quantum Portfolio Optimization with Expert Analysis Evaluation
   384|- [[quantum-portfolio-expert-eval]] - (existing skill reference) VQE/QAOA benchmark for portfolio optimization introducing Expert Analysis Evaluation framework — bridges gap between algorithmic performance and financial applicability (arXiv: 2507.20532)
   385|  - Financial professionals assess economic soundness of quantum-optimized portfolios
   386|  - Algorithmic convergence does not guarantee financial viability (diversification, risk exposure violations)
   387|  - **Activation**: quantum portfolio expert evaluation, VQE portfolio benchmark, QAOA financial viability
   388|
   389|### Quantum Portfolio Optimization: An Extensive Benchmark
   390|- [[quantum-portfolio-benchmark]] - (existing skill reference) Comprehensive benchmark comparing quantum annealing + QAOA against classical MIP, simulated annealing, tabu search on 250 real-world instances up to 1000 assets (arXiv: 2509.17876)
   391|  - Classical MIP solves all instances to proven optimality in seconds
   392|  - Problem-tailored heuristic consistently outperforms quantum approaches for fixed runtime
   393|  - Limited room for quantum advantage in standard portfolio optimization
   394|  - **Activation**: quantum portfolio benchmark, quantum advantage finance, portfolio optimization comparison
   395|
   396|## 2026-05-23 - Neuroscience Research: JET EEG Generation + ELSA SNN Accelerator (Cron Job)
   397|
   398|### JET: Just EEG Transformer — Continuous Flow Matching for EEG Generation
   399|- [[jet-eeg-flow-matching]] - Generative EEG framework using conditional flow matching that models neural signals as continuous trajectories, preserving spectral structure and temporal stationarity. ICML 2026. Reduces TS-FID by >40% (arXiv: 2605.21280)
   400|  - Continuous flow matching captures temporal continuity better than discrete diffusion-based EEG generation
   401|  - Principled constraints preserve spectral structure, temporal stationarity, and signal-level statistics
   402|  - Raw sequence modeling without domain-specific representations
   403|  - **Activation**: JET EEG transformer, conditional flow matching EEG, continuous EEG generation, EEG flow matching, spectral structure EEG generation, raw EEG sequence modeling
   404|
   405|### ELSA: An ELastic SNN Inference Architecture for Efficient Neuromorphic Computing
   406|- [[elsa-snn-elastic-inference]] - Near-SRAM dataflow architecture realizing true elastic inference via spine/token-wise pipeline, bundled AER protocol, and mini-batch spiking Gustavson-product for SNN sparsity. ISCA 2026. 3.4× speedup, 13.6-22.1× energy efficiency vs SOTA (arXiv: 2605.20802)
   407|  - Spine/token-wise pipeline forwards each spike immediately, enabling true elastic inference
   408|  - Bundled AER protocol reduces NoC communication traffic
   409|  - Mini-batch spiking Gustavson-product exploits inherent SNN sparsity
   410|  - SNNs can outperform quantized ANNs (4-bit ResNet-50) while maintaining accuracy
   411|  - **Activation**: ELSA SNN accelerator, elastic SNN inference, spine-wise pipeline neuromorphic, bundled AER protocol, spiking Gustavson product, near-SRAM SNN architecture
   412|
   413|## 2026-05-23 - Neuroscience Research: MIRAGE Mental Imagery + Platonic Representations (Cron Job)
   414|
   415|### MIRAGE: Robust Multi-Modal fMRI-to-Mental-Image Decoding
   416|- [[mirage-fmri-mental-imagery-decoding]] - Multi-modal fMRI decoder for cross-decoding visual perception to mental imagery. Linear backbone + multi-modal features (text, high-level, low-level image) → diffusion model, achieving SOTA on NSD-Imagery benchmark (arXiv: 2605.17198)
   417|  - SOTA on seen images ≠ SOTA on mental images: architecture must be explicitly designed for cross-decoding
   418|  - Low-dimensional image features + text guidance + multi-level features gives best mental image quality
   419|  - Linear backbone outperforms complex nonlinear encoders for mental image decoding
   420|  - Validated by both feature metrics and human raters
   421|  - **Activation**: MIRAGE, fMRI mental imagery, brain-to-image decoding, mental image reconstruction, NSD-Imagery, vision decoder generalization, fMRI diffusion model, neuroimaging decoding
   422|
   423|### Learning Sequence Timing and Replay Speed in Spiking Neural Networks
   424|- [[learning-sequence-timing-snn]] - Biologically plausible SNN sequence learning extending spiking Temporal Memory (sTM) with element-specific timing encoding via sequential population activation and oscillatory clock-based replay speed modulation (arXiv: 2605.22523)
   425|  - sTM model extended to encode element-specific durations via synfire chain propagation
   426|  - Oscillatory background input (θ/γ rhythms) provides flexible clock signal for replay speed control
   427|  - Elapsed time encoded by unique sparse spatiotemporal neural activity patterns
   428|  - Links replay speed to EEG/LFP oscillatory patterns (θ during wake, γ during sleep)
   429|  - **Activation**: spiking temporal memory, sTM model, sequence timing SNN, replay speed control, oscillatory clock neural, synfire chain timing, SNN sequence learning, theta gamma replay
   430|
   431|### Mamba Spike Forecaster for Behavioral Decoding in BCIs
   432|- [[mamba-spike-forecaster-bci]] - Single Mamba state-space model trained on next-step spike counts at Neuropixels scale simultaneously forecasts neural population activity and decodes behavioral state via lightweight linear readout. Achieves 75.7% choice decoding on Steinmetz benchmark (arXiv: 2605.12999)
   433|  - Mamba SSM forecaster predicts next-step spike counts → denoised rates improve decoding by 4-6 pp over raw spikes
   434|  - Lightweight per-session linear readout calibrates in just 100-150 trials
   435|  - Validated on 39 sessions, ~27,000 neurons, 1,994 held-out trials
   436|  - Pipeline fits within 50 ms bin budget on workstation GPUs for closed-loop BCI
   437|  - **Activation**: Mamba neural decoding, spike forecasting BCI, implicit behavioral decoding, Neuropixels Mamba, state space model neuroscience, Steinmetz benchmark, closed-loop BCI Mamba
   438|
   439|### Platonic Representations in the Human Brain: Unsupervised Recovery of Universal Geometry
   440|- [[platonic-representations-brain-universal-geometry]] - Self-supervised recovery of universal neural geometry across subjects using fMRI. Evidence that human visual cortex representations are approximately isometric and translatable via unsupervised orthogonal rotations (arXiv: 2605.20496)
   441|  - Self-supervised encoder learns subject-specific embeddings from fMRI alone via repeated stimulus presentations
   442|  - Unsupervised orthogonal rotation alignment translates independently learned brain spaces across subjects
   443|  - Shared latent space via synchronized pairwise rotations improves cross-subject retrieval
   444|  - Bridges ANN representation convergence and biological neural geometry
   445|  - **Activation**: platonic representation, universal geometry, brain representation, cross-subject alignment, fMRI visual cortex, isometric embedding, Natural Scenes Dataset, self-supervised brain encoding
   446|
   447|## 2026-05-23 - Economics, Investment + Quantum Finance (Cron Job)
   448|
   449|### Constraint Locality XY-Mixer Design under Trotterized Adiabatic Evolution
   450|- [[constraint-locality-xy-mixer-design]] - XY-mixer effectiveness under Trotterization depends on constraint locality: global constraints suffer Trotter errors, local blocks excel (arXiv: 2605.02465)
   451|  - 核心要点: XY-mixer dominant Trotter error depends on individual constraint structure, not total problem size
   452|  - 核心要点: Single global equality constraint → use Pauli-X mixer; multiple disjoint local blocks → use XY-mixer
   453|  - 核心要点: Dedicated 2-way-1-hot mixer Hamiltonian for TSP-like constraints
   454|  - **Activation**: XY-mixer design, Trotterized adiabatic evolution, constraint locality, constraint-preserving mixer, combinatorial optimization quantum, quantum portfolio optimization mixer
   455|
   456|### Quantum Tilted Loss in Variational Optimization
   457|- [[quantum-tilted-loss-optimization]] - Operator-level exponential tilting that reshapes VQA optimization landscapes to mitigate barren plateaus by amplifying gradient signals (arXiv: 2605.02850)
   458|  - 核心要点: QTL objective L(θ) = log Tr[exp(-βH)ρ(θ)] amplifies gradients where standard VQAs flatten
   459|  - 核心要点: Single tunable parameter β controls landscape sharpness; annealing schedule provides exploration→exploitation
   460|  - 核心要点: Naturally captures tail risk in financial applications (CVaR-like behavior)
   461|  - **Activation**: quantum tilted loss, QTL optimization, barren plateau mitigation, VQA training improvement, exponential tilting quantum, variational quantum algorithm landscape
   462|
   463|### Digital Spreading Framework for Quantum Expectation Computation
   464|- [[digital-spreading-quantum-finance]] - Resolves rotation gate vs arithmetic circuit tradeoff using pruned Cuccaro ripple-carry — eliminates both sine-to-square bias and O(n²) complexity (arXiv: 2604.05452)
   465|  - 核心要点: Analog rotation gates suffer sine-to-square bias; digital WeightedAdder circuits are O(n²) — both exceed NISQ limits
   466|  - 核心要点: Pruned Cuccaro ripple-carry achieves O(n) gate count with no rotation gates
   467|  - 核心要点: Pure digital expectation computation compatible with NISQ coherence times
   468|  - **Activation**: digital spreading quantum, Cuccaro ripple-carry quantum, quantum finance NISQ, rotation-free quantum computation, quantum expectation computation, financial engineering quantum
   469|
   470|### Contextual Quantum Neural Networks for Stock Price Prediction
   471|- [[contextual-qnn-stock-prediction]] - Multi-asset stock prediction via quantum multi-task learning with share-and-specify ansatz (arXiv: 2503.01884)
   472|  - 核心要点: Share-and-specify ansatz enables simultaneous multi-asset training on single quantum circuit
   473|  - 核心要点: Quantum batch gradient update (QBGU) accelerates convergence over standard quantum SGD
   474|  - 核心要点: Logarithmic qubit overhead O(log N) for N assets via quantum superposition
   475|  - **Activation**: contextual quantum neural network, stock price prediction, quantum multi-task learning, QMTL, share-and-specify ansatz, quantum batch gradient update, QBGU, quantum finance
   476|
   477|### FiD-QAE: Fidelity-Driven Quantum Autoencoder for Fraud Detection
   478|- [[fid-quantum-autoencoder-fraud]] - Quantum autoencoder for fraud detection using SWAP test fidelity estimation (arXiv: 2512.12689)
   479|  - 核心要点: Fidelity estimation via SWAP test as anomaly detection criterion
   480|  - 核心要点: Maintains consistent performance under multiple quantum noise models
   481|  - 核心要点: Validated on IBM Quantum hardware with results consistent with simulation
   482|  - **Activation**: quantum autoencoder, fraud detection, fidelity estimation, SWAP test, anomaly detection, quantum machine learning, credit card fraud
   483|
   484|### Comparative QML Architecture Analysis for Fraud Detection
   485|- [[qml-fraud-detection-comparison]] - Systematic comparison of VQC, SQNN, EQNN for financial fraud detection (arXiv: 2412.19441)
   486|  - 核心要点: VQC consistently achieves F1-score of 0.88, outperforming SQNN and EQNN
   487|  - 核心要点: Feature map and ansatz configuration choices dominate architecture selection
   488|  - 核心要点: ANOVA validation confirms statistical significance of performance differences
   489|  - **Activation**: quantum machine learning comparison, VQC, SQNN, EQNN, fraud detection architecture, quantum feature map, ansatz configuration, ANOVA validation
   490|
   491|## 2026-05-23 - Neuroscience Cron (Spiking Language Models + Spike Operators)
   492|
   493|### SymbolicLight V1: Spike-Gated Dual-Path Language Modeling with High Activation Sparsity
   494|- [[symboliclight-spike-gated-language]] - First natively trained spiking language model combining binary LIF spike dynamics with continuous residual stream. 194M params, >89% activation sparsity, PPL 8.88 on bilingual corpus (arXiv: 2605.21333)
   495|  - Dual-Path SparseTCAM replaces dense self-attention with exponential-decay path + spike-gated local attention
   496|  - Ablation proves temporal integration (not sparsity alone) drives performance
   497|  - 0.8B scale-up demonstrates sparsity preservation at larger scale
   498|  - **Activation**: symboliclight, spike-gated language model, spiking language model, LIF language model, activation sparsity
   499|
   500|### Plug-and-Play Spiking Operators: Breaking the Nonlinearity Bottleneck
   501|
