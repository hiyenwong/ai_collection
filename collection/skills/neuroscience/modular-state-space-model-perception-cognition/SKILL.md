---
name: modular-state-space-model-perception-cognition
description: "A modular state-space model for human perception, cognition, and decision dynamics that links sensory inputs to behavior through latent internal states while maintaining interpretable connections to neuro-cognitive mechanisms."
metadata:
  arxiv_id: "2607.14078"
  authors: "Sven Schoonebeek, Carlo Cenedese, Anahita Jamshidnejad"
  published: "2026-07-17"
  categories: "eess.SY; cs.SY; q-bio.NC"
---

# Modular State-Space Model of Human Perception, Cognition, and Decision Dynamics

**arXiv**: 2607.14078v2 | **Published**: 2026-07-17

## Context
This paper addresses the need for behavioral models that are both psychologically interpretable and mathematically analyzable in human-centered adaptive systems. Many existing predictors operate as black-box input-output mappings or provide limited access to latent internal dynamics.

## Core Methodology
The authors propose a modular state-space model where behavior is modeled as a perception-cognition-decision pipeline. The model consists of coupled mathematical mappings representing:
1. Attentional selection
2. Predictive inference
3. Cognitive-state evolution
4. Intention formation
5. Action selection

The model links sensory inputs to observable behavior through latent internal states while retaining interpretable connections to neuro-cognitive mechanisms.

## Key Contributions
- Provides a white-box dynamical structure for estimation, validation, and model-based control in human-centered settings.
- Establishes sufficient conditions for boundedness, Lipschitz regularity, forward invariance, contraction of perceptual inference under constant input, and input-to-state stability of cognitive state dynamics.
- Demonstrates a closed-loop rehabilitation case study where a receding-horizon controller uses the model to adapt movement difficulty from partial feedback.
- Shows that the model-based controller sustains simulated task participation and achieves lower realized cumulative cost than target-following and random baselines.

## Implementation Steps
1. Define the perception-cognition-decision pipeline as a series of coupled mathematical mappings.
2. Model attentional selection, predictive inference, cognitive-state evolution, intention formation, and action selection as separate modules.
3. Link sensory inputs to observable behavior through latent internal states.
4. Ensure the model maintains interpretable connections to neuro-cognitive mechanisms.
5. Establish mathematical properties (boundedness, Lipschitz regularity, etc.) for stability and robustness.
6. Perform numerical sensitivity analysis to verify interpretable changes in perceptual tracking, cognitive amplification, intention expression, and action decisiveness.
7. Apply the model to real-world scenarios such as rehabilitation, where a receding-horizon controller adapts task difficulty based on partial feedback.

## Pitfalls
- Ensuring the model remains psychologically interpretable while being mathematically rigorous.
- Validating the model against empirical neuro-cognitive data.
- Computational complexity of estimating latent states in real-time applications.
- Balancing model complexity with interpretability.

## Verification
- Compare model predictions with empirical behavioral and neurophysiological data.
- Conduct sensitivity analyses to ensure robustness of inferred parameters.
- Validate the model-based controller in simulated and real-world rehabilitation settings.
- Assess whether the model provides insights into neuro-cognitive mechanisms that black-box models obscure.

## Activation
modular state-space model, perception-cognition-decision pipeline, human-centered modeling, computational neuroscience, brain network modeling, state-space modeling, 2607.14078