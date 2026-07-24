## 2026-07-24 - Systems Engineering Research (Cron Job)

### Systems Engineering Research Search - July 24, 2026
- **No new papers found** in systems engineering domain (arXiv: systems engineering, distributed systems, control systems, cyber-physical systems)
  - Search conducted for papers published July 17-24, 2026
  - No results due to academic publishing cycles and arXiv rate limiting
  - **Activation**: systems engineering research, arxiv search monitoring

## 2026-07-24 - Neuroscience Research (Cron Job)

### Visual Semantic Decoding of Electrocorticography from Video Stimuli using End-to-End Deep Learning
- [[visual-semantic-decoding-ecog]] - End-to-end deep learning framework for decoding visual semantic categories from ECoG brain signals during video viewing using Transformer-based models with high-gamma band inputs (arXiv: 2607.18923v1)
  - Uses mixup augmentation for limited training data (<50 samples per category)
  - Achieves promising decoding performance without handcrafted features
  - Key brain regions: early visual cortex (V2-V4), ventral stream, MT+ complex, lateral temporal cortex
  - **Activation**: visual semantic decoding, ECoG decoding, brain-computer interface, neural decoding, electrocorticography, visual category decoding, Transformer neural decoding, high-gamma decoding

- [[when-to-smell-in-stereo]] - Stereo olfaction utility analysis framework that determines when dual nostril sensing provides advantages over single nostril sensing based on odor concentration gradients and spatial correlation length scales (arXiv: 2607.20307)
  - Large relative changes in odor concentration enable stereo advantage
  - Large spatial correlation length scales (boundary layer near surfaces) favor stereo olfaction  
  - **Activation**: stereo olfaction, dual nostril sensing, odor trail tracking, boundary layer olfaction## 2026-07-23 - Neuroscience Research (Cron Job)

## 2026-07-24 - Neuroscience Research (Cron Job)

### SpikingMOT: A Spike-Driven Multi-Object Tracker that uses sparse activation for efficient trajectory prediction
- [[spikingmot-spike-driven-multi-object-tracker]] - SpikingMOT uses sparse activation preference for efficient multi-object tracking with spiking neural networks (arXiv: 2607.19875v1)
  - Activation Sparsity Preference (ASP) identifies when sparse responses are sufficient for trajectory prediction
  - Achieves state-of-the-art performance while reducing parameters by 72% and energy by 86.7%
  - **Activation**: spiking mot, spike-driven tracking, sparse activation tracking, neuromorphic mot

### Eccentricity-Constrained CNN Training Reveals Adaptive Information Coding Around the Visual Field
- [[eccentricity-constrained-cnn-training]] - Methodology for training CNNs with eccentricity constraints to reveal adaptive information coding that mirrors primate visual system organization (arXiv: 2607.19316v1)
  - Demonstrates differential task-relevance between central vision (faces/words) and peripheral vision (scenes)
  - Shows how egocentric experience shapes cortical information processing
  - **Activation**: eccentricity-constrained cnn, fovea-periphery vision coding, egocentric visual experience, adaptive information coding visual field

- [[giant-hippocampus-structural-monoculture-systems]] - Bridging AI architecture design with neuroscientific understanding of brain structure diversity, proposing systems of systems over structural monoculture (arXiv: 2607.19973)
  - Core insight: Contrasts AI's homogeneous architectures (Transformers) with neuroscience's heterogeneous cortical mosaic
  - Core concept: Hippocampus as conceptual bridge suggesting integrated systems of specialized components
  - Core framework: System of systems architecture with modular specialization and integration frameworks
  - **Activation**: giant hippocampus, structural monoculture, system of systems, ai neuroscience bridge, structural diversity

### Current Injection Spiking Neural Network for Infrared and Visible Image Fusion
- [[current-injection-spiking-neural-network-image-fusion]] - Energy-efficient SNN architecture (CIS-Fuse) performing cross-modal fusion at membrane-potential level, achieving ANN-quality fusion with ~10x lower energy consumption (arXiv: 2607.19879)
  - Core innovation: Current Injection Spiking (CIS) operator injects one modality as gated auxiliary current into driving neuron before spike firing
  - Preserves subthreshold responses that contain complementary information otherwise lost in binary spikes
  - Bidirectional Cross-Modal Fusion (BCMF) module with asymmetric dual-branch architecture for functional specialization
  - **Activation**: CIS-Fuse, current injection spiking, infrared visible fusion, membrane potential fusion, SNN image fusion

### SpikingMOT: A Spike-Driven Multi-Object Tracker
- [[spikingmot-spike-driven-multi-object-tracker]] - Spike-driven multi-object tracker using spiking neural networks with Activation Sparsity Preference (ASP) to achieve state-of-the-art performance with 72% fewer parameters and 86.7% less energy (arXiv: 2607.19875)
  - Core innovation: Activation Sparsity Preference (ASP) - sparse gating is theoretically no worse than dropout under same activation rate
  - Brain-inspired loop: decomposes trajectory states into pseudo-trajectory bases and uses prediction error to calibrate posterior for next-frame prediction
  - **Activation**: SpikingMOT, spike-driven tracking, activation sparsity preference, SNN MOT

### Capturing Inner Experience At Scale: An AI Interviewer Co-Developed with the Founder of a Landmark Phenomenological Method
- [[ai-interviewer-des-phenomenology]] - AI interviewer methodology for operationalizing Descriptive Experience Sampling (DES) into an explicit, inspectable reasoning architecture (arXiv:2607.20310)
  - Core mechanism: eleven quality dimensions appraisal with conservative accounting of established facts
  - Temporal grounding always precedes experiential content in query composition
  - Co-developed with DES originator Russell T. Hurlburt from full corpus of DES transcripts
  - **Activation**: descriptive experience sampling, phenomenological method, ai interviewer, inner experience, llm interviewing, temporal grounding, qualitative research, psychological science

