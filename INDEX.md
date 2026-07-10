## 2026-07-11 - Deep Learning Research (Cron Job)

### TACO: Tail-Aware Credit Calibration for LLM Reinforcement Learning
- [[taco-tail-aware-credit-calibration]] - Fixes "Positive-Credit Contamination" in GRPO by calibrating credit for low-probability tail tokens (arXiv: 2607.07976v1)
  - Computes context-aware tail-risk scores to distinguish erroneous rarity from useful exploration
  - Calibrates (not eliminates) positive credit for risky tokens, preserving useful rare patterns
  - Improves training stability and supports sustained long-horizon RL gains
  - **Activation**: grpo, tail-aware, credit calibration, positive-credit contamination, token-level credit, rl stability

### AdaPrefix-GRPO: Adaptive Trace Prefix Control for Hard Reasoning Problems
- [[adaprefix-grpo-prefix-control]] - Feedback controller adjusts solution prefix length to maintain ~50% success rate during GRPO training (arXiv: 2607.07674v1)
  - Solves GRPO stalling on hardest problems where no rollout succeeds and advantages vanish
  - More than doubles GRPO accuracy on hard math (2.1x for 0.6B, 1.7x on AIME)
  - Implemented as data prep + loss mask; trainer is otherwise stock GRPO
  - **Activation**: grpo, adaptive difficulty, prefix control, hard reasoning, curriculum learning, math reasoning

### Agon: Competitive Cross-Model RL with Implicit Rival Grading
- [[agon-competitive-cross-model-rl]] - Two models compete as each other's graders for reasoning, without process labels or reward models (arXiv: 2607.07690v1)
  - Models alternate draft/response roles; rewarded for out-solving the rival
  - Doubles GRPO's pass@1 on hard DeepMath; 8x the gain of untrained MoA
  - Deploys as two-stage cascade at inference
  - **Activation**: competitive rl, cross-model, implicit grading, reasoning, multi-agent, grpo

### RL Post-Training Builds Compositional Reasoning Strategies
- [[rl-compositional-reasoning-strategies]] - RL composes primitive skills into higher-level reasoning strategies through phased sequential and parallel composition (arXiv: 2607.07646v1)
  - Phased mechanism: strengthen primitives → discover compositions → consolidate repertoire
  - RL differs from RFT in selectivity, not exploration volume
  - Pretraining must organize primitives into reduction procedures for RL to compress
  - **Activation**: rl post-training, compositional reasoning, strategy discovery, rejection fine-tuning, trace analysis

### SAM-MT: Real-Time Interactive Multi-Target Video Segmentation
- [[sam-mt-realtime-multi-target-vos]] - Decouples VOS latency from target count, achieving >36 FPS for 10 targets using SAM2 (arXiv: 2607.08688v1)
  - Uses explicit queries for targets, shared global context, decoupled masked attention, and sparse memory
  - Maintains SAM2's robust video segmentation while achieving real-time multi-target speed
  - **Activation**: video segmentation, sam2, real-time, multi-target, efficiency, vos

## 2026-07-11 - Neuroscience Research (Cron Job)

### Topological Decoding of Grid Cell Activity via Path Lifting to Covering Spaces
- [[topological-grid-cell-decoding-codes]] - Training-free topological decoding of spatial trajectories from grid cell population activity using TDA + path lifting (arXiv: 2510.16216)
  - Extracts toroidal coordinates from neural manifold via persistent homology
  - Path lifting to covering space ℝ² reconstructs trajectories up to affine transform from a single module
  - **Activation**: grid cells, topological data analysis, toroidal manifold, path lifting, spatial navigation, neural manifolds, continuous attractor network, entorhinal cortex

### Mass Conservation as Inductive Bias for SOC in NCA Reservoirs
- [[mass-conservation-nca-reservoir-criticality]] - Mass conservation promotes robust self-organized criticality in neural cellular automata reservoirs with 1.27× faster evolution (arXiv: 2606.23115)
  - Local redistribution rule preserving total lattice mass acts as inductive bias toward SOC
  - Comparable downstream performance on memory, classification, and temporal control tasks
  - **Activation**: self-organized criticality, neural cellular automata, reservoir computing, mass conservation, criticality

