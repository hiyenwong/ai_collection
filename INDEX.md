## 2026-07-31 - Neuroscience Research (Cron Job)

### ZUNA1.1: A more flexible EEG foundation model for Denoising and Super-resolution
- [[zuna1-1-flexible-eeg-foundation-model]] - A 380M-parameter diffusion autoencoder for flexible EEG signal reconstruction with arbitrary channel configurations and temporal intervals (arXiv: 2607.27308)
  - Handles variable length sequences up to 30s with arbitrary numbers of EEG channels at arbitrary scalp locations
  - Can reconstruct arbitrary temporal intervals within channels in addition to entire channels
  - Outperforms standard EEG denoising methods like spherical spline interpolation while maintaining flexibility
  - **Activation**: zuna1.1 eeg foundation model, flexible eeg denoising, eeg super-resolution diffusion, arbitrary channel eeg reconstruction, variable length eeg diffusion## 2026-07-31 - Quantum Computing Research (Cron Job)

### Practical Quantum Topological Data Analysis with Applications to High-Dimensional Feature Extraction and Time Series Analysis
- [[practical-quantum-topological-data-analysis]] - Quantum TDA as a feature-extraction method using low-order spectral information from the combinatorial Laplacian as a proxy for high-dimensional topology. (arXiv: 2607.27206)
  - Higher-order TDA features improve predictive performance in fMRI analysis for neurodegenerative disease classification and financial time-series analysis for market instability detection
  - Low-order moments (including relative trace) strongly correlate with high-dimensional Betti information, even when relative Betti number is small
  - Includes circuit constructions, resource estimates, quantum-classical crossover projections, and experimental results from a Barium development system
  - **Activation**: quantum TDA, topological data analysis, quantum feature extraction, Laplacian moments, Betti numbers, time series analysis, fMRI analysis

## 2026-07-31 - Systems Engineering Research (Cron Job)

### A Physics-Informed Framework for PID Tuning of Chemical Processes Using Large Language Model Agents
- [[physics-informed-llm-pid-tuning]] - A physics-informed framework that uses Large Language Model agents for PID tuning of chemical processes, combining closed-loop response features, control-engineering diagnoses, and physics-informed reinforcement learning. (arXiv: 2607.26594)
  - Hosted LLMs (DeepSeek-V4-Flash, Qwen3.7-Plus) achieve 75-89% success rate on FOPDT cases and 77-79% on SOPDT cases
  - Local SLM (Qwen3-0.6B) with SFT achieves 86.5% first-recommendation success, improved to 94.0% with PI-GRPO
  - Combines engineer-like workflow formalization with physics-informed constraints and iterative correction
  - **Activation**: PID tuning, chemical process control, physics-informed LLM, control system optimization, process control

## 2026-07-31 - Neuroscience Research (Cron Job)

### EEG Foundation Models Lose Long-Range Temporal Correlations: A Spectral-Temporal Dissociation Behind Their Cross-Population Fragility
- [[eeg-foundation-temporal-correlations-blindness]] - EEG foundation models lose long-range temporal correlations: framework for analyzing spectral-temporal dissociation and cross-population fragility in EEG foundation models. Provides methodology for testing LRTC recovery via DFA exponent and evaluating cross-cohort transfer performance. (arXiv: 2607.24834)
  - None of five tested EEG FMs represented LRTC; raw-waveform models failed on both DFA and 1/f slope
  - Spectral-input models recovered 1/f slope strongly (R²=0.59-0.73) but not DFA across cohorts
  - Classical DFA feature recovered exponent (R²=0.32-0.38); LRTC orthogonal to aperiodic slope (r=-0.06)
  - All FMs dominated by recording-site axis (0.98-1.00 vs 0.500 chance); DFA exponent site-robust (0.71)
  - **Activation**: eeg foundation models, long-range temporal correlations, dfa exponent, spectral-temporal dissociation, cross-population fragility, site robustness

### The Sparsity Ceiling: Where Spiking Networks Can and Cannot Trade Activity for Energy
- [[sparsity-ceiling-spiking-networks-energy]] - The Sparsity Ceiling methodology for analyzing energy-efficiency limits in spiking neural networks based on task characteristics and architectural constraints. Provides information-theoretic bounds on firing rates based on memory load, state width, and task difficulty. (arXiv: 2607.26648)
  - Information-theoretic bound ρ >= H_b^{-1}(log2 M / H) predicts minimum firing rates
  - Feed-forward perception: 5% firing, no accuracy cost; Recurrent LM: ~50% minimum; Spiking Transformer: 2% firing
  - Attention trades firing floor for memory wall (full key-value cache storage)
  - Event-driven perception isolated as primary domain where neuromorphic hardware wins
  - **Activation**: sparsity ceiling, spiking neural networks, energy efficiency, neuromorphic computing, firing rate limits, memory-computation tradeoff, event-driven perception, recurrent compression