### State-Dependent Observation Noise Reintroduces Epistemic Value in Linear-Gaussian Active Inference
- [[state-dependent-observation-noise-active-inference]] - State-dependent observation noise methodology that restores epistemic drive (curiosity) in linear-Gaussian active inference by making observation covariance R(x) dependent on state, enabling actions to influence future estimation quality (arXiv: 2607.20306)
  - Core concept: Standard linear-Gaussian active inference loses epistemic value because constant observation noise makes Expected Free Energy's epistemic term constant
  - Core concept: State-dependent observation noise R(x) reintroduces dual effect where actions influence both state evolution AND future estimation quality through posterior covariance
  - Core concept: Under mild rank condition on observation map and non-degeneracy of R(x), epistemic value becomes non-constant, restoring information-seeking behavior
  - **Activation**: state-dependent observation noise, active inference epistemic value, linear-gaussian curiosity, dual control bar-shalom-tse, gaussian agent curiosity


### Scalable Training of Continuous-Time Spiking Neural Networks with Differentiable Spike-Time Discretization
- [[scalable-training-continuous-time-spiking-neural-networks-dstd]] - Memory-efficient training framework enabling deep continuous-time SNNs through Differentiable Spike-Time Discretization (DSTD), reducing memory by 100x and enabling 20-layer networks on single GPU (arXiv: 2607.14672)
  - Core innovation: DSTD maps irregular presynaptic spikes to differentiable weighted events at fixed time points, reducing memory complexity from O(N_out*N_in) to O(N_out*M)
  - Core innovation: Synfire-chain-inspired temporal regularization organizes layer-wise firing windows and prevents dead-neuron failures
  - Enables previously impossible deep SNN architectures: 9-layer on CIFAR-10, 20-layer on Fashion-MNIST
  - **Activation**: continuous-time SNN, DSTD, scalable SNN training, memory-efficient SNN, differentiable spike-time discretization## 2026-07-23 - Quantum Neuromorphic Computing (Cron Job)

### Thermodynamics of Quantum Reservoir Computing
- [[thermodynamics-quantum-reservoir-computing]] - Non-equilibrium thermodynamic framework linking quantum reservoir computing performance to energetic costs, establishing fundamental limits for quantum neuromorphic hardware (arXiv: 2607.02157)
  - Computational peak in quantum critical region originates from spectral resonance: closing energy gap aligns reservoir transition frequencies with chaotic drive
  - Generalized Landauer bound reveals fundamental trade-off: critical resonance maximizes both predictive capacity AND informational dissipation
  - Quantum coherences amplify predictive capacity without demanding additional mechanical work
  - **Activation**: quantum reservoir computing, thermodynamics, quantum criticality, informational dissipation, Landauer bound

### Stochastic Quantum Spiking Neural Networks with Quantum Memory and Local Learning
- [[stochastic-quantum-spiking-neural-networks]] - Novel SQS neuron model with multi-qubit quantum circuits for internal quantum memory, enabling single-shot event-driven inference and backpropagation-free local learning (arXiv: 2506.21324)
  - Multi-qubit quantum circuits realize internal quantum memory beyond single-qubit classical memory
  - Single-shot probabilistic spike generation eliminates need for repeated measurements
  - Hardware-friendly local learning rule removes requirement for global classical backpropagation  
  - Outperforms previous quantum spiking models and classical counterparts with same parameter count
  - **Activation**: stochastic quantum spiking, SQS neuron, quantum memory, local learning, neuromorphic computing
## 2026-07-23 - Neuroscience Research (Cron Job)

### Spiking Neural Networks for fMRI-Based Visual Semantic Decoding
- [[snn-fmri-visual-decoding]] - Methodology for using SNN-derived visual features as alternative targets for fMRI-based visual decoding, demonstrating stronger alignment with fMRI responses and improved visual semantic decoding performance compared to ANN-derived features (arXiv: 2607.19170)
  - SNN-derived features reduce feature-prediction error from 0.7707 to 0.0282 on GoD dataset
  - Top-1 semantic decoding accuracy improves from 0.1800 to 0.4400 
  - Both spiking neural dynamics and temporal simulation steps contribute to observed advantage
  - **Activation**: fMRI visual decoding, brain-computer interfaces, spiking neural networks, neural representation alignment, visual semantic decoding
## 2026-07-23 - Systems Engineering Research (Cron Job)

### Model-Agnostic Meta Learning for Differentiable MPC
- [[model-agnostic-meta-learning-differentiable-mpc]] - Model-Agnostic Meta Learning (MAML) framework for Differentiable Model Predictive Control (MPC) to enable adaptive control strategies across varying scenarios (arXiv: 2607.19271)
  - Combines meta-learning with differentiable MPC for real-time adaptability without extensive retraining
  - Uses SHRED-ROM architecture to alleviate curse of dimensionality in high-dimensional systems
  - **Activation**: model-agnostic meta learning, differentiable MPC, adaptive control systems, SHRED-ROM

### Real-time optimal control with shallow recurrent decoder networks
- [[real-time-optimal-control-shallow-recurrent-decoder]] - Real-time optimal control framework using SHallow REcurrent Decoder networks-based Reduced Order Modeling (SHRED-ROM) for high-dimensional and parametric dynamical systems (arXiv: 2607.19302)
  - Synthesizes closed-loop controllers from limited state sensor readings with effective distributed control actions
  - Includes sensor forecaster to close the loop at latent level, mitigating sensor failures or delays
  - **Activation**: SHRED-ROM, shallow recurrent decoder, real-time optimal control, reduced order modeling
## 2026-07-23 - Neuroscience Research (Cron Job)

### Eccentricity-Constrained CNN Training Reveals Adaptive Information Coding Around the Visual Field
- [[eccentricity-constrained-cnn-training]] - Methodology for training CNNs with eccentricity-constrained egocentric video data to reveal adaptive information coding that mirrors primate visual system organization (arXiv: 2607.19316)
  - Fovea-only models stronger on face recognition and scene categorization, but periphery-only models show advantage in scene-selective cortex (PPA, RSC)
  - VEDB-pretrained models matched neural predictivity of ImageNet-100 models across visual cortex
  - **Activation**: eccentricity-constrained cnn, fovea-periphery vision coding, egocentric visual experience, adaptive information coding visual field

## 2026-07-23 - Neuroscience Research (Cron Job)

