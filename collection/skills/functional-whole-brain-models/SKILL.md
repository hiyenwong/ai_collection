---
name: functional-whole-brain-models
description: >
  Functional Whole-Brain Models (fWBMs) methodology — a unified modeling paradigm
  integrating structural and dynamical realism with task-performing capacity. Bridges
  bottom-up whole-brain modeling (WBM) and top-down neuroconnectionism. Defines four
  minimal criteria for fWBMs and establishes a three-pillar roadmap. Use when designing,
  evaluating, or reviewing whole-brain models, neuroconnectionist architectures,
  biologically-grounded neural networks, or cross-scale brain simulation frameworks.
  Activation: functional whole-brain model, fWBM, whole-brain modeling, neuroconnectionism,
  brain structure function integration, biologically realistic neural network.
---

# Functional Whole-Brain Models (fWBMs)

Unified framework for integrating bottom-up whole-brain modeling with top-down
neuroconnectionist approaches.

## Paper Reference

- **Title**: Functional Whole-Brain Models: A New Framework for Unifying Brain Structure and Cognitive Function
- **Authors**: Mario Senden, Leonardo Dalla Porta, Jan Fousek, Jorge F. Mejias, Gorka Zamora-López
- **arXiv**: 2605.18118 (May 18, 2026)
- **Category**: q-bio.NC

## The Problem: A Divided Field

Computational neuroscience features two largely independent traditions:

1. **Bottom-up (WBM)**: Biophysically detailed simulations from structural connectomes.
   - Reproduce neural activation profiles across scales.
   - **Limitation**: No functional competence — cannot perform meaningful behavior.

2. **Top-down (Neuroconnectionism)**: Deep neural networks optimized for task performance.
   - Accurately predict neural activity during cognition.
   - **Limitation**: Limited biological grounding — architecture doesn't reflect biology.

Result: Models of the brain's machinery AND models of the mind's abilities, but no
principled bridge between them.

## Four Minimal Criteria for fWBMs

An fWBM must satisfy ALL four criteria:

### 1. Structural Grounding
- Empirical connectome-based architecture (DWI-derived structural connectivity)
- Regional biological constraints (cell-type composition, receptor density, gene expression)
- Multi-scale anatomical data integration

### 2. Continuous-Time Dynamical Realism
- Ordinary/stochastic differential equations for neural dynamics
- Biophysically plausible node models (not artificial neuron abstractions)
- Gradient flow through differential equations or discrete spiking events

### 3. Functional Competence
- Task-performing capacity across cognitive domains
- Trained on ecologically valid stimuli (natural language, sensory input)
- Behavioral output matching human/animal performance

### 4. Mappable Observables
- Simulated outputs mappable to neuroimaging (fMRI, EEG, MEG)
- Electrophysiological signal correspondence (LFP, spikes)
- Behavioral data alignment

## Three-Pillar Roadmap

### Short-term Pillar: Methodological Integration
- Differentiable WBM frameworks (gradients through ODEs/SDEs)
- Surrogate gradient methods for spiking dynamics
- Multi-scale parameter optimization connecting cellular to systems level

### Mid-term Pillar: Empirical Validation
- Cross-modal validation (fMRI + EEG + behavior)
- Lesion studies: compare model damage to clinical deficits
- Individual-specific models using personalized connectomes

### Long-term Pillar: Clinical Translation
- Digital twin frameworks for neurological disorders
- Predictive modeling of intervention outcomes
- Biomarker discovery through model-based hypothesis testing

## Key Technical Patterns

### Pattern 1: Differentiable Whole-Brain Simulation
```python
# Pseudocode for differentiable WBM training
class DifferentiableWBM(nn.Module):
    def __init__(self, connectome, regional_params):
        self.SC = connectome  # Structural connectivity matrix
        self.params = regional_params
    
    def forward(self, initial_state, stimulus, dt):
        # Neural mass model ODE with gradients flowing through
        state = initial_state
        for t in range(T):
            dstate = neural_mass_dynamics(state, self.SC, stimulus[t], self.params)
            state = state + dt * dstate  # Euler integration, differentiable
        return state
```

### Pattern 2: Multi-Scale Integration
- **Macro scale**: Whole-brain connectome (parcellation nodes + SC edges)
- **Meso scale**: Regional microcircuit models (E/I balance, cell-type diversity)
- **Micro scale**: Biophysical constraints (ion channels, receptor distributions)

### Pattern 3: Cross-Modal Prediction
- fMRI: Hemodynamic response function applied to simulated activity
- EEG/MEG: Forward model from source activity to sensor space
- Behavior: Readout layers mapping neural states to task outputs

## Evaluation Criteria

When evaluating an fWBM:

1. **Biological fidelity**: Does architecture match known anatomy?
2. **Dynamical validity**: Do simulated dynamics reproduce empirical spectra?
3. **Task performance**: Does the model solve cognitive tasks?
4. **Cross-scale alignment**: Do predictions match data at multiple scales?
5. **Perturbation robustness**: Does simulated damage match clinical patterns?

## Relation to Existing Skills

- **brain-dit-fmri-foundation-model**: fMRI foundation models (complementary approach)
- **spiking-neural-network-analysis**: SNN analysis (potential node models)
- **brain-network-controllability**: Network control theory (structural connectivity)
- **geometric-brain-dynamics-mapping**: Geometric brain mapping (spatial constraints)

## Common Pitfalls

- **Over-parcellation**: Too many regions → parameter explosion, overfitting
- **Under-constrained optimization**: Too many free parameters → non-unique solutions
- **Scale mismatch**: Mixing macro and micro scales without proper bridging
- **Validation circularity**: Using same data for training and validation
- **Ignoring individual variability**: Group-averaged connectomes mask important differences
