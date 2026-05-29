## 2026-05-30 - Neuroscience Research (Cron Job) - Part 2

### Embodied Virtual Reality Feedback Reshapes Neural Representations to Support Continuous Three-Dimensional Motor Imagery Decoding
- [[embodied-vr-feedback-3d-motor-imagery-bci]] - First systematic investigation of embodied VR feedback for continuous 3D motor imagery BCI, with 8.9-13.0% improvement over screen feedback (arXiv: 2605.29677)
  - VR feedback elicits inherently more decodable and generalisable neural representations
  - CNN-LSTM decoder achieves r=0.762 correlation under VR vs r=0.672 under screen
  - Neurophysiological: stronger sensorimotor-parietal desynchronisation, enhanced motor-frontal connectivity
  - **Activation**: embodied VR feedback, motor imagery BCI, 3D decoding, neurorehabilitation, continuous BCI

### Neural-Behavioral Representation of Natural Whole-body Movement in Monkeys
- [[neural-behavioral-whole-body-movement-monkeys]] - First framework combining large-scale epidural cortical signals with multi-view motion capture to decode unconstrained whole-body kinematics in primates (arXiv: 2605.29355)
  - Behavior prior learning via autoregressive encoder-decoder model
  - Decodes accurate/realistic whole-body movement without explicit physics constraints
  - Novel proof-of-concept for natural whole-body movement decoding
  - **Activation**: whole-body movement, motor decoding, primate neuroscience, behavior prior, motion capture

## 2026-05-30 - Neuroscience Research (Cron Job)

### Comprehensive Neural Dynamics Analysis Methodology
- [[neural-dynamics-analysis-methodology]] - Unified framework integrating neural population decoding, brain network dynamics, neural criticality assessment, spiking neural network dynamics, and connectome computational analysis (Synthesized from multiple recent arXiv papers)
  - Neural population decoding: dimensionality reduction, temporal dynamics, cross-subject generalization
  - Brain network dynamics: dynamic connectivity, control theory, Kuramoto oscillators, tensor decomposition
  - Neural criticality assessment: power-law distributions, branching ratio, Griffiths phase
  - Spiking neural network dynamics: LIF models, synchrony, oscillations, E/I balance
  - Connectome computational analysis: graph metrics, hub identification, GNN, optimal transport
  - **Activation**: neural dynamics, computational neuroscience, brain networks, neural population, spiking networks, criticality, connectome analysis, 神经动力学分析方法论

### Common Noise-Induced Group-Level Synchronization Between Uncoupled Groups of Oscillators
- [[noise-induced-oscillator-synchronization]] - Proves common noise synchronizes uncoupled oscillator groups via Kuramoto order parameter; phase density evolution mapping explains collective dynamics without inter-group coupling (arXiv: 2605.29529)
  - Complex Kuramoto order parameter R(t) synchronizes across groups sharing identical noise
  - Phase density evolution derivation: common noise creates correlated collective phases
  - Neurophysiological implication: shared input explains functional connectivity without anatomical connections
  - **Activation**: noise-induced synchronization, Kuramoto model, oscillator dynamics, common noise, phase density evolution, neural synchronization

## 2026-05-30 - Economics, Investment + Quantum (Cron Job)

### End-to-End PDE-Based Quantum Algorithms for Multi-Asset Option Pricing under Local and Stochastic Volatility
- [[quantum-pde-option-pricing]] - End-to-end quantum PDE framework for European option pricing achieving polynomial speedup N^{d/2} (BS) and N^d (Heston) over classical baselines (arXiv: 2605.26610)
  - Finite-difference discretization on spatial grids with explicit Clifford+T resource accounting
  - Gate complexity O~(d^2 N^{2+d/2}) for local-vol BS, O~(d^2 N^{d+2}) for Heston
  - **Activation**: quantum PDE option pricing, quantum Black-Scholes, quantum Heston model, multi-asset derivatives, finite-difference quantum, 量子期权定价

### A Penalty-Free Pipeline for Direct Quantum-Annealer Portfolio Optimization
- [[penalty-free-quantum-annealing-portfolio]] (enhanced) - Drops cardinality penalty from QUBO, enforcing constraints via classical post-processing; reduces chain-break from 71-92% to 0.04% (arXiv: 2605.17628)
  - Dense penalty term makes logical graph complete regardless of covariance structure
  - Objective-only QUBO + classical cardinality enforcement yields lower-energy feasible portfolios
  - **Activation**: penalty-free quantum annealing, quantum portfolio optimization, D-Wave QUBO, cardinality constraints