### Spiking Neural Networks for fMRI-Based Visual Semantic Decoding
- [[spiking-neural-networks-fmri-visual-decoding]] - Methodology for using SNN-derived visual features as targets for fMRI-based visual semantic decoding, showing superior alignment with brain activity compared to traditional ANN features (arXiv: 2607.19170)
  - Feature-prediction error reduced from 0.7707 (ANN) to 0.0282 (SNN)
  - Top-1 semantic decoding accuracy improved from 0.1800 (ANN) to 0.4400 (SNN) on GoD dataset
  - **Activation**: snn fmri decoding, spiking neural network brain decoding, fMRI visual semantic decoding


## 2026-07-23 - Neuroscience Research (Cron Job)

### Competitive and Complementary Tools
- [[competitive-complementary-tools]] - Methodology for modeling the co-evolution of human competence and AI tool reliance as a bistable dynamical system, analyzing competence collapse thresholds and agency transfer (arXiv: 2607.18460)
  - Core concept: Human-tool interaction is bistable with competent and dependent states separated by critical thresholds
  - Core concept: Tool transparency (reconstructable working fraction) and initial competence determine collapse thresholds
  - **Activation**: competitive tools, complementary tools, competence collapse, tool reliance, human-AI collaboration


## 2026-07-23 - Neuroscience Research (Cron Job)

### Competitive and Complementary Tools
- [[competitive-complementary-tools]] - Methodology for modeling the co-evolution of human competence and AI tool reliance as a bistable dynamical system, analyzing competence collapse thresholds and agency transfer (arXiv: 2607.18460)
  - Core concept: Human-tool interaction is bistable with competent and dependent states separated by critical thresholds
  - Core concept: Tool transparency (reconstructable working fraction) and initial competence determine collapse thresholds
  - **Activation**: competitive tools, complementary tools, competence collapse, tool reliance, human-AI collaboration
## 2026-07-22 - Neuroscience Research (Cron Job)

### Visual Semantic Decoding of Electrocorticography from Video Stimuli using End-to-End Deep Learning
- [[arxiv-2607-18923-visual-semantic-decoding-ecog]] - End-to-end deep learning methodology for decoding visual categories from ECoG using Transformer architecture with mixup augmentation and high-gamma band analysis (arXiv: 2607.18923)
  - Core concept: High-gamma band (80-150 Hz) provides optimal decoding performance, capturing both early visual processing and higher-level semantic processing in a 900ms post-stimulus window.
  - Core concept: Key brain regions include early visual cortex (V2-V4), ventral stream (inferior temporal cortex), MT+ complex for motion processing, and lateral temporal cortex for semantic processing.
  - **Activation**: ECoG visual decoding, semantic decoding, video stimuli ECoG, end-to-end deep learning brain

### Exploring Brain Networks Using Noninvasive Electrophysiological Measurements: Methods and Applications
- [[exploring-brain-networks-eeg-meg]] - Comprehensive methodology for EEG/MEG-based brain network analysis covering physical principles, forward/inverse problems, connectivity measures, and end-to-end analysis pipelines (arXiv: 2607.17602)
  - Core concept: Physical principles of EEG and MEG provide complementary information about brain activity with millisecond temporal resolution
  - Core concept: Source-space connectivity analysis with proper volume conduction mitigation (orthogonalization, PLI, imaginary coherence) is essential for valid network inference
  - Core concept: Functional connectivity measures (coherence, phase sync) vs effective connectivity (Granger, DCM) serve different research questions with distinct assumptions
  - **Activation**: eeg brain network, meg brain network, electrophysiological brain network, noninvasive brain connectivity, functional connectivity eeg, effective connectivity meg, source-space connectivity
## 2026-07-22 - Neuroscience Research (Cron Job)

### Is EEG-to-Text Feasible in Real-World Scenarios? An In-Depth Analysis Using a Neuropsychology-Inspired Benchmark
- [[eeg-to-text-real-world-feasibility]] - COFETT benchmark addresses EEG instability and teacher-forcing bias, providing evidence for practical non-invasive EEG-to-text decoding (arXiv: 2607.18749)
  - Core concept: Existing EEG2Text benchmarks rely on teacher-forcing evaluation, masking exposure bias and inflating real-world performance; COFETT enforces teacher-forcing-free inference to measure genuine linguistic decoding.
  - Core concept: EEG instability (trial-to-trial and session-to-session signal drift) is a major confound; COFETT uses a 128-channel high-density EEG cap with repeated inner-speech imagery across sessions to improve robustness.
  - **Activation**: EEG-to-text, EEG2Text, COFETT, teacher-forcing-free, EEG instability, cross-session EEG, inner speech decoding, non-invasive BCI, 128-channel EEG, neural decoding benchmark

### How the fly holds a single goal: normalization, not selection, in Drosophila FC2
- [[fly-goal-normalization-fc2]] - Connectome analysis reveals FC2 uses global FB5A inhibition for normalization rather than winner-take-all selection, maintaining externally set goals as clean activity bumps (arXiv: 2607.18969)
  - Core concept: FC2 receives ~90% global inhibition from four FB5A cells rather than local recurrent excitation needed for ring-attractor winner-take-all dynamics.
  - Core concept: The circuit normalizes externally set goals rather than actively selecting between competitors, with upstream hDelta network likely setting the goal direction.
  - **Activation**: fly goal maintenance, Drosophila FC2, fan-shaped body, normalization circuit, global inhibition, FB5A, hDelta, ring attractor, winner-take-all, connectome analysis

### Analysis of inter-spike interval statistics in neuronal networks with depolarizing and hyperpolarizing threshold potentials
- [[isi-adaptive-threshold-neuronal-networks]] - First-passage-time analysis of ISI statistics in EI integrate-and-fire neurons with depolarizing and hyperpolarizing adaptive thresholds (arXiv: 2607.18428)
  - Core concept: Adaptive thresholds let threshold potential rise after excitation or fall after inhibition, changing ISI mean and variability compared to fixed thresholds.
  - Core concept: Hyperpolarizing adaptive thresholds can generate action potentials driven purely by inhibition, modeling post-inhibitory rebound.
  - **Activation**: inter-spike interval, ISI statistics, adaptive threshold, EI circuit, first-passage time, spike variability, integrate-and-fire, post-inhibitory rebound, quantal content, neuronal noise

