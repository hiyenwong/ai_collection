# AI Collection Index

## 2026-06-06 - Quantum Computing Research (Cron Job)

### Quantum Element-Wise Transforms
- [[quantum-element-wise-transforms]] - Quantum algorithms for element-wise polynomial transforms with exponential space reduction, correcting prior work errors. Applications to ML, simulation, and signal processing (arXiv: 2606.06456)
  - Exponential space reduction in polynomial degree vs prior constructions
  - Block encoding approach with element-wise independent application
  - Rectifies errors in previous quantum algorithm constructions
  - Unified framework for QSVT, LCU, and element-wise transforms
  - **Activation**: quantum-element-wise, polynomial-transform, QSVT, block-encoding, numerical-linear-algebra

### Breakeven Demonstration of Quantum LDPC Codes
- [[quantum-ldpc-breakeven]] - First breakeven demonstration of qLDPC codes on trapped-ion hardware with 9× better logical error rate. OMG architecture enables addressable mid-circuit measurement without ion transport (arXiv: 2606.06455)
  - Logical error rate 9× better than previous superconducting demonstration
  - OMG architecture: addressable mid-circuit measurement and reset
  - No ion transport or dedicated coolant ions required
  - 9 different codes on single device without hardware reconfiguration
  - **Activation**: qLDPC, quantum-error-correction, trapped-ion, breakeven, OMG-architecture, fault-tolerant

### Non-Hermitian SSH Model Charge Correlations
- [[non-hermitian-ssh-charge-correlations]] - Enhancement of charge correlations and topological markers in interacting non-Hermitian SSH model. Open boundary conditions amplify staggered correlations near exceptional points (arXiv: 2606.06466)
  - Real-space topological marker robust under interactions
  - Open boundary conditions dramatically enhance charge correlations
  - Low-energy state accumulation near exceptional points promotes electronic instabilities
  - Non-Hermiticity amplifies interaction effects and CDW tendencies
  - **Activation**: non-hermitian, SSH-model, topology, charge-correlations, exceptional-points

### Room-Temperature Dipole Synchronization in Nanocavities
- [[room-temperature-dipole-synchronization-nanocavity]] - Room-temperature synchronized dipole state in plasmonic nanogap 2D arrays. Novel driven-dissipative system with spatial coherence but suppressed temporal photon coherence (arXiv: 2606.06490)
  - Spatial coherence across distant dipoles via sub-nm gap coupling
  - NOT a laser/BEC/polariton condensate: unique synchronization state
  - Fast temporal coherence decay from rapid radiative/non-radiative emission
  - Scalable room-temperature platform for quantum photonic technologies
  - **Activation**: room-temperature-synchronization, nanocavity, plasmonic, driven-dissipative, spatial-coherence

## 2026-06-06 - Systems Engineering Research (Cron Job)

### HANDOFF: Humanoid Agentic Task-Space Whole-Body Control
- [[handoff-humanoid-control]] - Multi-teacher KL distillation for mixture-of-experts humanoid control with compact task-space interface. VLM-driven agentic planner with zero task-specific fine-tuning (arXiv: 2606.06493)
  - Compact, explicit task-space interface design (intuitive, general, modular, expressive)
  - Three complementary teachers: motion tracking (safety-filtered), locomotion, fall-recovery
  - Context-conditioned gating for MoE student architecture
  - Unitree G1 hardware validation with natural language task roll-outs
  - **Activation**: humanoid control, whole-body control, task-space interface, multi-teacher distillation, MoE robotics, VLM planner, safety-filtered control, complementary teachers, KL distillation robotics, agentic manipulation

### Code2LoRA: Hypernetwork-Generated Adapters for Code LLMs
- [[code2lora-hypernetwork-adapter]] - Hypernetwork generates repository-specific LoRA adapters for zero inference overhead. Supports static snapshot (Code2LoRA-Static) and dynamic evolution (Code2LoRA-Evo with GRU state) scenarios (arXiv: 2606.06492)
  - Hypernetwork-generated repository-specific LoRA adapters (zero inference token overhead)
  - Two usage scenarios: Static (stable codebases) and Evo (active development with GRU)
  - RepoPeftBench: First repository-level PEFT benchmark (604 repos, 40K+12K static, 215K+87K evo tasks)
  - Matches per-repo LoRA upper bound (static), +5.2 pp over shared LoRA (evo)
  - **Activation**: code LLM adaptation, repository-specific LoRA, hypernetwork adapters, software evolution, code adaptation, zero overhead knowledge injection, GRU-based adapter, RepoPeftBench, assertion completion, code drift handling

