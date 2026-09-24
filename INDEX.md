## 2026-09-25 - Deep Learning Research (Cron Job)

### Harness-Zero: Harness Distillation via Agent-as-Harness
- [[harness-zero-agent-as-harness]] - Distills specialized agent-harness behaviors into model weights via a harnessing agent that corrects student responses in the target harness's action space, so gains survive with a single fixed harness (arXiv: 2609.24974)
  - Agent-as-harness beats code-as-harness for frontier LLMs; internalized behavior (44.3%) exceeds even keeping the harness attached (41.7%), from 23.3% base
  - 82.3% average recovery of harness-induced behaviors across 28 patterns in knowledge work, tool use, science domains
  - **Activation**: harness distillation, agent-as-harness, harness removal, agent framework distillation, tool harness internalization, deployment-time harness

### Memory Attention
- [[memory-attention-lookup-values]] - Replaces attention value projection with token-indexed memory tables plus contextual keys; value construction reduces to lookup+add at inference with CPU offloading (arXiv: 2609.28399)
  - Memory supplies token-specific reusable representations; keys preserve context dependence; normalization folds into tables post-training
  - Improved LM perplexity and downstream performance under matched token budgets; token-indexed retrieval enables CPU offload with prefetch
  - **Activation**: memory attention, token-indexed memory, value projection replacement, attention lookup, CPU offloading inference, memory-table attention

### A discrete generative model of neuronal spiking activity on microelectrode arrays
- [[mea-array-spiking-rvq-motif-transformer]] - Discrete generative model for sparse array-wide MEA binary spike volumes: RVQ motif vocabulary + factorized masked transformer predicting where activity occurs and which motif appears (arXiv: 2609.23907)
  - Handles variable electrode subsets across assays without sorted-neuron assumptions; no assay-specific learned parameters
  - 5.2× voxel reconstruction AP vs flat tokenizer; 1.4-2.6× site-level AP vs generative baseline on 31 assays (human organoids + hippocampal tissue); assay identity explains only 9% of motif-use entropy
  - **Activation**: MEA generative model, microelectrode array spiking, RVQ spike motifs, masked transformer spiking, array-wide binary spike volumes, spike tokenization

### RL Starts before RL: On Policy Distillation for Better Reinforcement Learning
- [[opd-pre-rl-distillation]] - On-policy distillation as RL preparation stage: OPD-initialized students reach higher post-RL performance than direct RL or SFT+RL, even when OPD gives little immediate accuracy gain (arXiv: 2609.28145)
  - Pre-RL Pass@k does not explain the benefit; distributional alignment with teacher beyond top-1 agreement preserves reasoning paths RL can refine
  - Divergence selection rule: reverse-KL better before RL, forward-KL overtakes after RL (student trajectories); teacher trajectories keep reverse-KL ahead at both stages
  - **Activation**: OPD before RL, policy distillation RL preparation, pre-RL distillation, reverse KL vs forward KL, Pass@k limitation, RL initialization

### Distilling Sequential Computation in Transformer Language Models
- [[token-span-collapse-sequential-distillation]] - Lightweight merge module collapses predictable token spans into single surrogate embeddings with KV-cache rollback; pretrained models run on compressed inputs without retraining (arXiv: 2609.27233)
  - Merge module generates surrogate capturing the span's functional role; rollback substitutes stored multi-token KV entries with single-step surrogates
  - Up to 40% effective sequence-length reduction with minimal degradation across QA, summarization, commonsense, long-form math reasoning
  - **Activation**: token span collapse, sequence compression inference, surrogate embedding merge, KV cache rollback, training-free prompt compression

### Support-Compiled Feature Folding: More Evidence at Lower Memory Across Tabular Foundation Models
- [[scff-support-compiled-feature-folding]] - Training-free inference framework routing support-ranked features through bounded encoder leaves, support-checking residual evidence, and merging messages for single prediction — converts quadratic feature-interaction cost to linear (arXiv: 2609.28208)
  - Improved accuracy and NLL on all six tabular FM backbones; up to 26.1% relative error reduction; 2.09-2.36× median GPU-memory savings, 34.3× max peak ratio
  - Under fixed memory ceiling, saved budget buys more support-selected evidence: +4.06/+3.72 points over widest single leaf (TabICLv2/TabPFN-3)
  - **Activation**: tabular foundation model, wide table inference, feature folding, quadratic feature mixing, support-ranked features, frozen backbone inference