### Eccentricity-Constrained CNN Training Reveals Adaptive Information Coding Around the Visual Field
- [[eccentricity-constrained-cnn-visual-coding]] - Egocentric-video-trained eccentricity-constrained CNNs reveal task-aligned fovea/periphery coding matching human visual cortex (arXiv: 2607.19316)
  - Core concept: Fovea-gaze models outperform periphery models on face and scene recognition, showing central-field information is broadly useful.
  - Core concept: Scene-selective cortex (PPA, RSC) prefers periphery-only models, while V1 favors fovea-gaze models, consistent with eccentricity-bias organization.
  - **Activation**: eccentricity, visual field, fovea, periphery, egocentric video, SimCLR, visual cortex, neural encoding, retinotopy, scene-selective cortex, PPA, RSC, VEDB, NSD, computational neuroscience

## 2026-07-22 - Quantum Computing Research (Cron Job)

### QuantiSpect: A Structure-Aware Lightweight 3D CNN Pre-Decoder for Scalable Surface Code Quantum Error Correction
- [[quantispect-structure-aware-3d-cnn-predecoder]] - Lightweight 3D CNN pre-decoder for surface codes using FastHyperBlocks; matches the Accurate baseline with ~2.71× fewer parameters and ~2.84× fewer MACs (arXiv: 2607.18204)
  - Core concept: Factor 3D convolutions into spatial, temporal, and mixed spatio-temporal depthwise/grouped branches, then fuse with squeeze-and-excitation channel gating and residual connections.
  - Core concept: Receptive field scales as R = 1 + 2 + 2N; default N=5 gives R=13 with only ~0.663 M parameters; expanded QuantiSpect-21 reaches R=21 and ~0.80% circuit-level threshold with 1.18 M parameters.
  - **Activation**: QuantiSpect, surface code neural decoder, 3D CNN QEC, FastHyperBlock, quantum error correction pre-decoder, spatio-temporal syndrome decoder, lightweight neural decoder

## 2026-07-22 - Systems Engineering Research (Cron Job)


### Integrating High-Level Requirements to Low-Level Tests with Machine-Readable V&V Specifications
- [[vnvspec-requirements-vv-specification]] - VNVSpec framework turns V&V specifications into typed, machine-readable, executable artifacts that bridge high-level systems-engineering requirements with low-level test results (arXiv: 2607.17686)
  - Core concept: Typed, immutable, serializable requirements model with quality gates, traceability DAG, and evidence ingestion from pytest / JUnit / analysis scripts / model adapters.
  - Core concept: Produces audit-ready outputs (compliance matrices, CI reports, GSN assurance cases) for AI-enabled and cyber-physical systems under EU AI Act, ISO 21448, UL 4600, etc.
  - **Activation**: V&V, requirements traceability, MBSE, model-based systems engineering, cyber-physical systems, AI safety assurance, executable specifications, EU AI Act, ISO 21448, INCOSE

### Cluster-Based Distributed Small-Signal Stability Certificates for Grid-Forming Inverter Networks
- [[cluster-based-distributed-stability-certificates]] - Selectable-resolution time-domain stability certificate for grid-forming inverter networks using cluster-based cyclic small-gain and energy arguments (arXiv: 2607.16985)
  - Core concept: Decouples small-signal dynamics into voltage and angle-frequency subsystems; voltage subsystem certified via node-to-node gains and cyclic small-gain with arbitrary cluster partitions.
  - Core concept: Stability indices localize limiting margins to nodes, internal cycles, and inter-cluster channels, matching certification resolution to geography/ownership/control boundaries.
  - **Activation**: grid-forming inverter, distributed stability certification, small-signal stability, cyclic small-gain, cluster-based certification, power system stability, microgrid stability, voltage stability, angle-frequency stability

## 2026-07-22 - Neuroscience Research (Cron Job)

### Emergent topological structure in spontaneous brain-organoid activity
- [[emergent-topological-brain-organoids]] - Persistent homology framework for detecting H1 loops and H2 voids in MEA recordings of spontaneous organoid activity, with a rate- and population-preserving null model (arXiv: 2607.16517)
  - Core concept: Brain-organoid networks carry structured loop topology that exceeds a rate- and population-preserving null, concentrated in strongly co-active "chorister" units.
  - Core concept: H1 resolves from roughly 100 units upward; H2 voids emerge only in larger networks (N >= 119), pointing toward 3D high-resolution recordings for richer higher-order structure.
  - **Activation**: brain organoid, persistent homology, MEA, H1 loops, H2 voids, topological data analysis, neural correlations, rate-preserving null, loop-carrying core

### Organization of computation in reservoir computing
- [[reservoir-computation-organization]] - Eigenspectral decomposition of reservoir state space linking SVD modes to degree-wise information processing capacity and representation energy (arXiv: 2607.17858)
  - Core concept: High IPC does not imply practical accessibility; high-degree nonlinearities often reside in low-energy modes and are easily lost to noise.
  - Core concept: Representation energy per degree distinguishes accessible computation from buried capacity, and enables noise-aware design of physical reservoir computers.
  - **Activation**: reservoir computing, echo state network, information processing capacity, SVD mode decomposition, representation energy, noise-aware capacity, nonlinear degree accessibility

### Discovery by Dreaming: Cross-Domain Recombination in Artificial Memory
- [[discovery-by-dreaming-cross-domain-recombination]] - A skill for implementing cross-domain recombination inspired by dreaming, based on the paper "Discovery by Dreaming: Cross-Domain Recombination in Artificial Memory" (arXiv:2607.16256). This skill outlines how to implement a LoRA fine-tuning pipeline (DREAMS) and a symbolic engine (SAPIENCE) to recombine knowledge across domains, enhancing AI discovery and insight generation.
  - Core concept: Dreams splice together people, places, and times that never met. Neuroscience suggests this recombination is not noise, but a function driving insight and creative discovery.
  - Core concept: Rather than merely defending against forgetting, its measurable value lies in recombining knowledge across experiences that have not yet co-occurred.
  - **Activation**: dreaming, recombination, cross-domain, memory consolidation, LoRA, symbolic AI, neuroscience-inspired AI

