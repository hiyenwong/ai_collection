## 2026-08-05 - Neuroscience Research (Cron Job)

### Persistent homology broadens the controllable subspace in human structural connectomes
- [[persistent-homology-brain-network-control]] - Methodology for applying persistent homology to brain network control theory, revealing that topological driver node selection provides geometric advantages over traditional degree-based approaches while maintaining similar control energy costs (arXiv: 2608.03181)
  - Dissociation between control cost and control geometry: topology-informed sets distribute controllability across more state space dimensions
  - Better-conditioned controllability matrices with robustness preserved even when high-degree hub nodes are removed
  - Functional signature: different cortical territories targeted, shaping which brain-state transitions are energetically favored
  - **Activation**: persistent homology, brain network control, structural connectome, controllability, topology, driver nodes

### AS-FedBridge: Pseudo-Spike Bridge Distillation for Heterogeneous ANN-SNN Federated Learning
- [[as-fedbridge-ann-snn-federated-learning]] - Framework for mixed ANN-SNN federated learning that addresses representational misalignment through a lightweight Bridge with Pseudo-Spike Interface, enabling effective collaboration between continuous-valued ANNs and discrete spiking SNNs while preserving data privacy (arXiv: 2608.03324)
  - Lightweight Bridge with Pseudo-Spike Interface projects continuous signals into spike-compatible space
  - Positive correlation between ANN-SNN alignment degree and collaborative FL performance across four datasets
  - Highly controllable trade-off between model performance and resource efficiency with marginal computational overhead
  - **Activation**: AS-FedBridge, ANN-SNN federated learning, pseudo-spike interface, representational alignment, heterogeneous federated learning

## 2026-08-06 - Neuroscience Research (Cron Job)

### A Landau-Ginzburg Phenomenology of Sleep-Stage Transitions
- [[landau-ginzburg-sleep-stage-transitions]] - Methodology for modeling sleep-stage transitions using Landau-Ginzburg phenomenology with spatially extended neural fields, treating different sleep boundaries as distinct phase transitions (fold, crossover, first-order-like switch) while providing spatial predictions absent from scalar models (arXiv: 2608.03000)
  - Sleep onset as fold-like loss of wake stability; N1-N2/N2-N3 as continuous crossovers; NREM-REM as first-order desynchronizing switch
  - Ginzburg term adds spatial predictions: correlation length growth and local-to-global recruitment dynamics
  - Framework distinguishes bifurcation, coexistence, noise-driven escape, smooth crossover, and scoring-induced discontinuity
  - **Activation**: landau-ginzburg, sleep-stage transitions, phase transitions, neural fields, EEG analysis, sleep staging

### Detecting high-frequency brain disorder signals using dynamic mode decomposition from EEG
- [[dmd-high-frequency-eeg-brain-disorder-detection]] - Methodology for extracting consistent high-frequency dynamical patterns from EEG using Dynamic Mode Decomposition (DMD) to identify neurological signatures that distinguish clinical groups like alcohol-dependent patients from controls (arXiv: 2608.02804)
  - High-frequency DMD modes serve as robust features for brain disorder detection with ~70% consistency rate across samples
  - Statistical validation framework using random distribution tests ensures feature reliability
  - PCA components of validated features form consistent patterns distinguishing alcohol-dependent group from control group
  - **Activation**: DMD EEG analysis, high-frequency brain signals, dynamic mode decomposition neuroscience, EEG brain disorder detection

