---
name: functional-whole-brain-models-fwbm
description: "Functional Whole-Brain Models (fWBMs) - unified modeling paradigm integrating bottom-up whole-brain modeling with top-down neuroconnectionism. Defines 4 minimal criteria and 3-pillar roadmap for unifying brain structure and cognitive function. Based on arXiv:2605.18118 (May 2026). Use when studying whole-brain modeling, neural mass models, brain-inspired DNN architectures, connectome-based modeling, or cross-scale brain computation frameworks."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.18118"
  published: "2026-05-18"
  authors: "Mario Senden, Leonardo Dalla Porta, Jan Fousek, Jorge F. Mejias, Gorka Zamora-López"
  categories: [q-bio.NC, q-bio.q-bio]
  tags: [whole-brain-modeling, neuroconnectionism, functional-whole-brain-models, neural-mass-models, connectome, brain-dynamics, cognitive-modeling, continuous-time-dynamics, brain-inspired-ai, computational-neuroscience]
---

# Functional Whole-Brain Models (fWBMs): A Framework for Unifying Brain Structure and Cognitive Function

**Source:** arXiv:2605.18118 (q-bio.NC), published 2026-05-18  
**Authors:** Mario Senden, Leonardo Dalla Porta, Jan Fousek, Jorge F. Mejias, Gorka Zamora-López

## Description

This skill provides the methodology, criteria, and roadmap for constructing **Functional Whole-Brain Models (fWBMs)** — a new modeling paradigm that unifies two traditionally disconnected approaches in computational neuroscience: bottom-up biophysical whole-brain modeling (WBM) and top-down task-optimized neuroconnectionism. fWBMs define a class of models that simultaneously satisfy structural grounding, continuous-time dynamical realism, functional competence, and mappable observables. This skill is intended for researchers building brain models that bridge structure and function, designing brain-inspired AI architectures, or developing clinical tools for brain disorders.

---

## 1. The Problem: Two Complementary but Disconnected Traditions

Contemporary computational neuroscience features two highly successful yet disconnected modeling traditions.

### 1.1 Bottom-Up Whole-Brain Modeling (WBM)

WBMs start from empirical neuroanatomy — structural connectomes derived from diffusion MRI, histological tracing, or other modalities — and simulate large-scale neural dynamics using biophysically realistic neural mass or mean-field models at each node.

**Strengths:**
- Biophysically grounded: parameters map to known physiology (e.g., synaptic strengths, ion channel densities)
- Realistic dynamics: captures resting-state fMRI functional connectivity, spontaneous fluctuations, metastability
- Clinically relevant: can simulate structural perturbations (lesions, degeneration, stimulation)

**Limitations:**
- Lacks functional competence: cannot perform cognitive tasks
- Optimized for dynamics, not computation: no notion of task goals, inputs, or outputs
- Validation restricted to resting-state correlations with empirical neuroimaging

### 1.2 Top-Down Neuroconnectionism

Neuroconnectionist models (a term encompassing deep neural networks trained on cognitive tasks) are optimized purely for functional performance.

**Strengths:**
- Functional competence: excel at vision, language, navigation, working memory
- Task-aligned representations: learned representations correlate with neural data
- Mechanistic interpretability: can analyze how computations emerge from network dynamics

**Limitations:**
- Limited biological grounding: typically use spatially uniform, layer-wise architectures
- Discrete processing: information propagates through discrete layers, not continuous-time dynamics
- Task-specific: different architectures for different tasks, lack unified whole-brain framework

### 1.3 The Gap

The key observation: WBMs capture *where* and *how* brain activity emerges from structure, while neuroconnectionist models capture *what* the brain computes. Neither alone provides a complete account of brain function. fWBMs are proposed as the bridge.

---

## 2. Four Minimal Criteria for fWBMs

A model qualifies as a **Functional Whole-Brain Model (fWBM)** if and only if it satisfies all four of the following criteria:

### Criterion 1: Structural Grounding

The model must incorporate empirically derived brain structure at multiple scales:

- **Macroscale connectome:** Structural connectivity derived from diffusion MRI tractography, polarized light imaging (PLI), or histological tract tracing, typically represented as a weighted adjacency matrix between brain regions (e.g., parcellated into 100-1000 nodes)
- **Regional biology:** Biophysically meaningful node models that incorporate region-specific properties (e.g., cortical vs. subcortical differences, laminar structure, receptor densities)
- **Spatial embedding:** White matter tract lengths, conduction delays, and distance-dependent connectivity constraints

