## 2026-05-13 - 医学 + 量子力学 (Cron Job - 周三医学主题)

### Quantum Circuit Simulation of Compartmental Drug Dynamics: Leveraging Variational Algorithms for Nonlinear Mixed-Effects Population Pharmacokinetics
- [[quantum-pkpd-simulation]] - Reformulates compartmental PK/PD models as open quantum systems using PennyLane quantum circuits for population pharmacokinetics parameter estimation (arXiv: 2605.09691)
  - Classical ODE-based PK/PD models encoded as quantum circuit evolution
  - Variational quantum algorithms for nonlinear mixed-effects population model fitting
  - Potential exponential speedup for multi-compartment drug dynamics simulation
  - Population-level predictions via quantum expectation values
  - **Activation**: quantum PK/PD, quantum pharmacokinetics, drug dynamics simulation, compartmental quantum model, quantum circuit drug simulation, variational quantum healthcare

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

## 2026-05-13 - Neuroscience Research (Cron Job - Batch 3)

### Multi-Timescale Conductance Spiking Networks: A Sparse, Gradient-Trainable Framework with Rich Firing Dynamics for Enhanced Temporal Processing
- [[multi-timescale-conductance-snn]] - SNN framework using fast/slow/ultra-slow conductances to shape I-V curve, enabling direct BPTT (no surrogate gradients) with rich firing regimes and high sparsity (arXiv: 2605.11835)
  - Multi-timescale conductance parametrization replaces phenomenological LIF dynamics
  - Direct backpropagation through time without surrogate gradient approximation
  - Single model exhibits tonic, phasic, and bursting firing regimes
  - Outperforms LIF and AdLIF on Mackey-Glass regression with substantially sparser activity
  - **Activation**: multi-timescale spiking, conductance SNN, gradient-trainable SNN, I-V curve shaping, temporal processing SNN, direct BPTT SNN

### Probabilistic Prediction of Neural Dynamics via Autoregressive Flow Matching
- [[autoregressive-flow-matching-neural-dynamics]] - Generative forecasting framework using autoregressive flow matching for probabilistic neural dynamics prediction from multimodal sensory input and past neural history (arXiv: 2604.11178)
  - Flow matching learns conditional distribution of future neural states given past dynamics
  - Autoregressive factorization captures temporal dependencies between predictions
  - Past neural history is the dominant predictor — more than sensory input alone
  - Significantly outperforms GLM and non-autoregressive baselines on fMRI data
  - **Activation**: neural dynamics prediction, autoregressive flow matching, fMRI forecasting, probabilistic neural prediction, closed-loop neurotechnology, transport-based generative modeling

     1|## 2026-05-13 - Quantum Metrology Research (Cron Job)
     2|
     3|### Optimal FALQON for Quantum Approximate Optimization via Layer-wise Parameter Tuning
     4|- [[optimal-falqon-qaoa]] - Treats per-layer time step (δ_k) and scaling factor (M_k) as classical optimization variables, reducing circuit depth vs standard FALQON, outperforms QAOA on all 94 3-regular graphs (12 vertices) (arXiv: 2605.08332)
     5|  - Single circuit evaluation per layer maintained, NISQ-compatible
     6|