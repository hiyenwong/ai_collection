## 2026-05-19 - Neuroscience Research (Cron Job)

### Hippocampal-Entorhinal Inspired World Model
- [[hippocampal-entorhinal-world-model]] - Brain-inspired hierarchical world model for structure abstraction and generalization from video (arXiv: 2605.15733)
  - Simultaneously infers latent transitions and constructs predictive visual world model
  - HPC-MEC coupling dissociates relational structures (MEC) from integrated episodic scenes (HPC)
  - **Activation**: hippocampal-entorhinal model, world model, structure abstraction, HPC-MEC coupling

### Cortical Microcircuit Information Flux Optimization
- [[cortical-microcircuits-information-flux-optimization]] - Simulation-based reverse engineering of cortical microcircuit optimization for information flux (arXiv: 2605.14680)
  - Reverse engineering study of whether cortical microcircuits are optimized for information transmission
  - Simulation-based approach comparing natural vs. optimized circuit configurations
  - **Activation**: cortical microcircuit, information flux, reverse engineering, circuit optimization

### Implicit Behavioral Decoding from Spike Forecasts
- [[implicit-behavioral-decoding-spike-forecasts]] - Joint neural population forecasting and behavioral decoding from spiking activity (arXiv: 2605.12999)
  - Single model handles both spike forecasting and behavioral readout implicitly
  - Eliminates separate forecast → decode pipelines for closed-loop BCI systems
  - **Activation**: spike forecast behavioral, implicit behavioral decoding, closed-loop BCI

## 2026-05-19 - Deep Learning Research (Cron Job)
## 2026-05-19 - Neuroscience Research (Cron Job)

### Implicit Behavioral Decoding from Next-Step Spike Forecasts at Population Scale
- [[spike-forecast-behavioral]] - Joint neural population forecasting and behavioral decoding from spiking activity (arXiv: 2605.12999)
  - Single model handles both spike forecasting and behavioral readout implicitly
  - Eliminates separate forecast → decode pipelines for closed-loop BCI systems
  - **Activation**: spike forecast behavioral, implicit behavioral decoding, closed-loop BCI, population neural forecasting

### Mechanistic Interpretability of EEG Foundation Models via Sparse Autoencoders
- [[eeg-sae-interpretability]] - Extracting clinically interpretable features from EEG foundation model activations using SAE decomposition (arXiv: 2605.13930)
  - First application of SAE-based interpretability to EEG foundation models
  - Discovers human-interpretable features: sleep spindles, epileptiform patterns, frequency-band encodings
  - **Activation**: EEG foundation model interpretability, sparse autoencoder EEG, mechanistic interpretability, clinical EEG auditing

### STS: Efficient Sparse Attention with Speculative Token Sparsity
- [[speculative-sparse-attention-sts]] - Training-free sparse attention using draft model attention scores to construct dynamic token-and-head-wise sparsity masks for LLM inference, achieving 2.67x speedup at ~90% sparsity (arXiv: 2605.15508)
  - Cross-model attention correlation: small draft model predicts important tokens for large target model
  - Integrates with speculative decoding — no extra inference cost
  - Maintains accuracy at high sparsity levels unlike static pruning
  - **Activation**: speculative sparse attention, draft model sparsity, attention mask training-free, long context LLM inference

### DualKV: Shared-Prompt Flash Attention for Efficient RL Training
- [[dualkv-shared-prompt-flash-attention]] - FlashAttention kernel variant eliminating shared-prompt replication during GRPO/DAPO training, achieving 1.63-3.82x speedup and raising MFU from 36% to 76% (arXiv: 2605.15422)
  - Causal masking makes prompt representations invariant across N rollout sequences
  - Fused CUDA kernels process prompt once across all rollouts
  - Data pipeline repacks N(P+R) tokens into P+NR per micro-batch
  - **Activation**: dualkv, shared prompt flash attention, GRPO training speedup, RL kernel optimization

