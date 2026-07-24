---
name: modular-state-space-model-260714078
description: "Model human perception, cognition, and decision dynamics as a modular perception-cognition-decision pipeline state-space model. Provides mathematical formulation, stability conditions, and application to rehabilitation control. Use when you need interpretable dynamical models linking neural mechanisms to behavior."
metadata:
  arxiv_id: "2607.14078"
  authors: ["Sven Schoonebeek", "Carlo Cenedese", "Anahita Jamshidnejad"]
  categories: ["eess.SY", "q-bio.NC", "cs.SY"]
---
# Modular State-Space Model of Human Perception, Cognition, and Decision Dynamics (arXiv:2607.14078)

## Overview
This skill encapsulates the methodology from arXiv:2607.14078 for modeling human behavior as a perception-cognition-decision pipeline using coupled state-space models. It provides the mathematical framework for attentional selection, predictive inference, cognitive-state evolution, intention formation, and action selection, linking sensory inputs to observable behavior through latent neural states. The skill includes stability analysis conditions and demonstrates application in a rehabilitation control scenario.

## Core Components

### 1. Perception-Cognition-Decision Pipeline
The model decomposes behavior into five coupled subprocesses:
- **Attentional selection**: filters sensory inputs
- **Predictive inference**: generates predictions about sensory input
- **Cognitive-state evolution**: updates internal beliefs and goals
- **Intention formation**: selects goals and prepares actions
- **Action selection**: executes motor commands

Each subprocess is represented as a state-space model with explicit input-output mappings.

### 2. Mathematical Formulation
For each subprocess \(i\), we define:
- State vector \(x_i \in \mathbb{R}^{n_i}\)
- Input \(u_i\) (from previous subsystem or sensory input)
- Output \(y_i\) (to next subsystem or behavior)
- Dynamics: \(x_{i,k+1} = A_i x_{i,k} + B_i u_{i,k} + w_{i,k}\)
- Measurement: \(y_{i,k} = C_i x_{i,k} + v_{i,k}\)

Coupling occurs through the interconnections:
- Sensory input → Attentional selection
- Attentional output → Predictive inference
- Predictive inference → Cognitive-state evolution
- Cognitive-state evolution → Intention formation
- Intention formation → Action selection → Observable behavior

### 3. Stability and Performance Properties
The paper establishes sufficient conditions for:
- **Boundedness**: states remain bounded for bounded inputs
- **Lipschitz regularity**: Lipschitz continuity of state transition maps
- **Forward invariance**: certain sets remain invariant under dynamics
- **Contraction of perceptual inference**: contraction mapping under constant input
- **Input-to-state stability (ISS)**: cognitive state dynamics are ISS with respect to inputs

These properties ensure the model is well-behaved and suitable for control applications.

### 4. Application: Rehabilitation Control
A closed-loop rehabilitation case study demonstrates:
- Using the model to predict patient motor capabilities from partial feedback
- A receding-horizon model predictive controller adjusts task difficulty
- The model-based controller sustains task participation and reduces cumulative cost compared to baseline strategies
- This illustrates how the model enables model-based control in human-centered settings

## Workflow

### Step 1: Define Subsystems
Identify the relevant subprocesses for your application (attention, prediction, cognition, intention, action) and define their state, input, and output dimensions.

### Step 2: Specify Dynamics
Choose appropriate state-space matrices (A, B, C) for each subsystem based on known neurocognitive mechanisms or identified from data.

### Step 3: Couple Subsystems
Connect the outputs of each subsystem to the inputs of the next according to the perception-cognition-decision pipeline.

### Step 4: Analyze Stability
Verify that the chosen parameters satisfy the sufficient conditions for boundedness, Lipschitz regularity, and input-to-state stability.

### Step 5: Simulate and Validate
Simulate the model with synthetic or empirical data to ensure it produces interpretable changes in perceptual tracking, cognitive amplification, intention expression, and action decisiveness.

### Step 6: Apply to Control (Optional)
Design a model-based controller (e.g., MPC) that uses the model's predictions to influence behavior, such as adapting task difficulty in rehabilitation.

## Resources

### scripts/
- `simulate_pipeline.py`: Example simulation of the coupled state-space model
- `analyze_stability.py`: Checks stability conditions for given system matrices

### references/
- `math_details.md`: Detailed derivations of the state-space equations and coupling terms
- `stability_conditions.md`: List of sufficient conditions for boundedness and ISS
- `rehabilitation_case.md`: Detailed description of the rehabilitation control experiment

### assets/
- `diagram_pipeline.png`: Block diagram of the perception-cognition-decision pipeline
- `template_controller.m`: MATLAB template for MPC controller design

## Usage Notes
- Validate subsystem dimensions before coupling
- Use numerical integration (e.g., Euler or Runge-Kutta) for simulation
- For parameter estimation, consider subspace identification or expectation-maximization
- The model is particularly useful when interpretability of latent states is required

---
**Activation**: modular state-space model, perception cognition decision, behavioral modeling, human-centered control, arXiv:2607.14078