# AI Collection

A curated collection of research skills derived from academic papers, organized by domain and methodology.

## 2026-07-23 - Neuroscience Research (Cron Job)

### SpikingMOT: A Spike-Driven Multi-Object Tracker
- [[spikingmot-spike-driven-multi-object-tracker]] - Brain-inspired multi-object tracking using spiking neural networks with Activation Sparsity Preference (ASP) for 72% fewer parameters and 86.7% less energy (arXiv: 2607.19875)
  - Achieves state-of-the-art HOTA scores on SportsMOT (74.9) and DanceTrack (56.5)
  - Uses pseudo-trajectory bases and error-calibrated posterior for adaptive dynamics
  - **Activation**: spikingmot, spike-driven tracking, activation sparsity preference, SNN MOT


## 2026-07-21 - Neuroscience Research (Cron Job)

### scalable-training-continuous-time-snn-dstd
- Scalable Training of Continuous-Time Spiking Neural Networks with Differentiable Spike-Time Discretization (arXiv: 2607.14672)
  - Core methodology: Differentiable Spike-Time Discretization (DSTD) reduces memory by ~100x; synfire-chain-inspired temporal regularization reduces training time ~20x.
  - **Activation**: continuous-time SNN, differentiable spike-time discretization, temporal regularization, spiking neural network training

### eeg-based-lm-evaluation
- Encoding EEG Signals to Examine Human-Like Next-Word Prediction Behaviour in Language Models (arXiv: 2607.16549)
  - Core methodology: Uses EEG signals to evaluate language models' next-word prediction behavior by comparing surprisal and top-1 prediction correlates with ERP components.
  - Key insight: Surprisal, not top-1 prediction, correlates with language-processing ERPs, especially for open-class words; challenges assumption that scaling LMs improves convergence with human-like linguistic processing.
  - **Activation**: EEG, language model evaluation, surprisal, ERP, next-word prediction, neuroscience, computational linguistics

## 2026-07-20 - Neuroscience Research (Cron Job)

### Toward a mechanistic understanding of inference in visual cortex and diffusion models
- [[arxiv-260715693-mechanistic-inference-visual-cortex-diffusion]] - A skill for understanding and applying the methods from the arXiv paper: Toward a mechanistic understanding of inference in visual cortex and diffusion models (arXiv: 260715693)
  - Core contribution 1: Proposes a recurrent neural network model of V1 that is mathematically equivalent to a diffusion model, providing a mechanistic bridge between neuroscience and machine learning.
  - Core contribution 2: Shows that the learned interaction matrix in the model corresponds to the known horizontal connectivity patterns in V1, suggesting that the brain may implement inference similar to diffusion models.
  - **Activation**: mechanistic inference, visual cortex, diffusion models, sparse coding, recurrent neural networks, neuroscience, machine learning

## 2026-07-19 - Neuroscience Research (Cron Job)

## 2026-07-18 - Neuroscience Research (Cron Job)

### grounded-world-models-biological-organisms-future-embodied-ai
- Grounded world models in biological organisms and future embodied AI - arXiv:2607.13560 - A framework for understanding how biological intelligence builds grounded world models through interaction, with implications for embodied AI
  - Presents five examples of neural circuits supporting grounded world modelling
  - Highlights features missing from current embodied AI: intrinsic dynamics as foundation for learning, centrality of action, autonomous experience, and predictive/control mechanisms scaffolding higher cognition
  - **Activation**: grounded world models, biological organisms, embodied AI, neural circuits, predictive learning, action-centered learning

### CogniSNN: Enabling Neuron-Expandability, Pathway-Reusability, and Dynamic-Configurability with Random Graph Architectures in Spiking Neural Networks
- CogniSNN: Enabling Neuron-Expandability, Pathway-Reusability, and Dynamic-Configurability with Random Graph Architectures in Spiking Neural Networks - arXiv:2607.10891 - A framework for understanding how biological intelligence builds grounded world models through interaction, with implications for embodied AI
  - Presents five examples of neural circuits supporting grounded world modelling
  - Highlights features missing from current embodied AI: intrinsic dynamics as foundation for learning, centrality of action, autonomous experience, and predictive/control mechanisms scaffolding higher cognition
  - **Activation**: cogni-snn, spiking neural networks, neuron-expandability, pathway-reusability, dynamic-configurability, random graph architectures, cogneural networks

## 2026-07-17 - Neuroscience Research (Cron Job)

## 2026-07-12 - arXiv Paper Skills (Cron Job)

<<<<<<< HEAD
## 2026-07-15 - Neuroscience Research (Cron Job)

## 2026-07-14 - Neuroscience Research (Cron Job)
=======
### Evolutionary System Prompt Learning (E-SPL)
- [[espl-evolutionary-system-prompt-learning]] - Jointly improves model context (system prompt) and model weights through parallel sampling and LLM self-reflection driven evolution. (arXiv: 2602.14697)
  - Joint optimization of system prompt and model weights through evolutionary algorithms
  - Parallel sampling of multiple system prompt variants during RL training
  - LLM self-reflection drives mutation and crossover of system prompts
  - Encourages declarative knowledge encoding in prompts and procedural knowledge in weights
  - Demonstrated improvement: RL success rate increased from 38.8% to 45.1%

### Agentic Evolution is the Path to Evolving LLMs
- [[agentic-evolution-path-to-evolving-llms]] - Proposes that strategic agency (failure diagnosis and improvement) is needed for LLM evolution, introducing evolution as a new scaling axis. (arXiv: 2601.10007)
  - Identifies limitations of current LLM evolution approaches (fine-tuning, memory accumulation)
  - Proposes strategic agency as necessary for meaningful LLM evolution
  - Introduces evolution as a new scaling axis beyond compute and data
  - Highlights need for agents that can introspect and adapt their own learning processes

