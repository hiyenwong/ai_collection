# Paper Summary: A modular state-space model of human perception, cognition, and decision dynamics (arXiv:2607.14078)

## Core Contribution
This paper proposes a modular state-space framework for modeling human perception, cognition, and decision-making as interacting dynamical systems. Each cognitive module is modeled as a linear-Gaussian state-space system with nonlinear observation functions, interacting through bidirectional coupling terms.

## Key Concepts

### Perception-Cognition-Decision Pipeline
The model decomposes behavior into five coupled subprocesses:
1. **Attentional selection**: filters sensory inputs
2. **Predictive inference**: generates predictions about sensory input
3. **Cognitive-state evolution**: updates internal beliefs and goals
4. **Intention formation**: selects goals and prepares actions
5. **Action selection**: executes motor commands

### Mathematical Formulation
For each subsystem i:
- State vector x_i ∈ R^n_i
- Input u_i (from previous subsystem or sensory input)
- Output y_i (to next subsystem or behavior)
- Dynamics: x_{i,k+1} = A_i x_{i,k} + B_i u_{i,k} + w_{i,k}
- Measurement: y_{i,k} = C_i x_{i,k} + v_{i,k}

Coupling occurs through interconnections between subsystems in the perception-cognition-decision pipeline.

### Stability and Performance Properties
The paper establishes sufficient conditions for:
- **Boundedness**: states remain bounded for bounded inputs
- **Lipschitz regularity**: Lipschitz continuity of state transition maps
- **Forward invariance**: certain sets remain invariant under dynamics
- **Contraction of perceptual inference**: contraction mapping under constant input
- **Input-to-state stability (ISS)**: cognitive state dynamics are ISS with respect to inputs

## Applications
- Modeling human perception, cognition, and decision dynamics
- Rehabilitation control (demonstrated in paper)
- Brain-computer interfaces
- Cognitive modeling in AI systems
- Human-robot interaction

## Validation Approach
- Parameter estimation via expectation-maximization algorithms
- Validation on multiple datasets (fMRI, EEG, behavioral data)
- Demonstration of ability to reproduce cognitive phenomena:
  * Perceptual multistability
  * Memory retrieval dynamics
  * Speed-accuracy tradeoffs in decision-making
- Closed-loop rehabilitation case study showing model-based control outperforms baselines

## Extensions
- Hierarchical organization of modules
- Nonlinear extensions for complex cognitive dynamics
- Integration with machine learning for parameter identification
- Application to clinical populations and neurological disorders

## Reference
Schoonebeek, S., Cenedese, C., & Jamshidnejad, A. (2026). A modular state-space model of human perception, cognition, and decision dynamics. arXiv:2607.14078.