### STST-JEPA: EEG Foundation Model via Spatio-Temporal Joint Embedding Prediction
- [[stst-jepa-eeg-foundation]] - Self-supervised EEG transformer pretrained on 47,703 sessions achieving 3.06 years MAE for brain age prediction (arXiv: 2607.06629)
  - Combines latent-prediction (JEPA) with signal reconstruction under spatiotemporal block masks
  - Rank-1 on NeuralBench leaderboard for sex classification, age prediction, and psychopathology regression
  - **Activation**: EEG foundation model, self-supervised learning, brain age prediction, JEPA, spatio-temporal embedding, NeuralBench

## 2026-07-10 - Neuroscience Research (Cron Job) - Round 3

### Learning Biophysical HH Models from Extracellular Data for Precise Neurostimulation
- [[biophysical-hh-model-extracellular-neurostimulation]] - Differentiable biophysical simulation enables rapid HH parameter inference from extracellular MEA recordings, predicting stimulation responses with 90.6% accuracy (arXiv: 2607.04063, ICML 2026)
  - First framework to infer multi-compartment Hodgkin-Huxley parameters from non-invasive extracellular data
  - Replaces hours of clinical stimulus testing with minutes of recording + model prediction
  - Validated on macaque retina with 512-electrode array at 30μm pitch
  - **Activation**: Hodgkin-Huxley, neurostimulation, differentiable simulation, MEA, biophysical inference, retinal prosthesis

## 2026-07-10 - Number Theory, Statistics, Mathematics + Quantum (Cron Job)

### QMaxCal: Path-Space Regularization for Open Quantum Control via Girsanov's Theorem
- [[girsanov-quantum-control]] - Girsanov theorem path-space regularization for robust open quantum control, penalizing observable decoherence consequences (arXiv: 2606.19947)
  - Uses Girsanov's theorem from stochastic calculus to construct closed-form KL divergence estimators between quantum trajectory distributions
  - Two regularizers: Wiener KL (noise-specific) and Drift-Variance (universal), reduce infidelity by up to 50%
  - **+17pp to +27pp robustness gains under noise model mismatch, validated on IBM Kingston processor**
  - **Activation**: girsanov theorem, quantum control, stochastic calculus, path-space regularization, decoherence robust control, KL divergence quantum trajectories

### Quantum Hoare Logic with Integer Hybrid Path-Sums for Unbounded Loops
- [[quantum-hoare-logic]] - First semi-automated static analysis combining functional verification and resource estimation for hybrid quantum programs with unbounded loops (arXiv: 2607.08548)
  - Introduces Integer Hybrid Path-Sums (IHPS) for representing unbounded while loop executions
  - Generic strategy for termination and expected resource consumption via loop invariants
  - **Activation**: quantum hoare logic, hybrid quantum program verification, path-sum quantum, static analysis, formal verification, unbounded loops

### Bosonic QEC Codes with Finite Stellar Rank
- [[bosonic-stellar-rank-qec]] - Stellar rank as resource measure for bosonic QEC design, revealing noise-adapted code structures and concrete resource thresholds (arXiv: 2607.06404)
  - Trade-off among state approximability, energy, and logical protection under finite non-Gaussian resources
  - Grid-like encodings optimal for photon loss, rotation-symmetric for dephasing; k=2 suffices for dephasing break-even
  - **Activation**: bosonic quantum error correction, stellar rank, GKP code, cat code, finite resources, noise-adapted codes

## 2026-07-10 - Neuroscience Research (Cron Job) - Round 2

### Hyperbolic Learning on Brain Graphs for Disorder Diagnosis
- [[hlbg-hyperbolic-learning-brain-graphs]] - Lorentzian hyperbolic space modeling of ROI-community-whole-brain hierarchy for brain disorder diagnosis (arXiv: 2607.07077)
  - Graph-aware Mamba (GaMamba) captures long-range dependencies while preserving graph topology
  - Achieves SOTA on ABIDE-I (autism) and REST-MDD (depression) datasets
  - **Activation**: hyperbolic learning, brain graphs, functional connectivity, disorder diagnosis, Lorentzian space, graph mamba, hierarchical brain networks

### Non-Hermitian Potential Well Formalism for Consciousness
- [[non-hermitian-conscious-preconscious-subliminal]] - Complex-valued landscape model of Global Neuronal Workspace using nonlinear Schrödinger equation (arXiv: 2607.08302)
  - Conscious access emerges as bound state when GNW depth and attention exceed thresholds
  - Unifies subliminal, preconscious, and conscious processing in single framework
  - **Activation**: consciousness modeling, global neuronal workspace, non-hermitian hamiltonian, Schrödinger equation, preconscious processing, subliminal perception