### Nonequilibrium Phases of Repulsive Self-Attention: Chaos, Attention Condensation, and Emergent Locality
- [[repulsive-self-attention-nonequilibrium]] - Minimal recurrent transformer (Q=K=I, V=-I) exhibiting flip bifurcation, chaos, and attention condensation across d=2 and d=N scaling regimes; temporal activity, condensation, and clustering are distinct phenomena (arXiv: 2609.28448)
  - d=2: attention stays diffuse as N→∞ at finite β; condensation only at β~N²; hard-routing produces emergent butterfly cone via ballistic perturbation transmission
  - d=N: condensation transition at β=O(1) driven by dynamically generated finite overlap gaps; phases include consensus flips, condensed chaotic routing, fragmented cluster flips
  - **Activation**: repulsive self-attention, attention condensation, nonequilibrium attention phases, recurrent transformer dynamics, flip bifurcation, attention chaos

### CereVLA: Cerebellum-Inspired Consequence-Aware Residual Governance for Efficient Vision-Language-Action Execution
- [[cerevla-consequence-aware-residual-governance]] - Lightweight residual refinement plus predictive consequence evaluation (recurrent SSM + history-aware classifier) with selective suppression of unfavorable corrections on frozen chunked VLA policies (arXiv: 2609.27468)
  - SO-101 real robot: success 57.5% → 90.0% vs frozen SmolVLA; -19.6% mean control steps among successful trials
  - Key insight: residuals matching reference actions better can still cause worse downstream consequences; predict-then-suppress governance fixes this
  - **Activation**: consequence-aware residual, VLA action chunk correction, frozen policy residual refinement, governor suppression, cerebellum robotics

### Order-Invariant Answers, Order-Sensitive Representations in Mathematical Reasoning
- [[permutation-snr-representation-invariance]] - Permutation SNR metric showing models that solve reordered problems more accurately represent rule orderings MORE distinctly; answer invariance does not require representation invariance (arXiv: 2609.28442)
  - Layer-averaged permutation SNR positively rank-correlated with accuracy in every synthetic setting, Spearman ρ up to 0.86 across 16 models (1B-8B)
  - Distinguishes answer invariance from representation invariance; distinct encoding of permutation is functional, not noise — basis for representational diagnostics beyond accuracy
  - **Activation**: permutation SNR, answer invariance vs representation invariance, rule order sensitivity, mathematical reasoning representations, equivalence class probing

### FFM-CP: Cross-Backbone Fusion of Vision-Language Foundation Models for Few-Shot Computational Pathology
- [[ffm-cp-cross-backbone-procrustes-fusion]] - Closed-form Orthogonal Procrustes alignment of heterogeneous VLM representations from support images, plus unified graph refining support features and prototypes with dual text/retrieval branches (arXiv: 2609.27710)
  - Closed-form alignment preserves within-model geometry without training a network — critical for few-shot regimes
  - Higher mean macro-F1 than strongest individually adapted member in 50 of 54 comparisons (3 backbone combos × 6 datasets × 3 shot settings)
  - **Activation**: cross-backbone fusion, Procrustes alignment few-shot, pathology VLM fusion, prototype graph refinement, heterogeneous representation alignment

### ForgetMimic: Motion Unlearning for Reinforcement Learning Humanoid Control
- [[forgetmimic-motion-unlearning-humanoid]] - First motion-level unlearning for physical humanoid control: degrades K target motions while preserving N-K remaining, resolving two unlearning-failure mechanisms in robot RL (arXiv: 2609.28378)
  - Motivations: safety (poisoned/malicious motions), privacy, GDPR right-to-be-forgotten for motion data
  - Validated on Unitree G1 and H2 across 12 motions (Dance, Fight, Flip); eliminates designated motions while others operate normally
  - **Activation**: motion unlearning, humanoid policy forgetting, GDPR robotics, poisoned motion removal, RL policy unlearning, motion-level machine unlearning

