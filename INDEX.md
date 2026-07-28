## 2026-07-28 - Quantum Neuromorphic Research (Cron Job)

### Leveraging unlabelled data for generalizable neural population decoding
- [[mojo-ssl-neural-decoding]] - MOJO (Masked autOencoder-based JOint training) framework that combines self-supervised learning via masked autoencoding with supervised learning objectives for spike-tokenizing neural models, enabling superior performance with limited labelled data (arXiv: 2607.14086)
  - Joint SSL+SL training improves few-shot finetuning capability when only small amounts of labelled data from new sessions are available
  - Yields more interpretable neuronal representations, improving brain region classification and spike-statistics prediction without explicit optimization
  - Generalizes beyond spiking data to human electrocorticography during speech, achieving performance comparable to neuro-foundation models
  - **Activation**: neural decoding, spike-tokenizing, self-supervised learning, few-shot finetuning, brain-computer interface, neuro-foundation models, unlabelled neural data
## 2026-07-28 - Systems Engineering Research (Cron Job)

### Allostatic Control Systems: Goal Governance in Changing Environments
- [[allostatic-control-systems-goal-governance]] - Framework for designing control systems that govern not only goal pursuit but also goal appropriateness in changing environments, implementing two-timescale control with fast regulation loop and slow goal governance loop (arXiv: 2607.21771)
  - Two-timescale architecture separates fast goal pursuit from slow goal governance
  - Central principle: revise inappropriate goals faster than serviceability is lost by defending them
  - Evidence-based goal revision with timing-critical evidence-to-effect pathways
  - **Activation**: allostatic control, goal governance, adaptive reference, changing environments, two-timescale control, serviceability assessment## 2026-07-28 - Neuroscience Research (Cron Job)

### Universal BCI Personalization: One API for Frozen EEG Trunks and Foundation Models
- [[universal-bci-personalization-api]] - Trunk-agnostic BCI personalization API that works across heterogeneous frozen EEG trunks without per-architecture personalization stacks (arXiv: 2607.22397)
  - Single contract encode to Bayesian head to BrainState architecture enables OEMs to integrate once and swap trunks
  - Achieves orders of magnitude less adaptation wall time while recovering much of fine-tune accuracy gain
  - Calibration-only-when-clean holds in 12/18 experimental cells with subject-level confidence intervals
  - **Activation**: universal bci personalization, trunk-agnostic eeg, nimbus personalizer, frozen eeg trunks, bci foundation models
### NUMA balancing hampering performance of spiking network simulations
- [[numa-balancing-snn-performance]] - NUMA balancing performance optimization that can reduce energy consumption by 30% in spiking network simulations by disabling automatic NUMA balancing on HPC systems (arXiv: 2607.22275)
  - Identifies that automatic NUMA balancing dynamically interacts with spiking network memory access patterns, causing performance fluctuations
  - Provides methodology for per-job NUMA balancing control to optimize performance and energy consumption
  - **Activation**: numa balancing snn, spiking neural network numa optimization, hpc snn performance tuning, energy efficient snn simulation, numa balancing disable neuroscience

### On a cross coupling of Rulkov neural maps
- [[rulkov-neural-maps-cross-coupling]] - Novel coupling methodology for Rulkov neural maps preserving chaos and generating strange attractors (arXiv: 2607.22318)
  - Introduces cross-coupling that preserves chaotic dynamics while enabling complex synchronization patterns
  - Generates strange attractors through carefully designed coupling functions
  - Demonstrates applications in secure communication and pattern recognition
  - **Activation**: rulkov maps, cross coupling, chaos preservation, strange attractors, neural dynamics

### Spectral theory for population density dynamics of spiking neurons with refractoriness
- [[spectral-theory-spiking-neurons-refractoriness]] - Rigorous operator-theoretic framework using non-self-adjoint boundary eigenvalue problems for Fokker-Planck operators to analyze spiking neuron populations with refractory periods (arXiv: 2607.20699)
  - Solves long-standing open problem of incorporating absolute refractory periods into population density approaches
  - Provides complete spectral characterization and identifies exceptional points where oscillatory modes emerge
  - Derives exact transfer function correcting previous heuristic derivations with additional threshold-noise contributions
  - Shows refractoriness can facilitate limit cycle onset in interacting neuron populations under mean-field approximation
  - **Activation**: spectral theory, spiking neurons, refractoriness, population density, Fokker-Planck

### When Language Models Meet NeuroGraphs: Exploring Enhanced Agentic LLM Framework Towards Brain Network Analysis
- [[brainagent-agentic-llm-brain-network]] - BrainAgent agentic LLM framework for knowledge-enhanced brain network analysis, reformulating connectome classification as iterative topology-aware understanding, external retrieval, reasoning, and reflection (arXiv: 2607.22082)
  - Converts raw brain networks into compact multi-level structural descriptions through brain-specific analysis tools
  - Retrieves relevant neuroscience knowledge and task-specific cases to ground the reasoning process
  - Generates structured predictions with reflective verification for comprehensive, multi-level explanations
  - **Activation**: brain network analysis, connectome classification, agentic LLM neuroscience, knowledge-enhanced brain analysis, NeuroGraphs, BrainAgent framework

