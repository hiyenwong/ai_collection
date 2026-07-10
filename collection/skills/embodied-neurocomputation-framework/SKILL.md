---
name: embodied-neurocomputation-framework
description: >
  Embodied Neurocomputation framework for interfacing biological neural cultures
  with scaled task-driven validation. Systems-level approach to multi-variable
  optimization of encoding/decoding between silicon computing and living biology.
  Demonstrates that biological neural networks (BNNs) can outperform DQN agents
  in goal-driven navigation when encoding parameters are properly optimized.
category: neuroscience
tags: [biological-neural-networks, neurocomputation, MEA, encoding-decoding, bio-silicon, hybrid-computing, parameter-optimization]
related_skills:
  - embodied-neurocomputation-framework
  - neural-digital-twins-bci
  - neural-brain-framework
  - energy-based-neurocomputation
activation_keywords:
  - embodied neurocomputation
  - biological neural network computing
  - MEA neurocomputation
  - bio-silicon computing
  - biological neural culture interfacing
  - cortical labs CL1
  - neural encoding optimization
---

# Embodied Neurocomputation Framework

**Paper**: *Embodied Neurocomputation: A Framework for Interfacing Biological Neural Cultures with Scaled Task-Driven Validation*
**Authors**: Johnson Zhou, Daniel Tanneberg, Forough Habibollahi, Alon Loeffler, Kiaran Lawson, Valentina Baccetti, Kwaku Dad Abu-Bonsrah, Candice Desouza, Finn Doensen, Bradley Watmuff, Daria Kornienko, Azin Azadi, Justin L. Bourke, Bernhard Sendhoff, Brett J. Kagan
**Institutions**: Cortical Labs (Australia), Honda Research Institute Europe (Germany)
**arXiv**: 2605.13315 (May 13, 2026)
**Category**: cs.ET, cs.LG, cs.NE

## Overview

This paper introduces a formal **Embodied Neurocomputation Framework** — a systems-level approach to interfacing biological neural networks (BNNs) with conventional computers via Micro-Electrode Arrays (MEAs). The framework conceptualizes the digital-biological interface as a multi-variable optimization problem across four interdependent modules: encoding, biological transformation, decoding, and feedback. It validates this through the first large-scale parameter optimization of encoding configurations for BNN agents performing closed-loop navigation.

## Core Framework

### Mathematical Formulation

Neurocomputation f at time t, with parameter set theta_t, as sequential feed-forward mappings:

```
y_t = f(x_t; theta_t) = d(b(e(x_t; theta_e); theta_b,t); theta_d)
```

Where:
- **e(x_t; theta_e)**: Encoding — transforms task information into electrical stimuli
- **b(u_t; theta_b,t)**: Biological transformation — BNN's intrinsic dynamics
- **d(v_t; theta_d)**: Decoding — transforms neural responses into task-relevant outputs
- **r(Score; theta_r)**: Feedback — drives BNN adaptation toward objectives

Biological adaptation:
```
theta_b,t+1 = g(r(Score; theta_r); theta_b,t)
```

### Four Key Modules

#### 1. Encoding (theta_e = theta_task union theta_stim)
- Transforms task-specific information into stimulation matrix u_t in {0,1}^(C x tau_in)
- **C**: stimulation channels, **tau_in**: pulse delivery time steps
- Parameters: frequency, amplitude, pulse width, waveform morphology, spatiotemporal distribution
- **Rate encoding**: sensor value -> sequence of stimulations at interpolated frequencies

#### 2. Biological Transformation (b)
- Non-stationary mapping depending on temporal structure of input
- Parameters theta_b evolve according to stimulation/response history, feedback, and spontaneous processes
- Produces *qualitative change*: reorganizes informational structure, not just scaling/filtering
- **"Third-order" information-processing system**: response depends on how previous outputs shaped transformation
- Non-invertible: reflects reorganization and compression of information

#### 3. Decoding (theta_d)
- Inverse of encoding: transforms BNN responses into task-relevant formats
- Response matrix v_t in R^(C x tau_out) -> output
- **Count decoding**: spike counts aggregated in spatial regions, normalized against baseline spontaneous activity
- Action with highest relative spike density is executed

#### 4. Feedback (theta_r)
- Special form of encoding designed to drive BNN adaptation
- **Reinforcing (r+)**: structured bursts for favorable outcomes
- **Plasticity-inducing (r-)**: random stimulation to encourage alternative mappings

## Empirical Evaluation

### Task: Goal-Driven Navigation
- Simulated 6x6 gridworld with barrier, food source, and odor gradient
- Agent actions: move forward, turn left, turn right
- Scalar sensor: odor strongest to left (-1), front (0), right/behind (1)
- Three evaluation modes: 30 steps/1 episode, 150 steps/1 episode, 30 steps/5 episodes

