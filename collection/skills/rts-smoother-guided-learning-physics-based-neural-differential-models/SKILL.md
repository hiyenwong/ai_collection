# rts-smoother-guided-learning-physics-based-neural-differential-models

## Paper Information
- **Title**: RTS Smoother-Guided Learning of Physics-Based Neural Differential Models
- **Authors**: Ahmet Demirkaya, Georgios Stratis, Tales Imbiriba, Zachary D. Danziger, Deniz Erdogmus
- **arXiv ID**: 2607.15180
- **URL**: http://arxiv.org/abs/2607.15180
- **Subjects**: Machine Learning (cs.LG); Systems and Control (eess.SY)
- **Abstract**: Ordinary differential equations (ODEs) are widely used to model dynamical systems in physics, biology, neuroscience, and physiology, but in many applications some equations of the dynamics are unknown and only a subset of the state variables are measured. We propose a hybrid neural--physics framework in which the known components of the ODE are kept explicit and the missing components are represented by a neural network. The proposed method consists of two stages where we alternate between state and parameter estimation and iterate until a predetermined criterion is met. Specifically, in the first step, we treat the model parameters as being known and we infer the latent states from the available measurements using a Rauch--Tung--Striebel (RTS) smoother. In the second stage, we treat the smoothed trajectories as being known and use them to estimate the neural networks' parameters through backpropagation. We evaluate the method on benchmark systems spanning linear, nonlinear, and stiff dynamics under partial state observation. Across these settings, the proposed method learns missing ODE components from incomplete measurements while exploiting and retaining interpretable mechanistic structure and improving latent-state reconstruction and long-horizon prediction.

## Skill Description
This skill is generated from the arXiv paper 2607.15180: RTS Smoother-Guided Learning of Physics-Based Neural Differential Models.
It encapsulates the RTS Smoother-Guided Learning methodology for physics-based neural differential models, particularly relevant for neuroscience applications where partial observations of neural dynamics are common.

## Core Methodology

### Two-Stage Alternating Optimization
1. **State Estimation Step**: Treat model parameters as known, infer latent states from measurements using Rauch-Tung-Striebel (RTS) smoother
2. **Parameter Estimation Step**: Treat smoothed trajectories as known, estimate neural network parameters via backpropagation
3. **Iteration**: Alternate between steps until convergence criterion is met

### Key Advantages
- Learns missing ODE components from incomplete measurements
- Retains interpretable mechanistic structure
- Improves latent-state reconstruction
- Enhances long-horizon prediction capabilities
- Handles linear, nonlinear, and stiff dynamics under partial observation

## Application to Neuroscience
This method is particularly applicable to neuroscience where:
- Neural dynamics can be modeled as ODEs with known biophysical components
- Only partial neural activity is observable (e.g., via calcium imaging, EEG)
- Unknown components (e.g., synaptic dynamics, neuromodulatory effects) can be learned
- Preserves interpretability of known neuroscience mechanisms

## Activation Keywords
rts smoother, neural differential models, physics-informed neural networks, PINNs, system identification, neuroscience modeling, latent state estimation, 2607.15180

## References
- arXiv:2607.15180 - RTS Smoother-Guided Learning of Physics-Based Neural Differential Models