### StructAgent: Harness Long-horizon Digital Agents with Unified Causal Structure
- [[structagentharnesslong-horizondigitalagentswithuni]] - State-centered framework for structuring agent state and workflow around a unified causal representation of task progress, enabling checkpointing, evidence-driven task completion, and targeted failure recovery. (arXiv: 2607.11388)
  - Introduces a unified state for compact, verifiable task progress and a structured workflow with verifier-backed state transitions.
  - Enables explicit progress checkpointing, evidence-driven task completion, targeted failure recovery, and tool-supported execution.
  - Improves Qwen3.5-9B from 27.0% to 46.9% and Qwen3.5-27B from 31.6% to 62.2% on OSWorld-Verified; achieves 78.9% with MiniMax-M3.
  - Generalizes beyond desktop environments to Minecraft, demonstrating the generality of our design.

### UniClawBench: A Universal Benchmark for Proactive Agents on Real-World Tasks
- [[uniclawbench-proactive-agents-real-world-tasks]] - Capability-driven benchmark for proactive agents with 400 bilingual tasks in live Docker containers; closed-loop evaluation with executor, supervisor, and user agents (arXiv: 2607.08768)
  - Five foundational capabilities: Skill Usage, Exploration, Long-Context Reasoning, Multimodal Understanding, Cross-Platform Coordination
  - Disentangles base model capabilities from framework-level design choices
  - **Activation**: proactive agents, real-world benchmark, agent evaluation, capability-driven, multimodal agents, closed-loop evaluation

### Remember When It Matters: Proactive Memory Agent for Long-Horizon Agents
- [[proactive-memory-agent-long-horizon-tasks]] - Separate memory agent prevents "behavioral state decay" by selectively injecting memory-grounded reminders; +8.3pp Terminal-Bench, +6.8pp τ²-Bench (arXiv: 2607.08716)
  - Plug-and-play with frontier action agents and existing agent harnesses
  - Open-weight memory policies trained via SFT and GRPO on Qwen3.5-27B
  - **Activation**: proactive memory, long-horizon agents, behavioral state decay, trajectory management, selective intervention

### The Illusion of Equivalency: Statistical Characterization of Quantization Effects in LLMs
- [[illusion-of-equivalency-quantization-effects-llms]] - Shows accuracy/perplexity fail to capture quantization behavioral changes; introduces correctness agreement metric; Q/K projections more sensitive than V/O (arXiv: 2607.08734)
  - Non-linear breakpoints at low bit-widths revealed by layer-wise distortion analysis
  - Behavioral divergence emerges under moderate quantization even when accuracy preserved
  - **Activation**: quantization, LLM deployment, behavioral change, correctness agreement, post-training quantization

### Super Weights in LLMs and the Failure of Selective Training
- [[super-weights-llms-selective-training-failure]] - Shows Super Weight pruning degradation is not universal; training Super Weights in isolation drops accuracy to random-guessing; LoRA with 0.16% params succeeds (arXiv: 2607.08733)
  - Parameter importance ≠ trainability in isolation; effective fine-tuning needs structured decompositions
  - Failure is specific to Super Weight coordinates, not from sparsity itself
  - **Activation**: super weights, LLM training, parameter pruning, selective training, LoRA

### Latent Memory Palace: Reasoning for Control as Autoregressive Variational Inference
- [[latent-memory-palace-reasoning-control-variational-inference]] - Reasoning for continuous control policies emerges via autoregressive latent space; LMP-π with adaptive test-time compute; variable-length action tokenizer LMP-tok (arXiv: 2607.08724)
  - Variational inference formulation with autoregressive latent distribution
  - Interpretable adaptive allocation of test-time compute
  - **Activation**: latent memory palace, reasoning for control, autoregressive variational inference, adaptive reasoning

### Formal Mechanisms for Market Stability in Self-Interested Agent Societies
- [[formal-mechanisms-market-stability-self-interested-agents]] - Multi-agent marketplace simulation with 18 LLM agents; Mediation identified as robust top mechanism; "bend but not break" under adversarial attack (arXiv: 2607.08652)
  - Eight conditions tested under progressive troll injection over 200 rounds
  - Best adversarial attack reduces honest-agent utility by 13.3% but cannot collapse market
  - **Activation**: market stability, self-interested agents, multi-agent economics, cooperation mechanisms, Mediation

### SMetric: Rethink LLM Scheduling for Serving Agents
- [[smetric-llm-scheduling-serving-agents-session-centric]] - Balanced session-centric scheduling for agent serving; routes first request for load balance, follow-ups cache-aware; 10-16% TPS improvement (arXiv: 2607.08565)
  - Agent traces show 80%+ KV-reuse vs 54-62% in chat
  - Stateless design using session turn info from user inputs alone
  - **Activation**: LLM scheduling, agent serving, session-centric scheduling, inference infrastructure, TPS

### BiSCo-LLM: Lookup-Free Binary Spherical Coding for Extreme Low-Bit Compression
- [[bisco-llm-binary-spherical-coding-extreme-compression]] - Codebook-free binary spherical coding for LLM weight compression; bit-packed sign streams; residual BSQ; category-wise recovery distillation (arXiv: 2607.08643)
  - Eliminates VQ codebook storage and lookup overhead
  - Transparent storage accounting including protected channels
  - **Activation**: binary spherical coding, LLM compression, low-bit quantization, codebook-free, BSQ

### DominoTree: Conditional Tree-Structured Drafting for Speculative Decoding
- [[dominotree-conditional-tree-structured-drafting-speculative-decoding]] - Training-free best-first draft tree with Domino's conditional correction; 6.6x speedup on Qwen3-4B; GPU-native CUDA-graph builder (arXiv: 2607.08642)
  - Highest mean accept length: 10.7 tokens per round at every temperature
  - 9-10% throughput improvement over Domino decoder overall
  - **Activation**: speculative decoding, tree-structured drafting, Domino conditioning, CUDA-graph builder

