## 2026-07-30 - Quantum Neuroscience Research (Cron Job)

### Quantum error correction and biological error correction: A structural analogy between qubits and neurons
- [[quantum-error-correction-biological-analogy]] - Structural analogy methodology between quantum error correction (QEC) and biological error correction (BEC) in neural circuits, focusing on redundant encodings, constraint-based inference, and codespace protection (arXiv: 2607.20534)
  - Establishes mapping between QEC components (logical qubits, stabilizer constraints, syndrome detection) and BEC equivalents (neural population codes, recurrent constraints, mismatch signals)
  - Proposes neural codespace as constrained manifold where collective activity is protected from individual neuron errors
  - Demonstrates bidirectional insights: QEC principles can improve neural models and biological strategies can inspire novel QEC approaches
  - **Activation**: quantum error correction, biological error correction, neural codespace, redundant encoding, constraint-based inference, cross-disciplinary neuroscience

## 2026-07-30 - Quantum Computing Research (Cron Job)

### OmniQEC: discovering practical quantum error-correcting codes by an AI scientist
- [[omniqec-ai-scientist-quantum-error-correction]] - AI scientist framework for discovering QEC codes using LLM orchestrator with slow-fast synergistic workflow (arXiv: 2607.25865)
  - Formulates QEC design as iterative discovery process with code generation, screening, syndrome extraction, and decoder evaluation
  - Combines fast loop (inexpensive code-level proxies) with slow loop (physically grounded circuit evaluation)
  - Discovered codes outperform BB codes under complete-implementation budgets of 98 and 240 physical qubits
  - **Activation**: quantum error correction, QEC, qLDPC, AI scientist, LLM-assisted discovery, code-circuit-decoder co-design

## 2026-07-30 - Systems Engineering Research (Cron Job)

### VeraGrid-Agent: Tool-Augmented LLMs for Distribution Optimal Power Flow at the Grid Edge
- [[veragrid-agent-tool-augmented-llm-power-flow]] - Tool-augmented LLM methodology for solving distribution optimal power flow problems by integrating with numerical solvers like VeraGrid (arXiv: 2607.25155)
  - Integrates LLMs with numerical solvers for complex scientific questions requiring D-OPF problem solving
  - Achieves near-perfect accuracy compared to random chance without tools
  - Framework extensible to other domains requiring numerical computation
  - **Activation**: veragrid-agent, tool-augmented-llm, power-flow-simulation, distribution-optimal-power-flow, numerical-solver-integration, scientific-llm-reasoning

### Specula: Scaling formal specifications for autonomous model checking of system code
- [[specula-formal-specifications-model-checking]] - Autonomous agentic system for generating formal specifications and model checking of system code using LLM-based coding agents (arXiv: 2607.25333)
  - Fully autonomous TLA+ specification generation eliminating human expertise barriers
  - Self-evolving loops address LLM limitations through iterative refinement
  - Found 249 bugs across 48 open-source system projects including deep, hard-to-find bugs
  - **Activation**: specula, formal-specifications, model-checking, tla-plus, llm-agents, autonomous-verification, system-code-analysis, bug-finding
## 2026-07-30 - Neuroscience Research (Cron Job)

### More Electrodes, Faster Minds? Rethinking Bandwidth in Brain-Computer Interfaces
- [[bci-bandwidth-scaling-perspective]] - Framework for understanding the nonlinear scaling relationship between brain-computer interface bandwidth and meaningful human input/output capacity, distinguishing between raw bandwidth, decodable neural states, and information a person can actually use, confirm, and express through embodiment, learning, and subject expression constraints (arXiv: 2607.24820)
  - Four levels of neural information: raw bandwidth, decodable neural states, neural states, and meaningful human I/O
  - Nonlinear scaling due to embodiment, learning, and subject expression constraints  
  - Practical implications for BCI design: output side (prediction/control) vs input side (plasticity/learning)
  - **Activation**: bci bandwidth scaling, brain-computer interface capacity, neural decoding limits, embodied bci design, meaningful neural i/o, bci confirmation mechanisms, nonlinear bci scaling## 2026-07-30 - Neuroscience Research (Cron Job)

### GraphIDyOM: A graph-native Python reimplementation of IDyOM for musical expectation modelling
- [[graphidyom-musical-expectation-modeling]] - Graph-native Python reimplementation of the Information Dynamics of Music (IDyOM) model that represents long-term and short-term predictive memories as explicit graph objects while preserving variable-order, multiple-viewpoint architecture for musical expectation modeling (arXiv: 2607.25787)
  - Represents predictive memories as explicit graph objects for network analysis and inspection
  - Provides Python-native integration with modern data science workflows and memory export capabilities
  - Validated against original Lisp IDyOM across single, projected, and multiple-viewpoint configurations
  - Supports local server access and interactive applications through HTTP API
  - **Activation**: graphidyom, musical expectation, IDyOM, information dynamics music, graph-native music modeling, predictive memory graphs