### NeuroWorld: A Latent Brain World Model for Stimulus-Conditioned Human Brain Dynamics
- [[neuroworld-latent-brain-world-model]] - First brain world model framework that casts naturalistic brain functional dynamics prediction as stimulus-conditioned evolution in learned latent brain-state space, separating endogenous states from exogenous multimodal stimuli with strictly causal forecasting capabilities (arXiv: 2608.01773)
  - Two-stage architecture: Latent Dynamics Learning (LDL) for causal dynamics without reconstruction, and Latent Rollout Decoding (LRD) for subject-specific brain response generation
  - State-of-the-art multi-step rollout performance under strictly causal stimulus access with greater robustness to long-horizon autoregressive drift
  - Validated on SG-MIND dataset (20 participants, 8,519 paired clips, 140.7 person-hours) and three naturalistic movie-fMRI benchmarks
  - **Activation**: neuroworld, brain world model, latent brain dynamics, stimulus-conditioned forecasting, fMRI prediction

### Divisive Normalization Shapes Low-Rank Slow Manifolds for Continuous Working Memory
- [[recurrent-divisive-normalization-working-memory]] - Recurrent Divisive Normalization Network (RDNN) methodology that uses divisive normalization to create robust low-rank slow manifolds for continuous working memory, preventing manifold shattering under time-varying inputs while enabling high-fidelity continuous representations (arXiv: 2608.01947)
  - Divisive normalization introduces activity-dependent local gradient scaling during BPTT, leading to self-compression of effective rank
  - Mathematically essential for preventing manifold shattering under time-varying inputs (subtractive inhibition insufficient for dynamic conditions)
  - Creates robust, high-fidelity slow manifolds that maintain continuous variables without discretization into point attractors
  - **Activation**: divisive normalization, working memory, continuous attractor, recurrent neural network, slow manifold, RDNN

### SeekBrain: An Autonomous Multi-Agent System for Accelerating Neuroscience Discovery
- [[seekbrain-autonomous-neuroscience-discovery]] - Autonomous multi-agent framework for accelerating neuroscience discovery through domain-grounded hierarchical planning and cross-modal data analysis, dynamically constructing analysis recipes from code-paper pairs and generating hypotheses on demand (arXiv: 2607.29347)
  - Extracts analysis recipes from neuroscience code-paper pairs to codify domain expertise
  - Uses hierarchical planning to decompose research questions into executable subtasks
  - Integrates behavioral, neural, and anatomical data to reveal structured neural representations
  - Validated on BrainArena benchmark showing substantial outperformance over agent baselines
  - **Activation**: seekbrain, autonomous neuroscience, multi-agent neuroscience, brainarena benchmark

## 2026-08-06 - Deep Learning Research (Cron Job)

### TurnSight: Turn-Level Hindsight Self-Distillation for Tool-Integrated Reasoning
- [[turnsight-turn-level-hindsight-self-distillation]] - Turn-Level Hindsight Self-Distillation framework for Tool-Integrated Reasoning (TIR) that derives supervision from execution-conditioned hindsight with multiple lookahead horizons and cross-horizon directional agreement for reliable credit assignment in long-horizon agentic tasks (arXiv: 2608.04007)
  - Execution-conditioned hindsight derives supervision from states actually visited by the agent during execution
  - Multi-horizon hindsight views with different lookahead horizons enable robust signal selection
  - Cross-horizon directional agreement filters out unreliable supervision signals
  - Normalized advantage modulation preserves original optimization direction while adapting RL advantages
  - **Activation**: turnsight, turn-level hindsight, tool-integrated reasoning, TIR, hindsight self-distillation

### Sparse Weight Decomposition for Efficient Circuit Extraction from Pretrained Transformers
- [[sparse-weight-decomposition-circuit-extraction]] - Sparse Weight Decomposition (SWD) for efficient circuit extraction from pretrained transformers that reparameterizes linear projections by factorizing weight matrices into two sparse factors with shared intermediate coordinates as circuit units (arXiv: 2608.03913)
  - No separate training required - works directly on pretrained models
  - Uses less than 1% of data required by strong baselines like Transcoder
  - Features zero-data variant enabling broader mechanistic interpretability analysis
  - Matches held-out fidelity of strong baselines while being more data-efficient
  - **Activation**: sparse weight decomposition, swd, circuit extraction, mechanistic interpretability, transformer interpretability