## 2026-07-27 - Neuroscience Research (Cron Job)

### Flow-based Phase-space Tomography of Continuous-variable Quantum States
- [[qst-flow-quantum-tomography]] - QST-Flow framework using flow-based generative modeling for continuous-variable quantum state tomography, with QST-QFlow for Husimi-Q functions and QST-WFlow for Wigner functions as difference of normalized flows (arXiv: 2607.21584)
  - Models phase-space quasiprobability distributions with normalized, samplable neural densities instead of truncated density matrices
  - Enables exact density evaluation, direct sampling, and importance-sampled learning from finite measurements without fixed grid
  - Benchmarks show accurate reconstruction of non-Gaussian cat, binomial, GKP, number, and Fock states with improved error over prior ML methods
  - **Activation**: qst-flow, quantum tomography flow, phase-space tomography, continuous-variable tomography, Wigner flow modeling

### Spectral theory for population density dynamics of spiking neurons with refractoriness
- [[spectral-theory-spiking-neurons-refractoriness]] - Spectral theory framework providing complete spectral characterization of Fokker-Planck operator generator, identifying defective eigenvalues as exceptional points for oscillatory modes, and deriving exact transfer function correcting prior heuristics (arXiv: 2607.20699)
  - Solves open problem of incorporating absolute refractory period into population density approaches via non-self-adjoint boundary eigenvalue problem
  - Proves dissipativity and contraction semigroup existence, reveals threshold-noise contributions missed by previous heuristic derivations
  - Demonstrates that refractoriness facilitates limit cycle onset (stable firing rate oscillations) in interacting neuron populations
  - **Activation**: spectral theory spiking neurons, refractoriness population density, Fokker-Planck boundary eigenvalue, defective eigenvalues neural oscillations, transfer function refractory period

## 2026-07-26 - Systems Engineering Research (Cron Job)

### Search Hardness-Aware LLM-Based Problem Formulation for Expensive Simulation-Driven Design
- [[search-hardness-aware-llm-problem-formulation]] - SHA-PF framework that optimizes problem formulations themselves rather than just algorithms, prioritizing rare samples with greater progress potential to reduce expensive simulation requirements (arXiv: 2607.21220)
  - Moves beyond design-intent alignment to consider search process efficiency in LLM-based problem formulation
  - Defines formulation search objective guided by search hardness, scoring candidates by their ability to identify high-potential regions
  - Validated on real-world multi-objective benchmarks and five expensive antenna design problems, showing significant evaluation reduction
  - **Activation**: search hardness awareness, LLM problem formulation, expensive simulation design, SHA-PF framework, rare sample prioritization

## 2026-07-26 - Neuroscience Research (Cron Job)

### Spectral theory for population density dynamics of spiking neurons with refractoriness
- [[spectral-theory-spiking-neurons-refractoriness]] - Rigorous operator-theoretic framework using non-self-adjoint boundary eigenvalue problems for Fokker-Planck operators to analyze spiking neuron populations with refractory periods (arXiv: 2607.20699)
  - Solves long-standing open problem of incorporating absolute refractory periods into population density approaches
  - Provides complete spectral characterization and identifies exceptional points where oscillatory modes emerge
  - Derives exact transfer function correcting previous heuristic derivations with additional threshold-noise contributions
  - Shows refractoriness can facilitate limit cycle onset in interacting neuron populations under mean-field approximation
  - **Activation**: spectral theory, spiking neurons, refractoriness, population density, Fokker-Planck

### Weight-norm Criticality: A Mechanism for Loss Spikes Induced by the Normalization and Weight Decay
- [[weight-norm-criticality-loss-spikes]] - Framework explaining loss spikes through weight-norm criticality caused by normalization-weight decay interactions, providing mechanistic understanding beyond learning-rate criticality (arXiv: 2607.21005)
  - Identifies critical boundary where excessive weight decay drives scale-invariant weight norms toward zero, destabilizing optimization
  - Explains why weight penalties improve generalization but cannot be made arbitrarily strong
  - Provides testable predictions validated empirically in networks with scale-invariant components
  - **Activation**: weight-norm criticality, loss spikes, weight decay instability, normalization criticality, scale-invariant components

### Spiking Tolman-Eichenbaum Machine: Biologically Realistic Hippocampal Model for Navigation and Planning
- [[spiking-tolman-eichenbaum-machine]] - sTEM implements cognitive maps and model-based planning using spiking neural networks with hippocampal-inspired architecture, supporting both navigation and flexible planning (arXiv: 2607.19835)
  - First biologically realistic implementation of Tolman-Eichenbaum machine using spiking neurons
  - Demonstrates how place cells and grid cells can support both reactive navigation and deliberative planning
  - Shows how replay mechanisms enable flexible route planning without explicit pathfinding algorithms
  - **Activation**: spiking Tolman-Eichenbaum, cognitive maps, hippocampal navigation, model-based planning, place cells

### Attractor Landscape Methodology for Working Memory in Neural Networks
- [[neuro-attractor-landscape-working-memory]] - Framework for analyzing working memory as attractor dynamics in recurrent neural networks, revealing how network structure shapes memory capacity and stability (arXiv: 2607.19423)
  - Connects network connectivity patterns to attractor landscape properties
  - Shows how different network motifs create different memory characteristics
  - Provides analytical tools for designing networks with specific memory properties
  - **Activation**: attractor landscape, working memory, recurrent networks, memory stability, network motifs