### Reconstructing Backpropagation from Forward Fluctuations in Noise-modulated Neural Networks
- [[reconstructing-backpropagation-noise-modulated-networks]] - Methodology for reconstructing backpropagation-like learning without weight transport by using noise-modulated neural networks that estimate gradients from forward-pass statistics. Solves the weight transport problem through local differential estimation. (arXiv: 2607.26483)
  - Uses weight mirror + local differential estimation to approximate gradient signals
  - Leverages noise-modulated networks to extract gradient information from forward fluctuations
  - Enables biologically plausible backpropagation without requiring symmetric feedback pathways
  - Demonstrates successful learning on standard benchmarks without explicit error backpropagation
  - **Activation**: reconstructing backpropagation, noise-modulated networks, weight transport problem, biologically plausible learning, local differential estimation, forward fluctuation gradients

## 2026-07-31 - Deep Learning Research (Cron Job)

### TurboVLA: Real-Time Vision-Language-Action Model at 32 Hz on an RTX 4090 with <1 GB VRAM
- [[turbovla-real-time-vla]] - TurboVLA architecture for real-time vision-language-action models achieving 32 Hz inference with <1 GB VRAM. Reformulates conventional V→L→A pathway as direct V+L→A mapping with lightweight bidirectional vision-language interaction. (arXiv: 2607.27205)
  - Direct V+L→A mapping avoids LLM-centric overhead, achieving 31.2 ms latency and 0.9 GB VRAM usage
  - 97.7% average success on LIBERO with only 0.2B parameters, matching larger VLA policies
  - Lightweight bidirectional vision-language interaction enables task-conditioned representations
  - **Activation**: TurboVLA, real-time VLA, vision-language-action efficiency, robotic manipulation real-time, sub-1GB VRAM robotics, V+L→A mapping, lightweight VLA, consumer GPU robotics, 32 Hz inference, compact VLA decoder

### Metis: Memory Foundation Model
- [[metis-memory-foundation-model]] - Metis Memory Foundation Model framework for native memory capabilities in foundation models. Introduces persistent dynamically evolving memory state within backbone and native memory procedures for autonomous information storage/utilization. (arXiv: 2607.26760)
  - Native memory formalized as persistent memory state + autonomous memory procedures through computation
  - Gradient-free online memory maintenance requiring only forward pass, with all weights frozen during inference
  - Large-scale memory-specific training data with multiple optimization objectives acquires native memory procedures
  - **Activation**: Metis memory foundation model, native memory capabilities, frozen-weight memory inference, gradient-free memory maintenance, memory attention mechanisms, autonomous memory transformation, internalized agent memory, memory state compression, foundation model memory, AI agent native memory## 2026-07-30 - Neuroscience Research (Cron Job)

### The Sparsity Ceiling: Where Spiking Networks Can and Cannot Trade Activity for Energy
- [[sparsity-ceiling-spiking-networks-energy]] - The Sparsity Ceiling framework for analyzing where Spiking Neural Networks can and cannot trade activity for energy efficiency. Provides information-theoretic bounds on firing rates based on memory load, state width, and task difficulty. (arXiv: 2607.26648)
  - Information-theoretic bound ρ >= H_b^{-1}(log2 M / H) predicts minimum firing rates
  - Feed-forward perception: 5% firing, no accuracy cost; Recurrent LM: ~50% minimum; Spiking Transformer: 2% firing
  - Attention trades firing floor for memory wall (full key-value cache storage)
  - Event-driven perception isolated as primary domain where neuromorphic hardware wins
  - **Activation**: sparsity ceiling, SNN energy efficiency, neuromorphic hardware limits, firing rate bounds, spiking transformer efficiency, recurrent vs attention energy, event-driven perception, memory load sparsity, information-theoretic bounds