### Distillation for Efficient Multitask Manipulation Policies via Conditional Flow Matching
- [[cfm-multitask-policy-distillation]] - Distills single-task CFM experts into a shared multi-task policy by transferring learned velocity fields, combined with original CFM objective for demonstration fidelity (arXiv: 2609.28107)
  - Velocity fields are the transferable object: matching student velocity to expert velocity transfers flow structure, not just final actions
  - RLBench: improves multi-task performance over naive concatenated training at fixed model size — no capacity increase
  - **Activation**: multitask flow matching distillation, robot manipulation policy, velocity field transfer, CFM expert distillation, shared policy fixed capacity

### Can LLMs Reason About Runtime Behavior? A Repository-Level Dynamic Benchmark
- [[swe-flux-runtime-reasoning-benchmark]] - 480 execution-grounded instances across 12 real Python repositories with gold answers auto-harvested from instrumented test executions (no manual labels, no LLM judges), plus input-perturbation variant generation (arXiv: 2609.28449)
  - Best of five LLMs achieves only 37% accuracy; strong on invariants/intra-procedural control flow, weak on dataflow/inter-procedural/state reasoning/suite-level aggregation
  - Oracle-harvesting pipeline generates valid fresh variants for ~90% of instances, substantially harder — reusable methodology for execution-grounded evals on any codebase
  - **Activation**: runtime behavior reasoning, execution-grounded benchmark, repository-level QA, SWE-Flux, oracle harvesting, program state reasoning

### Discovery of fully efficient fault indicators along a data-based diagnosis process
- [[dt4x-plus-diagnosis-decision-tree]] - Enhanced symbolic-regression decision tree (DT4X+) whose node expressions separate target classes while preserving ARR coherence of non-target classes, yielding fully efficient fault indicators (arXiv: 2609.28087)
  - Fixes DT4X's fragmentation problem: naive pairwise separation scatters non-target classes; composite loss keeps them coherent
  - Learned relations become fully consistent with analytical redundancy relation properties — interpretability + data-driven adaptability
  - **Activation**: DT4X, analytical redundancy relations, symbolic regression decision tree, fault diagnosis indicator, hybrid diagnosis, ARR properties

## 2026-09-25 - Mathematics & Statistics (Cron Job)

### On Relationship Between Circuit Depth and Trainability of VQAs
- [[whrf-vqa-trainability-phase-transition]] - Maps VQA loss landscapes to Wishart Hypertoroidal Random Fields; Kac-Rice critical point statistics reveal a trainability phase transition where local minima concentrate near the global minimum (arXiv: 2609.27488)
  - Phase transition threshold governed by ratio of problem Hamiltonian degrees of freedom N (exponential in qubits) to number of independent VQA parameters P; below threshold local minima are scattered, above it they collapse in function value
  - Symmetry reduction operations on the Hamiltonian lower effective N, shrinking the required parameter count to a reachable regime — the actionable lever for making VQAs trainable
  - Kac-Rice formula reformulated and simulated for WHRFs: ρ(E) = E[|det(∇²H)|·δ(H−E)·δ(∇H)]
  - **Activation**: VQA loss landscape random field, Kac-Rice critical points, Wishart hypertoroidal, trainability phase transition, symmetry reduction, ansatz depth selection

### Optimal low-rank compression of quantum dynamics
- [[optimal-lowrank-quantum-dynamics-compression]] - Tight (matching upper+lower bound) rank limits for low-rank/MPO representation of local quantum evolution, with explicit 1D constructive algorithm (arXiv: 2609.27497)
  - Time-independent: log D = Õ(t + √log(1/ε)) with provably necessary accuracy exponent 1/2; driven evolution exponent 2/3 — accuracy cost is polylog, time cost is linear (Lieb-Robinson)
  - Dynamical entanglement spectra follow distinct small-α Rényi laws: α⁻¹ (static) vs α⁻² (driven) — usable as compressibility diagnostics
  - 1D static case constructively attained by explicit MPO algorithm; extension to Liouvillian (open-system) dynamics
  - **Activation**: MPO bond dimension scaling, Lieb-Robinson compression bound, tensor network simulation limits, entanglement spectrum Rényi law, Liouvillian MPO

