# AI Collection Index

## 2026-06-06 - Economics, Investment + Quantum Finance (Cron Job)

### Efficient Complex-Valued State Preparation on Bucket Brigade QRAM
- [[bbqram-state-preparation-finance]] - Architecture-aware quantum state preparation using BBQRAM + segment tree for O(log²(MN)) query time, eliminating QPU arithmetic via classical precomputation (arXiv: 2604.25644)
  - 核心要点 1: Classical precomputation of rotation angles removes U_2CR reversible arithmetic from QPU
  - 核心要点 2: Complex-valued extension via two-step magnitude-then-phase procedure with leaf phase storage
  - **Activation**: BBQRAM state preparation, bucket brigade QRAM, complex-valued quantum encoding, quantum finance data loading, classical precomputation rotation angles, magnitude-then-phase

## 2026-06-06 - Neuroscience Research (Cron Job)

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
  - **Activation**: dealer market, competition, internalisation, externalisation, Nash equilibrium, inventory risk, market microstructure, quoting strategy

### ESG & Joint Fragility in Equity Markets
- [[esg-joint-fragility-equity-markets]] - Framework analyzing ESG association with clustered fragility (simultaneous downside + vol spike + illiquidity). Higher ESG → lower cofragility exposure (arXiv: 2606.05631)
  - Three fragility dimensions: downside returns, volatility spikes, illiquidity
  - Cofragility state: multiple dimensions occurring simultaneously
  - Panel regression with firm and time fixed effects
  - Environmental pillar most strongly reduces fragility
  - Effect persists after controlling for traditional risk factors
  - **Activation**: ESG, joint fragility, cofragility, equity markets, downside risk, volatility spike, illiquidity, portfolio resilience, S&P 500

### Long-Range Dependence in Financial Markets
- [[long-range-dependence-financial-markets]] - Empirical study of LRD across equity, commodity, energy sectors. Most deep generative models fail to reproduce LRD; diffusion models perform best (arXiv: 2509.19663)
  - Three LRD detection methods: R/S analysis, DFA, wavelet estimation
  - Equity: H ≈ 0.55-0.65 (persistent); commodities show stronger LRD
  - Energy markets exhibit regime-dependent LRD
  - GANs, VAEs fail to reproduce LRD; diffusion models best
  - Synthetic data is too "short-memory" without LRD constraints
  - **Activation**: long-range dependence, Hurst exponent, financial time series, R/S analysis, DFA, wavelet analysis, generative models, market memory, synthetic data

## 2026-06-06 - Neuroscience Research (Cron Job)

### TRIBE v2: Tri-modal Foundation Model for Brain Decoding
- [[tribev2-brain-foundation-model]] - Large encoding model pretrained on 1000+ hours of fMRI responses to video/audio/language. Synthetic data augmentation for boosting brain-to-image decoding in low-data regimes (arXiv: 2606.06345v1)
  - Addresses fundamental limitation: availability of labeled neural data
  - Grid-based evaluation: augmentation effectiveness varies with synthetic ratio, quality threshold, domain mismatch
  - Key finding: 20-40% accuracy boost for small datasets (< 50 subjects), optimal 30-50% synthetic ratio
  - Quality filtering critical: > 0.80 confidence threshold for synthetic samples
  - **Activation**: brain decoding, fMRI, TRIBE, foundation model, data augmentation, brain-to-image, encoding model, synthetic fMRI, low-data regime

### ITP-STDP: Power-of-Two Learning Engine for On-Chip SNN Training
- [[itp-stdp-snn-training]] - Hardware-efficient STDP algorithm using power-of-two weight encoding and intrinsic timing. 50x resource reduction, 100x energy reduction for on-chip SNN training (arXiv: 2606.06159v1)
  - Power-of-two weights: multiplication → bit shift (multipliers eliminated)
  - Intrinsic timing: local neuron dynamics replace global timing circuits
  - LUT-based STDP: exponential computation → lookup table
  - Hardware efficiency: 50x area reduction, 100x energy reduction per update
  - Trade-off: ~1.3% accuracy drop for massive hardware efficiency gain
  - **Activation**: SNN training, STDP, on-chip learning, neuromorphic hardware, FPGA, ASIC, power-of-two, intrinsic timing, synaptic plasticity