### Foundation Models for EEG Are Blind to Long-Range Temporal Correlations: A Spectral-Temporal Dissociation Behind Their Cross-Population Fragility
- [[eeg-fm-temporal-correlations-blindness]] - EEG foundation models lose long-range temporal correlations (LRTC) in their embeddings, creating a spectral-temporal dissociation that limits cross-population transfer (arXiv: 2607.24834)
  - Raw-waveform models recover neither DFA exponent nor 1/f slope (R² ≤ 0.12)
  - Spectral-input models recover 1/f strongly (R² = 0.59-0.73) but not DFA across cohorts
  - All five FMs dominated by recording-site axis (decodable at 0.98-1.00 vs. 0.500 chance)
  - **Activation**: EEG foundation models, Long-range temporal correlations, DFA exponent, Cross-population transfer, Spectral-temporal dissociation

### A Path Integral Model of Cognition
- [[path-integral-cognition-model]] - Path Integral Model of Cognition methodology combining quantum physics path integrals with cognitive cost optimization using imaginary-time evolution under projector Hamiltonians and Wick rotation for unitary equivalent representation (arXiv: 2607.24807)
  - Imaginary-time evolution coincides with double-bracket flow as Riemannian gradient flow of Hilbert-Schmidt cost
  - Wick rotation provides equivalent unitary evolution with exact discrete path-integral representation
  - Consciousness continuum mapped to system-environment coupling strength: weak coupling → GKSL decoherence (unconscious), strong coupling → projective fixation ("Aha" insight)
  - **Activation**: path integral cognition, imaginary time evolution cognition, Wick rotation consciousness, projector Hamiltonian cognition, GKSL cognitive model
## 2026-07-25 - Neuroscience Research (Cron Job)

### CogniSNN: Enabling Neuron-Expandability, Pathway-Reusability, and Dynamic-Configurability with Random Graph Architectures in Spiking Neural Networks
- [[cognisnn-random-graph-architecture]] - CogniSNN framework for scalable spiking neural networks with random graph architectures enabling neuron-expandability, pathway-reusability, and dynamic-configurability (arXiv: 2512.11743)
  - Introduces Random Graph Architecture (RGA) to overcome rigid hierarchical limitations of traditional ANNs
  - Implements Key Pathway-based Learning without Forgetting (KP-LwF) using Betweenness Centrality for continual learning
  - Features Dynamic Growth Learning (DGL) algorithm for temporal dimension structural plasticity
  - **Activation**: cognisnn, random graph architecture, neuron expandability, pathway reusability, dynamic configurability

### Event-driven eligibility propagation in large sparse networks: efficiency shaped by biological realism
- [[event-driven-eligibility-propagation]] - Event-driven learning in sparse SNNs showing biological realism (sparsity, irregularity) drives 10-15x computational efficiency vs dense backpropagation (arXiv: 2511.21674)
  - Translates time-driven eligibility propagation into event-driven for large-scale spiking networks
  - Integrates biologically plausible features: continuous dynamics, strict locality, sparse connectivity
  - Demonstrates scalability to millions of neurons without compromising learning performance
  - **Activation**: event-driven eligibility propagation, sparse SNNs, biological realism, computational efficiency

### Sparse by Rule: Probability-Based N:M Pruning for Spiking Neural Networks
- [[nm-pruning-spiking-neural-networks]] - First SNN-oriented semi-structured N:M pruning framework (SpikeNM) that learns sparse SNNs from scratch with at most N non-zeros per M-weight block (arXiv: 2511.12097)
  - Uses M-way basis-logit parameterization with differentiable top-k sampler for linear complexity
  - Implements eligibility-inspired distillation (EID) to align mask probabilities with spiking dynamics
  - Maintains or improves accuracy at 2:4 sparsity while yielding hardware-amenable patterns
  - **Activation**: nm pruning, spikeNM, semi-structured pruning, spiking neural networks

### Spectral theory for population density dynamics of spiking neurons with refractoriness
- [[spectral-theory-spiking-neurons-refractoriness]] - Rigorous operator-theoretic framework for analyzing spiking neuron population dynamics with absolute refractory periods using non-self-adjoint boundary eigenvalue problems and spectral decomposition methods (arXiv: 2607.20699)
  - Complete spectral characterization of Fokker-Planck generator proving dissipativity and contraction semigroup existence
  - Identifies defective eigenvalues as exceptional points where oscillatory modes emerge from coalescing relaxational modes
  - Derives exact transfer function accounting for boundary conditions modulated by external input
  - **Activation**: spectral theory, population density, spiking neurons, refractoriness, Fokker-Planck, non-self-adjoint, boundary eigenvalue problem