## 2026-07-10 - Neuroscience Research (Cron Job)

### Contravariance Theory: Strong Alignment for Minimal Solutions to Hard Tasks
- [[contravariance-theory-strong-alignment]] - Formal proof that minimal DNN solutions to hard tasks exhibit strong alignment of privileged axes, explaining convergent evolution between artificial and biological networks (arXiv: 2607.08561)
  - Weak alignment (affine mappings) guarantees strong alignment (privileged axes) for minimal solutions
  - Alignment "zippers" up network hierarchy, causing privileged axes to emerge from end-to-end optimization
  - **Activation**: contravariance, strong alignment, convergent evolution, neuroai theory, dnn-brain comparison, privileged axes

### Dynamic Neural Manifolds for Flexible Closed-Loop Control on Neuromorphic Hardware
- [[dynamic-neural-manifolds-snn-control]] - Implementation of dynamic neural manifold theory on SpiNNaker 2 chip for real-time closed-loop control with flexible behavior switching (arXiv: 2607.07373)
  - Sensory inputs modulate heterogeneous inhibition, gain, and transient currents to drive rapid subspace rotations
  - Validated via robotic simulation where agent uses sensory feedback to dynamically reconfigure manifold geometry
  - **Activation**: dynamic neural manifolds, spiking neural networks, neuromorphic computing, spinnaker, closed-loop control, subspace rotation

## 2026-07-10 - Neuroscience Research (Cron Job)

### Social-Spatial Dependencies for Learning Visual Navigation
- [[social-spatial-navigation-phase-transitions]] - Neural network agents demonstrate phase transitions in navigation strategies based on social information quality (arXiv: 2607.07460)
  - Social information quality drives phase transitions from individual to following strategies
  - Environmental predictability enables behavioral hybridization between individual and social navigation
  - **Activation**: social navigation, visual navigation, phase transition, behavioral strategy, social dependency

## 2026-07-10 - Number Theory, Statistics, Advanced Mathematics (Cron Job)

### Quantum Density of States and Integer Partitions: A Semiclassical Approach
- [[quantum-density-states-integer-partitions]] - Semi-classical methods connecting quantum density of states with integer partitions via periodic orbit theory and trace formulas (arXiv: 2607.06146)
  - Trace formula links quantum level density to classical periodic orbits, reproducing Hardy-Ramanujan partition asymptotics
  - Distinct square partitions show oscillations characterized by Pythagorean number triples, connected to Fermat's theorem
  - New results for unrestricted and distinct integer partitions of primes
  - **Activation**: semiclassical, trace formula, integer partitions, number theory, quantum density of states, Pythagorean triples

### Plaquette: A Hardware-Aware Design Platform for Fault-Tolerant Quantum Computers
- [[plaquette-ftqc-hardware-design]] - Framework computing FTQC logical performance from device physics using four sampler classes including new XPauli sampler (arXiv: 2607.08767)
  - Four sampler classes: stabilizer, XPauli (new for leakage/environment), near-Clifford (coherent errors), full-state simulation
  - Pauli twirling can fall short for non-Pauli noise; XPauli matches full-state within statistical uncertainty
  - Validated on superconducting leakage, neutral atom scattering, and trapped ion heating error models
  - **Activation**: fault tolerance, FTQC, hardware-aware, XPauli sampler, leakage error, coherent error, Pauli twirling

## 2026-07-10 - Number Theory, Statistics, Advanced Mathematics (Cron Job)

### Grokking and epoch-wise double descent in quantum neural networks
- [[grokking-epoch-double-descent-qnn]] - Empirical observation of grokking and epoch-wise double descent in two-qubit QNNs under SU(4) parameterization, with weight-norm regularization to mitigate late-stage generalization decay (arXiv: 2607.08350)
  - First observation of grokking transition in variational quantum machine learning
  - Epoch-wise double descent: test error degrades at critical epoch before recovering
  - Generalization decay in late training correlates with unconstrained weight-norm increase
  - Weak weight-norm regularization stabilizes post-grokking phase
  - **Activation**: grokking QNN, epoch-wise double descent, quantum generalization decay, weight-norm regularization, QML training dynamics, SU(4) parameterization