## 2026-06-06 - Economics, Investment + Quantum Finance (Cron Job)

### Certified Higher-Order QAOA for Collateral Optimization
- [[certified-higher-order-qaoa-collateral]] - CR-HO-QAOA: certified higher-order quantum framework for margin- and CSA-aware collateral allocation with feasible-subspace mixers and CP-SAT certification (arXiv: 2606.04235)
  - Adapter-first margin normalization (SIMM, proxy SIMM, legacy IA, VM-only, RQV)
  - Higher-order binary model captures concentration pressure, custody batches, substitution tickets, chunky lots, liquidity effects
  - Collateral-specific feasible-subspace mixers preserve one-hot choices and movement budgets
  - Deterministic CP-SAT master solver certifies every quantum candidate
  - Improves certified sample quality vs. QUBO-style and generic-mixer baselines
  - **Activation**: certified QAOA collateral, margin-aware quantum optimization, CSA collateral allocation, higher-order QAOA finance, feasible-subspace mixer, quantum collateral optimization, CP-SAT quantum certification

### Efficient Complex-Valued State Preparation on Bucket Brigade QRAM
- [[bbqram-state-preparation-finance]] - Architecture-aware quantum state preparation using BBQRAM + segment tree for O(log²(MN)) query time, eliminating QPU arithmetic via classical precomputation (arXiv: 2604.25644)
  - 核心要点 1: Classical precomputation of rotation angles removes U_2CR reversible arithmetic from QPU
  - 核心要点 2: Complex-valued extension via two-step magnitude-then-phase procedure with leaf phase storage
  - **Activation**: BBQRAM state preparation, bucket brigade QRAM, complex-valued quantum encoding, quantum finance data loading, classical precomputation rotation angles, magnitude-then-phase

## 2026-06-06 - Neuroscience Research (Cron Job)

### Bio-plausible Neuromorphic Disturbance Observer Based on Emulation Theory
- [[neuromorphic-disturbance-observer]] - Neuromorphic control framework using integrate-and-fire neuron dynamics with adaptive-threshold triggering inspired by spike-frequency adaptation (SFA). Reduces spike events to 42.6% under noise while maintaining robustness and adaptability (arXiv: 2606.05189)
  - Event-driven control via spike-timing encoding (not continuous-time)
  - Adaptive-threshold mechanism: history-dependent regulation inspired by biological SFA
  - Bio-plausible robustness: 42.6% spike reduction under noisy conditions
  - Applicable to neuromorphic hardware (Loihi, SpiNNaker) and robotic control
  - **Activation**: neuromorphic, disturbance observer, IF neuron, spike-frequency adaptation, bio-plausible control, event-driven, adaptive threshold, neural control, neuromorphic hardware

### SC-TauPath: Structural Connectivity Attribution for Tau Propagation
- [[sc-taupath-alzheimer-tau-propagation]] - Attribution framework mapping Alzheimer's tau propagation pathways using gradient × input on NDM-augmented MLP. Multi-scale pathway maps (backbone edges, high-traffic routes, hub ROIs) validated against Braak staging anatomy from 234 ADNI participants (arXiv: 2606.04066)
  - Network Diffusion Model (NDM)-augmented MLP for tau prediction
  - Gradient × input attribution: biologically interpretable pathway maps
  - Multi-scale representation: backbone edges, high-traffic routes, hub ROIs
  - Validated against Braak staging anatomy (stages I-II, III-IV, V-VI)
  - Low biophysical assumptions: learning-based approach vs physics-based diffusion models
  - **Activation**: Alzheimer's, tau propagation, structural connectivity, attribution framework, Braak staging, network diffusion, gradient attribution, pathway mapping, ADNI, neurodegeneration

