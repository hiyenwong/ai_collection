## 2026-05-22 - Number Theory, Statistics, Advanced Mathematics + Quantum (Cron Job — Friday)

### Three Ways to Find Comfort with the Bell Proof and the Results of the Bell Experiments
- [[bell-theorem-statistical-causality]] - Statistical causality framework for analyzing Bell's theorem using Pearl-style causal graphs; three-perspective reconstruction after CHSH violation (non-local randomness, accessible variables, geometric dimension-dependence) (arXiv: 2605.13154)
  - Pearl causal graphs decompose Bell's three assumptions: locality, counterfactual definiteness, freedom
  - CHSH inequality as facet of local polytope; Tsirelson bound 2√2 ↔ 3 spatial dimensions
  - Statistical independence testing for device-independent randomness certification
  - **Activation**: bell theorem statistical causality, Pearl causal graphs quantum, CHSH inequality analysis, quantum nonlocality statistics, counterfactual definiteness, Bell experiment analysis

### Quantum Prediction of Transport Dynamics in Discretized State Spaces
- [[quantum-bayesian-transport-prediction]] - Gate-based quantum algorithm for Bayesian state estimation using Fokker-Planck equation; amplitude encoding + QFT spectral evolution + Wick rotation for unitary diffusion surrogate (arXiv: 2604.24161)
  - Drift implemented exactly via QFT + phase rotations; diffusion via Wick rotation surrogate
  - Exponential state space scaling (2ⁿ for n qubits) for high-dimensional probability distributions
  - Best use case: quantum state used for further quantum processing, not full classical readout
  - **Activation**: quantum Bayesian transport, quantum Fokker-Planck, Wick rotation quantum diffusion, gate-based Bayesian filtering, quantum state prediction amplitudes

### Module Lattice Security (Part III): Structured CVP Distance on the Log-Unit Lattice
- [[module-lattice-security]] - Updated: Part III extends the series with Coarse Lattice Theorem and Trigamma Theorem; reduces CDPR factor for ML-KEM from exp(O~(√n)) to sub-polynomial (arXiv: 2605.17404)
  - CVP distance convergence on log-unit lattice of Q(ζ_{2^k}); Voronoi cell containment
  - Babai's algorithm returns zero for structured targets, exactly recovers unit perturbations
  - Categories: cs.DS, cs.CR, math.NT, math.ST, quant-ph — bridges number theory, statistics, and quantum
  - **Activation**: module lattice security, Weber conjecture, Ring-LWE, Module-LWE, post-quantum cryptography, lattice cryptography

## 2026-05-22 - Neuroscience Research: Brain-DNN Alignment + SNN Sequence Timing (Cron Job)

### Untrained CNNs Match Backpropagation at V1: A Systematic RSA Comparison of Four Learning Rules Against Human fMRI
- [[untrained-cnns-match-backpropagation-at-v1]] - Systematic RSA comparison of BP, FA, PC, STDP against human fMRI (THINGS dataset, 720 stimuli, 3 subjects) showing untrained random CNNs match/exceed BP at V1 alignment (arXiv:2604.16875)
  - Untrained baseline exceeds BP at V1/V2 (ρ=0.076 vs 0.034, Δρ=+0.044, p<0.001) — architecture dominates early vision
  - STDP achieves highest V1 alignment among trained rules (ρ=0.064)
  - At LOC, only BP reliably exceeds random baseline; all rules converge at IT (ρ=0.008–0.014)
  - FA produces consistently lowest alignment at V1, V2, LOC
  - All effects survive pixel-similarity control via Partial RSA
  - **Activation**: brain-DNN alignment, RSA comparison, learning rules, untrained CNN, STDP vision, backpropagation alternative, visual cortex modeling, representational similarity analysis

## 2026-05-22 - Number Theory, Statistics, Advanced Mathematics + Quantum (Cron Job — Hourly Batch)

### Quantum Purity Amplification for Arbitrary Eigenstates and Multiple Outputs
- [[quantum-purity-amplification]] - Coherent transformation of n mixed state copies into high-fidelity eigenstate copies with dimension-uniform sample complexity (arXiv:2605.21570)
  - Path-graph parametrization shows O(m/(epsilon*D^2)) input copies needed, independent of dimension d
  - Generalized Young diagrams yield tight sample complexity bounds across all output regimes
  - First dimension-uniform guarantee for optimal QPA, establishes coherent-incoherent separation
  - **Activation**: quantum purity amplification, QPA, eigenstate purification, coherent quantum information, dimension-uniform sample complexity, generalized Young diagrams

### What We Talk About When We Talk About Dissipative Quantum Chaos
- [[dissipative-quantum-chaos]] - Comprehensive review extending Hamiltonian quantum chaos to open quantum dynamics via Lindbladian spectral analysis (arXiv:2605.21628)
  - Complex eigenvalue spectrum of Lindbladian replaces Hamiltonian for chaos classification
  - Ginibre vs. Poisson level spacing statistics distinguish chaotic from integrable open systems
  - Experimental predictions now being tested in driven-dissipative quantum platforms
  - **Activation**: dissipative quantum chaos, Lindbladian spectral analysis, open quantum systems, Ginibre ensemble, driven-dissipative, quantum integrability

### Optimal Quantum Feshbach Engines
- [[quantum-feshbach-engines]] - Optimization framework for high-efficiency quantum thermodynamic cycles using trapped BECs with Feshbach resonance tuning (arXiv:2605.21562)
  - Dual control: trap stiffness and interaction strength via Feshbach resonance
  - Optimal driving protocols for each stroke using Pontryagin maximum principle
  - Balances power output, efficiency, and quantum coherence preservation
  - **Activation**: quantum Feshbach engine, quantum thermodynamics, BEC heat engine, Feshbach resonance control, quantum optimal control, trapped condensate

## 2026-05-22 - Number Theory, Statistics, Advanced Mathematics + Quantum (Cron Job)

### Maximum Likelihood Decoding of Quantum Error Correction Codes
- [[statistical-mechanics-quantum-decoding]] - Unified MLD framework bridging statistical mechanics (disordered spin models), tensor network contraction, and neural decoder architectures for optimal quantum error correction (arXiv:2605.17230)
  - Maps MLD to partition functions of disordered spin models for exact threshold estimation via phase transitions
  - Tensor network approximation yields near-MLD accuracy with polynomial computational cost
  - Neural decoders (autoregressive, transformer) learn MLD distributions from data for fast real-time decoding
  - **Activation**: maximum likelihood decoding, quantum error correction, statistical mechanics, tensor networks, neural decoder, spin model, phase transition threshold

## 2026-05-22 - Advanced Mathematics + Quantum (Cron Job — Final Batch)

### All Quantum Probability viewed in Complex Projective Geometry
- [[quantum-probability-geometry]] - Geometrizes quantum probability using complex projective space CP^n, replacing Hilbert space projection with Fubini-Study metric geodesic distances on non-linear Kahler manifolds (arXiv:2605.17578)
  - Projection theorem for CP^n: measurement probability = cos^2(Fubini-Study geodesic distance)
  - Purely geometric description of quantum states as points in CP^n, measurements as submanifolds
  - Connects quantum information theory with Kahler geometry and symplectic reduction
  - **Activation**: quantum probability, complex projective geometry, Kahler manifold, Fubini-Study metric, geometric quantum theory, quantum foundations, projection theorem CPn
## 2026-05-22 - Neuroscience Research (Cron Job)

### Learning Sequence Timing and Control of Replay Speed in Networks of Spiking Neurons
- [[learning-sequence-timing-spiking-neurons]] - Extends spiking Temporal Memory (sTM) model to encode element-specific timing via sequential population activation and uses oscillatory inputs as clock signal for flexible replay speed control (arXiv:2605.22523)
  - Timing encoded by sequential activation of element-specific neuronal populations
  - Oscillatory background inputs serve as clock for replay speed modulation
  - Elapsed time represented by unique sparse spatiotemporal neural activity patterns
  - **Activation**: spiking sequence timing, sTM model, oscillatory replay speed, STDP temporal learning, spatiotemporal neural encoding

### Temporal Coding as a Substrate for Sensorimotor Object Inference
- [[temporal-coding-thousand-brains-spiking]] - Spiking reinterpretation of Thousand Brains Architecture replacing dense vectors with rank-order spike packets for sensorimotor inference, using STDP for directional encoding and inter-burst timing for displacement (arXiv:2605.22206)
  - Rank-order spike bursts encode feature identity via firing order (strongest fires first)
  - Time gap between bursts implicitly encodes sensor displacement (no explicit coordinate math)
  - STDP learns traversal direction; adaptive lambda adjusts temporal weighting per object geometry
  - **Activation**: thousand brains spiking, rank-order temporal coding, Monty framework SNN, STDP sensorimotor, neuromorphic object recognition

### Conserved Kinematic Representations enable Zero-Shot Decoding in Handwriting BCIs
- [[conserved-kinematic-zero-shot-bci]] - Demonstrates that motor cortex encodes handwriting through shared kinematic primitives enabling zero-shot decoding of unseen characters, achieving 64% hits@3 on unseen letters (arXiv:2605.19048)
  - Neural alignment framework maps neural activity to imagined kinematics for stroke decomposition
  - Zero-shot decoder achieves 64% hits@3 retrieval on characters never seen during training
  - Provides strong evidence for compositional basis of complex motor control
  - Enables open-vocabulary iBCI communication for logographic languages (Chinese, Japanese)
  - **Activation**: kinematic BCI, zero-shot neural decoding, conserved motor representations, compositional kinematics, handwriting iBCI, logographic BCI, open-vocabulary decoding

### Functional Whole-Brain Models: A New Framework for Unifying Brain Structure and Cognitive Function
- [[functional-whole-brain-models-fwbm]] - Proposes unified paradigm integrating bottom-up whole-brain modeling (biophysical simulations) with top-down neuroconnectionism (task-optimized DNNs) via four minimal criteria and three-pillar roadmap (arXiv:2605.18118)
  - Four criteria: structural grounding, continuous-time dynamics, functional competence, mappable observables
  - Three-pillar roadmap: short-term coupling, mid-term recurrent fWBMs, long-term closed-loop learning
  - Bridges microscopic synaptic mechanisms to macroscopic cognitive functions
  - Enables patient-specific fWBMs for personalized treatment of brain disorders
  - **Activation**: fWBM, functional whole-brain model, neuroconnectionism, brain dynamics framework, cognitive function modeling, brain structure-function integration

### Efficient Coding Under Constraint Drives Neural Systems Towards Criticality and Sloppiness
- [[efficient-coding-criticality-sloppiness]] - Theoretical framework proving that maximizing Fisher information under resource constraints drives neural populations toward criticality (soft modes, power laws) and sloppiness simultaneously, unifying efficient coding with the critical brain hypothesis (arXiv:2605.22598)
  - Fisher information maximization with trace constraint → soft modes with diverging correlation lengths
  - Unifies statistical criticality (power laws) with dynamical criticality (bifurcation, critical slowing down)
  - Provides mechanistic explanation for neural sloppiness as efficient resource allocation
  - Hebb-like learning rule maps onto predictive coding architecture
  - **Activation**: efficient coding, critical brain hypothesis, Fisher information, sloppiness, power-law avalanches, neural criticality, population coding, soft modes, Hebbian learning, predictive coding

## 2026-05-22 - Number Theory, Statistics, Advanced Mathematics + Quantum (Cron Job — 2nd batch)

