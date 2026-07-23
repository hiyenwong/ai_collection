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

### Dendritic In-Context Learning in a Single-Layer Spiking Neural Network
- [[dendritic-icl-snn]] - Breakthrough showing dendritic subthreshold dynamics implement complete online LMS, enabling ICL in single-layer SNN without attention or inference-time plasticity (arXiv: 2607.02283)
  - Single dendritic compartment structurally identical to leaky online Widrow-Hoff LMS; linear probe recovers trajectory at R²=0.93
  - Seed-stable at super-dimensional Garg-2022 ICL where dense Transformers exhibit grokking-style instability
  - ICL requires neither attention, depth, nor inference-time plasticity—compartmental dynamics suffice
  - **Activation**: dendritic computation, in-context learning, ICL, compartmental SNN, online LMS, Widrow-Hoff, seed-stable, Garg-2022, single-layer SNN

### DRIADA: A Python Toolkit for Cross-Scale Analysis of Single-Neuron Selectivity and Population Dynamics
- [[driada-cross-scale-neural-analysis]] - Open-source Python toolkit unifying neural signals and behavior in shared data model for cross-scale analysis from single neurons to population dynamics and functional networks (arXiv: 2607.00851)
  - Cross-scale pipeline: information-theoretic selectivity testing → dimensionality reduction → network analysis in unified workflow
  - Hippocampal findings: 90.1% single-feature selectivity in CA1, significant representational drift across sessions, systematic feature prevalence ranking across 13 mice
  - Validated on synthetic data with ground truth and continuous attractor network simulations
  - **Activation**: DRIADA toolkit, cross-scale neural analysis, single-neuron selectivity, population dynamics, hippocampal calcium imaging, representational drift, CellReg


### Chimera State in a Neuronal Network under the Action of a Magnetic Field
- [[chimera-magnetic-field-neuronal]] - Magnetic field transforms chimera state incoherence into coherence in Hindmarsh-Rose networks, revealing multitraveling and multialternating chimera states (arXiv: 2607.07426)
  - Three spatial configurations tested (full, half, dual-region) with magnetic field applications
  - Discovers multitraveling and multialternating chimera states as novel phenomena
  - **Activation**: chimera state, magnetic field, hindmarsh-rose, neuronal synchronization, multicluster chimera, brain cells, TMS

### Dynamic neural manifolds for flexible closed-loop control on neuromorphic hardware
- [[dynamic-neural-manifolds-neuromorphic-control]] - Ring attractor network with sensory-modulated control neurons (speed, shape, selection) drives subspace rotations and trajectory control on SpiNNaker 2 for real-time closed-loop robotic navigation (arXiv: 2607.07373)
  - Three control neuron types modulate manifold geometry: speed (gain), shape (inhibition), selection (targeted inhibition)
  - Fully explainable neuromorphic architecture — predictable ring dynamics + geometric manifold interpretation
  - Validated on robotic maze navigation with real-time sensory feedback on SpiNNaker 2 chip
  - **Activation**: dynamic neural manifold, neuromorphic control, spinnaker 2, ring attractor, closed-loop spiking, subspace rotation, neural trajectory, manifold geometry, explainable neuromorphic

### SA-HGNN: Sample-Adaptive Hyperbolic Graph Neural Network for EEG-Based Depression Recognition
- [[sa-hgnn-eeg-depression-hyperbolic]] - Novel GNN combining sample-adaptive graph construction, hyperbolic graph convolution, and attention pooling to capture hierarchical brain network structure in EEG-based depression recognition (arXiv: 2607.02063)
  - Hyperbolic geometry overcomes Euclidean bottleneck for tree-like hierarchical brain networks in depression
  - Sample-adaptive topology captures individual connectivity patterns vs. fixed static graphs
  - Attention pooling adaptively filters redundant noise channels in EEG signals
  - **Activation**: sa-hgnn, hyperbolic GNN, eeg depression recognition, sample-adaptive graph, hyperbolic convolution, attention pooling, functional connectivity hierarchy

## 2026-07-12 - Neuroscience Research (Cron Job)

### BUS: Brain-Inspired Unsupervised Self-Reflection for Advanced Multimodal Reasoning
- [[bus-brain-inspired-self-reflection-vlm]] - 脑启发无监督自反思框架，利用大脑反向预测机制实现VLM无标注自我验证推理 (arXiv: 2607.07361)
  - 核心要点 1: 证明VLM具有类似人脑的backward prediction能力（65%+一致性），可用前驱表征进行自验证
  - 核心要点 2: 提出两阶段BUS框架，阶段I生成多推理-答案对，阶段II引导反向预测实现无标注训练
  - **Activation**: brain-inspired self-reflection, backward prediction VLM, unsupervised self-reflection, BUS framework, 脑启发自反思

## 2026-07-12 - Quantum Neuromorphic Research (Cron Job)

### Computational Superiority of Non-Markovian Kerr Feedback in Continuous-Variable Quantum Reservoir Computing
- [[non-markovian-kerr-feedback-qrc]] - Proves unbounded resource separation: single Kerr mode with time-delayed feedback achieves arbitrary cross-time nonlinear rank, replacing up to ~100 linear modes in CV-QRC (arXiv: 2606.06689)
  - N-mode Gaussian reservoir has hard ceiling at 2N cross-time nonlinear rank; single Kerr+feedback depth D achieves rank D (no ceiling)
  - Counterintuitively, loss enables distinct fingerprints per round-trip; without loss passes would be redundant
  - **Activation**: Kerr feedback, non-Markovian QRC, continuous-variable quantum, cross-time nonlinear correlations, Gaussian limitations, time-delay feedback, optical computing
### Temporal Processing of Quantum States with Hybrid Quantum-Classical Reservoirs
- [[hybrid-quantum-classical-reservoirs]] - Hybrid quantum-classical reservoir computing (HRC) combining qubit QRC with classical ESN overcomes linearity barrier for nonlinear functionals like purity and entropy (arXiv: 2606.21327)
  - Quantum reservoir alone fundamentally linear for single input state; classical ESN provides nonlinear approximation, quantum reservoir provides enhanced information retrieval
  - Advantage persists under partial measurements (single-axis); online monitoring protocol accounts for measurement back-action and finite ensembles
  - **Activation**: hybrid quantum-classical reservoir, echo state network, quantum state processing, nonlinear functionals, purity estimation, measurement back-action, near-term qubit

## 2026-07-12 - Neuroscience Research (Cron Job)

