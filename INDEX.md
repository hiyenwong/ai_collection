## 2026-08-12 - Systems Engineering Research (Cron Job)

### GENCO – A Unified Neural Solver Embedded in a Development Framework for Steady-State Grid Analysis
- [[genco-unified-neural-solver-grid-analysis]] - GENCO unified neural solver for power grid analysis. (arXiv: 2608.09921)
  - Unified neural solver capable of solving Power Flow (PF), Optimal Power Flow (OPF), and State Estimation (SE) problems simultaneously
  - Open-source GridFM Development Framework with large-scale datasets for training and validation
  - **Activation**: genco neural solver, grid analysis framework, power flow neural network, unified grid solver, GridFM development framework

### Model-Based Systems Engineering Framework for SysML-Driven Design of Autonomous UAVs
- [[sysml-driven-uav-design-framework]] - SysML-driven MBSE framework for autonomous UAV design. (arXiv: 2608.09547)
  - Four-layer SysML-driven approach mapping requirements to ROS 2 architecture
  - Supports traceability and verification throughout the development lifecycle
  - **Activation**: sysml uav design, mbse autonomous uav, sysml ros2 integration, uav systems engineering, model-based uav design
## 2026-08-12 - Neuroscience Research (Cron Job)

### PTQ4SNN: Membrane-Aware Post-Training Quantization for Spiking Neural Networks
- [[ptq4snn-membrane-aware-post-training-quantization]] - PTQ4SNN membrane-aware post-training quantization for SNNs. (arXiv: 2608.07066)
  - Channel-wise Unified Scale Bridge constrains membrane scale as s_mem,c = s_w,c * 2^k_c, enabling shift-compatible scale conversion
  - Mixed-Precision Bit Allocation assigns 2/4/8-bit precision to membrane channels based on firing activity and quantization sensitivity
  - Supports both convolutional SNNs and spike-driven Transformers without backbone retraining
  - **Activation**: PTQ4SNN, membrane-aware quantization, SNN quantization, post-training quantization spiking, membrane state quantization

### Graph Analysis of Neuronal-Culture Connectivity Derived from a Reservoir-Computing Model
- [[graph-analysis-neuronal-culture-reservoir-computing]] - Graph analysis of neuronal cultures using Reservoir Computing-derived connectivity maps. Extracts Intrinsic Connectivity Maps (ICM) from neural activity and applies graph centrality measures to quantify network dynamics. (arXiv: 2608.09773)
  - Reservoir Computing framework reconstructs network connectivity from MEA recordings by training to extract Intrinsic Connectivity Matrix (ICM)
  - Interprets ICM as effective adjacency matrix for graph-theoretical analysis including node centrality measures and global network metrics
  - Validated against ground-truth networks with strong performance: ROC AUC up to 0.922, F1 scores up to 0.796, NMWA Pearson correlation up to 0.692
  - **Activation**: neuronal culture connectivity, reservoir computing connectivity, ICM graph analysis, MEA graph theory, neuronal network centrality, in vitro connectivity inference, graph analysis reservoir computing

## 2026-08-11 - Quantum Computing Research (Cron Job)

### SuperNeuroMAT: An Efficient Matrix-based Simulator for Spiking Neural Networks
- [[superneuromat-efficient-matrix-snn-simulator]] - SuperNeuroMAT: Matrix-based SNN simulator. (arXiv: 2608.08479)
  - Novel matrix-based approach for LIF neuron dynamics with dense/sparse execution modes
  - Simulates 10K neurons (dense) or 100K neurons (sparse) on standard hardware without specialized requirements
  - Outperforms NEST, Brian2, BindsNET, and snnTorch in execution speed and memory efficiency
  - Supports machine learning benchmarks, neuromorphic vision tasks, and general-purpose workloads including shortest path algorithms and arithmetic operations
  - **Activation**: SuperNeuroMAT, matrix-based SNN simulator, efficient spiking neural network simulation, neuromorphic computing framework, LIF neuron dynamics matrix approach

### NeuroRefiner: Morphology-Aware Multi-Agent Refinement for 3D Fluorescence Microscopy Neuron Segmentation
- [[neurorefiner-multi-agent-neuron-segmentation]] - NeuroRefiner multi-agent 3D neuron segmentation framework. (arXiv: 2608.09636)
  - Three collaborative agents: diagnosing topological errors, generating correction instructions, validating refinement quality
  - Uses TopoRefineNet 3D U-Net-based tool with cross-modality feature fusion
  - Achieves 3.02% F1 improvement on ZBFWB dataset
  - **Activation**: neurorefiner, multi-agent neuron segmentation, 3d fluorescence microscopy, neuron morphology refinement, topological error correction, TopoRefineNet