**Implementation forms:**
- Diffusion MRI + tractography → structural connectivity matrix
- Histological atlases (e.g., Allen Brain Atlas, BigBrain) → regional gene expression, cytoarchitecture
- Receptor/neurotransmitter maps → regional heterogeneity in neural dynamics

### Criterion 2: Continuous-Time Dynamical Realism

The model must employ continuous-time dynamical systems, not discrete processing layers:

- **Neural mass models (NMMs):** Mean-field reductions of local populations (excitatory/inhibitory), e.g., Jansen-Rit, Wong-Wang, reduced FitzHugh-Nagumo
- **Neural field models:** Spatially continuous extensions capturing wave propagation
- **Conduction delays:** Axonal transmission delays between regions based on tract lengths and conduction velocities
- **Recurrent dynamics:** Within- and between-region recurrent connectivity enabling attractor dynamics, oscillations, and transient computation

**Key requirement:** Information processing must emerge from ongoing dynamics, not from feedforward layer-by-layer computation. The model should exhibit spontaneous activity, multistability, and sensitivity to initial conditions — hallmarks of biological neural systems.

### Criterion 3: Functional Competence

The model must be capable of performing cognitive tasks across one or more domains:

- **Task input:** Task-relevant stimuli must be able to drive the model's dynamics (e.g., visual input to occipital nodes, tactile input to somatosensory nodes)
- **Task readout:** Behavioral outputs (e.g., decision, motor response) must be decodable from model activity
- **Cognitive domains:**
  - Working memory (parametric, spatial, verbal)
  - Decision-making (perceptual, value-based, multi-attribute)
  - Attention (spatial, feature-based, executive control)
  - Learning and plasticity (supervised, reinforcement, unsupervised)
  - Language processing (at the level of word/phrase representations)
  - Navigation and spatial cognition

**Evaluation:** Performance metrics matched to human/animal behavioral benchmarks. The model should capture not just accuracy but also reaction times, error patterns, and cognitive biases.

### Criterion 4: Mappable Observables

The model must generate predictions that can be directly compared to empirical measurements:

- **BOLD fMRI:** Hemodynamic forward models (e.g., Balloon-Windkessel model) convert neural activity to simulated BOLD signals for resting-state and task-based comparisons
- **EEG/MEG:** Electromagnetic forward models project neural currents to sensor-level signals, enabling comparison of evoked potentials, spectral power, and connectivity
- **Electrophysiology:** Local field potentials (LFPs), multi-unit activity (MUA), and single-unit spiking activity
- **Behavioral data:** Reaction times, response choices, eye movements, and other behavioral readouts
- **Lesion/degeneration simulations:** Structural perturbations to test causal predictions against clinical data

**Validation approach:**
- Resting-state: functional connectivity (FC) matrices, dynamic FC, metastability measures
- Task-based: evoked responses, representational similarity analysis (RSA), encoding models
- Perturbation: compare simulated lesion effects to patient data or pharmacological interventions

---

## 3. Three-Pillar Roadmap

The paper outlines a phased roadmap spanning short, mid, and long-term horizons.

### 3.1 Short-Term Horizon (Immediately Feasible)

**Goal:** Demonstrate feasibility by integrating existing components.

| Action | Description | Current Status |
|--------|-------------|----------------|
| Simple task modules + existing WBMs | Add minimal task inputs and readouts to existing biophysical models (e.g., threshold-based decisions in TheVirtualBrain) | Multiple groups already have proofs of concept |
| Structural-functional benchmarks | Develop standardized benchmarks that jointly evaluate structural fidelity and task performance | Gap: no consensus benchmarks exist |
| Common validation protocols | Establish shared pipelines for comparing fWBMs across labs (standardized preprocessing, null models, statistics) | Adapt existing neuroimaging analysis workflows |
| Open-source repositories | Create shared code repositories with modular, extensible fWBM frameworks | TheVirtualBrain (TVB) serves as natural platform |