### STST-JEPA: Shallow-Target Spatio-Temporal Joint Embedding Predictive Architecture for EEG Self-Supervised Learning
- [[stst-jepa-eeg-foundation]] - Largest EEG foundation model (47,703 sessions, ages 5-81) using JEPA-style latent prediction with EMA tokenizer + auxiliary reconstruction; rank 1 on NeuralBench across 3 tasks (arXiv: 2607.06629)
  - Joint objective: latent prediction (MSE vs EMA tokenizer targets, λ=1.0) + auxiliary signal reconstruction (Smooth-L1, λ=0.35); maps to predictive processing theory
  - PMA channel pooling collapses 128 channels per temporal index via Set Transformer attention, handling montage heterogeneity (115 vs 128 channels) across corpora
  - Brain age gap negatively correlates with cognitive efficiency across 21 behavioral targets; 7 survive BH-FDR correction (q=0.05)
  - **Activation**: STST-JEPA, EEG foundation model, brain age prediction, self-supervised EEG, JEPA, brain age gap, cognitive efficiency, PMA channel pooling, NeuralBench
### Intrinsic-Noise Consolidation: A Doob-Barrier-Conditioned Diffusion Turns Analog Device Noise into a Continual-Learning Resource
- [[doob-barrier-noise-consolidation]] - Doob h-transform applied to per-synapse weight dynamics turns analog device noise into memory consolidation resource; validated on real BrainScaleS-2 silicon (arXiv: 2607.06924)
  - Doob barrier-conditioning creates restoring force amplified by noise variance itself; diverges at barrier
  - Falsifiable inverted-U prediction: noise level non-monotonically improves retention (10.9 pp gain on Split-MNIST)
  - Real BrainScaleS-2: 15.6 pp better retention at matched accuracy; noise reframed from tax to consolidation dividend
  - **Activation**: Doob barrier, noise consolidation, continual learning, catastrophic forgetting, analog neuromorphic, BrainScaleS-2, h-transform
### Dynamic Neural Manifolds for Flexible Closed-Loop Control on Neuromorphic Hardware
- [[dynamic-neural-manifolds-control]] - Maps circuit mechanisms to low-dimensional manifold geometry on SpiNNaker 2 for real-time closed-loop robotic control; sensory inputs modulate inhibition, gain, and transient currents for behavior switching (arXiv: 2607.07373)
  - Subspace rotations enable rapid behavior switching; trajectory speed modulation adapts movement timing
  - Validated via robotic maze navigation where agent dynamically reconfigures manifold geometry from sensory feedback
  - **Activation**: dynamic neural manifolds, closed-loop control, neuromorphic hardware, SpiNNaker 2, subspace rotation, manifold geometry, behavior switching, trajectory control, explainable AI
### Scalable Perturbation Learning for Online Self-Supervised Echo State Networks
- [[scalable-perturbation-learning-esn]] - Orthogonal decomposition of ESN self-supervised cost reduces perturbation dimension from reservoir size to input dimension, enabling scalable online self-supervised learning (arXiv: 2607.06079)
  - Perturbing only input-dependent component avoids reservoir-size-dependent variance growth
  - Design principle: online learning should target dynamically necessary low-dimensional component of objective
  - **Activation**: echo state networks, perturbation learning, self-supervised learning, online learning, reservoir computing, orthogonal decomposition
### Online Data Reduction with Spiking Neural Networks for the ePIC dRICH Detector
- [[snn-online-data-reduction-physics]] - SNN-based online data reduction for 320K SiPM channels at 100 MHz; temporal-coincidence encoder + distributed SNN achieves ≥5× data reduction while preserving Cherenkov photon signals (arXiv: 2607.03492)
  - Temporal-coincidence encoding converts SiPM hit patterns into spike trains; SNN classifies genuine Cherenkov vs. dark count noise
  - Event-driven distributed architecture eliminates idle-time computation at 100 MHz; scalable to future collider detectors
  - **Activation**: snn online data reduction, temporal-coincidence encoder, dRICH detector, ePIC experiment, SiPM dark count filtering, neuromorphic particle physics
### Shunting Inhibition and Dendritic Branching Shape Local Credit Assignment
- [[shunting-inhibition-dendritic-credit]] - Exact gradient factorization in conductance-based dendritic networks: local eligibility × compartment error; shunting inhibition reshapes error geometry for restricted somatic feedback (arXiv: 2607.03556)
  - Gradient = Local Eligibility (presynaptic activity × driving force × input resistance) × Compartment Error (path-specific error transported through dendritic gains)
  - Shunting LocalCA achieves within 5-6 percentage points of backprop on MNIST with per-soma 5-factor feedback; feedback-field fidelity remains the bottleneck
  - **Activation**: shunting inhibition, dendritic credit assignment, local learning, backpropagation biological plausibility, E/I conductance, compartment-specific error, somatic feedback
### Contravariance Theory: Strong Alignment for Minimal Solutions to Hard Tasks
- [[contravariance-theory-strong-alignment]] - Formal proof that weak affine alignment guarantees strong privileged-axis alignment in minimal DNN solutions; alignment "zippers" up hierarchy (arXiv: 2607.08561)
  - Convergent evolution between DNNs and brains is inevitable for sufficiently hard tasks; metric choice for comparison is insensitive
  - **Activation**: contravariance theory, NeuroAI alignment, privileged axes, convergent evolution, minimal DNN solutions
### Dynamic Neural Manifolds for Flexible Closed-Loop Control on Neuromorphic Hardware
- [[dynamic-neural-manifolds-snn-control]] - Spiking ring networks on SpiNNaker 2 use three control knobs (gain, inhibition, transient currents) to dynamically steer low-dimensional manifold geometry for explainable closed-loop robotic control (arXiv: 2607.07373)
  - Three control knobs: additive current shapes trajectory radius, multiplicative gain controls sequence speed, heterogeneous inhibition rotates subspaces for behavior switching
  - Spike-based communication + sparse circulant connectivity enables real-time operation (<1ms time step) with linear scaling in spike count
  - Demonstrated on virtual maze navigation: agent dynamically reconfigures manifold geometry to steer, jump, and turn based on sensory feedback
  - **Activation**: neural manifolds, neuromorphic control, SpiNNaker, ring network, subspace rotation, explainable SNN, closed-loop control, dynamic manifolds
### Non-Hermitian Potential Well Formalism for Conscious–Preconscious–Subliminal Processing
- [[non-hermitian-gnw-consciousness]] - Nonlinear Schrödinger-type equation with non-Hermitian, non-normal Hamiltonian models conscious access as bound state emergence in the Global Neuronal Workspace (arXiv: 2607.08302)
  - Hermitian Hamiltonian component drives recognition (localization at landscape minima); anti-Hermitian component drives broadcasting (spatial spreading)
  - Conscious access requires both sufficient stimulus strength (U > threshold) AND top-down attention (A > A_c); reproduces subliminal/preconscious/conscious taxonomy
  - Bound state emergence at attention threshold is a first-order phase transition with finite spatial extent
  - **Activation**: GNW, consciousness, non-Hermitian, neural field theory, bound states, sensory processing hierarchy, cloud functions, global neuronal workspace
