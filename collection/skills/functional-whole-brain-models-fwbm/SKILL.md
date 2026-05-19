---
name: functional-whole-brain-models-fwbm
description: >
  Functional Whole-Brain Models (fWBMs) — a unified modeling paradigm
  integrating structural/dynamical realism with task-performing capacity.
  Bridges bottom-up whole-brain modeling and top-down neuroconnectionism.
  Four criteria: structural grounding, continuous-time dynamics, functional
  competence, mappable observables to neuroimaging/EEG/behavioral data.
  Use when designing brain models needing both biological grounding and
  cognitive competence, building connectome-grounded neural networks,
  or evaluating multi-scale brain simulation frameworks.
  Activation: functional whole-brain model, fWBM, whole-brain modeling,
  neuroconnectionism, brain structure function integration,
  connectome-grounded model, cognitive brain model, biophysically realistic
---

# Functional Whole-Brain Models (fWBMs)

Unified framework integrating biophysical realism with cognitive task performance.

## Core Problem

Two disconnected traditions in computational neuroscience:
- **Bottom-up WBM**: biophysically detailed simulations of brain structure/dynamics — lacks functional competence
- **Top-down Neuroconnectionism**: deep neural networks optimized for task performance — limited biological grounding

fWBMs unify both by requiring four minimal criteria.

## Four Defining Criteria

1. **Structural Grounding**: Empirical connectomes + regional biology as architectural prior
2. **Continuous-Time Dynamical Realism**: Realistic temporal dynamics, not discrete forward passes
3. **Functional Competence**: Task-performing capacity across cognitive domains
4. **Mappable Observables**: Outputs mappable to neuroimaging (fMRI), electrophysiology (EEG/MEG), and behavioral data

## Three-Pillar Roadmap

### Short-Term
- Integrate existing WBM dynamics with task-oriented objectives
- Develop mapping functions from model states to empirical observables
- Validate against multi-modal datasets simultaneously

### Mid-Term
- Build cross-scale models linking micro-circuitry to whole-brain dynamics
- Incorporate regional transcriptomic and cytoarchitectonic data
- Establish common benchmarks for biological × functional evaluation

### Long-Term
- Achieve unified models that predict both brain activity patterns and behavioral outcomes
- Enable clinical applications (virtual patients, treatment simulation)
- Develop common language across computational neuroscience subfields

## Implementation Patterns

### Architecture Design
```
Connectome (structural prior) + Regional dynamics (biological constraints)
→ Task-optimized readout layers → Observable mapping (fMRI/EEG/behavior)
```

### Validation Pipeline
1. Train model on cognitive task with connectome-constrained architecture
2. Map internal states to fMRI/EEG via learned or analytical forward models
3. Compare mapped predictions against empirical data
4. Iterate: adjust biological constraints vs. task performance tradeoff

### Key Tradeoffs
- More biological detail → less flexibility for task optimization
- More task optimization → potentially less biological plausibility
- fWBMs seek Pareto-optimal points on this frontier

## Scientific Opportunities

- **Mechanistic understanding**: What circuit properties enable specific cognitive functions?
- **Clinical translation**: Virtual patient models for neuropsychiatric disorders
- **Cross-scale hypotheses**: Link molecular/cellular changes to behavioral phenotypes
- **Common language**: Bridge subfields that currently use incompatible frameworks

## Activation Keywords
- functional whole-brain model
- fWBM
- whole-brain modeling
- neuroconnectionism
- brain structure-function integration
- connectome-grounded neural network
- biophysically realistic task model
- multi-scale brain simulation
- cognitive brain model
- brain modeling paradigm

## Related Skills
- brain-digital-twins-execution-semantics-v3
- computational-neuroscience-in-llm-era
- neural-code-dynamics-analysis
