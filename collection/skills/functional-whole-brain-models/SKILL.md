---
name: functional-whole-brain-models
description: "Functional Whole-Brain Models (fWBMs) methodology — unifying bottom-up whole-brain modeling (biophysically detailed simulations) with top-down neuroconnectionism (task-performing DNNs). Four minimal criteria: structural grounding in empirical connectomes, continuous-time dynamical realism, functional competence across cognitive domains, mappable observables to neuroimaging/electrophysiology/behavior. Use when: designing whole-brain computational models, integrating structural and functional brain modeling, neuroconnectionist frameworks, biophysically grounded deep learning, brain simulation with task performance."
---

# Functional Whole-Brain Models (fWBMs)

## Core Problem

Two disconnected traditions in computational neuroscience:
- **Bottom-up WBM**: biophysically detailed brain simulations lacking functional competence
- **Top-down neuroconnectionism**: task-performing DNNs with limited biological grounding

## fWBM Definition (Four Minimal Criteria)

1. **Structural grounding**: empirical connectomes + regional biology
2. **Continuous-time dynamical realism**: realistic neural dynamics
3. **Functional competence**: performance across cognitive domains
4. **Mappable observables**: correspondence to neuroimaging, electrophysiology, and behavioral data

## Three-Pillar Roadmap

- **Short-term**: Integrate existing WBM and neuroconnectionist components
- **Mid-term**: Develop unified architectures with shared representational formats
- **Long-term**: Full multi-scale models from molecular dynamics to cognitive behavior

## Application Patterns

```python
class FunctionalWholeBrainModel:
    """fWBM combining structural realism with task competence."""
    def __init__(self, connectome, regional_properties):
        self.connectome = connectome  # Empirical structural connectivity
        self.regions = regional_properties  # Regional biology
        
    def simulate(self, task_stimulus):
        # Continuous-time dynamics on structural scaffold
        # Task-performing output
        # Observable mapping to fMRI/EEG/behavior
        pass
```

## When to Apply

- Bridging biophysical brain models and task-performing neural networks
- Designing models with both biological realism and functional competence
- Clinical applications requiring both structural and functional accuracy
- Cross-scale hypothesis generation in computational neuroscience