### Parameterized 4-Qubit EWL Quantum Game Circuits with Dirac-Solow-Swan Hamiltonian for Innovation Recommender Systems
- [[ewl-quantum-game-economics]] - 4-qubit EWL quantum game circuit mapping measurement probabilities to Dirac-Solow-Swan Hamiltonian for disruptive innovation forecasting in quadruple helix ecosystems (arXiv: 2605.18080)
  - Only 22 gates, circuit depth 11, NISQ-compatible
  - Calibrated from EC CORDIS funding data for real-world recommender scoring
  - **Activation**: EWL quantum game, Dirac-Solow-Swan Hamiltonian, quantum recommender system, quadruple helix, 量子博弈论经济学

### Where the Quantum Lives in D-Wave Hybrid Portfolio Optimization
- [[quantum-hybrid-audit]] - Audit methodology for decomposing hybrid quantum-classical optimization workflows, measuring actual quantum contribution vs classical overhead (arXiv: 2605.17623)
  - QPU access time is only 0.7% of 5-second wall-clock budget in D-Wave hybrid solver
  - Hybrid matches Gurobi MIQP optimum on all 54 provable instances despite minimal quantum time
  - Quantum Contribution Index (QCI) framework for investment decision support
  - **Activation**: quantum hybrid audit, D-Wave hybrid analysis, quantum contribution measurement, hybrid solver decomposition, 量子混合审计

### Noise-Induced Landscape Distortion in QAOA for Constrained Binary Optimization
- [[qaoa-landscape-audit]] - Landscape Span Compression (LSC) metric for device-agnostic audit of QAOA hardware noise impact, predicting optimization failure before expensive quantum runs (arXiv: 2604.19426)
  - LSC = 1 - (observed_span/ideal_span); LSC > 0.7 indicates near barren plateau
  - Empirically validated on IBM quantum hardware for constrained QUBO problems
  - Pre-run diagnostic saves quantum compute resources by predicting failure
  - **Activation**: qaoa landscape audit, landscape span compression, qaoa noise analysis, quantum barren plateau detection, 量子优化景观审计

### Constrained Counterdiabatic Quantum Approximate Optimization Algorithm for Portfolio Optimization
- [[constrained-counterdiabatic-qaoa-portfolio]] (enhanced) - CCD-QAOA with approximate adiabatic gauge potentials from nested commutators for constrained portfolio optimization (arXiv: 2605.06858)
  - Incorporates counterdiabatic terms into variational ansatz for improved convergence
  - Handles realistic budget and risk constraints with XY-mixer Hamiltonian
  - **Activation**: counterdiabatic QAOA, portfolio optimization, adiabatic gauge potential, constrained quantum optimization