### Action potentials and solitons
- [[action-potentials-solitons]] - Framework for understanding nerve pulse propagation using soliton theory, connecting nonlinear wave dynamics to action potential generation and propagation in neurons (arXiv: 2607.20496)
  - Solitons as stable, localized wave packets maintaining shape during neural propagation
  - Provides physical insights into pulse stability and propagation speed complementing Hodgkin-Huxley models
  - Enables alternative modeling approaches for action potential propagation and energy efficiency analysis
  - **Activation**: action potentials solitons, nerve pulse propagation, soliton neuroscience, nonlinear wave neurons, solitary waves action potentials

## 2026-07-25 - Quantum Neuromorphic Computing (Cron Job)

### Quantum-Driven Neuromorphic Computing for Million-Qubit Scale Systems
- [[quantum-driven-neuromorphic-million-qubit]] - Quantum-Driven Neuromorphic Computing methodology for million-qubit scale systems. Integrates quantum computing principles with neuromorphic architectures to achieve scalable, energy-efficient computation at million-qubit scales.
  - Quantum-enhanced spiking neurons using superposition and entanglement for information processing
  - Hierarchical architecture enabling million-qubit scalability with error-corrected quantum memory
  - Energy-efficiency optimization through coherent dynamics and topological protection
  - **Activation**: quantum neuromorphic, million-qubit, quantum-driven neuromorphic

## 2026-07-25 - Systems Engineering Research (Cron Job)

### Toward Federated Cognitive Digital Twins over the Edge-to-Cloud Continuum
- [[federated-cognitive-digital-twins-edge-cloud]] - Federated Cognitive Digital Twin (FCDT) architecture methodology combining federation and cognition within a unified approach for distributed Cyber-Physical Systems (CPSs) (arXiv: 2607.21357)
  - Combines federated digital twins (scalability) with cognitive digital twins (semantic reasoning) in unified architecture
  - Distributes intelligence across edge-to-cloud continuum through local twins (real-time monitoring) and global twins (system-level reasoning)
  - Improves scalability, responsiveness, and decision-making in complex distributed CPSs like smart cities
  - **Activation**: federated digital twins, cognitive digital twins, edge-to-cloud continuum, distributed CPS, semantic reasoning, autonomous coordination

## 2026-07-25 - Neuroscience Research (Cron Job)

### Search Hardness-Aware LLM-Based Problem Formulation for Expensive Simulation-Driven Design
- [[search-hardness-aware-llm-problem-formulation]] - Search Hardness-Aware LLM-Based Problem Formulation (SHA-PF) framework that prioritizes formulations guiding efficient search by focusing on rare samples with greater progress potential, significantly reducing evaluation requirements in expensive simulation-driven design (arXiv: 2607.21220)
  - Moves beyond design-intent alignment to consider search process efficiency in problem formulation
  - Defines formulation search objective guided by search hardness, scoring candidates by progress potential
  - Demonstrates significant evaluation reduction on real-world multi-objective and antenna design benchmarks
  - **Activation**: search hardness awareness, LLM problem formulation, expensive simulation design, SHA-PF framework, rare sample prioritization

### Weight-norm Criticality: A Mechanism for Loss Spikes Induced by the Normalization and Weight Decay
- [[weight-norm-criticality-loss-spikes]] - Weight-norm Criticality framework for understanding loss spikes in deep neural network training induced by the interaction between normalization and weight decay (arXiv: 2607.21005)
  - Identifies weight-norm criticality as additional training instability beyond learning-rate criticality
  - Explains how normalization introduces scale-invariant components that interact with weight decay to cause loss spikes
  - **Activation**: weight-norm criticality, loss spikes, weight decay instability, normalization weight decay interaction, scale-invariant training dynamics

### Spectral theory for neuronal population dynamics with refractory time
- [[spectral-theory-neuronal-population-dynamics]] - Spectral theory framework for analyzing population density dynamics of spiking neurons with finite refractory time, providing rigorous operator-theoretic methods for studying neuronal population stability and oscillatory modes (arXiv: 2607.20699)
  - Augments state space to include refractory history and formulates as non-self-adjoint boundary eigenvalue problem for Fokker-Planck operator
  - Proves dissipativity and existence of contraction semigroup, identifies defective eigenvalues as exceptional points where oscillatory modes emerge
  - Derives exact transfer function accounting for boundary conditions and reveals additional threshold-noise contributions
  - **Activation**: spectral theory neuronal population, refractory period population dynamics, Fokker-Planck boundary eigenvalue, neuronal oscillatory modes, population transfer function

