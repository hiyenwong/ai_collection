# Paper Summary: Subjective Functions (arXiv:2512.15948)

## Core Contribution
This paper introduces a mathematical framework for modeling subjective experiences as emergent properties of neural processes. It proposes that subjective functions—higher-order objective functions endogenous to the agent—can be modeled using principles from predictive coding and integrated information theory.

## Key Concepts

### Subjective Functions
- Defined as higher-order objective functions that emerge from an agent's internal structure
- Map neural states to qualitative experiences
- Contrast with externally imposed objective functions

### Expected Prediction Error as Subjective Function
- Proposes that expected prediction error (a key concept in predictive coding) serves as a concrete subjective function
- Links subjective surprise to neural prediction errors
- Formalized as: S(z) = E[p(s|z)][-log p(s|z)] where z is neural state and s is sensory input

### Variational Principle for Inference
- Provides a method to infer subjective functions from neural data
- Uses evidence lower bound (ELBO) optimization
- Enables estimation of subjective processes from objective measurements

## Mathematical Framework

### Subjective Function Definition
```
S(z) = 𝔼[p(s|z)] [-log p(s|z)]
```
where the expectation is over the likelihood p(s|z).

### Variational Objective
```
L = 𝔼[q(z|x)] [log p(x|z)] - KL[q(z|x) || p(z)]
```
where x represents neural observations and z represents latent states including subjective components.

### Prediction Error Dynamics
```
ε = x - g(z)
ż = f(z) + Kε
```
where ε is prediction error, g is observation function, f is dynamics, and K is Kalman gain.

## Applications
- Modeling relationship between neural activity and subjective experience
- Developing AI systems with endogenous goal formation
- Analyzing perceptual bistability and decision hysteresis
- Bridging objective neural measurements with subjective reports
- Studying consciousness in biological and artificial systems

## Validation Approaches
1. Predictive Validity: Test if model predicts future neural activity better than baselines
2. Construct Validity: Verify correlation with independent subjective reports
3. Predictive Novelty: Confirm prediction of novel phenomena like perceptual bistability
4. Parameter Interpretability: Ensure inferred parameters map to known neural mechanisms

## Extensions
- Hierarchical subjective functions for multi-level processing
- Integration with reinforcement learning frameworks
- Application to artificial neural networks for machine consciousness
- Extension to social cognition and theory of mind

## Reference
Gershman, S. J. (2025. Subjective functions. Subjective functions. arXiv:2512.15948.