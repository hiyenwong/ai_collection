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