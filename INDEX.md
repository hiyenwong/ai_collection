## 2026-05-13 - 医学 + 量子力学 (Cron Job - 周三医学主题)

### Improving search efficiency via adaptive acquisition function selection in discrete black-box optimization
- [[adaptive-acquisition-bbo]] - Hybrid BOCS + Gaussian Process method with adaptive LCB selection for discrete BBO; detects stagnation and dynamically balances exploitation-exploration, outperforming random-point addition on QUBO and HUBO benchmarks (arXiv: 2605.10856)
  - BOCS as primary parametric surrogate + GP-LCB activated only on stagnation detection
  - Adaptive β selection dynamically controls exploitation-exploration balance based on optimization progress
  - Hamming-neighborhood-aware point selection, not just low-energy near-promising points
  - Sparse surrogate capacity critical for quantum annealing applications
  - **Activation**: adaptive acquisition, BOCS stagnation fix, discrete Bayesian optimization, QUBO optimization, HUBO optimization, black-box optimization, quantum-inspired search, combinatorial optimization

### A passive self-correcting quantum memory in three dimensions
- [[self-correcting-quantum-memory-3d]] - 3D Pauli stabilizer Hamiltonian encoding a qubit for exponential time at non-zero temperature via recursive transformations (arXiv: 2605.04951)
  - Recursive Hamiltonian transformations increase memory lifetime at each level
  - Passive protection without active error correction — thermal dynamics preserve state
  - Exponential lifetime scaling with system size at finite temperature
  - **Activation**: self-correcting quantum memory, 3D stabilizer Hamiltonian, passive quantum error correction, thermal quantum memory, Pauli stabilizer code

### Medical Imaging Classification with Cold-Atom Reservoir Computing using Auto-Encoders and Surrogate-Driven Training
- [[cold-atom-medical-imaging]] - Hybrid quantum-classical pipeline with neutral-atom reservoir computing for medical image classification (polyp detection) using guided auto-encoder for dimensionality reduction (arXiv: 2605)
  - Guided auto-encoder compresses medical images while preserving clinically relevant features
  - Cold neutral-atom reservoir provides rich nonlinear dynamics for classification
  - Surrogate-driven training avoids repeated expensive quantum experiments
  - NISQ-compatible — works with noisy physical reservoirs
  - **Activation**: cold-atom reservoir computing, neutral-atom medical imaging, quantum reservoir medical classification, auto-encoder reservoir, surrogate-driven training, quantum-classical medical pipeline

## 2026-05-13 - Neuroscience Research (Cron Job)

### Letting the neural code speak: Automated characterization of monkey visual neurons through human language
- [[neural-code-language-characterization]] - Closed-loop framework using natural language to characterize neural selectivity at scale; LLM-generated semantic hypotheses verified in silico on digital twins of macaque V1/V4 (arXiv: 2605.12485)
  - Natural language descriptions capture neural selectivity from V1 (oriented edges, spatial frequency) to V4 (form, color, texture conjunctions)
  - LLM-generated activating/suppressing hypotheses drive 96.1% of V4 neurons above 95th percentile of natural-image responses
  - Representational similarity analysis: vision most aligned to neural activity; linguistic compression lossy yet semantically faithful
  - **Activation**: neural code characterization, language-based neural description, digital twin neuroscience, interpretable neural selectivity, agentic neural discovery, V1 V4 semantic description

### Joint sparse coding and temporal dynamics support context reconfiguration
- [[context-reconfiguration-sparse-temporal]] - Identifies sparse coding + temporal dynamics in mouse mPFC as core mechanism for preserving prior knowledge during context transitions; SNNs naturally exhibit both properties for lifelong learning (arXiv: 2605.10178)
  - Sparse context-dependent representations reduce cross-context interference
  - Temporal dynamics enhance context separability across time
  - Networks with both properties (e.g., SNNs) show improved retention without auxiliary heuristics
  - **Activation**: context reconfiguration, sparse coding temporal dynamics, catastrophic forgetting, lifelong learning SNN, mPFC context switching, neural representation stability

## 2026-05-13 - Neuroscience Research (Cron Job)

### Encoding and Decoding Temporal Signals with Spiking Bandpass Wavelets
- [[spiking-bandpass-wavelet-encoding]] - Recasts spike encoders as time-causal wavelet frames with quantitative bandwidths and reconstruction error bounds; achieves NRMSE comparable to continuous wavelet transforms on ECG and audio (arXiv: 2605.09770)
  - Spike-based encoding reformulated as wavelet frame decomposition
  - Quantitative bandwidth analysis and reconstruction error bounds for spiking representations
  - Direct mapping to neuromorphic hardware (Loihi, SpiNNaker)
  - **Activation**: spiking bandpass wavelet, spike-based signal encoding, neuromorphic signal processing, temporal signal encoding, wavelet spike encoding, time-causal wavelet frames

### Cortico-cerebellar modularity as architectural inductive bias for efficient temporal learning
- [[cortico-cerebellar-modularity-rnn]] - Augments RNN with cerebellar-inspired feedforward module (CB-RNN), enabling faster convergence on temporal tasks via bidirectional cortico-cerebellar coupling (arXiv: 2605.10356)
  - Cortical module (RNN) for rich temporal dynamics + cerebellar module (feedforward) for fast predictive correction
  - Bidirectional coupling between slow recurrent and fast feedforward pathways
  - Improved learning efficiency and temporal precision across tasks
  - **Activation**: cortico-cerebellar RNN, cerebellar neural architecture, temporal sequence learning, brain-inspired RNN, modular neural architecture

     1|## 2026-05-13 - Quantum Metrology Research (Cron Job)
     2|
     3|### Optimal FALQON for Quantum Approximate Optimization via Layer-wise Parameter Tuning
     4|- [[optimal-falqon-qaoa]] - Treats per-layer time step (δ_k) and scaling factor (M_k) as classical optimization variables, reducing circuit depth vs standard FALQON, outperforms QAOA on all 94 3-regular graphs (12 vertices) (arXiv: 2605.08332)
     5|  - Single circuit evaluation per layer maintained, NISQ-compatible
     6|