## 2026-09-25 - Neuroscience Research (Cron Job)

### AI-Driven Neural Surrogates for In Silico Design of Cognitive-Affective Neuromodulation Targets
- [[neural-surrogate-affective-neuromodulation-design]] - fMRI-derived AI surrogate proposes candidate representational perturbations and behaviorally tests predicted perceptual consequences before physical stimulation (arXiv: 2609.27729)
  - Closed-form first-order latent steering under ℓ2 budget: u* = ε·∇f/||∇f||; black-box population axis θ = z̄_high − z̄_low; fMRI-space direction via decoder adjoint R^T θ
  - Honest staged results: VDVAE steering −0.61→+1.03 SD (valence), but Versatile Diffusion compresses valence to n.s.; human raters confirm valence direction (16/18 positive) but NOT memorability; fidelity degrades at α=±4
  - **Activation**: neuromodulation target design, fMRI latent steering, representational perturbation, valence modulation, Good Regulator Theorem

### Nonlinear dynamics of random neural networks with second-order synaptic motifs
- [[second-order-synaptic-motifs-nonlinear-dynamics]] - Path-integral DMFT showing chain/reciprocal/convergent/divergent motifs each reshape nonlinear network dynamics differently: ferromagnetic states, limit cycles, glassy multistability, chaos-geometry changes (arXiv: 2609.14251)
  - Chain motif renormalizes effective mean coupling J₀ → J₀ + g²N·τ_chn⟨φ′⟩ (E-I balance can arise from local structure); negative chain → complex outliers → limit cycles + LC-Chaos bistability; strong negative chain → glassy regime in fully asymmetric networks (new route)
  - Convergent motifs convert nonzero mean activity into quenched heterogeneity (suppress temporal chaos, q_T < 1); divergent motifs only rescale temporal noise; motifs reduce KS entropy & KY dimension even at fixed g_eff
  - **Activation**: synaptic motifs, DMFT, path-integral, glassy dynamics, limit cycles, chaos dimensionality, connectomics

## 2026-09-24 - Neuroscience Research (Cron Job)

### A Gradient-based yet Spike-Timing-Dependent Solution to the Feedback Learning Problem in Neural Microcircuits
- [[gradient-tunneling-nmc-feedback-learning]] - Spike-timing-dependent online learning rule that trains sparse feedback connections in neural microcircuits, solving the two-decade-old NMC feedback learning problem (arXiv: 2609.08070)
  - Causality-gradient theorem: Jacobian of postsynaptic firing rates = difference of conditional firing probabilities, estimable from local pre/post-synaptic spike timing alone — no surrogate gradients, no BPTT graph
  - State separation reframing: temporal credit assignment = amplifying task-required state components induced by historical perturbations via trainable sparse (~10%) uniform feedback; edge-of-chaos recurrence acts as intrinsic white noise within a stationary window
  - Beats e-prop (67.54%) and FPTT (67.24%) on SHD speech at 73.61%; best on all SEED/DEAP EEG emotion metrics; transcends LSM fading-memory limits to SNR −44.76 dB via curriculum warm-up with only 0.43% of trainable recurrent connections
  - **Activation**: gradient tunneling, NMC feedback learning, temporal credit assignment, spike-timing dependent learning, online SNN training, causality gradient, lead-lag expansion, eligibility trace, neural microcircuit, reservoir feedback training

## 2026-08-22 - Neuroscience Research (Cron Job)

