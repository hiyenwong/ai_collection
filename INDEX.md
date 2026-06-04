# AI Collection Index

## 2026-06-05 - Neuroscience Research (Cron Job)

### SC-TauPath: Structural Connectivity Attribution for Alzheimer Tau Propagation
- [[sc-taupath-alzheimer-tau-propagation]] - 首个神经生物学可解释的 Tau 传播路径图谱框架，结合 NDM 增强 MLP + 梯度归因，验证 Braak 分期解剖结构 (arXiv: 2606.04066)
  - 网络扩散模型增强 MLP + 梯度×输入归因量化每条结构连接边的贡献
  - 多尺度通路图谱：骨干边、高流量路线、枢纽 ROI，映射 Tau 传播路径
  - ADNI 234 名参与者验证，归因分数符合 Braak 分期解剖，揭示 SC 编码病理信息
  - **Activation**: tau propagation, Alzheimer, structural connectivity, attribution, network diffusion, Braak staging, DTI, PET, pathway mapping, interpretability, gradient attribution

## 2026-06-05 - Number Theory, Statistics, Advanced Mathematics + Quantum Mechanics (Cron Job)

### Low-rank Distributional Matrix Completion
- [[distributional-matrix-completion]] - Matrix completion with probability distribution entries using kernel mean embeddings + Tucker rank decomposition (arXiv: 2606.04176)
  - Kernel mean embeddings map probability distributions to RKHS for distributional matrix representation
  - Tucker rank extended to distribution-valued matrices capturing low-rank structure in distributional space
  - Functional unfolding operators bridge infinite-dimensional embeddings with finite-dimensional tensor computation
  - Non-asymptotic error bounds characterize statistical performance vs sample complexity
  - **Activation**: distributional matrix completion, kernel mean embedding, tucker rank distribution, functional unfolding, RKHS, probability distribution matrix, statistical matrix recovery, non-asymptotic bounds

### Monitored Chaotic Scattering
- [[monitored-chaotic-scattering-rmt]] - Extends random matrix theory of chaotic scattering to quantum dots with time-resolved measurements (arXiv: 2606.04794)
  - Constructs Kraus operator ensembles from circular ensembles for monitored quantum evolution
  - Derives discrete-time quantum master equation for charge transfer statistics
  - Equipartition conjecture enables closed-form RMT predictions for monitored transport
  - **Activation**: monitored chaotic scattering, random matrix theory, kraus operators, quantum master equation, charge transfer, mesoscopic physics, circular ensemble

### Convergence Rates of Sum-of-Hermitian-Squares for Pauli Algebra
- [[sum-of-hermitian-squares-pauli-convergence]] - Explicit convergence rates for noncommutative polynomial optimization relaxations in quantum theory (arXiv: 2606.04940)
  - Develops convergence rates for Sum-of-Hermitian-Squares hierarchies on Pauli algebra
  - Covers ground state energy estimation and other quantum optimization problems
  - Bridges moment relaxation theory with quantum many-body computation
  - **Activation**: sum of hermitian squares, pauli algebra, noncommutative optimization, convergence rates, quantum ground state, moment relaxation, polynomial optimization

### Decoded Quantum Interferometry Beyond Hamming Space
- [[decoded-quantum-interferometry-beyond-hamming]] - Extends DQI algorithm beyond Hamming space to finite geometries with translation symmetry (arXiv: 2606.04843)
  - Generalizes decoded quantum interferometry to rank-metric and translation association schemes
  - Uses quantum Fourier transform on finite geometries for structured optimization
  - Shell-based distance grouping enables coherent decoding beyond binary Hamming space
  - **Activation**: decoded quantum interferometry, rank-metric codes, translation association schemes, finite geometry, quantum fourier transform, structured optimization

### Fermionic Non-Gaussianity via Bell Sampling
- [[fermionic-bell-sampling-non-gaussianity]] - Bridge degree monotone for fermionic non-Gaussianity via Bell sampling, stronger Gaussian conversion no-go theorems (arXiv: 2606.05066)
  - Bridge degree: largest eigenvalue sector of Λ = Σγ_j⊗γ_j on two copies, non-increasing under post-selected Gaussian protocols
  - Stronger no-go theorems for Gaussian conversion than previously known monotones
  - Efficiently witnessed through Bell sampling; lower-bounds non-Gaussian gate complexity
  - Two algorithmic primitives: Gaussianity test with perfect completeness, state 2-design test
  - **Activation**: fermionic non-gaussianity, bell sampling, bridge degree, gaussian conversion, fermionic quantum computing, resource theory

### Entanglement Measure from Quantum Optimal Transport
- [[quantum-optimal-transport-entanglement]] - Bipartite entanglement via minimal quantum Wasserstein distance to separable states, Lipschitz dual formulation (arXiv: 2606.04969)
  - E(ρ) = min_{σ separable} W_1(ρ, σ) satisfies all entanglement axioms in single geometric framework
  - Lipschitz dual gives explicit lower bounds for pure and mixed states, sharp constant for two-qubit
  - Quantitative connection to entanglement witnesses: negative witness → certified lower bound on E
  - Natural subadditivity and trace-distance estimates, points toward large-deviation conjectures
  - **Activation**: quantum optimal transport, entanglement measure, Wasserstein distance, Lipschitz witness, separable states, experimental entanglement detection

### No-Go Theorem for Gaussian Quantum Repeaters
- [[no-go-gaussian-quantum-repeaters]] - Proves Gaussian repeaters cannot enhance quantum capacity of pure-loss channels via fractional extendibility framework (arXiv: 2606.05097)
  - Fractional extendibility generalizes k-extendibility for Gaussian states
  - Any Gaussian+LOCC repeater chain bounded by direct transmission capacity
  - Closes open question about Gaussian vs non-Gaussian repeater protocols
  - Framework applicable to broader Gaussian quantum network analysis
  - **Activation**: gaussian quantum repeaters, no-go theorem, fractional extendibility, quantum capacity, bosonic channels, pure-loss channels

### Hybrid Gaussian-Exponential Zero-Noise Extrapolation
- [[gaussian-exponential-zero-noise-extrapolation]] - Hybrid Gaussian-exponential ZNE model for periodic quantum circuits, improved error mitigation (arXiv: 2605.29242)
  - Hybrid model f(λ) = A·exp(-αλ²) + B·exp(-βλ) + C captures both Gaussian and exponential error components
  - Superior to standard exponential ZNE for circuits with oscillatory error behavior
  - Polynomial sample complexity, applicable to parameterized quantum circuits
  - Requires 5-7 noise scale factors for stable fitting
  - **Activation**: zero noise extrapolation, ZNE, gaussian exponential model, periodic circuits, error mitigation, NISQ

## 2026-06-04 - Systems Engineering + Quantum Mechanics (Cron Job)

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
  - **Activation**: dealer market, competition, internalisation, externalisation, Nash equilibrium, inventory risk, market microstructure, quoting strategy

### Competition, Stability, and Functionality in E-I Neural Circuits
- [[competition-stability-ei-circuits]] - Game-theoretic energetic framework for asymmetric E-I networks, extending energy-based models to biological circuits (arXiv: 2512.05252)
  - Each neuron as agent minimizing local energy in competitive game