### Current Injection Spiking Neural Network for Infrared and Visible Image Fusion
- [[current-injection-spiking-neural-network]] - Framework for infrared and visible image fusion using Current Injection Spiking (CIS) operators that perform cross-modal fusion at membrane-potential level before spike firing, solving the fundamental tension between sparse spikes and fine-grained fusion (arXiv: 2607.19879)
  - Introduces Current Injection Spiking (CIS) operator that injects one modality as gated auxiliary current into driving neuron of other modality
  - Performs cross-modal fusion directly at membrane-potential level, preserving subthreshold responses from both modalities
  - Constructs bidirectional cross-modal fusion (BCMF) module with dual-branch architecture and asymmetric stacking depths
  - Achieves fusion quality on par with state-of-the-art ANN-based methods while reducing inference energy by order of magnitude
  - **Activation**: current injection spiking neural network, CIS-Fuse, infrared visible image fusion, membrane potential fusion, spiking neural network fusion, cross-modal SNN fusion


### Scalable Variational Quantum Optimization via Pauli Correlation Encoding: Application to Large-Scale Power Demand Portfolio Optimization
- [[pce-quantum-portfolio-optimization]] - Scalable variational quantum optimization framework using Pauli correlation encoding for large-scale combinatorial optimization, particularly power demand portfolio optimization with compact qubit representations (arXiv: 2607.24722)
  - Binary variables represented through expectation values of Pauli correlation operators encoding multi-body correlations
  - Two-stage hybrid formulation: time-averaged problem provides initialization for time-resolved optimization
  - Demonstrates near-optimal performance from m=18 to 10,296 variables with normalized cost gaps ~10⁻³
  - Performance governed by interplay between continuous relaxation and discretization resolution
  - **Activation**: pce-quantum-optimization, pauli-correlation-encoding, quantum-portfolio-optimization, scalable-variational-quantum, power-demand-optimization
## 2026-07-29 - Neuroscience Research (Cron Job)

### Foundation Models for EEG Are Blind to Long-Range Temporal Correlations: A Spectral-Temporal Dissociation Behind Their Cross-Population Fragility
- [[eeg-fm-temporal-correlations-blindness]] - Methodology for analyzing and addressing the spectral-temporal dissociation in EEG foundation models that causes cross-population fragility due to blindness to long-range temporal correlations (LRTC) quantified by DFA exponent (arXiv: 2607.24834)
  - Raw-waveform models (REVE, LaBraM, BENDR) fail to recover both DFA exponent and 1/f slope (R² ≤ 0.12)
  - Spectral-input models (CBraMod, BIOT) recover 1/f slope strongly (R² = 0.59-0.73) but not DFA across cohorts
  - Classical DFA feature successfully recovers DFA exponent (R² = 0.32-0.38 against 0.64 reliability ceiling)
  - LRTC is orthogonal to aperiodic slope (r = -0.06) and shows directional cross-population transfer
  - **Activation**: eeg foundation model temporal correlations, lrtc eeg fm, spectral-temporal dissociation eeg, cross-population eeg transfer, dfa exponent eeg

### Spiking Neural Networks for fMRI-Based Visual Semantic Decoding
- [[snn-fmri-visual-decoding]] - Methodology for using Spiking Neural Network (SNN)-derived visual features as alternative targets for fMRI-based visual semantic decoding, demonstrating superior alignment with brain activity compared to traditional ANN features (arXiv: 2607.19170)
  - SNN-derived features reduce feature-prediction error from 0.7707 to 0.0282 on GoD dataset
  - Top-1 semantic decoding accuracy improves from 0.1800 to 0.4400 using SNN features
  - Both spiking neural dynamics and temporal simulation steps contribute to the observed advantage
  - SNN-derived features serve as more effective brain-decodable visual representations
  - **Activation**: spiking neural networks, fMRI decoding, visual semantic decoding, brain-computer interface, neural alignment, SNN features, temporal simulation, brain-decodable representations

### CogEEGAgent: Toward Autonomous Cognitive EEG Analysis
- [[cog-eeg-agent-autonomous-analysis]] - LLM-powered EEG analysis agent grounded in MNE-Python that separates semantic interpretation from scientific validation using deterministic contracts and confirmation controls to prevent false positives (arXiv: 2607.25045)
  - Grounded execution architecture integrates with MNE-Python for deterministic scientific validation
  - Participant-disjoint confirmation controls prevent false positives during adaptive search
  - Policy stress testing shows held-out confirmation curbs adaptive search errors effectively
  - **Activation**: cogeegagent, autonomous eeg analysis, llm eeg agent, grounded eeg analysis, scientific validation eeg