## 2026-08-11 - Quantum Computing Research (Cron Job)

### A Quantum Reservoir for Neurodynamical Forecasting
- [[quantum-reservoir-neurodynamical-forecasting]] - Quantum Reservoir Computing (QRC) methodology using transverse-field Ising model, heterogeneous quantum measurements, and polynomial ridge regression for neural activity forecasting. (arXiv: 2608.00139)
  - Combines quantum reservoir based on transverse-field Ising model with heterogeneous quantum measurements and polynomial ridge regression
  - Demonstrates feasibility on actual quantum hardware with stable, convergent predictions on simulated EEG data
  - Uses parallel reservoir architecture for biological signal processing with ensemble prediction approach
  - Establishes practical baseline for clinical time-series forecasting with quantum systems
  - **Activation**: quantum reservoir computing, neurodynamical forecasting, QRC EEG, quantum neural forecasting, transverse-field Ising reservoir
## 2026-08-11 - Systems Engineering Research (Cron Job)

### Dual-Node NVIDIA DGX Spark Distributed LLM Training over Tailscale Mesh VPN with Direct Fiber Link
- [[dual-node-dgx-spark-distributed-llm-training]] - Dual-node DGX Spark LLM training over Tailscale. (arXiv: 2608.07226)
  - Deploys distributed LLM training across two NVIDIA DGX Spark systems with GB10 Grace Blackwell SoC and 128GB unified memory
  - Uses dedicated 200 Gb/s QSFP56 direct fiber link for training communication with Tailscale mesh VPN for remote administration
  - Achieves ~1,890 tokens/second throughput with Depth-20 NanoChat model and global batch of 131,072 tokens per step
  - **Activation**: distributed systems, DGX Spark, LLM training, Tailscale, NCCL, multi-node training, cybersecurity fine-tuning

### Causal World System for Decision Making and Agentic AI Ecosystems
- [[causal-data-management-ecosystem-agentic-ai]] - Causal World System for agentic AI decision making. (arXiv: 2608.07214)
  - Builds explicit causal layer in integrated AI ecosystems to distinguish drivers from correlates
  - Enables trustworthy autonomous agents through counterfactual and prescriptive analysis
  - Integrates heterogeneous data sources with queryable interface for decision support
  - **Activation**: causal reasoning, data management, agentic AI, decision making, Causal World System, counterfactual analysis

## 2026-08-11 - Neuroscience Research (Cron Job)

### PTQ4SNN: Membrane-Aware Post-Training Quantization for Spiking Neural Networks
- [[ptq4snn-membrane-aware-post-training-quantization]] - PTQ4SNN membrane-aware SNN quantization framework for joint weight and membrane state quantization without retraining. (arXiv: 2608.07066)
  - Addresses critical gap in SNN deployment by quantizing both weights and recurrent membrane states using only small calibration set
  - Introduces Channel-wise Unified Scale Bridge constraining membrane scale as s_mem,c = s_w,c * 2^k_c for hardware efficiency
  - Implements Mixed-Precision Bit Allocation assigning 2/4/8-bit precision based on firing activity and quantization sensitivity
  - Supports both convolutional SNNs and spike-driven Transformers with reusable projection-LIF architecture
  - **Activation**: PTQ4SNN, membrane quantization, SNN quantization, post-training quantization, spiking neural networks, neuromorphic deployment, low-bit SNN

### FedDOSE: Federated Learning Framework Decomposing Site Effects for Modeling Brain Dynamic Functional Connectivity
- [[feddose-federated-learning-dynamic-functional-connectivity]] - Novel federated learning framework that explicitly decomposes site effects for dynamic functional connectivity analysis using Modularity-Guided Tucker Decomposition and class-specific prototypes with Optimal Transport barycenter formulation. (arXiv: 2608.07393)
  - Addresses statistical heterogeneity and site differences in multi-site fMRI datasets through explicit site effect decomposition
  - Introduces Modularity-Guided Tucker Decomposition to encode high-dimensional dFC tensors and capture modular-level spatio-temporal patterns
  - Uses class-specific prototypes aligned globally via Optimal Transport barycenter formulation and Procrustes analysis
  - Outperforms state-of-the-art methods in ASD and ADHD detection on ABIDE-I, ABIDE-II, and ADHD-200 datasets
  - **Activation**: FedDOSE federated learning, Dynamic functional connectivity dFC, Multi-site fMRI privacy, Modularity-Guided Tucker Decomposition, Optimal Transport barycenter fMRI