### Constraint Preserving XY-Mixers under Trotterized Adiabatic Evolution
- [[constraint-preserving-quantum-mixers]] (enhanced) - XY-mixer design methodology under Trotterized adiabatic evolution for constrained quantum optimization (arXiv: 2605.02465)
  - Constraint locality analysis for XY-mixer Hamiltonian design
  - Trotterized adiabatic evolution preserves feasibility throughout optimization
  - **Activation**: constraint preserving mixers, XY-mixer, Trotterized evolution, constrained quantum optimization

     1|## 2026-05-29 - Number Theory, Statistics, Advanced Mathematics + Quantum (Cron Job)
     2|
     3|### Algorithms with Polynomially-Improved Approximation Factors for the 2→q Norm
     4|- [[norm-approximation-algorithms]] - Multiplicative weight update algorithm for matrix 2→q norm approximation with polynomial improvement over spectral methods, applications to hypercontractivity and quantum separability (arXiv: 2605.25303)
     5|  - MWU framework achieves O(n^{1/4-δ}) vs prior O(n^{1/4} log d)
     6|  - Applications: hypercontractivity testing, quantum separability certification, small-set expansion
     7|  - **Activation**: matrix norm approximation, 2-to-q norm, operator norm, hypercontractivity, multiplicative weight update, quantum separability
     8|
     9|### Bell's Theorem: Why Probability Factorisation Fails
    10|- [[bell-probability-factorization]] - Statistical foundations of Bell's theorem showing why joint probability factorization P(A,B|a,b,λ)=P(A|a,λ)P(B|b,λ) fails in quantum systems (arXiv: 2605.29589)
    11|  - Factorization assumption incompatible with quantum entanglement
    12|  - CHSH inequality as statistical diagnostic for non-classical correlations
    13|  - **Activation**: Bell theorem, probability factorization, quantum nonlocality, CHSH inequality, joint distributions
    14|
    15|### Comparing Classical Simulation and Sample-Based Learning of Quantum Systems
    16|- [[quantum-ml-simulation-learning-comparison]] - Empirical framework comparing simulability vs learnability for quantum systems via Born-rule statistics (arXiv: 2605.28986)
    17|  - Simulation (from classical description) and learning (from measurement samples) need not coincide
    18|  - Provides complexity-theoretic and empirical methodology for quantum advantage verification
    19|  - **Activation**: quantum simulation vs learning, sample-based quantum learning, simulability learnability, Born-rule statistics
    20|
    21|### Analytic Properties of the Jost Functions via the Poincaré-Picard Theorem
    22|- [[jost-function-analytic-ode]] - ODE-theoretic analysis of Jost function analyticity for quantum scattering and complex energy plane continuation (arXiv: 2605.28859)
    23|  - Applies Poincaré-Picard theorem to parameter-dependent radial Schrödinger equation
    24|  - Bridges mathematical analysis (ODE theory) with quantum scattering physics
    25|  - **Activation**: jost function, quantum scattering, analytic continuation, Poincaré-Picard, complex energy plane
    26|
    27|### HyperPrecision: High-Precision Numerical Evaluation of Multivariate Hypergeometric Functions
    28|- [[hypergeometric-high-precision-evaluation]] - Mathematica package for high-precision evaluation of Horn-type hypergeometric functions via Pfaffian systems, applicable to QFT, string theory, number theory, and statistics (arXiv: 2605.30216)
    29|  - Automatic Pfaffian system construction from hypergeometric function definition
    30|## 2026-05-29 - Neuroscience Research (Cron Job)
    31|
    32|### A Deep Learning Model of Mental Rotation Informed by Interactive VR Experiments
    33|- [[deep-learning-mental-rotation-vr]] - Longitudinal subcortical shape analysis with cognitive associations in aging (arXiv: 2605.29703)
    34|  - Equivariant neural encoder for 3D spatial representations
    35|  - Neuro-symbolic object encoder combining perception + reasoning
    36|  - Interactive VR experiments for human behavioral validation
    37|  - **Activation**: mental rotation, spatial cognition, VR, neuro-symbolic, equivariant networks
    38|
    39|### Subcortical Shape Variations and Their Associations with Cognition Across the 8th Decade of Life
    40|- [[subcortical-shape-cognition-aging]] - Longitudinal analysis of subcortical morphology + cognition (arXiv: 2605.29703)
    41|  - Shape-based analysis captures subtle aging patterns missed by volumetry
    42|  - Lothian Birth Cohort 1936: 9-year trajectory (age 70-79)
    43|  - Regional specificity: hippocampal head → memory, thalamus → processing speed
    44|  - **Activation**: subcortical morphology, brain aging, cognitive decline, shape analysis
    45|
    46|  - One-dimensional contour restriction reduces multivariate PDE to ODE for efficient evaluation
    47|  - **Activation**: hypergeometric, pfaffian, high-precision, horn-type, mathematica, multivariate, laurent expansion, quantum field theory
    48|
    49|### On modular forms of rational weight satisfying the canonical second-order linear modular differential equation
    50|- [[modular-forms-kaneko-zagier-classification]] - Complete classification of rational weights for Kaneko-Zagier differential equation admitting modular forms solutions (arXiv: 2605.23383)
    51|  - Transforms KZ equation to hypergeometric form, constructs monodromy representation matrices
    52|  - Stringent commutativity constraints limit admissible weights to specific set
    53|  - **Activation**: modular forms, kaneko-zagier, differential equation, monodromy, hypergeometric, rational weight, congruence subgroup
    54|
    55|### Iterative maps emerging from cohomological structure of primes
    56|- [[prime-cohomological-iterative-maps]] - Prime gaps described by iterative maps with cohomological structure linking to statistical and quantum mechanics (arXiv: 2605.17622)
    57|  - Iterative map predicts primary growth of successive primes
    58|  - Residual fluctuations encode well-defined cohomological structure
    59|  - **Activation**: prime numbers, cohomology, iterative maps, statistical mechanics, quantum mechanics, prime gaps
    60|
    61|### A Uniform Random-Lattice Tail Bound for the SVP Kissing-Profile Parameter
    62|- [[svp-lattice-tail-bound]] - Dimension-uniform tail bound for SVP kissing-profile parameter with implications for quantum algorithms and post-quantum cryptography (arXiv: 2605.21966)
    63|  - μ_n{γ(L) > T} ≤ C·T^{-1} for Haar-Siegel random lattices, uniformly in dimension
    64|  - γ(L) = 2^{o(n)} with high probability for random lattices
    65|  - **Activation**: SVP, shortest vector problem, lattice, tail bound, quantum algorithms, post-quantum cryptography
    66|
    67|### Hadamard product of convex functions and Jackson operator
    68|- Note: Jackson operator q-theory skill already exists; no new skill needed (arXiv: 2605.18412)
    69|
    70|## 2026-05-29 - Number Theory, Statistics, Advanced Mathematics + Quantum (Cron Job)
    71|
    72|### Wasserstein Least Squares: A Canonical Regression Method for Probability Distributions
    73|- [[wasserstein-least-squares-regression]] - Distributional regression via optimal transport, achieving n^{-1/2} rate with exponential improvement for Wasserstein barycenters (arXiv: 2605.30266)
    74|  - Canonical extension of Euclidean least squares to probability distribution space via convex analysis
    75|  - Template deformation model enables n^{-1/2} estimation rate; exponential barycenter improvement
    76|  - **Activation**: Wasserstein regression, distributional regression, optimal transport, probability distributions, Wasserstein barycenter, template deformation
    77|
    78|### Improved Sample Complexity Bound for Sample-Based Lindbladian Simulation
    79|- [[lindbladian-sample-complexity]] - Sharp dichotomy between typical-case O(t²/ε²) and worst-case Ω(d⁴t²/ε²) for quantum Lindbladian simulation (arXiv: 2605.30301)
    80|  - WML algorithm with trace condition determines typical vs worst case
    81|  - Random Lindblad operators satisfy typical case with high probability
    82|  - **Activation**: Lindbladian simulation, sample complexity, quantum channels, open quantum systems, WML algorithm, random matrix theory
    83|
    84|## 2026-05-29 - Neuroscience Research (Cron Job)
    85|
    86|### Domain-Informed Multi-Objective Framework for EEG Channel Selection in Motor Imagery BCIs
    87|- [[domain-informed-moeeg-channel-selection-bci]] - Multi-objective optimization combining spatial relevance (Gaussian kernel) + functional discriminability (ERD) for compact EEG channel selection (arXiv: 2605.29943)
    88|  - NSGA-II/MOPSO/MOEA/D algorithms achieve 87%, 71%, 75%, 65% on Physionet, OpenBMI, HighGamma, BCIIV-2A
    89|  - 87% dimensionality reduction (64→8 channels), sensorimotor cortex prioritization
    90|  - **Activation**: EEG channel selection, motor imagery BCI, multi-objective optimization, Pareto front, ERD, sensorimotor cortex
    91|
    92|### Learning Robust and Task-Invariant Functional Representation from fMRI through Siamese Self-Supervised Learning
    93|- [[brainsimsiam-self-supervised-fmri]] - BrainSimSiam lightweight self-supervised framework for cross-task generalization without large-scale pretraining (arXiv: 2605.28990)
    94|  - Positive-only contrastive learning, stop-gradient mechanism, outperforms supervised baselines
    95|  - +15% ADHD accuracy, -8% age regression MSE, comparable to foundation models with 90% less compute
    96|  - **Activation**: self-supervised fMRI, Siamese learning, BrainSimSiam, positive-only contrastive, cross-task generalization
    97|
    98|## 2026-05-29 - Neuroscience Research (Cron Job)
    99|
   100|### LLM ICL Representational Geometry Reorganization
   101|- [[llm-icl-representational-geometry-reorganization]] - ICL models reorganize representations dynamically via prototype comparison (arXiv: 2605.28854)
   102|  - RDM correlation increases during untangling tasks
   103|  - Eigenvalue spectrum separates task information
   104|  - **Activation**: ICL, representational geometry, prototypes, untangling, RDM correlation, online learning
   105|
   106|### Brain-IT-VQA: From Brain Signals to Answers
   107|- [[brain-it-vqa-fmri-visual-question-answering]] - Brain-IT-VQA framework for VQA from fMRI, decodes language tokens from brain activity (arXiv: 2605.29588)
   108|  - Token-level decoding outperforms pixel reconstruction
   109|  - NSD-VQA benchmark with 20 controlled question categories
   110|  - **Activation**: Brain-IT, VQA, fMRI decoding, brain question answering, NSD-VQA
   111|
   112|
   113|## 2026-05-29 - Number Theory, Statistics, Advanced Mathematics + Quantum (Cron Job)
   114|
   115|### Paper 2605.29052
   116|- [[quantum-nonautonomous-ode-simulation]] - 量子算法模拟非自治ODE非幺正动力学，通过SVD分解将传播子写为酉算子之和 (arXiv: 2605.29052)
   117|  - quantum ODE
   118|  - nonunitary dynamics
   119|  - SVD dilation
   120|  - quantum simulation
   121|  - **Activation**: quantum ODE, nonunitary dynamics, SVD dilation, quantum simulation
   122|
   123|### Paper 2605.28892
   124|- [[funessian-process-non-markovian]] - Funessian过程：正可分非马尔可夫过程，初始状态记忆贯穿演化，互信息表征非马尔可夫性 (arXiv: 2605.28892)
   125|  - non-Markovian
   126|  - memory effect
   127|  - Chapman-Kolmogorov
   128|  - ergodicity breaking
   129|  - **Activation**: non-Markovian, memory effect, Chapman-Kolmogorov, ergodicity breaking
   130|
   131|### Paper 2605.29130
   132|- [[mersenne-numbers-doubling-map]] - 梅森数与倍角映射动力学联系，无需显式计算即可求因子的替代Lucas-Lehmer方法 (arXiv: 2605.29130)
   133|  - Mersenne numbers
   134|  - doubling map
   135|  - prime testing
   136|  - dynamical systems
   137|  - **Activation**: Mersenne numbers, doubling map, prime testing, dynamical systems
   138|
   139|### Paper 2605.28906
   140|- [[quantum-classical-uncertainty-electromagnetism]] - 经典与量子电磁理论统一不确定关系ΔrΔk≥5/2，适用于光束和单光子 (arXiv: 2605.28906)
   141|  - uncertainty relations
   142|  - electromagnetism
   143|  - classical-quantum correspondence
   144|  - **Activation**: uncertainty relations, electromagnetism, classical-quantum correspondence
   145|
   146|### Paper 2605.28974
   147|- [[quantum-ml-statistics-invariant-theory]] - 基于quiver不变量理论的iPCA模型MLE存在性检验算法，连接统计学与不变量理论 (arXiv: 2605.28974)
   148|  - MLE existence
   149|  - invariant theory
   150|  - quiver representation
   151|  - iPCA
   152|  - **Activation**: MLE existence, invariant theory, quiver representation, iPCA
   153|
   154|### Paper 2605.28931
   155|- [[quantum-ml-ground-state-measurement]] - SIC-POVM测量空间量子基态变分学习，自回归GRU编码概率分布+物理性约束 (arXiv: 2605.28931)
   156|  - quantum ground state
   157|  - SIC-POVM
   158|  - variational learning
   159|  - autoregressive neural network
   160|  - **Activation**: quantum ground state, SIC-POVM, variational learning, autoregressive neural network
   161|
   162|## 2026-05-29 - Neuroscience Research (Cron Job)
   163|
   164|### Graph Neural Network Reveals the Cortical Morphology of Local Brain Aging in Normal Cognition and Alzheimer's Disease
   165|- [[gnn-cortical-morphology-brain-aging]] - GNN-based local brain age estimation from cortical morphology (arXiv: 2601.10912)
   166|  - High-resolution (1.37mm) vertex-level aging pattern analysis
   167|  - Identifies association cortices aging in CN, widespread MCI patterns, comprehensive AD cortical aging
   168|  - Links regional LBA gaps to neuropsychological measures
   169|  - **Activation**: brain age, cortical morphology, GNN, Alzheimer, cognitive impairment, aging patterns
   170|
   171|     1|## 2026-05-29 - Number Theory, Statistics, Advanced Mathematics (Cron Job)
   172|     2|
   173|     3|### End-to-End Formalization of Quantum Error Correction
   174|     4|- [[qec-formal-verification]] - 量子纠错码端到端形式化验证方法论，SAT验证约简+机器检查距离证明 (arXiv: 2605.16523)
   175|     5|  - 稳定子码理论完整形式化（线性代数、Pauli群、二元辛表示）
   176|     6|  - 距离认证问题通过验证SAT约简机器检查
   177|     7|  - BitVec编码将变量数从O(n)降至O(√n)
   178|     8|  - **Activation**: quantum error correction formal verification, stabilizer code distance proof, machine-checked quantum verification, qLDPC certification, QECC end-to-end formalization
   179|     9|
   180|    10|
   181|    11|### Best-First Ordered Statistics Decoding of Quantum LDPC Codes
   182|    12|- [[bf-osd-qldpc-decoding]] - BF-OSD遍历错误候选空间按似然降序，1/100查询预算达到BP+OSD同等性能 (arXiv: 2605.25777)
   183|    13|  - Best-First OSD替代暴力枚举，优先级队列按似然排序
   184|    14|  - 固定BP迭代次数后调用OSD，而非等待收敛
   185|    15|  - 全电路级噪声下特别有效，BP不可靠时优势明显
   186|    16|  - **Activation**: quantum error correction, QLDPC decoding, BF-OSD, belief propagation, ordered statistics decoding
   187|    17|
   188|    18|### Quantum Mechanics: Problems and Paradoxes
   189|    19|- [[quantum-foundations-probability]] - 量子力学基础公理体系：概率起源、Planck常数本质、波函数本体论、测量问题 (arXiv: 2605.30067)
   190|    20|  - 量子理论公理体系形式化
   191|    21|  - 经典振荡器+热浴→量子行为对应模型
   192|    22|  - 概率振幅本质与Born规则推导
   193|    23|  - **Activation**: quantum foundations, quantum probability, measurement problem, wave function ontology, axiom system
   194|    24|
   195|    25|### Entropy-Governed Speedup for Quantum Algorithms on Local Hamiltonians
   196|    26|- [[entropy-governed-quantum-speedup]] (enhanced) - 利用熵结构超越Grover界的量子算法，在深度-d状态上实现更低能量估计 (arXiv: 2605.18241)
   197|    27|  - 输出态能量不超过深度-d态的最小能量
   198|    28|  - 区分强纠缠态与经典可描述态
   199|    29|  - **Activation**: quantum algorithm speedup, local Hamiltonian, entropy-governed, Grover bound
   200|    30|
   201|
