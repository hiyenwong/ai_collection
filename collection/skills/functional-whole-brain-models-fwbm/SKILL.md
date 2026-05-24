---
name: functional-whole-brain-models-fwbm
description: "Functional Whole-Brain Models (fWBMs): A unified modeling paradigm integrating structural/dynamical realism (bottom-up WBM) with task-performing capacity (top-down neuroconnectionism). Use when studying brain structure-function integration, building biophysically constrained neural networks that perform cognitive tasks, or connecting connectome data with functional competence."
arxiv_id: "2605.18118"
date: "2026-05-18"
authors: "Mario Senden, Leonardo Dalla Porta, Jan Fousek, Jorge F. Mejias, Gorka Zamora-Lopez"
tags: [whole-brain-modeling, neuroconnectionism, computational-neuroscience, brain-connectome, structure-function-integration, fWBM]
---

# Functional Whole-Brain Models (fWBMs)

## Overview
Proposes **functional Whole-Brain Models (fWBMs)** as a unified modeling paradigm that bridges the gap between:
- **Bottom-up WBM**: Biophysically detailed simulations of brain structure and dynamics (biologically realistic but functionally passive)
- **Top-down neuroconnectionism**: Deep neural networks optimized for functional performance (functionally competent but biologically weak)

## The Four Minimal Criteria for fWBMs

1. **Structural grounding** - Grounded in empirical connectomes and regional biology (tractography, cytoarchitecture)
2. **Continuous-time dynamical realism** - Built on ODE/SDE-based neural dynamics, not discrete feedforward activations
3. **Functional competence** - Must perform cognitive/behavioral tasks (working memory, vision, language)
4. **Mappable observables** - Model outputs must map to neuroimaging (fMRI, EEG), electrophysiological, and behavioral data

## Three-Pillar Roadmap

### Short-term: Multisimulator Data Pipelines
- Shared data formats and protocols across simulation/optimization platforms (TheVirtualBrain, NEST, Brian2)
- Direct gradient propagation through biophysically detailed dynamics via ODE/SDE adjoint methods

### Mid-term: (f)WBM Blueprint Language
- Formal specification language for model architecture, connectome constraints, dynamics equations
- Standardized evaluation benchmarks across structural/functional/metric/competence dimensions

### Long-term: Community-Shared (f)WBM Ecosystem
- Open model zoo with standardized benchmarks
- Collaborative infrastructure for model sharing, comparison, and iteration
- Integration with brain initiative data platforms

## Key Applications

- **Connectome-constrained learning** (Damicelli et al., 2022): Replace random reservoir connectivity with empirical connectomes
- **Biophysics-informed deep learning** (de Leeuw et al., 2024): Task-train cortical column mean-field models via gradient descent
- **Oscillatory recurrent networks** (Effenberger et al., 2024): Harmonic oscillators as recurrent units for wave-based computation
- **Cortico-cerebellar modular RNNs**: Biological architecture as inductive bias for task-optimized learning

## Significance

fWBMs offer a path to:
- Scientifically valid models that explain **how** biological structure gives rise to cognitive function
- Clinically useful models for predicting brain disorder effects on behavior
- A common language between WBM and neuroconnectionist communities

## Activation Keywords
functional whole-brain model, fWBM, whole-brain modeling, neuroconnectionism, connectome-constrained neural network, biophysics-informed deep learning, brain structure-function integration
