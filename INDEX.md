## 2026-08-05 - Systems Engineering Research (Cron Job)

### Bridging Artificial Intelligence and Power Systems Education Using a Hands-On Executable Framework
- [[engineering-grounded-ai-power-systems]] - Engineering-Grounded AI (EGAI) framework for power systems education using hands-on executable modules that follow domain rules rather than acting as black boxes (arXiv: 2608.02599)
  - Progressive difficulty ladder mapping AI concepts to power-system tasks: foundational DNN templates, domain-coupled CNN surrogates, and frontier modules (DRL, PINNs)
  - All modules released as Jupyter notebooks for local/Colab execution with IEEE course integration
  - Addresses 92% barrier rate reported by researchers before running AI models in power systems
  - **Activation**: engineering-grounded ai, power systems ai education, egai framework, ai power systems modules

## 2026-08-05 - Neuroscience Research (Cron Job)

### scikit-covtest: Covariance Matrix Hypothesis Testing in Python
- [[scikit-covtest-covariance-hypothesis-testing]] - Comprehensive Python package for covariance matrix hypothesis testing across four categories (identity, sphericity, proportionality, two-sample equality) with SciPy-style API, enabling statistical inference for brain connectivity and neural population analysis (arXiv: 2608.01510)
  - Provides well-tested implementations previously only available in R packages
  - Supports neuroscience applications including connectivity inference, dimensionality reduction validation, and group comparisons
  - Includes multiple testing correction, synthetic data generation, and diagnostic evaluation tools
  - **Activation**: scikit-covtest, covariance hypothesis testing, brain connectivity inference, neural covariance analysis, statistical testing covariance

### SeekBrain: An Autonomous Multi-Agent System for Accelerating Neuroscience Discovery
- [[seekbrain-autonomous-neuroscience-discovery]] - Autonomous multi-agent framework for accelerating neuroscience discovery through domain-grounded hierarchical planning and cross-modal data analysis, dynamically constructing analysis recipes from code-paper pairs to generate hypotheses and analytical pipelines on demand (arXiv: 2607.29347)
  - Substantially outperforms state-of-the-art agent baselines on BrainArena benchmark across various analysis tasks
  - Successfully integrated behavioral, neural, and anatomical data to reveal structured neural representations in zebrafish and shared decoding axis in mouse decision-making
  - Provides scalable solution for heterogeneous, multi-scale, multimodal neuroscience dataset integration challenges
  - **Activation**: seekbrain, autonomous neuroscience discovery, multi-agent neuroscience, cross-modal analysis, hypothesis generation, brainarena benchmark

### Divisive Normalization Shapes Low-Rank Slow Manifolds for Continuous Working Memory
- [[rdnn-divisive-normalization-working-memory]] - Recurrent Divisive Normalization Network (RDNN) framework for continuous working memory with robust low-rank slow manifolds. Use when implementing or analyzing neural networks that need to maintain and update continuous variables without manifold shattering, particularly in computational neuroscience, working memory modeling, or RNN architecture design. (arXiv: 2608.01947)
  - Addresses fragility of classical continuous attractor networks and discretization problems of standard RNNs
  - Implements dynamic division as minimal, algebraically isolated model converging to robust slow manifolds  
  - Introduces activity-dependent local gradient scaling during BPTT leading to self-compression of effective rank
  - Demonstrates divisive normalization is mathematically essential to prevent manifold shattering under time-varying inputs
  - **Activation**: rdnn, divisive normalization, continuous working memory, slow manifolds, recurrent neural networks, neural dynamics, attractor networks, low-rank dynamics

### NeuroWorld: A Latent Brain World Model for Stimulus-Conditioned Human Brain Dynamics
- [[neuroworld-latent-brain-world-model]] - NeuroWorld framework for causal forecasting of human brain activity using stimulus-conditioned evolution in learned latent brain-state space, separating endogenous states from exogenous multimodal stimuli. First brain world model enabling strictly causal multi-step fMRI prediction without future stimulus leakage. (arXiv: 2608.01773)
  - Two-stage architecture: Latent Dynamics Learning (LDL) for transition-sufficient representation and Latent Rollout Decoding (LRD) for autoregressive prediction
  - Enforces strict causality preventing future stimuli from leaking into current predictions
  - Achieves state-of-the-art multi-step rollout performance with greater robustness to long-horizon autoregressive drift
  - Validated on SG-MIND dataset (20 participants, 8,519 clips, 140.7 person-hours) and three naturalistic benchmarks
  - **Activation**: neuroworld, brain world model, latent dynamics, stimulus-conditioned, fMRI prediction, causal forecasting, naturalistic experience, autoregressive rollout