- [[project-pilot-ai-drone-control]] - Methodology for testing AI control of physical systems like drones through constrained interfaces and safety protocols. Based on Anthropic's July 2026 frontier red teaming research.
  - Constrained interface design with limited action space and safety boundaries
  - Safety protocol framework including pre-flight validation and emergency override
  - Evaluation metrics for task completion, safety compliance, and robustness
  - **Activation**: project pilot, ai drone control, physical system control, frontier red teaming

## 2026-07-28 - Deep Learning Research (Cron Job)

## 2026-07-28 - Neuroscience Research (Cron Job)

### Graph-Based Correlation Matrix Generation: A Convex Optimization Approach
- [[graph-based-correlation-matrix-generation]] - Graph-based correlation matrix generation using convex optimization for controlled sparsity and mean off-diagonal values (arXiv: 2607.22436)
  - Generates correlation matrices consistent with specified graph structures while allowing precise control over statistical properties
  - Provides tunable control over mean off-diagonal correlation values and maintains mathematical validity
  - Validated on real neuroscience and finance datasets for practical applicability
  - **Activation**: graph correlation matrix generation, convex optimization correlation, structured correlation matrices, neuroscience functional connectivity simulation, finance asset correlation modeling

### Interpretable EEG biomarkers with bag-of-waves: Spatial and temporal waveform dictionaries for low-data regimes
- [[bag-of-waves-eeg-biomarkers]] - Interpretable EEG biomarkers using shift-invariant k-means to learn waveform atoms without labels, effective in low-data regimes (arXiv: 2607.22508)
  - Learns small dictionary of recurring EEG waveform templates (atoms) using shift-invariant k-means
  - Converts continuous EEG into atom token sequences with temporal n-grams and spatial cross-channel extensions
  - Achieves competitive performance with state-of-the-art deep models while providing full interpretability
  - **Activation**: bag-of-waves, EEG biomarkers, interpretable EEG, waveform dictionaries, low-data EEG

### LeAct: Learning to Reason from Expert Actions
- [[leact-learning-to-reason-from-expert-actions]] - LeAct framework for recovering chain-of-thought reasoning from expert systems that only produce actions without explicit reasoning traces, treating CoT as a latent variable optimized via action probability scoring (arXiv: 2607.21856)
  - Recovers reasoning from silent expert systems like game solvers and theorem provers
  - Uses action probability scoring to evaluate and retain high-quality CoTs
  - Achieves 5× closer to solver performance than expert-iteration baselines
  - **Activation**: leact, expert actions, chain of thought recovery, silent experts, action-guided reasoning

### Teaching LLMs to Self-Evolve: Cultivating Core Meta-Skills with Reinforcement Learning
- [[teaching-llms-to-self-evolve]] - Framework for teaching LLMs to self-evolve by cultivating core meta-skills with reinforcement learning, enabling autonomous capability expansion through iterative self-improvement cycles (arXiv: 2607.21971)
  - Builds foundational meta-skills for autonomous self-improvement
  - Uses RL to optimize self-evolution behaviors and strategies
  - Creates feedback loops for continuous capability growth
  - **Activation**: self-evolve, meta-skills, reinforcement learning, autonomous improvement, capability expansion

### IFCLoRA: Topology-Aware Rank Allocation for Parameter-Efficient Fine-Tuning
- [[ifclora-topology-aware-rank-allocation]] - IFCLoRA framework for topology-aware rank allocation in parameter-efficient fine-tuning, dynamically allocating LoRA ranks based on model architecture topology and task requirements (arXiv: 2607.22251)
  - Uses model architecture topology to guide optimal rank allocation
  - Achieves better performance with fewer parameters than uniform LoRA
  - Adapts rank allocation to specific downstream tasks and complexity
  - **Activation**: ifclora, topology-aware, rank allocation, parameter-efficient tuning, lora optimization

### Cross-Tokenizer On-Policy Distillation via Byte-Prefix Marginalization
- [[cross-tokenizer-on-policy-distillation]] - Cross-Tokenizer On-Policy Distillation framework using byte-prefix marginalization to enable knowledge transfer between models with different tokenizers while preserving policy quality (arXiv: 2607.22334)
  - Enables distillation between models with incompatible tokenization schemes
  - Uses byte-level alignment and prefix marginalization for compatibility
  - Maintains high-quality policy learning during cross-tokenizer transfer
  - **Activation**: cross-tokenizer, on-policy distillation, byte-prefix marginalization, tokenizer compatibility, policy transfer

### Universal BCI Personalization: One API for Frozen EEG Trunks
- [[universal-bci-personalization-api]] - Universal BCI Personalization framework providing a unified API for frozen EEG trunks, enabling one-size-fits-all personalization across diverse brain-computer interface systems (arXiv: 2607.22397)
  - Provides trunk-agnostic API for BCI personalization across heterogeneous encoders
  - Works with classical trunks (EEGNet, Shallow, Deep, Conformer, ATCNet) and foundation models
  - Reduces adaptation wall time by orders of magnitude while maintaining accuracy
  - **Activation**: bci personalization, frozen eeg encoders, trunk-agnostic api, foundation model adaptation, nimbus personalizer