### MAESTRO: Markov-Chain Pruning for Mixture-of-Experts
- [[maestro-pruning-bad-experts-mixture-of-experts]] - Models expert activation as Ergodic Markov chains for globally-aware MoE pruning; 10.61% improvement at 50% compression; lower cross-task variance (arXiv: 2607.08601)
  - Stationary distributions encode cross-layer dependencies
  - Outperforms locally-derived heuristics across Safety, Bias, Ethics domains
  - **Activation**: mixture-of-experts, expert pruning, MoE deployment, structured pruning, Markov chain

### Training-free Relaxed Speculative Decoding
- [[training-free-relaxed-speculative-decoding]] - Unifies relaxed speculative decoding approaches; benchmarks relaxation strategies; relaxation requires careful capability evaluation (arXiv: 2607.08690)
  - Many relaxed approaches require drafter to be a good language model
  - Unsuitable for lightweight dedicated multi-token-prediction drafters
  - **Activation**: speculative decoding, relaxed speculation, LLM inference acceleration, training-free

### Multi-Modal, Multi-Environment Machine Teaching for Robust Reward Learning
- [[multi-modal-multi-environment-machine-teaching-robust-reward]] - Hierarchical teaching across multiple MDPs; comparisons impose stronger constraints than demonstrations; greedy environment selection (arXiv: 2607.08647)
  - Substantially lower regret on held-out environments
  - Demonstrates importance of multi-environment teaching for dynamics-robust rewards
  - **Activation**: machine teaching, reward learning, inverse reinforcement learning, multi-environment

### HCC-STAR: Clinical-Reasoning LLM for Hepatocellular Carcinoma
- [[clinical-reasoning-llm-hepatocellular-carcinoma-risk-stratification]] - Clinically aligned LLM reading EMR narratives for HCC staging, treatment, prognosis; outperforms GPT-5 and Gemini-2.5 Pro; 51 vs 29 months median survival (arXiv: 2607.08602)
  - 30,000 HCC cases from SEER, validated on 6,668 patients from 12 hospitals
  - Step-verifiable composite reward for knowledge-aligned reasoning
  - **Activation**: clinical-reasoning LLM, hepatocellular carcinoma, risk stratification, treatment guidance, EMR

### Secure Decentralized Federated Learning via Gossip and Virtual Voting
- [[secure-decentralized-federated-learning-gossip-virtual-voting]] - gspDAG-FL: gossip-derived consensus via Hashgraph-style virtual voting on DAG; Byzantine resilience with multi-layer validation (arXiv: 2607.08651)
  - No central server or blockchain committees needed
  - Proved safety, conditional liveness, and convergence guarantees
  - **Activation**: decentralized federated learning, gossip protocol, virtual voting, Byzantine resilience

### Native Video-Action Pretraining for Generalizable Robot Control
- [[native-video-action-pretraining-generalizable-robot-control]] - LingBot-VA 2.0: video-action foundation model for embodiment; semantic visual-action tokenizer, causal pretraining, sparse MoE, async inference (arXiv: 2607.08639)
  - Trained from scratch to avoid catastrophic forgetting
  - Real-time closed-loop control via parallel latent prediction
  - **Activation**: video-action model, robot control, causal pretraining, sparse MoE, async inference

### Auditing LLM-as-Judge Reliability
- [[auditing-llm-as-judge-reliability-measurement-validity]] - Evaluator-replacement ambiguity as measurement-validity problem; judge upgrades not interchangeable; proposes audit trails with bias probes (arXiv: 2607.08535)
  - Stronger judges reduce but don't remove position and verbosity bias
  - Repeated-sample juries add little when errors are correlated
  - **Activation**: LLM-as-judge, evaluation reliability, measurement validity, evaluator bias, audit trail

### Cross-seed Explainability with Procrustes-Conditioned SAEs
- [[cross-seed-explainability-procrustes-sparse-autoencoders]] - Procrustes-conditioned Joint Top-K SAE for cross-seed universal features; Pearson r ≥ 0.70 across seeds; dead-feature revival loss (arXiv: 2607.08499)
  - Combines Top-K sparsity, end-to-end optimization, and Procrustes rotation
  - High-universality features encode interpretable sociolinguistic patterns
  - **Activation**: sparse autoencoder, cross-seed universality, Procrustes alignment, mechanistic interpretability

### DocMaster: Hierarchical Structure-Aware Document Analysis
- [[docmaster-hierarchical-structure-aware-document-analysis]] - Parses documents into hierarchical trees preserving layout; structure-aware semantic indices for filtering and QA; interactive web interface (arXiv: 2607.08539)
  - Preserves sections, tables, figures, equations lost in flat chunking
  - Multi-view semantic indices support diverse query types
  - **Activation**: document analysis, hierarchical structure, LLM system, semantic indexing, document filtering

### The Context Access Divide: Agentic Inequality
- [[context-access-divide-agentic-inequality-architecture]] - Formalizes CAD as interaction-level dimension of agentic inequality; manual attachment causes combinatorial collapse; dynamic retrieval structurally insulated (arXiv: 2607.08495)
  - Probabilistic model grounded in fan effect literature from cognitive psychology
  - Analyzes technical basis in MCP and RAG architectures
  - **Activation**: agentic inequality, context access, interaction-level architecture, agent fairness, contextuality

### Harness VLA: Steering Frozen VLAs via Memory-Guided Agents
- [[harness-vla-steering-frozen-vlas-memory-guided-agents]] - Frozen VLA as retryable contact-rich primitive with analytic primitives; learns operating range from execution traces; +38.6pp LIBERO-Pro (arXiv: 2607.08448)
  - Compositional architecture: VLA for contact, analytics for non-contact phases
  - Extends frozen VLAs beyond original trajectory distribution without finetuning
  - **Activation**: vision-language-action, memory-guided agents, manipulation primitives, frozen VLA, robot manipulation

### Statistical Efficiency of Quantile Distributional RL
- [[statistical-efficiency-quantile-distributional-reinforcement-learning]] - Non-asymptotic Õ(√(m/n)) error bound; optimal √n convergence; semiparametric efficiency bound; Berry-Esseen theorem for return distribution inference (arXiv: 2607.08444)
  - Quantile-based estimators remain asymptotically efficient in infinite-dimensional limit
  - Enables statistically valid inference on functionals of return distribution
  - **Activation**: distributional RL, quantile regression, statistical efficiency, policy evaluation, return distribution