**Immediate low-hanging fruit:**
- Add a perceptual decision-making module to a resting-state WBM: present sensory evidence to sensory regions, accumulate evidence in decision-related areas (e.g., parietal), read out decision when threshold crossing occurs
- Implement working memory in a spiking neural mass model using sustained activity in prefrontal cortex nodes

### 3.2 Mid-Term Horizon (3-7 Years)

**Goal:** Build hybrid models with learned task components grounded in realistic dynamics.

| Action | Description | Key Challenge |
|--------|-------------|---------------|
| Hybrid parameter optimization | Use gradient-based methods (e.g., backpropagation through time, BPTT) to optimize task-relevant parameters while constraining biophysical realism | Differentiable simulation of biophysical models |
| Cross-scale linking hypotheses | Develop formal relationships between microscopic (synaptic, cellular), mesoscopic (columnar, areal), and macroscopic (whole-brain, behavioral) variables | Bridging the scales is the hardest open problem |
| Shared software infrastructure | Build modular, composable frameworks where structural connectomes, node models, task modules, and forward models can be mixed and matched | Interoperability between different codebases |
| Multi-task training | Train a single fWBM on multiple cognitive tasks simultaneously to test for emergent task-general representations | Catastrophic forgetting, capacity limits |

**Key enabler:** Differentiable neural mass models — enabling gradient-based optimization of synaptic weights, time constants, and connectivity parameters while preserving biophysical realism. This links neuroconnectionist learning to WBM realism.

### 3.3 Long-Term Horizon (10+ Years)

**Goal:** Realize fully unified fWBMs with biophysical realism and multi-domain cognitive capability.

| Action | Description |
|--------|-------------|
| Fully unified fWBMs | Models that satisfy all four criteria at scale: whole-brain realism, multiple cognitive domains, and comprehensive empirical validation |
| Clinical translation | fWBMs as digital twins for individual patients: predict how structural pathology (trauma, neurodegeneration, neurodevelopmental disorders) translates to cognitive deficits |
| Stimulation optimization | Closed-loop optimization of brain stimulation targets and protocols (TMS, tDCS, DBS) using personalized fWBMs |
| Developmental modeling | Track and simulate structural-functional coupling across development, aging, and learning |
| Theory building | Use fWBMs as in silico laboratories to test foundational theories of neural computation: predictive coding, free energy principle, dynamic causal models |

**Ultimate vision:** An fWBM trained on the same tasks humans perform, grounded in a subject-specific connectome, generating dynamics that match the subject's fMRI/EEG, and capable of predicting the cognitive effects of structural changes.

---

## 4. Scientific and Clinical Opportunities

### 4.1 Brain Disorders and Clinical Neuroscience

| Application | Approach |
|-------------|----------|
| **Neurodegeneration** (Alzheimer's, Parkinson's) | Seed structural pathology in specific regions, simulate spread along connectome, predict cognitive deficits at each stage |
| **Psychiatric disorders** (schizophrenia, depression, autism) | Alter regional excitability/inhibition balance, simulate effects on large-scale dynamics and task performance |
| **Stroke and traumatic brain injury** | Remove or degrade specific nodes/connections, predict functional compensation and recovery trajectories |
| **Neurodevelopmental disorders** (ADHD, dyslexia) | Simulate altered developmental trajectories with regionally specific structural differences |
| **Epilepsy** | Model seizure propagation dynamics and test surgical resection strategies in silico |

### 4.2 Brain Stimulation Optimization

| Modality | fWBM Contribution |
|----------|-------------------|
| **Transcranial Magnetic Stimulation (TMS)** | Predict downstream effects of focal stimulation; optimize frequency, intensity, and target |
| **Transcranial Direct Current Stimulation (tDCS)** | Model current spread and network-level neuromodulation |
| **Deep Brain Stimulation (DBS)** | Test electrode placement and stimulation parameters for movement and psychiatric disorders |

### 4.3 Cognitive Science and Systems Neuroscience

| Opportunity | Description |
|-------------|-------------|
| **Mechanistic hypothesis testing** | Test competing theories of cognitive function (e.g., is working memory maintained by persistent activity or activity-silent synaptic traces?) in the same whole-brain model |
| **Structural-functional coupling** | Quantify how much of functional connectivity is explained by structural connectivity vs. task demands |
| **Causal inference** | Perform in silico lesion experiments impossible in humans: selective inactivation of specific connections or cell types |
| **Individual differences** | Link individual variation in connectome structure to variation in cognitive performance |
| **Comparative neuroscience** | Build connectome-specific fWBMs for different species to study evolution of cognitive capacity |