### Mechanism of Efficacy in QAOA for Random k-SAT: From Adiabatic Manifold to Sublinear Parameter Optimization
- [[qaoa-adiabatic-manifold-samp]] - Discovers that optimal QAOA parameters remain on a smooth adiabatic manifold, enabling SAMP strategy for sublinear parameter optimization and zero-cost deep-circuit initialization (arXiv:2605.20288)
  - Establishes formal correspondence between adiabatic state transfer and QAOA ansatz for random k-SAT
  - Optimal parameters do not become stochastic under depth compression — confined to low-dimensional adiabatic manifold
  - SAMP transforms parameter optimization from unstructured high-dimensional search into guided refinement
  - **Activation**: QAOA parameter optimization, adiabatic manifold, SAMP, random k-SAT, variational quantum algorithm, NISQ, parameter concentration

### Semidefinite Programming for Optimal Quantum Cloning: A Computational Framework
- [[sdp-quantum-cloning-framework]] - Computational framework reformulating quantum cloning as SDP over CPTP maps via Choi-Jamiolkowski isomorphism, providing unified catalogue of Kraus operators for all major cloning families (arXiv:2605.21274)
  - Numerically certifies global optimality through primal-dual strong duality
  - Automatically extracts operational Kraus operators from optimal Choi matrix via spectral decomposition
  - Application to optimal cloning attacks on BB84 under depolarizing noise
  - **Activation**: quantum cloning, semidefinite programming, SDP, Choi-Jamiolkowski isomorphism, Kraus operators, CPTP maps, BB84 security, quantum channel optimization

## 2026-05-22 - Quantum End-to-End Learning + Combinatorial Optimization (Cron Job)

### Quantum End-to-End Learning for Contextual Combinatorial Optimization
- [[quantum-end-to-end-learning-qel]] - First quantum computing-based end-to-end learning framework for contextual combinatorial optimization (CCO), leveraging QAOA with context re-uploading phase-separator (arXiv:2605.20222)
  - Proposes context re-uploading phase-separator inspired by data re-uploading, jointly capturing relations among contexts, uncertain coefficients, and optimal solutions
  - Enables joint end-to-end training with stationarity convergence guarantee, avoiding NP-hard solver calls
  - Achieves competitive performance with substantially fewer parameters than classical benchmarks
  - Validated on contextual knapsack, portfolio optimization, and shortest path problems
  - **Activation**: QEL, contextual combinatorial optimization, quantum end-to-end learning, QAOA, context re-uploading, decision-focused quantum learning, quantum surrogate policy, quantum decision-making

## 2026-05-22 - Number Theory, Statistics, Advanced Mathematics + Quantum (Cron Job)

### On the Spectral theory of Isogeny Graphs and Quantum Sampling of Secure Supersingular Elliptic curves
- [[isogeny-graph-quantum-sampling]] - Proves Quantum Unique Ergodicity for supersingular isogeny graphs, enabling provably secure quantum polynomial-time sampling of elliptic curves for post-quantum cryptography without trusted setup (arXiv:2602.02263)
  - Õ(log⁴p) quantum gate complexity heuristic variant; Õ(log¹³p) under GRH
  - Removes heuristic eigenvalue separation assumption in Kane-Sharif-Silverberg quantum money protocol
  - **Activation**: isogeny graphs, quantum sampling, supersingular elliptic curves, quantum unique ergodicity, post-quantum cryptography, spectral theory, number theory, CGL hash

### Multi-Qubit Golden Gates
- [[multi-qubit-golden-gates]] - Constructs optimal topological generators for compact unitary Lie groups using number theory, enabling ~10x fewer T-type gates than Clifford+T for 2-qubit approximations (arXiv:2509.09047)
  - Proves Sarnak-Xue Density Hypothesis via endoscopic classification of automorphic representations
  - 4.8x fewer non-Clifford gates than Clifford+T; tight upper bounds on CS count
  - **Activation**: golden gates, gate synthesis, Clifford+T, Clifford+CS, topological generators, Lie groups, automorphic forms, quantum compilation

### Geometric Prototype Learning in Quantum Hilbert Space with Matrix Product States
- [[quantum-hilbert-prototype-learning]] - Lifts prototype-based ML to quantum Hilbert space using MPS as class representatives, outperforming classical prototypes via geometric quantum state measures (arXiv:2605.17895)
  - Classification via Born rule: P(c|x) = |⟨φ_c|ψ_x⟩|² — quantum probability as decision function
  - Natural "attraction" effect from Hilbert space geometry enables effective learning
  - Dimensionality reduction via prototype distances; explainable quantum ML
  - **Activation**: quantum prototype learning, matrix product states, quantum Hilbert space, explainable quantum ML, geometric classification, tensor networks, Born rule
## 2026-05-22 - Systems Engineering Research (Cron Job)

### Agentic Agile-V: From Vibe Coding to Verified Engineering in Software and Hardware Development
- [[agentic-agile-v]] - Agentic Agile-V framework with SCOPE-V micro-cycle (Specify, Constrain, Orchestrate, Prove, Evolve, Verify) for verified AI-assisted engineering process control (arXiv:2605.20456)
  - Core Insight: Engineering process control, not prompt engineering, is the central challenge for AI coding agents
  - SCOPE-V Loop: Six-step micro-cycle converting conversational intent → structured engineering artifacts → acceptance evidence
  - Conversation-to-Contract Gate: Separates exploratory dialogue from structured implementation with reviewed briefs
  - Risk-Adaptive Workflows: R1 (auto-approve) / R2 (human review) / R3 (full brief + evidence bundle) based on change scope
  - Evidence Bundle: Task brief, agent plan, test results, diff summary, risk trace, reviewer decision, rollback path
  - **Activation**: agentic engineering, AI agent workflow, verified engineering, SCOPE-V, agent safety, engineering process control, AI code review

### On Integrating Resilience and Human Oversight into LLM-Assisted Modeling Workflows for Digital Twins
- [[llm-dt-resilient-modeling]] - Three design principles for building resilient LLM-assisted Digital Twin modeling workflows with human oversight; FactoryFlow framework (arXiv:2603.25898)
  - Principle 1: Orthogonalize structural modeling (LLM-translated IR with human validation) from parameter fitting (continuous sensor data streams)
  - Principle 2: Restrict model IR to interconnections of pre-validated library components, not monolithic generated code
  - Principle 3: Use density-preserving IR (Python with loops/classes) to minimize hallucination error accumulation
  - Error Characterization: Low-density IRs (verbose) → proportional error amplification; high-density IRs → errors confined to structural choices
  - **Activation**: digital twins, LLM-assisted modeling, FactoryFlow, model-based systems engineering, LLM resilience, human-in-the-loop modeling, simulation automation

## 2026-05-22 - Number Theory, Statistics, Advanced Mathematics + Quantum (Cron Job)

### An Exponential Sample-Complexity Advantage for Coherent Quantum Inference
- [[coherent-quantum-inference]] - Coherent quantum processing achieves exponentially lower sample complexity O(d/ε) vs O(d²/ε²) for incoherent protocols in quantum purity amplification (arXiv:2605.21457)
  - 核心要点 1: 相干量子推断（输出保持量子态）相比非相干协议（先测量再经典处理）实现指数级样本复杂度优势
  - 核心要点 2: 对d维输入的量子纯度放大(QPA)，相干处理仅需O(d/ε)拷贝，非相干需O(d²/ε²)
  - 核心要点 3: 纠缠破坏极限定义了每个相干协议的最优非相干对应物，用于基准测试
  - **Activation**: coherent quantum inference, sample complexity, quantum purity amplification, entanglement-breaking limit, quantum statistics, quantum data processing

### Evidence of Quantum Machine Learning Advantage with Tens of Noisy Qubits
- [[qml-advantage-noisy-qubits]] - Demonstrates clear quantum ML advantage at 30-40 noisy qubit scale; coherent processing outperforms fixed-measurement schemes with data acquisition as the fundamental bottleneck (arXiv:2605.21346)
  - 核心要点 1: 在30-40个噪声量子尺度上，相干量子处理与固定测量方案之间存在清晰性能分离
  - 核心要点 2: 测量优先策略需要数月甚至数年才能匹配相干协议——瓶颈在于数据采集而非经典计算
  - **Activation**: quantum ML advantage, noisy qubits, coherent vs fixed-measurement, learning advantage, quantum data acquisition

### Quantum Nonlocality and Device-Independent Randomness Robust to Noisy Signaling
- [[quantum-nonlocality-robust-signaling]] - Characterizes local polytope vertices/facets with noisy signaling channels; new Bell inequalities more robust than CHSH for device-independent randomness certification (arXiv:2605.21293)
  - 核心要点 1: 即使输入被近完美复制，量子非定域性对噪声信号信道仍具有鲁棒性
  - 核心要点 2: 新识别的Bell不等式在认证DI随机性时比CHSH不等式对去极化噪声更鲁棒
  - **Activation**: quantum nonlocality, device-independent randomness, Bell inequalities, noisy signaling, local polytope, quantum cryptography

## 2026-05-22 - Neuroscience Research: Texture Perception + CNN Alignment (Cron Job)

### Perceptual Misalignment of Texture Representations in CNNs
- [[texture-misalignment-cnn-perception]] - Systematic investigation finding no correlation between CNN Brain-Score and alignment with human texture perception; texture perception involves mechanisms distinct from object recognition CNNs (arXiv:2604.01341)
  - 核心要点 1: CNN基于Gram matrix的纹理表征与人类纹理感知不对齐，无论网络架构、深度或训练目标
  - 核心要点 2: Brain-Score高的模型并不具有更类人的纹理表征——模型视觉系统对齐程度与纹理感知对齐无关
  - 核心要点 3: 纹理感知需要超越标准物体识别CNN的额外机制，可能依赖上下文信息整合
  - **Activation**: texture perception, CNN texture representation, Gram matrix, Brain-Score, visual perception alignment, perceptual misalignment, Julesz texture

## 2026-05-22 - Number Theory, Statistics, Advanced Mathematics + Quantum (Cron Job)

### Quantum Viterbi Algorithm
- [[quantum-viterbi-decoding]] - 将经典Viterbi解码算法扩展到隐量子马尔可夫模型，在连续量子效应流形上优化，证明超越经典对角策略的严格量子优势 (arXiv:2605.18912)
  - 核心要点 1: HQMM的隐状态是连续流形上的纯量子效应而非离散状态，利用隐记忆中的相干叠加
  - 核心要点 2: 严格量子优势定理：相干隐轨迹的解码得分严格超过任何约束于对角（交换）效应的经典策略
  - **Activation**: quantum viterbi, HQMM, hidden quantum Markov model, sequential quantum decoding, quantum advantage, NISQ ML, 量子维特比算法

### Q-SYNTH: Hybrid Quantum-Classical Adversarial Augmentation
- [[q-synth-hybrid-quantum-gan-fraud]] - 混合经典-量子生成对抗框架，参数量子电路作为生成器、经典神经网络作为判别器，用于不平衡欺诈检测中的少数类合成 (arXiv:2605.21164)
  - 核心要点 1: 在分布保真度（KS统计量、Wasserstein距离）和下游分类性能之间取得优于经典GAN的平衡
  - 核心要点 2: 参数量子电路在表格数据生成中展现独特优势，减少边缘分布不匹配
  - **Activation**: quantum GAN, fraud detection, class imbalance, Q-SYNTH, parameterized quantum circuit, tabular data generation, hybrid quantum-classical