### Transition-Related Potentials as Markers of Narrative Comprehension in Continuous EEG
- [[trp-narrative-comprehension-eeg]] - Methodology for extracting transition-related potentials (TRPs) from continuous EEG during film viewing, demonstrating that narrative context shapes EEG responses detectable with deep neural networks (arXiv: 2607.20720)
  - Validates continuous EEG analysis as alternative to traditional trial-based ERP paradigms
  - Shows TRPs are systematically shaped by narrative context vs. scene-scrambled versions with matched sensory input
  - Provides semi-automated framework using compact DNNs that generalize across films and subject groups
  - Enables analysis of naturalistic cognitive processing closer to real-world experience
  - **Activation**: transition-related potentials, narrative comprehension, continuous EEG, cinematic cuts, naturalistic neuroscience

### Spiking Neural Network Analysis Framework
- [[spiking-neural-network-analysis]] - Comprehensive methodology for analyzing Spiking Neural Network (SNN) research papers, extracting technical patterns, implementation details, and performance benchmarks for practical application
  - Systematic approach to distilling SNN research into actionable engineering knowledge
  - Covers neuron models, learning algorithms, hardware considerations, and benchmark datasets
  - Includes templates for experimental replication and performance comparison
  - **Activation**: SNN analysis, spiking neural networks, neuromorphic computing, research distillation

### Memoir: Should a Model Write to Its Memory While It Thinks?
- [[memoir-memory-rewriting-neural-networks]] - Methodology comparing coupled memory rewriting vs read-only pondering architectures, showing memory rewriting causes learning-speed penalty but not capability penalty (arXiv: 2607.20792)
  - Tests riskiest coupling where pondering iterations rewrite the fast memory tier they read from
  - Demonstrates that coupled recall (0.5203) lags behind read-only recall (0.6557) at 240 training steps but both reach 1.0000 by 960 steps
  - Shows memory rewriting does not corrupt energy signal - energy margin grows and holds during training
  - Provides kernel restructuring reducing delta-rule forward time from 0.907 ms to 0.351 ms
  - **Activation**: memory rewriting, neural network inference, coupled memory, read-only pondering, learning speed penalty

## 2026-07-26 - Anthropic Research (Cron Job)

### Project Pilot: Can AI control a drone?

## 2026-07-27 - Neuroscience Research (Cron Job)

### Spiking Neural Networks for fMRI-Based Visual Semantic Decoding
- [[snn-fmri-visual-decoding]] - Methodology demonstrating that SNN-derived visual features provide superior targets for fMRI-based visual decoding compared to ANN features, with stronger brain alignment and improved semantic decoding performance (arXiv: 2607.19170)
  - Reduces feature-prediction error from 0.7707 to 0.0282 and improves top-1 semantic decoding accuracy from 0.1800 to 0.4400 on GoD dataset
  - Shows both spiking neural dynamics and temporal simulation steps contribute to the observed advantage
  - Validates SNN-derived features as effective brain-decodable visual representations
  - **Activation**: fMRI visual decoding, spiking neural networks, brain-computer interface, visual semantic decoding, SNN features

### Perspective Latents as an Architectural Condition for Causal Emergence in Active Inference Agents
- [[perspective-latents-causal-emergence-active-inference]] - Framework for measuring causal emergence (ΦID) in active inference agents with perspective latents architecture, analyzing how architectural separation between fast perception and slow global latents affects information-theoretic signatures of integration (arXiv: 2607.20708)
  - Tests causal emergence using Integrated Information Decomposition (ΦID) in reward-free active inference agents
  - Identifies slow global latent g as architectural locus of ΦID-relevant temporal organization
  - Shows aggregate ΦID magnitude is largely architectural and decreases with training
  - Reveals learning effects only at atom-compositional level: decoupling flips sign and becomes regime-invariant
  - Argues against reading scalar ΦID as direct index of learned integration
  - **Activation**: perspective latents, causal emergence, active inference, integrated information decomposition, slow global latent, fast perception latent, structural decoupling, regime-switching

### Spectral theory for population density dynamics of spiking neurons with refractoriness
- [[spectral-theory-spiking-neurons-refractoriness]] - Rigorous operator-theoretic framework using non-self-adjoint boundary eigenvalue problems for Fokker-Planck operators to analyze spiking neuron populations with refractory periods (arXiv: 2607.20699)
  - Solves long-standing open problem of incorporating absolute refractory periods into population density approaches
  - Provides complete spectral characterization and identifies exceptional points where oscillatory modes emerge
  - Derives exact transfer function correcting previous heuristic derivations with additional threshold-noise contributions
  - Shows refractoriness can facilitate limit cycle onset in interacting neuron populations under mean-field approximation
  - **Activation**: spectral theory, spiking neurons, refractoriness, population density, Fokker-Planck
- [[project-pilot-ai-drone-control]] - Methodology for testing AI control of physical systems like drones through constrained interfaces and safety protocols. Based on Anthropic's July 2026 frontier red teaming research.
  - Constrained interface design with limited action space and safety boundaries
  - Safety protocol framework including pre-flight validation and emergency override
  - Evaluation metrics for task completion, safety compliance, and robustness
  - **Activation**: project pilot, ai drone control, physical system control, frontier red teaming