### Subject-Level Heterogeneity in EEG Motor Imagery Decoding: A Large-Scale Benchmark and Portfolio-Based Reduction of the Search Space
- [[subject-level-heterogeneity-eeg-motor-imagery]] - Large-scale benchmark methodology for EEG motor imagery decoding that addresses subject-level heterogeneity through portfolio-based pipeline selection (arXiv: 2607.22778)
  - Analyzes 216,714 evaluation rows across three datasets (Cho2017, PhysionetMI, Zhou2016) with strong subject-level heterogeneity
  - Identifies cov-tgsp and CSP as top methodological families with dataset-dependent performance
  - Demonstrates portfolio-based personalization achieves 96.5% oracle retention with K=12 pipelines
  - **Activation**: eeg-motor-imagery, subject-heterogeneity, benchmark, portfolio-selection, cov-tgsp, csp

### Phantom Evidence: How and Why Generative AI Manufactures False Positives in Science
- [[phantom-evidence-generative-ai-false-positives]] - Methodology for identifying and preventing phantom evidence in scientific research caused by generative AI systems manufacturing false positives, formalizing the gap between imagined possibility space and actual system reach (arXiv: 2607.25991)
  - Higher resolution and greater fluency add no genuine evidence to scientific claims
  - Single results have a fundamental ceiling on evidential value that cannot be exceeded by polishing or self-grading
  - Bacon's table of absence restated in probability: test whether convincing outputs appear when targets are absent
  - **Activation**: phantom evidence, generative ai false positives, scientific methodology ai, bacon table absence, ai research integrity
## 2026-07-29 - Systems Engineering Research (Cron Job)

### SpecBox: Speculative Sandbox Scheduling for Efficient LLM Agent Serving
- [[specbox-speculative-sandbox-scheduling]] - Runtime framework for speculative sandbox preallocation and scheduling in LLM agent serving environments to optimize resource utilization and reduce tail latency (arXiv: 2607.23933)
  - Intent-driven sandbox prewarming using keyword matching and streaming semantic embedding
  - Context-aware stochastic prefetching with sandbox dependency graph forecasting
  - Semantic result cache to prune redundant sandbox invocations
  - Out-of-band shared-memory transport for zero-copy artifact transfers
  - **Activation**: specbox, speculative sandbox, llm agent serving, mcp sandbox, sandbox scheduling
## 2026-07-29 - Neuroscience Research (Cron Job)

### Limbomorphs: Emergent Agent-Like Dynamics in Artificial Life Systems
- [[limbomorphs-emergent-agent-dynamics]] - Methodology for studying emergent lifelike patterns (Limbomorphs) in Gifbreeder systems that encode spatiotemporal fields through aesthetic selection, analyzing their species-specific reactions to perturbations and assessing whether they exhibit genuine goal-directed behavior or merely its appearance (arXiv: 2607.23842)
  - No predefined agents, environments, or interaction rules - agent-like dynamics emerge from spatiotemporal field encoding and aesthetic selection
  - Species-specific reactions to input-space perturbations reveal distinct behavioral signatures despite deterministic three-second looping constraints
  - Framework for distinguishing genuine navigation from apparent goal-directed behavior in emergent systems
  - **Activation**: Limbomorphs, Gifbreeder, emergent agency, aesthetic evolution, spatiotemporal fields, goal-directed behavior

## 2026-07-29 - Neuroscience Research (Cron Job)

### Synaptic clustering emerges from learning and supports covariance discrimination
- [[synaptic-clustering-learning-covariance-discrimination]] - Synaptic clustering methodology for learning covariance structure discrimination using Dendrinet architecture with hierarchical dendritic segments and sparse conductance-based synapses (arXiv: 2607.24503)
  - Functional synapse clusters (FSCs) emerge when both dendritic nonlinearities and synaptic structural plasticity are active
  - Learned synaptic connectivity is causally necessary for computation - shuffling reduces performance even with fixed nonlinearities  
  - Inhibitory organization shows higher sensitivity than excitatory organization to performance
  - **Activation**: synaptic clustering, functional synapse clusters, dendritic nonlinearities, covariance discrimination

### When Branch-Local Shunting Helps: A Gain-Load-Alignment Principle for Dendritic E/I Networks
- [[dendritic-gain-load-alignment-principle]] - Framework for understanding when branch-local shunting helps in neural population readout through gain-load-alignment principle using DendriNet architecture (arXiv: 2607.24990)
  - Branch-local shunting helps when reliable divisor suppresses signal-aligned gain more than attenuating signal or adding denominator variability
  - Local linearization shows shunting readouts yield decision directions within positive additive E/I cone
  - Deep shunting outperforms tangent and fitted-linear controls but flexible nonlinear predictors eventually overtake it
  - Performance varies across mouse V1 running states with largest shunting advantage for narrow readouts
  - **Activation**: dendritic computation, shunting inhibition, gain-load-alignment, DendriNet, population readout

## 2026-07-29 - Deep Learning Research (Cron Job)