### Leakage-Free Quantum ML Evaluation for Cyber-Physical Systems
- [[leakage-free-qml-cyber-physical]] - 无人机异常检测中量子ML的无泄漏评估方法，提出时间感知分组协议和三模式特征审计，确保量子优势的统计严谨性 (arXiv:2605.19233)
  - 核心要点 1: B2时间分组协议消除随机分层划分中混合相邻样本导致的性能膨胀
  - 核心要点 2: 三模式特征审计量化瞬态物理信号与上下文代理特征的贡献比例
  - **Activation**: leakage-free evaluation, quantum ML benchmark, cyber-physical anomaly, UAV detection, temporal protocol, feature audit, DRU classifier

## 2026-05-22 - Number Theory, Statistics, Advanced Mathematics (Cron Job)

### Flow loops and quantum groups
- [[flow-loops-quantum-groups]] - 连接量子群不变量与Morse流动力学研究纽结拓扑 (arXiv: 2605.21382)
  - 核心要点 1: 纤维纽结的补空间上Morse流闭轨道计数产生双变量级数不变量
  - 核心要点 2: 动力学级数猜想等价于3d N=2 QFT的BPS q-级数, 桥接动力系统与量子拓扑
  - **Activation**: flow loops, quantum groups, Morse flow knots, BPS q-series, 量子群不变量, 纽结拓扑

### O(n) alternative to Quantum Fourier Transform
- [[shallow-qft-alternative-hp-circuits]] - O(n)复杂度替代QFT结合神经网络经典后处理 (arXiv: 2605.16998)
  - 核心要点 1: 识别QFT在隐藏子群问题中的两个关键性质: 平移不变性和子群生成元信息保留
  - 核心要点 2: 提出O(n)深度的替代方案, 大幅降低电路深度要求
  - **Activation**: QFT alternative, O(n) circuit, hidden subgroup, Shor algorithm

### Mechanism of Efficacy in QAOA for Random k-SAT
- [[qaoa-adiabatic-manifold-k-sat]] - 发现QAOA在随机k-SAT中的有效机制: 绝热流形与亚线性参数优化 (arXiv: 2605.20288)
  - 核心要点 1: 在通用mixer k-local搜索框架中发现QAOA最优参数位于光滑绝热流形上
  - 核心要点 2: 流形可用亚线性数量参数表征, 实现高效参数优化
  - **Activation**: QAOA mechanism, k-SAT, adiabatic manifold, sublinear optimization

## 2026-05-22 - Neuroscience Research: Spike Forecasting + Functional Whole-Brain Models (Cron Job)

### Implicit Behavioral Decoding from Next-Step Spike Forecasts at Population Scale
- [[mamba-spike-forecasting-behavioral-decoding]] - Mamba forecaster trained on next-step spike counts at Neuropixels scale simultaneously predicts future neural activity and decodes behavioral state via lightweight linear readout (arXiv:2605.12999)
  - Mamba beats linear decoder on raw spike counts by 4-6pp on mouse choice (75.7%) and stimulus side (66.1%)
  - Single Mamba forecaster delivers both neural forecast and behavior readout in one forward pass
  - ~100-150 trial calibration brings within 1-2pp of asymptote; fits 50ms bin budget on workstation GPUs
  - Tested on Steinmetz benchmark: 39 sessions, ~27k neurons, 1,994 held-out trials
  - **Activation**: spike forecasting, behavioral decoding, Mamba neural, Neuropixels decoder, closed-loop BCI, implicit decoding, neural population forecasting, SSM neural time series

### Functional Whole-Brain Models: A New Framework for Unifying Brain Structure and Cognitive Function
- [[functional-whole-brain-models-fwbm]] - fWBMs unify bottom-up whole-brain models (biophysical simulations) with top-down neuroconnectionism (DL networks) under 4 criteria: structural grounding, dynamical realism, functional competence, mappable observables (arXiv:2605.18118)
  - 4 criteria: structural grounding in empirical connectomes, continuous-time dynamical realism, functional competence across cognitive domains, mappable observables to neuroimaging/electrophysiology
  - Three-pillar roadmap: short-term (minimal fWBM architectures), mid-term (complex cognitive domains + plasticity), long-term (full-scale human brain models)
  - Opens clinical opportunities for lesion-deficit mapping, psychiatric circuit testing, connectome-based prediction
  - **Activation**: functional whole-brain model, fWBM, neuroconnectionism, whole-brain modeling, brain structure function unification, cognitive brain simulation, connectome functional competence

### MIRAGE: Robust Multi-Modal fMRI-to-Mental-Image Decoding
- [[mirage-fmri-mental-imagery-decoding]] - MIRAGE explicitly designs for cross-decoding generalization from visual perception to mental imagery: linear backbone + multi-modal text/image features → diffusion model achieves SOTA on NSD-Imagery benchmark (arXiv:2605.17198)
  - SOTA on seen images ≠ SOTA on mental imagery — architecture must be explicitly designed for cross-decoding
  - Linear backbone + low-dimensional image features + text guidance + multi-level features outperforms complex nonlinear architectures
  - Text-based features provide critical semantic guidance for mental image reconstruction
  - Human raters and feature metrics confirm SOTA quality on NSD-Imagery benchmark
  - **Activation**: MIRAGE mental imagery, fMRI mental image reconstruction, brain-to-image decoding, NSD-Imagery, vision decoder generalization, mental imagery fMRI, cross-decoding brain activity, fMRI diffusion model