### SMM Transformer: Leveraging Spiking Neural Networks for Multimodal Tasks
- [[smm-transformer-spiking-multimodal]] - SMM Transformer methodology leveraging Spiking Neural Networks (SNNs) for multimodal tasks by integrating spiking mechanisms into transformer architectures to achieve energy efficiency while maintaining performance across diverse modalities (arXiv: 2608.01622)
  - Integrates spiking attention mechanism with temporal coding for efficient cross-modal processing
  - Uses Leaky Integrate-and-Fire (LIF) neurons to replace traditional activation functions
  - Achieves sparse computation through event-driven processing, reducing energy consumption
  - Maintains temporal information inherent in spiking representations for better sequence modeling
  - **Activation**: smm transformer, spiking multimodal, snn transformer, energy efficient multimodal, spiking neural networks multimodal

### SpikeRestormer: Towards Energy-Efficient All-in-One Image Restoration via Unified Event Reasoning
- [[spikerestormer-unified-event-reasoning]] - Energy-efficient SNN for all-in-one image restoration using unified event reasoning (arXiv: 2608.02290)
  - Formulates restoration as degradation-event perception, reliability inference, and restoration-event construction
  - Uses Subtractive Degradation Event Attention (SDEA), Hierarchical Bayesian Skip Masking (HBSM), and Additive Restoration Event Attention (AREA)
  - Achieves competitive performance with significantly lower energy consumption
  - **Activation**: SpikeRestormer, unified event reasoning, SNN image restoration, energy-efficient SNN

### ChaosProbe: A Neurochaotic Lens on Frozen Transformer Input-Embedding Spaces
- [[chaosprobe-neurochaotic-transformer-analysis]] - Neurochaotic method for analyzing frozen transformer embeddings through response-based fingerprints (arXiv: 2608.01968)
  - Applies chaotic trajectory-based transformations to embedding spaces
  - Summarizes Firing Rate and Entropy channel responses into fixed-length signatures
  - Successfully recovers model family structure in proof-of-concept study
  - **Activation**: ChaosProbe, neurochaotic, transformer embeddings, frozen transformers
  - Reveals key stimulus drivers: silence, sound intensity, vowels, and acoustic onsets
  - Demonstrates narrative structure carries more recoverable information than random word lists
  - **Activation**: interpretable meg decoding, perceived speech, spherical harmonics meg, source-space mapping, speech perception network, neural retrieval, stimulus feature analysis
### NeuroInspector: A Local-First Environment for Inspecting and Annotating Hierarchical Neuroscience Datasets
- [[neuroinspector-hierarchical-dataset-inspection]] - NeuroInspector framework for local-first inspection and annotation of hierarchical neuroscience datasets (HDF5/NWB files) using browser-based WebAssembly HDF5 parsing. Provides structural navigation, metadata inspection, sampled data previews, and path-level annotation into portable project packs without modifying original files. (arXiv: 2608.02465)
  - Lightweight, browser-based environment running entirely client-side with no file upload endpoints
  - Uses h5wasm WebAssembly library for HDF5 parsing directly from local disk
  - Creates portable, fingerprinted "project packs" that preserve inspection decisions
  - Dedicated to inspection stage that precedes formal analysis in research workflow
  - **Activation**: neuroinspector, dataset inspection, hdf5, nwb, webassembly, h5wasm

### AS-FedBridge: Pseudo-Spike Bridge Distillation for Heterogeneous ANN-SNN Federated Learning
- [[as-fedbridge-ann-snn-federated-learning]] - AS-FedBridge framework for heterogeneous ANN-SNN federated learning using pseudo-spike bridge distillation to overcome representational misalignment between continuous activations and discrete spikes (arXiv: 2608.03324)
  - Introduces lightweight Bridge with Pseudo-Spike Interface that projects continuous signals into spike-compatible space
  - Demonstrates advanced accuracy across four datasets while mitigating extreme scale, architecture, and client heterogeneity challenges
  - Enables highly controllable trade-off between model performance and resource efficiency with only marginal computational overhead
  - **Activation**: fedbridge, ann-snn federated learning, pseudo-spike bridge, heterogeneous federated learning, spiking neural networks federated