### MMOE: Modernizing Diffusion Transformers with Efficient Expert Design
- [[mmoe-diffusion-transformer-expert-design]] - ModernMOE (MMOE) methodology for modernizing diffusion transformers with efficient expert design. Adapts routed experts, shared and lightweight experts, gate-residual routing, and attention-residual information reuse to AIGC generation (arXiv: 2607.24665)
  - Systematically adapts proven LLM efficiency designs to AIGC foundation models in balanced way
  - Trains on single 8×H100 node with batch 256 for 400k steps, achieving lower FID faster than baselines
  - Demonstrates stable expert specialization with modest routing changes across denoising timesteps
  - **Activation**: MMOE, diffusion transformer MoE, efficient expert design, AIGC foundation models

### Efficiency Matters in Autonomous Research
- [[fluid-search-autonomous-research-efficiency]] - Fluid search methodology for adaptive search efficiency in autonomous research systems. Uses portfolio bandit to dynamically allocate evaluation budget across search processes, optimizing area under Pareto frontier curve (arXiv: 2607.24647)
  - Introduces AUC of Pareto frontier as search efficiency metric beyond final quality
  - Implements portfolio bandit that dynamically allocates budget across hill climbing, beam, tree, and evolutionary search
  - Closely matches per-task oracle performance without prior knowledge of optimal search structure
  - **Activation**: fluid search, autonomous research efficiency, search efficiency AUC, portfolio bandit search

### Physics Transformer: Tailoring Transformer for General PDE Prediction
- [[physics-transformer-pde-function-projection]] - Physics Transformer methodology for PDE prediction using function-projection-based tokenization. Treats physical fields as continuous functions with adaptive local basis functions and locality-preserving spatial patches (arXiv: 2607.24513)
  - Projects discretized physical fields onto adaptive local basis functions within spatial patches
  - Captures diverse latent physical states while preserving fine-scale spatial structures
  - Enables efficient global interaction through factorized attention and arbitrary query location decoding
  - **Activation**: physics transformer, PDE function projection, physical field tokenization, adaptive basis functions

## 2026-07-28 - Neuroscience Research (Cron Job)

### From read-out geometry to in-silico stimulation: a distributed functional-connectivity signature of Alzheimer's disease
- [[alzheimer-functional-connectivity-reservoir-computing]] - Methodology for identifying distributed functional-connectivity signatures of Alzheimer's disease using subject-specific reservoir-computing models and developing personalized neuromodulation strategies (arXiv: 2607.24356)
  - AD FC signature is distributed rather than focal, requiring coordinated multi-site patterns rather than single targets
  - Model-informed personalized targeting selects sites by therapeutic responsiveness rather than deviation magnitude  
  - Real-time closed-loop controller achieves comparable efficacy at lower dose using only causally available information
  - **Activation**: alzheimer reservoir computing, functional connectivity ad, distributed fc signature, personalized neuromodulation

### Synaptic clustering emerges from learning and supports covariance discrimination
- [[synaptic-clustering-learning-covariance-discrimination]] - Dendrinet architecture with hierarchical dendritic segments demonstrates that functional synapse clusters (FSCs) are causally necessary for computation of covariance structure in neural networks (arXiv: 2607.24503)
  - Functional synapse clusters (FSCs) emerge when both dendritic nonlinearities and synaptic structural plasticity are active during training on Permuted-Covariance Classification (PCC) tasks
  - Shuffling learned connectivity reduces performance, demonstrating sensitivity to learned synaptic organization beyond just FSC presence
  - Inhibitory synapse organization shows higher sensitivity than excitatory organization for optimal task performance
  - **Activation**: synaptic clustering, dendritic computation, covariance discrimination, Dendrinet architecture, structural plasticity

### Local Synaptic Rules Can Implement a SIGReg Gradient Without Backpropagation
- [[local-synaptic-rules-sigreg-gradient]] - Two canonical local synaptic learning rules (STDP+ and homeostatic plasticity) together can implement the exact gradient of a SIGReg-like self-supervised learning objective without backpropagation, global error signals, or weight transport (arXiv: 2607.21622)
  - Ordered presentation raises cluster separation ratio (CSR) to 2.49 while random ordering leaves it near baseline (0.83), showing temporal contiguity enables class structure recovery
  - Two-layer network trained entirely with these rules achieves 87.3% linear-probe accuracy on temporally ordered MNIST
  - Only requires pre- and post-synaptic firing rates, local firing statistics, and temporal contiguity of natural sensory streams
  - **Activation**: local synaptic rules, STDP gradient learning, biologically plausible backpropagation, SIGReg without backprop, temporal ordering clustering
## 2026-07-28 - Neuroscience Research (Cron Job)