### Experimental Setup
- **26 BNN cultures** via Cortical Labs CL1 platform
- Distributed optimization: Optuna HPO server + multiple CL1 clients
- **1,296 parameter combinations** screened
- **4,000+ hours** of real-time agent-environment interactions
- Two-stage screening: Stage 1 (n=1,296 -> n=64), Stage 2 (n=64 -> n=12 top configurations)

### Encoding Parameters Screened

| Parameter | Stage 1 Values | Top (n=12) |
|-----------|---------------|------------|
| Min Frequency (Hz) | 2.0, 3.0, 4.0, 5.0 | 4.0 |
| Max Frequency (Hz) | 40.0, 60.0, 80.0, 100.0 | 40.0, 60.0, 80.0 |
| Amplitude (uA) | 1.0, 2.0, 2.5 | 2.5 |
| Pulse Width (us) | 40.0, 80.0, 160.0 | 40.0, 80.0 |
| Tick Rate (Hz) | 1.0, 2.0, 4.0 | 1.0, 2.0 |
| Ticks per Step | 2, 4, 8 | 4 |

### Key Findings

1. **Maximum frequency is strongest driver**: favors moderate values (40-60 Hz)
2. **Higher amplitude, shorter pulse width, faster interaction rates** support improved performance
3. **BNN agents significantly outperform DQN benchmarks** under equivalent training steps
4. **12 configurations** consistently demonstrated learning across multiple episodes

### SHAP Analysis Results
- Max Frequency: strongest positive impact on top 1% performance
- Amplitude: higher values (2.5 uA) favored
- Pulse Width: shorter (40 us) preferred
- Ticks/Step: moderate (4) optimal
- Tick Rate: lower (1-2 Hz) better
- Min Frequency: moderate (4 Hz) optimal

### Biological Setups Tested
- **Group 1**: 7 cortical/hippocampal cultures in PDMS ring
- **Group 2**: 9 cortical/hippocampal cultures on astrocytes, monolayer
- **Group 3**: 5 cortical-only cultures, monolayer (Stage 2)
- **Group 4**: 5 cortical-only cultures, monolayer (Stage 2)

## Applications

1. **Hybrid bio-silicon computing**: Bridging biological efficiency with silicon programmability
2. **Robotic control**: BNN-driven adaptive decision-making for embodied agents
3. **Neuroscience research**: Understanding biological learning mechanisms through task-driven validation
4. **Energy-efficient computing**: Alternative to von Neumann bottleneck limitations
5. **Benchmarking framework**: Establishing field-wide standards for neurocomputation

## Framework Principles

### Systems Thinking
- Each component is interconnected and highly parameterized
- Adjusting any single part changes the entire system response
- Configuration is a multi-variable optimization problem

### Learning vs Training Distinction
- **Learning**: biological adaptation emerging from intrinsic biophysical plasticity
- **Training**: algorithmic optimization in artificial neural networks
- This distinction emphasizes that biological adaptation is fundamentally different from gradient-based updates

### Hardware Agnosticism
- Framework encapsulates physical interactions within mapping functions
- Applicable to MEA, optogenetic, chemical, or other interfacing modalities

## Key Insights for Practice

1. **Parameter optimization is essential**: Heuristic/ad-hoc stimulation protocols are insufficient for robust BNN computing
2. **Biological stochasticity requires replication**: Identical parameters must be evaluated across multiple cultures simultaneously
3. **Rate encoding with moderate frequencies** (40-60 Hz max) provides the best coupling with BNN biophysics
4. **Feedback design matters**: Structured bursts for reinforcement, random stimulation for plasticity induction
5. **Calibration time**: 4,000+ hours of real-time interaction needed — not trivial

## Comparison to Silicon-Based AI

| Aspect | BNN | Silicon DNN |
|--------|-----|-------------|
| Energy efficiency | Extremely high (mW range) | High (GPU/TPU watts) |
| Continual learning | Intrinsic | Requires specific techniques |
| Non-stationarity | High (adaptive, evolving) | Fixed after training |
| Parameter optimization | Biological (plasticity) | Gradient-based |
| Scalability | Limited by culture setup | Massive scale possible |
| Task performance | Surpasses DQN (this work) | Superior on complex tasks |

## Pitfalls

1. **Biological variability**: Each culture has unique dynamics; parameters optimized for one may not transfer
2. **Parameter space is vast**: 6 encoding parameters x 4-5 values each = 1,296 combinations minimum
3. **Real-time constraint**: Experiments run at biological speed (not accelerated)
4. **Hardware limitations**: MEA platforms are expensive and require specialized expertise
5. **Decoding simplicity**: Current count decoding is rudimentary; more sophisticated methods needed
6. **Feedback design**: Fixed feedback regimen may not be optimal for all parameter configurations

## References

- Cortical Labs CL1 platform: https://corticallabs.com/cloud
- Optuna HPO framework
- Count decoding from Cortical Labs prior work
- Related: Cortical Labs "DishBrain" (Pong-playing neural culture)
