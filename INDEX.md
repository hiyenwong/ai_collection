## 2026-05-13 - Neuroscience Research (Cron Job)

### Spatiotemporal TDANN for MT Direction Maps
- [[mt-direction-maps-spatiotemporal]] - 3D ResNet with MoCo self-supervised learning + spatial loss produces brain-like direction-selective maps and pinwheel structures matching macaque MT physiology (arXiv: 2605.11718)
  - Extends TDANN to dorsal stream: 3D ResNet trained on naturalistic videos via contrastive learning
  - MT tuning emerges from strict trade-off between discriminative pressure and spatial regularization
  - Quantitative match to in vivo macaque MT: direction selectivity index, circular variance, pinwheel density
  - Unifies ventral and dorsal stream topographic origins under single computational mechanism
  - **Activation**: MT direction maps, spatiotemporal TDANN, dorsal stream self-organization, motion direction selectivity, cortical topography, MoCo visual neuroscience

### Attractor Models for Language and Reasoning
- [[attractor-models-language-reasoning]] - Fixed-point attractor architecture with implicit differentiation for scalable iterative refinement; 770M outperforms 1.3B Transformer on 2× tokens, 27M achieves 91.4% Sudoku-Extreme (arXiv: 2605.12466)
  - Two-stage: backbone proposes embeddings, attractor refines via fixed-point solving
  - Constant memory for effective depth; iterations chosen adaptively by convergence
  - Equilibrium internalization: fixed-point training enables solver removal at inference
  - Outperforms Claude and GPT-o3 on challenging reasoning tasks with tiny model
  - **Activation**: attractor models, fixed-point reasoning, implicit differentiation, looped Transformer, iterative refinement, equilibrium internalization

### EEG Microstate Discovery via Variational Deep Embedding
- [[eeg-microstate-variational-embedding]] - Variational deep embedding replaces k-means microstate clustering with uncertainty-aware latent space learning for interpretable EEG analysis (arXiv: 2605.10947)
  - Deep VAE learns continuous temporal representation of EEG segments
  - Systematic architecture search identifies optimal configuration
  - Multi-quadrant evaluation: interpretability, stability, accuracy, scalability
  - Principled uncertainty quantification via variational posterior
  - **Activation**: EEG microstate discovery, variational EEG embedding, microstate clustering, interpretable EEG analysis, deep EEG pipeline

## 2026-05-13 - 医学 + 量子力学 (Cron Job - 周三医学主题)

### Hybrid Quantum Neural Networks for Enhanced Breast Cancer Thermographic Classification
- [[hybrid-quantum-medical-imaging]] - Integrates quantum variational circuits with classical CNN backbones for thermographic breast cancer classification, leveraging quantum advantage in complex thermal pattern discrimination (arXiv: 2604.16953)
  - Hybrid architecture: Classical CNN encoder → Quantum variational layer → Classical classifier
  - Amplitude encoding of CNN features into quantum states for enhanced discrimination
  - Quanvolutional filters as alternatives to convolutional layers for medical image patches
  - Joint classical-quantum optimization using parameter-shift rule for gradient computation
  - **Activation**: hybrid quantum neural network, quantum medical imaging, thermographic cancer detection, quanvolutional network, quantum healthcare AI, breast cancer quantum classification

## 2026-05-14 - 医学 + 量子力学 (Cron Job - 周三医学主题)

### FQPDR: Federated Quantum Neural Network for Privacy-preserving Early Detection of Diabetic Retinopathy
- [[fqpdr-quantum-medical-diagnosis]] - Federated Quantum Neural Network for distributed medical diagnosis across hospitals without sharing patient data; trains local QNNs and aggregates via FedAvg (arXiv: 2605.08324)
  - Multi-hospital federated QNN architecture with parameterized quantum circuits
  - Classical medical features encoded into quantum states via angle embedding
  - Privacy-preserving: patient data never leaves originating institution
  - Applicable to rare disease detection requiring pooled sparse data
  - **Activation**: federated quantum, quantum medical diagnosis, FQN, privacy-preserving medical AI, diabetic retinopathy quantum, distributed quantum healthcare

## 2026-05-14 - Quantum Computing Research (Cron Job)

### Pre-Asymptotic Trainability in Photonic Variational Circuits under Postselection
- [[photonic-variational-trainability]] - Challenges barren plateau assumption in passive photonic circuits; postselection prevents strong mixing dynamics that cause gradient vanishing (arXiv: 2605.11879)
  - Linear optical quantum computing shows trainability despite deep circuits
  - Postselection maintains gradient variance at usable levels
  - Implications for photonic VQA optimization and NISQ-era training

## 2026-05-13 - 医学 + 量子力学 (Cron Job - 周三医学主题)

### Quantum Entanglement Degree as Novel PET Biomarkers for Hypoxia
- [[quantum-pet-biomarkers]] - Novel quantum sensing method using positronium photon entanglement degree, lifetime, and annihilation ratios to non-invasively assess tissue oxygen concentration (arXiv: 2605.00021)
  - Two approaches: (1) dual-parameter τ_oPs + R_oPs-3γ/2γ measurement, (2) entanglement degree sensitivity to pick-off vs self-annihilation
  - Derived formula linking pO₂ to quantum entanglement metrics
  - Quantitative C_QE predictions across tissue types (adipose: 0.890, water: 0.867)
  - **Activation**: quantum PET biomarkers, positronium hypoxia sensing, quantum entanglement PET, positronium lifetime oxygen, pick-off conversion annihilation

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