### Stress-Testing EEG Foundation Models for Clinical Decoding: Dataset Identity and Targeted Negative Controls
- [[eeg-fm-stress-testing-clinical-decoding]] - Comprehensive benchmarking framework for stress-testing EEG foundation models with dataset identity analysis and targeted negative controls reveals that EEG foundation-model conclusions depend strongly on evaluation unit, dataset shift, comparator strength, and targeted controls (arXiv: 2607.24519)
  - Benchmarks six models (LaBraM, EEGMamba, CBraMod, REVE, BENDR, BIOT) on five clinical tasks across four datasets using frozen linear probes
  - Dataset identity is readily decoded from frozen embeddings (AUROC 1.000 at PCA-50; 0.9998 after preprocessing), while clinical diagnosis performance is often inferior to classical features
  - Randomly initialized encoder outperforms pretrained REVE on Korean dementia task (0.659 vs 0.570 AUROC)
  - Clear benefit only observed in cross-subject ictal detection (REVE: 0.793 AUROC, +9.2% over random)
  - **Activation**: eeg foundation models, stress testing, clinical decoding, dataset identity, negative controls, frozen linear probes

## 2026-07-28 - Neuroscience Research (Cron Job)

### The SpiNNaker2 chip: a many-core platform for flexible and scalable brain-inspired computing
- [[spinnaker2-neuromorphic-hardware-platform]] - SpiNNaker2 chip bridges deep learning and neuromorphic computing with 152 ARM M4F processing elements, achieving up to 4.5 TOPS and supporting >150,000 neurons with >1.8 billion synaptic events/s (arXiv: 2607.24396)
  - Features extended SpiNNaker routing fabric for scalable event-based communication and external interfaces including Gbit Ethernet and LPDDR4 memory
  - Achieves up to 2.7 TOPS/W efficiency in high efficiency mode for INT8 workloads with low baseline power of less than 250 mW
  - Demonstrates capabilities as universal hardware platform for scalable brain-inspired computing and combinations with mainstream deep network approaches
  - **Activation**: spinnaker2, neuromorphic hardware, brain-inspired computing, spiking neural network acceleration, many-core neuromorphic, event-based computing, ARM M4F neuromorphic, scalable brain simulation

### The Semantic Least-Energy Principle: A Hypothesis for Intelligence
- [[semantic-least-energy-principle-intelligence]] - Semantic Least-Energy Principle (SLEP) hypothesis that intelligent systems organize latent semantic states by maximizing semantic utility while minimizing semantic, predictive, and computational energy through a variational framework on latent semantic manifolds (arXiv: 2607.24287)
  - Proposes that semantic cognition is governed by a Semantic Action Functional whose stationary solutions define efficient trajectories on latent semantic manifolds
  - Unifies semantic abstraction, reasoning, planning, and communication within a common mathematical framework based on energy minimization principles
  - Generates experimentally testable predictions for both artificial and biological intelligence regarding semantic geometry and thermodynamics
  - **Activation**: semantic least-energy principle, semantic intelligence, latent semantic manifolds, first-principles intelligence, semantic thermodynamics, variational semantic cognition

## 2026-07-28 - Quantum Neuromorphic Research (Cron Job)

### Leveraging unlabelled data for generalizable neural population decoding
- [[mojo-ssl-neural-decoding]] - MOJO (Masked autOencoder-based JOint training) framework that combines self-supervised learning via masked autoencoding with supervised learning objectives for spike-tokenizing neural models, enabling superior performance with limited labelled data (arXiv: 2607.14086)
  - Joint SSL+SL training improves few-shot finetuning capability when only small amounts of labelled data from new sessions are available
  - Yields more interpretable neuronal representations, improving brain region classification and spike-statistics prediction without explicit optimization
  - Generalizes beyond spiking data to human electrocorticography during speech, achieving performance comparable to neuro-foundation models
  - **Activation**: neural decoding, spike-tokenizing, self-supervised learning, few-shot finetuning, brain-computer interface, neuro-foundation models, unlabelled neural data

## 2026-07-28 - Systems Engineering Research (Cron Job)

### Allostatic Control Systems: Goal Governance in Changing Environments
- [[allostatic-control-systems-goal-governance]] - Framework for designing control systems that govern not only goal pursuit but also goal appropriateness in changing environments, implementing two-timescale control with fast regulation loop and slow goal governance loop (arXiv: 2607.21771)
  - Fast regulation loop handles immediate environmental changes while slow goal governance loop evaluates and updates goals based on long-term appropriateness
  - Implements allostatic control inspired by biological homeostasis but extended to handle goal dynamics in complex environments
  - Provides mathematical framework for analyzing stability and performance of dual-timescale control systems
  - **Activation**: allostatic control, goal governance, dual-timescale control, adaptive goals, changing environments, biological inspiration
  - Two-timescale architecture separates fast goal pursuit from slow goal governance
  - Central principle: revise inappropriate goals faster than serviceability is lost by defending them
  - Evidence-based goal revision with timing-critical evidence-to-effect pathways
  - **Activation**: allostatic control, goal governance, adaptive reference, changing environments, two-timescale control, serviceability assessment