### Where the Quantum Lives in D-Wave Hybrid Portfolio Optimization
- [[quantum-finance-stack]] (enhanced) - Audit reveals D-Wave hybrid QPU contributes only 0.7% of wall-clock time; 99% classical decomposition, identical solutions across all budgets showing determinism (arXiv: 2605.17623)
  - QPU mean access time 0.034s out of 5s budget on 54 instances (N=10-640)
  - Cardinality penalty creates dense rank-one term collapsing density benchmark axis
  - Constraint-native interface = classical pipeline + tiny QPU contribution, not quantum sampling win
  - **Activation**: dwave hybrid audit, quantum portfolio benchmark, QPU time analysis, constraint-native, classical decomposition, 量子组合优化审计

### Quantum Portfolio Optimization: An Extensive Benchmark
- [[quantum-finance-stack]] (enhanced) - 250-instance benchmark (up to 1000 assets): MIP solves all in seconds, classical heuristics outperform QA/QAOA (arXiv: 2509.17876)
  - Only very limited room for quantum advantage in portfolio optimization
  - Problem-tailored heuristic consistently outperforms quantum approaches for fixed runtime
  - **Activation**: quantum portfolio benchmark, MIP vs quantum annealing, QAOA comparison, 量子组合优化基准

### Hot-Starting Quantum Portfolio Optimization
- [[hotstart-quantum-portfolio]] (enhanced) - Restricts search to compact Hilbert space around continuous optimum, reducing qubits and outperforming on D-Wave Advantage (arXiv: 2510.11153)
  - Compact Hilbert space QUBO: O(N log δ) qubits vs O(N log M) standard
  - Integrates relaxed continuous solution insights into discrete quantum search
  - **Activation**: hot-start QUBO, quantum portfolio warm-start, compact Hilbert space, reduced qubit portfolio, 量子组合优化热启动

### A Quantum Reservoir Computing Approach to Quantum Stock Movement Forecasting
- [[quantum-reservoir-stock-forecasting]] (enhanced) - QRC with ≤6 qubits achieves >86% accuracy on 20 quantum-sector stock trend predictions, platform-agnostic (arXiv: 2602.13094)
  - Predicts daily closing volumes (2020-2025) and minute-by-minute out-of-market volumes
  - Optimal reservoir parameters identified; works on superconducting circuits and trapped ions
  - **Activation**: quantum reservoir computing, QRC stock forecasting, quantum time-series prediction, small-scale quantum ML, 量子储备池计算股票预测

