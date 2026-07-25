---
name: real-time-optimal-control-shallow-recurrent-decoder
description: "Real-time optimal control framework using SHallow REcurrent Decoder networks-based Reduced Order Modeling (SHRED-ROM) for high-dimensional and parametric dynamical systems. Enables synthesis of closed-loop controllers from limited state sensor readings with effective distributed control actions in new scenarios."
metadata:
  arxiv_id: "2607.19302"
  published: "2026-07-21"
  authors: ["Matteo Tomasetto", "Francesco Braghin", "J. Nathan Kutz", "Andrea Manzoni"]
  subjects: ["Machine Learning (cs.LG)", "Optimization and Control (math.OC)"]
  tags: [SHRED-ROM, real-time-control, recurrent-decoder, reduced-order-modeling, optimal-control, systems-engineering]
license: Complete terms in LICENSE.txt
---

# Real-time Optimal Control with Shallow Recurrent Decoder Networks

## Overview
This methodology exploits SHallow REcurrent Decoder networks-based Reduced Order Modeling (SHRED-ROM) to synthesize real-time closed-loop controllers for high-dimensional and parametric dynamics, relying solely on limited state sensor readings.

## Core Methodology

### Problem Context
Controlling dynamical systems in real-time across multiple scenarios is critical for adaptive control strategies, ensuring stability and efficiency. Traditional optimal control problems require several system simulations, which are computationally demanding due to high-dimensionality of underlying spatio-temporal dynamics.

### Solution Approach
SHRED-ROM synthesizes real-time closed-loop controllers by:
1. Training on a few optimal examples from an expert demonstrator
2. Mimicking expert behavior with effective distributed control actions in new scenarios
3. Alleviating the curse of dimensionality through reduced-order modeling
4. Synthesizing a sensor forecaster to close the loop at the latent level

### Key Components

1. **Expert Demonstrator Examples**: Limited optimal control examples serve as training data
2. **SHRED-ROM Architecture**: Shallow recurrent decoder networks for reduced-order modeling
3. **Distributed Control Actions**: Effective control distribution across system parameters
4. **Sensor Forecaster**: Mitigates sensor failures or delays by closing the loop at latent level
5. **Latent-Level Control**: Operates in reduced-dimensional latent space for efficiency

## Implementation Workflow

### Step 1: Expert Data Collection
- Gather optimal control examples from expert demonstrator
- Focus on diverse scenarios covering expected operational range
- Include both standard and edge-case operating conditions

### Step 2: SHRED-ROM Training
- Implement shallow recurrent decoder network architecture
- Train model to mimic expert behavior from limited examples
- Validate generalization to unseen scenarios

### Step 3: Sensor Forecaster Synthesis
- Develop forecaster to predict sensor readings at latent level
- Integrate forecaster into control loop for robustness
- Test under various sensor failure/delay conditions

### Step 4: Real-time Deployment
- Deploy trained SHRED-ROM controller for real-time operation
- Monitor performance across different scenarios
- Implement fallback mechanisms for extreme conditions

### Step 5: Performance Assessment
- Evaluate on challenging high-dimensional cases
- Test parametric density control scenarios
- Validate fluid flow control performance
- Compare computational efficiency vs. traditional approaches

## Applications

- **Parametric Density Control**: Adaptive control for systems with varying density parameters
- **Fluid Flow Control**: Real-time optimization of complex fluid dynamics
- **High-dimensional Systems**: Control of systems with many degrees of freedom
- **Limited Sensor Scenarios**: Operation with minimal sensor infrastructure
- **Real-time Adaptive Control**: Rapid response to changing system conditions

## Pitfalls and Considerations

### Training Data Limitations
- Quality and diversity of expert examples directly impact generalization
- Insufficient coverage of operational scenarios leads to poor performance

### Model Architecture Design
- Balance between model depth and real-time computational requirements
- Shallow architecture must capture essential dynamics without overfitting

### Sensor Integration
- Sensor forecaster effectiveness depends on available sensor modalities
- Latent-level control requires careful design of observation mapping

### Validation Complexity
- High-dimensional test cases require significant computational resources
- Multiple scenario validation is essential for robustness assessment

## Activation Keywords
- SHRED-ROM
- shallow recurrent decoder
- real-time optimal control
- reduced order modeling
- latent-level control
- sensor forecaster
- distributed control actions
- systems engineering control

## References
- Original Paper: arXiv:2607.19302 [cs.LG, math.OC]
- Related Work: Reduced-order modeling for control systems
- Implementation: SHallow REcurrent Decoder networks architecture