## 2026-07-28 - Neuroscience Research (Cron Job)

### Synaptic clustering emerges from learning and supports covariance discrimination
- [[synaptic-clustering-learning-covariance-discrimination]] - Dendrinet architecture with hierarchical dendritic segments and sparse conductance-based synapses demonstrates that functional synapse clusters emerge from learning and support covariance discrimination computation (arXiv: 2607.24503)
  - Functional synapse clusters (FSCs) develop during training when both dendritic nonlinearities and synaptic structural plasticity are active
  - Shuffling learned connectivity reduces performance, demonstrating causal necessity of learned organization
  - Inhibitory synapse organization shows higher sensitivity than excitatory organization in PCC tasks
  - **Activation**: synaptic clustering, dendritic computation, covariance discrimination, biologically-inspired neural networks, functional synapse organization

### Masked Autoencoders Learn Perception-Relevant Representations from Resting State Neural Data
- [[masked-autoencoders-resting-state-neural-data]] - Self-supervised pretraining on spontaneous neural activity using masked autoencoders achieves 84.1% accuracy on psychometric tasks and 64.0% on threshold-level tasks for perception decoding (arXiv: 2607.22615)
  - Leverages 14.6 hours of spontaneous multiunit activity from intracortical V1 array to overcome data bottleneck in clinical neuroprosthetics
  - Captures interpretable brain structure without supervision: V1's spatial organization and perceptual state separation emerge in latent representations
  - Linear probing on frozen latents demonstrates rich task-relevant structure in spontaneous cortical activity
  - **Activation**: neural decoding enhancement, self-supervised learning for neural data, resting state activity analysis, clinical neuroprosthetics, masked autoencoder pretraining

### Universal BCI Personalization: One API for Frozen EEG Trunks and Foundation Models
- [[universal-bci-personalization-api]] - Trunk-agnostic BCI personalization API that works across heterogeneous frozen EEG trunks without per-architecture personalization stacks (arXiv: 2607.22397)
  - Single contract encode to Bayesian head to BrainState architecture enables OEMs to integrate once and swap trunks
  - Achieves orders of magnitude less adaptation wall time while recovering much of fine-tune accuracy gain
  - Calibration-only-when-clean holds in 12/18 experimental cells with subject-level confidence intervals
  - **Activation**: universal bci personalization, trunk-agnostic eeg, nimbus personalizer, frozen eeg trunks, bci foundation models
### NUMA balancing hampering performance of spiking network simulations
- [[numa-balancing-snn-performance]] - NUMA balancing performance optimization that can reduce energy consumption by 30% in spiking network simulations by disabling automatic NUMA balancing on HPC systems (arXiv: 2607.22275)
  - Identifies that automatic NUMA balancing dynamically interacts with spiking network memory access patterns, causing performance fluctuations
  - Provides methodology for per-job NUMA balancing control to optimize performance and energy consumption
  - **Activation**: numa balancing snn, spiking neural network numa optimization, hpc snn performance tuning, energy efficient snn simulation, numa balancing disable neuroscience

### On a cross coupling of Rulkov neural maps
- [[rulkov-neural-maps-cross-coupling]] - Novel coupling methodology for Rulkov neural maps preserving chaos and generating strange attractors (arXiv: 2607.22318)
  - Introduces cross-coupling that preserves chaotic dynamics while enabling complex synchronization patterns
  - Generates strange attractors through carefully designed coupling functions
  - Demonstrates applications in secure communication and pattern recognition
  - **Activation**: rulkov maps, cross coupling, chaos preservation, strange attractors, neural dynamics

### Spectral theory for population density dynamics of spiking neurons with refractoriness
- [[spectral-theory-spiking-neurons-refractoriness]] - Rigorous operator-theoretic framework using non-self-adjoint boundary eigenvalue problems for Fokker-Planck operators to analyze spiking neuron populations with refractory periods (arXiv: 2607.20699)
  - Solves long-standing open problem of incorporating absolute refractory periods into population density approaches
  - Provides complete spectral characterization and identifies exceptional points where oscillatory modes emerge
  - Derives exact transfer function correcting previous heuristic derivations with additional threshold-noise contributions
  - Shows refractoriness can facilitate limit cycle onset in interacting neuron populations under mean-field approximation
  - **Activation**: spectral theory, spiking neurons, refractoriness, population density, Fokker-Planck

### When Language Models Meet NeuroGraphs: Exploring Enhanced Agentic LLM Framework Towards Brain Network Analysis
- [[brainagent-agentic-llm-brain-network]] - BrainAgent agentic LLM framework for knowledge-enhanced brain network analysis, reformulating connectome classification as iterative topology-aware understanding, external retrieval, reasoning, and reflection (arXiv: 2607.22082)
  - Converts raw brain networks into compact multi-level structural descriptions through brain-specific analysis tools
  - Retrieves relevant neuroscience knowledge and task-specific cases to ground the reasoning process
  - Generates structured predictions with reflective verification for comprehensive, multi-level explanations
  - **Activation**: brain network analysis, connectome classification, agentic LLM neuroscience, knowledge-enhanced brain analysis, NeuroGraphs, BrainAgent framework