### Intrinsic Computational Functionalism
- [[intrinsic-computational-functionalism]] - Framework for observer-independent computational structures in consciousness research. Two criteria: system-intrinsic instantiation (C1) + causal-dynamical intervention (C2). Three-tier decomposition identifies dynamics-internal grain selection as key (arXiv: 2606.06424)
  - Addresses observer-relativity objection: anti-computational arguments succeed only at tier (i) interpreter-relative labels
  - C1: Property specifiable without observer labelling, invariant under structure-preserving relabellings
  - C2: Grounded in state-space structure with mutually constraining variables, exhibited in counterfactual intervention responses
  - Tier (iii) dynamics-internal grain selection is where intrinsic computational properties emerge
  - Syntax-is-not-semantics, mapmaker arguments, biological-naturalist objections succeed against tier (i) but intrinsic computational functionalism survives
  - **Activation**: computational functionalism, consciousness, observer-relativity, intrinsic computation, state-space dynamics, causal intervention, computational neuroscience, tier decomposition

## 2026-06-06 - Economics/Investment + Quantum (Cron Job)

### Derivative-Informed Operator Learning for Finance
- [[derivative-informed-operator-learning-finance]] - Neural operators trained to match pricing operators AND Fréchet derivatives for on-the-fly Greeks, hedging, and control. Vega error -40%, Delta error -15% (arXiv: 2606.05900)
  - Neural operator learns entire pricing map, not just pointwise prices
  - Fréchet derivative matching ensures accurate Greeks (Delta, Vega, Gamma)
  - Theoretical hedging error bounds from operator approximation theory
  - Random-feature DeepONet for efficient volatility surface fitting
  - Optimizer stability guarantees under approximation error
  - **Activation**: derivative pricing, operator learning, neural operator, DeepONet, Fréchet derivative, Greeks, hedging, Vega, Delta, volatility surface, quantitative finance

### Market Informedness & RL Market Making
- [[market-informedness-rl-market-making]] - Multi-agent RL (MAPPO) for market making with Hawkes-driven order flow. Counterintuitive: profitability increases with market informedness (arXiv: 2606.05882)
  - Heterogeneous agents: informed traders, noise traders, market makers
  - MAPPO in CTDE (Centralized Training, Decentralized Execution)
  - Hawkes process models self-exciting order flow arrivals
  - Finite-horizon stability guarantees for deployable strategies
  - Informed flow provides more predictable adverse selection patterns
  - **Activation**: market making, informedness, adverse selection, reinforcement learning, multi-agent, MAPPO, CTDE, Hawkes process, order flow, liquidity

### Dealer Market Competition with Internalisation
- [[dealer-market-competition-nash-equilibrium]] - Closed-form Nash equilibrium for multi-dealer order flow competition using variational approach. Balances internalisation vs externalisation for inventory risk (arXiv: 2606.06413)
  - Variational formulation of N-dealer quoting game
  - Internalisation: skew quotes to attract offsetting flow
  - Externalisation: offload inventory in inter-dealer market
  - Closed-form solution via coupled Riccati equations
  - Competition intensity determines spread compression  
  - Strategic inventory management through spread adjustments
  - **Activation**: dealer market, Nash equilibrium, internalisation, inventory risk, variational approach, quoting game, market microstructure

## 2026-06-05 - AI Systems Engineering (Cron Job)

### Multi-Stage Warm-Start Deep Learning for Unit Commitment
- [[warmstart-dl-unit-commitment]] - Three-stage warm-start pipeline for unit commitment optimization: ML warm-start → primal-dual formulation → branch-and-bound refinement. Solves 24-hour instances in 3.96s with warm-start (vs 5400s cold) (arXiv: 2606.05903)
  - Stage 1: Machine learning model predicts initial solution
  - Stage 2: Primal-dual problem formulation with ML-predicted bounds
  - Stage 3: Branch-and-bound refinement with warm-start bounds
  - Reduces solve time by 99.93% compared to cold start
  - Combines ML speed with mathematical programming optimality guarantees
  - **Activation**: unit commitment, warm-start, primal-dual, branch-and-bound, power system optimization, mixed-integer programming, deep learning warm-start