### BUS: Brain-Inspired Unsupervised Self-Reflection for Advanced Multimodal Reasoning
- [[bus-brain-inspired-self-reflection-vlm]] - Brain-inspired unsupervised self-reflection enables VLMs to self-correct complex visual reasoning without labeled data (arXiv: 2607.07361)
  - Recurrent feedback loops mimic cortical prediction error signaling for iterative reasoning improvement
  - Cross-modal validation between visual evidence and textual reasoning steps reduces hallucination
  - **Activation**: brain-inspired self-reflection, VLM reasoning improvement, unsupervised reasoning correction, self-correcting vision-language models, BUS methodology
### Hardware-Aware Mixed-Signal SNN Framework for Design Space Exploration
- [[hardware-aware-mixed-signal-snn-framework]] - Open-source framework for mixed-signal SNN hardware design space exploration capturing analog/digital non-idealities (arXiv: 2607.06456)
  - Models device mismatch, thermal noise, finite precision, and routing latency for energy-accuracy Pareto analysis
  - Supports architecture variants from fully analog to fully digital with modular pluggable neuron/synapse models
  - **Activation**: mixed-signal SNN, hardware-aware simulation, design space exploration, neuromorphic edge, non-ideal hardware modeling, SNN accelerator
### EEG-Based Imagined Speech Decoding Using a Hybrid CNN-SNN Architecture
- [[cnn-snn-imagined-speech-decoding]] - First integration of SNNs into EEG-based imagined speech decoding; hybrid CNN-SNN pipeline achieves 80.13% accuracy on BCI Competition III benchmark, surpassing existing methods by 10% (arXiv: 2607.03844)
  - CNN extracts spatial-temporal EEG features, SNN performs spike-based temporal classification
  - Biologically grounded pipeline enabling energy-efficient neuromorphic BCI applications
  - **Activation**: imagined speech decoding, EEG speech BCI, CNN-SNN hybrid architecture, spike-based speech classification, neuromorphic BCI, BCI Competition III
### Dynamic neural manifolds for flexible closed-loop control on neuromorphic hardware
- [[dynamic-neural-manifolds-snn-control]] - 动态神经流形在神经形态硬件上的灵活闭环控制，通过感觉输入调制异质抑制、增益和瞬态电流实现行为切换和轨迹控制 (arXiv: 2607.07373v1)
  - 核心要点 1：将群体神经活动建模为低维流形轨迹，通过环网络上的电路机制（异质抑制、增益、瞬态电流）参数化流形几何
  - 核心要点 2：首次在 SpiNNaker 2 芯片上实现动态流形闭环控制，机器人通过感觉反馈动态重构流形几何完成迷宫导航
  - **Activation**: neural manifold, neuromorphic control, SpiNNaker, closed-loop, ring network, subspace rotation
### Dendritic In-Context Learning in a Single-Layer Spiking Neural Network
- [[dendritic-in-context-learning-snn]] - 单层树突脉冲神经网络的上下文学习，用树突室动力实现在线LMS估计，所有突触权重推理时冻结 (arXiv: 2607.02283v1)
  - 核心要点 1：证明单个树突室的阈下动力学本身就实现了完整的在线学习算法（leaky online Widrow-Hoff LMS），无需注意力、深度或推理时可塑性
  - 核心要点 2：DendriCL 是唯一在超维 Garg-2022 ICL 任务（d≥30）中种子稳定的架构，线性探针从顶树突膜恢复 LMS 轨迹 R²=0.93
  - **Activation**: in-context learning, dendritic computation, LMS, compartmental neuron, frozen weights, Garg-2022
### Intrinsic-Noise Consolidation via Doob-Barrier-Conditioned Diffusion
- [[doob-barrier-noise-consolidation]] - Doob h-transform turns analog device noise into continual-learning resource; noise-amplified restoring force yields inverted-U retention curve on BrainScaleS-2 (arXiv: 2607.06924v1)
  - 核心要点 1: 将突触持续学习建模为 Doob h-变换，条件化权重扩散不跨越记忆关键屏障，产生 σ²·∂w log h 恢复力
  - 核心要点 2: 预注册 falsifier 通过 — Split-MNIST 上 retention 提升 10.9pp (σ*=0.02, p=0.004)，在真实 BrainScaleS-2 硅片上验证 15.6pp 提升
  - **Activation**: doob h-transform, noise consolidation, continual learning, catastrophic forgetting, BrainScaleS-2, neuromorphic noise, analog hardware, synaptic consolidation
### Adaptive Conduction Delays and Phase Locking in Spiking Haken Lighthouse Networks
- [[adaptive-conduction-delays-haken-lighthouse]] - Analytically tractable theory of phase-locked activity in delayed spiking networks; activity-dependent myelination plasticity modulates axonal conduction speed (arXiv: 2606.21508)
  - Self-consistency conditions and linear stability theory for phase-locked states via spike-time perturbations; circulant symmetry enables Fourier mode decomposition
  - Slow-fast dynamics: frozen phase-locked branches organize adaptive dynamics; plasticity selects commensurate delay-period relationships
  - **Activation**: adaptive conduction delays, phase locking, Haken Lighthouse, myelination plasticity, spiking networks, event-driven simulation, slow-fast dynamics, delayed networks
### Formal Verification of Probabilistic Spiking Neural Networks via Quotient Abstractions
- [[formal-verification-probabilistic-snn-quotient]] - CogSpike framework for formal verification of probabilistic SNNs using weight-discretized quotient abstractions; ~17x state reduction per neuron with formal correctness guarantees (arXiv: 2606.20674)
  - Weight-discretized quotient model abstraction; two-sided fidelity theorem bounds firing disagreement; Asymptotic Silence theorem guarantees permanent silence of unforced neurons
  - Validated across seven canonical topologies via PRISM-based probabilistic model checking of DTMC encodings
  - **Activation**: formal verification, probabilistic SNN, quotient abstraction, CogSpike, PRISM, DTMC, state space explosion, synaptic weight discretization, fidelity theorem
### Soliton-like Waves in 2D Recurrent SNN with Weighted STDP
- [[soliton-waves-wstdp-snn]] - 2D recurrent SNN with multiplicative WSTDP, divisive normalization, homeostatic threshold, and refractory period spontaneously produces dissipative soliton waves that learn propagation direction and encode spatial memory via collision boundaries (arXiv: 2606.21432)
  - Dissipative solitons maintain stable profile, constant speed, and annihilate upon frontal collision
  - WSTDP engraves propagation direction; network learns to sustain one direction while suppressing reverse
  - Wave collision defines semi-persistent boundary encoding relative phase/frequency of dual sources
  - **Activation**: soliton waves, weighted STDP, cortical traveling waves, spatial memory, divisive normalization, 2D recurrent SNN