### International Transfer of Stochastic Cortical Self-Reconstruction
- [[international-transfer-stochastic-cortical-self-reconstruction]] - Stochastic Cortical Self-Reconstruction (SCSR) framework for personalized mapping of gray matter atrophy with cross-population transferability evaluation from UK Biobank to Chinese dataset. (arXiv: 2608.07092)
  - Estimates individualized healthy reference directly from observed cortical thickness at vertex level for subtle subject-specific deviation detection
  - Evaluates four training strategies: direct application, fine-tuning, training from scratch, and joint training across populations
  - Compares MLP and Spherical UNet reconstruction backbones with fine-tuned SUNet achieving highest discriminative performance (AUC = 0.848)
  - Demonstrates strong cross-population transferability with low reconstruction errors across lifespan despite narrow training age distribution
  - **Activation**: Stochastic Cortical Self-Reconstruction, SCSR personalized mapping, Gray matter atrophy vertex-level, Cross-population transfer neuroimaging, UK Biobank Chinese dataset

## 2026-08-10 - Neuroscience Research (Cron Job)

### Layered Surprise Cascades: From Local Learning to Global Prediction Through Layered Surprise Cascades
- [[layered-surprise-cascades-predictive-coding]] - Layered Surprise Cascades framework for biologically plausible predictive coding using local contrastive learning and activity cancellation. (arXiv: 2608.05481)
  - Implements recurrent Forward-Forward algorithm with inverted objective for negative data to yield predictive representations across layers
  - Eliminates need for error-coding neurons by using local contrastive learning and activity cancellation mechanisms
  - Creates natural surprise signals that cascade through multiple layers with top-down modulation
  - **Activation**: layered surprise cascades, predictive coding, hierarchical processing, contrastive learning, forward-forward algorithm, cortical computation, surprise signaling, top-down modulation

### PTQ4SNN: Membrane-Aware Post-Training Quantization for Spiking Neural Networks
- [[ptq4snn-membrane-aware-quantization]] - Framework that jointly quantizes weights and recurrent membrane states using channel-wise Unified Scale Bridge and Mixed-Precision Bit Allocation. (arXiv: 2608.07066)
  - Channel-wise Unified Scale Bridge constrains membrane scale as `s_mem,c = s_w,c * 2^k_c` for shift-compatible scale conversion
  - Mixed-Precision Bit Allocation assigns 2/4/8-bit precision to membrane channels based on firing activity and quantization sensitivity
  - Enables full low-bit SNN deployment while preserving accuracy under W4 weight quantization and ~4-bit membrane precision
  - **Activation**: PTQ4SNN, membrane-aware quantization, SNN quantization, post-training quantization spiking, membrane state quantization, unified scale bridge, mixed-precision SNN

### Effective pruning of task-trained recurrent neural networks using noisy fluctuations and connection rescaling
- [[effective-pruning-task-trained-rnn-noisy-fluctuations]] - Noise-prune preserves task performance in RNNs. (arXiv: 2608.05464)
  - Biologically-plausible local pruning rule using noisy fluctuations to determine connection importance
  - Samples connections to preserve based on importance and strengthens retained connections
  - Outperforms magnitude-based pruning and matches/exceeds second-order methods
  - Optimal empirical rescaling factor is lower than theoretical prediction
  - **Activation**: noise-prune, RNN pruning, biologically plausible pruning, task-trained RNN, connection rescaling, noisy fluctuations

## 2026-08-10 - Anthropic Research (Cron Job)

### An off switch for dual-use knowledge in AI models
- [[off-switch-dual-use-knowledge-control]] - GRAM methodology for controlling dual-use knowledge in AI models with an off switch.
  - Gradient-Routed Auxiliary Modules (GRAM) provide selective control over harmful capabilities
  - Auxiliary modules can be disabled at inference time without affecting other model functions
  - Enables training with gradient routing to selectively enable/disable capabilities
  - **Activation**: dual-use knowledge control, GRAM methodology, AI safety, harmful capability control, gradient routing