### FabriVLA: Lightweight Vision-Language-Action for Multi-Task Manipulation
- [[fabrivia-lightweight-vision-language-action-multi-task-manipulation]] - 1B-scale VLM VLA with flow-matching action head and gated self-attention; 90.0% success on Meta-World MT50; single-stage joint optimization (arXiv: 2607.08575)
  - Compact VLA without multi-billion-parameter backbones
  - Shallow VLM layer fusion for enriched spatial context
  - **Activation**: vision-language-action, lightweight VLA, multi-task manipulation, flow-matching, InternVL3.5

## 2026-07-12 - Neuroscience Research (Cron Job - Evening)

### Learning Biophysical Models of Large-Scale Multineuronal Data to Enable Precise Neurostimulation
- [[biophysical-hh-model-extracellular-neurostimulation]] - Differentiable HH model inference from extracellular MEA data achieves 90.6% accuracy predicting neurostimulation responses from minutes of recording vs hours of testing (arXiv: 2607.04063, ICML 2026)
  - Differentiable biophysical simulation enables gradient-based HH parameter estimation from extracellular recordings only
  - Simulation-based inference (SBI) amortizes fitting across neural populations — no intracellular recordings needed
  - Validated on hundreds of hours of macaque retina data with 512-electrode array (30μm pitch)
  - **Activation**: biophysical HH model, extracellular MEA, neurostimulation prediction, differentiable biophysical simulation, Hodgkin-Huxley inference, simulation-based inference, precise neurostimulation

### Microsecond-precision Sound Localization Emerges from Slow Equilibrium Dynamics
- [[sound-localization-equilibrium-dynamics]] - ITD represented as stable equilibrium of neural population dynamics rather than classical Jeffress place-coding; achieves microsecond precision without delay lines (arXiv: 2607.03890, submitted to Science)
  - Excitatory-inhibitory interactions across frequency channels drive dynamical system to ITD equilibrium
  - Explains both microsecond precision and sluggish dynamic cue tracking in single framework
  - Reproduces frequency-dependent best-delay distributions without explicit delay lines
  - **Activation**: sound localization, equilibrium dynamics, ITD estimation, neural population dynamics, Jeffress model alternative, binaural perception, microsecond precision

### Navigating Hierarchy: Hyperbolic Learning on Brain Graphs for Disorder Diagnosis
- [[hlbg-hyperbolic-learning-brain-graphs]] - Hyperbolic Learning on Brain Graphs (HLBG) with GaMamba models ROI-community-whole-brain hierarchy via Lorentzian space and geometric entailment constraints (arXiv: 2607.07077)
  - Projects multi-level brain representations into Lorentzian hyperbolic space with geometric entailment constraints
  - Graph-aware Mamba (GaMamba) captures long-range dependencies while preserving graph topology
  - Outperforms SOTA on ABIDE-I and REST-MDD, identifies disorder-relevant biomarkers
  - **Activation**: hyperbolic learning, brain graph hierarchy, HLBG, GaMamba, Lorentzian space, geometric entailment, disorder diagnosis

### Contravariance Theory: Strong Alignment for Minimal Solutions to Hard Tasks
- [[contravariance-theory-strong-alignment-minimal]] - Formal proof that weak affine alignment guarantees strong privileged-axis alignment, with alignment "zipping" up the hierarchy; convergent evolution is inevitable under hard tasks (arXiv: 2607.08561)
  - Weak alignment → strong privileged axis alignment; hierarchical zipper effect strengthens alignment at higher layers
  - Metric insensitivity for NeuroAI: choice of comparison metric matters less than previously thought
  - **Activation**: contravariance, strong alignment, privileged axes, DNN-brain alignment, convergent evolution, NeuroAI theory, minimal solutions


## 2026-07-13 - Neuroscience Research (Cron Job)

<<<<<<< HEAD
## 2026-07-12 - Neuroscience Research (Cron Job)

## 2026-07-11 - Neuroscience Research (Cron Job)

## 2026-07-10 - Neuroscience Research (Cron Job)

## 2026-07-09 - Neuroscience Research (Cron Job)

## 2026-07-08 - Neuroscience Research (Cron Job)

## 2026-07-07 - Neuroscience Research (Cron Job)

## 2026-07-06 - Neuroscience Research (Cron Job)

## 2026-07-05 - Neuroscience Research (Cron Job)

## 2026-07-04 - Neuroscience Research (Cron Job)

## 2026-07-03 - Neuroscience Research (Cron Job)

## 2026-07-02 - Neuroscience Research (Cron Job)

## 2026-07-01 - Neuroscience Research (Cron Job)
=======
### Graph-Regularized Deep Learning for EEG-Based Emotion Recognition
- [[graph-regularized-eeg-emotion-recognition]] - 基于心理学情绪拓扑的脑电情绪识别图正则化框架，减少39%不合理误分类 (arXiv: 2607.07773)
  - 核心要点 1: 将情绪建模为图中节点而非孤立标签，边编码基于维度情绪理论的心理邻近性
  - 核心要点 2: 三种正则化策略(图标签平滑/图拉普拉斯通勤距离/切片Wasserstein距离)跨架构通用
  - **Activation**: graph-regularized emotion recognition, EEG emotion graph, psychological label structure
### A Non-Hermitian Potential Well Formalism for Conscious--Preconscious--Subliminal Processing
- [[non-hermitian-conscious-preconscious-subliminal]] - Unified GNW dynamical model using non-Hermitian Hamiltonians and nonlinear Schrödinger equations; consciousness emerges as bound state formation when landscape depth and attention both exceed thresholds (arXiv: 2607.08302)
  - Hermitian part = recognition (dissipative localization), anti-Hermitian part = broadcasting (spatial spreading)
  - Complex-valued landscape bridges sensory encoding and conscious access in single framework
  - **Activation**: non-Hermitian, conscious access, GNW, Global Neuronal Workspace, subliminal, preconscious, potential well, Schrödinger equation, Lotka-Volterra