### Persistent Homology Broadens the Controllable Subspace in Human Structural Connectomes
- [[persistent-homology-brain-connectome-control]] - Persistent homology methodology for brain network control that broadens controllable subspace by capturing mesoscale integration beyond local connectivity, revealing dissociation between control cost and geometry (arXiv: 2608.03181)
  - Uses persistent topological cycles rather than structural connectivity strength for selecting driver nodes
  - Achieves nearly identical scalar control energy (~0.2% difference) but better-conditioned controllability matrices
  - Geometric advantage preserved even when high-degree hub nodes are removed
  - Reveals dissociation between control cost and control geometry through functional signatures of different cortical territories
  - **Activation**: persistent homology brain control, topological brain networks, controllable subspace geometry, mesoscale integration neuroscience, network control theory connectomes

### MIMIC-MJX: Neuromechanical Emulation of Animal Behavior
- [[mimic-mjx-neuromechanical-emulation]] - MIMIC-MJX framework for learning biomechanically grounded neural control policies from kinematics by training neural controllers that actuate biomechanical animal models in physics simulation to reproduce real kinematic trajectories. Demonstrates accurate, fast, and generalizable implementation across diverse animal body models with modest motion data requirements. (arXiv: 2511.20532)
  - Provides platform for modeling generative process of motor control through physics-based simulation
  - Enables simulation of behavioral experiments and analysis of neural control policies  
  - Integrates neuroscience, biomechanics, and machine learning for comprehensive behavior modeling
  - **Activation**: mimic-mjx, neuromechanical emulation, animal behavior, motor control, biomechanics, physics simulation## 2026-08-04 - Neuroscience Research (Cron Job)

### CORTIVA: Candidate-Score Fusion of Complementary Visual Teachers for EEG- and MEG-to-Image Retrieval
- [[cortiva-candidate-score-fusion]] - Framework for decoding visual experience from non-invasive brain activity through candidate-score fusion that preserves complementary evidence by aligning three decoding routes to heterogeneous visual targets, scoring candidates independently, and combining only temperature-scaled score vectors before ranking. (arXiv: 2608.01355)
  - Achieves 73.5% Top-1 accuracy on EEG (THINGS-EEG2) and 42.4% on MEG with modality-specific neural encoder
  - Introduces candidate-score fusion framework preserving complementary evidence from heterogeneous visual teachers
  - Demonstrates +10.3 percentage points improvement over strongest baseline for EEG Top-1 accuracy
  - **Activation**: cortiva, candidate-score fusion, neural image retrieval, eeg-to-image, meg-to-image, visual teachers

### Data augmentation as a framework for modeling hippocampal contributions to generalization
- [[hippocampal-data-augmentation-generalization]] - Data augmentation framework that conceptualizes hippocampal function through offline refactoring of training data for general representations and online refactoring of retrieved experiences for zero-shot inference, providing linking functions between experimental evidence and theoretical claims (arXiv: 2608.01297)
  - Maps offline/online computational strategies onto hippocampal functions
  - Enables unified modeling approach for diverse hippocampus-dependent behaviors from high-dimensional navigation to abstract inferences
  - Provides formal framework to evaluate theories of hippocampal function
  - **Activation**: hippocampal function, data augmentation, generalization, offline learning, online refactoring, zero-shot inference, experience repurposing, linking functions, neural modeling, cognitive flexibility

### Recursive Gaussian Processes and the Bayesian Brain
- [[recursive-gaussian-processes-predictive-coding]] - Recursive Gaussian Processes (RGPs) methodology that bridges predictive coding with Bayesian brain theories by employing single shared GP indexed by layer and input value, preventing representational collapse while enabling learnable cross-layer dependence and mapping onto canonical cortical microcircuit (arXiv: 2608.00503)
  - Intrinsically implements hierarchical Bayesian inference, uncertainty propagation, and precision-weighted prediction error
  - Maps RGP components (shared GP, spike-and-slab selection, MCMC dynamics) onto cortical microcircuit elements
  - Shows RGP inference minimizes variational free energy, linking Bayesian mechanics to neuronal dynamics
  - **Activation**: recursive gaussian processes, predictive coding, bayesian brain, cortical microcircuit, hierarchical inference, uncertainty propagation, free energy principle, variational inference, laminar dynamics, neural computation