### Probabilistic Chunk Masking for Efficient VLA RL
- [[vla-probabilistic-chunk-masking]] - Drop-in GRPO modification using success-failure action variance to allocate gradient computation to informative trajectory chunks, achieving 2.38x speedup while backpropagating through <20% of chunks (arXiv: 2605.16154)
  - Success-failure action variance proxies per-phase gradient variance
  - No reward model or learned critic required
  - 60% lower peak activation memory
  - **Activation**: probabilistic chunk masking, efficient GRPO, VLA RL, gradient variance

### Self-evolving Agent Experience (DrugSAGE)
- [[self-evolving-agent-experience]] - Framework for LLM agents that accumulates cross-task memory of verified skills, statistical evidence, and error-fix patterns, enabling zero-test-time search on new tasks (arXiv: 2605.15461)
  - Memory components: verified skills, statistical evidence, error-fix records
  - Direct transfer of working solutions without search
  - Outperforms baselines by 10-30% in zero-search regime
  - **Activation**: self-evolving agent, cross-task memory, experience reuse, agent skill accumulation

### Compound LLM Agent Design in Adversarial POMDPs
- [[compound-llm-agent-design]] - Systematic study of 12 agent configurations revealing deliberation cascade pattern and that programmatic state abstraction delivers highest returns per token (arXiv: 2605.16205)
  - Deliberation cascade: distributing deliberation across hierarchy degrades performance up to 3.4x
  - Hierarchy without deliberation achieves best absolute performance
  - Context engineering more cost-effective than deliberation
  - **Activation**: compound agent design, deliberation cascade, hierarchical agents, RPTS, adversarial POMDP

### Stepwise Reasoning with External Subgraph Generation
- [[stepwise-reasoning-subgraph]] - Stepwise reasoning framework building query-specific subgraphs from external KBs to ground intermediate reasoning steps, improving LLM accuracy and factual reliability (arXiv: 2605.16117)
  - Three-stage: subgraph construction → progressive reasoning → trajectory combination
  - Reduces hallucination by grounding in structured knowledge
  - **Activation**: stepwise reasoning, subgraph generation, knowledge grounding, external KB reasoning

### Federated Learning of SNNs under Heterogeneous Temporal Resolutions
- [[federated-snn-heterogeneous-temporal]] - Federated learning framework for SNNs addressing temporal resolution mismatch across edge devices, enabling local-resolution training with global model compatibility (arXiv: 2605.15355)
  - Naive FedAvg fails when clients have different sampling rates
  - Adaptation methods recover accuracy lost to temporal mismatch
  - Applies to SNNs and broader class of stateful-neuron networks
  - **Activation**: federated SNN, temporal resolution mismatch, heterogeneous edge FL

### RecMem: Recurrence-based Memory Consolidation for LLM Agents
- [[recurrence-memory-consolidation]] - Memory consolidation storing interactions in subconscious layer, only invoking LLM when sustained recurrence detected, reducing token cost by up to 87% while exceeding accuracy (arXiv: 2605.16045)
  - Lightweight embedding for subconscious storage, LLM only for recurring patterns
  - Semantic refinement recovers fine-grained facts omitted by compression
  - Drop-in replacement for consolidation step in existing memory systems
  - **Activation**: recmem, recurrence memory consolidation, lazy memory, agent memory efficiency

### Cortical Microcircuit Information Flux Optimization
- [[cortical-microcircuits-information-flux-optimization]] - Simulation-based reverse engineering of whether cortical microcircuits are optimized for information flux (arXiv: 2605.14680)
  - Investigates if biological cortical circuits operate near information transmission optima
  - Uses mutual information between successive network states as optimization objective
  - **Activation**: cortical microcircuit optimization, information flux neural networks, reverse engineering brain circuits
## 2026-05-18 - Neuroscience + Quantum Mechanics (Cron Job - 23:00)

