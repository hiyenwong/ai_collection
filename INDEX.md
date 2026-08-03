## 2026-08-04 - Neuroscience Research (Cron Job)

### MPP-GNN: Subject-Adaptive Community Detection for fMRI-Based Alzheimer's Disease Classification
- [[mpp-gnn-subject-adaptive-community-detection]] - Meta Probabilistic Pooling GNN framework that performs adaptive graph partitioning hierarchically to discover subject-specific functional modules and uses them as explicit priors to guide edge refinement and representation learning for Alzheimer's disease classification, achieving highest AUC on two public datasets (arXiv: 2607.28681)
  - Frames task as coupled bilevel optimization: upper level discovers subject-specific modules, lower level uses modules as explicit priors for edge refinement
  - Overcomes fixed module assumption in traditional GNN methods by enabling personalized community detection
  - Shows significant alignment with Yeo brain atlas and reveals network-level dedifferentiation pattern for AD
  - **Activation**: MPP-GNN, subject-adaptive community detection, fMRI Alzheimer's classification, bilevel optimization GNN, functional module discovery, brain network dedifferentiation

### Multi-Source Multi-View Graph Domain Adaptation with Hyperbolic Residual Encoding for Cross-Site MDD Identification from rs-fMRI
- [[multi-source-multi-view-graph-domain-adaptation-hyperbolic]] - Multi-Source Multi-View Graph Domain Adaptation with Hyperbolic Residual Encoding framework for cross-site Major Depressive Disorder (MDD) identification from resting-state fMRI, achieving 73.60% mean accuracy and 71.90% AUC across seven unlabeled target domains (arXiv: 2607.29531)
  - Constructs Pearson correlation, sparse representation, and Granger causality graphs for multi-view functional connectivity
  - Uses dual-stream adaptive fusion to integrate pairwise cross-view interactions while preserving view-specific information
  - Applies lightweight hyperbolic residual encoding for curvature-aware representation refinement
  - Implements class-wise Cauchy-Schwarz alignment, adversarial learning, information maximization, and confidence-aware pseudo-labeling for multi-source domain adaptation
  - **Activation**: multi-source domain adaptation brain, hyperbolic residual encoding fmri, cross-site mdd identification, multi-view functional connectivity, graph domain adaptation neuroscience

### Parameter-Efficient Fine-Tuning for Spiking Point Cloud Models
- [[spikepeft-parameter-efficient-snn-finetuning]] - First parameter-efficient fine-tuning framework for spiking point cloud models using Intrinsic Dynamics Tuning (IDT) and Silent-State Disambiguation Adaptation (SSDA), achieving 92.4% accuracy on ModelNet40 while updating only ~5% of parameters (arXiv: 2607.29048)
  - Intrinsic Dynamics Tuning (IDT) modulates membrane decay and firing thresholds while keeping synaptic weights frozen
  - Silent-State Disambiguation Adaptation (SSDA) recovers task-relevant information from informative silent states
  - Preserves energy efficiency advantages of SNNs while enabling efficient downstream task adaptation
  - **Activation**: spikepeft, parameter-efficient fine-tuning snn, spiking point cloud models, intrinsic dynamics tuning, silent state disambiguation, neuromorphic vision models

### ZUNA1.1: A more flexible EEG foundation model for Denoising and Super-resolution
- [[zuna1-1-flexible-eeg-foundation-model]] - 380M-parameter diffusion autoencoder for flexible EEG signal reconstruction with arbitrary channel configurations and temporal intervals, substantially outperforming spherical spline interpolation while maintaining ZUNA1 performance (arXiv: 2607.27308)
  - Supports variable sequence lengths up to 30s, arbitrary channel counts at arbitrary scalp locations
  - Can reconstruct specific temporal intervals within channels rather than entire channels
  - Handles real-world scenarios with non-uniform corruption across channels and time
  - **Activation**: zuna1.1 eeg foundation model, flexible eeg denoising, eeg super-resolution diffusion, arbitrary channel eeg reconstruction, variable length eeg diffusion