- [[project-pilot-ai-drone-control]] - Methodology for testing AI control of physical systems like drones through constrained interfaces and safety protocols. Based on Anthropic's July 2026 frontier red teaming research.
  - Constrained interface design with limited action space and safety boundaries
  - Safety protocol framework including pre-flight validation and emergency override
  - Evaluation metrics for task completion, safety compliance, and robustness
  - **Activation**: project pilot, ai drone control, physical system control, frontier red teaming

## 2026-07-28 - Deep Learning Research (Cron Job)

## 2026-07-28 - Neuroscience Research (Cron Job)

### Graph-Based Correlation Matrix Generation: A Convex Optimization Approach
- [[graph-based-correlation-matrix-generation]] - Graph-based correlation matrix generation using convex optimization for controlled sparsity and mean off-diagonal values (arXiv: 2607.22436)
  - Generates correlation matrices consistent with specified graph structures while allowing precise control over statistical properties
  - Provides tunable control over mean off-diagonal correlation values and maintains mathematical validity
  - Validated on real neuroscience and finance datasets for practical applicability
  - **Activation**: graph correlation matrix generation, convex optimization correlation, structured correlation matrices, neuroscience functional connectivity simulation, finance asset correlation modeling

### Interpretable EEG biomarkers with bag-of-waves: Spatial and temporal waveform dictionaries for low-data regimes
- [[bag-of-waves-eeg-biomarkers]] - Interpretable EEG biomarkers using shift-invariant k-means to learn waveform atoms without labels, effective in low-data regimes (arXiv: 2607.22508)
  - Learns small dictionary of recurring EEG waveform templates (atoms) using shift-invariant k-means
  - Converts continuous EEG into atom token sequences with temporal n-grams and spatial cross-channel extensions
  - Achieves competitive performance with state-of-the-art deep models while providing full interpretability
  - **Activation**: bag-of-waves, EEG biomarkers, interpretable EEG, waveform dictionaries, low-data EEG

### LeAct: Learning to Reason from Expert Actions
- [[leact-learning-to-reason-from-expert-actions]] - LeAct framework for recovering chain-of-thought reasoning from expert systems that only produce actions without explicit reasoning traces, treating CoT as a latent variable optimized via action probability scoring (arXiv: 2607.21856)
  - Recovers reasoning from silent expert systems like game solvers and theorem provers
  - Uses action probability scoring to evaluate and retain high-quality CoTs
  - Achieves 5× closer to solver performance than expert-iteration baselines
  - **Activation**: leact, expert actions, chain of thought recovery, silent experts, action-guided reasoning

### Teaching LLMs to Self-Evolve: Cultivating Core Meta-Skills with Reinforcement Learning
- [[teaching-llms-to-self-evolve]] - Framework for teaching LLMs to self-evolve by cultivating core meta-skills with reinforcement learning, enabling autonomous capability expansion through iterative self-improvement cycles (arXiv: 2607.21971)
  - Builds foundational meta-skills for autonomous self-improvement
  - Uses RL to optimize self-evolution behaviors and strategies
  - Creates feedback loops for continuous capability growth
  - **Activation**: self-evolve, meta-skills, reinforcement learning, autonomous improvement, capability expansion

### IFCLoRA: Topology-Aware Rank Allocation for Parameter-Efficient Fine-Tuning
- [[ifclora-topology-aware-rank-allocation]] - IFCLoRA framework for topology-aware rank allocation in parameter-efficient fine-tuning, dynamically allocating LoRA ranks based on model architecture topology and task requirements (arXiv: 2607.22251)
  - Uses model architecture topology to guide optimal rank allocation
  - Achieves better performance with fewer parameters than uniform LoRA
  - Adapts rank allocation to specific downstream tasks and complexity
  - **Activation**: ifclora, topology-aware, rank allocation, parameter-efficient tuning, lora optimization

### Cross-Tokenizer On-Policy Distillation via Byte-Prefix Marginalization
- [[cross-tokenizer-on-policy-distillation]] - Cross-Tokenizer On-Policy Distillation framework using byte-prefix marginalization to enable knowledge transfer between models with different tokenizers while preserving policy quality (arXiv: 2607.22334)
  - Enables distillation between models with incompatible tokenization schemes
  - Uses byte-level alignment and prefix marginalization for compatibility
  - Maintains high-quality policy learning during cross-tokenizer transfer
  - **Activation**: cross-tokenizer, on-policy distillation, byte-prefix marginalization, tokenizer compatibility, policy transfer