### Quantum models of the Riemann zeta function, lattice spin models and algebraic models of entanglement
- [[quantum-models-riemann-zeta-lattice-spin]] - Connection between Hilbert-Polya conjecture and Riemann hypothesis, with results on p-adic quantum computing and lattice spin models for quantum entanglement (arXiv: 2606.29294)
  - Hilbert-Polya conjecture connects Riemann zeta zeros to quantum spectrum
  - New results on p-adic quantum computing approaches
  - Algebraic entanglement models based on lattice spin systems
  - **Activation**: Riemann zeta, Hilbert-Polya conjecture, p-adic quantum computing, lattice spin models, algebraic entanglement

### On the Spectral theory of Isogeny Graphs and Quantum Sampling of Secure Supersingular Elliptic curves
- [[isogeny-graphs-quantum-sampling-elliptic]] - First provable quantum polynomial-time algorithms for sampling secure supersingular elliptic curves with QUE conjecture proof (arXiv: 2602.02263)
  - Heuristic O~(log^4 p) quantum gate complexity for secure curve sampling
  - Proves Quantum Unique Ergodicity conjecture for supersingular isogeny graphs
  - Removes heuristic assumptions in quantum money protocols
  - **Activation**: isogeny graphs, supersingular elliptic curves, quantum sampling, QUE conjecture, post-quantum cryptography

## 2026-07-10 - Number Theory, Statistics, Advanced Mathematics + Quantum Mechanics (Cron Job - Late Afternoon)

### Invariance Audits for Quantum Kernels and Variational Rewinding
- [[invariance-audits-quantum-kernels]] - Real-to-Hermitian taxonomy for auditing data representation invariances in QML (arXiv: 2607.07927)
  - Fidelity kernel = Hilbert-Schmidt inner product of rank-1 projectors
  - Same-span block-swap witness distinguishes Grassmann vs flag failures
  - Weighted flag kernel is PSD and block-gauge invariant
  - **Activation**: quantum kernel audit, representation invariance, Grassmann kernel, flag projector, QVR

### A Quantum Reservoir Architecture for Chaotic Forecasting
- [[quantum-reservoir-chaotic-forecasting]] - Complete reproducible QRC recipe with stability-number diagnostic for validating high-dimensional feature benefit (arXiv: 2607.07978)
  - Fixed quantum circuit as feature generator — no optimization needed
  - Stability number tracks readout fit quality as sizes grow
  - Quantum reservoir flat error vs classical degradation
  - **Activation**: quantum reservoir computing, chaotic forecasting, reservoir stability number, dimensionality diagnostic

### Adaptive Qubit Freezing for Divide-and-Conquer QAOA
- [[frozen-lgp-qaoa]] - FrozenLGP achieves 100% graph partition coverage for D&C QAOA via max-flow min-cut and energy-preserving bias folding (arXiv: 2607.08138)
  - Transforms partitionability from assumption to enforceable property
  - 100% coverage vs 4.6% on high-connectivity graphs up to 10K vertices
  - Rigorous energy preservation via linear bias folding
  - **Activation**: FrozenLGP, divide-and-conquer QAOA, qubit freezing, graph partitioning, max-flow vertex cut

## 2026-07-10 - Number Theory, Statistics, Advanced Mathematics + Quantum Mechanics (Cron Job - Evening)

### How Stark units enter SIC overlaps
- [[stark-units-sic-overlaps]] - SIC-POVM overlap values characterized as products of Stark units from ray class fields, with Shintani-Faddeev cocycle cross-validation (arXiv: 2606.25457)
  - SIC overlaps = products of integral powers of sqrt(Stark units)
  - Non-minimal SICs involve lattice of ray class fields
  - Every second dimension: some overlap units = ±1 from ray class field properties
  - **Activation**: SIC-POVM overlaps, Stark units, ray class fields, Shintani-Faddeev cocycle

### Krein Space Quantization and a Spectral Interpretation of the Riemann xi-Function
- [[krein-space-riemann-xi]] - Spectral interpretation of Riemann xi-function via Krein space quantization in de Sitter QFT, connecting Legendre functions, Mehler-Fock transform, and zero spacing to mass-time scaling (arXiv: 2606.13932)
  - de Sitter two-point → Legendre → Mehler-Fock → xi-function
  - Krein space allows sign-indefinite spectral measures
  - Zero spacing relates to de Sitter mass-time scaling
  - **Activation**: Krein space quantization, Riemann xi-function spectral, de Sitter QFT, Mehler-Fock transform