### Diagonal Adaptive Non-local Observables on Quantum Neural Networks
- [[diagonal-ano-quantum-observables]] - Diagonal adaptive non-local observables for VQAs: reduces O(n²) to O(n) parameters while retaining full expressivity via canonical diagonal representation (arXiv: 2605.15410)
  - Diagonal observables are canonical representatives of ANO space modulo unitary similarity
  - Equivalent expressivity to full Hermitian ANO with far fewer parameters
  - Faster convergence and easier classical optimization
  - Hardware-friendly: diagonal measurements native on most platforms
  - **Activation**: diagonal ANO, adaptive non-local observables, VQA parameter efficiency, quantum measurement design, observable adaptivity

### Extreme Quantum Cognition Machines
- [[extreme-quantum-cognition]] - Quantum learning architecture for deliberative decision making with dynamical attention, noise-tolerant to contradictory data (arXiv: 2603.05430)
  - Fixed quantum dynamics as nonlinear feature map, learning only in linear readout
  - Input-dependent Hamiltonian attention modulates quantum evolution
  - No barren plateaus, inherent noise regularization
  - **Activation**: extreme quantum cognition, EQCM, quantum reservoir computing, quantum extreme learning, dynamical attention quantum

### Deep Boltzmann Quantum States for Spin Glasses
- [[deep-boltzmann-quantum-states]] - Neural quantum states + Boltzmann machine for frustrated quantum many-body systems (arXiv: 2605.15899)
  - Captures complex entanglement in classical/quantum spin glasses
  - Boltzmann architecture naturally models competing interactions and frustration
  - Unified framework for classical and quantum disordered systems
  - **Activation**: deep boltzmann quantum states, spin glass quantum, frustrated many-body, neural quantum states, variational monte carlo

## 2026-05-18 - Neuroscience Research (Cron Job - 23:00)

### Scalable neuromorphic computing from autonomous spiking dynamics in a clockless reconfigurable chip
- [[clockless-neuromorphic-snn]] - Clockless asynchronous Boolean spiking neural networks on FPGA achieving nanosecond-scale spike dynamics with 100x energy efficiency over clocked implementations (arXiv: 2605.16114)
  - Boolean spiking neurons with configurable excitatory/inhibitory weights and propagation delays
  - Quasi-analog dynamics emerge from autonomous time-continuous evolution of digital logic (no global clock)
  - 84.5% accuracy on SHD audio classification, competitive with analog neuromorphic state-of-the-art
  - 2 orders of magnitude lower power than digital FPGA SNN implementations
  - **Activation**: clockless neuromorphic, boolean spiking neuron, async spiking network, liquid state machine FPGA, energy-efficient SNN hardware

### Structure Abstraction and Generalization in a Hippocampal-Entorhinal Inspired World Model
- [[hpc-mec-world-model]] - Brain-inspired hierarchical world model using HPC-MEC coupling for structure abstraction and zero-shot generalization from real-world video (arXiv: 2605.15733)
  - MEC encodes abstract relational structures via CANN; HPC binds content-specific episodic information
  - Inverse model learns latent transitions from observation-only videos (no action labels needed)
  - Demonstrates zero-shot transfer: extract transitions from human videos, apply to novel objects/scenes
  - 84 FPS inference on A100; trained on SSv2 (220K videos), evaluated on OmniObject3D and robotics benchmarks
  - **Activation**: hpc-mec world model, hippocampal entorhinal model, structure abstraction, cognitive map AI, grid cell model, latent transition reuse

     1|## 2026-05-18 - Polariton BEC Quantum Neuromorphic (Cron Job - 22:01)
     2|
     3|### Polariton BECs: Theory and Concepts
     4|- [[polariton-bec-quantum-neuromorphic]] - Polariton Bose-Einstein condensate theory for room-temperature quantum neuromorphic computing, driven-dissipative dynamics, and optical neural networks (arXiv: 2605.16256)
     5|  - Polaritons are WISI (Weakly-Interacting, Strongly-Interfering) particles combining light interference with exciton interactions
     6|