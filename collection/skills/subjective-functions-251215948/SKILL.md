---
name: subjective-functions-251215948
description: A skill for modeling subjective experiences as emergent properties of neural processes based on the mathematical framework of subjective functions. Use this skill when you need to bridge objective neural measurements with subjective reports, model endogenous objective functions, or study consciousness in biological and artificial systems.
---

# Subjective Functions (arXiv:2512.15948)

## Overview
This skill implements the mathematical framework for modeling subjective experiences as emergent properties of neural processes. It introduces the concept of subjective functions—higher-order objective functions that are endogenous to the agent (defined with respect to the agent's features rather than external tasks). The core idea is that expected prediction error can serve as a concrete example of a subjective function, linking subjective experience to neural processing through principles of integrated information theory and predictive coding.

## When to Use This Skill
- Modeling the relationship between neural activity and subjective experience
- Developing AI systems with endogenous goal formation
- Analyzing perceptual bistability and decision hysteresis phenomena
- Bridging objective neural measurements with subjective reports
- Studying consciousness in biological and artificial systems
- Applying variational principles to infer subjective functions from neural data

## Core Concepts

### Subjective Functions
A subjective function is a higher-order objective function that emerges from an agent's internal structure rather than being imposed externally. It maps neural states to qualitative experiences.

### Expected Prediction Error as a Subjective Function
The paper proposes that expected prediction error—a key concept in predictive coding—can serve as a concrete subjective function. This links subjective surprise to neural prediction errors.

### Variational Principle for Inference
The framework includes a variational principle for inferring subjective functions from neural data, enabling the estimation of subjective processes from objective measurements.

### Applications to Perception and Decision-Making
The model predicts phenomena like perceptual bistability and decision hysteresis, which can be validated with electrophysiological and behavioral data.

## Workflow

### 1. Define the Neural State Space
- Identify relevant neural features or activities
- Establish the dynamical system governing neural state evolution
- Specify observation models linking neural states to measurable signals

### 2. Formulate the Subjective Function
- Define the subjective function as a mapping from neural states to subjective values
- For expected prediction error: E[error] = ∫ p(sensorium|neural state) × surprise(sensorium) dsensorium
- Parameterize the subjective function based on neural mechanisms

### 3. Apply the Variational Principle
- Use neural data to infer parameters of the subjective function
- Maximize the evidence lower bound (ELBO) for the subjective model
- Validate inferred subjective functions against subjective reports

### 4. Predict and Validate Phenomena
- Simulate the model to predict perceptual bistability or decision hysteresis
- Compare predictions with electrophysiological and behavioral data
- Refine the model based on empirical validation

## Key Equations

### Subjective Function Definition
```
S(z) = E[p(s|z)] [ -log p(s|z) ]
```
where z is neural state, s is sensory input, and the expectation is over the likelihood.

### Variational Objective
```
L = E[q(z|x)] [ log p(x|z) ] - KL[q(z|x) || p(z)]
```
where x represents neural observations, z represents latent states including subjective components.

### Prediction Error Dynamics
```
ε = x - g(z)
ż = f(z) + Kε
```
where ε is prediction error, g is observation function, f is dynamics, and K is Kalman gain.

## Implementation Notes

### Data Requirements
- Neural time series data (EEG, fMRI, single-unit recordings)
- Behavioral measures (reaction times, choices)
- Subjective reports (when available for validation)

### Computational Considerations
- The variational inference can be implemented using variational autoencoders or variational Bayes
- For large-scale neural data, consider variational approximations or sampling methods
- The framework can be combined with deep learning for feature extraction from raw neural signals

## Validation Approaches
1. **Predictive Validity**: Test whether the model predicts future neural activity better than baseline models
2. **Construct Validity**: Verify that the subjective function correlates with independent subjective reports
3. **Predictive Novelty**: Confirm that the model predicts novel phenomena like perceptual bistability
4. **Parameter Interpretability**: Ensure that inferred parameters map to known neural mechanisms

## Extensions
- Hierarchical subjective functions for multi-level processing
- Integration with reinforcement learning frameworks
- Application to artificial neural networks for machine consciousness
- Extension to social cognition and theory of mind

## References
- Gershman, S. J. (2025). Subjective functions. arXiv:2512.15948.
- Friston, K. (2010). The free-energy principle: a unified brain theory? Nature Reviews Neuroscience.
- Seth, A. K. (2013). Interoceptive inference, emotion, and the embodied self. Trends in Cognitive Sciences.
- Seth, A. K., & Hohwy, J. (2022). Predictive processing and the self. Trends in Cognitive Sciences.