### The Sparsity Ceiling: Where Spiking Networks Can and Cannot Trade Activity for Energy
- [[sparsity-ceiling-spiking-networks-energy]] - Framework for analyzing energy-efficiency limits in Spiking Neural Networks through the sparsity ceiling concept, identifying minimum firing rates below which computational quality breaks down based on architecture, memory load, and task complexity (arXiv: 2607.26648)
  - Architecture-dependent ceilings: feed-forward perception (5% firing), recurrent language models (~50% firing), spiking transformers (2% firing)
  - Formalizes ceiling with information-theoretic bound ρ ≥ H_b^(-1)(log₂ M / H) where M is memory load and H is state width
  - Reveals trade-off axes: recurrence pays on firing rate axis, attention pays on memory wall axis
  - Identifies event-driven perception as domain where neuromorphic hardware excels
  - **Activation**: sparsity ceiling, SNN energy efficiency, spiking neural network limits, neuromorphic computing constraints, firing rate floor, memory wall attention

### Quantifying the cost of network computations to unpack structure-function relationships in the brain
- [[computational-affordance-landscape-brain-networks]] - Framework for quantifying network computation costs using control theory to understand structure-function relationships through computational affordance landscapes (arXiv: 2607.29537)
  - Defines computational affordance landscape as distribution of transition costs encoding which computations network structure readily supports
  - Insect navigation circuits: updating orientation is least costly computation, predictions match known circuitry
  - Human brain: sensory networks show heterogeneous landscapes (specialized processing), association networks show homogeneous landscapes (generalized processing)
  - RNNs: learning progressively increases landscape heterogeneity, reshaping affordable computations
  - **Activation**: computational affordance landscape, network computation cost, brain structure-function, neural circuit control, activity transition cost

### Adaptive FastOPD: Progress-Aware Rollout Horizon Expansion for Efficient On-Policy Distillation
- [[adaptive-fastopd]] - Adaptive FastOPD methodology for efficient on-policy distillation with progress-aware rollout horizon expansion. Reduces training time by 49.1-71.2% while maintaining or improving performance by dynamically expanding rollout horizons only when learning has plateaued and current horizon is sufficiently utilized. (arXiv: 2607.29494)
  - Uses four teacher-student signals measured relative to horizon entry values to detect learning plateaus
  - Prevents expansion triggered by small number of long responses through horizon utilization check
  - Achieves highest average performance while reducing training time by 49.1-71.2% relative to OPD 15K
  - **Activation**: adaptive-fastopd, progress-aware rollout, efficient on-policy distillation, dynamic horizon expansion, teacher-student agreement signals

### Knowing When to Quit: Diagnosing and Training LLMs to Abort Futile Reasoning
- [[carl-capability-aligned-rl]] - CaRL (Capability-aligned Reinforcement Learning) methodology for training LLMs to recognize and abort futile reasoning on beyond-capability tasks. Reduces computationally expensive yet semantically void reasoning through reward shaping and hindsight refusal augmentation. (arXiv: 2607.29211)
  - Characterizes futile reasoning as universal capability overreach with systematic miscalibration
  - Dominant failure mode is specious reasoning with subtle errors escalating with task difficulty
  - Uses reward shaping to incentivize refusal over futile reasoning
  - Converts failures into refusal supervision via hindsight refusal augmentation
  - **Activation**: carl, capability-aligned reinforcement learning, futile reasoning, specious reasoning, refusal training, capability boundaries, hindsight refusal augmentation

### The Parts Are Greater Than the Sum: Automated Task Sequencing for Efficient Training of Multi-Policy LLMs
- [[multi-policy-peft-task-sequencing]] - Automated task sequencing methodology for efficient training of multi-policy LLMs using QLoRA-based decoupled adaptation paths. Organizes optimization-compatible adaptation paths via task grouping and sequencing to maximize performance under fixed parameter budgets. (arXiv: 2607.29601)
  - Implements independent QLoRAs for each policy with fixed parameter budget constraints
  - Automatically groups tasks based on optimization compatibility and interference patterns
  - Sequences training to minimize negative transfer between policies
  - Achieves 44.78 score on TRACE benchmark demonstrating superior multi-task performance
  - **Activation**: multi-policy peft, automated task sequencing, qlora decoupled adaptation, optimization path organization, fixed parameter budget, task grouping compatibility