### Stationary Covariance Spectra of Non-Normal Random Recurrent Dynamics
- [[non-normal-covariance-spectra-rnn]] - Free-probability derivation of closed functional equation for stationary covariance spectrum of discrete-time non-normal RNNs; continuous-time analog yields infinite Schwinger-Dyson hierarchy (arXiv: 2606.31944)
  - Closed form enables tail eigenvalue analysis in critical regime for discrete-time dynamics
  - Fundamental asymmetry: discrete-time has closed scalar equation, continuous-time has infinite hierarchy
  - Provides testable predictions for comparing non-normal RNN models to neural population data
  - **Activation**: non-normal dynamics, stationary covariance spectrum, free probability, critical regime, Schwinger-Dyson equations, PCA analysis

### Learning Biophysical Models of Large-Scale Multineuronal Data to Enable Precise Neurostimulation
- [[hh-model-inference-from-mea]] - Rapid HH parameter inference from extracellular MEA data using differentiable simulation + SBI; 90.6% accuracy predicting unseen stimulation on macaque retina (arXiv: 2607.04063v1)
  - Replaces hours of clinical stimulus testing with model-based prediction from minutes of recording
  - Scales to hundreds of neurons simultaneously, capturing population heterogeneity
  - **Activation**: HH model fitting, extracellular MEA inference, neurostimulation prediction, differentiable biophysical simulation, simulation-based inference, Hodgkin-Huxley, biophysical parameter estimation
### Navigating Hierarchy: Hyperbolic Learning on Brain Graphs for Disorder Diagnosis
- [[hyperbolic-learning-brain-graphs]] - First hyperbolic framework modeling ROI→community→whole-brain hierarchy via Lorentzian space; introduces Graph-aware Mamba (GaMamba) for long-range dependency capture; SOTA on ABIDE-I and REST-MDD (arXiv: 2607.07077v1)
  - Two geometric entailment constraints enforce hierarchical relationships in hyperbolic space
  - GaMamba injects GAT-derived structural prompts into Mamba's output matrix for topology-aware long-range modeling
  - **Activation**: hyperbolic brain graphs, HLBG, GaMamba, Graph-aware Mamba, brain disorder diagnosis, Lorentzian space, hierarchical brain network, biomarker identification, ABIDE, REST-MDD
### Adaptive Conduction Delays and Phase Locking in Spiking Haken Lighthouse Networks
- [[adaptive-conduction-delays-haken-lighthouse]] - Analytically tractable theory of phase-locked activity in delayed spiking networks; introduces activity-dependent myelination plasticity that modulates axonal conduction speed (arXiv: 2606.21508)
  - Self-consistency conditions and linear stability theory for phase-locked states via spike-time perturbations; circulant symmetry enables Fourier mode decomposition for ring networks
  - Slow-fast dynamics: frozen phase-locked branches organize adaptive dynamics; plasticity selects commensurate delay-period relationships enabling synchrony emergence, frequency-locked states, and slow switching between patterns
  - **Activation**: adaptive conduction delays, phase locking, Haken Lighthouse, myelination plasticity, spiking networks, event-driven simulation, slow-fast dynamics, delayed networks, circulant symmetry
### Formal Verification of Probabilistic Spiking Neural Networks via Quotient Abstractions
- [[formal-verification-probabilistic-snn-quotient]] - CogSpike framework for formal verification of probabilistic SNNs using weight-discretized quotient abstractions; ~17x state space reduction per neuron with formal correctness guarantees (arXiv: 2606.20674)
  - Weight-discretized quotient model abstraction preserves relative synaptic contribution; two-sided fidelity theorem bounds firing disagreement to gray zone; Asymptotic Silence theorem guarantees permanent silence of unforced neurons
  - Validated across seven canonical topologies via PRISM-based probabilistic model checking of DTMC encodings; enables verification of networks otherwise intractable
  - **Activation**: formal verification, probabilistic SNN, quotient abstraction, CogSpike, PRISM, DTMC, state space explosion, synaptic weight discretization, fidelity theorem

## 2026-07-12 - Systems Engineering Research (Cron Job)

### Modeling Normal Is All You Need: Joint Latent Clustering for Anomaly Detection in Multimodal Cyber-Physical Systems
- [[miim-cps-anomaly-detection]] - Joint latent representation + GMM clustering for CPS anomaly detection under MIIM assumptions; drops reconstruction scoring; fair protocol with raw point-wise metrics and difficulty stratification (arXiv: 2607.06094)
  - MIIM assumption set characterizes CPS normal behaviour as union of imbalanced curved thin-fringed operating regimes
  - Latent-only GMM scoring outperforms deep detectors (USAD, TranAD, GDN) on difficult correlation/dynamics faults
  - Fair evaluation protocol: raw point-wise metrics, trivial-detector splits, prevalence-matched F1
  - **Activation**: cps anomaly detection, miim, multimodal anomaly, latent clustering, cyber-physical systems, fault detection