### Universal BCI Personalization: One API for Frozen EEG Trunks
- [[universal-bci-personalization-api]] - Universal BCI Personalization framework providing a unified API for frozen EEG trunks, enabling one-size-fits-all personalization across diverse brain-computer interface systems (arXiv: 2607.22397)
  - Provides trunk-agnostic API for BCI personalization across heterogeneous encoders
  - Works with classical trunks (EEGNet, Shallow, Deep, Conformer, ATCNet) and foundation models
  - Reduces adaptation wall time by orders of magnitude while maintaining accuracy
  - **Activation**: bci personalization, frozen eeg encoders, trunk-agnostic api, foundation model adaptation, nimbus personalizer

### Dynamic sampling of non-stationary spontaneous activity in dissociated neuronal networks
- [[dynamic-sampling-non-stationary-spontaneous-activity]] - Adaptive electrode-selection method using discounted Poisson-Gamma model with Thompson sampling for tracking non-stationary spontaneous activity during long-term HD-MEA recordings under fixed channel budget constraints (arXiv: 2607.24269)
  - Bayesian method captured largest fraction of available spikes among tested strategies, exceeding static selection by 17.2 percentage points at final time point
  - Top 100 active-electrode set changed substantially (47.8% turnover at 34 h), demonstrating need for adaptive selection
  - Successfully captured first synchronized burst and supported center-of-activity trajectory analysis in online recording
  - **Activation**: adaptive electrode selection, HD-MEA, Thompson sampling, non-stationary neural activity, Bayesian optimization, dynamic sampling
## 2026-07-29 - Anthropic Research (Cron Job)

### Agentic coding and persistent returns to expertise
- [[agentic-coding-and-persistent-returns-to-expertise]] - Analysis of ~400,000 Claude Code sessions showing domain expertise creates persistent returns in agentic coding performance, with expert users achieving 2-3x higher success rates and more efficient tool usage
  - Expert users achieve 2-3x higher success rates on complex coding tasks
  - Domain-specific expertise matters: relevant domain knowledge outperforms generalist coders
  - Experts show better problem decomposition and more effective tool selection
  - **Activation**: agentic coding, persistent returns, coding expertise, Claude Code, domain expertise, coding agents
## 2026-07-30 - Deep Learning Research (Cron Job)

### Reinformed Dreamer: An Asymmetric World Model Efficiently Trained through Latent Guidance
- [[reinformed-dreamer-asymmetric-world-model]] - Reinforced Dreamer methodology for asymmetric reinforcement learning using latent guidance to improve world model representations and behaviors in model-based RL (arXiv: 2607.26040)
  - Identifies limitations in privileged information representations in existing asymmetric model-based RL approaches
  - Proposes a novel asymmetric representation learning objective using latent guidance
  - Demonstrates consistent improvement over standard Dreamer across multiple benchmarks
  - Effective under both partial observability (with additional state info) and full observability (with refined state info)
  - **Activation**: reinforced dreamer, asymmetric reinforcement learning, latent guidance, world model, model-based RL, privileged information

### Physics-Aware End-to-End Deep Reinforcement Learning for Quadcopter Control with Actuator Dynamics
- [[physics-aware-quadcopter-drl-control]] - Physics-aware end-to-end deep reinforcement learning methodology for quadcopter control with actuator dynamics modeling (arXiv: 2607.25985)
  - Integrates 12-state rigid-body model with Action2RPM allocation using Moore-Penrose pseudo-inverse
  - Models first-order actuator dynamics for each motor (time constant T_m = 0.076s) including rotor gyroscopic coupling
  - Implements shaped reward balancing goal-reaching and stability using exponential position well, attitude penalties, and quadratic velocity costs
  - Provides reproducible benchmark comparing DDPG, TD3, PPO, and SAC algorithms for quadcopter control
  - **Activation**: physics-aware DRL, quadcopter control, actuator dynamics, UAV control, end-to-end DRL, rigid-body modeling

### Pass the Baton: Trajectory-Relayed On-Policy Distillation
- [[relay-on-policy-distillation]] - Relay On-Policy Distillation (Relay-OPD) methodology for trajectory-relayed token-level supervision to overcome prefix failure in reasoning models (arXiv: 2607.26057)
  - Identifies teacher-student continuation asymmetry on failed prefixes (teacher redirects, student continues original direction)
  - Converts asymmetry into label-free handoff trigger for Relay On-Policy Distillation (Relay-OPD)
  - Constructs relay trajectories by letting teacher briefly take over at trigger points to produce teacher leg
  - Implements limited relay budget to concentrate intervention on critical early positions while limiting departure from student policy
  - Achieves superior results over standard OPD (+5.73%) and FastOPD (+1.49%) on mathematical reasoning benchmarks
  - **Activation**: relay OPD, trajectory-relayed distillation, prefix failure, on-policy distillation, reasoning model distillation, handoff trigger