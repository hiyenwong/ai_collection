---
name: functional-whole-brain-models
description: >
  Functional Whole-Brain Models (FWBM) methodology bridging bottom-up whole-brain modeling
  and top-down neuroconnectionism. Combines biophysically detailed simulations with
  functional-performance-driven deep neural networks. Use when: designing brain-scale
  computational models, integrating structure and function in neural modeling, building
  neuroconnectionist models with biological grounding, developing hybrid brain models
  that achieve both biological fidelity and functional competence.
  Activation: whole-brain modeling, neuroconnectionism, functional brain model, brain
  simulation, WBM, FWBM, biophysically detailed brain, brain DNN integration, brain
  foundation model, brain dynamics modeling.
  Based on arXiv:2605.18118 (May 2026).
---

# Functional Whole-Brain Models (FWBM)

## Core Concept

Proposes a new paradigm that bridges two prominent computational neuroscience traditions:

- **Bottom-up Whole-Brain Modeling (WBM)**: Biophysically detailed simulations of brain structure and dynamics. Achieves biological fidelity but lacks functional competence.
- **Top-down Neuroconnectionism**: Deep neural networks optimized for functional performance. Achieves task competence but limited biological grounding.

**FWBM** unifies both by incorporating anatomical constraints and biophysical realism into architectures that are also trained for functional competence.

## Key Contributions (arXiv:2605.18118)

1. **Hybrid Architecture**: Combines structural connectivity matrices (from DWI/tractography) with deep learning architectures that can be trained end-to-end on cognitive tasks.
2. **Biological Constraints as Regularizers**: Uses empirical brain data (fMRI, MEG, DWI) as architectural and training constraints rather than mere validation targets.
3. **Multi-scale Integration**: Bridges micro-scale (neuron-level dynamics) with macro-scale (region-level functional connectivity) through hierarchical modeling.
4. **Functional Validation**: Models must simultaneously reproduce neural activity patterns AND achieve behavioral task performance.

## Methodology Framework

### Step 1: Structural Foundation
- Load individual or template structural connectome (SC matrix)
- Define regional parcellation (e.g., Schaefer, AAL, HCP-MMP)
- Map SC to network connectivity weights

### Step 2: Biophysical Embedding
- Incorporate neural mass models or mean-field approximations at each node
- Use empirical delays from tractography-derived fiber lengths
- Set coupling strengths based on empirical SC weights

### Step 3: Functional Training
- Define target tasks (cognitive, perceptual, motor)
- Train with task loss + biological regularization loss
- Biological loss terms: FC matching, spectral matching, dynamic FC matching

### Step 4: Validation
- Compare simulated FC to empirical FC
- Compare temporal dynamics (power spectra, metastability)
- Evaluate behavioral task performance

## Implementation Patterns

```python
# Conceptual framework
class FunctionalWholeBrainModel:
    def __init__(self, sc_matrix, regions, delays):
        self.sc = sc_matrix  # structural connectivity
        self.regions = regions  # parcellation
        self.delays = delays  # conduction delays
        
    def forward(self, input_signal, params):
        # Biophysical dynamics at each node
        # Coupled through structural connectivity
        # Differentiable for gradient-based training
        pass
    
    def loss(self, predictions, targets, empirical_data):
        task_loss = compute_task_loss(predictions, targets)
        bio_loss = compute_biological_loss(predictions, empirical_data)
        return task_loss + lambda_ * bio_loss
```

## Activation Keywords

- whole-brain modeling
- neuroconnectionism
- functional brain model
- brain simulation
- brain DNN
- biophysical brain model
- structure-function coupling
- brain foundation model
- computational brain modeling
- neural mass modeling

## Related Skills

- brain-dit-fmri-foundation-model
- neural-dynamics-universal-translator
- brain-inspired-snn-pattern-analysis
- computational-neuroscience-in-llm-era

## References

- Paper: arXiv:2605.18118 (May 2026)
- Related: The Virtual Brain platform, Dynamic Causal Modeling, Neural Mass Models
