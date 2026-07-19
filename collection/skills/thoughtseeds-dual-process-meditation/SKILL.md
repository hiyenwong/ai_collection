---
name: thoughtseeds-dual-process-meditation
description: "Computational phenomenology of focused-attention meditation as a dual-process active inference model with thoughtseeds as latent causes"
metadata:
  arxiv_id: "2607.14833"
  authors: ["Prakash Chandra Kavi", "Daniel Ari Friedman", "Gustavo Patow"]
  submitted: "2026-07-16"
  comments: "29 pages including Supplementary section. 10 figures"
  subjects: ["Neurons and Cognition (q-bio.NC)"]
license: Complete terms in LICENSE.txt
---

# Thoughtseeds as Latent Causes: A Dual-Process Computational Phenomenology of Focused-Attention Meditation

This skill implements the computational framework from arXiv:2607.14833 for modeling focused-attention meditation as a dual-process active inference system with three-layer nested Markov-blanket architecture.

## Core Methodology

The model implements a three-layer nested Markov-blanket architecture:

### Layer 1 (L1): Physiological Neuronal Substrate
- High-dimensional physiological neuronal substrate modeled as a stochastic multivariate Ornstein--Uhlenbeck process
- Operates over attentional Yeo networks (7-network parcellation of cerebral cortex)
- Represents the biological substrate of attentional dynamics

### Layer 2 (L2): Low-Dimensional Generative Model (System 1)
- Encodes latent mental content as thoughtseeds
- Evaluates autonomic action tendencies
- Represents intuitive, automatic processing (System 1 in dual-process theory)
- Thoughtseeds are discrete latent causes that generate patterns of neural activity

### Layer 3 (L3): Agentic Metacognitive Monitor (System 2)
- Implements a Global Neuronal Workspace (GNW) capacity bottleneck
- Selectively gates autonomic tendencies from L2
- Meta-awareness functions as the GNW ignition signal
- Derived from policy-prior divergence
- Dynamically gated by competition between orchestrator and distractor thoughtseeds

## Key Mechanisms

1. **Policy Selection**: Actively minimizes expected free energy
2. **Descending Predictions**: L2 actions furnish descending predictions over network activity
3. **Enactive Perception-Action Cycle**: Closed through L2 → network activity predictions
4. **Training**: Uses variational Expectation-Maximization (EM) across expert and novice phenotypes
5. **Attractor States**: Four attractor states in meditation dynamics:
   - Breath focus
   - Mind-wandering
   - Meta-awareness
   - Redirect attention

## Implementation Steps

1. **Define Attentional Networks**: Implement Yeo 7-network parcellation (Visual, Somatomotor, Dorsal Attention, Ventral Attention, Limbic, Frontoparietal, Default Mode)
2. **Model L1 Dynamics**: Implement multivariate Ornstein-Uhlenbeck process for neuronal substrate
3. **Define Thoughtseed Space**: Create discrete latent variable space for mental content representations
4. **Implement L2 Generative Model**: Map thoughtseeds to autonomic action tendencies and neural predictions
5. **Implement L3 GNW Mechanism**: 
   - Policy-prior divergence calculation for meta-awareness signal
   - Competitive gating between orchestrator/distractor thoughtseeds
   - Capacity-limited global broadcasting
6. **Implement Active Inference Loop**:
   - Action selection via expected free energy minimization
   - Prediction error minimization across hierarchical levels
   - Perception-action cycle closure
7. **Train with EM Algorithm**: 
   - E-step: Infer posterior over hidden states (thoughtseeds, neuronal states)
   - M-step: Update model parameters to maximize expected free energy
   - Train separately on expert vs. novice meditator phenotypes

## Validation Procedures

1. **Behavioral Validation**: 
   - Simulate reaction times to probe stimuli during different meditation states
   - Compare with empirical data from meditation studies
   - Validate reaction time distributions during breath focus vs. mind-wandering

2. **Neurophysiological Validation**:
   - Simulate EEG/MEG power spectra across frequency bands
   - Compare with empirical meditation neurophysiology
   - Validate alpha power increases during focused attention
   - Validate theta increases during meditative states

3. **Phenomenological Validation**:
   - Simulate first-person report distributions
   - Compare with phenomenological surveys of meditation experience
   - Validate prevalence of reported mental states (focus, wandering, meta-awareness)

4. **Individual Differences Validation**:
   - Simulate expert vs. novice differences
   - Validate with longitudinal meditation training studies
   - Check for increased meta-awareness frequency with practice

## Pitfalls and Limitations

1. **Model Complexity**: The three-layer hierarchical structure requires careful parameter tuning
2. **Thoughtseed Granularity**: Choosing appropriate resolution for latent mental state space
3. **Yeo Network Limitations**: 7-parcellation may not capture fine-grained attentional dynamics
4. **OU Process Assumption**: Ornstein-Uhlenbeck may not fully capture neural dynamics complexity
5. **GNW Implementation**: Simplified global workspace may not capture full consciousness complexity
6. **EM Convergence**: Variational EM may get stuck in local optima for complex landscapes
7. **Parameter Identifiability**: Multiple parameter sets may produce similar behavioral outputs
8. **Empirical Validation Data**: Requires multimodal datasets (behavioral + neurophysiological + phenomenological)

## Execution Guidelines

When applying this model to meditation research:

1. **Parameter Initialization**:
   - L1: Set OU parameters based on empirical resting-state functional connectivity
   - L2: Initialize thoughtseed space dimensionality based on phenomenological categories
   - L3: Set GNW capacity based on working memory capacity estimates (~4 chunks)

2. **Training Protocol**:
   - Collect multi-session meditation data (behavioral, EEG, phenomenological reports)
   - Use variational EM to fit individual subject parameters
   - Validate hierarchical model comparison (1-layer vs 2-layer vs 3-layer)

3. **Analysis Focus**:
   - Extract latent timescales from hierarchical timescales of each layer
   - Analyze thoughtseed transition matrices during meditation
   - Quantify meta-awareness ignition events as policy-prior divergence peaks
   - Measure orchestrator-distractor competition strength

## Applications

1. **Meditation Training Optimization**: Identify optimal training parameters for developing meta-awareness
2. **Clinical Applications**: Model attentional dysregulation in ADHD, anxiety, depression
3. **Brain-Computer Interfaces**: Develop neurofeedback protocols based on latent state dynamics
4. **Artificial Intelligence**: Implement artificial mindfulness in artificial agents
5. **Theoretical Integration**: Bridge contemplative neuroscience with active inference frameworks

## Verification

This skill implements the exact framework described in:
- arXiv:2607.14833 "Thoughtseeds as Latent Causes: A Dual-Process Computational Phenomenology of Focused-Attention Meditation"
- Submitted: 2026-07-16
- Comments: 29 pages including Supplementary section. 10 figures
- Subjects: Neurons and Cognition (q-bio.NC)

## Activation Keywords

- thoughtseeds
- dual-process
- meditation
- active inference
- global neuronal workspace
- latent causes
- attentional networks
- ornstein-uhlenbeck
- variational EM
- meta-awareness
- policy-prior divergence