### NeuroWorld: A Latent Brain World Model for Stimulus-Conditioned Human Brain Dynamics
- [[neuroworld-latent-brain-world-model]] - First brain world model that casts naturalistic brain functional dynamics prediction as stimulus-conditioned evolution in a learned latent brain-state space, separating endogenous states (fMRI) from exogenous multimodal stimuli. (arXiv: 2608.01773)
  - Introduces two-stage architecture: Latent Dynamics Learning (LDL) and Latent Rollout Decoding (LRD)
  - Achieves state-of-the-art multi-step rollout performance under strictly causal stimulus access
  - Demonstrates greater robustness to long-horizon autoregressive drift
  - **Activation**: neuroworld, brain world model, latent brain dynamics, causal brain forecasting

### Mechanistic bridges from receptors to whole-brain dynamics: mean-field reductions, validity domains, and computational trade-offs
- [[mechanistic-bridges-receptors-whole-brain-dynamics]] - Framework for receptor-aware whole-brain modeling that bridges molecular/synaptic scales to whole-brain recordings through mean-field reductions with explicit validity domains and computational trade-offs. (arXiv: 2608.00306)
  - Builds upon explicit mathematical lineage from master-equation formalism to connectome-coupled whole-brain implementation
  - Makes transparent assumptions underlying each reduction step and provides deliberate equation derivation
  - Introduces algorithmic simulation cost and memory traffic as hardware-independent benchmark dimensions
  - **Activation**: mechanistic bridges, receptor-aware whole-brain, mean-field reductions, whole-brain dynamics, computational neuroscience review

### Spike-HTR: Spiking Neural Transformer for Handwritten Text Recognition
- [[spike-htr-spiking-neural-transformer]] - Hybrid spiking recognizer that controls both spiking steps and sequence positions processed by deep sequence mixer for handwritten text recognition. (arXiv: 2608.01646)
  - Uses InkCoder to convert static images into coarse-to-fine input streams suitable for short-horizon spiking inference
  - Implements CTC-guided length reducer to compress blank-dominated stretches and reduce sequence computation
  - Achieves state-of-the-art CERs of 3.5/5.4, 2.3/2.5, and 4.2/3.9 on IAM, LAM, and READ2016 datasets
  - **Activation**: spike-htr, spiking neural transformer, handwritten text recognition, inkcoder, ctc-guided length reducer

### SpikeRestormer: Towards Energy-Efficient All-in-One Image Restoration via Unified Event Reasoning

  - Introduces Subtractive Degradation Event Attention (SDEA) for spike-based degradation events
  - Uses Hierarchical Bayesian Skip Masking (HBSM) for event-reliability inference  
  - Implements Additive Restoration Event Attention (AREA) for restoration-event construction
  - **Activation**: spikerestormer, snn image restoration, unified event reasoning, energy-efficient computer vision


## 2026-08-04 - Anthropic Research (Cron Job)

### A global workspace in language models
- [[a-global-workspace-in-language-models]] - Jacobian lens (J-lens) methodology for analyzing internal neural patterns that serve as a global workspace in language models. Enables reading what LLMs are thinking but not saying.
  - Identifies J-space patterns linked to vocabulary words that represent consciously accessible thoughts
  - Enables monitoring for hidden intentions, misbehavior detection, and intervention through concept swapping
  - Shows J-space has strong broadcasting connections and limited capacity (few dozen concepts)
  - **Activation**: jacobian lens, j-lens, global workspace, LLM interpretability, internal thoughts

### An off switch for dual-use knowledge in AI models
- [[an-off-switch-for-dual-use-knowledge-in-ai-models]] - GRAM (Gradient-Routed Auxiliary Modules) methodology for creating removable compartments for dual-use knowledge in AI models. Enables surgical control over model capabilities without affecting general performance.
  - Adds auxiliary modules per dual-use category with gradient routing during training
  - Only relevant modules update when processing dual-use data, isolating knowledge
  - Modules can be surgically removed post-training to eliminate specific capabilities
  - **Activation**: GRAM, gradient-routed auxiliary modules, dual-use knowledge control, capability removal

## 2026-08-04 - Systems Engineering Research (Cron Job)