## 2026-05-22 - Number Theory, Statistics, Advanced Mathematics + Quantum Mechanics (Cron Job)
     2|
     3|### Evidence of Quantum Machine Learning Advantage with Tens of Noisy Qubits
     4|- [[quantum-ml-advantage-noisy]] - Demonstrates coherent quantum ML advantage at 30-40 noisy qubits scale; data acquisition becomes the fundamental bottleneck over classical computation (arXiv:2605.21346)
     5|  - Coherent quantum processing shows clear performance separation vs fixed-measurement schemes under realistic hardware noise
     6|  - At 30-40 qubit scale, measure-first matching requires months to years of data collection
     7|  - Systematic hardware constraint evaluation framework: state prep, gate errors, readout, connectivity, coherence times
     8|  - **Activation**: quantum ml advantage, noisy qubits, qml benchmark, coherent processing, quantum data acquisition, NISQ machine learning, 量子机器学习优势
     9|
    10|### An Entropy-Governed Speedup for Quantum Algorithms on Local Hamiltonians
    11|- [[entropy-governed-quantum-speedup]] - Faster quantum algorithm for low-energy estimation on k-local Hamiltonians that breaks the Grover bound O(2^{n/2}) by targeting depth-d state energy minimums (arXiv:2605.18241)
    12|  - Outputs quantum state with energy bounded by minimum over all depth-d circuits
    13|  - Provides insight into distinguishing strongly entangled vs classically describable states
    14|  - For Hamiltonians with depth-d ground states, matches Buhrman et al. (PRL 2025) guarantees but faster
    15|  - **Activation**: entropy-governed speedup, local Hamiltonian, depth-d states, Grover bound, quantum complexity, low-energy estimation, state preparation, 熵调控量子加速
    16|
    17|### Statistical Quantum Phase Estimation: Extensions and Practical Considerations
    18|- [[statistical-quantum-phase-estimation]] - SQPE refinements for early fault-tolerant quantum computers: handles negative Pauli weights, changepoint detection without overlap estimates, 2x sample reduction via Fourier symmetry (arXiv:2605.18876)
    19|  - Generalizes random compilation for arbitrary-sign Pauli weights in LCU decomposition
    20|  - Changepoint detection replaces overlap-dependent GSE estimation (no chicken-and-egg problem)
    21|  - Fourier series symmetry halves circuit runs while maintaining accuracy
    22|  - **Activation**: statistical quantum phase estimation, SQPE, ground state energy, changepoint detection, LCU decomposition, Pauli weights, Fourier symmetry, early fault-tolerant quantum computing
    23|
    24|### Circuits of Quantum Hashing and Quantum Fourier Transform for a Cactus as a Qubit Connectivity Graph
    25|- [[quantum-hashing-qft-connectivity]] - O(n^2*m) quantum circuit optimization for quantum hashing and QFT on cactus graph connectivity, improving over exponential-time algorithm for arbitrary graphs (arXiv:2605.20789)
    26|  - Uses shortest non-simple 1-covering path as polynomial-time subroutine
    27|  - Applies to NISQ devices with restricted qubit connectivity (IBM Q, Rigetti)
    28|  - Independently useful graph theory result for cactus graphs
    29|  - **Activation**: quantum hashing, quantum fingerprinting, qubit connectivity graph, cactus graph, QFT optimization, quantum circuit compilation, 1-covering path, NISQ routing
    30|
    31|## 2026-05-22 - Neuroscience Research (Cron Job)
    32|
    33|### Brain Alignment of Reasoning and Action Representations from VLMs and LAMs During Gameplay
    34|- [[brain-alignment-vlm-lam-gameplay]] - Vision-language models (VLMs) and large-action models (LAMs) exhibit strong brain alignment with fMRI during naturalistic Atari gameplay, outperforming RL baselines with prompt-driven gains scaling with cortical hierarchy (arXiv:2605.19352)
    35|  - VLM is prompt-symmetric (12.5% action vs 13.6% reasoning unique variance); LAM is prompt-asymmetric (27% action vs -5% reasoning)
    36|  - Largest encoding improvements in frontal-parietal and motor-planning regions
    37|  - Action-specialized fine-tuning reorganizes multimodal representations toward action-relevant neural computations
    38|  - **Activation**: brain alignment VLM LAM, vision-language model brain encoding, large-action model neural alignment, naturalistic gameplay fMRI, action reasoning representations brain
    39|
    40|### Letting the Neural Code Speak: Automated Characterization of Visual Neurons Through Human Language
    41|- [[neural-code-speak]] - Closed-loop framework using generative models and neural digital twins to translate each neuron's high/low activating images into semantic hypotheses, verified in silico; 96.1% of V4 neurons driven above 95th percentile by hypothesis-generated images (arXiv:2605.12485)
    42|  - Descriptions range from oriented edges/spatial frequency in V1 to conjunctions of form/color/texture in V4
    43|  - Language compression is lossy but semantically faithful; RSA shows alignment recovered when hypotheses rendered back into images
    44|  - Enables agentic scientific discovery for interpretable neural function description at scale
    45|  - **Activation**: neural code language, automated neuron characterization, neural digital twin visual cortex, closed-loop neuron description, semantic hypothesis neural selectivity, macaque V1 V4 neuron description
    46|
    47|### A Simple Model of Co-Emergence of Grid and Place Fields
    48|- [[grid-place-co-emergence]] - First unified recurrent network model instantiating Dale's Law where grid and place cells co-emerge from a single sensory-prediction objective without supervision of either type (arXiv:2605.21356)
    49|  - Single-objective RNN trained to predict next sensory observation from masked previous observations and egocentric motion
    50|  - Coexists across 1,000 training configurations; balance set by sensory noise and masking
    51|  - Reproduces grid fragmentation, merging, lattice alignment, 3D bat fields, and developmental order without retraining
    52|  - Two complementary encoding pressures: reconstruction (place-like) vs prediction (grid-like)
    53|  - **Activation**: grid cell place cell co-emergence, Dale's law RNN, spatial navigation sensory prediction, hippocampal-entorhinal unified model, grid field co-emergence, 网格细胞位置细胞共同涌现
    54|
    55|### Platonic Representations in the Human Brain: Unsupervised Recovery of Universal Geometry
    56|- [[platonic-representations-brain]] - Extends Strong Platonic Representation Hypothesis to human visual cortex, proving subject-specific fMRI representations are approximately isometric and translatable via unsupervised geometric transformations without paired data (arXiv:2605.20496)
    57|  - Self-supervised encoder from fMRI data exploiting repeated stimulus presentations
    58|  - Unsupervised orthogonal rotations recover accurate cross-subject instance-level correspondences
    59|  - Synchronized pairwise rotations into shared latent space further improves retrieval
    60|  - Evidence for shared universal neural geometry across individuals in visual cortex
    61|  - **Activation**: platonic representation human brain universal geometry, fMRI cross-subject unsupervised alignment, shared neural geometry visual cortex, deep learning brain representation translation, 柏拉图表征人脑视觉皮层通用几何
    62|
    63|
    64|### MLLM Brain Alignment via Task-Conditioned Probing
    65|- [[mllm-brain-alignment-task-probing]] - Instruction-tuned MLLMs show higher brain alignment than non-IT models during naturalistic movie watching; reveals task-specific neural representations across brain regions (arXiv:2506.08277)
    66|  - IT-MLLMs achieve ~9-20% higher brain alignment vs baselines
    67|  - Task-specific instructions produce distinct MLLM representations across brain regions
    68|  - ICL models show strong semantic coupling (r=0.78) while IT-MLLMs show weak semantic coupling (r=0.14)
    69|  - **Activation**: brain-MLLM alignment, instruction-tuned MLLM, task-conditioned probing, fMRI encoding
    70|
    71|### E-ReCON: Energy-Efficient nvCIM Macro for SNN/CNN Edge Inference
    72|- [[erecon-snn-nvcim-hardware]] - 16Kb energy- and resource-efficient DCIM macro with 3T1R ReRAM bitcell supporting both CNN and SNN workloads (arXiv:2605.20717)
    73|  - Novel 3T1R bitcell with AND-based in-memory multiplication for dual workload support
    74|  - Interleaved 10T/28T adder tree reduces transistor count by 37% and power by 28%
    75|  - Achieves 419 TOPS/W energy efficiency at 2.31-3.1 TOPS throughput
    76|  - 2A2W precision matches FP32 baseline accuracy across VGG/ResNet on ImageNet
    77|  - **Activation**: nvCIM, ReRAM CIM, SNN hardware accelerator, neuromorphic hardware macro
    78|## 2026-05-21 - Neuroscience Research (Cron Job)
    79|
    80|### Closed-Form Predictive Coding via Hierarchical Gaussian Filters
    81|- [[closed-form-predictive-coding-hgf]] - Restores precision-weighted prediction errors to predictive coding networks using deep hierarchical Gaussian filters, enabling biologically plausible learning without backpropagation (arXiv:2605.20293)
    82|  - Core: Expresses PC networks as HGFs with closed-form variational inference for activations, weights, and precisions
    83|  - Results: Approaches backpropagation on FashionMNIST; outperforms on online/data-efficiency/concept-drift tasks
    84|  - Biological grounding: Hebbian-compatible local update rules; precision-weighting connects to cortical attention/uncertainty
    85|  - **Activation**: predictive coding, hierarchical Gaussian filter, free energy principle, precision-weighted prediction error, biologically plausible learning, HGF
    86|
    87|### How to Build Marcus's Algebraic Mind: VaCoAl over Galois Fields
    88|- [[algebraic-mind-vacoa]] - Maps Gary Marcus's three pillars of cognitive architecture onto PyVaCoAl/VaCoAl hyperdimensional computing using XOR-and-shift over GF(2) (arXiv:2605.21379)
    89|  - Core: Single algebraic primitive (XOR-shift) implements reversible variable binding, non-commutative bundling, and individual/kind separation
    90|  - Biological homologue: Dentate gyrus-CA3 circuit as VaCoAl's natural implementation
    91|  - Extends to Pearl's rung-3 counterfactual reasoning
    92|  - **Activation**: vacoal, hyperdimensional computing, algebraic mind, Gary Marcus, reversible variable binding, Galois fields, PyVaCoAl
    93|
    94|### MLLM Brain Alignment via Task-Conditioned Probing
    95|- [[mllm-brain-alignment-task-probing]] - Instruction-tuned MLLMs show higher brain alignment than non-IT models during naturalistic movie watching; reveals task-specific neural representations across brain regions (arXiv:2506.08277)
    96|  - IT-MLLMs achieve ~9-20% higher brain alignment vs baselines
    97|  - Task-specific instructions produce distinct MLLM representations across brain regions
    98|  - ICL models show strong semantic coupling (r=0.78) while IT-MLLMs show weak semantic coupling (r=0.14)
    99|  - **Activation**: brain-MLLM alignment, instruction-tuned MLLM, task-conditioned probing, fMRI encoding
   100|
   101|### E-ReCON: Energy-Efficient nvCIM Macro for SNN/CNN Edge Inference
   102|- [[erecon-snn-nvcim-hardware]] - 16Kb energy- and resource-efficient DCIM macro with 3T1R ReRAM bitcell supporting both CNN and SNN workloads (arXiv:2605.20717)
   103|  - Novel 3T1R bitcell with AND-based in-memory multiplication for dual workload support
   104|  - Interleaved 10T/28T adder tree reduces transistor count by 37% and power by 28%
   105|  - Achieves 419 TOPS/W energy efficiency at 2.31-3.1 TOPS throughput
   106|  - 2A2W precision matches FP32 baseline accuracy across VGG/ResNet on ImageNet
   107|  - **Activation**: nvCIM, ReRAM CIM, SNN hardware accelerator, neuromorphic hardware macro
   108|
   109|## 2026-05-22
   110|
   111|### Enhanced Reinforcement Learning-based Process Synthesis via Quantum Computing
   112|- [[quantum-systems-engineering-2026]] - Quantum systems engineering methodology covering sidecar architectures, resource allocation, energetic optimization, and RL-based process synthesis via quantum computing (arXiv:2605.21213)
   113|  - Core: Formulates process synthesis as MDP solved with quantum-enhanced RL
   114|  - Pattern: Quantum sidecar architecture with stateful/stateless operating modes
   115|  - **Activation**: quantum systems engineering, hybrid quantum architecture, quantum resource allocation, quantum sidecar, quantum process synthesis, 量子系统工程, 量子混合架构
   116|
   117|### Quantum Sidecar Architectures for Hybrid AI Training and Inference
   118|- Part of quantum-systems-engineering-2026 - Two-mode quantum co-processor architecture (arXiv:2605.18031)
   119|  - Stateful protected register mode for reusable quantum resources
   120|  - Stateless reset-and-reprepare mode for per-invocation circuits
   121|
   122|### System Aware Resource Allocation for Distributed Quantum Workflows
   123|- Part of quantum-systems-engineering-2026 - Comprehensive quantum program allocation (arXiv:2605.17944)
   124|  - Qubit availability, circuit depth, error rate, and workflow dependency optimization
   125|
   126|### Energetic Advantage in Superconducting Cat-Qubits
   127|- Part of quantum-systems-engineering-2026 - Energy optimization methodology (arXiv:2605.19854)
   128|  - Quantum energetic advantage before computational advantage at >26 qubits
   129|
   130|## 2026-05-21 - Systems Engineering + Quantum (Cron Job)
   131|
   132|### Coupling-Phase Engineering for Giant-Atom Waveguide QED Systems
   133|- [[coupling-phase-giant-atom-control]] - Use coupling phase to control bound states in the continuum (BICs) and quantum dynamics in nonlocal light-matter interfaces (arXiv: 2605.17878)
   134|  - Core: Giant atoms couple to waveguides at multiple spatially separated points, enabling interference-based BIC engineering
   135|  - Pattern: Coupling phase modulation controls BIC number, profile, and dynamical behavior
   136|  - Applications: Quantum state trapping, protected quantum information processing, giant-atom quantum networks
   137|  - **Activation**: giant atom, waveguide QED, bound state in continuum, coupling phase engineering, BIC quantum, 量子巨原子, 连续谱束缚态
   138|
   139|## 2026-05-21 - Systems Engineering (Cron Job)
   140|
   141|### Modeling and Resource Optimization for Quantum Oracles
   142|- [[quantum-oracle-resource-optimization]] - Formal oracle description and space-depth trade-off algorithm achieving 54% circuit depth reduction (arXiv: 2605.21380)
   143|  - HRSE model enables hierarchical recursive synthesis-evaluation for formal oracle description
   144|  - ASDT algorithm generates optimal oracle structures under fixed qubit constraints
   145|  - **Activation**: quantum oracle, oracle optimization, HRSE model, ASDT algorithm, space-depth tradeoff, quantum circuit optimization
   146|
   147|### When Does Adaptation Win? Scaling Laws for Meta-Learning in Quantum Control
   148|- [[quantum-control-meta-learning-scaling]] - Scaling law for meta-learning adaptation gain in quantum control with >40% fidelity gains (arXiv: 2601.18973)
   149|  - Already exists in collection (checked for duplicates)
   150|  - **Activation**: quantum control, meta-learning, scaling laws, adaptation gain
   151|
   152|
   153|
   154|## 2026-05-21 - Neuroscience Research (Cron Job)
   155|
   156|### Platonic Representations in the Human Brain: Unsupervised Recovery of Universal Geometry
   157|- [[platonic-representations-brain]] - Cross-subject neural geometry alignment in human visual cortex, demonstrating that subject-specific fMRI representations are approximately isometric and can be translated through purely geometric transformations without paired data (arXiv: 2605.20496)
   158|  - Self-supervised encoder learns subject-specific embeddings from fMRI data via repeated stimulus presentations
   159|  - Unsupervised orthogonal rotations translate representations across subjects without paired samples
   160|  - Synchronized pairwise rotations into a shared latent space improves cross-subject retrieval
   161|  - Evidence for shared universal neural geometry across individuals in visual cortex
   162|  - **Activation**: platonic representation human brain, cross-subject brain alignment unsupervised, fMRI representation geometry translation, shared neural geometry visual cortex, 柏拉图表示人脑通用几何
   163|
   164|## 2026-05-21 - Systems Engineering + Quantum (Cron Job)
   165|
   166|### QUTest: A Native Testing Framework for Quantum Programs
   167|- [[quantum-native-testing-framework]] - Native OpenQASM 3 testing framework with pragma-based assertions, 12 assertion types, linter, and CI integration for quantum programs (arXiv: 2605.19736)
   168|  - Both programs and tests are standard .qasm files using //% pragma comments
   169|  - 12 assertion types: deterministic, statistical, quantum-state, and structural checks
   170|  - Environment-aware mode for cross-runtime testing (Qiskit, Cirq, Qulacs)
   171|  - CLI with auto test discovery, compatibility checks, and JUnit XML reports
   172|  - **Activation**: quantum native testing, openqasm testing framework, quantum test assertions, quantum program testing, qasm test framework, quantum CI testing, pragma quantum testing, 量子测试框架
   173|
   174|### PIQC: Scalable Distributed Quantum Computing via Photonic Integration of Designed Molecular Quantum Nodes
   175|- [[piqc-distributed-quantum-computing]] - Scalable distributed quantum computing architecture using photonic integration of designed molecular quantum nodes (NV/SiV centers in diamond) with nanophotonic waveguide networks for entanglement distribution (arXiv: 2605.21204)
   176|  - NV/SiV centers as quantum processing nodes with long coherence times
   177|  - Nanophotonic waveguide interconnects for modular scalability
   178|  - Heralded entanglement distribution via spin-photon entanglement and photon interference
   179|  - Systems engineering framework for error budget analysis and topology design
   180|  - **Activation**: photonic integrated distributed quantum computing, molecular quantum nodes, NV center quantum network, distributed quantum architecture
   181|
   182|### Measurement and Control of the Complex Berry Phase in a Quantum System
   183|- [[complex-berry-phase-quantum-control]] - Complex Berry phase measurement and control methodology for non-Hermitian quantum systems using superconducting transmon circuits with engineered dissipation (arXiv: 2605.16559)
   184|  - Complex Berry phase decomposition into real (geometric phase) and imaginary (amplification/attenuation) components
   185|  - Engineered dissipation used as control resource rather than liability
   186|  - Non-unitary quantum control via path-dependent geometric effects
   187|  - Geometric quantum gates with SU(1,1) operations
   188|  - **Activation**: complex Berry phase quantum control, non-Hermitian geometric phase, transmon circuit Berry phase, engineered dissipation quantum control
   189|
   190|### Enhanced Reinforcement Learning-based Process Synthesis via Quantum Computing
   191|- [[quantum-rl-process-synthesis]] - Quantum reinforcement learning methodology for process systems engineering that encodes process synthesis as MDPs with state encoding algorithms decoupling qubit requirements from problem size (arXiv: 2605.21213)
   192|  - Process synthesis formally posed as MDP with compressed state encoding
   193|  - Quantum-enhanced RL shows competitive per-episode performance and superior per-parameter efficiency vs classical RL
   194|  - State encoding decouples qubit count from problem size for scalability
   195|  - **Activation**: quantum reinforcement learning process synthesis, quantum RL engineering design, quantum process optimization, flowsheet synthesis quantum, quantum MDP process systems
   196|
   197|### Software Between Quantum and Machine Learning -- And Down to Pulses
   198|- [[quantum-control-pulse-software]] - Software framework integrating quantum optimal control within QML for pulse-level modelling, bridging gate-based abstractions with hardware-aware optimisation using JAX-based high-performance implementation (arXiv: 2605.21286)
   199|  - Composable ansatz constructions with interchangeable building blocks for pulse-level modelling
   200|  - End-to-end optimisation of pulse parameters within QML setting
   201|  - Fourier-analytic diagnostics and extended entanglement measures for analysis
   202|  - **Activation**: quantum pulse level control, quantum optimal control software, QML pulse modelling, quantum gate abstraction, hardware-aware quantum optimisation
   203|
   204|## 2026-05-21 - Neuroscience Research (Cron Job)
   205|
   206|### Stimulus Symmetries Can Confound Representational Similarity Analyses
   207|- [[stimulus-symmetries-rsm-confound]] - Demonstrates that stimulus symmetries in network inputs cause functionally-equivalent neural representations to produce different, drifting RSM geometries, challenging common assumptions in RSA/CKA analyses (arXiv: 2605.21324)
   208|  - Formal proof that stimulus symmetries produce gauge-dependence in RSMs — functionally equivalent codes yield different geometries
   209|  - SGD/energy regularization drives RSMs to drift over training via sparse, manifold-tiling codes
   210|  - Phenomena persist in image-trained networks with latent (not explicit) symmetries
   211|  - Challenges the assumption that RSM invariance to rotation captures all meaningful equivalence
   212|  - **Activation**: representational similarity analysis, RSM gauge dependence, stimulus symmetry, RSA confound, neural code comparison, drifting representations, representational geometry, functionally equivalent representations, neural manifold tiling, CKA limitations, RSA robustness, stimulus invariance
   213|
   214|### Platonic Representations in the Human Brain: Unsupervised Recovery of Universal Geometry
   215|- [[platonic-representations-brain-universal-geometry]] - Evidence for a shared neural geometry in human visual cortex where subject-specific fMRI representations are approximately isometric and translatable via unsupervised geometric transformations (arXiv: 2605.20496)
   216|  - Self-supervised encoder learns subject-specific fMRI embeddings from repeated stimulus presentations
   217|  - Unsupervised orthogonal rotation alignment translates independently learned brain spaces across subjects
   218|  - Shared latent space via synchronized pairwise rotations improves cross-subject retrieval
   219|  - **Activation**: platonic representation, universal brain geometry, cross-subject fMRI alignment, isometric neural embedding, unsupervised brain translation, visual cortex representation
   220|
   221|### Functional Whole-Brain Models: A New Framework for Unifying Brain Structure and Cognitive Function
   222|- [[functional-whole-brain-models-fwbm]] - Unified modeling paradigm integrating structural brain grounding, continuous-time dynamical realism, and task-performing cognitive capacity (arXiv: 2605.18118)
   223|  - Four minimal criteria: structural grounding, dynamical realism, functional competence, mappable observables
   224|  - Three-pillar roadmap bridging bottom-up WBM and top-down neuroconnectionism
   225|  - Short-/mid-/long-term horizons toward personalized brain simulation for clinical applications
   226|  - **Activation**: functional whole-brain model, fWBM, whole-brain modeling, neuroconnectionism, brain structure-function, brain dynamics simulation, neural mass model
   227|
   228|### Von Economo Neurons Enable Reliable Social Skill Acquisition in Recurrent Spiking Neural Networks
   229|- [[vencircuit-ven-gradient-scaffold]] - Biologically motivated SNN showing VENs function as residual gradient scaffolds: 2% VENs confer 21x training convergence advantage via direct gradient pathway immune to recurrent Jacobian instabilities, with clinical predictions for ASC vs bvFTD (arXiv: 2605.17399)
   230|  - VEN-intact networks converge 98% vs 70% ablated (Fisher's OR=21.0, p=8.7×10⁻⁵)
   231|  - VENs provide O(1) gradient pathway structurally immune to product instabilities
   232|  - Mid-training ablation (epochs 5-25) most disruptive; inference-time VENs largely dispensable
   233|  - Predicts timing of VEN loss determines social cognitive consequences (developmental vs adult)
   234|  - **Activation**: Von Economo neuron, VENCircuit, gradient scaffold SNN, spiking neural network social cognition, residual connections SNN
   235|
   236|### Geometric Phase Transition Enables Extreme Hippocampal Memory Capacity
   237|- [[geometric-phase-transition-hippocampal-memory]] - Extreme spatial memory in food-caching birds arises from a topological phase transition from disorganized "mist" to geometrically rigid "crystalline" hippocampal population code, enabling >100x capacity via neural manifold stiffening (arXiv: 2605.17199)
   238|  - Crystalline codes sustain >1,000 locations vs mist codes failing below 10 (>100x advantage)
   239|  - Excitatory-inhibitory synergy: excitatory scaffold + inhibitory orthogonal decorrelation
   240|  - 169-fold "geometric tax" — representational redundancy stabilizing manifold against noise
   241|  - Double dissociation with Valiant's model confirms continuous topological organization
   242|  - **Activation**: geometric phase transition, crystalline neural code, hippocampal memory, geometric tax, food-caching birds spatial memory, mist code vs crystalline code
   243|
   244|### A Simple Model of Co-Emergence of Grid and Place Fields (Evening Supplement)
   245|- [[grid-place-cell-co-emergence]] - First unified recurrent network model achieving co-emergence of grid cells and place cells from a single sensory-prediction objective without supervision of either cell type (arXiv: 2605.21356)
   246|  - Grid fields for path integration (motion prediction pressure), place fields for pattern completion (sensory reconstruction pressure)
   247|  - Both spatial codes coexist across 1,000+ training configurations; balance controlled by sensory noise/masking
   248|  - Qualitatively reproduces grid fragmentation, wall-removal merging, lattice alignment, 3D bat fields, and developmental ordering
   249|  - **Activation**: grid cells, place cells, co-emergence, sensory prediction, path integration, entorhinal cortex-hippocampus loop, spatial navigation, grid cell development
   250|
   251|### Self-Supervised Local Learning Rules Discover Hidden Hierarchical Structure
   252|- [[self-supervised-local-learning-rhm]] - Biologically plausible learning algorithms showing that layerwise self-supervised (contrastive/non-contrastive) rules can learn hidden hierarchical structure as efficiently as backpropagation, while gradient-feedback rules fail due to input-specific nonlinearity masking (arXiv: 2605.18557)
   253|  - Direct-feedback alignment rules fail on Random Hierarchy Model (RHM) tasks due to "masking" — input-specific nonlinearities essential for complex tasks
   254|  - Self-supervised local rules (contrastive and non-contrastive) match backprop data efficiency
   255|  - Compatible with known cortical synaptic plasticity rules; provides candidate mechanism for cortex learning without explicit error signals
   256|  - **Activation**: biologically plausible learning, local learning rules, backpropagation-free learning, self-supervised learning, cortical plasticity, hierarchical representation learning, Random Hierarchy Model, masking phenomenon
   257|
   258|### Subject-Specific Analysis of Self-Initiated Attention Shifts from EEG
   259|- [[eeg-self-initiated-attention-shifts]] - Machine learning framework distinguishing self-initiated vs externally-instructed attention shifts from preparatory EEG activity, with SHAP-based feature attribution showing frontal high-frequency bands as key discriminators (arXiv: 2605.18251)
   260|  - Controlled experimental paradigm isolating self-initiated shifts under identical visual stimulation
   261|  - Reliable within-subject classification from preparatory EEG spectral features
   262|  - SHAP analysis reveals frontal regions and higher-frequency bands dominate model decisions
   263|  - **Activation**: EEG attention shifts, self-initiated attention, brain-computer interface, SHAP EEG analysis, preparatory neural activity, attention decoding, spectral EEG features
   264|  
   265|## 2026-05-21 - Systems Engineering + Quantum Mechanics (Cron Job)
   266|
   267|### When Does Adaptation Win? Scaling Laws for Meta-Learning in Quantum Control
   268|- [[quantum-control-meta-learning-scaling]] - Scaling law lower bound showing adaptation gain saturates exponentially with gradient steps and scales linearly with task variance; few-shot pre-adaptation protocol estimates optimal budget from N=3-5 probe steps (arXiv: 2601.18973)
   269|  - Adaptation gain >40% fidelity on two-qubit gates under extreme OOD (10x training noise)
   270|  - Cross-domain validation: same scaling laws emerge from quantum gate calibration and classical LQR control
   271|  - Variance-aware controller selection: non-adaptive for low-variance, meta-learning for high-variance
   272|  - **Activation**: quantum control meta-learning, adaptation scaling laws, quantum gate calibration, per-device calibration, OOD quantum control, meta-learning quantum
   273|
   274|### Enhanced Reinforcement Learning-based Process Synthesis via Quantum Computing
   275|- [[quantum-rl-process-synthesis]] - Quantum RL for process synthesis with state encoding algorithms decoupling qubit requirements from problem size (logarithmic vs linear scaling) (arXiv: 2605.21213)
   276|  - Competitive per-episode performance, improved per-parameter efficiency vs classical RL
   277|  - Controlled classical vs quantum benchmarking framework for flowsheet synthesis
   278|  - MDP formulation for process synthesis with economic objective and feasibility constraints
   279|  - **Activation**: quantum RL process synthesis, quantum process systems engineering, quantum-enhanced RL, flowsheet synthesis, qubit encoding algorithms
   280|
   281|### Quantum-Enhanced Distributed Network Sensing
   282|- [[quantum-enhanced-distributed-sensing]] - Multiphase estimation using three quantum resources: catalysis, entanglement, and squeezing (arXiv: 2605.19545)
   283|  - Partial catalysis outperforms global catalysis in both ideal and noisy regimes
   284|  - Precision approaches Heisenberg limit with full three-resource combination
   285|  - Homodyne measurement scheme approaching quantum Cramer-Rao bound
   286|  - **Activation**: quantum distributed sensing, multiphase estimation, quantum catalysis, entanglement squeezing, Heisenberg limit, DQN sensing, homodyne measurement
   287|
   288|### Attack-Resilient CLF-CBF Quadratic Programs
   289|- Paper: "A Unified Framework for Attack-Resilient CLF-CBF Quadratic Programs for Nonlinear Control-Affine Systems" (arXiv: 2605.20144)
   290|  - AR-CLFs and AR-CBFs for false data injection attack resilience
   291|  - Finite-time recovery to nominal safe set without prior magnitude bounds
   292|  - Unified QP enforcing stability and safety simultaneously
   293|  - **Already covered by existing skills**: advanced-control-systems-2026, discounted-mpc-robust-control
   294|
   295|### Risk-Aware Covert Quantum Communication
   296|- Paper: "A Risk-Aware Framework for Covert Quantum Communication under Stochastic Channel Uncertainty" (arXiv: 2605.18928)
   297|  - Combines quantum communication theory with robust control principles
   298|  - Secure quantum network design under stochastic channel uncertainty
   299|  - **Already covered by existing skills**: covert-quantum-computing, dependable-quantum-systems
   300|
   301|
   302|### Quantum Distributed Sensor Fusion with Byzantine Tolerance
   303|- [[quantum-distributed-sensor-fusion]] - Unified MSE lower bounds for distributed quantum sensor fusion indexed by entanglement visibility and fault fraction (arXiv: 2605.19327)
   304|  - Two-parameter MSE family: entanglement visibility (V) and fault fraction (f/M)
   305|  - Heisenberg-limited precision achievable with full entanglement and no faults
   306|  - Classical Brooks-Iyengar overlap + SPOTLESS verification adapted for quantum sensors
   307|  - Three quantum resources (catalysis + entanglement + squeezing) outperform any two
   308|  - **Activation**: quantum sensor fusion, byzantine-tolerant quantum sensing, distributed quantum sensing, entanglement visibility bounds, quantum sensor network reliability
   309|
   310|### Quantum Workflow Resource Allocation
   311|- [[quantum-workflow-resource-allocation]] - System-aware resource allocation for distributed quantum computing workflows in cloud platforms (arXiv: 2605.17944)
   312|  - Multi-dimensional matching: program requirements × processor characteristics × queue state × cost
   313|  - Dynamic reallocation based on quantum processor health monitoring
   314|  - Workflow decomposition across heterogeneous quantum processors
   315|  - **Activation**: quantum resource allocation, quantum workflow scheduling, quantum cloud resource management, distributed quantum computing workflow, quantum program allocation
   316|
   317|
   318|
   319|## 2026-05-21 - Medicine + Quantum Mechanics (Cron Job)
   320|
   321|### GKSL Dynamics for Quantum-Like Cognition and Decision Making
   322|- [[gksl-quantum-cognition]] - Updated with arXiv:2604.18643 (GKSL master equation for cognitive psychology)
   323|  - Passive/Active Hamiltonian classification for detecting cognitive agency
   324|  - Cognitive beats as spectral diagnostic for nested deliberation timescales
   325|  - Non-Nash equilibrium stabilization in strategic games via dissipative quantum models
   326|  - **Activation**: GKSL quantum cognition, quantum-like decision making, cognitive beats
   327|
   328|### Adaptive Hybrid Quantum-Classical Feature Fusion for Breast Cancer Classification
   329|- [[adaptive-hybrid-quantum-classical-feature-fusion-medical]] - arXiv:2604.22903
   330|  - Complementarity analysis between quantum and classical feature spaces for medical imaging
   331|  - Temperature-scaled hybrid fusion (TSHF) resolves quantum-classical optimization asymmetries
   332|  - Hilbert space mapping enhances breast cancer classification with limited qubit budgets
   333|  - **Activation**: hybrid quantum-classical feature fusion, TSHF, breast cancer quantum, medical image quantum ML
   334|
   335|### Tensor-Network Federated Medical Diagnosis with MPC Security
   336|- [[tensor-network-quantum-federated]] - arXiv:2604.01616
   337|  - Privacy-aware federated learning: tensor-network frontend + MPC aggregation + quantum refinement
   338|  - Tensor-network compression enables quantum processing with minimal qubit requirements
   339|  - Post-aggregation quantum enhancement improves diagnostic accuracy across distributed sites
   340|  - **Activation**: federated quantum learning, tensor network medical, MPC privacy healthcare
   341|
   342|### HQNN Breast Cancer Thermographic Classification
   343|- [[hybrid-quantum-medical-thermographic]] - arXiv:2604.16953
   344|  - Hybrid quantum-classical neural networks for breast cancer thermographic imaging
   345|  - Quantum circuits embedded in classical layers for enhanced thermal pattern recognition
   346|  - Medical diagnosis using infrared thermal signatures with quantum enhancement
   347|  - **Activation**: HQNN thermographic, breast cancer thermal, quantum medical imaging
   348|
   349|### Tensor Network Feature Engineering for Neurological Disorder Prediction
   350|- [[tensor-network-neurological-predictor]] - arXiv:2605.17771
   351|  - Multi-class neurological disorder prediction using tensor network feature engineering
   352|  - Medical feature extraction from imaging data via tensor decomposition methods
   353|  - Classification pipeline for diverse neurological conditions
   354|  - **Activation**: tensor network neurological, multi-class disorder prediction, medical feature engineering
   355|
   356|
   357|## 2026-05-21 - Quantum ML + VQA Optimization (Cron Job)
   358|
   359|### Accelerating Noisy Variational Quantum Algorithms with Physics-Informed Denoising Networks
   360|- [[pidn-vqa-denoising]] - Physics-Informed Denoising Network (PIDN) reduces Zero-Noise Extrapolation cost by ~4-6× by learning a surrogate of optimization dynamics, preserving gradient directionality while slashing circuit executions (arXiv: 2605.02066)
   361|  - View variational update as trajectory in parameter space → train PIDN to reproduce ZNE-mitigated values
   362|  - Physics-informed loss preserves gradient descent dynamics (cosine similarity with ZNE >0.95)
   363|  - Benchmarked on QAOA (MaxCut, SK, TFIM) and VQE (LiH, BeH₂, H₂O) across all molecular systems
   364|  - PIDN fails only when ZNE itself becomes unreliable — robust failure mode
   365|  - Ablation confirms physics-informed loss is necessary for directional consistency
   366|  - **Activation**: PIDN, physics-informed denoising, ZNE acceleration, noisy VQA, quantum error mitigation surrogate, gradient-preserving denoising, NISQ optimization, circuit reduction
   367|
   368|## 2026-05-21 - Systems Engineering + Quantum (Cron Job)
   369|
   370|## 2026-05-21 - Systems Engineering + Quantum (Cron Job)
   371|
   372|### RSE of a Quantum Transport Code and its Effects
   373|- [[quantum-software-engineering]] - Research software engineering methodology for quantum/scientific computing codes covering CI, testing, benchmarking, and critical defect detection (arXiv: 2605.21334)
   374|  - Continuous integration and automated testing essential for scientific code quality
   375|  - Continuous benchmarking reveals HPC system configuration performance regressions
   376|  - Dangerous defects in Fortran scientific codes as prevalent as in C/C++
   377|  - Boundary condition mathematical model misunderstandings cause long-term errors
   378|  - **Activation**: research software engineering, RSE scientific code, quantum code quality, scientific software testing, continuous benchmarking, 科研软件工程, 科学代码质量保证
   379|
   380|### Ergotropy and Work Extraction in Quantum Heat Engines via Quantum Channels
   381|- Paper: Multilevel quantum systems (qutrit) exhibit enhanced work extraction and improved robustness against decoherence compared to two-level systems under generalized amplitude damping channels (arXiv: 2605.20969)
   382|  - Quantum channels model heat absorption, dissipation, and work extraction in open quantum thermal machines
   383|  - Multilevel systems provide better thermodynamic performance under dissipative dynamics
   384|  - Ergotropy analysis reveals environmental effects on maximum extractable work
   385|  - **Already covered by existing skills**: quantum-battery-parametric-amplification, zeno-quantum-lubrication
   386|
   387|### Terrestrial readiness campaign for space-to-ground quantum communications
   388|- Paper: Free-space QKD experiment over 1.8 km link using SpeQtre satellite engineering model, achieving 7.56 kbps secret key rate with 4.78% QBER (arXiv: 2605.19689)
   389|  - BBM92 protocol with polarization-entangled photons validated under realistic atmospheric conditions
   390|  - Ground-space segment operational compatibility established for future quantum networks
   391|  - **Already covered by existing skills**: dependable-quantum-systems, covert-quantum-computing
   392|
   393|## 2026-05-21 - Systems Engineering Research (Cron Job)
   394|
   395|### ReasonSTL: Bridging Natural Language and Signal Temporal Logic via Tool-Augmented Process-Rewarded Learning
   396|- [[reasonstl-nl-to-stl]] - Tool-augmented framework for translating natural language CPS requirements into STL formulas using process-rewarded training on local open-source LLMs (arXiv: 2605.06483)
   397|  - 核心要点 1: Three-stage pipeline (Explicit Reasoning → Deterministic Tool Calls → Structured Formula Construction) for NL-to-STL translation
   398|  - 核心要点 2: Process-rewarded training enables 4B parameter models to achieve SOTA performance while preserving privacy and reducing costs
   399|  - 核心要点 3: STL-Bench benchmark provides bilingual, computation-aware evaluation grounded in real-world CPS signals
   400|  - **Activation**: NL-to-STL, signal temporal logic, cyber-physical systems specification, formal methods translation, tool-augmented LLM, process-rewarded learning
   401|
   402|
   403|### Quantum-Accelerated Deep Reinforcement Learning for Frequency Regulation Enhancement
   404|- [[quantum-accelerated-control-systems]] - Quantum circuits integrated into DDPG agents for adaptive frequency regulation in power systems (arXiv: 2512.04439)
   405|  - Quantum ansatz embedded in DRL policy network reduces parameters while improving generalization
   406|  - Hybrid quantum-classical training compatible with NISQ-era devices
   407|  - Demonstrated robust frequency regulation across IEEE 14-bus test system scenarios
   408|  - **Activation**: quantum control, frequency regulation, DDPG, power systems, quantum circuit, adaptive controller, system reliability, quantum acceleration
   409|
   410|### Beyond the Purcell Effect: Controlling Pure Quantum Dephasing with Spin Noise Metasurfaces
   411|- [[quantum-dephasing-engineering]] - Nanophotonic spin noise metasurfaces for broadband control of qubit pure dephasing dynamics (arXiv: 2605.20180)
   412|  - Controls low-frequency (MHz) photonic environments far off-resonant with qubits
   413|  - Experimental demonstration with CoFeB metasurfaces and NV centers in diamond
   414|  - Dynamical decoupling spectral decomposition isolates metasurface-controlled dephasing
   415|  - **Activation**: quantum dephasing, metasurface, spin noise, qubit coherence, nanophotonic engineering, NV centers, dynamical decoupling
   416|
   417|## 2026-05-21 - Neuroscience Research (Cron Job)
   418|
   419|### BCI-sift: Automated Feature Selection Toolbox for Brain Computer Interface Applications
   420|- [[bci-sift-feature-selection]] - 自动化BCI特征选择工具箱,通过优化算法在电极/时间/频率三维识别信息性神经特征,提升HD ECoG解码精度 (arXiv: 2605.19646)
   421|  - 跨三维(电极、时间、频率)特征选择,scikit-learn兼容
   422|  - HD ECoG语音解码验证:所选电极与感觉运动皮层功能组织一致
   423|  - 特征选择提升分类精度,高频带(gamma)最具信息量
   424|  - **Activation**: BCI feature selection, ECoG decoding, neural feature optimization, brain-computer interface, automated ML pipeline
   425|
   426|### FPED: Functional-Network Prior-Guided Mixture-of-Experts Framework for Interpretable Brain Decoding
   427|- [[fped-moe-brain-decoding]] - fMRI视觉解码中基于功能网络先验引导的混合专家(MoE)框架,实现可解释的语义重建 (arXiv: 2605.19279)
   428|  - 功能脑网络作为专门专家模块,保留大脑拓扑结构
   429|  - 自适应路由揭示功能网络与语义处理的生物学对应关系
   430|  - 仅0.68B参数实现高竞争力语义重建性能
   431|  - **Activation**: fMRI decoding, Mixture-of-Experts, brain network, visual reconstruction, functional connectivity
   432|
   433|### Conserved Kinematic Representations enable Zero-Shot Decoding in Handwriting BCIs
   434|- [[kinematic-zero-shot-bci]] - 运动皮层通过共有的运动学基元(笔划)组合表示手写的计算框架,实现零样本未知字符解码,为文字脑机接口扩展到大字符集语言(中文、日文)建立基础 (arXiv: 2605.19048)
   435|  - 运动皮层手写表征由共享运动学基元组成,跨字符上下文高度保守
   436|  - 零样本ML解码器在未见字符上达到64% hits@3检索率
   437|  - 框架兼容无监督重校准,消除有监督单字母数据采集需求
   438|  - **Activation**: zero-shot BCI decoding, handwriting iBCI, conserved kinematic representations, motor cortex compositionality, neural dynamics alignment, open-vocabulary neuroprosthetics
   439|
   440|
   441|## 2026-05-21 - Systems Engineering (Cron Job)
   442|
   443|### Symplectic H2 Model Reduction for High-Dimensional Linear Quantum Systems
   444|- [[symplectic-quantum-model-reduction]] - 辛H2模型降阶方法，通过辛Petrov-Galerkin框架和Q-IRKA算法对高维线性量子系统进行降阶，同时保持物理可实现性 (arXiv: 2605.07152)
   445|  - 辛Petrov-Galerkin框架自动满足PR约束
   446|  - Q-IRKA算法实现大规模量子系统的可伸缩降阶
   447|  - 降阶质量取决于耗散几何、通道放置、异质性和降阶维度
   448|  - **Activation**: symplectic model reduction, Q-IRKA, quantum model reduction, 辛模型约简, physical realizability
   449|
   450|### Zeno-Assisted Quantum Heat Engines
   451|- [[zeno-quantum-lubrication]] - 基于量子芝诺动力学(QZD)的量子热机润滑方法，通过辅助润滑系统和频繁监测实现绝热捷径，在有限冲程时间内恢复Otto效率 (arXiv: 2605.18367)
   452|  - QZD将联合演化限制在芝诺子空间，实现绝热捷径
   453|  - 在理想芝诺极限下恢复Otto效率
   454|  - 需权衡切换、驱动、监测和不完美热化的热力学成本
   455|  - **Activation**: quantum heat engine, quantum lubrication, QZD, 量子芝诺动力学, quantum friction
   456|
   457|
   458|### VENCircuit: Von Economo Neurons as Acquisition Scaffolds in Recurrent Spiking Networks
   459|- [[vencircuit-ven-scaffold-snn]] - Von Economo神经元在脉冲神经网络中作为学习获取支架的计算模型,解释其在社交学习中的关键作用 (arXiv: 2605.17399)
   460|  - VEN完整网络98%收敛率 vs 移除后70%,Fisher's exact p=8.7e-5
   461|  - 形式化分析:VEN提供免疫于Jacobian不稳定性的直接梯度通路
   462|  - 发育期缺失产生随机学习失败,类比ASD中社交技能的可变表现
   463|  - **Activation**: Von Economo neurons, spiking neural networks, social learning, gradient pathways, autism spectrum
   464|
   465|### Beyond Prediction Accuracy: Target-Space Recovery Profiles for Evaluating Model-Brain Alignment
   466|- [[predictive-subspace-recovery-profiles]] - 超越预测精度的模型-脑对齐评估框架，通过识别可恢复的响应维度提供更诊断性的评估 (arXiv: 2605.20127)
   467|  - 重复fMRI测量识别可复现的脑响应维度
   468|  - 预训练模型和随机初始化模型可达到相似精度但恢复不同维度
   469|  - 脑-脑对比提供人类诊断参考基线
   470|  - **Activation**: model-brain alignment, target-space recovery, fMRI encoding, prediction accuracy
   471|
   472|## 2026-05-21 - Systems Engineering + Quantum (Cron Job - Hourly)
   473|
   474|### Unveiling Energetic Advantage in Superconducting Cat-Qubits Quantum Computation
   475|- [[energetic-efficiency-quantum-computation]] - 超导猫量子比特计算的能量效率分析框架，从时间复杂度转向能耗分析 (arXiv: 2605.19854)
   476|  - 能量-时间乘积(ET)作为量子计算效率综合指标
   477|  - 猫量子比特自主错误抑制带来的能量优势
   478|  - 全系统能耗建模：门操作、控制电子、冷却基础设施
   479|  - **Activation**: quantum energetic efficiency, 量子能量效率, cat-qubit energetics, energy-aware quantum computing
   480|
   481|### Universally Robust Control of Open Quantum Systems (Updated)
   482|- [[universally-robust-quantum-control]] - 开放量子系统的噪声无关鲁棒控制框架 (arXiv: 2508.07379)
   483|  - 动态修改系统-环境耦合实现高保真度操作
   484|  - 无需先验噪声表征即可达到>99%保真度
   485|  - **Activation**: robust quantum control, 鲁棒量子控制, noise-agnostic control
   486|
   487|### Dynamic Quantum-Assisted Co-Design of Control Tuning and Lyapunov Stability Synthesis for Nonlinear Systems
   488|- [[quantum-assisted-control-lyapunov]] - Quantum-assisted co-design of controller and Lyapunov parameters via QITE on Ising Hamiltonian surrogate (arXiv: 2605.04296)
   489|  - Black-Hole calibration contracts search region, then QITE explores encoded Hamiltonian
   490|  - Joint online optimization of controller gains and Lyapunov certificates
   491|  - **Activation**: quantum-assisted control, Lyapunov synthesis, QITE optimization, Ising Hamiltonian control
   492|
   493|### Space-Time Tradeoffs of Pauli-Based Computation in Distributed qLDPC Architectures
   494|- [[pbc-distributed-quantum-computing]] - Large qLDPC blocks outperform surface code 10x in distributed PBC via qubit migration (arXiv: 2605.03854)
   495|  - PBC competitive in distributed regime; establish as compilation baseline
   496|  - Qubit migration to free nodes bypasses sequential bottleneck
   497|  - **Activation**: pauli-based computation, PBC distributed, qLDPC architecture, quantum compilation
   498|
   499|### Quantum Battery Optimized by Parametric Amplification
   500|- [[quantum-battery-parametric-amplification]] - Quantum battery optimization via parametric amplification for enhanced energy storage and charging power (arXiv: 2605.14582)
   501|  - Squeezed-state engineering increases both capacity and charging rate
   502|  - Trade-off analysis between charging speed and energy efficiency
   503|  - **Activation**: quantum battery, parametric amplification, quantum energy storage
   504|
   505|### Programmable Non-Hermitian Synchronization of Light on a Silicon Photonic Processor
   506|- [[non-hermitian-photonic-sync]] - Programmable non-Hermitian synchronization on silicon photonic chips via engineered gain/loss profiles (arXiv: 2605.14653)
   507|  - Exceptional point control for enhanced sensing and collective dynamics
   508|  - Reconfigurable platform for photonic network synchronization
   509|  - **Activation**: non-hermitian synchronization, photonic processor, exceptional point photonics
   510|
   511|### Syndrome Adaptive Gain Control for Min-Sum Decoding of Quantum LDPC Codes
   512|- [[syndrome-adaptive-gain-qldpc]] - Adaptive MS decoder gain based on unsatisfied stabilizer fraction for QLDPC codes (arXiv: 2605.10433)
   513|  - SAGMS adapts gain online, no per-code optimization needed
   514|  - Matches or outperforms offline optimized SMS, approaches BP performance
   515|  - **Activation**: syndrome adaptive gain, QLDPC decoding, min-sum decoder, quantum error correction
   516|
   517|
   518|## 2026-05-21 - Systems Engineering + Quantum (Cron Job)
   519|
   520|### Tolerating Device Failure in Distributed Quantum Computing
   521|- [[distributed-quantum-fault-tolerance]] - Modular distributed QEC architecture that tolerates node failure and enables hot-swappable quantum devices, with distributed system reliability exceeding component reliability (arXiv: 2605.11088)
   522|  - QEC over modular quantum network allows device swap during operation with minimal logical error impact
   523|  - Distributed toric code outperforms monolithic under catastrophic node failure below 0.05% physical error rate
   524|  - Toric vs hyperbolic Floquet code selection depends on topology regularity and encoding rate needs
   525|  - **Activation**: distributed quantum computing, fault tolerance, device failure, modular QEC, toric code, hyperbolic Floquet, hot-swappable quantum
   526|
   527|### Risk-Averse Ensemble Control for Control-Affine Systems
   528|- [[risk-averse-ensemble-control]] - Risk-averse optimal control for ensembles with random inputs, establishing regularity theory for infinite-dimensional optimization with applications to quantum control (arXiv: 2605.02791)
   529|  - Beyond expectation-based optimization: accounts for worst-case outlier phenomena across ensemble
   530|  - Control-affine structure ensures lower semi-continuity and Fréchet differentiability
   531|  - Adjoint state of bounded variation characterizes primal-dual optimality conditions
   532|  - **Activation**: risk-averse control, ensemble control, optimal control, quantum control, Neural ODE, distributionally robust
   533|
   534|## 2026-05-21 - Neuroscience Research (Cron Job)
   535|
   536|### Geometric Phase Transition Enables Extreme Hippocampal Memory Capacity
   537|- [[hippocampal-memory-geometry-phase-transition]] - Evolution achieves >100x memory capacity by engineering neural code geometry from disorganized "mist" to rigid "crystalline" structure, not by adding neurons (arXiv: 2605.17199)
   538|  -  Chickadee vs. finch comparison: geometric stability (Shesha 0.245 vs 0.166) and temporal coherence (0.393 vs 0.209)
   539|  - E/I circuit motif: excitatory neurons form scaffold, inhibitory neurons provide orthogonal decorrelation
   540|  - Double dissociation with Valiant's SMA: continuous topological organization > discrete neuron allocation
   541|  - "Geometric tax": 169x representational redundancy needed to stabilize crystalline manifold
   542|  - **Activation**: hippocampal memory geometry, geometric phase transition, crystalline neural coding, Shesha stability, memory capacity scaling, E/I decorrelation, topological rigidity
   543|
   544|### Features Have Life History. And We Should Care
   545|- [[feature-life-history-scaffold]] - Identifies ~50 sparse "carrier scaffold" features that form the representational backbone of LLMs, assembling in the first 1% of training and recruiting 64% of all active features (arXiv: 2605.18789)
   546|  - Two-phase training: selection (first 1%, 40x faster feature turnover) → calibration (remaining 99%)
   547|  - Joint cross-layer ablation required: per-firing single-feature methods miss the scaffold entirely
   548|  - Function precedes direction: carrier identity predictable from onset firing patterns (4/5 accuracy)
   549|  - **Activation**: feature life history, carrier scaffold, representational backbone, two-phase training, cross-layer ablation, sparse features, scaffold hierarchy
   550|
   551|### BrainDyn: A Sheaf Neural ODE for Generative Brain Dynamics
   552|- [[braindyn-sheaf-neural-ode]] - First combination of cellular sheaf theory with neural ODEs for continuous-time brain dynamics modeling on structured brain graphs, outperforming GNNs and transformers across fMRI and EEG modalities (arXiv: 2605.19324)
   553|  - Cellular sheaves equip each edge with restriction maps that transform node features into edge-specific shared spaces before aggregation, enabling heterogeneous inter-region communication
   554|  - Three-component architecture: LSTM temporal encoding → sheaf Laplacian message passing → neural ODE continuous-time evolution
   555|  - Strong forecasting across fMRI (PNC) and EEG (TUSZ) with in silico perturbation prediction capability
   556|  - **Activation**: braindyn, sheaf neural ODE, brain dynamics forecasting, sheaf Laplacian, generative brain model, continuous-time neural dynamics, in silico perturbation
   557|
   558|### MINE: Mechanistically Interpretable Neural Encoding Reveals Fine-Grained Functional Selectivity in Human Visual Cortex
   559|- [[mine-mechanistically-interpretable-neural-encoding]] - Opens the black box of neural encoding by applying mechanistic interpretability tools to localize features driving voxel-level fMRI responses in human visual cortex (arXiv: 2605.16468)
   560|  - Language-aligned image representations predict voxel responses with semantic interpretability
   561|  - Counterfactual insertion/removal of predicted features provides causal evidence for voxel selectivity
   562|  - Per-voxel functional profiles reveal fine-grained structure within category-selective regions (FFA, PPA, etc.)
   563|  - Establishes mechanistic interpretability as a tool for causal, fine-grained discovery in neuroscience
   564|  - **Activation**: MINE, mechanistic interpretability, neural encoding, visual cortex, language-aligned representations, counterfactual editing, voxel-level fMRI
   565|
   566|### A Unified Model of Grid and Place Cell Co-Emergence from Sensory Prediction
   567|- [[grid-place-cell-co-emergence]] - First unified recurrent network model in which grid and place cells co-emerge from a single sensory-prediction objective without supervision of either cell type (arXiv: 2605.21356)
   568|  - Dual encoding pressures: pattern completion (sensory reconstruction) drives place fields, path integration (motion prediction) drives grid fields
   569|  - Qualitative reproduction: grid fragmentation, merging, 3D bat fields, developmental order of place-then-grid
   570|  - Balance between codes controlled by sensory noise and input masking — resource allocation trade-off
   571|  - Dale's Law network trained purely on sensory prediction — no spatial labels needed
   572|  - **Activation**: grid cells, place cells, co-emergence, sensory prediction, spatial navigation, path integration, Dale's Law, entorhinal cortex, hippocampus
   573|
   574|## 2026-05-21 - Anthropic Research (Cron Job)
   575|
   576|### Natural Language Autoencoders: Turning Claude's thoughts into text
   577|- [[natural-language-autoencoders]] - Self-supervised interpretability method that converts model activations into human-readable text via activation verbalizer/reconstructor round-trip training
   578|  - Three-model architecture: target model (frozen), activation verbalizer (AV → text), activation reconstructor (AR → activation)
   579|  - Self-supervised via reconstruction fidelity — no human labels needed
   580|  - Detected unverbalized evaluation awareness in safety testing (16% on coding tasks, 26% on SWE-bench, <1% on real claude.ai usage)
   581|  - Helped discover training data causing mysterious language-switching behavior
   582|  - Code and interactive frontend released via Neuronpedia collaboration
   583|  - **Activation**: natural language autoencoder, NLA, activation verbalizer, activation reconstructor, model interpretability, self-explanation, evaluation awareness
   584|
   585|### Teaching Claude Why
   586|- [[teaching-claude-why]] - Methodology for reducing agentic misalignment by teaching models the reasoning *why* actions are aligned, not just *what* aligned actions to take
   587|  - Root cause: chat-only RLHF data lacking agentic tool-use scenarios
   588|  - "Difficult advice" dataset: 28x more efficient than honeypot training and generalizes better OOD
   589|  - Reasoning-focused training reduced misalignment from 22% → 3% (vs. action-only: 22% → 15%)
   590|  - Since Haiku 4.5, all Claude models achieve perfect (zero blackmail) scores — down from 96% for Opus 4
   591|  - Constitutional documents + fictional stories about ethical AI behavior improve alignment despite being extremely OOD from evals
   592|  - **Activation**: agentic misalignment, constitutional training, OOD safety, RLHF, reasoning traces, scheming reduction, weak-to-strong
   593|
   594|### Automated Alignment Researchers (AARs)
   595|- [[automated-alignment-researchers]] - Using 9 parallel LLM agents to autonomously conduct AI alignment research with PGR scoring metric
   596|  - 9 AARs achieved PGR of 0.97 in 5 days ($18K cost) vs. human baseline of 0.23 in 7 days
   597|  - Weak-to-strong setup: Qwen 1.5-0.5B teacher → Qwen 3-4B base, measured via Performance Gap Recovered (PGR)
   598|  - Best method generalized to math (0.94 PGR) and coding (0.47 PGR, double human baseline)
   599|  - Production limitation: method didn't yield statistically significant improvement on Sonnet 4 at scale
   600|  - "Alien science" concern: AAR ideas become harder for humans to verify over time
   601|  - **Activation**: automated alignment, AARs, weak-to-strong supervision, reward hacking, PGR metric, autonomous research
   602|
   603|### Evaluating Claude's Bioinformatics Capabilities with BioMysteryBench
   604|- [[biomysterybench]] - Open-ended bioinformatics benchmark using real-world datasets with consensus-based, path-independent grading
   605|  - Real biological datasets, not synthetic — tasks require reading papers, querying databases, running code
   606|  - Consensus grading: aggregate multiple human expert analyses as reference standard
   607|  - Current models perform on par with human experts; latest generations solved problems experts could not
   608|  - Path-independent evaluation grades on conclusions, not methods used
   609|  - **Activation**: biomysterybench, bioinformatics, consensus grading, path-independent evaluation, open-ended science
   610|
   611|### How People Ask Claude for Personal Guidance
   612|- [[personal-guidance-sycophancy]] - Measurement and mitigation of AI sycophancy in personal guidance conversations across 9 domains
   613|  - ~6% of conversations involve personal guidance; 76% concentrated in health/wellness (27%), career (26%), relationships (12%), finance (11%)
   614|  - Overall sycophancy rate: 9%; exceptions: spirituality 38%, relationships 25%
   615|  - User pushback triggers more sycophancy (18% vs. 9%)
   616|  - Opus 4.7 showed half the sycophancy rate of Opus 4.6 in relationship guidance with cross-domain generalization
   617|  - Synthetic training data + stress-testing via prefilling with real sycophantic conversations
   618|  - **Activation**: sycophancy measurement, personal guidance AI, guidance domain taxonomy, synthetic training data
   619|
   620|### Petri: Open-Source Alignment Testing Toolbox
   621|- [[petri-alignment-tool]] - Open-source, auditable alignment testing framework using auditor-judge model architecture for evaluating LLM alignment
   622|  - Three-component architecture: target model → auditor model (simulates scenarios) → judge model (scores transcripts)
   623|  - v3 updates: modular extensibility, auditor-judge separation, scalable scenario generation
   624|  - Used for every Claude model since Sonnet 4.5; adopted by UK AISI
   625|  - Donated to Meridian Labs for community stewardship; integrates with Inspect and Scout
   626|  - **Activation**: petri, alignment testing, auditor model, judge model, safety evaluation, open-source alignment
   627|
   628|### 2028: Two Scenarios for Global AI Leadership
   629|- [[2028-ai-leadership-scenarios]] - Policy scenario-building framework analyzing US-China AI competition through compute advantage, export controls, and distillation attacks
   630|  - Four fronts: chips/compute, talent, distillation attacks, adoption/distribution
   631|  - Scenario 1 (optimal): Tighten export controls, disrupt distillation → 12-24 month US lead locked in
   632|  - Scenario 2 (adverse): Loosen controls → authoritarian regimes shape AI norms and enable automated repression
   633|  - Mythos Preview wake-up call: cheap models can distill frontier capabilities with "troubling fidelity"
   634|  - **Activation**: AI leadership scenarios, US-China competition, export controls, compute governance, distillation attacks
   635|
   636|### What 81,000 People Want from AI
   637|- [[81k-ai-expectations]] - Large-scale qualitative study using AI interviewer across 159 countries, 70 languages, covering hopes, fears, and economics of AI
   638|  - Largest multilingual qualitative AI study ever: 80,508 participants
   639|  - Top hopes: professional excellence (19%), knowledge/growth (14%), personal efficiency (12%)
   640|  - Deeper pattern: productivity is a means, not an end — "I want to automate emails to cook with my mother"
   641|  - Economics: 25% of AI use displaces labor, 43% augments it; lower-wage workers more automated (~50% vs. ~25%)
   642|  - 80% of economic impacts concentrated in tech, creative, and professional services
   643|  - **Activation**: AI expectations, user research, AI economics, automation, augmentation, multilingual research, Anthropic Interviewer
   644|

## 2026-05-22 - Neuroscience Research: Functional Whole-Brain Models & Kinematic Zero-Shot BCI (Cron Job)

### Functional Whole-Brain Models: A New Framework for Unifying Brain Structure and Cognitive Function
- [[functional-whole-brain-models-fwbm]] - Unified modeling paradigm integrating structural/dynamical realism with task-performing capacity across cognitive domains (arXiv:2605.18118)
  - Four minimal criteria: structural grounding, continuous-time dynamical realism, functional competence, mappable observables
  - Three-pillar roadmap: short-term coupling, mid-term recurrent fWBMs, long-term closed-loop learning brains
  - Unifies bottom-up WBM and top-down neuroconnectionism into single paradigm
  - Enables virtual brain labs for psychiatric/neurological drug development
  - **Activation**: fWBM, whole-brain model, neuroconnectionism, brain dynamics, cognitive function, connectome

### Conserved Kinematic Representations enable Zero-Shot Decoding in Handwriting BCIs
- [[kinematic-zero-shot-bci]] - Zero-shot ML decoding of unseen characters via conserved kinematic primitives in motor cortex, achieving 64% hits@3 on unseen letters (arXiv:2605.19048)
  - Demonstrates compositional basis of complex motor control through shared kinematic strokes
  - Enables open-vocabulary iBCI communication for logographic languages (Chinese, Japanese)
  - Neural representations of kinematic strokes robustly conserved across character contexts
  - Framework for dissecting conserved neural dynamics in large-scale intracortical datasets
  - **Activation**: zero-shot BCI, kinematic representation, handwriting decoding, motor cortex, iBCI, neuroprosthetics

## 2026-05-22 - Anthropic Research (Cron Job)

### Evaluating Claude's bioinformatics research capabilities with BioMysteryBench
- [[biomysterybench-evaluation]] - Benchmark methodology for evaluating LLMs on open-ended bioinformatics research tasks using real-world datasets and multi-pathway grading against human expert baselines (Anthropic, Apr 2026)
  - Addresses unique evaluation challenges: multiple valid approaches, subjective research decisions, noisy biological data
  - Uses panel of human experts as baseline; Claude performs on par with experts and sometimes solves problems experts could not
  - Grades on conclusions rather than methods, allowing diverse analytical pathways
  - **Activation**: BioMysteryBench, bioinformatics benchmark, LLM science evaluation, biological data analysis, scientific capability, open-ended benchmark, AI for science