### Current Injection Spiking Neural Network for Infrared and Visible Image Fusion
- [[current-injection-spiking-neural-network-image-fusion]] - Spiking neural network architecture that performs cross-modal fusion at membrane-potential level using current injection spiking (CIS) operator, solving subthreshold information loss in infrared-visible image fusion while maintaining energy efficiency (arXiv: 2607.19879)
  - Introduces Current Injection Spiking (CIS) operator that injects one modality as gated auxiliary current into driving neuron of other before spike firing
  - Preserves subthreshold responses containing complementary cues that would be lost in binary spike communication
  - Achieves fusion quality on par with state-of-the-art ANNs while reducing inference energy by order of magnitude
  - **Activation**: current injection spiking, CIS-Fuse, infrared visible fusion, membrane potential fusion, SNN image fusion

  ## 2026-07-24 - Neuroscience Research (Cron Job)

  ### Transition-Related Potentials as Markers of Narrative Comprehension in Continuous EEG
  - [[transition-related-potentials-narrative-comprehension-eeg]] - Extracts Transition-Related Potentials (TRPs) from continuous EEG aligned to cinematic transitions, demonstrating narrative context sensitivity and semi-automated detection using deep neural networks (arXiv: 2607.20720)
    - Naturalistic paradigm moves beyond traditional ERP by analyzing continuous EEG during film viewing
    - TRPs exhibit canonical ERP-like temporal structure systematically shaped by narrative coherence vs. scene-scrambled versions
    - Compact DNN recovers cut-related EEG signatures directly from group-averaged continuous recordings
    - **Activation**: transition-related potentials, narrative comprehension EEG, continuous EEG analysis, cinematic transitions EEG, naturalistic neuroscience, TRP detection, film narrative EEG

  ### Spectral theory for population density dynamics of spiking neurons with refractoriness
  - [[spectral-theory-population-density-spiking-neurons]] - Rigorous operator-theoretic framework for neuronal population dynamics with finite refractory time, providing complete spectral characterization and exact transfer functions (arXiv: 2607.20699)
    - Formulates Fokker-Planck operator as non-self-adjoint boundary eigenvalue problem
    - Identifies defective eigenvalues as exceptional points where oscillatory modes emerge
    - Derives exact transfer function with threshold-noise contributions missed in previous work
    - **Activation**: spectral theory, population density, spiking neurons, refractoriness, Fokker-Planck operator, oscillatory modes, transfer function

  ### Perspective Latents as an Architectural Condition for Causal Emergence in Active Inference Agents
  - [[perspective-latents-causal-emergence-active-inference]] - Framework for measuring causal emergence in active inference agents through Integrated Information Decomposition, identifying global latents as architectural locus of temporal organization (arXiv: 2607.20708)
    - Separates fast perception latent (z) from slow global latent (g) with structural decoupling from policy gradients
    - Demonstrates ΦID concentration in global latent (g) with aggregate magnitude being largely architectural
    - Reveals substantive learning effects only at atom-compositional level with regime-invariant decoupling
    - **Activation**: causal emergence, active inference, integrated information decomposition, perspective latents, temporal organization, architectural conditions

  ## 2026-07-24 - Systems Engineering Research (Cron Job)

  ### Systems Engineering Research Search - July 24, 2026
  - **No new papers found** in systems engineering domain (arXiv: systems engineering, distributed systems, control systems, cyber-physical systems)
    - Search conducted for papers published July 17-24, 2026
    - No results due to academic publishing cycles and arXiv rate limiting
    - **Activation**: systems engineering research, arxiv search monitoring

### SpikingMOT: A Spike-Driven Multi-Object Tracker
- [[spikingmot-spike-driven-multi-object-tracker]] - Spike-driven multi-object tracker using brain-inspired spiking neural networks with Activation Sparsity Preference (ASP) for efficient trajectory prediction, achieving SOTA performance with 72% fewer parameters and 86.7% less energy (arXiv: 2607.19875)
  - Introduces Activation Sparsity Preference (ASP): sparse gating is no worse than dropout under same activation rate
  - Implements brain-inspired tracking loop with pseudo-trajectory bases and error-calibrated posterior
  - **Activation**: SpikingMOT, spike-driven tracking, activation sparsity preference, SNN MOT