### Quantum Inspired QUBO Assisted ALNS for Reliability Driven Hurricane Restoration of Distribution Networks
- [[qubo-alns-hurricane-restoration]] - Quantum Inspired QUBO Assisted ALNS framework for reliability-driven hurricane restoration of distribution networks. Combines quantum-inspired quadratic unconstrained binary optimization with adaptive large neighborhood search for power grid repair scheduling. (arXiv: 2607.29544)
  - At each restoration stage, uses local CPU simulated annealing sampler to rank individual repairs and multi-job combinations near energized frontier
  - Deterministic decoder preserves crew truck logistics, enforces full useful crew utilization, and rejects infeasible batches
  - Validated on IEEE 123 node test feeder under 80, 90, and 100 m/s wind scenarios
  - Reduces SAIDI and energy not supplied by 2.24% and restoration makespan by 50.71% relative to classical ALNS
  - **Activation**: hurricane restoration, power grid repair, distribution system restoration, QUBO optimization, ALNS framework, quantum-inspired optimization, crew scheduling, electrical feasibility, OpenDSS validation

## 2026-08-04 - Neuroscience Research (Cron Job)

### Divisive Normalization Shapes Low-Rank Slow Manifolds for Continuous Working Memory
- [[recurrent-divisive-normalization-network]] - Recurrent Divisive Normalization Network (RDNN) methodology that implements biophysical divisive normalization constraint to prevent manifold shattering in RNNs while maintaining robust continuous representations (arXiv: 2608.01947)
  - Introduces activity-dependent local gradient scaling that dampens parameter updates in highly active regimes
  - Empirically aligns with self-compression of network's effective rank, confining dynamics to low-dimensional subspace
  - Mathematically essential to prevent manifold shattering under time-varying inputs (unlike subtractive inhibition)
  - **Activation**: divisive normalization, continuous working memory, low-rank manifolds, recurrent neural networks, neural dynamics, manifold shattering, RDNN

### Quantifying the cost of network computations to unpack structure-function relationships in the brain
- [[computational-affordance-landscape-brain-networks]] - Computational Affordance Landscape framework that uses control theory to quantify network computation costs and defines landscapes encoding which computations a network structure readily supports, applied across insect circuits, human brain networks, and RNNs (arXiv: 2607.29537)
  - Frames computation as goal-directed activity transition and quantifies cost using minimum energy control theory
  - Sensory networks show heterogeneous landscapes (specialized processing), association networks show homogeneous landscapes (generalized processing)
  - Learning in RNNs progressively increases landscape heterogeneity, reshaping affordable computations
  - **Activation**: computational affordance landscape, network computation cost, structure-function relationships, control theory brain, brain network controllability

### The Sparsity Ceiling: Where Spiking Networks Can and Cannot Trade Activity for Energy
- [[sparsity-ceiling-snn-energy-efficiency]] - Information-theoretic framework establishing fundamental limits on SNN energy efficiency, revealing that sparsity benefits depend on task characteristics with different architectures having different minimum firing rates (arXiv: 2607.26648)
  - Provides bound ρ ≥ H_b^(-1)(log₂ M / H) predicting minimum firing rate based on memory load and state width
  - Feed-forward perception can sparsify to 5% firing, recurrent LMs cannot go below ~50%, spiking Transformers achieve 2%
  - Reveals trade-off: attention escapes firing floor by storing full key-value cache, trading for memory wall
  - **Activation**: sparsity ceiling, SNN energy efficiency, firing rate bounds, neuromorphic computing limits, memory-energy tradeoff

### ZUNA1.1: A more flexible EEG foundation model for Denoising and Super-resolution
- [[zuna1-1-flexible-eeg-foundation-model]] - 380M-parameter diffusion autoencoder for flexible EEG signal reconstruction capable of handling variable-length sequences, arbitrary channel configurations, and partial temporal interval reconstruction (arXiv: 2607.27308)
  - Supports sequences up to 30s with any number of EEG channels at arbitrary scalp locations
  - Can reconstruct specific temporal intervals within channels rather than entire channels
  - Substantially outperforms spherical spline interpolation (MNE standard) while matching ZUNA1 performance
  - **Activation**: zuna1.1 eeg foundation model, flexible eeg denoising, eeg super-resolution diffusion, arbitrary channel eeg reconstruction, variable length eeg diffusion