## 2026-06-06 - Economics/Investment + Quantum Finance (Cron Job)

### Quantum Computing for Financial Transformation: A Comprehensive Review
- [[quantum-finance-stack-analysis]] - Financial computation stack framework evaluating quantum advantage across five domains: portfolio optimization, derivative pricing, tail-risk estimation, QML, and post-quantum security (arXiv: 2604.08180)
  - Five-domain stack: constrained portfolio optimization, derivative pricing, tail-risk estimation, QML, post-quantum security
  - Evaluation logic: identify bottleneck → specify quantum primitive → compare classical benchmark → assess realistic constraints
  - Key conclusion: hybrid workflows strongest near-term case; quantum optimization credible when constrained search dominates
  - Amplitude estimation matters most when repeated expectation evaluation is the binding cost
  - Post-quantum cryptography strategically necessary — financial infrastructures must migrate before fault-tolerant attacks arrive
  - 134 pages, handbook-style entry point combining system-level synthesis with reproducible case studies
  - **Activation**: quantum finance stack, quantum portfolio optimization, derivative pricing, amplitude estimation, post-quantum security, hybrid quantum finance, QML finance, financial computation stack

### Hot-Starting Quantum Portfolio Optimization
- [[hotstart-quantum-portfolio-optimization]] - Novel approach restricting quantum portfolio search to discrete solutions near continuous optimum via compact Hilbert space construction, reducing qubit count (arXiv: 2510.11153)
  - Hot-starting from relaxed continuous solution outperforms SOTA on D-Wave Advantage quantum annealer
  - Compact Hilbert space around continuous optimum reduces qubit requirements
  - Smooth convex objective function + integer trading constraints = natural discrete mean-variance problem
  - **Activation**: hot-start quantum optimization, portfolio optimization, quantum annealing, compact Hilbert space, D-Wave, QUBO, mean-variance portfolio, continuous relaxation

## 2026-06-06 - Neuroscience Research (Cron Job)

### Brain-CLIPLM: Semantic Compression for EEG-to-Text Decoding
- [[brain-cliplm-semantic-compression-eeg]] - Two-stage EEG decoding framework: semantic anchor recovery via contrastive learning + retrieval-grounded LLM reconstruction. Granularity matching principle aligns decoding complexity with neural information scale (arXiv: 2604.16370)
  - Semantic compression hypothesis: EEG preserves recoverable semantic anchors, not full sentences
  - Stage 1: Contrastive alignment extracts ordered keyword-level evidence
  - Stage 2: Anchor-guided sentence reconstruction with chain-of-thought reasoning
  - ZuCo benchmark: Top-5 retrieval 67.6%, Top-25 85.0%, intermediate granularity optimal
  - **Activation**: EEG decoding, semantic compression, anchor recovery, granularity matching, CLIP alignment, retrieval-grounded LLM, brain-to-text, ZuCo benchmark

### Vision Hopfield Memory Networks: Brain-Inspired Backbone
- [[vision-hopfield-memory-networks]] - Hierarchical Hopfield associative memory + predictive-coding refinement replaces Transformer/Mamba. Local patch memory + global episodic memory + error correction. Enhanced interpretability, data efficiency, biological plausibility (arXiv: 2603.25157)
  - Memory retrieval exposes input-to-pattern relationships for transparent decisions
  - Three-layer architecture: Local Hopfield (V1 analogy), Global Hopfield (V2-V4 analogy), Predictive Coding
  - Pattern reuse reduces training data needs, improves efficiency
  - Biological justification: mirrors visual hierarchy and cortical feedback loops
  - **Activation**: Hopfield memory, associative memory, predictive coding, interpretability, biological plausibility, vision backbone, hierarchical memory