### Visual Semantic Decoding of Electrocorticography from Video Stimuli using End-to-End Deep Learning
- [[visual-semantic-decoding-ecog]] - End-to-end deep learning framework for decoding visual semantic categories from ECoG brain signals during video viewing using Transformer-based models with high-gamma band inputs (arXiv: 2607.18923v1)
  - Uses mixup augmentation for limited training data (<50 samples per category)
  - Achieves promising decoding performance without handcrafted features
  - Key brain regions: early visual cortex (V2-V4), ventral stream, MT+ complex, lateral temporal cortex
  - **Activation**: visual semantic decoding, ECoG decoding, brain-computer interface, neural decoding, electrocorticography, visual category decoding, Transformer neural decoding, high-gamma decoding

### Is EEG-to-Text Feasible in Real-World Scenarios? An In-Depth Analysis Using a Neuropsychology-Inspired Benchmark
- [[eeg-to-text-real-world-feasibility]] - Neuropsychology-inspired COFETT benchmark enabling teacher-forcing-free EEG-to-text evaluation, addressing EEG instability issues and demonstrating practical feasibility for non-invasive communication restoration (arXiv: 2607.18749)
  - Introduces Corpus OF Eeg-To-Text (COFETT) with 128-channel high-density EEG for robust evaluation
  - Enables autonomous text generation without ground truth dependency, essential for real-world deployment
  - Provides state-of-the-art ability to distinguish model performances and validate EEG linguistic decodability
  - **Activation**: EEG-to-text feasibility, COFETT benchmark, teacher-forcing-free EEG2Text, non-invasive BCI communication, EEG instability decoding, real-world EEG2Text evaluation, high-density EEG language

- [[when-to-smell-in-stereo]] - Stereo olfaction utility analysis framework that determines when dual nostril sensing provides advantages over single nostril sensing based on odor concentration gradients and spatial correlation length scales (arXiv: 2607.20307)
  - Large relative changes in odor concentration enable stereo advantage
  - Large spatial correlation length scales (boundary layer near surfaces) favor stereo olfaction  
  - **Activation**: stereo olfaction, dual nostril sensing, odor trail tracking, boundary layer olfaction

### The Giant Hippocampus: From Structural Monoculture to a System of Systems
- [[giant-hippocampus-system-of-systems]] - Framework for designing heterogeneous AI architectures that avoid applying one architectural template (like Transformers) to all cognitive tasks, instead using structurally diverse modules with standardized interfaces (arXiv: 2607.19973)
  - Identifies the "giant hippocampus" problem: modern AI standardizes on architectural monocultures despite neuroscience showing different brain regions have qualitatively different structures
  - Proposes Heterogeneous Topological Network (HTN): System of Systems with distinct modules maintaining inductive biases and communicating through standardized interfaces  
  - Argues CNNs succeeded by encoding structural priors directly, but this lesson was abandoned for scale over structure
  - **Activation**: giant hippocampus, structural monoculture, heterogeneous topological network, system of systems, architectural diversity
## 2026-07-30 - Anthropic Research (Cron Job)

### A global workspace in language models
- [[global-workspace-j-space-analysis]] - Jacobian lens (J-lens) methodology for analyzing language model internal representations using the global workspace framework. Identifies conscious-accessible thoughts in LLMs through J-space patterns.
  - Uses J-lens technique to find internal activity patterns linked to future word predictions
  - Enables monitoring of hidden thoughts like recognizing fake scenarios or malicious intentions  
  - Allows intervention by editing J-space patterns to influence decision-making
  - **Activation**: j-space, jacobian lens, global workspace, LLM interpretability, conscious access

### Teaching Claude why
- [[teaching-claude-why-alignment-training]] - Alignment training methodology that teaches models to explain their reasoning rather than just correct actions. Uses "difficult advice" dataset and constitution training for robust alignment.
  - Focuses on ethical reasoning quality over action correctness
  - Uses out-of-distribution "difficult advice" scenarios where user faces ethical dilemmas
  - Directly trains on constitution document content for principled understanding
  - **Activation**: teaching claude why, alignment training, difficult advice, constitution training, ethical reasoning

### Agentic coding and persistent returns to expertise
- [[agentic-coding-expertise-framework]] - Framework for analyzing agentic coding sessions based on expertise levels, work modes, and success metrics. Shows domain expertise amplifies AI effectiveness more than coding proficiency.
  - Clear division: humans make 70% planning decisions, AI makes 80% execution decisions
  - Domain expertise enables 5x more output per prompt and better error recovery
  - Success determined by problem understanding, not coding training
  - **Activation**: agentic coding, claude code, returns to expertise, coding agents, human-ai collaboration