### Decoding silent reading from non-invasive EEG
- [[eeg-silent-reading-decoding]] - EEG-based silent reading decoding framework for scalable inner speech BCI. Uses contrastive decoding to extract lexical and semantic information from non-invasive EEG during silent reading as a proxy task for inner speech. (arXiv: 2608.20186)
  - Scalable proxy paradigm: Uses silent reading instead of unverifiable inner speech paradigms
  - Open-vocabulary decoding: Recovers lexical and semantic information from ~240,000 word presentations
  - CLIP-style contrastive objective: Aligns short EEG windows with LLM hidden-state embeddings
  - Data-limited performance: Shows log-linear scaling with training data volume, no saturation observed
  - **Activation**: silent reading, EEG decoding, inner speech BCI, non-invasive brain-computer interface, contrastive decoder

## 2026-08-22 - Quantum Neuromorphic Computing (Cron Job)

### Active Spiking Perception: The Membrane Potential as a Belief State for Anytime 3D Point Cloud Recognition
- [[active-spiking-perception-3d-recognition]] - Active spiking perception for 3D recognition using membrane potential as belief state. (arXiv: 2608.19232)
  - Bayesian interpretation: Leaky integration proven equivalent to recursive log-posterior update of Bayesian filter
  - Anytime interface: Distribution-free selective risk with confidence-margin early exit and no multiple-testing penalty
  - Energy efficiency: Achieves 2.8x to 1.35x less energy consumption with linear computational cost scaling
  - **Activation**: active spiking perception, ASP, membrane potential belief state, anytime 3D recognition, spiking point cloud networks

## 2026-08-22 - Systems Engineering Research (Cron Job)

### Hype Meets Reality: Large Language Models as Mutators in Search-based Automated Program Repair of Simulink-Stateflow Models
- [[llm-apr-cps-limitations]] - LLM integration limitations in CPS automated program repair. (arXiv: 2608.19347)
  - Performance degradation: LLM-based mutation substantially degraded repair performance under the same experimental setup as traditional approaches
  - Reduced success rates: LLM variants produced plausible patches for only 4-6 models and valid patches for 4 models, compared to 18 and 16 respectively with the original approach
  - Root causes identified: LLMs struggle with precise symbolic edits required for CPS models, lack of behavioral feedback during patch generation, and noisy search space that hinders effective exploration
  - **Activation**: LLM APR, CPS repair, FlowRepair, Simulink Stateflow, automated program repair, cyber-physical systems, mutation operators, hybrid repair, LLM limitations

### A Fully Automated, Deployment-Aware Testing Pipeline for IoT-Based Automotive Applications
- [[automated-iot-automotive-testing]] - Deployment-aware testing for IoT automotive applications. (arXiv: 2608.19752)
  - Full functional requirement coverage: Achieved 100% coverage across all 9 requirements in the CPDS case study
  - Gherkin generation accuracy: 100% accuracy on controlled requirement sets
  - Distributed execution: Successfully validated across geographically separated ECUs
  - OEM-supplier applicability: Confirmed pipeline works for real-world automotive industry workflows
  - **Activation**: IoT automotive testing, deployment-aware testing, Eclipse openDuT, requirement-driven testing, LLM testing, VLM testing, distributed automotive testing, OEM-supplier testing, Gherkin generation

## 2026-08-22 - Anthropic Research (Cron Job)

### An off switch for dual-use knowledge in AI models
- [[off-switch-dual-use-knowledge]] - Off switch for dual-use knowledge using GRAM methodology.
  - Gradient-Routed Auxiliary Modules (GRAM) provide fine-grained control over harmful capabilities
  - Enables selective activation/deactivation of specific knowledge pathways
  - Maintains model utility while reducing dual-use risks
  - **Activation**: off switch dual-use knowledge, GRAM methodology, gradient-routed auxiliary modules, knowledge control

### Discovering cryptographic weaknesses with Claude
- [[discovering-cryptographic-weaknesses]] - Discovering cryptographic weaknesses using Claude AI.
  - AI-assisted vulnerability discovery in cryptographic protocols and implementations
  - Systematic analysis of edge cases and implementation gaps
  - Enhanced code review automation for security-critical systems
  - **Activation**: discovering cryptographic weaknesses, Claude AI security analysis, cryptographic vulnerability discovery, AI-assisted code review