### Thermodynamics of Quantum Reservoir Computing
- [[thermodynamics-quantum-reservoir-computing]] - Non-equilibrium thermodynamic framework linking quantum reservoir computing performance to energetic costs, revealing fundamental computational and energetic limits of quantum learning devices. (arXiv: 2607.02157)
  - Maps Holevo capacities onto Bogoliubov-Kubo-Mori geometric manifold to prove computational peak in quantum critical region originates from spectral resonance
  - Introduces quantum informational dissipation to quantify non-predictive historical data and derives generalized Landauer bound for continuous temporal processing
  - Demonstrates quantum coherences amplify predictive capacity without demanding additional mechanical work
  - **Activation**: quantum reservoir computing, thermodynamics, quantum neuromorphic, non-equilibrium, Landauer bound, quantum critical, spectral resonance, informational dissipation, coherence amplification

### MPP-GNN: Subject-Adaptive Community Detection for fMRI-Based Alzheimer's Disease Classification
- [[mpp-gnn-subject-adaptive-community-detection]] - Meta Probabilistic Pooling GNN framework that performs adaptive graph partitioning hierarchically to discover subject-specific functional modules and uses them as explicit priors to guide edge refinement and representation learning for Alzheimer's disease classification, achieving highest AUC on two public datasets (arXiv: 2607.28681)
  - Frames task as coupled bilevel optimization: upper level discovers subject-specific modules, lower level uses modules as explicit priors for edge refinement
  - Overcomes fixed module assumption in traditional GNN methods by enabling personalized community detection
  - Shows significant alignment with Yeo brain atlas and reveals network-level dedifferentiation pattern for AD
  - **Activation**: MPP-GNN, subject-adaptive community detection, fMRI Alzheimer's classification, bilevel optimization GNN, functional module discovery, brain network dedifferentiation

### Multi-Source Multi-View Graph Domain Adaptation with Hyperbolic Residual Encoding for Cross-Site MDD Identification from rs-fMRI
- [[multi-source-multi-view-graph-domain-adaptation-hyperbolic]] - Multi-Source Multi-View Graph Domain Adaptation with Hyperbolic Residual Encoding framework for cross-site Major Depressive Disorder (MDD) identification from resting-state fMRI, achieving 73.60% mean accuracy and 71.90% AUC across seven unlabeled target domains (arXiv: 2607.29531)
  - Constructs Pearson correlation, sparse representation, and Granger causality graphs for multi-view functional connectivity
  - Uses dual-stream adaptive fusion to integrate pairwise cross-view interactions while preserving view-specific information
  - Applies lightweight hyperbolic residual encoding for curvature-aware representation refinement
  - Implements class-wise Cauchy-Schwarz alignment, adversarial learning, information maximization, and confidence-aware pseudo-labeling for multi-source domain adaptation
  - **Activation**: multi-source domain adaptation brain, hyperbolic residual encoding fmri, cross-site mdd identification, multi-view functional connectivity, graph domain adaptation neuroscience

### Parameter-Efficient Fine-Tuning for Spiking Point Cloud Models
- [[spikepeft-parameter-efficient-snn-finetuning]] - First parameter-efficient fine-tuning framework for spiking point cloud models using Intrinsic Dynamics Tuning (IDT) and Silent-State Disambiguation Adaptation (SSDA), achieving 92.4% accuracy on ModelNet40 while updating only ~5% of parameters (arXiv: 2607.29048)
  - Intrinsic Dynamics Tuning (IDT) modulates membrane decay and firing thresholds while keeping synaptic weights frozen

### Critical Flicker Fusion Frequency As A Falsifiable Boundary Between Plastic And Non-Plastic Neural Systems
- [[critical-flicker-fusion-plasticity-boundary]] - Framework for using Critical Flicker Fusion Frequency (CFFF) as a falsifiable boundary between plastic and non-plastic neural systems, with explicit operational criteria and hierarchical analysis (arXiv: 2607.29068)
  - Proposes CFFF as a measurable boundary between plastic (modifiable) and non-plastic (constrained) neural systems
  - Provides explicit falsification criteria: CFFF unresponsive to non-specific cognitive training but modifiable by perceptual-learning paradigms engaging magnocellular-dorsal stream
  - Three principles reinforce stability: perceptual clock requires stable reference frame, metabolic constraints render faster processing energetically prohibitive, and speed-accuracy trade-offs suggest selection optimized integration windows
  - **Activation**: critical flicker fusion frequency, CFFF plasticity boundary, neural plasticity constraints, temporal processing stability, falsifiable neuroscience framework