### Auto-DSM Under the Lens: A Black-Box Evaluation Framework for LLM-Based DSM Generation
- [[auto-dsm-evaluation-framework]] - Systematic benchmark methodology for evaluating LLM-generated Design Structure Matrices using structural, classification, and stability metrics synthesized into Composite Quality Score (arXiv: 2607.05985)
  - Three-perspective evaluation: single-run (Completeness, Correctness, Density), multi-run (Selective Accuracy, Abstention Coverage), stability (Entropy, Fleiss' κ)
  - Systematic failure modes identified: ambiguous definitions → hallucination, poor prompts → abstention failure
  - Transparent benchmark for auditing Auto-DSM pipelines in MBSE workflows
  - **Activation**: dsm generation, auto-dsm, mbse evaluation, llm systems engineering, design structure matrix

## 2026-07-10 - Neuroscience Research (Cron Job)

### A Non-Hermitian Potential Well Formalism for Conscious–Preconscious–Subliminal Processing
- [[non-hermitian-conscious-preconscious-subliminal]] - GNW modeled as complex-valued landscape with non-Hermitian Hamiltonian; conscious access = bound state emergence when depth + attention exceed thresholds (arXiv: 2607.08302)
  - Nonlinear Schrödinger-type equation in imaginary time with Lotka-Volterra term for norm preservation and nonlocal interactions
  - Hermitian part → recognition via dissipative localization; anti-Hermitian part → information broadcasting via spatial spreading
  - **Activation**: non-Hermitian consciousness, GNW landscape, bound state emergence, complex-valued Hamiltonian, subliminal processing
### Contravariance Theory: Strong Alignment for Minimal Solutions to Hard Tasks
- [[contravariance-theory-strong-alignment]] - Formalizes that weak alignment via affine mappings guarantees strong alignment of privileged axes in minimal DNN solutions; alignment "zippers" up hierarchy (arXiv: 2607.08561)
  - Proves convergent evolution between DNNs and brains is inevitable for sufficiently hard tasks; metric choice for comparison is insensitive
  - **Activation**: contravariance theory, NeuroAI alignment, privileged axes, convergent evolution, minimal DNN solutions
### Topological Decoding of Grid Cell Activity via Path Lifting to Covering Spaces
- [[topological-grid-cell-decoding-codes]] - TDA extracts toroidal coordinates from grid cell populations + path-lifting reconstructs trajectories in physical space (arXiv: 2510.16216)
  - Validated on CANN simulations and experimental grid cell recordings; single module suffices for path integration
  - **Activation**: grid cell decoding, toroidal manifold, path lifting, topological data analysis, covering spaces, spatial navigation
### Extended Predictive Coding Framework under Exponential-Family Assumption
- [[extended-predictive-coding-exponential-family]] - Extends FEP-PC correspondence from Gaussian to exponential family, enabling nonlinear heterogeneous neural dynamics (arXiv: 2605.30882)
  - Trainable by biologically plausible local plasticity rules; resolves negative firing rate problem
  - **Activation**: extended predictive coding, exponential family, free energy principle, local plasticity rules
### Human-like Object Grouping in Self-supervised Vision Transformers
- [[human-like-object-grouping]] - Behavioral benchmark shows DINO-trained ViTs best match human object segmentation via Gram matrix structure (arXiv: 2603.13994)
  - Object-centric structure in representations predicts human behavior; Gram anchoring improves alignment
  - **Activation**: human-like object grouping, DINO vision transformer, Gram matrix alignment, object-centric representations
### Synchronization Modes in Bipartite Oscillator Networks
- [[synchronization-bipartite-oscillator-networks]] - Kuramoto-Sakaguchi on bipartite networks exhibits partial synchrony via self-organized quasiperiodicity (arXiv: 2606.20345)
  - Models E/I population dynamics; global oscillations fail to entrain one population → quasiperiodic dynamics
  - **Activation**: bipartite synchronization, Kuramoto-Sakaguchi, partial synchrony, quasiperiodicity, E/I balance
### STST-JEPA: Shallow-Target Spatio-Temporal Joint Embedding for EEG SSL
- [[stst-jepa-eeg-foundation]] - Self-supervised EEG transformer pretrained on 47,703 sessions; MAE 3.06 years for brain age regression (arXiv: 2607.06629)
  - Latent-prediction + signal reconstruction objectives; 30-second windows, spatiotemporal block masks
  - **Activation**: STST-JEPA, EEG foundation model, brain age prediction, JEPA objective, NeuralBench

## 2026-07-11 - Anthropic Research (Cron Job)

### An off switch for dual-use knowledge in AI models
- [[off-switch-dual-use-gram]] - Gradient-Routed Auxiliary Modules (GRAM): train one LLM with removable knowledge compartments per dual-use category; delete modules to surgically remove capabilities without retraining
  - Adds extra neurons per Transformer layer, grouped into modules (one per dual-use category); general weights frozen during dual-use training so knowledge stays localized
  - 4 dual-use domains → 16 deployment configs from 1 training run; module deletion matches data filtering effectiveness; resists post-removal fine-tuning recovery
  - Performance gap (on vs off) widens at larger model sizes; bypass becomes harder as models scale
  - **Activation**: GRAM, gradient-routed auxiliary modules, dual-use knowledge, removable compartments, surgical knowledge removal, capability toggling


### Dendritic In-Context Learning in a Single-Layer Spiking Neural Network
- [[dendritic-in-context-learning-snn]] - First SNN to achieve general-purpose in-context learning via apical compartment dynamics that structurally implement online Widrow-Hoff LMS, seed-stable where Transformers grok-collapse (arXiv: 2607.02283)
  - Apical recurrence u_A(t+1) = α·u_A(t) + γ·e_t·W_A·x_t is structurally identical to leaky online LMS — no attention, depth, or inference-time plasticity needed
  - Linear probe recovers reference LMS trajectory from apical membrane at R² = 0.93; Transformer exhibits 3-mode grokking distribution at d=30 while DendriCL converges smoothly (σ ≤ 0.005)
  - **Activation**: dendritic in-context learning, compartmental SNN, online LMS dynamics, apical recurrence, Garg-2022 benchmark, seed-stable ICL, neuromorphic efficiency

### Dynamic Neural Manifolds for Flexible Closed-Loop Control on Neuromorphic Hardware
- [[dynamic-neural-manifolds-snn-control]] - SpiNNaker 2 implementation of dynamic neural manifold control for embodied robotics — ring network with sensory-modulated subspace rotations for maze navigation (arXiv: 2607.07373)
  - Three control parameters (multiplicative gain, additive current, random silencing) map to trajectory speed, shape, and subspace rotation — enabling behavior switching in real-time
  - Precise geometric scaling confirmed: subspace angle follows arccos(1-p_inh), speed controlled by gain modulation, bump size by additive current
  - **Activation**: dynamic neural manifolds, SpiNNaker 2 neuromorphic, closed-loop control, ring attractor, subspace rotation, explainable neuromorphic, embodied robotics

## 2026-07-11 - Quantum Computing Research (Cron Job)

### Robust Quantum Learning through Hamiltonian Reservoir Computing
- [[hamiltonian-quantum-reservoir-computing]] - Quantum reservoir computing via direct Hamiltonian encoding that circumvents barren plateaus, validated on both analog superconducting and digital gate-based platforms with dissipation-enhanced stability (arXiv: 2607.08037)
  - Hamiltonian encoding maps input data directly onto fixed Hamiltonian, evolved via quantum dynamics for nonlinear feature extraction
  - Two implementations: analog processor (hardware-efficient, bypasses gate overhead) and digital circuit (universal, higher overhead)
  - Finite dissipation constructively suppresses quantum-scrambling instabilities → noise as regularization
  - **Activation**: Hamiltonian reservoir computing, quantum reservoir computing, barren plateau mitigation, analog quantum processor, dissipation-enhanced quantum learning

## 2026-07-11 - Neuroscience Research (Cron Job)

### Omni-Sleep: Sleep Foundation Model via CNS-ANS Hierarchical Contrastive Learning
- [[omni-sleep-foundation]] - Sleep foundation model using CNS/ANS physiological partition as topology-constrained prior for multimodal PSG representation learning, pre-trained on 100K+ hours (arXiv: 2607.07720)
  - Three objectives: intra-system consistency, inter-system synchronization, latent-space masked temporal modeling
  - Outperforms baselines on sleep staging and multi-disease classification across datasets and modality-ablation settings
  - **Activation**: omni-sleep, sleep foundation model, CNS-ANS dynamics, polysomnography, multimodal biosignal, physiological hierarchy

### Graph-Regularized Deep Learning for EEG Emotion Recognition
- [[graph-regularized-eeg-emotion]] - EEG emotion recognition with psychologically-grounded label structure using graph regularization (GLS, CDGL, SWD) to penalize implausible misclassifications (arXiv: 2607.07773)
  - Three regularization strategies ordered by complexity: Graph Label Smoothing, Commuting Distance, Sliced Wasserstein Distance
  - Up to +5.42% accuracy, 39% reduction in psychologically implausible errors on SEED-IV/V across 3 backbones
  - **Activation**: graph-regularized EEG emotion, affective BCI, SEED dataset, emotion topology, Sliced Wasserstein, psychological label structure

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

## 2026-07-10 - Neuroscience Research (Cron Job) — q-bio.NC Sync Batch

### Non-Hermitian Potential Well Formalism for Conscious–Preconscious–Subliminal Processing
- [[non-hermitian-conscious-preconscious-subliminal]] - GNW modeled as complex-valued landscape; Hermitian part enables recognition, anti-Hermitian part enables broadcasting; conscious access = bound state emergence (arXiv: 2607.08302)
  - Nonlinear Schrödinger-type equation with Lotka–Volterra term preserves norm with spatially nonlocal interactions
  - Two-threshold model: conscious access requires both landscape depth and top-down attention to exceed thresholds
  - **Activation**: global neuronal workspace conscious access, non-Hermitian Hamiltonian, subliminal preconscious processing, Lotka-Volterra neural dynamics, complex Schrödinger perception

### Contravariance Theory: Strong Alignment for Minimal Solutions
- [[contravariance-theory-strong-alignment]] - Formalizes that weak alignment via affine mappings guarantees strong alignment of privileged axes in minimal DNN solutions to hard tasks (arXiv: 2607.08561)
  - Alignment "zippers" up the network hierarchy from end-to-end task optimization
  - Convergent evolution between artificial and brain networks probably inevitable under strong task constraints
  - **Activation**: contravariance theory, strong alignment minimal solutions, brain-DNN convergence, privileged axes, NeuroAI alignment

### Topological Decoding of Grid Cell Activity via Path Lifting
- [[topological-grid-cell-decoding-codes]] - Decodes spatial information from grid cell population using TDA to extract toroidal coordinates and path-lifting to reconstruct trajectories (arXiv: 2510.16216)
  - Reconstructed paths differ from original by affine transformation; validated on CANN simulations and experimental data
  - Co-modular grid cells contain sufficient information for path integration without external position data
  - **Activation**: topological grid cell decoding, path lifting covering spaces, toroidal manifold, grid cell population code, spatial navigation computation

### Extended Predictive Coding under Exponential Family Assumption
- [[extended-predictive-coding-exponential-family]] - Extends FEP-PC correspondence beyond Gaussian assumption to exponential family, capturing nonlinearity, heterogeneity, and biological plausibility (arXiv: 2605.30882)
  - Maintains FEP-PC correspondence up to second cumulant; trainable by local plasticity rules
  - Captures biological properties missing in Gaussian PC: nonlinearity, heterogeneous I/O, non-negative firing rates
  - **Activation**: exponential family predictive coding, free energy principle variational inference, biological plasticity rules, non-Gaussian perception

### STST-JEPA: Shallow-Target Spatio-Temporal Joint Embedding for EEG
- [[stst-jepa-eeg-foundation]] - Self-supervised transformer for resting-state and task EEG pretrained on 47,703 sessions, achieving MAE 3.06 years for brain age regression (arXiv: 2607.06629)
  - Latent-prediction objective with EMA-of-tokenizer target + auxiliary signal reconstruction under spatiotemporal block masks
  - Rank-1 on NeuralBench for sex classification (BA 0.911), age prediction (r=0.749), psychopathology regression (r=0.215)
  - **Activation**: STST-JEPA, EEG foundation model, brain age regression, self-supervised EEG, spatiotemporal masking, JEPA architecture

### Synchronization Modes in Bipartite Oscillator Networks
- [[synchronization-bipartite-oscillator-networks]] - Kuramoto-Sakaguchi on bipartite networks exhibits continuous/discontinuous transitions to partial synchrony with self-organized quasiperiodicity (arXiv: 2606.20345)
  - In PS regime, global oscillations fail to entrain one population whose oscillators display quasiperiodic dynamics
  - Models excitatory-inhibitory coexistence in neuronal systems with minimal bipartite structure
  - **Activation**: bipartite oscillator synchronization, Kuramoto Sakaguchi partial synchrony, self-organized quasiperiodicity, excitatory inhibitory dynamics, phase transitions

### Human-like Object Grouping in Self-supervised Vision Transformers
- [[human-like-object-grouping]] - Behavioral benchmark shows DINO-trained vision transformers achieve strongest alignment with human object segmentation; Gram matrix distillation improves alignment (arXiv: 2603.13994)
  - Novel metric quantifies object-centric component of representations via within/between-object patch similarity
  - Gram matrix structure drives perceptual alignment with human behavior
  - **Activation**: human-like object grouping, self-supervised vision transformers, DINO object segmentation, Gram matrix perceptual alignment, psychophysics benchmark

### Mass Conservation as Inductive Bias for Self-Organized Criticality in NCA Reservoirs
- [[mass-conservation-nca-reservoir-criticality]] - Mass conservation as inductive bias toward self-organized criticality in NCA reservoirs, 1.27× faster evolution (arXiv: 2606.23115)
  - Mass conservation promotes SOC without sacrificing downstream performance
  - Comparable performance on memory, classification, and temporal control tasks
  - **Activation**: self-organized criticality, neural cellular automata, reservoir computing, mass conservation, criticality

## 2026-07-11 - Neuroscience Research (Cron Job) Batch 2

### Efficient Perception in Automotive Detection and Tracking Using Neuromorphic Computing
- [[spike-yolo-automotive-perception]] - First comprehensive evaluation of SNNs for real-world automotive multi-object detection and tracking using SpikeYOLO (arXiv: 2607.04921)
  - Transfer learning from ANN-YOLO to SNN achieves mAP 0.937 (KITTI) and 0.771 (BDD100K MOT2020) for detection
  - HOTA 0.701 (KITTI) and 0.445 (BDD100K) for tracking — competitive with conventional deep learning
  - Energy-efficient edge deployment for autonomous vehicles and ADAS systems
  - **Activation**: SpikeYOLO, neuromorphic automotive perception, SNN object detection tracking, energy-efficient edge, KITTI neuromorphic

### The Pathwise Approach to Metastability and its Applications to Galves-Löcherbach Models
- [[pathwise-metastability-galves-locherbach]] - Comprehensive review of pathwise metastability theory for stochastic spiking neural network models (arXiv: 2607.05652)
  - Unifies metastability theory from chemistry to probability theory applied to GL model family
  - Self-contained proofs and identification of open problems in SNN metastability
  - Foundation for understanding metastable states in neural dynamics
  - **Activation**: metastability spiking neural networks, Galves Locherbach model, pathwise metastability, stochastic spiking networks, rare fluctuation
## 2026-07-11 - arXiv Paper Skills (Cron Job)

### SLORR: Simple and Efficient In-Training Low-Rank Regularization
- [[slorr-in-training-low-rank-regularization]] - Stateless, architecture-preserving low-rank regularization using Hoyer sparsity and nuclear norm for neural network compression with <8% training overhead (arXiv: 2607.08754)
  - GPU-friendly approximations for forward/backward passes; LLM pretraining at 135M and 560M scales
  - **Activation**: SLORR, low-rank regularization, Hoyer sparsity, nuclear norm, model compression, LLM pretraining compression

### ARDY: Autoregressive Diffusion with Hybrid Representation for Interactive Human Motion Generation
- [[ardy-autoregressive-diffusion-interactive-human-motion]] - Streaming generation framework for real-time 3D human motion controllable via text prompts and kinematic constraints (arXiv: 2607.08741)
  - Two-stage autoregressive transformer denoiser with variable history context; hybrid root+latent representation
  - **Activation**: ARDY, autoregressive diffusion motion, streaming motion generation, real-time 3D motion, text-to-motion

### Pose-to-Biomechanics: Bridging 3D Human Pose Estimation and Biomechanical Attribute Prediction
- [[pose-to-biomechanics-bridging-3d-pose-biomechanical]] - BioModule: lightweight plug-in temporal transformer for biomechanical attribute prediction from 3D skeletons (arXiv: 2607.08725)
  - Estimator-agnostic; bridges vision-based pose estimation to biomechanically meaningful motion analysis
  - **Activation**: Pose-to-Biomechanics, BioModule, biomechanical attribute prediction, 3D pose estimation, clinical movement analysis

### When Structured Sparse Autoencoders Learn Consistent Concepts Across Modalities
- [[structured-sparse-autoencoders-cross-modal-concepts]] - S²AE: Structured Sparse AutoEncoder enforcing concept consistency in vision-language models with attention-based patch grouping (arXiv: 2607.08605)
  - 6.06% improvement in semantic alignment on Qwen2.5-VL-7B; 60.81 l0 norm representational efficiency
  - **Activation**: Structured Sparse Autoencoder, S²AE, concept consistency multimodal, mechanistic interpretability, monosemanticity

### Cognitive-structured Multimodal Agent for Multimodal Understanding, Generation, and Editing
- [[cognitive-structured-multimodal-agent-understanding-generation]] - CMA with Episodic Visual Memory for long-horizon multimodal dialogue; 8B agent achieves 91.4% retrieval over 20-turn sessions (arXiv: 2607.08497)
  - Perceptual Abstraction Engine + Cognitive Retrieval Engine + Multimodal Executive Controller; CMA-Harness tool-augmented deployment
  - **Activation**: Cognitive-structured Multimodal Agent, CMA, episodic visual memory, long-horizon multimodal dialogue, CMA-Harness

### Beyond Backpropagation: Monte Carlo Method Can Train Deep Neural Networks
- [[beyond-backpropagation-monte-carlo-train-deep-networks]] - Simple Monte Carlo random mutation can train deep networks without gradients, no batchnorm or residual connections needed (arXiv: 2607.08406)
  - Supports pure pruning training, discrete weights, unconventional transfer functions; 20+ layer networks and Transformers
  - **Activation**: Monte Carlo training, gradient-free deep learning, random mutation training, beyond backpropagation, discrete weight training

### DrugGen 2: A disease-aware language model for enhancing drug discovery
- [[druggen-2-disease-aware-language-model-drug-discovery]] - Disease-conditioned molecule generation via fine-tuned GPT-2 with SFT + GRPO; outperforms baselines on diabetic nephropathy targets (arXiv: 2607.08404)
  - Disease ontology + target protein sequence conditioning; molecular docking validates strong binding potential
  - **Activation**: DrugGen-2, disease-aware drug discovery, GPT-2 molecule generation, GRPO drug design, de novo drug design

### On Exploring Input Resolution Scaling For Anytime LiDAR Object Detection
- [[anytime-lidar-resolution-scaling-object-detection]] - Anytime computing for LiDAR 3D object detection with multi-resolution single-model inference and deadline-aware scheduler (arXiv: 2607.08391)
  - Dynamically scales input resolution; collision-free navigation in simulated autonomous driving
  - **Activation**: anytime LiDAR detection, input resolution scaling, multi-resolution inference, deadline-aware scheduler, cyber-physical anytime computing

### WCog-VLA: A Dual-Level World-Cognitive Vision-Language-Action Model for End-to-End Autonomous Driving
- [[wcog-vla-dual-level-world-cognitive-autonomous-driving]] - Dual-level World-Cognitive VLA bridging semantic forecasting with generative world evolution; SOTA PDMS 92.9 on NAVSIM (arXiv: 2607.08375)
  - Game-theoretic Chain-of-Thought reasoning + Aligned Decoupled Diffusion Transformer (ADDT) for multi-agent trajectories
  - **Activation**: WCog-VLA, World-Cognitive VLA, vision-language-action autonomous driving, Game-CoT, ADDT, proactive autonomous driving

### Large-Language-Models-as-a-Judge in Theory-Agnostic Adaptive Metric-Alignment for Personality Recognition
- [[llm-judge-theory-agnostic-personality-recognition]] - JAM: theory-agnostic personality recognition with LLM-as-a-Judge, Attention-Pooled Graph Prototypical Network, and Cross-Theory Harmonization (arXiv: 2607.08374)
  - LLM-before-the-loop and LLM-in-the-loop configurations for ambiguous sample identification
  - **Activation**: JAM personality recognition, LLM-as-a-Judge, theory-agnostic personality, prototypical network, cross-theory harmonization

### Self-Adaptive Anomaly Detection with Reinforcement Learning and Human Feedback in Connected Vehicles
- [[self-adaptive-anomaly-detection-rl-human-feedback-vehicles]] - Online anomaly detection for connected vehicles with factorized DQN, drift detectors, and human-in-the-loop retraining; F1 0.69 vs 0.11 (arXiv: 2607.08373)
  - Sustained adaptation after concept drift: F1 recovers from 0.52 to 0.65 without catastrophic forgetting
  - **Activation**: self-adaptive anomaly detection, RL anomaly detection, connected vehicles, human-in-the-loop, concept drift, factorized DQN
 (feat: add 13 paper skills from arXiv 2026-07-11)

## 2026-07-10 - Neuroscience Research (Cron Job)

### DBNN: Neural Spike Classification Using a Deep Binarized Neural Network
- [[dbnn-spike-classification]] - Hardware-efficient neural spike classification with multiplier-free inference, achieving 98.7% accuracy with 0.014 mm² area and 122 nW power at 20 kHz (arXiv: 2607.05590)
  - Uses sign-controlled accumulation and bit-wise logic for implantable brain-computer interfaces
  - FPGA prototype: 828 ALMs, 1023 registers, 0 DSP blocks; ASIC: 0.014 mm², 122 nW @ 20 kHz
  - **Activation**: DBNN, spike sorting, binarized neural network, brain-computer interface, FPGA implementation, ASIC design, neural decoding, implantable devices

## 2026-07-10 - Number Theory, Statistics, Advanced Mathematics + Quantum (Cron Job)

### Analysis of the Sample Complexity for PAC-Learning Functions Defined over Quantum States
- [[quantum-pac-learning-theory]] - Analyzes sample complexity in quantum PAC-learning models where concepts are functions acting on quantum states, extending VC-dimension to quantum superposition examples (arXiv: 2607.07572)
  - Extends classical VC-dimension bounds to quantum superposition-based examples
  - Derives labeled example requirements for quantum concept classes with target accuracy/confidence
  - **Activation**: quantum PAC learning, quantum sample complexity, quantum VC dimension, quantum concept class, quantum function learning

### Towards Minimax Estimation of High-Order Functionals by Quantum Arguments
- [[quantum-minimax-estimation]] - Novel minimax estimation of high-order functionals (F_alpha(P) = sum p_i^alpha, tr(rho^alpha)) using quantum computing, connecting classical and quantum functionals to Renyi and Tsallis entropy (arXiv: 2607.07540)
  - Constructs estimators for both classical and quantum functionals using quantum arguments
  - Bridges minimax statistics with quantum computing for entropy estimation
  - **Activation**: quantum minimax estimation, quantum functional estimation, Renyi entropy, Tsallis entropy, quantum distribution estimation

### Faster Quantum Linear System Solver Beyond the Condition Number
- [[quantum-linear-system-beyond-condition]] - Two quantum algorithms solving Ax=b with complexity independent of the spectral condition number, using block encoding input model (arXiv: 2607.07691)
  - Breaks the traditional condition number bottleneck in quantum linear system solvers
  - Uses standard block encoding for matrix access and state preparation
  - **Activation**: quantum linear system solver, quantum condition number, block encoding quantum, HHL alternative, quantum linear algebra

### Error Bounds for the Truncated BCH and Zassenhaus Formulas in Unitary Problems
- [[bch-zassenhaus-error-bounds]] - Rigorous error bounds for truncated Baker-Campbell-Hausdorff and Zassenhaus formulas in unitary quantum problems, essential for quantum circuit decomposition accuracy (arXiv: 2607.07692)
  - Provides truncation error analysis for BCH and Zassenhaus formulas
  - Applies to quantum evolution operators and Trotter-Suzuki approximation
  - **Activation**: BCH formula error bounds, Zassenhaus formula, quantum unitary evolution, nested commutators, quantum operator splitting

### Human-AI Co-Discovery of Sign-Embedding Quantum Algorithms
- [[human-ai-co-discovery-quantum-algorithms]] - Human-AI co-discovery methodology for quantum algorithm design, demonstrated via sign-embedding quantum algorithms for matrix equations and functions (arXiv: 2606.24899)
  - AI expands human intuition into route maps, compares formulations, drafts proofs
  - Human gates: selects routes, rejects hidden conditions, refines implementations

## 2026-07-24 - Deep Learning Research (Cron Job)

### ELSAA: Efficient Low-Rank and Sparse Attention Approximation for Training Transformers
- [[elsaa-efficient-low-rank-sparse-attention]] - Efficient attention mechanism combining sparse and low-rank approximations to enable longer-context training while preserving both sharp token-level interactions and broad contextual mixing (arXiv: 2607.20214v1)
  - Dual-branch architecture: sparse branch captures high-similarity interactions, low-rank branch summarizes diffuse global interactions
  - Denominator-aware fusion scales sparse branch according to estimated attention mass relative to low-rank branch
  - **Activation**: ELSAA, efficient attention, low-rank attention, sparse attention, long-context transformers

### HeadCast: Casting Attention Heads for Efficient Autoregressive Video Generation
- [[headcast-attention-heads-video-generation]] - Training-free attention head classification and KV cache optimization framework that accelerates autoregressive video generation by up to 1.95x at 1080P while maintaining quality (arXiv: 2607.20125v1)
  - Four head archetypes: Sink, Dummy, Spatial, and Global heads with head-specific pathways
  - Retains Global heads to preserve long-range temporal consistency that aggressive eviction destroys
  - **Activation**: HeadCast, video generation, attention heads, KV cache optimization, autoregressive diffusion

### PoTRE: Test-Time Reasoning inspired by Cognitive Heterogeneity
- [[potre-cognitive-heterogeneity-reasoning]] - Heterogeneous multi-agent reasoning framework (Poly-Topological Reasoning Ensembles) that decouples inference into four specialized agents for complex reasoning tasks (arXiv: 2607.20268v1)
  - Four agents: Adversarial Refinement, Hierarchical Planning, Spectrum Search, and Direct Chain agents
  - Task-Adaptive Aggregation Layer dynamically reconciles perspectives via candidate selection, semantic synthesis, or neuro-symbolic verification
  - **Activation**: PoTRE, cognitive heterogeneity, multi-agent reasoning, poly-topological ensembles, adversarial refinement

### Language-Specific versus Cross-Lingual Knowledge Graphs for Implicit Aspect Identification in Arabic
- [[language-specific-vs-cross-lingual-knowledge-graphs]] - Comparative methodology showing native language knowledge graphs outperform cross-lingual English KGs by +0.199-0.251 micro-F1 for implicit aspect identification in Arabic (arXiv: 2607.20056v1)
  - Native Arabic KGs consistently outperform cross-lingual English KGs across multiple benchmarks
  - Task-specific fine-tuning raises performance from <=0.13 to 0.66-0.76 micro-F1, confirming task adaptation over model scale
  - **Activation**: knowledge graphs, multilingual NLP, aspect-based sentiment, implicit aspects, Arabic NLP
