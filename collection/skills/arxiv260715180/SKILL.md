# arxiv260715180

## Paper: RTS Smoother-Guided Learning of Physics-Based Neural Differential Models
- Authors: Ahmet Demirkaya, Georgios Stratis, Tales Imbiriba, Zachary D. Danziger, Deniz Erdogmus
- arXiv: 2607.15180v1
- Abstract: Ordinary differential equations (ODEs) are widely used to model dynamical systems in physics, biology, neuroscience, and physiology, but in many applications some equations of the dynamics are unknown and only a subset of the state variables are measured. We propose a hybrid neural--physics framework in which the known components of the ODE are kept explicit and the missing components are represented by a neural network. The proposed method consists of two stages where we alternate between state and parameter estimation and iterate until a predetermined criterion is met. Specifically, in the first step, we treat the model parameters as being known and we infer the latent states from the available measurements using a Rauch--Tung--Striebel (RTS) smoother. In the second stage, we treat the smoothed trajectories as being known and use them to estimate the neural networks' parameters through backpropagation. We evaluate the method on benchmark systems spanning linear, nonlinear, and stiff dynamics under partial state observation. Across these settings, the proposed method learns missing ODE components from incomplete measurements while exploiting and retaining interpretable mechanistic structure and improving latent-state reconstruction and long-horizon prediction.

## Methodology
This skill implements the RTS Smoother-Guided Learning approach for physics-based neural differential models. The method combines traditional state estimation techniques (RTS smoother) with neural network parameter estimation to learn unknown components of dynamical systems from partial measurements.

## Core Idea
The core idea is to decompose a dynamical system into known physics-based components and unknown components that are modeled by neural networks. By alternating between state estimation (using RTS smoother when parameters are known) and parameter estimation (using backpropagation when states are known), the method can learn the unknown neural network components while preserving the interpretability of the known physics-based components.

## Application Steps
1. **Model Decomposition**: Identify known components of the ODE that can be kept explicit and unknown components to be represented by neural networks
2. **State Estimation Phase**: Treat network parameters as fixed and use RTS smoother to estimate latent states from measurements
3. **Parameter Estimation Phase**: Treat smoothed trajectories as known and use backpropagation to update neural network parameters
4. **Iteration**: Alternate between steps 2 and 3 until convergence criteria are met
5. **Validation**: Evaluate on benchmark systems to verify learning of missing ODE components while retaining mechanistic interpretability

## References
- [arXiv:2607.15180] RTS Smoother-Guided Learning of Physics-Based Neural Differential Models

## Activation Keywords
260715180, neural differential equations, RTS smoother, physics-informed neural networks, system identification