## 2026-06-06 - Neuroscience Research (Cron Job)

### Updating the Standard Neuron Model in Artificial Neural Networks
- [[updated-neuron-model-ann]] - Breakthrough paper replacing 70-year-old point neuron model with realistic cortical cell model, achieving higher expressivity, robustness, learning speed with same parameters (arXiv: 2605.30370)
  - Neuroscience critique: point neuron too simplistic for fundamental neural processes since 1950s
  - Realistic cortical cell model substitution without parameter increase
  - Demonstrated advantages: expressivity boost, robustness enhancement, faster learning, reduced memorization, less training data needed
  - **Activation**: neuron model, artificial neural network, cortical cells, point neuron, expressivity, robustness, learning speed, realistic neuron, ANN architecture

### Learning Sequence Timing and Control of Replay Speed in Spiking Neural Networks
- [[snn-sequence-timing-replay]] - Biologically plausible spiking mechanism for temporal memory replay with variable speed control (arXiv: 2605.22523)
  - STDP-based sequence timing learning without external timing signals
  - Novel replay speed control: faster/slower than training speed, maintains temporal proportions
  - Compatible with hippocampal replay observations (compression/expansion during sleep)
  - **Activation**: spiking neural network, sequence timing, memory replay, replay speed, STDP, temporal memory, synaptic plasticity, neural replay, hippocampal replay

## 2026-06-06 - Economics, Investment + Quantum Mechanics (Cron Job)

### Contextual Quantum Neural Networks for Stock Price Prediction
- [[contextual-quantum-neural-stock-prediction]] - Quantum multi-task learning architecture with share-and-specify ansatz for simultaneous multi-asset stock price prediction using logarithmic qubit overhead (arXiv: 2503.01884)
  - Quantum Batch Gradient Update (QBGU) accelerates SGD using quantum superposition for simultaneous gradient processing
  - QMTL share-and-specify ansatz enables shared feature extraction + asset-specific operators on same circuit
  - Entanglement in shared layers naturally encodes inter-asset correlations
  - O(log₂N) qubit scaling for N-asset portfolio representation
  - **Activation**: quantum neural network, stock prediction, multi-task learning, QBGU, quantum batch gradient, QMTL, share-and-specify ansatz, quantum portfolio, multi-asset prediction, inter-asset correlation, quantum superposition gradient, amplitude encoding

## 2026-06-06 - Neuroscience Research (Cron Job)

### Ontology-Constrained Multi-LLM Scoring of Hypothesis Support in Predictive Processing
- [[ontology-constrained-llm-hypothesis-scoring]] - Local multi-LLM council for ontology-constrained literature synthesis in predictive coding neuroscience, producing quantitative hypothesis-space maps with auditable disagreement measurements (arXiv: 2606.05206)
  - 36-concept expert glossary across 3 hypotheses: Predictive Suppression, Feedforward Error Propagation, Ubiquity
  - 10 local LLM models score 31 studies independently, pairwise agreement analysis reveals structured disagreement
  - Hypothesis-space temperature: geometric dispersion metric (lower for local oddball, higher for global oddball)
  - Transition vectors quantify paradigm-dependent shifts between experimental contexts
  - **Activation**: predictive processing, predictive coding, ontology-constrained, multi-LLM, hypothesis scoring, literature synthesis, meta-analysis, evidence space, hypothesis-space mapping, local oddball, global oddball, LLM council, glossary validation, temperature metric

## 2026-06-06 - Economics, Investment + Quantum (Cron Job)

### The Inverse Born Rule Fallacy: On the Informational Limits of Phase-Locked Amplitude Encoding
- [[inverse-born-rule-fallacy]] - 识别振幅编码缺陷，提出动态哈密顿编码(DHE)实现非对易量子演化 (arXiv: 2602.21350)
  - 朴素振幅编码(psi=sqrt(P))使Hilbert空间阿贝尔化