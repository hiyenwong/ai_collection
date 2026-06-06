# AI Collection Index

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