### 4.4 Artificial Intelligence

| Opportunity | Description |
|-------------|-------------|
| **Brain-inspired architectures** | Extract design principles from fWBMs: continuous-time recurrent computation, spatial embedding, conduction delays, and noise |
| **Energy efficiency** | Spiking network implementations of fWBMs can inform neuromorphic computing |
| **Robustness** | Biological noise and degenerate solutions may inspire more robust AI systems |
| **Lifelong learning** | Structural plasticity mechanisms in fWBMs may inform continual learning approaches |

---

## 5. Implementation Methodology

### 5.1 Architecture Components

A complete fWBM implementation requires these composable modules:

```
fWBM = StructuralConnectome + NodeModel + TaskInterface + ForwardModel
```

1. **StructuralConnectome:** Adjacency matrix (N×N) with optional edge weights (tract count, fractional anisotropy), tract lengths, and inter-region conduction delays
2. **NodeModel:** Per-region dynamical system, either:
   - **Neural mass models:** Reduced population models (e.g., Wong-Wang for excitatory/inhibitory, Jansen-Rit for cortical columns)
   - **Mean-field models:** Single-population reduction (e.g., reduced FitzHugh-Nagumo, Kuramoto oscillators)
   - **Spiking models:** Izhikevich, AdEx, or Hodgkin-Huxley neurons (more computationally expensive)
   - **Hybrid models:** Different node types for different regions (e.g., thalamic nodes use different dynamics than cortical nodes)
3. **TaskInterface:** Input encoding (how stimuli enter the model) and output decoding (how behavior is read from model activity)
   - Input: stimulus features → regional activation patterns
   - Output: activity from task-relevant regions → decision/response classifier
4. **ForwardModel:** Mapping from neural activity to observable signals
   - Hemodynamic (Balloon-Windkessel → BOLD)
   - Electromagnetic (lead-field → EEG/MEG)

### 5.2 Model Design Decisions

| Decision | Options | Trade-off |
|----------|---------|-----------|
| Node model complexity | Spiking → NMM → reduced NMM | Biophysical detail vs. computational tractability |
| Connectome resolution | 100 → 1000+ nodes | Anatomical detail vs. parameter identifiability |
| Delay inclusion | Zero-delay → realistic delays | Accuracy vs. simulation stability |
| Noise | None → Poisson → Ornstein-Uhlenbeck | Biological realism vs. signal-to-noise ratio |
| Learning | Fixed weights → Hebbian → BPTT | Biological plausibility vs. functional performance |

### 5.3 Training and Optimization Pipeline

1. **Initialize** with empirical structural connectome and standard biophysical parameters
2. **Validate resting-state dynamics** — ensure spontaneous activity matches empirical FC, power spectra, and metastability measures
3. **Inject task structure** — add input encoding and output decoding mechanisms
4. **Optimize task parameters** — adjust local parameters (synaptic strengths, time constants, thresholds) to achieve task performance
5. **Validate task activity** — compare simulated task-evoked responses to empirical neuroimaging data
6. **Iterate** — structural parameters may also be adjusted within plausible bounds

### 5.4 Key Computational Tools

| Tool | Purpose |
|------|---------|
| **TheVirtualBrain (TVB)** | Established platform for large-scale WBM simulations; natural candidate for fWBM extension |
| **NEST / Brian2** | Spiking network simulators for detailed node models |
| **PyTorch / JAX** | Automatic differentiation for gradient-based optimization of task parameters |
| **DiffEq libraries** (torchdiffeq, Diffrax) | Differentiable ODE solvers enabling BPTT through neural mass dynamics |
| **NiBabel / Nilearn** | Neuroimaging data loading, manipulation, and analysis |

---

## 6. Evaluation Metrics and Benchmarking

### 6.1 Structural Fidelity Metrics

| Metric | Description |
|--------|-------------|
| **Structural connectome similarity** | Correlation between model connectome and empirical connectome |
| **Regional property matching** | Distribution of node model parameters matches empirical distribution (e.g., cortical thickness, myelination) |

### 6.2 Dynamical Fidelity Metrics

| Metric | Description |
|--------|-------------|
| **Functional connectivity (FC) correlation** | Pearson/Spearman correlation between simulated and empirical FC matrices |
| **Edge functional connectivity (eFC)** | Distribution of pairwise correlations between regions |
| **Dynamic FC (dFC)** | Sliding-window FC variability, metastability index |
| **Power spectra** | Band-limited power (delta, theta, alpha, beta, gamma) across regions |
| **Functional connectivity dynamics (FCD)** | Second-order FC: correlation between FC states over time |
| **Graph-theoretic measures** | Small-worldness, modularity, hub structure, rich-club organization |

### 6.3 Functional Performance Metrics

| Metric | Description | Example |
|--------|-------------|---------|
| **Task accuracy** | Percent correct on cognitive tasks | Perceptual decision: % correct choices |
| **Reaction times (RT)** | Simulated decision latencies | Match human RT distributions |
| **RT-accuracy trade-off** | Speed-accuracy characteristic | Compare to human speed-accuracy curves |
| **Representational similarity (RSA)** | Correlation of representational geometries between model and brain | IT cortex representations vs. model activity |
| **Encoding model performance** | How well model activity predicts neural responses | Variance explained in voxel responses |
| **Lesion behavior** | Performance degradation under simulated damage | Match patient neuropsychological profiles |

### 6.4 Unification Metrics

| Metric | Purpose |
|--------|---------|
| **Structure-function coherence** | How task performance depends on structural connectome fidelity |
| **Explanatory scope** | Number of empirical phenomena (across scales and modalities) simultaneously explained |
| **Predictive validity** | Out-of-sample prediction of novel empirical findings |

---

## 7. Activation Keywords

- functional whole-brain models, fWBM, functional WBM
- whole-brain modeling, whole brain model, large-scale brain model
- neuroconnectionism, neuroconnectionist model
- brain structure-function coupling, structure-function unification
- neural mass model, mean-field model, biophysical brain model
- connectome-based modeling, connectome-informed neural network
- continuous-time brain dynamics, brain dynamical system
- brain-inspired AI, brain-grounded AI
- cognitive modeling, brain task modeling
- brain stimulation optimization, TMS modeling, DBS modeling
- brain disorder modeling, clinical brain simulation

---

## 8. Related Skills

- `multi-objective-optimisation-oscillatory-snn`: Multi-objective optimization for oscillatory spiking neural networks — complementary numerical techniques
- `adaptive-spiking-neuron-asn`: Adaptive spiking neuron implementations for vision and language — can serve as node model component
- `spiking-neural-network-analysis`: Analysis framework for SNN papers — useful for evaluating fWBM node model dynamics

---

## References

- Senden, M., Dalla Porta, L., Fousek, J., Mejias, J. F., & Zamora-López, G. (2026). Functional Whole-Brain Models: A New Framework for Unifying Brain Structure and Cognitive Function. arXiv:2605.18118 [q-bio.NC].
- Sanz-Leon, P., Knock, S. A., Spiegler, A., & Jirsa, V. K. (2015). Mathematical framework for large-scale brain network modeling. NeuroImage, 111, 385-430.
- Deco, G., Jirsa, V. K., & McIntosh, A. R. (2011). Emerging concepts for the dynamical organization of resting-state activity. Nature Reviews Neuroscience, 12(1), 43-56.
- Yamins, D. L., & DiCarlo, J. J. (2016). Using goal-driven deep learning models to understand sensory cortex. Nature Neuroscience, 19(3), 356-365.

---

## Notes

- The fWBM framework is proposal-based — no single fWBM currently satisfies all four criteria simultaneously. The roadmap lays out a phased path toward that goal.
- The four criteria are deliberately minimal: any model satisfying them qualifies, regardless of specific implementation choices.
- Short-term integrations (Criterion 1 + 2 + task input/readout) are immediately feasible with existing tools and are likely to appear in the literature within 1-2 years.
- The framework is agnostic to node model choice — spiking models, neural masses, and reduced mean-field models are all valid depending on the research question.
- For clinical applications, subject-specific connectomes from patient MRI are essential for personalized fWBMs.

*Last updated: 2026-05-26*
